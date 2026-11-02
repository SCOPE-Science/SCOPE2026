"""Exact arithmetic checks for parity occupancy-frequency dependence. Stdlib only."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb,exp,factorial

checks=0

def calc(b,n,r):
    alpha=Fraction(b-2,b)
    beta=Fraction(b-3,b-1)
    p=Fraction(comb(n,r)*(b-1)**(n-r),b**n)
    return Fraction(b,2)*p*( (-1 if r%2==0 else 1) + b*alpha**n-(b-1)*beta**(n-r))

# Direct enumeration: count allocations without conditional event formulas.
for b in range(3,6):
    for n in range(2,8):
        sums_o=0
        sums_c=defaultdict(int)
        sums_oc=defaultdict(int)
        for arr in product(range(b),repeat=n):
            loads=[0]*b
            for j in arr:loads[j]+=1
            odd=sum(v%2 for v in loads)
            sums_o+=odd
            freq=defaultdict(int)
            for v in loads:freq[v]+=1
            for r in range(1,n+1):
                sums_c[r]+=freq[r]
                sums_oc[r]+=odd*freq[r]
        m=b**n
        for r in range(1,n+1):
            got=Fraction(sums_oc[r],m)-Fraction(sums_o*sums_c[r],m*m)
            assert got==calc(b,n,r),(b,n,r,got,calc(b,n,r))
            checks+=1

# Exact-rational phase pattern: all even frequencies negative; singleton positive;
# for odd r>=3 the first positive, if it exists, has no later nonpositive return.
for b in range(4,45):
    for r in range(1,18):
        signs=[]
        for n in range(max(2,r),150):
            x=calc(b,n,r)
            signs.append((x>0)-(x<0))
            if r%2==0: assert x<0
            elif r==1: assert x>0
            checks+=1
        if r>=3 and r%2==1:
            assert signs[0]==-1
            seen_nonnegative=False
            for s in signs:
                if s>=0:seen_nonnegative=True
                if seen_nonnegative:assert s>=0
                checks+=1

# Asymptotic covariance per box at positive density.
for r in (1,2,3,4,5,7,9):
    for lam in (.3,.7,1.5,2.5):
        limit=(exp(-lam)*lam**r/factorial(r)/2)*( (-1 if r%2==0 else 1) +exp(-2*lam)*(1+2*lam-2*r))
        for b in (2000,10000):
            n=round(lam*b)
            v=float(calc(b,n,r))/b
            assert abs(v-limit)<0.015,(r,lam,b,v,limit)
            checks+=1
print('VERIFY_OK',checks)
