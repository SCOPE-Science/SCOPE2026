#!/usr/bin/env python3
"""Exact finite reduced-Swiatkowski calculations for three unordered particles
on the Petersen graph; only Python's standard library is required."""
from itertools import combinations, combinations_with_replacement, permutations, product
from collections import Counter

VERTEX_LABELS = list(combinations(range(5), 2))
VERTEX_INDEX = {pair: i for i, pair in enumerate(VERTEX_LABELS)}
EDGES = [(i, j) for i in range(10) for j in range(i + 1, 10)
         if not set(VERTEX_LABELS[i]).intersection(VERTEX_LABELS[j])]
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
INCIDENT = [[] for _ in range(10)]
for k, (a, b) in enumerate(EDGES):
    INCIDENT[a].append(k)
    INCIDENT[b].append(k)
assert len(EDGES) == 15 and all(len(x) == 3 for x in INCIDENT)

# At each vertex v use the two generators h-h0 relative to its first
# incident halfedge. Edge monomials have degree equal to remaining weight.
BASES = []
INDEX = []
for d in range(4):
    layer = []
    for vertices in combinations(range(10), d):
        for choices in product(*(range(1, len(INCIDENT[v])) for v in vertices)):
            local = tuple(zip(vertices, choices))
            for monomial in combinations_with_replacement(range(15), 3 - d):
                layer.append((local, monomial))
    BASES.append(layer)
    INDEX.append({b: i for i, b in enumerate(layer)})
assert [len(b) for b in BASES] == [680, 2400, 2700, 960]

def boundary(d, basis_element):
    local, monomial = basis_element
    acc = {}
    for j, (v, choice) in enumerate(local):
        rest = local[:j] + local[j+1:]
        for edge, sgn in ((INCIDENT[v][choice], 1), (INCIDENT[v][0], -1)):
            row = INDEX[d-1][(rest, tuple(sorted(monomial + (edge,))))]
            acc[row] = acc.get(row, 0) + (-1 if j % 2 else 1) * sgn
    return {k: v for k, v in acc.items() if v}

def modular_rank(columns, prime):
    pivots = {}
    for column in columns:
        vec = {k: v % prime for k, v in column.items() if v % prime}
        while vec:
            pivot = max(vec)
            row = pivots.get(pivot)
            if row is None:
                m = pow(vec[pivot], -1, prime)
                pivots[pivot] = {k: (v * m) % prime for k, v in vec.items()}
                break
            m = vec[pivot]
            for k, c in row.items():
                v = (vec.get(k, 0) - m * c) % prime
                if v: vec[k] = v
                else: vec.pop(k, None)
    return len(pivots)

BOUNDARIES = [None] + [[boundary(d, b) for b in BASES[d]] for d in range(1, 4)]
# Check d^2=0 by direct signed integer multiplication, not just modulo a prime.
for d in (2, 3):
    for col in BOUNDARIES[d]:
        total = {}
        for row, c in col.items():
            for rr, val in BOUNDARIES[d-1][row].items():
                total[rr] = total.get(rr, 0) + c * val
        assert all(v == 0 for v in total.values())
print('Chain sizes:', [len(b) for b in BASES])
for prime, expected in [(2, (679, 1714, 960)), (3, (679, 1715, 960)),
                         (5, (679, 1715, 960))]:
    ranks = tuple(modular_rank(BOUNDARIES[d], prime) for d in (1, 2, 3))
    assert ranks == expected, (prime, ranks)
    ranks_full = (0,) + ranks + (0,)
    betti = tuple(len(BASES[d])-ranks_full[d]-ranks_full[d+1] for d in range(4))
    print('Characteristic', prime, 'boundary ranks', ranks, 'Betti', betti)

# Direct combinatorial 5-cycle certificate for the spanning graph cycle space.
PENTAGONS = [(0,7,3,4,9), (0,7,3,5,8), (0,7,6,1,9),
             (0,7,6,2,8), (0,8,2,4,9), (0,8,5,1,9)]
CYCLE_COLUMNS = []
for path in PENTAGONS:
    assert len(set(path)) == 5
    assert len(set(range(10))-set(path)) >= 2
    c = {}
    for i in range(5):
        u,v = path[i],path[(i+1)%5]
        e = EDGE_INDEX[tuple(sorted((u,v)))]
        c[e] = 1 if u<v else -1
    assert len(c)==5
    CYCLE_COLUMNS.append(c)
