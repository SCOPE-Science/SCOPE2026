"""Independent exhaustive verifier of return/crossing joint law."""
from itertools import product
from math import comb
from collections import Counter
from fractions import Fraction

def walk_stats(bits):
    s=0
    x=[s]
    for a in bits:
        s+=a
        x.append(s)
    n=len(bits)
    k=sum(x[j]==0 for j in range(1,n) if j%2==0)
    c=sum(x[j-1]*x[j+1]<0 for j in range(1,n))
    return k,c

def theoretical(m,k,c):
    if not 0<=c<=k<=m: return Fraction(0)
    return Fraction(comb(2*m-k,m)*comb(k,c),4**m)

checks=0
for m in range(0,9):
    n=2*m+1
    counts=Counter(walk_stats(bits) for bits in product((-1,1), repeat=n))
    assert sum(counts.values())==2**n
    for k in range(m+1):
        for c in range(k+1):
            got=Fraction(counts[k,c], 2**n)
            want=theoretical(m,k,c)
            assert got==want,(m,k,c,got,want)
            checks+=1

    for k in range(m+1):
        pK=sum(theoretical(m,k,c) for c in range(k+1))
        assert pK==Fraction(comb(2*m-k,m),2**(2*m-k))
        checks+=1
        for c in range(k+1):
            assert theoretical(m,k,c)==pK*Fraction(comb(k,c),2**k)
            checks+=1

    for c in range(m+1):
        pC=sum(theoretical(m,k,c) for k in range(c,m+1))
        assert pC==Fraction(comb(2*m+1,m+c+1),4**m),(m,c)
        checks+=1

    assert sum(theoretical(m,k,c) for k in range(m+1) for c in range(k+1))==1
    checks+=1

# Exact conditional-variance identity and characteristic functions.
for m in range(1,16):
    pm=[sum(theoretical(m,k,c) for c in range(k+1)) for k in range(m+1)]
    meanK=sum(Fraction(k)*pm[k] for k in range(m+1))
    meanK2=sum(Fraction(k*k)*pm[k] for k in range(m+1))
    meanC=sum(Fraction(c)*theoretical(m,k,c) for k in range(m+1) for c in range(k+1))
    covCK=sum(Fraction(c*k)*theoretical(m,k,c) for k in range(m+1) for c in range(k+1))-meanC*meanK
    d2=sum(Fraction((2*c-k)**2)*theoretical(m,k,c) for k in range(m+1) for c in range(k+1))
    assert meanC==meanK/2
    assert covCK==(meanK2-meanK**2)/2
    assert d2==meanK
    checks+=3

# For each complete return-time pattern the crossing indicators have the
# conditional Binomial distribution, not merely conditional on their count.
for m in range(0,7):
    n=2*m+1
    by_pattern={}
    for bits in product((-1,1), repeat=n):
        x=[0]
        for z in bits: x.append(x[-1]+z)
        pattern=tuple(j for j in range(2,n,2) if x[j]==0)
        c=sum(x[j-1]*x[j+1]<0 for j in range(1,n))
        by_pattern.setdefault(pattern,Counter())[c]+=1
    for pattern,freq in by_pattern.items():
        r=len(pattern)
        size=sum(freq.values())
        for c in range(r+1):
            assert Fraction(freq[c],size)==Fraction(comb(r,c),2**r)
            checks+=1

print('PASS exact assertions:',checks)
