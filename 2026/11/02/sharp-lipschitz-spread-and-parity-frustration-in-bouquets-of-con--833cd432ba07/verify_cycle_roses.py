#!/usr/bin/env python3
"""Exact small-case checks for sharp Lipschitz variance on cycle bouquets.
Analytical all-parameter proof is in RESULT.md; this script does not claim exhaustive verification of all integer parameters.
"""
from itertools import product


def cycle_data(q):
    """All vertices of root-normalized real 1-Lipschitz polytope of C_q.
    At least q-1 edges are tight; closure fixes remaining edge.
    """
    out = set()
    for increments in product((-1, 0, 1), repeat=q):
        if sum(increments):
            continue
        if q % 2 == 0:
            if 0 in increments: continue
        elif increments.count(0) != 1:
            continue
        v = tuple(sum(increments[:i]) for i in range(1, q))
        assert len(v) == q - 1
        assert all(abs(v[i]-v[i-1]) <= 1 for i in range(1, len(v)))
        assert abs(v[0]) <= 1 and abs(v[-1]) <= 1
        out.add(v)
    return out


def data_dist(q):
    d = tuple(min(i,q-i) for i in range(1,q))
    return sum(d),sum(z*z for z in d)


def verify():
    local_tests = 0
    for q in range(3,12):
        vs = cycle_data(q)
        a,b = data_dist(q)
        vals = [(sum(v), sum(x*x for x in v)) for v in vs]
        assert max(q*Q-S*S for S,Q in vals) == q*b-a*a
        assert (a,b) in vals and (-a,b) in vals
        assert max(abs(S) for S,Q in vals) == a
        # complete rooted cycle vertices: q-1 tight edges ensure spanning tree
        local_tests += len(vs)
    print('EXACT_ROOTED_CYCLE_VERTEX_MAXIMA_OK',local_tests)

    bouquet_tests=0
    for q in range(3,11):
        vs=cycle_data(q);a,b=data_dist(q)
        types={}
        for v in vs:
            S=sum(v);Q=sum(x*x for x in v)
            types[S]=max(types.get(S, -10**15),Q)
        for r in range(2,9):
            N=1+r*(q-1)
            states={0:0}
            for i in range(r):
                new={}
                for s,Q0 in states.items():
                    for s0,Q1 in types.items():
                        s1=s+s0
                        new[s1]=max(new.get(s1,-10**15),Q0+Q1)
                states=new
            exact=max(N*Q-S*S for S,Q in states.items())
            predicted=N*r*b-(a*a if r%2 else 0)
            assert exact==predicted,(q,r,exact,predicted)
            bouquet_tests+=1
    print('EXACT_ALL_EXTREME_PETAL_STATES_BOUQUET_OK',bouquet_tests)

    direct=0
    for q,r in [(3,2),(3,4),(4,2),(4,3),(4,4),(5,2),(5,3),(6,2),(6,3),(7,2)]:
        local=list(cycle_data(q));a,b=data_dist(q)
        N=1+r*(q-1)
        best=-1
        for petals in product(local,repeat=r):
            values=(0,)+sum(petals,())
            S=sum(values);Q=sum(x*x for x in values)
            value=N*Q-S*S
            best=max(best,value)
            direct+=1
        assert best == N*r*b - (a*a if r%2 else 0), (q,r,best)
    print('DIRECT_LABELLED_EXTREME_POTENTIALS_OK',direct)

    algebra=0
    for q in range(4,201):
        a,b=data_dist(q)
        assert a*a>=2*b
        for r in range(2,101,2):
            N=1+r*(q-1);NN=N+(q-1)
            assert (b*NN-a*a*N)<0
            assert (b*N+a*a*NN)>0
            algebra+=1
    print('EXACT_PARITY_SAWTOOTH_INEQUALITIES_OK',algebra)
    print('ALL_CONGRUENT_CYCLE_BOUQUET_SPREAD_CHECKS_OK')

if __name__=='__main__':verify()
