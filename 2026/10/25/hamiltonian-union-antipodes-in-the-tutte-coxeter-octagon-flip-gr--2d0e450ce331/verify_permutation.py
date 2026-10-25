"""Exact matching-permutation and distance certificate for the Tutte--Coxeter graph.

Run: python verify_permutation.py
Only the Python standard library is required.
"""
from collections import Counter, deque
from itertools import combinations
from hashlib import sha256


def sinthemes():
    duads = list(combinations(range(6), 2))
    positions = {pair: i for i, pair in enumerate(duads)}
    ans = []
    def extend(free, chosen):
        if not free:
            ans.append(tuple(sorted(positions[e] for e in chosen)))
            return
        x = min(free)
        for y in sorted(free - {x}):
            extend(free - {x, y}, chosen + ((x, y),))
    extend(set(range(6)), ())
    return duads, sorted(ans)


def enumerate_matchings(rows):
    all_m = []
    def backtrack(i, used, assignment):
        if i == len(rows):
            all_m.append(tuple(assignment))
            return
        for col in rows[i]:
            if not (used >> col) & 1:
                backtrack(i + 1, used | (1 << col), assignment + [col])
    backtrack(0, 0, [])
    return sorted(all_m)


def comp_cycle_lengths(m, rows):
    H = [[] for _ in range(30)]
    for i, row in enumerate(rows):
        for j in row:
            if m[i] != j:
                H[i + 15].append(j)
                H[j].append(i + 15)
    assert all(len(a) == 2 for a in H)
    seen = set()
    lengths = []
    for v in range(30):
        if v in seen:
            continue
        todo = [v]
        seen.add(v)
        for x in todo:
            for y in H[x]:
                if y not in seen:
                    seen.add(y)
                    todo.append(y)
        lengths.append(len(todo))
    return tuple(sorted(lengths))


def one_alternating_cycle(m, n):
    # Composition of the two bijections; non-fixed permutation cycles
    # are the connected components of the symmetric difference.
    inverse = [None] * 15
    for row, col in enumerate(m):
        inverse[col] = row
    perm = [inverse[n[i]] for i in range(15)]
    seen = set()
    nontrivial = []
    for i in range(15):
        if i not in seen:
            j, size = i, 0
            while j not in seen:
                seen.add(j)
                j = perm[j]
                size += 1
            if size > 1:
                nontrivial.append(size)
    return nontrivial


def bfs(s, adj):
    out = [-1] * len(adj)
    out[s] = 0
    queue = deque([s])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if out[v] == -1:
                out[v] = out[u] + 1
                queue.append(v)
    return out


def main():
    duads, rows = sinthemes()
    assert len(duads) == len(rows) == 15
    assert all(len(r) == 3 for r in rows)
    ms = enumerate_matchings(rows)
    assert len(ms) == len(set(ms)) == 288
    shape = [comp_cycle_lengths(m, rows) for m in ms]
    assert Counter(shape) == {(10, 20): 144, (30,): 144}
    adj = [[] for _ in ms]
    pairs = []
    for i, m in enumerate(ms):
        for j in range(i + 1, len(ms)):
            cyc = one_alternating_cycle(m, ms[j])
            if cyc == [4]:
                adj[i].append(j)
                adj[j].append(i)
                pairs.append((i, j))
    assert len(pairs) == 1440
    assert set(map(len, adj)) == {10}
    distances = [bfs(i, adj) for i in range(len(ms))]
    assert all(-1 not in x for x in distances)
    profiles = Counter()
    ecc = Counter()
    for i, d in enumerate(distances):
        profiles[(shape[i], tuple(Counter(d)[k] for k in range(max(d)+1)))] += 1
        ecc[(shape[i], max(d))] += 1
    p = {
        ((10, 20), (1, 10, 45, 97, 96, 37, 2)): 144,
        ((30,), (1, 10, 42, 97, 101, 37)): 144,
    }
    assert dict(profiles) == p
    assert dict(ecc) == {((10, 20), 6): 144, ((30,), 5): 144}
    antipodes = [(i, j) for i in range(len(ms)) for j in range(i+1,len(ms))
                 if distances[i][j] == 6]
    assert len(antipodes) == 144
    for i, j in antipodes:
        assert shape[i] == shape[j] == (10, 20)
        assert set(ms[i][r] for r in range(15)).__len__() == 15
        assert all(ms[i][r] != ms[j][r] for r in range(15))
        assert one_alternating_cycle(ms[i], ms[j]) == [15]
    # Conversely, any pair with Hamiltonian symmetric difference is antipodal.
    ham_union = [(i, j) for i in range(len(ms)) for j in range(i+1,len(ms))
                 if one_alternating_cycle(ms[i], ms[j]) == [15]]
    assert ham_union == antipodes
    canon = '\n'.join(f'{i},{j}' for i,j in pairs).encode() + b'\n'
    print('duads=15 synthemes=15 incidences=45')
    print('perfect_matchings=288')
    print('two_factor_types=10+20:144,30:144')
    print('eight_cycle_flip_edges=1440 degrees=10 connected_components=1')
    print('10+20_profile=1,10,45,97,96,37,2 count=144')
    print('30_profile=1,10,42,97,101,37 count=144')
    print('radius=5 diameter=6')
    print('distance_6_pairs=144 all_and_only_hamiltonian_symmetric_difference')
    print('adjacency_sha256=' + sha256(canon).hexdigest())
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
