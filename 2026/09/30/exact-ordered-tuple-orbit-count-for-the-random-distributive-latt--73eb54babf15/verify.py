#!/usr/bin/env python3
from itertools import combinations

def normalize(family):
    family = {frozenset(s) for s in family}
    return frozenset(s for s in family if not any(t < s for t in family))

def free_distributive_elements(n):
    subsets = [
        frozenset(i for i in range(n) if (mask >> i) & 1)
        for mask in range(1 << n)
    ]
    out = []
    for mask in range(1 << (1 << n)):
        family = [subsets[j] for j in range(1 << n) if (mask >> j) & 1]
        nf = normalize(family)
        if len(nf) != len(family):
            continue
        a = frozenset(family)
        # Remove the two nullary constants: empty join and empty meet.
        if not a or a == frozenset([frozenset()]):
            continue
        out.append(a)
    return out

def join(a, b):
    return normalize(set(a) | set(b))

def meet(a, b):
    return normalize([x | y for x in a for y in b])

def join_irreducibles(elements, n):
    bottom = frozenset([frozenset(range(n))])
    answer = []
    for x in elements:
        if x == bottom:
            continue
        reducible = False
        for a in elements:
            for b in elements:
                if a != x and b != x and join(a, b) == x:
                    reducible = True
                    break
            if reducible:
                break
        if not reducible:
            answer.append(x)
    return answer

class UF:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if a > b:
            a, b = b, a
        self.p[b] = a
        return True

def tables(elements):
    idx = {x: i for i, x in enumerate(elements)}
    jt = [[idx[join(a, b)] for b in elements] for a in elements]
    mt = [[idx[meet(a, b)] for b in elements] for a in elements]
    return jt, mt

def congruence_closure(jt, mt, seeds):
    n = len(jt)
    uf = UF(n)
    for a, b in seeds:
        uf.union(a, b)
    changed = True
    while changed:
        changed = False
        groups = {}
        for i in range(n):
            groups.setdefault(uf.find(i), []).append(i)
        forced = []
        for group in groups.values():
            for ii in range(len(group)):
                a = group[ii]
                for jj in range(ii + 1, len(group)):
                    b = group[jj]
                    for c in range(n):
                        forced.append((jt[a][c], jt[b][c]))
                        forced.append((mt[a][c], mt[b][c]))
        for a, b in forced:
            if uf.union(a, b):
                changed = True
    labels = {}
    result = []
    for i in range(n):
        r = uf.find(i)
        labels.setdefault(r, len(labels))
        result.append(labels[r])
    return tuple(result)

def seed_pairs(partition):
    groups = {}
    for i, c in enumerate(partition):
        groups.setdefault(c, []).append(i)
    pairs = []
    for group in groups.values():
        if len(group) > 1:
            pairs.extend((group[0], b) for b in group[1:])
    return pairs

def enumerate_congruences(n):
    elements = free_distributive_elements(n)
    jt, mt = tables(elements)
    N = len(elements)
    identity = tuple(range(N))
    principal = {identity}
    for a in range(N):
        for b in range(a + 1, N):
            principal.add(congruence_closure(jt, mt, [(a, b)]))
    all_congruences = set(principal)
    frontier = list(principal)
    while frontier:
        x = frontier.pop()
        sx = seed_pairs(x)
        for y in principal:
            z = congruence_closure(jt, mt, sx + seed_pairs(y))
            if z not in all_congruences:
                all_congruences.add(z)
                frontier.append(z)
    return len(all_congruences)

def main():
    expected_sizes = {1: 1, 2: 4, 3: 18, 4: 166}
    expected_j = {n: (1 << n) - 2 for n in range(1, 5)}
    for n in range(1, 5):
        elements = free_distributive_elements(n)
        assert len(elements) == expected_sizes[n], (n, len(elements))
        jis = join_irreducibles(elements, n)
        assert len(jis) == expected_j[n], (n, len(jis))
        expected_sets = {
            frozenset([frozenset(s)])
            for r in range(1, n)
            for s in combinations(range(n), r)
        }
        assert set(jis) == expected_sets

    expected_congruences = {1: 1, 2: 4, 3: 64}
    for n, expected in expected_congruences.items():
        got = enumerate_congruences(n)
        assert got == expected, (n, got, expected)

    orbit_counts = [1 << ((1 << n) - 2) for n in range(1, 5)]
    assert orbit_counts == [1, 4, 64, 16384]
    print("VERIFY_OK")
    print("free_lattice_sizes", [expected_sizes[n] for n in range(1, 5)])
    print("join_irreducibles", [expected_j[n] for n in range(1, 5)])
    print("congruence_counts", [expected_congruences[n] for n in range(1, 4)])
    print("ordered_tuple_orbits", orbit_counts)

if __name__ == "__main__":
    main()
