#!/usr/bin/env python3
from itertools import permutations
from math import factorial
from collections import Counter


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for a in range(lo, n + 1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


def formula(parts):
    N = sum(parts)
    S = 0
    total = 0
    for a in parts[:-1]:
        Q = N - (S + a)
        total += Q * (a * (2 * S + a + 1) // 2)
        S += a
    return total


def expected_optimal_count(parts):
    c = Counter(parts)
    ans = 1
    for a in parts:
        ans *= factorial(a)
    for m in c.values():
        ans *= factorial(m)
    return ans


def vertices(parts):
    return tuple((i, j) for i, a in enumerate(parts) for j in range(a))


def cost(order):
    pos = {v: i + 1 for i, v in enumerate(order)}
    vs = tuple(order)
    s = 0
    for u_i in range(len(vs)):
        u = vs[u_i]
        for v_i in range(u_i + 1, len(vs)):
            v = vs[v_i]
            if u[0] != v[0]:
                s += min(pos[u], pos[v])
    return s


def block_sorted(order, parts):
    # Every part is one contiguous block; block sizes are nondecreasing.
    labels = [v[0] for v in order]
    blocks = []
    seen = set()
    i = 0
    while i < len(labels):
        lab = labels[i]
        if lab in seen:
            return False
        seen.add(lab)
        j = i
        while j < len(labels) and labels[j] == lab:
            j += 1
        blocks.append(lab)
        i = j
    if len(blocks) != len(parts):
        return False
    sizes = [parts[lab] for lab in blocks]
    return all(sizes[i] <= sizes[i+1] for i in range(len(sizes)-1))


def main():
    graph_cases = 0
    permutation_cases = 0
    optimal_orders = 0
    structural_checks = 0
    for n in range(2, 9):
        for parts in partitions(n):
            if len(parts) < 2:
                continue
            graph_cases += 1
            vs = vertices(parts)
            best = None
            count = 0
            for order in permutations(vs):
                permutation_cases += 1
                c = cost(order)
                if best is None or c < best:
                    best = c
                    count = 1
                elif c == best:
                    count += 1
                is_struct = block_sorted(order, parts)
                if is_struct:
                    structural_checks += 1
                    if c != formula(parts):
                        raise AssertionError((parts, "structured order wrong cost", c, formula(parts)))
            if best != formula(parts):
                raise AssertionError((parts, "formula", best, formula(parts)))
            if count != expected_optimal_count(parts):
                raise AssertionError((parts, "count", count, expected_optimal_count(parts)))
            # Count equivalence plus every structured order having formula forces exact structural characterization.
            if count != sum(1 for o in permutations(vs) if block_sorted(o, parts)):
                raise AssertionError((parts, "structural characterization count mismatch"))
            optimal_orders += count
    # Published complete-bipartite special case: for a<=b, formula=b*a(a+1)/2.
    for a in range(1, 8):
        for b in range(a, 9-a):
            if formula((a,b)) != b*a*(a+1)//2:
                raise AssertionError((a,b,"bipartite specialization"))
    # Illustrative value.
    assert formula((1,2,4)) == 26
    print("ALL CHECKS PASSED")
    print(f"graph_cases={graph_cases}")
    print(f"permutation_cases={permutation_cases}")
    print(f"optimal_orders={optimal_orders}")
    print(f"structured_order_checks={structural_checks}")
    print("example_K_1_2_4=26")

if __name__ == "__main__":
    main()
