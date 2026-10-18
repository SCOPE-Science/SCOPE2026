"""Finite checks for the concept-class partition and exact expectation identities.
Run: python verify.py. Uses only the Python standard library.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb


def concept_profile(n, encoded):
    mask=(1<<n)-1
    rows=[(encoded>>(n*i))&mask for i in range(n)]
    cats=[0,0,0,0,0] # min side <=1, (2,2), (2,>=3), (>=3,2), (>=3,>=3)
    for extent in range(1<<n):
        intent=mask
        for i in range(n):
            if extent>>i&1:
                intent &=rows[i]
        closure=0
        for i in range(n):
            if (rows[i]&intent)==intent:
                closure |=1<<i
        if closure !=extent:
            continue
        a=extent.bit_count(); b=intent.bit_count()
        index=(0 if min(a,b)<=1 else 1 if a==2 and b==2 else 2 if a==2 else 3 if b==2 else 4)
        cats[index]+=1
    return cats


def expected_exact(n,p):
    q=1-p
    cat=[Fraction(0) for _ in range(5)]
    for a in range(n+1):
        for b in range(n+1):
            term=comb(n,a)*comb(n,b)*p**(a*b)*(1-p**a)**(n-b)*(1-p**b)**(n-a)
            idx=0 if min(a,b)<=1 else 1 if a==2 and b==2 else 2 if a==2 else 3 if b==2 else 4
            cat[idx]+=term
    two_two=comb(n,2)**2*p**4*(1-p*p)**(2*(n-2)) if n>=2 else 0
    two_many=comb(n,2)*sum(comb(n,k)*(p*p)**k*(1-p*p)**(n-k)*(1-p**k)**(n-2) for k in range(3,n+1)) if n>=2 else 0
    if n>=2:
        assert cat[1]==two_two,(n,p,cat[1],two_two)
        assert cat[2]==two_many and cat[3]==two_many
    return cat

checks=0
for n in range(1,5):
    N=n*n
    hist=defaultdict(lambda:[0]*5)
    for bits in range(1<<N):
        cat=concept_profile(n,bits)
        m=bits.bit_count()
        for j in range(5):hist[m][j]+=cat[j]
    for p in (Fraction(1,2),Fraction(1,3),Fraction(2,3)):
        actual=[sum(hist[k][j]*p**k*(1-p)**(N-k) for k in range(N+1)) for j in range(5)]
        expected=expected_exact(n,p)
        assert actual==expected,(n,p,actual,expected)
        checks+=1
print('VERIFY_OK',checks,'finite weighted context profiles; all 65,536 four-by-four contexts covered')
