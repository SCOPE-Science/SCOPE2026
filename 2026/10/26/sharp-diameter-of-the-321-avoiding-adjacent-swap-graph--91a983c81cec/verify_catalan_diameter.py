#!/usr/bin/env python3
"""Finite check of weak-order 321-avoidance distances (not an infinite proof)."""
from itertools import permutations
from collections import deque

def avoids321(p):
    n=len(p)
    for i in range(n):
        for j in range(i+1,n):
            if p[i] > p[j]:
                for k in range(j+1,n):
                    if p[j] > p[k]:
                        return False
    return True

def graph(n):
    vertices=[p for p in permutations(range(1,n+1)) if avoids321(p)]
    at={p:i for i,p in enumerate(vertices)}
    ranks=[sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)) for p in vertices]
    edges=[[] for _ in vertices]
    lower=[[] for _ in vertices]
    for i,p in enumerate(vertices):
        for a in range(n-1):
            q=list(p); q[a],q[a+1]=q[a+1],q[a]
            j=at.get(tuple(q))
            if j is not None:
                edges[i].append(j)
                if ranks[j] < ranks[i]: lower[i].append(j)
    return vertices,at,ranks,edges,lower

def main():
    counts=[1,2,5,14,42,132,429,1430]  # Catalan C_1 ... C_8
    for n in range(1,9):
        V,at,ranks,G,lower=graph(n)
        assert len(V)==counts[n-1]
        masks=[0]*len(V)
        next_bit=0
        for v in sorted(range(len(V)),key=lambda i:ranks[i]):
            bitmask=0
            for p in lower[v]:bitmask |= masks[p]
            if len(lower[v])==1:
                bitmask |= 1<<next_bit
                next_bit += 1
            masks[v]=bitmask
            assert bitmask.bit_count()==ranks[v],(n,V[v],bitmask.bit_count(),ranks[v])
        diameter=0
        for start in range(len(V)):
            distances=[-1]*len(V); distances[start]=0
            todo=deque([start])
            while todo:
                i=todo.popleft()
                for j in G[i]:
                    if distances[j] < 0:
                        distances[j]=distances[i]+1
                        todo.append(j)
            assert min(distances)>=0
            for j,d in enumerate(distances):
                assert d == (masks[start]^masks[j]).bit_count(), (n,V[start],V[j],d)
                diameter=max(diameter,d)
        expected=(n*n)//2-(1 if n%2==0 else 0)
        assert diameter==expected,(n,diameter,expected)
        print(f'n={n} vertices={len(V)} join_irreducibles={next_bit} diameter={diameter}')
    print('VERIFY_OK')
if __name__=='__main__':main()
