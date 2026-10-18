#!/usr/bin/env python3
"""Check the explicit unique six-element degree-pair collision."""
from collections import Counter
V=set(range(1,7))
base={(1,4),(1,5),(1,6),(2,5),(2,6),(3,4),(3,5),(4,5)}
P=base|{(1,2)}
Q=base|{(1,3)}

def degree(R):
    return {x:(sum(v==x for u,v in R),sum(u==x for u,v in R)) for x in V}

def check(R):
    assert len(R)==9
    assert all(u!=v and u in V and v in V for u,v in R)
    for u,v in R:
        for a,b in R:
            if v==a: assert (u,b) in R
    # no antichain of size 3
    from itertools import combinations
    for triple in combinations(V,3):
        assert any((x,y) in R or (y,x) in R for x,y in combinations(triple,2))
    # connectivity of underlying comparability graph
    reached={1}
    while True:
        more=reached|{v for u,v in R if u in reached}|{u for u,v in R if v in reached}
        if more==reached:break
        reached=more
    assert reached==V
for R in P,Q:check(R)
p=degree(P);q=degree(Q)
assert Counter(p.values())==Counter(q.values())
assert len(set(p.values()))==6
f={x:next(y for y in V if q[y]==p[x]) for x in V}
assert len(set(f.values()))==6
assert any((f[x],f[y]) not in Q for x,y in P)
# All unique degree pairs force f in an isomorphism: 2->3, but 2<6 maps to 3<6, absent in Q.
assert f[2]==3 and f[6]==6 and (2,6) in P and (3,6) not in Q
# A labeled pair of distinct connected width-two transitive digraphs
# with exactly the same net degrees also follows by relabeling Q by f.
assert all(p[x][0]-p[x][1] == q[f[x]][0]-q[f[x]][1] for x in V)

def second_round(R):
    d=degree(R)
    return Counter((d[x], tuple(sorted(d[y] for y in V if (y,x) in R)),
                    tuple(sorted(d[y] for y in V if (x,y) in R))) for x in V)

assert second_round(P) != second_round(Q)
print('P_relations=',sorted(P))
print('Q_relations=',sorted(Q))
print('P_degree_pairs=', sorted(p.items()))
print('Q_degree_pairs=', sorted(q.items()))
print('forced_profile_bijection=', sorted(f.items()))
print('NET_DEGREE_MATCH=', [p[x][0]-p[x][1] for x in sorted(V)])
print('PASS: transitive, width two, connected, same profile, nonisomorphic, second round separates')
