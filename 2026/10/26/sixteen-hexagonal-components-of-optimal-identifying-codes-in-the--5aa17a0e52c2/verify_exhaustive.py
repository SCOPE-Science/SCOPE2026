"""Exhaustive identifying-code classification and exchange graph for Shrikhande graph.

No external dependencies. Vertex 4*a+b represents (a,b) in Z4^2.
"""
from collections import Counter, deque
from itertools import combinations

DELTAS = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
VERTICES = tuple(range(16))

def nbr(i, j):
    return (((j // 4 - i // 4) % 4), ((j % 4 - i % 4) % 4)) in DELTAS

OPEN = {i: {j for j in VERTICES if nbr(i,j)} for i in VERTICES}
CLOSED = {i: OPEN[i] | {i} for i in VERTICES}

def identifies(C):
    signatures = [frozenset(C & CLOSED[i]) for i in VERTICES]
    return all(signatures) and len(set(signatures)) == 16

# Lower bound: 16 distinct nonempty subsets of |C| require 2^|C|-1 >=16.
assert 2**4-1 <16

OPT = {frozenset(c) for c in combinations(VERTICES,5) if identifies(set(c))}
assert len(OPT) == 96

COS = lambda x: {(4*((x//4+2*i)%4))+((x%4+2*j)%4) for i in range(2) for j in range(2)}
TEMPLATE = set()
for x in VERTICES:
    core = COS(x)-{x}
    assert len(core) == 3
    assert len(OPEN[x]) == 6
    assert sum(nbr(a,b) for a,b in combinations(sorted(OPEN[x]),2)) == 6
    for a,b in combinations(sorted(OPEN[x]),2):
        if nbr(a,b):
            TEMPLATE.add(frozenset(core|{a,b}))
assert OPT == TEMPLATE
assert len(TEMPLATE) == 96

# Each code has a unique 3-element core from one coset.
def core_index(C):
    return [x for x in VERTICES if COS(x)-{x} <= C]
assert all(len(core_index(C)) == 1 for C in OPT)

ADJ = {C: {D for D in OPT if len(C.symmetric_difference(D)) == 2} for C in OPT}
assert all(len(ADJ[C]) == 2 for C in OPT)
assert all(core_index(C)==core_index(D) for C in OPT for D in ADJ[C])
assert sum(len(ns) for ns in ADJ.values())//2 == 96

unseen=set(OPT); sizes=[]; cycle_checks=[]
while unseen:
    seed=unseen.pop(); reached={seed}; queue=deque([seed])
    while queue:
        C=queue.popleft()
        for D in ADJ[C]:
            if D not in reached:
                reached.add(D);queue.append(D)
    unseen-=reached; sizes.append(len(reached))
    edges=sum(len(ADJ[C]&reached) for C in reached)//2
    cycle_checks.append(edges==len(reached)==6 and len({core_index(C)[0] for C in reached})==1)
assert sorted(sizes)==[6]*16 and all(cycle_checks)

# Contrasting rook graph: K4 square K4 has identifying-code number six.
ROOK_CLOSED=[]
for i in VERTICES:
    a,b=divmod(i,4)
    ROOK_CLOSED.append({j for j in VERTICES if ((j//4==a) or (j%4==b))})
def rook_id(c):
    ss=[frozenset(c & n) for n in ROOK_CLOSED]
    return bool(all(ss)) and len(set(ss))==16
assert not any(rook_id(set(c)) for c in combinations(VERTICES,5))
rook6=sum(rook_id(set(c)) for c in combinations(VERTICES,6))
assert rook6==2208

print('CHECK_EXHAUSTIVE_OK')
print('five_candidates', 4368)
print('shrikhande_identifying_minimum',5)
print('shrikhande_optimal_codes',len(OPT))
print('canonical_family', '16 missing coset vertices times 6 neighborhood edges')
print('exchange_edges',sum(len(ns) for ns in ADJ.values())//2)
print('exchange_component_sizes', sorted(sizes))
print('exchange_isomorphism','16 disjoint C6')
print('rook_minimum',6,'rook_optimal_codes',rook6)
