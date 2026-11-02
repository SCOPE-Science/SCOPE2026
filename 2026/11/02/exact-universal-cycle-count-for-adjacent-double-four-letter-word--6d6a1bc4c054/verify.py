#!/usr/bin/env python3
"""Standalone exact finite checks for adjacent-double universal-cycle enumeration."""
from collections import Counter, defaultdict
from itertools import product
from math import factorial


def language(q):
    return sorted((a, b, c, d) for a, b, c, d in product(range(q), repeat=4)
                  if len({a,b,c,d}) == 3 and
                  ((a==b)+(b==c)+(c==d)) == 1)


def full_overlap(q):
    edges = language(q)
    vertices = sorted({e[:3] for e in edges} | {e[1:] for e in edges})
    pos = {v:i for i,v in enumerate(vertices)}
    adj = [[0]*len(vertices) for _ in vertices]
    for w in edges: adj[pos[w[:3]]][pos[w[1:]]] += 1
    return vertices, adj


def reduced_overlap(q):
    verts = [(phase,a,b) for phase in (0,1) for a in range(q) for b in range(q) if a!=b]
    pos={v:i for i,v in enumerate(verts)}
    adj=[[0]*len(verts) for _ in verts]
    for phase,a,b in verts:
        for c in range(q):
            if c not in (a,b): adj[pos[(phase,a,b)]][pos[(1-phase,b,c)]]+=1
    return verts,adj


def determinant_bareiss(A):
    A=[row[:] for row in A]
    n=len(A); sign=1; prev=1
    if not n: return 1
    for k in range(n-1):
        if A[k][k]==0:
            for j in range(k+1,n):
                if A[j][k]: A[k],A[j]=A[j],A[k];sign=-sign;break
            else: return 0
        pivot=A[k][k]
        for i in range(k+1,n):
            v=A[i][k]
            for j in range(k+1,n):
                val=A[i][j]*pivot-v*A[k][j]
                assert val%prev==0
                A[i][j]=val//prev
            A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]


def cofactor(adj):
    n=len(adj)
    L=[[((sum(adj[i]) if i==j else 0)-adj[i][j]) for j in range(n)] for i in range(n)]
    return determinant_bareiss([row[1:] for row in L[1:]])


def tau_formula(q):
    if q==3: return 0
    return q**(q-2)*(q-2)**(3*q-2)*(q-3)**(q*q-3*q+1)*(q-1)**(q*q-3*q)


def universal_formula(q):
    return tau_formula(q) * factorial(q-3)**(2*q*(q-1))


def components(adj):
    n=len(adj); unseen=set(range(n)); sizes=[]
    while unseen:
        root=unseen.pop(); stack=[root]; size=0
        while stack:
            i=stack.pop(); size+=1
            for j in range(n):
                if adj[i][j] or adj[j][i]:
                    if j in unseen: unseen.remove(j); stack.append(j)
        sizes.append(size)
    return sorted(sizes)


def witness(q):
    # Hierholzer; the list of explicit edge labels prevents any ambiguous identical edge.
    words=language(q); E=defaultdict(list)
    for w in words: E[w[:3]].append(w)
    root=words[0][:3]; stack=[(root,None)]; tour=[]
    while stack:
        v,_=stack[-1]
        if E[v]:
            w=E[v].pop()
            stack.append((w[1:],w))
        else:
            _,e=stack.pop()
            if e is not None: tour.append(e)
    tour.reverse()
    if len(tour)!=len(words): return None
    seq=tuple(w[0] for w in tour)
    seen=Counter(tuple(seq[(i+j)%len(seq)] for j in range(4)) for i in range(len(seq)))
    assert seen==Counter(words)
    return seq


def run():
    for q in (3,4,5):
        fullv,full=full_overlap(q)
        rv,red=reduced_overlap(q)
        assert len(language(q))==3*q*(q-1)*(q-2)
        assert sorted(set(sum(row) for row in full)) == ([1] if q==3 else [1,q-2])
        assert all(sum(full[i])==sum(row[i] for row in full) for i in range(len(full)))
        assert components(full)==([9,9] if q==3 else [len(fullv)])
        assert cofactor(red)==tau_formula(q), (q,'reduced')
        assert cofactor(full)==tau_formula(q), (q,'full')
        print('graph',q, 'edges',len(language(q)), 'vertices',len(fullv),
              'cofactor',tau_formula(q), 'universal_cycles', universal_formula(q))
    for q in (4,5,6,7):
        seq=witness(q)
        assert seq is not None
        assert len(seq)==3*q*(q-1)*(q-2)
        print('witness',q,'length',len(seq),'prefix', ''.join(map(str,seq[:min(32,len(seq))])))
    print('VERIFY_OK')

if __name__=='__main__': run()
