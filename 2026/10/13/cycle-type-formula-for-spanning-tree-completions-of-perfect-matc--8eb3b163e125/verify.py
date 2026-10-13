#!/usr/bin/env python3
"""Finite arithmetic checks for a crown-graph spanning-tree completion formula."""
from itertools import permutations, combinations
from math import factorial


def det_bareiss(M):
    a = [row[:] for row in M]
    n = len(a)
    if n == 0: return 1
    prev = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k+1, n) if a[j][k]), None)
            if j is None: return 0
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                val = a[i][j] * pivot - a[i][k] * a[k][j]
                assert val % prev == 0
                a[i][j] = val // prev
        for i in range(k+1, n): a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def cheby(k, x):
    assert k >= 0
    if k == 0: return 1
    a,b = 1,x
    for _ in range(2, k+1): a,b = b,2*x*b-a
    return b


def cycles(p):
    n=len(p); seen=set(); lengths=[]
    for i in range(n):
        if i in seen: continue
        j=i; l=0
        while j not in seen:
            seen.add(j);l+=1;j=p[j]
        lengths.append(l)
    return sorted(lengths)


def predicted(p):
    n=len(p); L=cycles(p)
    numerator=2**(len(L)-1)
    for ell in L:
        numerator *= cheby(ell,n-1)-((-1)**ell)
    assert numerator % (n*n)==0
    return numerator//(n*n)


def quotient_cofactor(p):
    n=len(p)
    # Vertices: selected matched pairs (a_i, b_{p(i)}), indexed by i.
    # Each original a_i-b_j with i!=j joins pair i to pair p^{-1}(j).
    inv=[0]*n
    for i,j in enumerate(p):inv[j]=i
    L=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:continue  # original deleted diagonal
            k=inv[j]
            if k==i:continue # selected matching edge becomes loop
            L[i][i]+=1;L[k][k]+=1
            L[i][k]-=1;L[k][i]-=1
    return det_bareiss([row[:-1] for row in L[:-1]])


def multigraph_cofactor(p):
    n=len(p)
    # Independent construction from 2K_n: remove one edge for each
    # directed permutation step (including both parallel copies for a 2-cycle).
    L=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            m=2-int(p[i]==j)-int(p[j]==i)
            assert 0<=m<=2
            L[i][i]+=m;L[j][j]+=m
            L[i][j]-=m;L[j][i]-=m
    return det_bareiss([row[:-1] for row in L[:-1]])


def brute_count(p):
    n=len(p); verts=list(range(2*n))
    selected=[(i,n+p[i]) for i in range(n)]
    excluded=set(selected)
    rest=[(i,n+j) for i in range(n) for j in range(n) if i!=j and (i,n+j) not in excluded]
    count=0
    for ext in combinations(rest,n-1):
        parent=list(range(2*n))
        def root(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        good=True
        for u,v in selected+list(ext):
            ru,rv=root(u),root(v)
            if ru==rv:
                good=False;break
            parent[ru]=rv
        if good and len({root(i) for i in verts})==1:count+=1
    return count


def run():
    total=0; brute=0; lengths={}; evidence={}
    for n in range(3,8):
        for p in permutations(range(n)):
            if any(p[i]==i for i in range(n)):continue
            L=tuple(cycles(p));pr=predicted(p)
            a=quotient_cofactor(p); b=multigraph_cofactor(p)
            assert pr==a==b,(n,p,pr,a,b)
            if n<=5:
                count=brute_count(p);brute+=1
                assert pr==count,(n,p,pr,count)
            total+=1
            if (n,L) in evidence:assert evidence[(n,L)]==pr
            evidence[n,L]=pr
            lengths[n]=lengths.get(n,0)+1
    assert evidence[(4,(2,2))]==32
    assert evidence[(4,(4,))]==36
    assert evidence[(3,(3,))]==3
    print('VERIFY_OK tested_derangements='+str(total)+' brute_matchings='+str(brute)+' by_order='+str(lengths))
    print('CYCLE_TYPE_COUNTS',sorted((n,ell,v) for (n,ell),v in evidence.items() if n<=6))
if __name__=='__main__':run()
