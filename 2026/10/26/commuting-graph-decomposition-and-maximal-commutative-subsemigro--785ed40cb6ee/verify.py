#!/usr/bin/env python3
"""Independent small-rank checks for free left-legal semigroup commutation."""
import itertools
from collections import Counter, deque
from math import factorial
from fractions import Fraction

def falling(n,r):
    x=1
    for a in range(r): x*=n-a
    return x

def B(m): return sum(falling(m,j) for j in range(m+1))
def C(m): return sum((2*j+1)*falling(m,j) for j in range(m+1))

def words(n):
    arr=list(range(n)); out=[]
    for k in range(1,n+1):
        for w in itertools.permutations(arr,k):
            out.append(w)
            out.append((w[0],)+w)
    return out

def normalize(w):
    seen=set(); unique=[]
    for a in w:
        if a not in seen: seen.add(a); unique.append(a)
    if len(w)>=2 and w[0]==w[1]: return (w[0],)+tuple(unique)
    return tuple(unique)

def multiply(a,b): return normalize(a+b)

def components(adjacency):
    rest=set(range(len(adjacency))); blocks=[]
    while rest:
        root=min(rest); todo=[root]; rest.remove(root); comp={root}
        while todo:
            for x in adjacency[todo.pop()]:
                if x in rest: rest.remove(x); comp.add(x); todo.append(x)
        blocks.append(comp)
    return blocks

def bron_kerbosch_count(adj):
    # Maximal cliques, optimized by recursion in sparse graph
    result=Counter()
    def recur(R,P,X):
        if not P and not X:
            result[len(R)]+=1
            return
        pivot=max(P|X,key=lambda v:len(P&adj[v]),default=None)
        for v in list(P-(adj[pivot] if pivot is not None else set())):
            recur(R|{v},P&adj[v],X&adj[v]);P.remove(v);X.add(v)
    recur(set(),set(range(len(adj))),set())
    return result

def lap_spec_recursive(m):
    if m==0:return Counter({0:1})
    prev=lap_spec_recursive(m-1); s=Counter({0:1,B(m):1})
    if m>=2:s[1]+=m-1
    for e,v in prev.items():
        if e: s[e+1]+=m*v
    return s

def predicted_lap(n):
    small=lap_spec_recursive(n-2)
    old=lap_spec_recursive(n-1)
    big=Counter({0:1,B(n-1)+1:1})
    for e,v in old.items():
        if e:big[e+1]+=v
    return Counter({e:n*v for e,v in big.items()})+Counter({e:n*(n-1)*v for e,v in small.items()})

def rational_nullity(a):
    if not a: return 0
    m=len(a); b=[[Fraction(v) for v in row] for row in a]; pivot=0
    for j in range(m):
        r=next((i for i in range(pivot,m) if b[i][j]),None)
        if r is None: continue
        b[pivot],b[r]=b[r],b[pivot]
        scale=b[pivot][j]
        for k in range(j,m): b[pivot][k]/=scale
        for i in range(pivot+1,m):
            t=b[i][j]
            if t:
                for k in range(j,m):b[i][k]-=t*b[pivot][k]
        pivot+=1
        if pivot==m:break
    return m-pivot

def run():
    for n in range(2,5):
        ws=words(n); m=len(ws)
        assert len(set(ws))==m==2*n*B(n-1)
        adj=[set() for _ in ws]; pair_count=m
        for i,x in enumerate(ws):
            assert multiply(x,x)==(x if len(x)>1 else (x[0],x[0]))
            for j in range(i+1,m):
                y=ws[j]
                if multiply(x,y)==multiply(y,x):
                    adj[i].add(j);adj[j].add(i);pair_count+=2
        predicted=n*(C(n-1)+2*B(n-1)+1)+n*(n-1)*C(n-2)
        assert pair_count==predicted,(n,pair_count,predicted)
        blocks=components(adj)
        sizes=Counter(map(len,blocks))
        expected=Counter()
        expected[1+B(n-1)]+=n
        expected[B(n-2)]+=n*(n-1)
        assert sizes==expected,(n,sizes,expected)
        cliques=bron_kerbosch_count(adj)
        expected_cliques=Counter({n+1:factorial(n),n-1:factorial(n)})
        assert cliques==expected_cliques,(n,cliques,expected_cliques)
        lap=predicted_lap(n)
        assert sum(lap.values())==m and lap[0]==n*n
        if n<=4:
            # Exact rational nullities; the Laplacian is symmetric and diagonalizable.
            empirical=Counter()
            for block in blocks:
                subset=sorted(block); ids={v:j for j,v in enumerate(subset)}
                mat=[]
                for v in subset:
                    row=[0]*len(subset); row[ids[v]]=len(adj[v])
                    for u in adj[v]:row[ids[u]]-=1
                    mat.append(row)
                for e in lap:
                    shifted=[[v-(e if i==j else 0) for j,v in enumerate(row)] for i,row in enumerate(mat)]
                    empirical[e]+=rational_nullity(shifted)
            assert empirical==lap,(n,empirical,lap)
        print('VERIFY_OK', 'rank',n,'elements',m,'components',len(blocks), 'ordered_commuting_pairs',pair_count,'maximal_cliques',dict(sorted(cliques.items())), 'laplacian_spectrum',dict(sorted(lap.items())))
if __name__=='__main__': run()
