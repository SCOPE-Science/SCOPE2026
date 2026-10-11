"""Exact finite checks for coordinate-symmetry homology of generalized Mycielskian independence complexes.
Usage: python3 myc_verification.py (Python standard library only).
"""
from functools import lru_cache
from itertools import permutations

def graph(n, ell):
    vertices = [(j, i) for j in range(ell + 1) for i in range(n)] + [('apex', -1)]
    idx = {v: p for p, v in enumerate(vertices)}
    edges = set()
    def edge(a, b):
        x, y = idx[a], idx[b]
        assert x != y
        edges.add(tuple(sorted((x, y))))
    for j in range(ell):
        for i in range(n):
            for h in range(n):
                if i != h:
                    edge((j, i), (j + 1, h))
    for i in range(n):
        for h in range(i):
            edge((ell, i), (ell, h))
        edge((0, i), ('apex', -1))
    return vertices, edges

def apply_perm(vertices, perm):
    idx = {v: i for i, v in enumerate(vertices)}
    return [idx[v] if v[0] == 'apex' else idx[(v[0], perm[v[1]])] for v in vertices]

def orbit_euler(n, ell, perm):
    vertices, edges = graph(n, ell)
    action = apply_perm(vertices, perm)
    orbits, seen = [], set()
    for i in range(len(vertices)):
        if i in seen:
            continue
        orbit, j = [], i
        while j not in seen:
            orbit.append(j)
            seen.add(j)
            j = action[j]
        orbits.append(orbit)
    valid = [orb for orb in orbits if all(tuple(sorted((i, j))) not in edges
             for i in orb for j in orb if i < j)]
    adj = [0] * len(valid)
    for i in range(len(valid)):
        for j in range(i):
            if any(tuple(sorted((a, b))) in edges for a in valid[i] for b in valid[j]):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    @lru_cache(None)
    def eval_minus_one(s):
        if not s:
            return 1
        v = (s & -s).bit_length() - 1
        return eval_minus_one(s & ~(1 << v)) - eval_minus_one(s & ~(1 << v) & ~adj[v])
    # Each invariant coordinate orbit contributes -1 after alternating sign and orientation sign.
    return -eval_minus_one((1 << len(valid)) - 1)

def expected(n, ell, perm):
    f = sum(i == perm[i] for i in range(n))
    a = f - 1
    k, r = divmod(ell, 3)
    if r == 0:
        return a ** (k+1) + a**k, 2*k
    return a**(k+1), 2*k+1

def independent_faces(n, ell):
    vertices, edges = graph(n, ell)
    neighbors = [0] * len(vertices)
    for i, j in edges:
        neighbors[i] |= 1 << j
        neighbors[j] |= 1 << i
    faces = [0]
    for v in range(len(vertices)):
        faces.extend([mask | (1 << v) for mask in list(faces) if not (mask & neighbors[v])])
    return vertices, edges, faces

def direct_euler(n, ell, perm):
    vertices, _, faces = independent_faces(n, ell)
    action = apply_perm(vertices, perm)
    reduced_trace = 0
    for mask in faces:
        ids = [i for i in range(len(vertices)) if mask >> i & 1]
        images = [action[i] for i in ids]
        if set(images) != set(ids):
            continue
        parity = sum(images[i] > images[j] for i in range(len(ids)) for j in range(i+1, len(ids))) % 2
        reduced_trace += -1 if (len(ids)-1+parity) % 2 else 1
    return reduced_trace

def ranks_mod_two(n, ell):
    _, _, faces = independent_faces(n, ell)
    by_size = {}
    for f in faces:
        by_size.setdefault(f.bit_count(), []).append(f)
    ranks = {0: 0}
    max_size = max(by_size)
    for k in range(1, max_size+1):
        lower = {f: i for i, f in enumerate(by_size[k-1])}
        pivots = {}
        for face in by_size[k]:
            col = 0
            mask = face
            while mask:
                bit = mask & -mask
                col ^= 1 << lower[face ^ bit]
                mask ^= bit
            while col:
                high = col.bit_length()-1
                if high not in pivots:
                    pivots[high] = col
                    break
                col ^= pivots[high]
        ranks[k] = len(pivots)
    return {k-1: len(by_size[k]) - ranks[k] - ranks.get(k+1,0)
            for k in range(1,max_size+1) if len(by_size[k])-ranks[k]-ranks.get(k+1,0)}

def test_fold_layers(n, ell):
    for removed_apex in [True, False]:
        V,E = graph(n,ell)
        N=[set() for _ in V]
        for i,j in E:N[i].add(j);N[j].add(i)
        alive=set(range(len(V)))
        if removed_apex:alive.remove(len(V)-1)
        else:
            alive.remove(len(V)-1)
            alive -= {j*n+i for i in range(n) for j in [0]}
        start=2 if removed_apex else 3
        for layer in range(start,ell+1,3):
            for i in range(n):
                u,v=(layer-2)*n+i,layer*n+i
                assert u in alive and v in alive
                assert N[u]&alive <= N[v]&alive,(n,ell,removed_apex,layer,i)
            alive -= {layer*n+i for i in range(n)}

if __name__ == '__main__':
    orbit_count = direct_count = homology_count = fold_count = 0
    for n, cap in [(2,10),(3,10),(4,8),(5,6)]:
        for ell in range(cap+1):
            test_fold_layers(n,ell)
            fold_count += 2
            for p in permutations(range(n)):
                formula,d=expected(n,ell,p)
                assert (-1)**d * orbit_euler(n,ell,p) == formula, (n,ell,p)
                orbit_count += 1
                if (n <= 3 and ell <= 4) or (n==4 and ell<=2):
                    assert direct_euler(n,ell,p)==orbit_euler(n,ell,p)
                    direct_count +=1
            if (n==2 and ell<=6) or (n==3 and ell<=4) or (n==4 and ell<=3):
                beta=ranks_mod_two(n,ell)
                rank,d=expected(n,ell,tuple(range(n)))
                assert beta=={d:rank},(n,ell,beta,d,rank)
                homology_count+=1
    print('VERIFY_OK',f'folds={fold_count}',f'orbit_characters={orbit_count}',f'direct_traces={direct_count}',f'mod2_homology_cases={homology_count}')
