"""Exact independent finite checks for greedy crown-graph dimer jamming."""
from fractions import Fraction
from functools import lru_cache
from math import prod

@lru_cache(None)
def reduced(m,q):
    if m==1: return Fraction(q)
    z=m*m-q
    a=Fraction(0)
    for w,k in ((q*(q-1),q-2),(2*q*(m-q),q-1),((m-q)**2,q)):
        if w:a+=Fraction(w,z)*reduced(m-1,k)
    return a

@lru_cache(None)
def independent(left,right):
    m=left.bit_count()
    if not m:return Fraction(0)
    pairs=[(i,j) for i in range(N) if left>>i&1 for j in range(N) if right>>j&1 and i!=j]
    if not pairs:return Fraction(1)
    return sum((independent(left^(1<<i),right^(1<<j)) for i,j in pairs),Fraction(0))/len(pairs)

for N in range(2,7):
    full=(1<<N)-1
    exact=independent(full,full)
    formula=reduced(N,N)
    assert exact==formula,(N,exact,formula)
    H=sum((Fraction(1,k) for k in range(1,N)),Fraction(0))
    lo=Fraction(2,N+1)-Fraction(4,(N+1)*(N+2))*(H+2-Fraction(2,N))
    hi=Fraction(2,N+1)
    assert lo<=exact<=hi
    print(f'n={N} P={exact} interval=[{lo},{hi}]')

# Separately enumerate transition counts from explicit remaining endpoint sets.
for N in range(3,8):
    for left in range(1<<N):
        m=left.bit_count()
        if m<2: continue
        for right in range(1<<N):
            if right.bit_count()!=m: continue
            q=(left&right).bit_count()
            bins=[0,0,0]
            for i in range(N):
                if not(left>>i&1):continue
                for j in range(N):
                    if i==j or not(right>>j&1):continue
                    q2=((left^(1<<i))&(right^(1<<j))).bit_count()
                    bins[q-q2]+=1
            assert bins==[(m-q)**2,2*q*(m-q),q*(q-1)],(N,m,q,bins)
print('All exact independent finite-state checks passed.')
