#!/usr/bin/env python3
"""Exact finite verification of the dihedral character of the C6 strong-Morse complex.
No network calls or external Python packages. Run: python3 verify_hexagon_strong_morse.py
"""
from collections import Counter
from itertools import combinations, permutations

N = 6

def pair_label(v, u):
    """Vertex v paired to edge {u,v}; labels follow cyclic edge e_i={i,i+1}."""
    if (v + 1) % N == u:
        return 2 * v
    if (u + 1) % N == v:
        return 2 * u + 1
    raise ValueError((v, u))

def gradient_from_filtration(order):
    """For a graph, descending domination is exactly one earlier neighbor."""
    earlier = set()
    matching = []
    for v in order:
        lower = [w for w in ((v - 1) % N, (v + 1) % N) if w in earlier]
        if len(lower) == 1:
            matching.append(pair_label(v, lower[0]))
        earlier.add(v)
    return tuple(sorted(matching))

def gap_root_facet(gap, root_position):
    """Path after deleting gap; other vertices pair toward the chosen root."""
    chain = [(gap + 1 + j) % N for j in range(N - 1)]
    facet = []
    for j in range(N - 2):
        if j < root_position:
            facet.append(pair_label(chain[j], chain[j+1]))
        else:
            facet.append(pair_label(chain[j+1], chain[j]))
    return tuple(sorted(facet))

def closure(generators):
    faces = {()}
    for f in generators:
        for k in range(1, len(f) + 1):
            faces.update(combinations(f, k))
    return faces

filtration_matchings = {gradient_from_filtration(p) for p in permutations(range(N))}
facets = {gap_root_facet(i, r) for i in range(N) for r in range(N-1)}
assert len(facets) == 30
assert len({x for x in filtration_matchings if len(x) == 4}) == 30
assert closure(filtration_matchings) == closure(facets)
faces = closure(facets)
assert len(faces) == 163
by_degree = {d: sorted(x for x in faces if len(x) == d+1) for d in range(4)}
f_vector = tuple(len(by_degree[d]) for d in range(4))
assert f_vector == (12, 48, 72, 30)

def rank_f2(columns):
    basis = {}
    for x in columns:
        while x:
            pivot = x.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = x
                break
            x ^= basis[pivot]
    return len(basis)

def boundary_rank(d):
    low = {f: i for i, f in enumerate(by_degree[d-1])}
    columns = []
    for f in by_degree[d]:
        column = 0
        for j in range(len(f)):
            column ^= (1 << low[f[:j]+f[j+1:]])
        columns.append(column)
    return rank_f2(columns)

ranks = tuple(boundary_rank(d) for d in range(1, 4))
assert ranks == (11, 37, 30), ranks
betti_f2 = (f_vector[0]-1-ranks[0],
            f_vector[1]-ranks[0]-ranks[1],
            f_vector[2]-ranks[1]-ranks[2],
            f_vector[3]-ranks[2])
assert betti_f2 == (0, 0, 5, 0)

def rotation(k, x):
    edge, endpoint = divmod(x, 2)
    return 2*((edge+k) % N)+endpoint

def reflection(k, x):
    edge, endpoint = divmod(x, 2)
    return 2*((k-edge-1) % N)+(1-endpoint)

def inversion_sign(seq):
    count = sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return -1 if count % 2 else 1

def reduced_lefschetz(action):
    alternating_chain_traces = [0]*4
    for d, simplices in by_degree.items():
        for simplex in simplices:
            moved = [action(x) for x in simplex]
            if tuple(sorted(moved)) == simplex:
                alternating_chain_traces[d] += (-1)**d * inversion_sign(moved)
    return sum(alternating_chain_traces) - 1, alternating_chain_traces

# Each combinatorial automorphism must preserve every face.
for typ in ('r','s'):
    for k in range(N):
        action = (lambda x, k=k: rotation(k,x)) if typ == 'r' else (lambda x, k=k:reflection(k,x))
        assert {tuple(sorted(action(x) for x in f)) for f in facets} == facets

rchars = tuple(reduced_lefschetz(lambda x,k=k:rotation(k,x))[0] for k in range(N))
schars = tuple(reduced_lefschetz(lambda x,k=k:reflection(k,x))[0] for k in range(N))
assert rchars == (5,-1,-1,5,-1,-1), rchars
assert schars == (1,1,1,1,1,1), schars
# The central rotation r^3 has trace equal to the full rational Betti number 5;
# since r^3 is an involution, this forces it to be the identity on rational H2.
# D6/<r^3> = S3. The class character is 1 + 2*standard of S3.
assert 1+2*2 == 5 and 1+2*(-1) == -1 and 1+2*0 == 1
print('VERIFY_OK facets=30 filtration_orders=720 simplices=163 f_vector=', f_vector,
      'boundary_ranks_F2=',ranks,'reduced_betti_F2=',betti_f2,
      'rotations=',rchars,'reflections=',schars)
for typ,k in [('r',0),('r',1),('r',2),('r',3),('s',0),('s',1)]:
    action = (lambda x,k=k: rotation(k,x)) if typ=='r' else (lambda x,k=k: reflection(k,x))
    print('ACTION',typ,k,'alternating_chain_by_dimension',reduced_lefschetz(action)[1])
