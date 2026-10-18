#!/usr/bin/env python3
"""Independent simplicial chains and group-character checks for the prism."""
import itertools
from collections import defaultdict

EDGES = [(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)]
vertices = range(6)
incidence = sorted((a,b) for x,y in EDGES for a,b in [(x,y),(y,x)])
pos = {arc:i for i,arc in enumerate(incidence)}
neighbors = {v:set() for v in vertices}
for x,y in EDGES:
    neighbors[x].add(y)
    neighbors[y].add(x)

# Build the simplicial complex independently, by expanding every vertex ordering
# immediately into all its nonempty subfaces (not by using the certificate).
by_degree = defaultdict(set)
for ordering in itertools.permutations(vertices):
    seen = set()
    arrow_ids = []
    for v in ordering:
        prev = [u for u in seen if u in neighbors[v]]
        if len(prev) == 1:
            arrow_ids.append(pos[(v, prev[0])])
        seen.add(v)
    for k in range(1, len(arrow_ids)+1):
        for subset in itertools.combinations(arrow_ids, k):
            by_degree[k-1].add(tuple(sorted(subset)))
assert [len(by_degree[d]) for d in (0,1,2)] == [18,66,24]
assert not by_degree[3]

def binary_rank(vectors):
    echelon = {}
    for v in vectors:
        while v:
            pivot = v.bit_length()-1
            if pivot in echelon:
                v ^= echelon[pivot]
            else:
                echelon[pivot] = v
                break
    return len(echelon)


def boundary_rank(k):
    low = {s:j for j,s in enumerate(sorted(by_degree[k-1]))}
    columns = []
    for simple in by_degree[k]:
        bits = 0
        for j in range(len(simple)):
            facet = simple[:j] + simple[j+1:]
            bits ^= 1 << low[facet]
        columns.append(bits)
    return binary_rank(columns)

assert boundary_rank(1) == 17
assert boundary_rank(2) == 24
assert [0, len(by_degree[1])-17-24, len(by_degree[2])-24] == [0,25,0]


def parity(indices):
    return -1 if sum(indices[i] > indices[j]
                     for i in range(len(indices))
                     for j in range(i+1,len(indices))) % 2 else 1


def graph_automorphism(base, switch):
    pvertex = {v:base[v%3] + 3*((v//3)^switch) for v in vertices}
    return {i:pos[(pvertex[a],pvertex[b])] for i,(a,b) in enumerate(incidence)}


def signed_trace_per_degree(perm):
    traces = []
    for degree in (0,1,2):
        total = 0
        for simplex in by_degree[degree]:
            image = [perm[i] for i in simplex]
            if set(image) == set(simplex):
                total += parity(image)
        traces.append(total)
    return traces

classes = defaultdict(list)
for base in itertools.permutations(range(3)):
    fixed = sum(base[i] == i for i in range(3))
    typ = {3:'identity',1:'transposition',0:'threecycle'}[fixed]
    eps = +1 if typ != 'transposition' else -1
    for switch in (0,1):
        arc_perm = graph_automorphism(base, switch)
        assert all(tuple(sorted(arc_perm[i] for i in f)) in by_degree[len(f)-1]
                   for dim in by_degree for f in by_degree[dim])
        traces = signed_trace_per_degree(arc_perm)
        # The complex is connected and has homology only in degree one.
        h1_trace = 1 - sum((-1)**d * tr for d,tr in enumerate(traces))
        assert h1_trace == (24 if typ=='identity' and switch==0 else 0)+eps
        classes[(typ,switch)].append(h1_trace)
assert len(classes) == 6 and sum(map(len,classes.values())) == 12
for key in classes:
    assert len(set(classes[key])) == 1

# On S_3 x C_2, the character 2*regular + inflated sign is integral-valued.
# Its trivial multiplicity is (1/12) times the sum of traces.
trivial_mult = sum(sum(x) for x in classes.values())//12
assert trivial_mult == 2
assert sorted((key[0], key[1], vals[0],len(vals)) for key,vals in classes.items()) == sorted([
    ('identity',0,25,1),('identity',1,1,1),
    ('threecycle',0,1,2),('threecycle',1,1,2),
    ('transposition',0,-1,3),('transposition',1,-1,3)])
print('MOD2_BOUNDARY_RANKS=(17,24) REDUCED_BETTI=(0,25,0)')
for (typ,switch), data in sorted(classes.items()):
    print('CHARACTER',typ,'LAYER_SWAP='+str(switch),'CLASS_SIZE='+str(len(data)),
          'H1_TRACE='+str(data[0]))
print('H1_Q = 2*Q[S3 x C2] + inflated_sign_S3; INVARIANTS=2')
print('VERIFY_REPRESENTATION_OK')
