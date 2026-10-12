#!/usr/bin/env python3
"""Exact reproducibility checks for finite identical-qubit heat baths.
Only Python standard library is required. Universal statements are proved in RESULT.md.
"""
from fractions import Fraction
from math import comb


def cat(j):
    return comb(2*j, j) // (j+1)


def by_shell(n,q):
    return sum(min(comb(n,k),comb(n,k-1))*q**k for k in range(1,n+1))/(1+q)**n


def by_catalan(n,q):
    m=(n+1)//2
    z=q/(1+q)**2
    return q/(1+q)*sum(cat(j)*z**j for j in range(m))


def brute_energy_sector(n,q):
    # Enumerate the initial nonzero eigenvalues of each energy sector.
    # The rank of the excited subspace bounds its total occupied weight.
    total=Fraction(0)
    for k in range(n+1):
        diag=[]
        for bath in range(1<<n):
            if bath.bit_count()==k:
                diag.append(q**k)
        dim_exc=sum(bath.bit_count()==k-1 for bath in range(1<<n))
        total+=sum(sorted(diag,reverse=True)[:dim_exc])
    return total/(1+q)**n

qvals=[Fraction(0), Fraction(1,5),Fraction(1,2),Fraction(2,3),Fraction(4,5),Fraction(1)]
tests=0
for n in range(1,14):
    for q in qvals:
        a=by_shell(n,q)
        b=by_catalan(n,q)
        assert a==b,(n,q,a,b)
        tests+=1
        if n<=9:
            c=brute_energy_sector(n,q)
            assert a==c,(n,q,a,c)
            tests+=1
for m in range(1,21):
    for q in qvals:
        a=by_shell(2*m,q)
        b=by_shell(2*m-1,q)
        assert a==b
        tests+=1
        if m>1:
            gain=by_shell(2*m-1,q)-by_shell(2*m-3,q)
            want=Fraction(cat(m-1))*q**m/(1+q)**(2*m-1)
            assert gain==want,(m,q,gain,want)
            tests+=1
for m in range(1,25):
    p=[0]*(2*m)
    for k in range(1,2*m):
        p[k]=min(comb(2*m-1,k),comb(2*m-1,k-1))
    left=[0]*(2*m+2)
    for k,a in enumerate(p):
        for offset,coef in enumerate([1,2,1]):
            left[k+offset]+=a*coef
    right=[0]*(2*m+2)
    for k in range(1,2*m+2):
        if k<=2*m+1:
            right[k]=min(comb(2*m+1,k),comb(2*m+1,k-1)) if k<=2*m+1 else 0
    left[m+1]+=cat(m)
    assert left==right,(m,left,right)
    tests+=1

# Universal thermal-majorization ceiling is q; finite values are strictly below q for 0<q<=1.
for n in range(1,20):
    for q in qvals[1:]:
        assert by_shell(n,q)<q
        tests+=1

# At the infinite-temperature endpoint, check exact central-binomial tail.
for m in range(1,25):
    assert by_shell(2*m-1,Fraction(1))==1-Fraction(comb(2*m,m),4**m)
    tests+=1

# Example: first size capable of positive ergotropy at q=2/3 is n=5.
assert by_shell(3,Fraction(2,3)) < Fraction(1,2)
assert by_shell(5,Fraction(2,3)) > Fraction(1,2)
print('VERIFY_OK',tests,'exact arithmetic checks')
