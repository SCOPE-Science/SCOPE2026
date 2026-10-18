"""Separate direct equitable-partition and cyclic-unit orbit checks."""
from collections import defaultdict, Counter
from math import gcd


def classes(n, g):
    k = gcd(n, g)
    H = set(range(0, n, k))
    P = defaultdict(list)
    for x in range(n):
        for y in range(n):
            if x in H and y in H:
                lab = ('point', x, y)
            elif x in H:
                lab = ('r', x)
            elif y in H:
                lab = ('c', y)
            elif (x + y) % n in H:
                lab = ('s', (x + y) % n)
            else:
                lab = ('z',)
            P[lab].append((x, y))
    return P


def line_counts(n, x, y, lookup, kind):
    result = Counter()
    if kind == 0:
        for b in range(n): result[lookup[(x, b)]] += 1
    elif kind == 1:
        for a in range(n): result[lookup[(a, y)]] += 1
    else:
        for a in range(n): result[lookup[(a, ((x + y) - a) % n)]] += 1
    return result


def orbital_partition(n, g):
    units = [u for u in range(1, n) if gcd(u, n) == 1 and (u * g) % n == g]
    unseen = set((a, b) for a in range(n) for b in range(n))
    orbits = []
    while unseen:
        a, b = next(iter(unseen))
        orbit = frozenset(((u*a) % n, (u*b) % n) for u in units)
        assert orbit <= unseen
        unseen -= orbit
        orbits.append(orbit)
    return orbits, units


def main():
    equitable_pairs = 0
    for n in range(2, 21):
        for g in range(1, n):
            P = classes(n, g)
            lookup = {point: lab for lab, points in P.items() for point in points}
            assert len(lookup) == n*n
            for lab, points in P.items():
                for relation in range(3):
                    standard = line_counts(n, *points[0], lookup, relation)
                    for point in points[1:]:
                        assert line_counts(n, *point, lookup, relation) == standard, (n,g,lab,relation,point)
            orbits, units = orbital_partition(n, g)
            h = n // gcd(n, g)
            expected_exact = h == n or (n == 4 and h == 2)
            actual_exact = {frozenset(q) for q in P.values()} == set(orbits)
            assert actual_exact == expected_exact, (n,g,h,units)
            equitable_pairs += 1
    print(f"PASS: direct equitable neighbour counts for 3 relations in {equitable_pairs} parameter pairs, n<=20")
    print(f"PASS: direct modular-unit orbits match iff g generates Z_n or n=4,g=2")
    for n,g in [(4,2), (6,2), (6,3), (9,3), (12,3), (12,6), (16,4)]:
        P = classes(n,g)
        o,u = orbital_partition(n,g)
        print(f"n={n},g={g},h={n//gcd(n,g)}: refinement={len(P)},orbits={len(o)},units={len(u)}")

if __name__ == '__main__':
    main()
