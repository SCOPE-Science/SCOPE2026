"""Direct finite-field checks of free class-two Lie retraction rank formula.
This script uses only the Python standard library and directly builds Lie maps.
"""
from itertools import product
from math import comb


def mat_mul(A,B,q):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%q for j in range(len(B[0]))] for i in range(len(A))]


def rank(A,q):
    A=[row[:] for row in A]
    if not A: return 0
    h,w=len(A),len(A[0]); r=0
    for j in range(w):
        k=next((k for k in range(r,h) if A[k][j]%q),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]
        inv=pow(A[r][j],-1,q)
        A[r]=[(x*inv)%q for x in A[r]]
        for k in range(h):
            if k!=r and A[k][j]:
                c=A[k][j]
                A[k]=[(x-c*y)%q for x,y in zip(A[k],A[r])]
        r+=1
        if r==h: break
    return r


def exterior(T,q):
    n=len(T)
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    return [[(T[i][a]*T[j][b]-T[i][b]*T[j][a])%q for (a,b) in pairs] for (i,j) in pairs]


def count(n,q):
    assert q in (2,3,5), 'prime fields only, not arbitrary q'
    c=comb(n,2)
    by_rank={}
    all_endomorphism_pairs=0
    idempotent_T_count=0
    for flat in product(range(q),repeat=n*n):
        T=[list(flat[i*n:(i+1)*n]) for i in range(n)]
        P=exterior(T,q)
        T2=mat_mul(T,T,q)
        isprojection=T2==T
        if isprojection:idempotent_T_count+=1
        for vals in product(range(q),repeat=c*n):
            all_endomorphism_pairs+=1
            if not isprojection:continue
            C=[list(vals[i*n:(i+1)*n]) for i in range(c)]
            # Independent full block-matrix implementation of idempotence.
            M=[[0]*(n+c) for _ in range(n+c)]
            for i in range(n):
                for j in range(n):M[i][j]=T[i][j]
            for i in range(c):
                for j in range(n):M[n+i][j]=C[i][j]
                for j in range(c):M[n+i][n+j]=P[i][j]
            if mat_mul(M,M,q)!=M:continue
            # Verify preserved brackets on every generator pair explicitly.
            pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
            for col,(a,b) in enumerate(pairs):
                for row,(i,j) in enumerate(pairs):
                    expected=(T[i][a]*T[j][b]-T[i][b]*T[j][a])%q
                    assert M[n+row][n+col]==expected
            r=rank(M,q)
            by_rank[r]=by_rank.get(r,0)+1
    predicted={}
    for r in range(n+1):
        # integer-only Gaussian binomial via exact product quotient
        numer=denom=1
        for i in range(r): numer*=q**(n-i)-1;denom*=q**(r-i)-1
        gauss=numer//denom
        exponent=(r*(n-r)*(n+2*r))//2
        t=r*(r+1)//2
        predicted[t]=predicted.get(t,0)+gauss*q**exponent
    assert by_rank==predicted,(n,q,by_rank,predicted)
    print(f'n={n}, q={q}; all_endomorphisms={all_endomorphism_pairs}; idempotent_linear_parts={idempotent_T_count}; rank_distribution={dict(sorted(by_rank.items()))}; OK')


if __name__=='__main__':
    for n,q in [(2,2),(2,3),(3,2)]:count(n,q)
    print('VERIFY_OK')
