#!/usr/bin/env python3
"""Standard-library exact rational checks for tree-chord price certificates.
Finite checks do not prove the universal theorem; see the proof in RESULT.md.
"""
from fractions import Fraction as F
from collections import deque
from itertools import combinations
from random import Random


def inverse(mat):
    n=len(mat)
    M=[[F(v) for v in row]+[F(i==j) for j in range(n)] for i,row in enumerate(mat)]
    for j in range(n):
        p=next(k for k in range(j,n) if M[k][j])
        M[j],M[p]=M[p],M[j]
        z=M[j][j]; M[j]=[v/z for v in M[j]]
        for k in range(n):
            if k!=j:
                z=M[k][j]
                M[k]=[v-z*w for v,w in zip(M[k],M[j])]
    return [row[n:] for row in M]


def tree_from_prufer(n,seq):
    degree=[1]*n
    for x in seq: degree[x]+=1
    result=[]
    for x in seq:
        y=next(k for k in range(n) if degree[k]==1)
        result.append((min(x,y),max(x,y)))
        degree[x]-=1;degree[y]-=1
    last=[i for i in range(n) if degree[i]==1]
    result.append(tuple(sorted(last)))
    return sorted(result)


def side(n,edges,edge,u):
    adj=[[] for _ in range(n)]
    for a,b in edges:
        if (a,b)!=edge:
            adj[a].append(b);adj[b].append(a)
    seen={u};q=deque([u])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if y not in seen: seen.add(y);q.append(y)
    return seen


def path(n,edges,u,v):
    adj=[[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b);adj[b].append(a)
    prev={u:None};q=deque([u])
    while q and v not in prev:
        x=q.popleft()
        for y in adj[x]:
            if y not in prev: prev[y]=x;q.append(y)
    out=[];x=v
    while x!=u:
        y=prev[x];out.append(tuple(sorted((x,y))));x=y
    return out[::-1]


def pinv(n,edgeweights):
    L=[[F(0) for j in range(n)] for i in range(n)]
    for (u,v),g in edgeweights.items():
        L[u][u]+=g;L[v][v]+=g;L[u][v]-=g;L[v][u]-=g
    Y=inverse([[L[i][j]+F(1,n) for j in range(n)] for i in range(n)])
    P=[[Y[i][j]-F(1,n) for j in range(n)] for i in range(n)]
    return sum(P[i][i] for i in range(n)),P


def marginal(P,u,v):
    return sum((P[k][u]-P[k][v])**2 for k in range(len(P)))


def checks():
    r=Random(20261014)
    tests=0
    for n in range(4,9):
        trees=[sorted((i,i+1) for i in range(n-1)),
               sorted((0,i) for i in range(1,n))]
        trees += [tree_from_prufer(n,[r.randrange(n) for _ in range(n-2)]) for _ in range(8)]
        for edges in trees:
            tree_set=set(edges)
            k={e:1+r.randrange(4) for e in edges}
            b={e: len(side(n,edges,e,e[0]))*(n-len(side(n,edges,e,e[0]))) for e in edges}
            price={e:F(b[e]*k[e]**2) for e in edges}
            B=sum(b[e]*k[e] for e in edges)
            base={e:F(1,k[e]) for e in edges}
            assert sum(price[e]*base[e] for e in edges)==B
            J,P=pinv(n,base)
            assert J==F(B,n)
            for u,v in edges:
                assert marginal(P,u,v)==F(price[(u,v)],n)
                tests+=1
            for u,v in combinations(range(n),2):
                if (u,v) in tree_set:continue
                es=path(n,edges,u,v)
                s=[len(side(n,edges,e,u)) for e in es]
                assert s==sorted(s)
                T=sum(F(min(s[i],s[j])*(n-max(s[i],s[j]))*k[es[i]]*k[es[j]])
                      for i in range(len(es)) for j in range(len(es)))
                # Exact complete-matrix gradient equals the path-cut certificate.
                assert marginal(P,u,v)==T/n,(n,edges,u,v,T)
                # A candidate chord priced strictly below T strictly improves J.
                cheap=T-F(1,10)
                delta=F(1,10000*(1+int(T)))
                scale=1-cheap*delta/B
                weights={e:base[e]*scale for e in edges}
                weights[(u,v)]=delta
                assert sum(price[e]*weights[e] for e in edges)+cheap*delta==B
                new_J,_=pinv(n,weights)
                assert new_J < J,(n,edges,u,v,J,new_J)
                tests+=3
    return tests

if __name__=='__main__':
    print('VERIFY_OK exact_rational_assertions=',checks())
