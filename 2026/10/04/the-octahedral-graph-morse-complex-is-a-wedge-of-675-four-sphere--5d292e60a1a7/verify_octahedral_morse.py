#!/usr/bin/env python3
from itertools import combinations, product
from collections import Counter

# Octahedral graph O = K_6 minus a perfect matching.
N = 6
MISSING = {(0,1),(2,3),(4,5)}
EDGES = [e for e in combinations(range(N), 2) if e not in MISSING]
EDGE_INDEX = {e:i for i,e in enumerate(EDGES)}
NEIGHBORS = {v: [] for v in range(N)}
PRIMS = []
PRIM_INDEX = {}
for ei, (a,b) in enumerate(EDGES):
    for v,w in ((a,b),(b,a)):
        PRIM_INDEX[(v,w)] = len(PRIMS)
        PRIMS.append((v, ei, w))
        NEIGHBORS[v].append(w)
for v in NEIGHBORS:
    NEIGHBORS[v].sort()

def has_directed_cycle(out):
    for start in out:
        seen = set()
        x = start
        while x in out:
            if x in seen:
                return True
            seen.add(x)
            x = out[x]
    return False

def enumerate_faces():
    faces = set()
    choices = [[None] + NEIGHBORS[v] for v in range(N)]
    for choice in product(*choices):
        used_edges = set()
        out = {}
        ids = []
        ok = True
        for v,w in enumerate(choice):
            if w is None:
                continue
            e = tuple(sorted((v,w)))
            if e in used_edges:
                ok = False
                break
            used_edges.add(e)
            out[v] = w
            ids.append(PRIM_INDEX[(v,w)])
        if not ok or has_directed_cycle(out):
            continue
        faces.add(tuple(sorted(ids)))
    return sorted(faces, key=lambda f: (len(f), f))

def greedy_matching(faces):
    face_set = set(faces)
    unmatched = {f for f in faces if f}
    pairs = []
    for p in range(len(PRIMS)):
        for f in sorted(tuple(unmatched), key=lambda x: (len(x), x)):
            if f not in unmatched or p in f:
                continue
            g = tuple(sorted(f + (p,)))
            if g in unmatched and g in face_set:
                unmatched.remove(f)
                unmatched.remove(g)
                pairs.append((f,g))
    critical = sorted(unmatched, key=lambda f: (len(f), f))
    return pairs, critical

def matching_is_acyclic(faces, pairs):
    nodes = [f for f in faces if f]
    node_set = set(nodes)
    pair_set = set(pairs)
    succ = {f: [] for f in nodes}
    indeg = {f: 0 for f in nodes}
    for tau in nodes:
        if len(tau) <= 1:
            continue
        for j in range(len(tau)):
            sigma = tau[:j] + tau[j+1:]
            if sigma not in node_set:
                raise AssertionError('face closure failure')
            if (sigma, tau) in pair_set:
                a,b = sigma,tau
            else:
                a,b = tau,sigma
            succ[a].append(b)
            indeg[b] += 1
    stack = [f for f in nodes if indeg[f] == 0]
    seen = 0
    while stack:
        u = stack.pop()
        seen += 1
        for v in succ[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                stack.append(v)
    return seen == len(nodes)

def gf2_rank(columns):
    pivots = {}
    rank = 0
    for x in columns:
        y = x
        while y:
            p = y.bit_length() - 1
            if p in pivots:
                y ^= pivots[p]
            else:
                pivots[p] = y
                rank += 1
                break
    return rank

def boundary_rank(faces_k, faces_km1):
    row = {f:i for i,f in enumerate(faces_km1)}
    cols = []
    for tau in faces_k:
        bits = 0
        for j in range(len(tau)):
            sigma = tau[:j] + tau[j+1:]
            bits ^= 1 << row[sigma]
        cols.append(bits)
    return gf2_rank(cols)

def main():
    assert len(EDGES) == 12
    assert len(PRIMS) == 24
    faces = enumerate_faces()
    bydim = {d: [f for f in faces if len(f) == d+1] for d in range(5)}
    fvec = tuple(len(bydim[d]) for d in range(5))
    assert fvec == (24, 228, 1072, 2496, 2304), fvec
    assert len(faces) == 6125  # includes the empty face

    pairs, critical = greedy_matching(faces)
    crit = Counter(len(f)-1 for f in critical)
    assert len(pairs) == 2724
    assert crit == Counter({0:1, 4:675}), crit
    assert matching_is_acyclic(faces, pairs)

    ranks = []
    for k in range(1,5):
        ranks.append(boundary_rank(bydim[k], bydim[k-1]))
    assert tuple(ranks) == (23,205,867,1629), ranks
    betti = [0]*5
    betti[0] = len(bydim[0]) - ranks[0]
    for k in range(1,4):
        betti[k] = len(bydim[k]) - ranks[k] - ranks[k-1]
    betti[4] = len(bydim[4]) - ranks[3]
    assert tuple(betti) == (1,0,0,0,675), betti
    assert sum(((-1)**d)*fvec[d] for d in range(5)) == 676

    print('graph_vertices=6 graph_edges=12 primitive_fields=24')
    print('f_vector=' + repr(fvec))
    print('matching_pairs=2724 critical={0:1,4:675}')
    print('boundary_ranks_mod2=' + repr(tuple(ranks)))
    print('betti_mod2=' + repr(tuple(betti)))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
