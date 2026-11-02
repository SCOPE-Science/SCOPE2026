"""Exact finite check for normal, modus-ponens preconditionals on small Boolean algebras.

Run: python3 checker.py
Uses only Python's standard library; all integer arithmetic is exact.
"""
from collections import Counter
from itertools import permutations, product


def mask_image(s, p):
    return sum(1 << p[i] for i in range(len(p)) if s & (1 << i))


def check_axioms(R, n):
    """Independently check P1--P5, identity, MP, and finite meet normality."""
    universe = (1 << n) - 1
    subsets = range(universe + 1)
    def imp(a, b):
        return sum(1 << x for x in range(n) if (R[a, x] & ~b) == 0)
    for a in subsets:
        for b in subsets:
            ab = imp(a, b)
            if a == universe and ab & ~b: return False  # P1
            if a & b & ~ab: return False                    # P2
            if ab & ~imp(a, a & b): return False           # P3
            if a & ab & ~b: return False                   # MP
            if a == b and ab != universe: return False    # identity
            for c in subsets:
                if imp(a, b & c) & ~ab: return False        # P4
                if imp(a, b & c) != (ab & imp(a, c)):
                    return False                          # normality
                if imp(a, imp(a & b, c)) & ~imp(a & b, c):
                    return False                          # P5
    return True


def strong_density(R, n):
    universe = (1 << n) - 1
    for a in range(universe + 1):
        for d in range(universe + 1):
            if d & ~a: continue
            for x in range(n):
                expansion = 0
                for y in range(n):
                    if R[a, x] & (1 << y): expansion |= R[d, y]
                if R[d, x] & ~expansion: return False
    return True


def free_keys(n):
    return [(a, x) for a in range(1, 1 << n)
            for x in range(n) if not (a & (1 << x))]


def frame_from_free(n, keys, vals):
    R = {(a, x): ((1 << x) if (a & (1 << x)) else 0)
         for a in range(1 << n) for x in range(n)}
    R.update(zip(keys, vals))
    return R


def transformed_free(R, keys, p):
    transformed = {}
    for a, x in keys:
        transformed[mask_image(a, p), p[x]] = mask_image(R[a, x], p)
    return tuple(transformed[key] for key in keys)


def enumerate_rank(n, verify_every_candidate=True):
    keys = free_keys(n)
    choices = [[s for s in range(1 << n) if not (s & ~a)] for a, x in keys]
    perms = list(permutations(range(n)))
    counts = Counter()
    orbit_reps = set()
    fixed_by_type = Counter()
    inspected = 0
    for vals in product(*choices):
        R = frame_from_free(n, keys, vals)
        good = strong_density(R, n)
        if verify_every_candidate:
            assert check_axioms(R, n) == good, (n, vals)
        inspected += 1
        if not good: continue
        counts['all'] += 1
        if all(s.bit_count() <= 1 for s in vals): counts['functional'] += 1
        rep = min(transformed_free(R, keys, p) for p in perms)
        orbit_reps.add(rep)
        current = tuple(vals)
        for p in perms:
            if transformed_free(R, keys, p) == current:
                cycle = tuple(sorted([sum(i == p[i] for i in range(n))]))
                fixed_by_type[cycle[0]] += 1
    counts['nonfunctional'] = counts['all'] - counts['functional']
    counts['isomorphism_classes'] = len(orbit_reps)
    counts['candidates'] = inspected
    assert sum(fixed_by_type.values()) == counts['isomorphism_classes'] * len(perms)
    return counts, fixed_by_type


def compact_formula():
    n = 3
    keys = [(a, x) for a in range(n) for x in range(n) if a != x]
    frequencies = Counter()
    total = 0
    for bits in product((0, 1), repeat=6):
        t = dict(zip(keys, bits))
        weight = 1
        for w in range(n):
            u, v = [i for i in range(n) if i != w]
            eligible = 0
            for S in [0, 1 << u, 1 << v, (1 << u) | (1 << v)]:
                if t[u, w] and not (S & (1 << u) or
                                     (S & (1 << v) and t[u, v])):
                    continue
                if t[v, w] and not (S & (1 << v) or
                                     (S & (1 << u) and t[v, u])):
                    continue
                eligible += 1
            weight *= eligible
        frequencies[weight] += 1
        total += weight
    return total, frequencies


if __name__ == '__main__':
    x1, _ = enumerate_rank(1)
    x2, _ = enumerate_rank(2)
    x3, fixed = enumerate_rank(3)
    assert (x1['all'], x2['all']) == (1, 4)
    assert (x3['all'], x3['functional'], x3['nonfunctional']) == (1235, 283, 952)
    assert x3['isomorphism_classes'] == 227
    assert fixed == Counter({3: 1235, 1: 105, 0: 22})
    independent_total, weights = compact_formula()
    assert independent_total == x3['all']
    assert weights == Counter({8: 8, 9: 3, 12: 6, 16: 15, 18: 12,
                              24: 6, 27: 4, 32: 6, 36: 3, 64: 1})
    assert (1235 + 3*35 + 2*11) // 6 == x3['isomorphism_classes']
    print('ALL_CHECKS_OK ranks=(1,2,3) candidates=' +
          str(x1['candidates'] + x2['candidates'] + x3['candidates']) +
          ' accepted=1235 functional=283 nonfunctional=952 orbits=227')
