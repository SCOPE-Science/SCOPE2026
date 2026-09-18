"""Finite verification of the weak-order Omega(P) formula.

The script implements the definitions of interval, relative down/up-set,
extremal boundary, W(S,C), saturation, and omega-bar directly for ordinal
sums of antichains. It checks all profiles with 2 <= h <= 4,
1 <= n_i <= 3, and total size <= 9.
"""
from itertools import product


def elements(ns):
    return [(i, j) for i, n in enumerate(ns) for j in range(n)]


def leq(x, y):
    return x == y or x[0] < y[0]


def connected(sub):
    sub = set(sub)
    if not sub:
        return False
    seen = {next(iter(sub))}
    stack = list(seen)
    while stack:
        x = stack.pop()
        for y in list(sub - seen):
            if leq(x, y) or leq(y, x):
                seen.add(y)
                stack.append(y)
    return len(seen) == len(sub)


def convex(sub, universe):
    sub = set(sub)
    for x in sub:
        for y in sub:
            if leq(x, y):
                for z in universe:
                    if leq(x, z) and leq(z, y) and z not in sub:
                        return False
    return True


def intervals(ns):
    universe = elements(ns)
    out = []
    for mask in range(1, 1 << len(universe)):
        s = {universe[k] for k in range(len(universe)) if (mask >> k) & 1}
        if connected(s) and convex(s, universe):
            out.append(frozenset(s))
    return out


def is_downset(s, t):
    return all(not (leq(x, y) and x not in s) for y in s for x in t)


def is_upset(c, t):
    return all(not (leq(y, x) and x not in c) for y in c for x in t)


def covers(x, y, t):
    if x == y or not leq(x, y):
        return False
    return not any(z != x and z != y and leq(x, z) and leq(z, y) for z in t)


def maximal(s):
    return {x for x in s if not any(x != y and leq(x, y) for y in s)}


def minimal(s):
    return {x for x in s if not any(x != y and leq(y, x) for y in s)}


def upper_boundary(s, t):
    return {x for x in t - s if any(covers(y, x, t) for y in s)}


def lower_boundary(c, t):
    return {x for x in t - c if any(covers(x, y, t) for y in c)}


def W(s, c, ints):
    out = []
    for t in ints:
        if not (s <= t and c <= t):
            continue
        if not is_downset(s, t) or not is_upset(c, t):
            continue
        if upper_boundary(s, t) != maximal(t - s):
            continue
        if lower_boundary(c, t) != minimal(t - c):
            continue
        out.append(t)
    return out


def omega_enumerated(ns):
    ints = intervals(ns)
    best = 0
    for s in ints:
        for c in ints:
            ws = W(s, c, ints)
            if len(ws) == 1:
                value = len(maximal(c - s)) + len(minimal(s - c))
                best = max(best, value)
    return best


def F(a, b):
    if a == b == 1:
        return 2
    if min(a, b) <= 2:
        return a + b - 1
    return a + b - 2


def omega_formula(ns):
    values = [F(ns[i], ns[i + 1]) for i in range(len(ns) - 1)]
    values.extend(
        ns[i] + ns[j]
        for i in range(len(ns))
        for j in range(i + 2, len(ns))
    )
    return max(values)


def main():
    checked = 0
    mismatches = []
    for h in range(2, 5):
        for ns in product(range(1, 4), repeat=h):
            if sum(ns) > 9:
                continue
            checked += 1
            direct = omega_enumerated(ns)
            closed = omega_formula(ns)
            if direct != closed:
                mismatches.append((ns, direct, closed))
    print(f"checked_profiles={checked}")
    print(f"mismatches={len(mismatches)}")
    if mismatches:
        for item in mismatches:
            print(item)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
