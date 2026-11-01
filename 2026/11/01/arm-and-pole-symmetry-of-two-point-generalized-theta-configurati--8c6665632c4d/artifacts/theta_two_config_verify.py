#!/usr/bin/env python3
"""Finite cellular checks for unordered two-point configurations on multi-theta graphs.
Run: python3 theta_two_config_verify.py. Only the Python standard library is needed.
"""
from itertools import combinations, permutations
from collections import defaultdict, deque
from math import comb


def build(m):
    vertices = tuple(range(2 * m + 2))
    edges = []
    labels = []
    for i in range(m):
        ai, bi = 2 + 2*i, 3 + 2*i
        edges += [(0, ai), (ai, bi), (1, bi)]
        labels += [("A", i), ("B", i), ("C", i)]
    edge_index = {label: i for i, label in enumerate(labels)}
    zero = list(combinations(vertices, 2))
    one = [(v, ei) for v in vertices for ei, e in enumerate(edges) if v not in e]
    two = [(ei, fi) for ei, fi in combinations(range(len(edges)), 2)
           if set(edges[ei]).isdisjoint(edges[fi])]
    one_index = {a:i for i,a in enumerate(one)}
    boundary2 = []
    incident = defaultdict(set)
    for idx, (ei, fi) in enumerate(two):
        e, f = edges[ei], edges[fi]
        bd = [(one_index[(e[0],fi)], -1), (one_index[(e[1],fi)],1),
              (one_index[(f[0],ei)], 1), (one_index[(f[1],ei)],-1)]
        boundary2.append(bd)
        for row,sgn in bd:incident[row].add(idx)
        # independently check boundary^2 = 0
        zbd=defaultdict(int)
        for row,sgn in bd:
            vert,edge_idx=one[row]
            x,y=edges[edge_idx]
            zbd[tuple(sorted((vert,x)))] -= sgn
            zbd[tuple(sorted((vert,y)))] += sgn
        assert all(n==0 for n in zbd.values())
    return vertices,edges,edge_index,zero,one,two,boundary2,incident


def verify_collapse(m, c):
    vertices,edges,edge_index,zero,one,two,boundary2,incident = c
    e = lambda typ,i:edge_index[(typ,i)]
    sq_index={pair:i for i,pair in enumerate(two)}
    remaining=set(range(len(two))); matched_one=set()
    def remove(ei,fi,free_cell):
        square=sq_index[tuple(sorted((ei,fi)))]
        row=one.index(free_cell)
        assert square in remaining and row not in matched_one
        assert incident[row] & remaining == {square}, (m,ei,fi,free_cell,incident[row]&remaining)
        matched_one.add(row); remaining.remove(square)
    # First stage has free edges even before any collapse.
    for i in range(m):
        remove(e('A',i),e('C',i),(2+2*i,e('C',i)))
    for i in range(m):
        for j in range(m):
            if i!=j:
                remove(e('A',i),e('B',j),(2+2*j,e('A',i)))
                remove(e('B',i),e('C',j),(3+2*i,e('C',j)))
    # After the first stage, each remaining square has its indicated free edge.
    for i in range(m):
        for j in range(m):
            if i!=j:
                remove(e('A',i),e('C',j),(2+2*i,e('C',j)))
    for i in range(m):
        for j in range(i+1,m):
            remove(e('B',i),e('B',j),(2+2*i,e('B',j)))
    assert not remaining
    assert len(matched_one)==len(two)


def verify_connected(m,c):
    vertices,edges,_,zero,one,_,_,_=c
    z_index={a:i for i,a in enumerate(zero)}
    nbr=[[] for _ in zero]
    for v,ei in one:
        x,y=edges[ei]
        a,b=tuple(sorted((v,x))),tuple(sorted((v,y)))
        nbr[z_index[a]].append(z_index[b]);nbr[z_index[b]].append(z_index[a])
    seen={z_index[(0,1)]}; queue=deque(seen)
    while queue:
        x=queue.popleft()
        for y in nbr[x]:
            if y not in seen:seen.add(y);queue.append(y)
    assert len(seen)==len(zero)


def trace(m,c,perm,swap):
    vertices,edges,_,zero,one,two,_,_=c
    def map_vertex(v):
        if v<=1:return 1-v if swap else v
        i,k=divmod(v-2,2)
        return 2+2*perm[i]+(1-k if swap else k)
    edge_map=[]
    lookup={frozenset(e):i for i,e in enumerate(edges)}
    for x,y in edges:
        a,b=map_vertex(x),map_vertex(y)
        idx=lookup[frozenset((a,b))]
        sign=1 if edges[idx]==(a,b) else -1
        edge_map.append((idx,sign))
    tr0=sum(tuple(sorted(map(map_vertex,z)))==z for z in zero)
    tr1=sum(sign for v,ei in one for idx,sign in [edge_map[ei]]
            if map_vertex(v)==v and ei==idx)
    tr2=0
    for ei,fi in two:
        a,sa=edge_map[ei];b,sb=edge_map[fi]
        if (a,b)==(ei,fi):tr2+=sa*sb
        elif (a,b)==(fi,ei):tr2-=sa*sb
    return 1-tr0+tr1-tr2, (tr0,tr1,tr2)


def cycles(perm):
    n=len(perm); seen=set(); lengths=[]
    for i in range(n):
        if i not in seen:
            x=i;l=0
            while x not in seen:seen.add(x);l+=1;x=perm[x]
            lengths.append(l)
    return lengths


def partition_reps(n):
    def partitions(rem,low=1):
        if not rem:
            yield []
        else:
            for x in range(low,rem+1):
                for rest in partitions(rem-x,x): yield [x]+rest
    for lens in partitions(n):
        perm=list(range(n));pos=0
        for k in lens:
            for j in range(k):perm[pos+j]=pos+(j+1)%k
            pos+=k
        yield tuple(perm)


def verify(m,all_perms):
    c=build(m)
    V,E,_,z,o,t,_,_=c
    assert len(z)==comb(2*m+2,2)
    assert len(o)==6*m*m
    assert len(t)==(7*m*m-5*m)//2
    verify_collapse(m,c);verify_connected(m,c)
    assert len(z)-len(o)+len(t)==1-comb(m,2)
    reps=permutations(range(m)) if all_perms else partition_reps(m)
    count=0
    for perm in reps:
        lens=cycles(perm)
        f=lens.count(1); twos=lens.count(2)
        for eps in (False,True):
            value,cell_traces=trace(m,c,perm,eps)
            expected=(-1 if eps else 1)*(comb(f,2)-twos)
            assert value==expected, (m,perm,eps,value,expected,cell_traces)
            count+=1
    print('m=%d cells=(%d,%d,%d) 2-cell collapses=%d H1_rank=%d automorphism_checks=%d OK' %
          (m,len(z),len(o),len(t),len(t),comb(m,2),count))

if __name__=='__main__':
    for m in range(3,8):verify(m,True)
    for m in (8,9,10):verify(m,False)
    print('VERIFY_OK')
