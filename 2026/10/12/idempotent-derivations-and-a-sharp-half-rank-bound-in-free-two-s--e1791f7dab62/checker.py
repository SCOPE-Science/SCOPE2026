#!/usr/bin/env python3
"""Finite-field validation of idempotent derivations of the cubic-truncated free associative algebra.

Uses only the Python standard library. Exhaustively enumerates every linear component
A on two generators over GF(2), GF(3), GF(4), GF(5), computes the degree-two
Leibniz action, and solves the idempotency equations for every quadratic lift.
Also brute-forces every quadratic lift over GF(2). It does not prove the
arbitrary-rank theorem; the proof is symbolic and independent of this script.
"""
from itertools import product
from collections import Counter

def add(a,b,q):
    return a^b if q==4 else (a+b)%q

def neg(a,q):
    return a if q in (2,4) else (-a)%q

def mul(a,b,q):
    if q!=4:return a*b%q
    z=0
    while b:
        if b&1:z^=a
        b>>=1
        a<<=1
        if a&4:a^=7  # GF(4)=F2[x]/(x^2+x+1)
    return z

def inv(a,q):
    assert a
    return next(b for b in range(1,q) if mul(a,b,q)==1)

def rank(rows,q):
    if not rows:return 0
    M=[r[:] for r in rows];m=len(M);n=len(M[0]);r=0
    for col in range(n):
        lead=next((i for i in range(r,m) if M[i][col]),None)
        if lead is None:continue
        M[r],M[lead]=M[lead],M[r]
        t=inv(M[r][col],q)
        M[r]=[mul(x,t,q) for x in M[r]]
        for i in range(m):
            if i==r or not M[i][col]:continue
            t=M[i][col]
            M[i]=[add(x,neg(mul(t,y,q),q),q) for x,y in zip(M[i],M[r])]
        r+=1
    return r

def mm(A,B,q):
    return [[sum_field((mul(A[i][k],B[k][j],q) for k in range(len(B))),q)
             for j in range(len(B[0]))] for i in range(len(A))]

def sum_field(seq,q):
    x=0
    for v in seq:x=add(x,v,q)
    return x

def bw(A,q):
    n=len(A);B=[[0]*(n*n) for _ in range(n*n)]
    for i in range(n):
        for j in range(n):
            for h in range(n):
                for k in range(n):
                    B[i*n+j][h*n+k]=add(mul(A[i][h], int(j==k), q),
                                             mul(int(i==h), A[j][k],q),q)
    return B

def predicted(n,q):
    if q in (3,5):return {0:1}
    out=Counter()
    for r in range(n+1):
        s=n-r
        num=1;den=1
        for i in range(r):num*=q**(n-i)-1;den*=q**(r-i)-1
        gauss=num//den
        out[r+2*r*s]+=gauss*q**(r*s+r**3+3*r*s*s)
    return dict(out)

def exact_via_linear_equations(n,q):
    L=n*n; tally=Counter()
    for flat in product(range(q),repeat=L):
        A=[list(flat[i*n:(i+1)*n]) for i in range(n)]
        if mm(A,A,q)!=A:continue
        B=bw(A,q)
        if mm(B,B,q)!=B:continue
        # Linear map F -> BF+FA-F on quadratic lifts F: K^n -> K^(n*n)
        constraints=[]
        for basis in range(L*n):
            F=[[0]*n for _ in range(L)]
            F[basis//n][basis%n]=1
            BF=mm(B,F,q);FA=mm(F,A,q)
            constraints.append([add(add(BF[i][j],FA[i][j],q),neg(F[i][j],q),q)
                                for i in range(L) for j in range(n)])
        M=[[constraints[col][row] for col in range(L*n)] for row in range(L*n)]
        dim=L*n-rank(M,q)
        r=rank(A,q)+rank(B,q)
        tally[r]+=q**dim
    return dict(tally)

def full_brute_2_2():
    n=2;q=2;L=n*n;tally=Counter();checks=0
    for a in product(range(q),repeat=L):
        A=[list(a[i*n:(i+1)*n]) for i in range(n)]
        B=bw(A,q)
        for f in product(range(q),repeat=L*n):
            F=[list(f[i*n:(i+1)*n]) for i in range(L)]
            M=[A[i]+[0]*L for i in range(n)]+[F[i]+B[i] for i in range(L)]
            if mm(M,M,q)!=M:continue
            # Confirm Leibniz directly on all basis pairs, not just on generators.
            def prod(x,y):
                z=[0]*(n+L)
                for i in range(n):
                    for j in range(n):
                        z[n+i*n+j]=mul(x[i],y[j],q)
                return z
            for i in range(n+L):
                for j in range(n+L):
                    e=[int(k==i) for k in range(n+L)]
                    h=[int(k==j) for k in range(n+L)]
                    de=[M[k][i] for k in range(n+L)]
                    dh=[M[k][j] for k in range(n+L)]
                    lhs=mm(M,[[z] for z in prod(e,h)],q)
                    rhs=[add(x,y,q) for x,y in zip(prod(de,h),prod(e,dh))]
                    assert [x[0] for x in lhs]==rhs
            tally[rank(M,q)]+=1
            checks+=1
    assert checks==353
    return dict(tally)

def main():
    for n,q in [(1,2),(1,3),(1,4),(1,5),(2,2),(2,3),(2,4),(2,5),(3,2)]:
        got=exact_via_linear_equations(n,q)
        want=predicted(n,q)
        assert got==want,(n,q,got,want)
        print('n,q=',n,q,'rank_census=',got)
    brute=full_brute_2_2()
    assert brute==predicted(2,2)
    print('DIRECT_GF2_TWO_GENERATOR_CHECK',brute)
    print('VERIFY_OK')
if __name__=='__main__':main()
