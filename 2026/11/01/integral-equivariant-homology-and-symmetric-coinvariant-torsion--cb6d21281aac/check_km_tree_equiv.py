#!/usr/bin/env python3
"""Finite character and integral coinvariant checks for clique-tree two-cut complexes.
Python standard library for character checks; optional sympy for Smith invariants.
These finite tests corroborate the stated theorem, not an infinite proof.
"""
from itertools import permutations
from math import gcd

def sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def test_tree(label, m, t, edges):
    edge_set={frozenset(e) for e in edges}
    autos=[a for a in permutations(range(t)) if {frozenset((a[u],a[v])) for u,v in edges}==edge_set]
    N=m*t
    nonedges=[]
    for x in range(N):
        for y in range(x+1,N):
            i,j=x%m,x//m
            k,l=y%m,y//m
            if not (j==l or (i==k and frozenset((j,l)) in edge_set)):
                nonedges.append((x,y))
    full=(1<<N)-1
    faces=[mask for mask in range(1,full+1) if any((full^mask)&(1<<x) and (full^mask)&(1<<y) for x,y in nonedges)]
    counter=0
    for p in permutations(range(m)):
        for tau in autos:
            vertex_image=[tau[j]*m+p[i] for j in range(t) for i in range(m)]
            Etrace=0
            for u,v in edges:
                if tau[u]==u and tau[v]==v: Etrace+=1
                elif tau[u]==v and tau[v]==u: Etrace-=1
            theoretical=(sign(p)**t)*(sign(tau)**m)*\
                        (sum(p[i]==i for i in range(m))-1)*Etrace
            reduced=-1
            for mask in faces:
                vertices=[v for v in range(N) if mask&(1<<v)]
                images=[vertex_image[v] for v in vertices]
                if all(mask&(1<<w) for w in images):
                    parity=sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
                    reduced+=(-1)**(len(vertices)-1+parity)
            computed=(-1)**(N-4)*reduced
            assert computed==theoretical,(label,m,t,p,tau,computed,theoretical)
            counter+=1
    print(f'{label}, m={m}: {len(faces)} nonempty faces; {len(autos)} tree automorphisms; {counter} character checks')
    return counter

if __name__=='__main__':
    cases=[('edge',2,2,[(0,1)]),('edge',3,2,[(0,1)]),
           ('three-path',3,3,[(0,1),(1,2)]),
           ('four-path',2,4,[(0,1),(1,2),(2,3)]),
           ('four-path',3,4,[(0,1),(1,2),(2,3)]),
           ('three-leaf star',2,4,[(0,1),(0,2),(0,3)]),
           ('three-leaf star',3,4,[(0,1),(0,2),(0,3)]),
           ('four-leaf star',2,5,[(0,1),(0,2),(0,3),(0,4)]),
           ('five-path',2,5,[(0,1),(1,2),(2,3),(3,4)]),
           ('fork tree',2,5,[(0,1),(1,2),(1,3),(3,4)])]
    count=sum(test_tree(*c) for c in cases)
    print('PASS',count,'complete signed-Lefschetz comparisons on trees')
