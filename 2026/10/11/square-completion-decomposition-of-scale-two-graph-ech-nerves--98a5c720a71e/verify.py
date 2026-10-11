#!/usr/bin/env python3
"""Standalone exact checker for square-completion collapse of closed-neighborhood complexes.

Only standard Python is used. This verifies finite instances; the accompanying
combinatorial argument establishes the statement for all admissible graphs.
"""
import itertools
from collections import defaultdict


def graph_product(a, b, cyclic_a=False, cyclic_b=False):
    verts = list(itertools.product(range(a), range(b)))
    edge_set = set()
    def link(x, y):
        p, q = sorted((x, y))
        edge_set.add((p, q))
    for i in range(a):
        for j in range(b):
            x = i*b+j
            if i+1<a:link(x,(i+1)*b+j)
            if j+1<b:link(x,i*b+j+1)
            if cyclic_a and i==a-1:link(x,j)
            if cyclic_b and j==b-1:link(x,i*b)
    return a*b, sorted(edge_set)


def hypercube(n):
    return 2**n, [(x,x^(1<<i)) for x in range(2**n) for i in range(n) if x<(x^(1<<i))]


def petersen():
    ed=[]
    for i in range(5):
        ed.extend([(i,(i+1)%5),(i,i+5),(i+5,((i+2)%5)+5)])
    return 10, [(min(a,b),max(a,b)) for a,b in ed]


def open_neighborhoods(n, edges):
    nb=[set() for _ in range(n)]
    for a,b in edges:
        assert 0<=a<b<n
        nb[a].add(b);nb[b].add(a)
    return nb


def admissible(n, edges):
    nb=open_neighborhoods(n,edges)
    for a in range(n):
        for b in range(a+1,n):
            if b in nb[a] and nb[a]&nb[b]:return False
            if len(nb[a]&nb[b])>2:return False
    return True


def closure(generators):
    faces=set()
    for s in generators:
        t=sorted(s)
        for k in range(1,len(t)+1):
            faces.update(frozenset(c) for c in itertools.combinations(t,k))
    return faces


def square_sets(n, nb):
    cycles=set()
    for a in range(n):
        for b in range(a+1,n):
            mids=sorted(nb[a]&nb[b])
            if len(mids)==2:
                cycles.add(tuple(sorted((a,b,*mids))))
    return cycles


def target(n, edges, cycles):
    faces=closure([frozenset((i,)) for i in range(n)]+[frozenset(e) for e in edges])
    for s in cycles:
        for triangle in itertools.combinations(s,3):
            faces.update(closure([frozenset(triangle)]))
    return faces


def check_collapse(n, edges, verbose=False):
    assert admissible(n,edges), 'Hypotheses not satisfied'
    nb=open_neighborhoods(n,edges)
    K=closure([frozenset(N|{v}) for v,N in enumerate(nb)])
    current=set(K);pairs1=pairs2=0
    def remove(a,b):
        assert a in current and b in current and a<b and len(b)==len(a)+1, (a,b)
        cofaces=[c for c in current if a<c]
        assert cofaces==[b], (a,b,cofaces)
        current.remove(a);current.remove(b)
    for size in range(max(map(len,nb)),2,-1):
        for v,N in enumerate(nb):
            for nodes in itertools.combinations(sorted(N),size):
                F=frozenset(nodes)
                remove(F,F|{v});pairs1+=1
    for a in range(n):
        for b in range(a+1,n):
            common=nb[a]&nb[b]
            if b not in nb[a] and len(common)==1:
                v=next(iter(common))
                remove(frozenset((a,b)),frozenset((a,b,v)));pairs2+=1
    cycles=square_sets(n,nb)
    expected=target(n,edges,cycles)
    assert current==expected, ('Residual mismatch',len(current),len(expected),len(current-expected),len(expected-current))
    if verbose:
        print('graph',n,len(edges),'squares',len(cycles),'initial_faces',len(K),'collapse_pairs',pairs1,pairs2,'residual_faces',len(current),'mod2_betti',betti_mod2(current))
    return K,current,(pairs1,pairs2),cycles


def mod2_rank(columns):
    pivot={}
    for c in columns:
        while c:
            high=c.bit_length()-1
            if high in pivot: c ^= pivot[high]
            else:
                pivot[high]=c
                break
    return len(pivot)


def betti_mod2(faces):
    by=defaultdict(list)
    for f in faces:by[len(f)-1].append(tuple(sorted(f)))
    dims=sorted(by)
    rank={}
    for d in range(1,max(dims)+1):
        idx={s:i for i,s in enumerate(by[d-1])}
        columns=[sum(1<<idx[s[:i]+s[i+1:]] for i in range(len(s))) for s in by[d]]
        rank[d]=mod2_rank(columns)
    return {d:len(by[d])-rank.get(d,0)-rank.get(d+1,0) for d in dims}


def main():
    scenarios=[('path_grid_3x4',graph_product(3,4)),
               ('square',graph_product(2,2)),
               ('cylinder_5x3',graph_product(5,3,cyclic_a=True)),
               ('torus_5x5',graph_product(5,5,cyclic_a=True,cyclic_b=True)),
               ('cube_3',hypercube(3)), ('cube_4',hypercube(4)),
               ('Petersen',petersen())]
    expected={'path_grid_3x4':{0:1,1:0,2:6},'square':{0:1,1:0,2:1},
              'cylinder_5x3':{0:1,1:1,2:10},'torus_5x5':{0:1,1:2,2:26},
              'cube_3':{0:1,1:0,2:7},'cube_4':{0:1,1:0,2:31},
              'Petersen':{0:1,1:6}}
    for label,(n,edges) in scenarios:
        K,Y,pairs,cycles=check_collapse(n,edges,True)
        got=betti_mod2(Y)
        assert got==expected[label],(label,got,expected[label])
    # Check every graph on <=5 labeled vertices, including disconnected cases.
    counter=0
    for n in range(1,6):
        edge_pool=list(itertools.combinations(range(n),2))
        for mask in range(1<<len(edge_pool)):
            ed=[edge_pool[i] for i in range(len(edge_pool)) if mask>>i&1]
            if admissible(n,ed):check_collapse(n,ed);counter+=1
    print('exact_exhaustive_labeled_graphs',counter)
    assert not admissible(5,[(a,b) for a in (0,1) for b in (2,3,4)])
    print('VERIFY_OK')

if __name__=='__main__':main()