assert modular_rank(CYCLE_COLUMNS,101) == 6
print('Five-cycle basis rank: 6 (mod 101); two fixed outside vertices available per cycle')
# Since graph has V=10,E=15 and is connected, its cycle lattice rank is 6.
# A single moving point on any certified pentagon, with the other two fixed
# off the cycle, supplies a three-particle configuration loop. The map
# summing particle paths has rank at least six in degree one. Thus over Q
# rank(d2)<=2400-679-6=1715. Since rank(d2)>=1715 mod 3, equality holds.
# rank(d1)<=679 by augmentation, and >=679 modulo 3. d3 has independent
# 960 columns mod 3 and therefore is injective over Q and Z.
print('Rational Betti: (1,6,25,0)')

# Complete S5-character from chain-level signed fixed-basis traces.
def partition(pi):
    seen = set(); sizes=[]
    for x in range(5):
        if x in seen: continue
        y=x;s=0
        while y not in seen:
            seen.add(y);s+=1;y=pi[y]
        sizes.append(s)
    return tuple(sorted(sizes,reverse=True))

def trace_data(pi):
    gv = [VERTEX_INDEX[tuple(sorted(pi[a] for a in pair))]
          for pair in VERTEX_LABELS]
    ge = [EDGE_INDEX[tuple(sorted((gv[a],gv[b])))] for a,b in EDGES]
    traces=[]
    for d, basis in enumerate(BASES):
        tr = 0
        for local, mon in basis:
            if tuple(sorted(ge[e] for e in mon)) != mon: continue
            old_vertices = [v for v,_ in local]
            new_vertices = [gv[v] for v in old_vertices]
            if sorted(new_vertices) != old_vertices: continue
            inv = sum(new_vertices[i]>new_vertices[j]
                      for i in range(d) for j in range(i+1,d))
            c = -1 if inv % 2 else 1
            old_local = dict(local)
            for v, choice in local:
                w = gv[v]
                target_edge = INCIDENT[w][old_local[w]]
                c *= (int(ge[INCIDENT[v][choice]] == target_edge)
                      - int(ge[INCIDENT[v][0]] == target_edge))
                if not c: break
            tr += c
        traces.append(tr)
    # H1 of graph: kernel of oriented-edge differential.
    edge_trace = 0
    for a,b in EDGES:
        if gv[a] == a and gv[b] == b: edge_trace += 1
        elif gv[a] == b and gv[b] == a: edge_trace -= 1
    vertex_trace = sum(gv[v]==v for v in range(10))
    h1 = edge_trace-vertex_trace+1
    euler_trace = sum((-1)**d * t for d,t in enumerate(traces))
    h2 = euler_trace - 1 + h1
    return traces,h1,h2

COUNTS = Counter(partition(p) for p in permutations(range(5)))
REPRESENTATIVES = {}
for pi in permutations(range(5)):
    REPRESENTATIVES.setdefault(partition(pi),pi)
EXPECTED = {
 (1,1,1,1,1):([680,2400,2700,960],6,25),
 (2,1,1,1):([28,24,-18,-12],0,-3),
 (3,1,1):([5,0,0,6],0,-2),
 (2,2,1):([28,0,-24,0],-2,1),
 (4,1):([2,0,0,0],0,1),
 (3,2):([1,0,0,0],0,0),
 (5,):([0,0,0,0],1,0),
}
print('cycle_type class_size chain_trace H1_trace H2_trace')
ALL_IRREP = [0]*7
for typ, (ct,h1,h2) in EXPECTED.items():
    tr = trace_data(REPRESENTATIVES[typ]);assert tr==(ct,h1,h2),(typ,tr)
    size=COUNTS[typ]; assert size>0
    print(str(typ),size,ct,h1,h2)
    pi=REPRESENTATIVES[typ]; sign=(-1)**(5-len(typ))
    std=typ.count(1)-1
    pi2=tuple(pi[pi[i]] for i in range(5))
    std2=partition(pi2).count(1)-1
    c32=(std*std+std2)//2-1-std
    c311=(std*std-std2)//2
    irr=[1,sign,std,sign*std,c32,sign*c32,c311]
    for i in range(7):ALL_IRREP[i]+=size*h2*irr[i]
assert all(s%120==0 for s in ALL_IRREP)
MULT = tuple(s//120 for s in ALL_IRREP)
assert MULT == (0,0,0,1,1,2,1), MULT
print('S5 multiplicities [5,1^5,4.1,2.1^3,3.2,2^2.1,3.1^2]:',MULT)
print('PETERSEN_THREE_PARTICLE_RATIONAL_CHARACTER_VERIFIED')
