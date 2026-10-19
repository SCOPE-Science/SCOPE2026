#!/usr/bin/env python3
"""Standalone finite checks for square-zero elements in truncated cyclic path algebras."""
from itertools import product
from math import comb

def admissible_supports(n):
    for mask in range(1 << n):
        S = tuple(i for i in range(n) if (mask >> i) & 1)
        if any((i+1) % n in S for i in S):
            continue
        yield S

def long_gaps(n,S):
    if not S:
        return 0
    k=len(S)
    gaps=[((S[(j+1)%k]-S[j])%n) or n for j in range(k)]
    assert all(g>=2 for g in gaps) and sum(gaps)==n
    return sum(g>=4 for g in gaps)

def formula(n,q):
    total=q**(2*n)
    for S in admissible_supports(n):
        if not S:
            continue
        k=len(S);h=long_gaps(n,S)
        total+=(q-1)**k*q**(2*n-k-h)
    return total

def equations(n,b,c,q):
    for i in range(n):
        if b[i]*b[(i+1)%n] % q:
            return False
        if (b[i]*c[(i+1)%n]+c[i]*b[(i+2)%n])%q:
            return False
    return True

def direct_count(n,q):
    total=0
    for b in product(range(q),repeat=n):
        if any(b[i]*b[(i+1)%n] % q for i in range(n)):
            continue
        for c in product(range(q),repeat=n):
            if equations(n,b,c,q):
                total+=1
    return total*q**n

def modrank(mat,p):
    a=[list(row) for row in mat]
    n=len(a);m=len(a[0]) if a else 0;r=0
    for j in range(m):
        piv=next((i for i in range(r,n) if a[i][j]%p),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        inv=pow(a[r][j],-1,p)
        for k in range(j,m):a[r][k]=(a[r][k]*inv)%p
        for i in range(n):
            if i!=r and a[i][j]%p:
                z=a[i][j]
                for k in range(j,m):a[i][k]=(a[i][k]-z*a[r][k])%p
        r+=1
    return r

def verify_support_rank(n,p):
    for S in admissible_supports(n):
        if not S:continue
        k=len(S); b=[int(i in S) for i in range(n)]
        a=[[0]*n for _ in range(n)]
        for i in range(n):
            a[i][(i+1)%n]=b[i]
            a[i][i]=b[(i+2)%n]
        assert modrank(a,p)==k+long_gaps(n,S),(n,p,S)

def perrin(n):
    a=[3,0,2]
    for i in range(3,n+1):a.append(a[i-2]+a[i-3])
    return a[n]

def top_counts(n):
    return 1+sum(1 for S in admissible_supports(n)
                 if S and not long_gaps(n,S))

def check_square_product(n):
    # Exhaustive full-algebra test over F_2 for n=4, including diagonal and length-three paths.
    q=2
    assert n==4
    for digits in product(range(2),repeat=4*n):
        a,b,c,d=[digits[j*n:(j+1)*n] for j in range(4)]
        expected=all(v==0 for v in a) and equations(n,b,c,q)
        # Path concatenation: coefficient of the path of length m based at i.
        coeff=[0]*(4*n)
        for i in range(n):
            for m in range(4):
                z=0
                for j in range(m+1):
                    z+=digits[j*n+i]*digits[(m-j)*n+(i+j)%n]
                coeff[m*n+i]=z%2
        actual=not any(coeff)
        assert actual==expected,(digits,coeff)

def run():
    check_square_product(4)
    testcases=[(n,2) for n in range(4,9)]+[(4,3),(5,3),(6,3),(4,5)]
    for n,q in testcases:
        got=direct_count(n,q); want=formula(n,q)
        assert got==want,(n,q,got,want)
        print('finite-count',n,q,got)
    for n in range(4,16):
        verify_support_rank(n,2)
        verify_support_rank(n,3)
        assert top_counts(n)==1+perrin(n),(n,top_counts(n),perrin(n))
    print('VERIFY_OK')

if __name__=='__main__':run()
