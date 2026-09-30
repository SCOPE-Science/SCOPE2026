#!/usr/bin/env python3
from itertools import combinations, product
from math import ceil


def partitions(n, lo=1):
    if n == 0:
        yield []
        return
    for x in range(lo, n + 1):
        for rest in partitions(n - x, x):
            yield [x] + rest


def closed_formula(ns):
    N = sum(ns)
    m = min(ns)
    mode_a = m + 1 + ceil((N - m - 1) / 2)
    mode_b = 10**9
    r = len(ns)
    for i, j in combinations(range(r), 2):
        if ns[i] < 2 or ns[j] < 2:
            continue
        ai = N - ns[i] - 1
        aj = N - ns[j] - 1
        eps = int(
            ai % 2 == 1
            and aj % 2 == 1
            and any(h not in (i, j) and ns[h] >= 2 for h in range(r))
        )
        mode_b = min(mode_b, 2 + ceil(ai / 2) + ceil(aj / 2) - eps)
    return min(mode_a, mode_b)


def support_minimum(ns):
    N = sum(ns)
    best = 10**9
    for ps in product(*[range(n + 1) for n in ns]):
        supp = [i for i, p in enumerate(ps) if p]
        if len(supp) < 2:
            continue
        k = sum(ps)
        zs = [n - p for n, p in zip(ns, ps)]
        Z = N - k
        if Z == 0:
            best = min(best, k)
            continue
        penalties = []
        for j in supp:
            if zs[j] == 0:
                penalties.append(ceil(Z / 2))
        for i, j in combinations(supp, 2):
            penalties.append(ceil((Z - zs[i]) / 2) + ceil((Z - zs[j]) / 2))
        if penalties:
            best = min(best, k + min(penalties))
    return best


def direct_label_minimum(ns):
    N = sum(ns)
    part = []
    for i, n in enumerate(ns):
        part.extend([i] * n)
    Delta = N - min(ns)
    L = ceil(Delta / 2) + 1
    best = 10**9
    for labels in product(range(L + 1), repeat=N):
        w = sum(labels)
        if w > best:
            continue
        pos = [v for v, x in enumerate(labels) if x > 0]
        if not pos:
            continue
        # The positive subgraph must have minimum degree at least one.
        if any(not any(part[u] != part[v] for u in pos) for v in pos):
            continue
        zeros = [v for v, x in enumerate(labels) if x == 0]
        feasible = True
        for v in zeros:
            ok = False
            for u in pos:
                if part[u] == part[v]:
                    continue
                z_neigh = sum(1 for z in zeros if part[z] != part[u])
                if labels[u] >= 1 + ceil(z_neigh / 2):
                    ok = True
                    break
            if not ok:
                feasible = False
                break
        if feasible:
            best = min(best, w)
    return best


def main():
    support_types = 0
    for N in range(2, 14):
        for ns in partitions(N):
            if len(ns) < 2:
                continue
            support_types += 1
            got = support_minimum(ns)
            want = closed_formula(ns)
            if got != want:
                raise AssertionError(("support", ns, got, want))

    direct_types = 0
    for N in range(2, 8):
        for ns in partitions(N):
            if len(ns) < 2:
                continue
            direct_types += 1
            got = direct_label_minimum(ns)
            want = closed_formula(ns)
            if got != want:
                raise AssertionError(("direct", ns, got, want))

    print(f"SUPPORT_TYPES={support_types}")
    print(f"DIRECT_TYPES={direct_types}")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
