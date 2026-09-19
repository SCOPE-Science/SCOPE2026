from itertools import combinations, permutations
from math import factorial


def overlaps(a, b):
    return bool(a & b) and not (a <= b or b <= a)


def is_noc(family):
    fam = list(family)
    for s in fam:
        if not any(all(not (overlaps(s, t) and x in t) for t in fam) for x in s):
            return False
    return True


def canonical_family(order):
    order = tuple(order)
    n = len(order)
    out = set()
    prefix = frozenset()
    for k in range(1, n + 1):
        for j in range(k - 1, n):
            out.add(prefix | {order[j]})
        prefix = prefix | {order[k - 1]}
    return frozenset(out)


def all_nonempty_subsets(n):
    x = range(n)
    return [frozenset(c) for r in range(1, n + 1) for c in combinations(x, r)]


def exhaustive(n):
    subsets = all_nonempty_subsets(n)
    best = -1
    maximizers = set()
    for mask in range(1 << len(subsets)):
        size = mask.bit_count()
        if size < best:
            continue
        fam = frozenset(subsets[i] for i in range(len(subsets)) if (mask >> i) & 1)
        if not is_noc(fam):
            continue
        if size > best:
            best = size
            maximizers = {fam}
        elif size == best:
            maximizers.add(fam)
    canon = {canonical_family(p) for p in permutations(range(n))}
    expected = 1 if n == 1 else factorial(n) // 2
    assert best == n * (n + 1) // 2
    assert maximizers == canon
    assert len(canon) == expected
    return best, len(maximizers)


def hasse_statistics(n):
    fam = canonical_family(range(n))
    vertices = list(fam)
    arcs = []
    for a in vertices:
        for b in vertices:
            if not b < a:
                continue
            if not any(b < c < a for c in vertices):
                arcs.append((a, b))
    indeg = {v: 0 for v in vertices}
    for a, b in arcs:
        indeg[b] += 1
    reticulations = sum(v >= 2 for v in indeg.values())
    assert len(vertices) == n * (n + 1) // 2
    assert len(arcs) == n * (n - 1)
    assert reticulations == max(0, n - 2)
    return len(vertices), len(arcs), reticulations


if __name__ == "__main__":
    for n in range(1, 5):
        best, count = exhaustive(n)
        print(f"n={n}: maximum={best}, extremal_families={count}")
    for n in range(2, 11):
        v, e, r = hasse_statistics(n)
        print(f"Hasse n={n}: vertices={v}, arcs={e}, reticulations={r}")
    print("all checks passed")
