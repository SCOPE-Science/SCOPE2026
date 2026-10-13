#!/usr/bin/env python3
"""Independent finite-field checks for the idempotent-derivation rank formulas.

Only the Python standard library is required. The direct enumeration tests the
matrix-unit Leibniz condition through the inner commutator construction and
checks composition-idempotence on all matrix units. GF(4) is represented by
F_2[t]/(t^2+t+1). No finite enumeration proves the unrestricted theorem.
"""
from itertools import product
from collections import Counter
from math import prod


def field(q):
    if q in (2, 3):
        return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q
    if q == 4:
        def mul(a,b):
            out = 0
            for i in range(2):
                if (a>>i)&1:
                    for j in range(2):
                        if (b>>j)&1:
                            out ^= 1<<(i+j)
            if out & 8:
                out ^= 8|4|2  # t^3=t^2+t in the quotient
            if out & 4:
                out ^= 4|2|1  # t^2=t+1
            return out
        return lambda a,b:a^b, mul
    raise ValueError(q)


def mm(A,B,n,add,mul):
    out=[0]*(n*n)
    for i in range(n):
        for k in range(n):
            a=A[i*n+k]
            if a:
                for j in range(n):
                    out[i*n+j]=add(out[i*n+j],mul(a,B[k*n+j]))
    return tuple(out)


def plus(A,B,add):
    return tuple(add(a,b) for a,b in zip(A,B))


def elementary(n,i,j):
    a=[0]*(n*n)
    a[i*n+j]=1
    return tuple(a)


def comm(A,X,n,add,mul,q):
    AX=mm(A,X,n,add,mul)
    XA=mm(X,A,n,add,mul)
    if q%2==0:
        return plus(AX,XA,add)
    return tuple((a-b)%q for a,b in zip(AX,XA))


def gauss_rank(rows,q,add,mul):
    M=[list(row) for row in rows]
    if not M: return 0
    m,n=len(M),len(M[0]); r=0
    for c in range(n):
        p=next((k for k in range(r,m) if M[k][c]),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        inv=next(x for x in range(1,q) if mul(x,M[r][c])==1)
        M[r]=[mul(inv,x) for x in M[r]]
        for k in range(m):
            if k!=r and M[k][c]:
                a=M[k][c]
                if q%2==0:
                    M[k]=[add(x,mul(a,y)) for x,y in zip(M[k],M[r])]
                else:
                    M[k]=[(x-mul(a,y))%q for x,y in zip(M[k],M[r])]
        r+=1
        if r==m: break
    return r


def gl(n,q):
    return prod(q**n-q**i for i in range(n))


def gaussian(n,r,q):
    if r<0 or r>n: return 0
    return prod(q**(n-i)-1 for i in range(r))//prod(q**(r-i)-1 for i in range(r))


def predicted(n,q):
    if q%2: return Counter({0:1})
    p=Counter({0:1})
    for r in range(1,n//2+1):
        number=gaussian(n,r,q)*q**(r*(n-r))
        if 2*r==n: number//=2
        p[2*r*(n-r)]+=number
    if n%2==0:
        p[n*n//2]+=gl(n,q)//(2*gl(n//2,q*q))
    return p


def enumerate_case(n,q):
    add,mul=field(q)
    idn=tuple(int(i==j) for i in range(n) for j in range(n))
    units=[elementary(n,i,j) for i in range(n) for j in range(n)]
    # A and A+scalar I produce the same map; set the (0,0)-entry to zero.
    seen=set()
    tally=Counter()
    candidate_matrices=0
    for a in product(range(q),repeat=n*n):
        sq=mm(a,a,n,add,mul)
        ma=plus(sq,a,add) if q%2==0 else tuple((x+y)%q for x,y in zip(sq,a))
        c=ma[0]
        if q%2==0 and any(ma[i*n+j] != (c if i==j else 0) for i in range(n) for j in range(n)):
            # In characteristic two the polynomial test is equivalent.
            continue
        candidate_matrices+=1
        base=a[0]
        representative=tuple(add(a[i*n+j],base if i==j else 0) if q%2==0
                             else (a[i*n+j]-base*(i==j))%q
                             for i in range(n) for j in range(n))
        if representative in seen: continue
        seen.add(representative)
        images=[comm(representative,E,n,add,mul,q) for E in units]
        if not all(comm(representative,Z,n,add,mul,q)==Z for Z in images):
            # Direct composition test, without relying on the theorem.
            seen.remove(representative)
            continue
        rank=gauss_rank(images,q,add,mul)
        tally[rank]+=1
    wanted=predicted(n,q)
    assert tally==wanted,(n,q,tally,wanted,candidate_matrices)
    print('PASS n=%d q=%d: '%(n,q),dict(sorted(tally.items())),
          'unique=',sum(tally.values()),'matrix_candidates=',candidate_matrices)


if __name__=='__main__':
    assert field(4)[1](2,2)==3
    assert field(4)[1](2,3)==1
    for n,q in [(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)]:
        enumerate_case(n,q)
    print('VERIFY_OK')
