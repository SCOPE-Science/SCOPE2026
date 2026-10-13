from fractions import Fraction
from itertools import permutations
from math import gcd

PARTS=[(4,),(3,1),(2,2),(2,1,1),(1,1,1,1)]
ALL_PRIMES=[2,3,5,7]
ODD_PRIMES=[3,5,7,11]
EXPECTED_ALL=[Fraction(31,16),Fraction(5,2),Fraction(91,36),Fraction(14,5),Fraction(96,35)]
EXPECTED_ODD=[Fraction(121,81),Fraction(16,9),Fraction(403,225),Fraction(208,105),Fraction(768,385)]

def local_I(p,e):
    return sum((Fraction(1,p**j) for j in range(e+1)), Fraction(0))

def maxima(primes):
    ans=[]
    for part in PARTS:
        r=len(part)
        best=Fraction(0)
        for exps in set(permutations(part)):
            v=Fraction(1)
            for p,e in zip(primes[:r],exps):
                v*=local_I(p,e)
            best=max(best,v)
        ans.append(best)
    return ans

assert maxima(ALL_PRIMES)==EXPECTED_ALL
assert maxima(ODD_PRIMES)==EXPECTED_ODD
assert max(EXPECTED_ALL)<3
assert max(EXPECTED_ODD)<2

LIMIT=100000
spf=list(range(LIMIT+1))
for i in range(2,int(LIMIT**0.5)+1):
    if spf[i]==i:
        for j in range(i*i,LIMIT+1,i):
            if spf[j]==j:
                spf[j]=i

def factor(n):
    f={}
    while n>1:
        p=spf[n]
        f[p]=f.get(p,0)+1
        n//=p
    return f

def abundance_from_factor(f):
    v=Fraction(1)
    for p,e in f.items():
        v*=local_I(p,e)
    return v

clubs={}
eligible=0
for n in range(1,LIMIT+1):
    f=factor(n)
    if sum(f.values())<=4:
        eligible+=1
        q=abundance_from_factor(f)
        clubs.setdefault(q,[]).append(n)

checked_pairs=0
for vals in clubs.values():
    if len(vals)<2:
        continue
    for i,a in enumerate(vals):
        for b in vals[i+1:]:
            checked_pairs+=1
            assert gcd(a,b)>1, (a,b,vals)

print(f"VERIFY_OK eligible={eligible} equal_ratio_pairs={checked_pairs} limit={LIMIT} max_all={max(EXPECTED_ALL)} max_odd={max(EXPECTED_ODD)}")
