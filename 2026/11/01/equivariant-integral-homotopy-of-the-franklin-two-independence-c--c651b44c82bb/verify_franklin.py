#!/usr/bin/env python3
"""Exact finite verification for the two-independence complex of the Franklin graph.

Pure Python 3, standard library only. Vertices 0,...,11 and LCF [5,-5]^6.
All exhaustive checks terminate after enumerating 2^12 vertex subsets.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
import json

N = 12

def graph():
    A = [0] * N
    for i in range(N):
        for j in ((i - 1) % N, (i + 1) % N, (i + (5 if i % 2 == 0 else -5)) % N):
            assert i != j
            A[i] |= 1 << j
            A[j] |= 1 << i
    assert all(a.bit_count() == 3 for a in A)
    assert sum(a.bit_count() for a in A) // 2 == 18
    return A


def degree_faces(A):
    return [m for m in range(1 << N) if all((A[i] & m).bit_count() <= 1
                     for i in range(N) if m & (1 << i))]


def component_faces(A):
    answer = []
    for m in range(1 << N):
        remaining = m
        valid = True
        while remaining:
            start = remaining & -remaining
            remaining ^= start
            queue = start
            size = 0
            while queue:
                b = queue & -queue
                queue ^= b
                size += 1
                if size > 2:
                    valid = False
                    break
                new = A[b.bit_length()-1] & remaining
                queue |= new
                remaining ^= new
            if not valid:
                break
        if valid:
            answer.append(m)
    return answer


def facets(m):
    remaining = m
    position = 0
    while remaining:
        bit = remaining & -remaining
        yield m ^ bit, (1 if position % 2 == 0 else -1)
        position += 1
        remaining ^= bit


def matching(faces):
    remaining = set(faces)
    pairs = []
    for vertex in range(N):
        bit = 1 << vertex
        for low in sorted(remaining):
            if low & bit:
                continue
            high = low | bit
            if high in remaining:
                remaining.remove(low)
                remaining.remove(high)
                pairs.append((low, high))
    assert pairs[0] == (0, 1)
    return pairs, remaining


def verify_acyclic(faces, pairs):
    # Ignore the augmented empty cell and its matched vertex pair; retain that vertex as a 0-cell.
    nonempty = set(faces) - {0}
    match = set(p for p in pairs if p[0] != 0)
    out = {f: [] for f in nonempty}
    indegree = {f: 0 for f in nonempty}
    edges = 0
    for high in nonempty:
        for low, _ in facets(high):
            if low == 0:
                continue
            if (low, high) in match:
                a, b = low, high
            else:
                a, b = high, low
            out[a].append(b)
            indegree[b] += 1
            edges += 1
    queue = deque([f for f in nonempty if indegree[f] == 0])
    reached = 0
    while queue:
        f = queue.popleft()
        reached += 1
        for g in out[f]:
            indegree[g] -= 1
            if indegree[g] == 0:
                queue.append(g)
    assert reached == len(nonempty), (reached, len(nonempty))
    return edges


def morse_matrix(pairs, critical):
    from_low = dict(pairs)
    upper = {u for _, u in pairs}
    critical_by_dim = defaultdict(list)
    for f in critical:
        critical_by_dim[f.bit_count()-1].append(f)
    for d in critical_by_dim:
        critical_by_dim[d].sort()

    @lru_cache(maxsize=None)
    def reduced(face):
        if face in critical:
            return {face: 1}
        if face in upper:
            return {}
        high = from_low[face]
        incidence = next(sign for low, sign in facets(high) if low == face)
        out = defaultdict(int)
        for lower, sgn in facets(high):
            if lower == face:
                continue
            for crit, weight in reduced(lower).items():
                out[crit] -= incidence * sgn * weight
        return {k: v for k, v in out.items() if v}

    dims = sorted(critical_by_dim)
    matrices = {}
    for dim in dims:
        if dim <= 0:
            continue
        rows = critical_by_dim.get(dim-1, [])
        columns = []
        for cell in critical_by_dim[dim]:
            out = defaultdict(int)
            for face, sign in facets(cell):
                for target, weight in reduced(face).items():
                    out[target] += sign * weight
            columns.append([out[row] for row in rows])
        matrices[dim] = columns
    return critical_by_dim, matrices


def rank_mod_prime(columns, p):
    if not columns:
        return 0
    pivots = {}
    rank = 0
    for col in columns:
        a = [v % p for v in col]
        while True:
            pos = next((i for i,v in enumerate(a) if v), None)
            if pos is None:
                break
            if pos not in pivots:
                inv = pow(a[pos], -1, p)
                pivots[pos] = [(v * inv) % p for v in a]
                rank += 1
                break
            x = a[pos]
            a = [(v - x * w) % p for v,w in zip(a, pivots[pos])]
    return rank


def homology_mod_prime(faces, p):
    by_dim = defaultdict(list)
    for f in faces:
        if f:
            by_dim[f.bit_count()-1].append(f)
    rows = {d: {f:i for i,f in enumerate(by_dim[d])} for d in by_dim}
    ranks = {}
    for d in by_dim:
        if d == 0:
            ranks[d] = 0
        else:
            vectors = []
            for f in by_dim[d]:
                vec = [0] * len(by_dim[d-1])
                for low,s in facets(f):
                    vec[rows[d-1][low]] = s
                vectors.append(vec)
            ranks[d] = rank_mod_prime(vectors, p)
    beta = {d:len(by_dim[d]) - ranks.get(d,0) - ranks.get(d+1,0) for d in by_dim}
    beta[0] -= 1
    return {d:b for d,b in beta.items() if b}, ranks


def automorphisms(A):
    assigned = {}
    used = set()
    results = []
    def walk():
        if len(assigned) == N:
            results.append(tuple(assigned[i] for i in range(N)))
            return
        v = max((i for i in range(N) if i not in assigned),
                key=lambda i:(sum(bool(A[i] & (1 << k)) for k in assigned), -i))
        for j in range(N):
            if j in used:
                continue
            if all(bool(A[v] & (1 << k)) == bool(A[j] & (1 << assigned[k]))
                   for k in assigned):
                assigned[v] = j
                used.add(j)
                walk()
                used.remove(j)
                del assigned[v]
    walk()
    assert len(results) == len(set(results))
    return results


def cycle_type(p):
    seen = set()
    lengths = []
    for i in range(N):
        if i in seen:
            continue
        k = i
        size = 0
        while k not in seen:
            seen.add(k)
            size += 1
            k = p[k]
        lengths.append(size)
    return tuple(sorted(lengths))


def homology_character(faces, p):
    trace = 0
    for face in faces:
        vertices = [i for i in range(N) if face & (1 << i)]
        images = [p[i] for i in vertices]
        if sorted(vertices) != sorted(images):
            continue
        inversions = sum(images[i] > images[j] for i in range(len(images))
                         for j in range(i+1,len(images)))
        orientation = -1 if inversions % 2 else 1
        alternating = 1 if len(vertices) % 2 else -1
        trace += alternating * orientation
    return trace


def main():
    A = graph()
    fs = degree_faces(A)
    assert fs == component_faces(A)
    assert len(fs) == 723
    fvector = Counter(f.bit_count()-1 for f in fs)
    assert [fvector[d] for d in range(-1,6)] == [1,12,66,184,264,168,28]
    pairs, crit = matching(fs)
    assert len(pairs) == 357
    assert len(crit) == 9
    assert Counter(f.bit_count()-1 for f in crit) == {3:2,4:7}
    hasse_edges = verify_acyclic(fs, pairs)
    dims, mats = morse_matrix(pairs,crit)
    assert dims[3] == [1066,2570]
    assert dims[4] == [1380,1698,2356,2388,2480,2706,2724]
    target = [[1,0],[1,0],[1,-1],[0,-1],[0,0],[0,-1],[-1,1]]
    assert mats[4] == target
    assert len(mats[3]) == 2 and all(not c for c in mats[3])
    # Columns one and four (0-based indices 0 and 3) have unit determinant -1.
    assert target[0][0] * target[3][1] - target[0][1] * target[3][0] == -1
    for prime in (2,3,5):
        beta, ranks = homology_mod_prime(fs, prime)
        assert beta == {4:5}, (prime, beta)
    autos = automorphisms(A)
    assert len(autos) == 48
    distribution = Counter((cycle_type(p), homology_character(fs,p)) for p in autos)
    expected = {
        ((1,)*12,5):1,
        ((2,)*6,1):1,
        ((1,)*8+(2,)*2,-3):3,
        ((1,)*4+(2,)*4,1):3,
        ((2,)*6,-1):12,
        ((2,2,4,4),1):12,
        ((3,3,3,3),-1):8,
        ((6,6),1):8,
    }
    assert distribution == Counter(expected), (distribution,expected)
    assert sum(trace*mult for (_,trace),mult in distribution.items()) == 0
    cert = {
        'graph_vertices':N,'graph_edges':18,'aut_group_order':len(autos),
        'augmented_faces':len(fs), 'face_vector': {str(d):fvector[d] for d in range(-1,6)},
        'matched_pairs_augmented':len(pairs), 'hasse_incidences_nonempty':hasse_edges,
        'critical_dimensions': {str(k):len(v) for k,v in dims.items()},
        'critical_3_faces':dims[3], 'critical_4_faces':dims[4],
        'morse_boundary_columns':target,
        'unit_minor_determinant':-1,
        'reduced_betti':{'4':5},
        'rational_invariant_rank':0,
        'character_distribution':[
            {'vertex_cycle_type':list(cyc),'trace_H4':trace,'multiplicity':freq}
            for (cyc,trace),freq in sorted(distribution.items(),key=lambda kv:(kv[0][0],kv[0][1]))],
        'verification':'FRANKLIN_INDEPENDENCE2_EQUIVARIANT_OK'
    }
    print(json.dumps(cert,sort_keys=True,ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
