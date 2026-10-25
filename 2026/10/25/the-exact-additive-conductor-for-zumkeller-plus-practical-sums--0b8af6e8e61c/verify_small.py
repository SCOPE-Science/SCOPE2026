"""Exact divisor-subset and practical-number checks for the finite certificate.
Run with Python 3 in the same directory as odd_z_witnesses.txt.
"""
from pathlib import Path
from math import isqrt

LIMIT=1_000_000
spf=list(range(LIMIT+1))
for p in range(2,isqrt(LIMIT)+1):
    if spf[p]==p:
        for n in range(p*p,LIMIT+1,p):
            if spf[n]==n:spf[n]=p

def factor(n):
    out=[]
    while n>1:
        p=spf[n];e=0
        while n%p==0:n//=p;e+=1
        out.append((p,e))
    return out

def divisors_and_sigma(n):
    divs=[1];sigma=1
    for p,e in factor(n):
        geom=sum(p**j for j in range(e+1));sigma*=geom
        old=divs
        divs=[d*p**j for d in old for j in range(e+1)]
    return divs,sigma

def is_zumkeller(n):
    if n<6:return False
    ds,sigma=divisors_and_sigma(n)
    if sigma%2 or sigma<2*n:return False
    target=sigma//2-n
    subset=1
    for d in ds:
        if d==n:continue
        subset|=subset<<d
        if (subset>>target)&1:return True
    return False

def is_practical(n):
    if n==1:return True
    sigma=1
    for p,e in factor(n):
        if p>sigma+1:return False
        sigma*=sum(p**j for j in range(e+1))
    return True

# A direct subset-sum implementation independently confirms the
# prime-factor characterization of practicality for small inputs.
for n in range(1,1001):
    ds,_=divisors_and_sigma(n)
    mask=1
    for d in ds:mask|=mask<<d
    direct=all((mask>>t)&1 for t in range(1,n+1))
    assert direct==is_practical(n),(n,direct,is_practical(n))

witnesses=[int(x) for x in Path('odd_z_witnesses.txt').read_text().split()]
assert len(witnesses)==1989 and witnesses==sorted(set(witnesses))
assert all(x<=LIMIT and x%2 and is_zumkeller(x) for x in witnesses)

# Exhaustively test every possible odd Zumkeller summand below 19067;
# every odd practical number is 1, so the other decomposition is Z+1.
odd_z=[n for n in range(1,19068,2) if is_zumkeller(n)]
assert len(odd_z)==38 and odd_z==[x for x in witnesses if x<=19067]
assert not is_zumkeller(19066)
assert all(not is_practical(19067-z) for z in odd_z if z<19067)
assert is_zumkeller(20176)

# Exhaustively determine all exceptional integers up to 19067.
zs=[n for n in range(1,19068) if is_zumkeller(n)]
ps=[n for n in range(1,19068) if is_practical(n)]
rep=0
for z in zs:
    rep|=sum(1<<(z+p) for p in ps if z+p<=19067)
bad=[n for n in range(1,19068) if not ((rep>>n)&1)]
assert len(bad)==720 and max(bad)==19067
assert bad==[int(x) for x in Path("exceptions.txt").read_text().split()]
print(f'SMALL_CERTIFICATE_OK odd_z={len(odd_z)} exceptions={len(bad)} last={max(bad)}')
