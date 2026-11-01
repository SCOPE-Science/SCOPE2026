"""Independent finite checks for a uniform two-independence homotopy formula.

Run: python3 verify.py
Only Python's standard library is required.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
from math import comb


def adjacency(n):
    adj = [0] * (2*n)
    for i in range(n):
        for j in range(n):
            if j != i and j != (i+1) % n:
                adj[i] |= 1 << (n+j)
                adj[n+j] |= 1 << i
    return adj


def direct_face(m, adj):
    return all((adj[i] & m).bit_count() <= 1
               for i in range(len(adj)) if m & (1 << i))


def cyclic_face(m, n):
    a = [i for i in range(n) if m >> i & 1]
    b = [j for j in range(n) if m >> (n+j) & 1]
    return (all(sum(j not in (i, (i+1) % n) for j in b) <= 1 for i in a)
            and all(sum(i not in ((j-1) % n, j) for i in a) <= 1 for j in b))


def faces(n):
    # Every mixed face has at most three vertices in each side.
    a_sides = [[sum(1 << i for i in z) for z in combinations(range(n), s)]
               for s in range(1, 4)]
    b_sides = [[sum(1 << (n+j) for j in z) for z in combinations(range(n), s)]
               for s in range(1, 4)]
    out = {m for m in range(1, 1 << n)}
    out |= {m << n for m in range(1, 1 << n)}
    for aa in a_sides:
        for bb in b_sides:
            for x in aa:
                for y in bb:
                    m = x | y
                    if cyclic_face(m, n):
                        out.add(m)
    return out


def sequential_match(face_set, vertex_order):
    available = set(face_set)
    pairs = []
    for v in vertex_order:
        bit = 1 << v
        for low in tuple(sorted(available)):
            high = low | bit
            if low & bit or low not in available or high not in available:
                continue
            pairs.append((low, high, v))
            available.remove(low)
            available.remove(high)
    return pairs, available


def acyclic(face_set, pairs):
    partner = {low: high for low, high, _ in pairs}
    indeg = {m: 0 for m in face_set}
    successors = defaultdict(list)
    for high in face_set:
        bits = high
        while bits:
            bit = bits & -bits
            bits -= bit
            low = high ^ bit
            if low not in face_set:
                continue
            u, v = (low, high) if partner.get(low) == high else (high, low)
            successors[u].append(v)
            indeg[v] += 1
    q = deque(m for m, d in indeg.items() if d == 0)
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        for v in successors[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return seen == len(face_set)


def expected_after_A(n):
    keep = {1}
    for j, k in combinations(range(n), 2):
        if k == j + 1 or (j == 0 and k == n-1):
            continue
        pj = max((j-1) % n, j)
        pk = max((k-1) % n, k)
        keep.add((1 << pj) | (1 << pk) | (1 << (n+j)) | (1 << (n+k)))
    for t in range(1 << n):
        s = t.bit_count()
        if s >= 4 or (s == 3 and all(not (t >> i & 1 and t >> ((i+1) % n) & 1) for i in range(n))):
            keep.add(t << n)
    return keep


def expected_final(n):
    stage = expected_after_A(n)
    keep = {m for m in stage if m & ((1 << n)-1)}  # includes the lone vertex a0
    for m in stage:
        if m & ((1 << n) - 1):
            continue
        t = m >> n
        if t.bit_count() != 4 or not (t & 1):
            continue
        # After b0, these quadruples survived exactly if the remaining triple
        # contains a path edge, i.e., is not independent in the index path.
        rem = t & ~1
        if all(not ((rem >> i & 1) and (rem >> (i+1) & 1)) for i in range(1, n-1)):
            continue
        # Remove the quadruples paired to independent triples {0,i,j}
        # by adding the index i-1.
        deleted = False
        for i in range(2, n-2):
            for j in range(i+2, n-1):
                if t == ((1 << 0) | (1 << (i-1)) | (1 << i) | (1 << j)):
                    deleted = True
        if not deleted:
            keep.add(m)
    return keep


def homology_mod2(fset, n):
    rows = [[] for _ in range(2*n+1)]
    for m in fset:
        rows[m.bit_count()].append(m)
    prev = 0
    betti = []
    for sz in range(1, 2*n+1):
        if sz + 1 <= 2*n:
            idx = {m: i for i, m in enumerate(rows[sz])}
            pivots = {}
            for m in rows[sz+1]:
                value = 0
                t = m
                while t:
                    bit = t & -t
                    t -= bit
                    value ^= 1 << idx[m ^ bit]
                while value:
                    k = value.bit_length()-1
                    if k not in pivots:
                        pivots[k] = value
                        break
                    value ^= pivots[k]
            nxt = len(pivots)
        else:
            nxt = 0
        # reduced H_0: suppress the single connected component
        val = len(rows[sz]) - prev - nxt - (1 if sz == 1 else 0)
        betti.append(val)
        prev = nxt
    return [(d, b) for d, b in enumerate(betti) if b]


def main():
    for n in range(3, 9):
        adj = adjacency(n)
        for m in range(1 << (2*n)):
            assert direct_face(m, adj) == cyclic_face(m, n), (n, m)
        print(f'INDEPENDENT_MEMBERSHIP n={n} subsets={1 << (2*n)}')
    for n in range(4, 13):
        ff = faces(n)
        pairs_A, remain_A = sequential_match(ff, range(n))
        assert remain_A == expected_after_A(n), (n, remain_A ^ expected_after_A(n))
        pairs, remain = sequential_match(ff, range(2*n))
        assert remain == expected_final(n), (n, remain ^ expected_final(n))
        counts = Counter(m.bit_count()-1 for m in remain)
        assert counts == {0: 1, 3: n*n-3*n-1}, (n, counts)
        assert acyclic(ff, pairs), n
        if n <= 8:
            betti = homology_mod2(ff, n)
            assert betti == [(3, n*n-3*n-1)], (n, betti)
            print(f'MOD2_HOMOLOGY n={n} {betti}')
        print(f'MORSE n={n} faces={len(ff)} pairs={len(pairs)} critical={dict(sorted(counts.items()))} acyclic=True')
    print('ALL_CHECKS_PASS')

if __name__ == '__main__':
    main()
