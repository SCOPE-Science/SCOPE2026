#!/usr/bin/env python3
from itertools import combinations
from collections import deque


def connected_bipartition(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    if any(len(adj[v])==0 for v in range(n)):
        return None, adj
    color=[None]*n
    color[0]=0; q=deque([0]); seen=1
    while q:
        v=q.popleft()
        for w in adj[v]:
            if color[w] is None:
                color[w]=1-color[v]; seen+=1; q.append(w)
            elif color[w]==color[v]:
                return None, adj
    if seen<n: return None, adj
    X={i for i,c in enumerate(color) if c==0}; Y=set(range(n))-X
    return (X,Y), adj

def square_free(adj):
    n=len(adj)
    for a,b in combinations(range(n),2):
        if len(adj[a] & adj[b])>=2:
            # two common neighbors create a 4-cycle; in a simple bipartite graph a,b are same side
            return False
    return True

def all_faces(facets):
    out=set()
    for F in facets:
        F=sorted(F)
        for k in range(1,len(F)+1):
            for s in combinations(F,k): out.add(frozenset(s))
    return out

def collapse_component(vertices, opposite, adj):
    facets={y:frozenset(adj[y] & vertices) for y in opposite}
    faces=all_faces(facets.values())
    initial=set(faces)
    roots={y:min(facets[y]) for y in opposite}
    steps=[]
    # every face of size >=2 belongs to a unique facet in a square-free bipartite graph
    for y in sorted(opposite):
        F=facets[y]; r=roots[y]
        others=sorted(F-{r})
        for k in range(len(others),1,-1):
            for tup in combinations(others,k):
                sigma=frozenset(tup); tau=frozenset(set(tup)|{r})
                if sigma not in faces or tau not in faces:
                    raise AssertionError(('missing pair',y,sigma,tau))
                # tau maximal now and sigma has exactly one strict coface, tau
                cofaces=[f for f in faces if sigma < f]
                if cofaces != [tau] and set(cofaces)!={tau}:
                    raise AssertionError(('not free',y,sigma,tau,cofaces[:10]))
                if any(tau < f for f in faces):
                    raise AssertionError(('tau not maximal',y,tau))
                faces.remove(sigma); faces.remove(tau); steps.append((sigma,tau))
    expected={frozenset({v}) for v in vertices}
    for y,F in facets.items():
        r=roots[y]
        for v in F-{r}: expected.add(frozenset({r,v}))
    if faces!=expected:
        raise AssertionError(('wrong spine',faces^expected))
    # compare graph ranks: spine T is obtained from G by contracting selected y-root edges
    E_T=sum(1 for f in faces if len(f)==2); V_T=len(vertices)
    E_G=sum(len(adj[y]) for y in opposite); V_G=len(vertices)+len(opposite)
    rank_T=E_T-V_T+1; rank_G=E_G-V_G+1
    if rank_T!=rank_G:
        raise AssertionError(('rank mismatch',rank_T,rank_G))
    return len(initial),len(steps),V_T,E_T,rank_G

def exhaustive(max_n=6):
    total=0; examples=[]
    for n in range(2,max_n+1):
        pairs=list(combinations(range(n),2))
        for mask in range(1,1<<len(pairs)):
            edges=[pairs[i] for i in range(len(pairs)) if mask>>i & 1]
            part,adj=connected_bipartition(n,edges)
            if part is None or not square_free(adj): continue
            X,Y=part
            a=collapse_component(X,Y,adj)
            b=collapse_component(Y,X,adj)
            total+=1
            if len(examples)<8: examples.append((n,tuple(edges),a,b))
    return total,examples

if __name__=='__main__':
    total,examples=exhaustive(6)
    print('EXHAUSTIVE_OK',total,'connected labeled bipartite square-free graphs on 2..6 vertices')
    for e in examples: print('EXAMPLE',e)
