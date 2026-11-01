#!/usr/bin/env python3
"""Independent direct shortest-path and eigenspectrum tests for two graph metrics.
Requires Python 3 and numpy. No network or data files required.
"""
from collections import deque
from itertools import combinations
from math import comb
import numpy as np


def graph_distances(vertices, edges):
    n=len(vertices); index={v:i for i,v in enumerate(vertices)}
    adj=[[] for _ in vertices]
    for a,b in edges:
        u=index[a];v=index[b];adj[u].append(v);adj[v].append(u)
    D=np.full((n,n),-1,dtype=np.int64)
    for s in range(n):
        D[s,s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if D[s,v]<0:D[s,v]=D[s,u]+1;q.append(v)
    assert np.min(D)>=0
    return D


def odd_graph():
    v=[sum(1<<i for i in c) for c in combinations(range(7),3)]
    edges=[(a,b) for i,a in enumerate(v) for b in v[i+1:] if not a&b]
    D=graph_distances(v,edges)
    for i,a in enumerate(v):
        for j,b in enumerate(v):
            intersection=(a&b).bit_count()
            expected=min(2*(3-intersection),2*intersection+1)
            assert int(D[i,j])==expected
    assert len(v)==35 and max(D.flat)==3
    return D


def folded_graph():
    # Representatives have seventh binary coordinate zero.
    v=list(range(64))
    edges=[(a,b) for i,a in enumerate(v) for b in v[i+1:] if ((a^b).bit_count() in (1,6))]
    D=graph_distances(v,edges)
    for a in v:
        for b in v:
            h=(a^b).bit_count()
            assert D[a,b]==min(h,7-h)
    assert len(v)==64 and max(D.flat)==3
    return D


def claimed_odd(p):
    a=2**p;b=3**p
    return sorted([4+12*a+18*b]+[5*a-3*b-3]*6+[2-3*b]*14+[3*b-3*a-1]*14)


def claimed_folded(p):
    a=2**p;b=3**p
    return sorted([7+21*a+35*b]+[3+a-5*b]*21+[-1-3*a+3*b]*35+[-5+9*a-5*b]*7)


def alpha():
    lo,hi=0.0,2/3
    for _ in range(90):
        mid=(lo+hi)/2
        if 3*(3**mid-2**mid)<1:lo=mid
        else:hi=mid
    return (lo+hi)/2


def universal_radial_coincidence():
    # Independent exact sums: Johnson top eigenvalue versus folded-cube middle-Walsh.
    for k in range(2,26):
        n=2*k+1; j=k+(k%2)
        odd={t:0 for t in range(1,k+1)}
        for i in range(1,k+1):
            t=min(2*i,2*(k-i)+1)
            odd[t]+=(-1)**i*comb(k,i)
        fold={t:0 for t in range(1,k+1)}
        for t in range(1,k+1):
            fold[t]=sum((-1)**s*comb(j,s)*comb(n-j,t-s)
                        for s in range(max(0,t-(n-j)),min(j,t)+1))
        assert odd==fold,(k,odd,fold)
    return 24


def main():
    coincident=universal_radial_coincidence()
    D1=odd_graph(); D2=folded_graph()
    a=alpha(); assert .5165<a<.5167
    passes=0
    for p in (0.0,.1,.25,a,.6,2/3,1.0,1.5):
        for D,expected in ((D1,claimed_odd),(D2,claimed_folded)):
            mat=np.where(D==0,0.0,D.astype(float)**p)
            # Full matrices, without using the closed-form distance-shell eigenvectors.
            actual=sorted(np.linalg.eigvalsh(mat).tolist())
            rhs=expected(p)
            assert np.allclose(actual,rhs,rtol=5e-10,atol=5e-10),(p,D.shape,max(abs(x-y) for x,y in zip(actual,rhs)))
            passes+=1
    # Only the shared critical sector approaches zero at the root.
    for D,nullity in ((D1,14),(D2,35)):
        mat=np.where(D==0,0.0,D.astype(float)**a)
        eig=np.linalg.eigvalsh(mat)
        assert np.count_nonzero(np.abs(eig)<1e-8)==nullity
        assert np.count_nonzero(eig>1e-8)==1
        assert np.count_nonzero(eig < -1e-8)==len(D)-1-nullity
        passes+=1
    print('SUCCESS: 24 all-shell universal coefficient identities, BFS graph distances, 16 full-matrix spectrum matches, 2 endpoint nullity checks')
    print('alpha=',format(a,'.15g'),'odd_rank=20 folded_rank=28, checks=',passes)

if __name__=='__main__':main()
