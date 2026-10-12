#!/usr/bin/env python3
"""Finite sanity tests for the two-radius distance-alphabet theorem.
Only mathematical, reproducible checks; no claim of an infinite exhaustive proof.
"""
from itertools import product
from math import floor

def rel(n, edges):
    return {(i,i) for i in range(n)} | {(u,v) for u,v in edges} | {(v,u) for u,v in edges}

def composition_power(A,n,k):
    reach=set((i,i) for i in range(n))
    for _ in range(k):
        reach={(x,z) for x,y in reach for yy,z in A if y==yy}
    return reach

def construct(A,B,n,a,b):
    k=floor(b/a)
    if k==1:
        r=(max(b/2,a/2)+a)/2
        s=(a+b)/2
        costs={(i,j):(0 if i==j else r if (i,j) in A else s if (i,j) in B else b) for i in range(n) for j in range(n)}
    else:
        r=(max(b/(k+1),a/2)+a)/2
        costs={(i,j):(0 if i==j else r if (i,j) in A else k*r if (i,j) in B else b) for i in range(n) for j in range(n)}
    d=[[costs[i,j] for j in range(n)] for i in range(n)]
    for t in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][t]+d[t][j])
    return d,k

def run():
    cases=0; realizable=0; max_levels={}
    for a,b in [(1,1.2),(1,1.99),(1,2),(1,2.1),(1,2.99),(1,3),(1,3.7),(1,4),(1,4.9)]:
        k=floor(b/a); max_level=0
        for n in range(1,5):
            pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
            for tags in product(range(3),repeat=len(pairs)):
                A=rel(n,[e for e,t in zip(pairs,tags) if t==2]); B=rel(n,[e for e,t in zip(pairs,tags) if t>=1])
                if not composition_power(A,n,k)<=B:continue
                d,_=construct(A,B,n,a,b)
                for i in range(n):
                    for j in range(n):
                        assert abs(d[i][j]-d[j][i])<1e-9
                        assert ((d[i][j]==0) == (i==j))
                        assert (d[i][j]<a)==((i,j) in A)
                        assert (d[i][j]<b)==((i,j) in B)
                        for t in range(n): assert d[i][j] <= d[i][t]+d[t][j]+1e-9
                levels={round(d[i][j],9) for i in range(n) for j in range(i+1,n)}
                max_level=max(max_level,len(levels))
                assert len(levels)<=(3 if k==1 else k+1)
                cases+=1
        max_levels[b]=max_level
    for k in range(2,10):
        n=k+2; A=rel(n,[(i,i+1) for i in range(n-1)])
        B=set((i,j) for i in range(n) for j in range(n) if abs(i-j)<=k)
        a=1.0;b=k+0.25
        d,_=construct(A,B,n,a,b)
        levels={round(d[i][j],9) for i in range(n) for j in range(i+1,n)}
        assert len(levels)==k+1,(k,levels)
        for i in range(1,n):
            for j in range(i+1,n): assert abs(d[0][i]-d[0][j])>1e-9
    n=3;A=rel(n,[(0,1)]);B=rel(n,[(0,1),(0,2)])
    d,_=construct(A,B,n,1,1.7)
    assert len({round(d[i][j],9) for i in range(n) for j in range(i+1,n)})==3
    print('VERIFY_OK',{'admissible_pairs_checked':cases,'max_levels_by_second_radius':max_levels,'lower_path_parameters':[2,3,4,5,6,7,8,9], 'k1_lower_witness':True})
if __name__=='__main__':run()
