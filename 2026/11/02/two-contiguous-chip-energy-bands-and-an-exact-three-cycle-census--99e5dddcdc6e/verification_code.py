"""Independent brute-force and constructive checks for primitive three-cycles of parallel chip-firing.
Run with Python 3.10+: python verification_code.py
Only standard library needed.
"""
from itertools import product, combinations
from collections import Counter


def edge_set_to_neighbors(n, edges):
    nbr = [set() for _ in range(n)]
    for u, v in edges:
        assert 0 <= u < v < n
        nbr[u].add(v); nbr[v].add(u)
    assert all(nbr)
    return [tuple(sorted(z)) for z in nbr]


def update(x, nbr):
    firing = [int(x[v] >= len(nbr[v])) for v in range(len(nbr))]
    return tuple(x[v] - len(nbr[v])*firing[v] + sum(firing[w] for w in nbr[v])
                 for v in range(len(nbr)))


def direct_period3_poly(nbr):
    degrees = [len(z) for z in nbr]
    counts=Counter()
    total=0
    for x in product(*(range(2*d) for d in degrees)):
        y=update(x,nbr)
        if y==x:continue
        z=update(y,nbr)
        if update(z,nbr)==x:
            assert z!=x
            counts[sum(x)] += 1
            total+=1
    assert all(v%3==0 for v in counts.values())
    return Counter({e:c//3 for e,c in counts.items()}),total


def phase_formula_poly(nbr):
    n=len(nbr);m=sum(map(len,nbr))//2
    sums=Counter(); valid_phase=0; trajectories=0
    for s in product(range(3),repeat=n):
        a=[sum((s[w]-s[v])%3==2 for w in nbr[v]) for v in range(n)]
        if not all(a):continue
        valid_phase+=1
        h=sum(s[v]==s[w] for v in range(n) for w in nbr[v] if v<w)
        # coefficient convolution in choices 0..a-1
        weights=Counter({0:1})
        for v in range(n):
            next_weights=Counter()
            for k,co in weights.items():
                for i in range(a[v]):next_weights[k+i]+=co
            weights=next_weights
        for t,count in weights.items():
            sums[m+h+t]+=count
            sums[3*m-n-h-t]+=count
            trajectories+=2*count
    assert all(v%3==0 for v in sums.values())
    return Counter({e:c//3 for e,c in sums.items()}),valid_phase,trajectories


def graph_connected(n,edges):
    nbr=[set() for _ in range(n)]
    for u,v in edges:nbr[u].add(v);nbr[v].add(u)
    seen={0};todo=[0]
    while todo:
        for w in nbr[todo.pop()]:
            if w not in seen:seen.add(w);todo.append(w)
    return len(seen)==n


def verify():
    cases=0; configs=0; nonzero=0
    # All connected labelled graphs through four vertices, and all connected
    # five-vertex graphs of edge count at most six.
    for n in range(2,6):
        potential=list(combinations(range(n),2))
        for mask in range(1<<len(potential)):
            edges=tuple(potential[i] for i in range(len(potential)) if mask>>i&1)
            if not graph_connected(n,edges):continue
            if n==5 and len(edges)>6:continue
            nbr=edge_set_to_neighbors(n,edges)
            formula,nph,traj=phase_formula_poly(nbr)
            direct,count=direct_period3_poly(nbr)
            assert formula==direct,(n,edges,formula,direct)
            assert traj==count,(n,edges,traj,count)
            if formula:
                m=len(edges)
                low=[e for e in formula if e<=2*m-n]
                high=[e for e in formula if e>=2*m]
                assert sorted(low)==list(range(min(low),2*m-n+1))
                assert sorted(high)==list(range(2*m,max(high)+1))
                assert set(formula)==set(low)|set(high)
                assert all(formula[e]==formula[4*m-n-e] for e in formula)
            cases+=1;configs+=__import__('math').prod(2*len(z) for z in nbr)
            nonzero +=bool(formula)
    print('ALL_GRAPH_CASES',cases,'BOUND_STATE_COMBINATIONS',configs,'CASES_WITH_PERIOD3',nonzero)

    # Select larger unicyclic graphs: a cycle with an arbitrary collection of
    # parent-linked leaves, with no restriction on tree attachment positions.
    u_cases=0;u_periodic_states=0
    from random import Random
    R=Random(43873)
    for cycle in range(3,7):
        for extra in range(0,4):
            for trial in range(3):
                n=cycle+extra
                edges=[(i,(i+1)%cycle) for i in range(cycle)]
                edges=[(min(u,v),max(u,v)) for u,v in edges]
                for v in range(cycle,n):
                    parent=R.randrange(v)
                    edges.append((parent,v))
                nbr=edge_set_to_neighbors(n,edges)
                P,ph,trajectory=phase_formula_poly(nbr)
                expected=Counter({n:2,2*n:2}) if cycle%3==0 else Counter()
                assert P==expected,(cycle,extra,edges,P,expected)
                u_cases+=1;u_periodic_states+=trajectory
    print('UNICYCLE_CASES',u_cases,'PERIODIC_STATES_CONSTRUCTED',u_periodic_states)

    # Exact conserved-chip distribution on book graphs (two core vertices
    # with r common degree-two neighbors), refining their total cycle count.
    from math import comb
    for r in range(1,9):
        edges=[(0,1)]+[(0,j) for j in range(2,r+2)]+[(1,j) for j in range(2,r+2)]
        computed,_,_=phase_formula_poly(edge_set_to_neighbors(r+2,edges))
        wanted=Counter()
        for k in range(r):
            coeff=2*sum(comb(r,j) for j in range(k+1))
            e=2*r+1+k
            wanted[e]=coeff
            wanted[7*r+2-e]=coeff
        assert computed==wanted,(r,computed,wanted)
        assert sum(computed.values())==r*2**(r+1)
    print('BOOK_ENERGY_DISTRIBUTIONS',8)

    # Spot-check every constructed phase/height state on two dense graphs.
    checks=0
    for n,edges in [(5,tuple(combinations(range(5),2))),
                    (6,tuple(combinations(range(6),2)))]:
        nbr=edge_set_to_neighbors(n,edges);d=[len(x) for x in nbr]
        for s in product(range(3),repeat=n):
            a=[sum((s[w]-s[v])%3==2 for w in nbr[v]) for v in range(n)]
            if not all(a):continue
            # deterministic extreme height choices
            for pick in [0,1]:
                u=[0 if pick==0 else av-1 for av in a]
                x=[]
                for v in range(n):
                    if s[v]==0:x.append(d[v]+u[v])
                    elif s[v]==1:x.append(d[v]+u[v]-a[v])
                    else:x.append(u[v]+sum(s[w]==2 for w in nbr[v]))
                x=tuple(x);y=update(x,nbr);z=update(y,nbr)
                assert update(z,nbr)==x and x!=y
                assert sum(x)==len(edges)+sum(s[v]==s[w] for v,w in edges)+sum(u)
                checks+=1
    print('DENSE_CONSTRUCTION_TESTS',checks)
    print('PERIOD3_WEIGHTED_COLORING_CHECKS_PASSED')


if __name__=='__main__':verify()
