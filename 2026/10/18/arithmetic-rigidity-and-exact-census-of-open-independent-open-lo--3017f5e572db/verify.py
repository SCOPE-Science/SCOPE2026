"""Reproducible finite checks for open-independent OLD codes on rook graphs.
No claim that finite checks alone establish generality."""
from itertools import combinations
from math import factorial
from collections import Counter

def neighbor_masks(m,n):
    return [sum(1 << (i*n+j) for i in range(m) for j in range(n)
                if (i==v//n) != (j==v%n)) for v in range(m*n)]

def valid(mask,nb):
    taken=set()
    for v,adj in enumerate(nb):
        z=adj&mask
        if z==0 or z in taken or (mask>>v&1 and z.bit_count()!=1):
            return False
        taken.add(z)
    return True

def expected(m,n):
    if n==2*m or n==2*m+1:
        return (2*m, factorial(n)//(2**m))
    if m==2*n or m==2*n+1:
        return (2*n, factorial(m)//(2**n))
    if (2*n-m)%3==0 and (2*m-n)%3==0:
        h=(2*n-m)//3;v=(2*m-n)//3
        if h>0 and v>0:
            return (2*(h+v),factorial(m)*factorial(n)//(2**(h+v)*factorial(h)*factorial(v)))
    return (None,0)

def exact_brute(m,n):
    nb=neighbor_masks(m,n)
    counts=Counter()
    for k in range(2,m*n+1,2):
        for comb in combinations(range(m*n),k):
            mask=sum(1<<p for p in comb)
            if valid(mask,nb):counts[k]+=1
    expected_k,expected_count=expected(m,n)
    assert sum(counts.values())==expected_count,(m,n,counts,(expected_k,expected_count))
    if counts:
        assert counts=={expected_k:expected_count},(m,n,counts)
    print('EXHAUSTIVE',m,n,'classes',dict(counts),'expected',expected_k,expected_count)

def construction(m,n,h,v,free_row=None,free_col=None):
    # explicitly allocate h horizontal two-vertex components, v vertical two-vertex components
    assert m == h+2*v+(free_row is not None)
    assert n == 2*h+v+(free_col is not None)
    rows=[i for i in range(m) if i!=free_row]
    cols=[j for j in range(n) if j!=free_col]
    S=[]
    for i in range(h):
        S.extend([(rows[i],cols[2*i]),(rows[i],cols[2*i+1])])
    for j in range(v):
        S.extend([(rows[h+2*j],cols[2*h+j]),(rows[h+2*j+1],cols[2*h+j])])
    mask=sum(1<<(a*n+b) for a,b in S)
    assert valid(mask,neighbor_masks(m,n)),(m,n,h,v,S)
    print('CONSTRUCTION',m,n,h,v,'SIZE',2*(h+v),'OK')

for m,n in [(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(3,7),(4,4),(4,5)]:
    exact_brute(m,n)
for h,v in [(1,1),(2,1),(1,2),(2,2),(3,1),(1,3),(4,3),(6,6)]:
    construction(h+2*v,2*h+v,h,v)
for h in [2,3,4,6,12]:
    construction(h,2*h,h,0)
    construction(h,2*h+1,h,0,free_col=2*h)
for v in [2,3,5]:
    construction(2*v,v,0,v)
    construction(2*v+1,v,0,v,free_row=2*v)
print('VERIFICATION_OK')
