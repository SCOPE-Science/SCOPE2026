#!/usr/bin/env python3
"""Exact rational checks for functional-network opinion intervention theorem."""
from collections import deque
from fractions import Fraction as F
from itertools import product, combinations
import random


def exact_centralities(succ, q, attention):
    """Compute v=(I-Q^T)^(-1) attention by leaf peeling and cycle closure."""
    n = len(succ)
    assert n == len(q) == len(attention)
    indeg = [0]*n
    h = list(attention)
    for i, j in enumerate(succ):
        assert (j == -1 and q[i] == 0) or (j != -1 and j != i and 0 <= q[i] < 1)
        if j >= 0: indeg[j] += 1
    que = deque(i for i in range(n) if indeg[i] == 0)
    val = [None]*n
    processed = [False]*n
    while que:
        i = que.popleft()
        val[i] = h[i]
        processed[i] = True
        j = succ[i]
        if j >= 0:
            h[j] += q[i]*val[i]
            indeg[j] -= 1
            if indeg[j] == 0: que.append(j)
    for start in range(n):
        if processed[start]: continue
        cyc = [start]
        cur = succ[start]
        while cur != start:
            assert not processed[cur]
            cyc.append(cur)
            cur = succ[cur]
        length = len(cyc)
        assert length >= 2
        numer = h[start]
        mult = F(1)
        for t in range(1, length):
            j = cyc[-t]
            mult *= q[j]
            numer += mult*h[j]
        prod = mult*q[cyc[0]]
        assert prod < 1
        val[start] = numer/(1-prod)
        for t in range(1, length):
            j, prev = cyc[t], cyc[t-1]
            val[j] = h[j]+q[prev]*val[prev]
        for j in cyc: processed[j] = True
    assert all(x is not None for x in val)
    return val


def gaussian(A,b):
    n=len(b)
    mat=[list(A[i])+[b[i]] for i in range(n)]
    for col in range(n):
        pivot=next((r for r in range(col,n) if mat[r][col]!=0),None)
        assert pivot is not None
        mat[col],mat[pivot]=mat[pivot],mat[col]
        z=mat[col][col]
        for j in range(col,n+1): mat[col][j]/=z
        for row in range(n):
            if row==col: continue
            z=mat[row][col]
            if z:
                for j in range(col,n+1): mat[row][j]-=z*mat[col][j]
    return [mat[i][n] for i in range(n)]


def baseline(succ,q,a):
    n=len(succ)
    A=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for j,k in enumerate(succ):
        if k>=0: A[k][j]-=q[j]
    return gaussian(A,a)


def direct_equilibrium(succ,q,s):
    n=len(succ)
    A=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for i,j in enumerate(succ):
        if j>=0: A[i][j]-=q[i]
    return gaussian(A,[(1-q[i])*s[i] for i in range(n)])


def choose_scores(succ,q,a,s,k):
    v=exact_centralities(succ,q,a)
    benefit=[(1-q[i])*v[i]*s[i] for i in range(len(succ))]
    return tuple(sorted(range(len(succ)),key=lambda i:(-benefit[i],i))[:k]),benefit


def failure_family(L):
    succ=[]
    # Full ternary in-tree, vertices appended breadth-first, root index 0.
    succ.append(-2)
    nodes=[0]
    for depth in range(L):
        new=[]
        for u in nodes:
            for t in range(3):
                new.append(len(succ));succ.append(u)
        nodes=new
    y=0
    z_first=len(succ)
    prev=y
    for j in range(2*L):
        z=len(succ);succ.append(-2);succ[prev]=z;prev=z
    x=len(succ);succ.append(-1);succ[prev]=x
    for j in range(4):succ.append(x)
    return succ,y,x


