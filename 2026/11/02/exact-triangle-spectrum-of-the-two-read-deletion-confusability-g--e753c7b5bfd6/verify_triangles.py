#!/usr/bin/env python3
"""Standalone exact enumerator for 2-read deletion confusability triangles."""
from itertools import product, combinations

def one_deletions(w):
    return {w[:i] + w[i+1:] for i in range(len(w))}

def direct_edges(q,n):
    words = list(product(range(q), repeat=n))
    dels = [one_deletions(w) for w in words]
    return {(i,j) for i in range(len(words)) for j in range(i+1,len(words))
            if len(dels[i] & dels[j]) >= 2}

def alternating_edges(q,n):
    words=list(product(range(q),repeat=n))
    index={w:i for i,w in enumerate(words)}
    edges=set()
    for i,w in enumerate(words):
        for lo in range(n-1):
            other=w[lo+1]
            a=w[lo]
            if a==other: continue
            for hi in range(lo+1,n):
                if w[hi] != (a if (hi-lo)%2==0 else other): break
                v=w[:lo]+tuple(other if (t-lo)%2==0 else a for t in range(lo,hi+1))+w[hi+1:]
                j=index[v]
                edges.add((min(i,j),max(i,j)))
    return edges,words

def triangle_count(q,n,verify_structure=False):
    e,W=alternating_edges(q,n)
    A=[set() for w in W]
    for i,j in e:A[i].add(j);A[j].add(i)
    actual=0;bad=0
    for i,neighbors in enumerate(A):
        for j in neighbors:
            if j<=i: continue
            for k in (neighbors & A[j]):
                if k<=j:continue
                actual+=1
                if verify_structure:
                    P=[W[i],W[j],W[k]]
                    intervals=[]
                    for s,t in combinations(range(3),2):
                        delta=[a for a in range(n) if P[s][a]!=P[t][a]]
                        assert len(delta)>=2 and delta==list(range(delta[0],delta[-1]+1))
                        intervals.append((delta[0],delta[-1],s,t))
                    big=max(intervals,key=lambda s:s[1]-s[0]); rest=[p for p in intervals if p!=big]
                    if not(set(range(big[0],big[1]+1))==set(range(rest[0][0],rest[0][1]+1))|set(range(rest[1][0],rest[1][1]+1)) and rest[0][1]<rest[1][0] or rest[1][1]<rest[0][0]):
                        bad+=1
    expected = q*(q-1)*sum((n-L+1)*(L-3)*q**(n-L) for L in range(4,n+1))
    assert actual == expected,(q,n,actual,expected)
    assert bad==0,(q,n,bad)
    return len(W),len(e),actual

if __name__=='__main__':
    direct_cases=0; triangle_cases=0
    for q,max_n in [(2,8),(3,6),(4,5)]:
        for n in range(1,max_n+1):
            E,W=alternating_edges(q,n)
            if n<=({2:7,3:5,4:4}[q]):
                D=direct_edges(q,n)
                assert E==D,(q,n,len(E),len(D),list(E^D)[:5]);direct_cases+=1
            W_size,edge_count,triangles=triangle_count(q,n,verify_structure=True)
            triangle_cases+=1
            print(f'q={q} n={n} words={W_size} edges={edge_count} triangles={triangles}')
    print(f'VERIFY_OK direct_edge_cases={direct_cases} triangle_structural_cases={triangle_cases}')
