"""Check wheel-zonotope smooth fixed-point counts by finite DAG enumeration.

For each rim size m, the graph is C_m joined to one hub h=m.
The result is a check over m=3,...,9, not a proof of the all-m theorem.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def closed_counts(m):
    # k is the number of spokes directed toward the hub.
    out = {0: 2 * m, m: 2 * m}
    for k in range(1, m):
        s = sum(
            Fraction(m * comb(k + r - 1, 2 * r - 1)
                       * comb(m - k + r - 1, 2 * r - 1), r)
            for r in range(1, min(k, m - k) + 1)
        )
        assert s.denominator == 1
        out[k] = int(s)
    return out


def recurrence_count(m):
    L0, L1 = 2, 3  # (3+sqrt(5))/2 and (3-sqrt(5))/2 power sums
    C0, C1 = 2, 1  # two primitive sixth roots power sums
    if m == 0:
        return L0 + C0 - 4
    if m == 1:
        return L1 + C1
    for _ in range(2, m + 1):
        L0, L1 = L1, 3 * L1 - L0
        C0, C1 = C1, C1 - C0
    return L1 + C1 + 4 * m - 4


def enumerate_by_reachability(m):
    n = m + 1
    edge_list = [(i, (i + 1) % m) for i in range(m)] + [
        (i, m) for i in range(m)
    ]
    data = Counter()
    acyclic_count = 0
    for mask in range(1 << len(edge_list)):
        succ = [0] * n
        indeg = [0] * n
        incoming_spokes = 0
        for j, (u, v) in enumerate(edge_list):
            if mask & (1 << j):
                u, v = v, u
            succ[u] |= 1 << v
            indeg[v] += 1
            if j >= m and v == m:
                incoming_spokes += 1
        todo = [i for i in range(n) if indeg[i] == 0]
        topo = []
        while todo:
            u = todo.pop()
            topo.append(u)
            for v in range(n):
                if succ[u] & (1 << v):
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        todo.append(v)
        if len(topo) != n:
            continue
        acyclic_count += 1
        reach = [0] * n
        for u in reversed(topo):
            for v in range(n):
                if succ[u] & (1 << v):
                    reach[u] |= (1 << v) | reach[v]
        covers = 0
        for u in range(n):
            for v in range(n):
                if not (succ[u] & (1 << v)):
                    continue
                if not any(
                    w != v and (succ[u] & (1 << w))
                    and (reach[w] & (1 << v))
                    for w in range(n)
                ):
                    covers += 1
        if covers == m:
            data[incoming_spokes] += 1
    return acyclic_count, dict(data)


def main():
    for m in range(3, 10):
        a, empirical = enumerate_by_reachability(m)
        expected = closed_counts(m)
        assert a == 3 ** m - 3, (m, a)
        assert empirical == expected, (m, empirical, expected)
        assert sum(expected.values()) == recurrence_count(m)
        print(
            f"m={m} acyclic={a} smooth={sum(empirical.values())} "
            f"by_incoming_spokes={[empirical.get(k, 0) for k in range(m + 1)]}"
        )
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