def verify():
    exhaustive=0
    for n in range(1,6):
        choices=[[ -1]+[j for j in range(n) if j!=i] for i in range(n)]
        for tup in product(*choices):
            q=[F(0) if j<0 else F(1,2) for j in tup]
            a=[F(1)]*n
            assert exact_centralities(tup,q,a)==baseline(tup,q,a)
            exhaustive+=1
    rng=random.Random(11831)
    random_tests=0
    optimizations=0
    for n in range(2,10):
        for repeat in range(110):
            choices=[[-1]+[j for j in range(n) if j!=i] for i in range(n)]
            succ=[rng.choice(choices[i]) for i in range(n)]
            q=[F(0) if j==-1 else rng.choice([F(0),F(1,7),F(1,3),F(1,2),F(3,4),F(7,8)]) for j in succ]
            a=[F(rng.randrange(0,5)) for _ in range(n)]
            if sum(a)==0:a[0]=F(1)
            s=[F(rng.randrange(0,9),8) for _ in range(n)]
            v=exact_centralities(succ,q,a)
            assert v==baseline(succ,q,a)
            first=direct_equilibrium(succ,q,s)
            total=sum(ai*zi for ai,zi in zip(a,first))
            assert total==sum(s[i]*(1-q[i])*v[i] for i in range(n))
            k=rng.randrange(1,min(n,4)+1)
            chosen,benefit=choose_scores(succ,q,a,s,k)
            best=sum(benefit[i] for i in chosen)
            assert best==max(sum(benefit[i] for i in T) for T in combinations(range(n),k))
            s2=[F(0) if i in chosen else s[i] for i in range(n)]
            after=sum(ai*zi for ai,zi in zip(a,direct_equilibrium(succ,q,s2)))
            assert total-after==best
            random_tests+=1
            optimizations+=1
    results=[]
    for L in range(1,10):
        succ,y,x=failure_family(L)
        n=len(succ)
        q=[F(0) if j==-1 else F(1,2) for j in succ]
        attention=[F(1)]*n
        v=exact_centralities(succ,q,attention)
        indeg=[0]*n
        for j in succ:
            if j>=0:indeg[j]+=1
        assert indeg[x]==5 and all(indeg[i]<=3 for i in range(n) if i!=x)
        vy=3*F(3,2)**L-2
        vx=4-F(1,2)**(2*L)+vy/F(2)**(2*L+1)
        assert v[y]==vy and v[x]==vx
        assert vx<5
        if L<=5: assert v==baseline(succ,q,attention)
        best=max((1-q[i])*v[i] for i in range(n))
        ratio=best/vx
        assert ratio>=vy/(2*vx)
        results.append((L,n,str(vy/2),str(vx),float(ratio)))
    print('EXHAUSTIVE_FUNCTIONAL_GRAPHS',exhaustive)
    print('HETEROGENEOUS_EXACT_TESTS',random_tests)
    print('OPTIMALITY_BRUTE_FORCE_TESTS',optimizations)
    print('UNBOUNDED_FAMILY_TESTS',len(results))
    for r in results: print('FAMILY',*r)
    family_checks=0
    for degree in (3,4,5,6):
        b=degree-1
        for L in range(1,8):
            # Complete b-ary in-tree plus an attenuating directed handle to a sink.
            succ=[-2]; level=[0]
            for depth in range(L):
                nxt=[]
                for parent in level:
                    for _ in range(b):
                        u=len(succ);succ.append(parent);nxt.append(u)
                level=nxt
            y=0
            path_length=L*max(1,(b-1).bit_length())
            old=y
            for _ in range(path_length):
                z=len(succ);succ.append(-2);succ[old]=z;old=z
            hub=len(succ);succ.append(-1);succ[old]=hub
            for _ in range(b):succ.append(hub)
            if len(succ)>60000:break
            q=[F(0) if j<0 else F(1,2) for j in succ]
            v=exact_centralities(succ,q,[F(1)]*len(succ))
            indeg=[0]*len(succ)
            for j in succ:
                if j>=0:indeg[j]+=1
            assert indeg[hub]==degree and all(indeg[i]<degree for i in range(len(succ)) if i!=hub)
            target=sum((F(b,2)**t for t in range(L+1)),F(0))
            assert v[y]==target
            assert v[hub]==1+F(b,2)+F(1,2)*(2*(1-F(1,2)**path_length)+F(1,2)**path_length*target)
            assert v[hub]<=degree+3
            assert max((1-q[i])*v[i] for i in range(len(succ)))>=target/2
            family_checks+=1
    print('BOUNDED_INDEGREE_HIERARCHY_TESTS',family_checks)
    print('ALL_CHECKS_PASS')

if __name__=='__main__':verify()
