#!/usr/bin/env python3
"""Finite checks for tuple types over a metric star.
All distances are integers in {1,2,3}; zero appears only on the diagonal.
The direct enumeration does not assume the leaf-factorization formula.
"""
from collections import Counter
from itertools import combinations, product
from math import comb

D=(1,2,3)

def metric_ok(matrix):
    m=len(matrix)
    return all(matrix[i][j] <= matrix[i][l]+matrix[l][j]
               for i in range(m) for j in range(m) for l in range(m))

def core_metrics(k):
    # Core vertices: 0=center; 1,...,k=ordered new tuple.
    edges=list(combinations(range(k+1),2))
    for vals in product(D, repeat=len(edges)):
        q=[[0]*(k+1) for _ in range(k+1)]
        for (i,j),d in zip(edges, vals): q[i][j]=q[j][i]=d
        if metric_ok(q): yield q

def multiplicity(m):
    k=len(m)-1
    b=0
    for u in product(D,repeat=k):
        # leaf is vertex k+1, always distance 1 to center
        mat=[row+[1 if i==0 else u[i-1]] for i,row in enumerate(m)]
        mat.append([1]+list(u)+[0])
        if metric_ok(mat): b+=1
    return b

def spectral(k):
    h=Counter()
    for core in core_metrics(k): h[multiplicity(core)]+=1
    return h

def direct(k,n):
    # Brute-force independent enumeration of all k*(n+1)+k*(k-1)/2
    # unknown positive distances in a fixed (n+1+k)-point metric.
    # Fixed: center-leaf=1, distinct leaves=2.
    size=k+n+1
    edges=list(combinations(range(size),2))
    free=[]
    base=[[0]*size for _ in range(size)]
    for i,j in edges:
        if i==0 and 1<=j<=n: d=1
        elif 1<=i<j<=n: d=2
        else: free.append((i,j));continue
        base[i][j]=base[j][i]=d
    t=0
    for values in product(D,repeat=len(free)):
        m=[row[:] for row in base]
        for (i,j),d in zip(free,values):m[i][j]=m[j][i]=d
        if metric_ok(m): t+=1
    return t

def main():
    for k in (1,2,3,4):
        h=spectral(k)
        assert sum(h.values())==sum(1 for _ in core_metrics(k))
        assert max(h)==3**k and h[3**k]==1
        if k>=2:
            b2=8*3**(k-2)
            assert sorted(h,reverse=True)[1]==b2, (k,sorted(h,reverse=True)[:5])
            assert h[b2]==comb(k,2)
        if k>=3:
            b3=22*3**(k-3)
            assert sorted(h,reverse=True)[2]==b3, (k,sorted(h,reverse=True)[:6])
            assert h[b3]==3*comb(k,3)
        print(f'k={k}: core_metrics={sum(h.values())}, three_highest={h.most_common()[:3]}, top_bases={sorted(h,reverse=True)[:5]}')
        for n in (0,1,2):
            if k>3 and n>0: continue
            expected=sum(c*b**n for b,c in h.items())
            observed=direct(k,n)
            assert observed==expected,(k,n,observed,expected)
            print(f'  brute(k={k},n={n}): {observed} = spectral_sum')
        if k==2:
            for n in (0,1,2,3,4):
                v=sum(c*b**n for b,c in h.items())
                explicit=9*4**n+6*5**n+6*6**n+7**n+8**n+9**n
                assert v==explicit
                print(f'  k=2 closed(n={n}): {v}')
    print('ALL_TESTS_PASS')

if __name__=='__main__': main()
