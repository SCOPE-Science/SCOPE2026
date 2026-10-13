"""Finite cross-checks for signed-line-graph frustration on vertex-disjoint-cycle cacti.

Python >=3.9, standard library only; run: python verify.py
"""
from itertools import combinations
from random import Random
from collections import defaultdict
from math import prod


def simple_cycles(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    result = set()
    for start in range(n):
        def walk(path, used):
            last = path[-1]
            for v in adj[last]:
                if v == start and len(path) >= 3:
                    forward = tuple(path)
                    reverse = (path[0],) + tuple(reversed(path[1:]))
                    result.add(min(forward, reverse))
                elif v > start and v not in used:
                    walk(path + (v,), used | {v})
        walk((start,), {start})
    return sorted(result)


def connected(n, edges):
    if n == 0: return False
    adj = [set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    seen={0};todo=[0]
    while todo:
        v=todo.pop()
        for w in adj[v] - seen:
            seen.add(w);todo.append(w)
    return len(seen)==n


def graph_formula(n, edges):
    cyc = simple_cycles(n, edges)
    vertices = set()
    for c in cyc:
        if vertices.intersection(c):
            return None
        vertices.update(c)
    deg=[0]*n
    for u,v in edges:
        deg[u]+=1;deg[v]+=1
    result=sum(min(deg[v]-1 for v in c) for c in cyc if len(c)%2)
    return result,cyc,deg


def orientation_minima(n, edges):
    e=len(edges)
    deg=[0]*n
    for u,v in edges:
        deg[u]+=1; deg[v]+=1
    minimum=None; count=0
    for mask in range(1<<e):
        indeg=[0]*n
        for i,(u,v) in enumerate(edges):
            indeg[u if ((mask>>i)&1) else v]+=1
        cost=sum(k*(d-k) for k,d in zip(indeg,deg))
        if minimum is None or cost<minimum:
            minimum=cost;count=1
        elif cost==minimum:
            count+=1
    return minimum,count


def independent_switching_minimum(n, edges):
    # Edge orientations u<v; signs are products of incidences of two adjacent edges.
    # Switching one signed-line vertex reverses signs of all incident signed-line edges.
    incidences=[]
    for u,v in edges:
        incidences.append({u:-1,v:1})
    signed=[]
    for i in range(len(edges)):
        for j in range(i+1,len(edges)):
            common=set(incidences[i]) & set(incidences[j])
            if common:
                vertex=next(iter(common))
                signed.append((i,j,incidences[i][vertex]*incidences[j][vertex]))
    vals=[]
    # Pin the switching of edge 0; the other global switching gives the same signature.
    for mask in range(1<<max(0,len(edges)-1)):
        score=0
        for i,j,sigma in signed:
            ti=0 if i==0 else (mask>>(i-1))&1
            tj=0 if j==0 else (mask>>(j-1))&1
            if (sigma<0) ^ bool(ti ^ tj): score+=1
        vals.append(score)
    return min(vals), vals.count(min(vals))


def check(n,edges,do_signed=False):
    if not connected(n,edges): return (0,0,0)
    pred=graph_formula(n,edges)
    if pred is None: return (0,0,0)
    expected,cycles,deg=pred
    computed, num_orientations=orientation_minima(n,edges)
    assert computed==expected,(n,edges,pred,computed)
    expected_count=2*prod(
        sum(1 if deg[v]==2 else 2 for v in cyc if deg[v]==min(deg[w] for w in cyc))
        for cyc in cycles if len(cyc)%2
    )
    assert num_orientations==expected_count,(n,edges,deg,cycles,num_orientations,expected_count)
    if do_signed:
        signed_min,sign_count=independent_switching_minimum(n,edges)
        assert signed_min==computed,(n,edges, signed_min,computed)
        assert sign_count*2==num_orientations,(n,edges,sign_count,num_orientations)
    return 1,1 if len(cycles)==1 else 0,1 if do_signed else 0


def exhaustive_small():
    graphs=unicyclic=signs=0
    for n in range(3,7):
        edges=list(combinations(range(n),2))
        # Connected cacti have at least n-1 edges; cycle-separated up to two cycles at n=6.
        for k in range(n-1,min(len(edges),n+1)+1):
            for selection in combinations(edges,k):
                a,b,c=check(n,selection,do_signed=(n<=6))
                graphs+=a;unicyclic+=b;signs+=c
    return graphs,unicyclic,signs


def make_cactus(seed):
    r=Random(seed)
    cycle_count=r.randrange(1,4)
    cycles=[];edges=[];next_vertex=0
    for _ in range(cycle_count):
        length=r.randrange(3,7)
        c=list(range(next_vertex,next_vertex+length));next_vertex+=length
        edges.extend(tuple(sorted((c[i],c[(i+1)%length]))) for i in range(length))
        cycles.append(c)
    for i in range(1,cycle_count):
        parent_cycle=cycles[r.randrange(i)]
        a=r.choice(parent_cycle);b=r.choice(cycles[i]); length=r.randrange(1,4)
        for step in range(length-1):
            v=next_vertex;next_vertex+=1
            edges.append(tuple(sorted((a,v))));a=v
        edges.append(tuple(sorted((a,b))))
    leaf_count=r.randrange(0,9)
    for _ in range(leaf_count):
        parent=r.randrange(next_vertex)
        v=next_vertex;next_vertex+=1
        edges.append(tuple(sorted((parent,v))))
    return next_vertex,sorted(set(edges))


def randomized():
    total=unicyclic=signed=0
    for seed in range(300):
        n,edges=make_cactus(seed)
        if len(edges)>15: continue
        a,b,c=check(n,edges,do_signed=(seed%8==0))
        total+=a;unicyclic+=b;signed+=c
    return total,unicyclic,signed


def examples():
    for cycle_length in (3,5,7):
        for leaves_per_vertex in (0,1,2):
            n=cycle_length;edges=[(i,(i+1)%cycle_length) for i in range(cycle_length)]
            for i in range(cycle_length):
                for j in range(leaves_per_vertex):
                    edges.append((i,n));n+=1
            edges=[tuple(sorted(e)) for e in edges]
            if len(edges)<=15:
                check(n,edges,True)

if __name__=='__main__':
    a=exhaustive_small();b=randomized();examples()
    print('ALL CHECKS PASSED')
    print('exhaustive_small_connected_cacti=%d; unicyclic=%d; direct_switch_checks=%d' % a)
    print('random_vertex_disjoint_cycle_cacti=%d; unicyclic=%d; direct_switch_checks=%d' % b)
    print('cactus_optimal_orientation_counts=verified; odd_cycle_leaf_profiles=verified')
