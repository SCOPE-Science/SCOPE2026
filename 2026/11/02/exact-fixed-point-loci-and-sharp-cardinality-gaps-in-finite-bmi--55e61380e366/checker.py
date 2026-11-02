#!/usr/bin/env python3
"""Finite-band tests of the fixed-point-locus theorem.
Run: python3 checker.py
"""
from itertools import product

def ymembers(tab,n):
    return {y for y in range(n) if all(tab[y][x] == tab[x][tab[y][x]] for x in range(n))}

def is_band(tab,n):
    return (all(tab[x][x] == x for x in range(n)) and
            all(tab[tab[x][y]][z] == tab[x][tab[y][z]]
                for x in range(n) for y in range(n) for z in range(n)))

def construct(k,r):
    # 0..k-1 form a chain semilattice with top k-1;
    # k..k+r-1 form a left-zero ideal.
    n=k+r
    def mul(x,y):
        if x<k and y<k: return min(x,y)
        if x>=k: return x
        return y
    return [[mul(x,y) for y in range(n)] for x in range(n)]

def check(tab,n):
    yy=ymembers(tab,n)
    assert yy, 'missing left unit'
    assert all(tab[y][z] in yy for y in yy for z in yy), 'Y not closed'
    assert all(tab[tab[y][z]][y] == tab[z][y] for y in yy for z in yy), 'not RRB'
    assert len(yy)!=n-1, 'forbidden singleton complement'
    for x in range(n):
      for y in range(n):
        assert (tab[y][x]==tab[x][tab[y][x]]) == (tab[x][y]==tab[y][tab[x][y]]), 'defect asymmetry'
    return len(yy)

# Every band with prescribed 0 as a left identity, through four elements.
for n in range(1,5):
    free=[(i,j) for i in range(1,n) for j in range(n) if i!=j]
    count=0; spectrum=set()
    for assign in product(range(n), repeat=len(free)):
        t=[[j if i==0 else (i if i==j else 0) for j in range(n)] for i in range(n)]
        for (i,j),v in zip(free,assign): t[i][j]=v
        if is_band(t,n):
            count+=1; spectrum.add(check(t,n))
    print('all-unital-bands',n,'count',count,'Y-spectrum',sorted(spectrum))
    assert spectrum==({n} if n<=2 else set(range(1,n-1))|{n})

for n in range(1,14):
    observed=set()
    for k in range(1,n+1):
        r=n-k
        if r==1: continue
        t=construct(k,r)
        assert is_band(t,n)
        assert t[k-1] == list(range(n)) if k>=1 else True
        observed.add(check(t,n))
    assert observed==({n} if n<=2 else set(range(1,n-1))|{n})
# Every small right-regular unital band can be realized with two new non-Y elements.
for n in range(1,5):
    free=[(i,j) for i in range(1,n) for j in range(n) if i!=j]
    rr_count=0
    for assign in product(range(n), repeat=len(free)):
        base=[[j if i==0 else (i if i==j else 0) for j in range(n)] for i in range(n)]
        for (i,j),v in zip(free,assign): base[i][j]=v
        if not is_band(base,n): continue
        if not all(base[base[x][y]][x]==base[y][x] for x in range(n) for y in range(n)): continue
        rr_count+=1
        N=n+2
        t=[[0]*N for _ in range(N)]
        for x in range(N):
          for y in range(N):
            t[x][y]=base[x][y] if x<n and y<n else (x if x>=n else y)
        assert is_band(t,N)
        assert ymembers(t,N)==set(range(n))
    print('RRB-representation',n,'bases',rr_count)
print('ALL_CHECKS_OK')
