#!/usr/bin/env python3
"""Independent exact checks for involutive anti-automorphisms of V + (V tensor V).
Run: python3 verify.py. Python standard library only.
"""
from collections import Counter
from itertools import product


def operations(q):
    if q == 4:
        # F_4 = F_2[t]/(t^2+t+1), encoded by 0, 1, t, 1+t.
        table = ((0,0,0,0), (0,1,2,3), (0,2,3,1), (0,3,1,2))
        return lambda a,b:a^b, lambda a,b:table[a][b], lambda a:a
    return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q, lambda a:(-a)%q


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matmul(A,B,q):
    add,mul,_=operations(q)
    return [[sum_field((mul(A[i][k],B[k][j]) for k in range(len(B))),add)
             for j in range(len(B[0]))] for i in range(len(A))]


def sum_field(seq,add):
    s=0
    for x in seq:s=add(s,x)
    return s


def rank(A,q):
    add,mul,neg=operations(q)
    A=[row[:] for row in A]
    rows,cols=len(A),len(A[0]) if A else 0
    r=0
    for col in range(cols):
        pivot=next((i for i in range(r,rows) if A[i][col]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=next(x for x in range(1,q) if mul(x,A[r][col])==1)
        A[r]=[mul(inv,x) for x in A[r]]
        for i in range(r+1,rows):
            if A[i][col]:
                z=neg(A[i][col])
                A[i]=[add(v,mul(z,w)) for v,w in zip(A[i],A[r])]
        r+=1
        if r==rows:break
    return r


def involutive_linear_parts(n,q):
    for values in product(range(q),repeat=n*n):
        L=[list(values[i*n:(i+1)*n]) for i in range(n)]
        if matmul(L,L,q)==eye(n):yield L


def anti_matrix(n,q,L,H):
    # Basis x_i then x_i*x_j. Product of two linear basis elements is their
    # corresponding quadratic basis element; all products involving degree 2 vanish.
    N=n+n*n
    _,mul,_=operations(q)
    S=[[0]*N for _ in range(N)]
    for i in range(n):
        for a in range(n):S[a][i]=L[a][i]
        for p in range(n*n):S[n+p][i]=H[p][i]
    for a in range(n):
        for b in range(n):
            for i in range(n):
                for j in range(n):
                    S[n+i*n+j][n+a*n+b]=mul(L[i][b],L[j][a])
    return S


def anti_multiplicative(S,n,q):
    # Directly tests sigma(x_i*x_j) = sigma(x_j)*sigma(x_i).
    _,mul,_=operations(q)
    for i in range(n):
        for j in range(n):
            col=n+i*n+j
            if any(S[a][col] for a in range(n)):return False
            for a in range(n):
                for b in range(n):
                    if S[n+a*n+b][col]!=mul(S[a][j],S[b][i]):return False
    return True


def brute_all_h(n,q):
    summary=Counter()
    for L in involutive_linear_parts(n,q):
        count=0
        for data in product(range(q),repeat=n*n*n):
            H=[list(data[p*n:(p+1)*n]) for p in range(n*n)]
            S=anti_matrix(n,q,L,H)
            if matmul(S,S,q)==eye(n+n*n):
                assert anti_multiplicative(S,n,q)
                count+=1
        summary[count]+=1
    return summary


def nullity_via_full_algebra(n,q,L):
    # Build the square equations on all generators by testing n^3 individual
    # quadratic perturbations in the original (n+n^2)-dimensional algebra.
    coeff=[]
    for k in range(n*n*n):
        H=[[0]*n for _ in range(n*n)]
        H[k//n][k%n]=1
        S=anti_matrix(n,q,L,H)
        SS=matmul(S,S,q)
        coeff.append([SS[row][col] for row in range(n,n+n*n) for col in range(n)])
    equations=list(map(list,zip(*coeff)))
    return n*n*n-rank(equations,q)


def compare_all_linear_parts(n,q):
    exponents=Counter()
    add,_,neg=operations(q)
    for L in involutive_linear_parts(n,q):
        invdim=rank([[add(L[i][j],neg(int(i==j))) for j in range(n)]
                     for i in range(n)],q)
        actual=nullity_via_full_algebra(n,q,L)
        if q%2==0:
            s=invdim;r=n-2*s
            expected=r*n*(n+1)//2+s*n*n
        else:
            # For L^2=I and odd characteristic the minus eigenspace has dimension invdim.
            expected=(n*n*n-n*(n-2*invdim))//2
        assert actual==expected,(n,q,invdim,actual,expected)
        exponents[(invdim,actual)]+=1
    return exponents


def ia_orbit_test(n=2,q=2):
    # Direct conjugation by all automorphisms with identity linear part.
    add,mul,neg=operations(q)
    parts=list(involutive_linear_parts(n,q))
    observed=Counter()
    for L in parts:
        accepted=[]
        for data in product(range(q),repeat=n*n*n):
            H=[list(data[p*n:(p+1)*n]) for p in range(n*n)]
            S=anti_matrix(n,q,L,H)
            if matmul(S,S,q)==eye(n+n*n):accepted.append(tuple(data))
        to_visit=set(accepted);orbits=[]
        while to_visit:
            seed=next(iter(to_visit))
            H=[list(seed[p*n:(p+1)*n]) for p in range(n*n)]
            S=anti_matrix(n,q,L,H)
            orb=set()
            for datum in product(range(q),repeat=n*n*n):
                G=[list(datum[p*n:(p+1)*n]) for p in range(n*n)]
                # U=I+g on generators, inverse=I-g, both fix the square.
                D=n+n*n
                U=eye(D);Uinv=eye(D)
                for p in range(n*n):
                    for j in range(n):
                        U[n+p][j]=G[p][j]
                        Uinv[n+p][j]=neg(G[p][j])
                X=matmul(matmul(U,S,q),Uinv,q)
                orb.add(tuple(X[n+p][j] for p in range(n*n) for j in range(n)))
            assert orb<=to_visit
            to_visit-=orb
            orbits.append(len(orb))
        invdim=rank([[add(L[i][j],neg(int(i==j))) for j in range(n)]
                     for i in range(n)],q)
        r=n-2*invdim
        assert len(orbits)==q**(r*n)
        observed[(invdim,len(orbits),min(orbits),max(orbits))]+=1
    return observed


def run():
    for q,expected in ((2,{16:3,64:1}),(3,{9:1,81:12,729:1})):
        histogram=brute_all_h(2,q)
        assert dict(histogram)==expected,(q,histogram)
        print('EXHAUSTIVE_ORIGINAL_SQUARE_AND_PRODUCTS',q,dict(sorted(histogram.items())),
              'total',sum(k*v for k,v in histogram.items()))
    for n,q in ((2,4),(3,2),(3,3)):
        print('FULL_ALGEBRA_LINEAR_KERNEL',n,q,
              sorted(compare_all_linear_parts(n,q).items()))
    print('ACTUAL_IA_CONJUGATION_ORBITS_F2',sorted(ia_orbit_test().items()))
    print('ANTI_INVOLUTION_CENSUS_AND_IA_ORBITS_OK')
if __name__=='__main__':run()
