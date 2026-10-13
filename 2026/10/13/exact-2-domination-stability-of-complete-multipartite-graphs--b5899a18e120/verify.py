from itertools import product


def gamma2_profile(parts):
    parts = tuple(sorted(x for x in parts if x > 0))
    if not parts:
        return 0
    best = sum(parts)
    for occ in product(*[range(n + 1) for n in parts]):
        s = sum(occ)
        if s >= best:
            continue
        if all(d == n or s - d >= 2 for n, d in zip(parts, occ)):
            best = s
    return best


def stability_profile(parts):
    parts = tuple(sorted(parts))
    g = gamma2_profile(parts)
    best = sum(parts)
    for deleted in product(*[range(n + 1) for n in parts]):
        k = sum(deleted)
        if k == 0 or k >= best:
            continue
        rest = tuple(sorted(n - d for n, d in zip(parts, deleted) if n - d > 0))
        if gamma2_profile(rest) != g:
            best = k
    return best


def closed_gamma2(parts):
    parts = tuple(sorted(parts))
    r = len(parts)
    if r == 2:
        a, b = parts
        if a == 1:
            return 2 if b <= 2 else b
        if a == 2:
            return 2
        return min(a, 4)
    u = sum(n == 1 for n in parts)
    v = sum(n == 2 for n in parts)
    return 2 if (v >= 1 or u >= 2) else 3


def closed_stability(parts):
    parts = tuple(sorted(parts))
    r = len(parts)
    if r == 2:
        a, b = parts
        if (a, b) == (1, 2):
            return 2
        if (a, b) == (2, 2):
            return 3
        if a == 3:
            return 1
        if a >= 4:
            return a - 3
        return 1
    u = sum(n == 1 for n in parts)
    v = sum(n == 2 for n in parts)
    w = sum(n >= 3 for n in parts)
    N = sum(parts)
    if v >= 1 or u >= 2:
        return N - 1 if w == 0 else u + 2 * v - 1
    m = min(n for n in parts if n >= 3)
    if r == 3 and u == 1:
        return 1
    return m - 2


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for first in range(lo, n + 1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


profiles = 0
deletions = 0
for N in range(2, 12):
    for p in partitions(N):
        if len(p) < 2:
            continue
        profiles += 1
        g = gamma2_profile(p)
        s = stability_profile(p)
        deletions += 1
        assert g == closed_gamma2(p), (p, g, closed_gamma2(p))
        assert s == closed_stability(p), (p, s, closed_stability(p))

bipartite = 0
for a in range(1, 21):
    for b in range(a, 21):
        p = (a, b)
        bipartite += 1
        assert gamma2_profile(p) == closed_gamma2(p), p
        assert stability_profile(p) == closed_stability(p), p

# Explicit checks against the standard definitions in the smallest boundary cases.
assert (gamma2_profile((1, 2)), stability_profile((1, 2))) == (2, 2)
assert (gamma2_profile((2, 2)), stability_profile((2, 2))) == (2, 3)
assert (gamma2_profile((2, 3)), stability_profile((2, 3))) == (2, 1)
assert (gamma2_profile((5, 5)), stability_profile((5, 5))) == (4, 2)

print(f"ALL CHECKS PASSED; multipartite_profiles_N<=11={profiles}; bipartite_profiles_a,b<=20={bipartite}")
