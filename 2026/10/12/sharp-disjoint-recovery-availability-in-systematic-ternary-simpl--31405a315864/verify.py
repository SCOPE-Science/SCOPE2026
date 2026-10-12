#!/usr/bin/env python3
"""Exact finite checks for projective recovery triples and disjoint availability."""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, product

Q=3

def norm(x):
    z = next(a for a in x if a)
    inv = 1 if z == 1 else 2
    return tuple((a*inv)%Q for a in x)

def combination(x,y,a,b):
    return tuple((a*u+b*v)%Q for u,v in zip(x,y))

def projective_line(x,y):
    assert norm(x) != norm(y)
    return tuple(sorted({norm(x),norm(y),norm(combination(x,y,1,1)),norm(combination(x,y,1,2))}))

def match_number(helper_points):
    # Enumerate optimal matchings of the actual recovery-helper graph by DP.
    n=len(helper_points)
    neighbors=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            if helper_points[i]!=helper_points[j]:
                neighbors[i]|=1<<j
                neighbors[j]|=1<<i
    @lru_cache(None)
    def rec(mask):
        if mask == 0: return 0
        bit=mask & -mask
        i=bit.bit_length()-1
        rest=mask ^ bit
        result=rec(rest)
        for j in range(n):
            if (rest & (1<<j)) and (neighbors[i] & (1<<j)):
                result=max(result,1+rec(rest ^ (1<<j)))
        return result
    return rec((1<<n)-1)

def run(n):
    cols=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    cols += [v for v in product(range(Q),repeat=n) if any(v)]
    ncol=len(cols)
    types=[norm(x) for x in cols]
    mult=Counter(types)
    axes={norm(tuple(int(i==j) for i in range(n))) for j in range(n)}
    assert len(axes)==n
    assert all(mult[p]==(3 if p in axes else 2) for p in mult)
    lines=defaultdict(list)
    for p in mult:
        for q in mult:
            if p!=q:
                lines[p].append(projective_line(p,q))
    L=(3**(n-1)-1)//2
    assert all(len(set(lines[p]))==L for p in mult)
    incidences=0
    degrees=Counter()
    for k,P in enumerate(types):
        grouped=defaultdict(list)
        for i,Qp in enumerate(types):
            if Qp!=P:
                grouped[projective_line(P,Qp)].append((i,Qp))
        assert len(grouped)==L
        count=0
        disjoint=0
        for line, item in grouped.items():
            assert len(set(t for i,t in item))==3
            for (i,a),(j,b) in combinations(item,2):
                if a != b:
                    assert P in projective_line(a,b)
                    count+=1
            disjoint+=match_number(tuple(t for i,t in item))
        h=sum(1 for z in P if z)
        expected=(12*L+4*(n-1) if h==1 else
                  12*L+4*n+1 if h==2 else 12*L+4*n)
        best=3*L+(1 if h==2 else 0)
        assert (count,disjoint)==(expected,best), (n,k,h,count,disjoint,expected,best)
        assert mult[P]-1==(2 if h==1 else 1)
        degrees[h]+=1
        incidences+=count
    assert degrees[1]==3*n
    assert degrees[2]==2*n*(n-1)
    assert sum(v for h,v in degrees.items() if h>=3)==3**n-1-2*n*n
    assert incidences % 3==0
    if n==2: assert incidences//3==60
    if n==3: assert incidences//3==572
    if n==4: assert incidences//3==4808
    print(f"n={n},length={ncol},minimal-nonparallel-dual-triples={incidences//3},coordinate-classes={dict(degrees)}")

if __name__=='__main__':
    for n in (2,3,4): run(n)
    print('VERIFY_OK')
