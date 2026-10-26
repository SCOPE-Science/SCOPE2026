"""Direct definition-based checks for fair-coalition partitions of three disjoint cliques.

Python 3.9+; no external libraries required.
"""
from itertools import combinations
from math import comb


def adjacencies(sizes):
    vertex_count = sum(sizes)
    adj = [0] * vertex_count
    start = 0
    for size in sizes:
        mask = sum(1 << v for v in range(start, start + size))
        for v in range(start, start + size):
            adj[v] = mask ^ (1 << v)
        start += size
    return adj


def make_checker(sizes):
    adj = adjacencies(sizes)
    full = (1 << len(adj)) - 1
    cache = {}

    def fair_dominates(selected):
        if selected not in cache:
            cache[selected] = all(
                (adj[v] & selected).bit_count() == 1
                for v in range(len(adj)) if not ((selected >> v) & 1)
            )
        return cache[selected]

    def valid_partition(blocks):
        if not blocks or (sum(blocks) != full):
            # Blocks are pairwise disjoint in the enumeration below.
            return False
        for i, A in enumerate(blocks):
            if A.bit_count() == 1 and fair_dominates(A):
                continue
            if fair_dominates(A):
                return False
            if not any(
                i != j and not fair_dominates(B) and fair_dominates(A | B)
                for j, B in enumerate(blocks)
            ):
                return False
        return True

    return valid_partition


def predicted(sizes):
    a, b, c = sizes
    vals = [a, b, c]
    answer = 1
    for n in vals:
        answer *= n * (n - 1)
    for i, n in enumerate(vals):
        if n == 3:
            x, y = [vals[j] for j in range(3) if j != i]
            answer += 3 * x * y * (x + y - 2)
    answer += 6 * sum(vals[i] == vals[j] == 3 for i in range(3) for j in range(i + 1, 3))
    return answer


def from_block_vertices(n, merged_sets):
    used = set().union(*merged_sets)
    return [sum(1 << v for v in g) for g in merged_sets] + [1 << v for v in range(n) if v not in used]


def near_singletons(sizes):
    n = sum(sizes)
    check = make_checker(sizes)
    universe = set(range(n))
    counts = [0, 0, 0, 0]
    # Delta 0.
    counts[0] = int(check([1 << v for v in range(n)]))
    # Delta 1: one double.
    for x in combinations(range(n), 2):
        counts[1] += check(from_block_vertices(n, [set(x)]))
    # Delta 2: one triple or two doubles.
    for x in combinations(range(n), 3):
        counts[2] += check(from_block_vertices(n, [set(x)]))
    for x in combinations(range(n), 2):
        remain = universe - set(x)
        for y in combinations(sorted(remain), 2):
            if y < x:
                continue
            counts[2] += check(from_block_vertices(n, [set(x), set(y)]))
    # Delta 3: one quartet; one triple and one double; or three doubles.
    for x in combinations(range(n), 4):
        counts[3] += check(from_block_vertices(n, [set(x)]))
    for x in combinations(range(n), 3):
        for y in combinations(sorted(universe - set(x)), 2):
            counts[3] += check(from_block_vertices(n, [set(x), set(y)]))
    for x in combinations(range(n), 2):
        remain = universe - set(x)
        for y in combinations(sorted(remain), 2):
            if y < x:
                continue
            for z in combinations(sorted(remain - set(y)), 2):
                if z < y:
                    continue
                counts[3] += check(from_block_vertices(n, [set(x), set(y), set(z)]))
    return counts


def all_set_partitions(sizes):
    n = sum(sizes)
    check = make_checker(sizes)
    best = 0
    count = 0
    visited = 0
    groups = [1]

    def visit(next_vertex):
        nonlocal best, count, visited
        if next_vertex == n:
            visited += 1
            if len(groups) >= best and check(groups):
                if len(groups) > best:
                    best, count = len(groups), 0
                count += 1
            return
        bit = 1 << next_vertex
        for i in range(len(groups)):
            groups[i] |= bit
            visit(next_vertex + 1)
            groups[i] ^= bit
        groups.append(bit)
        visit(next_vertex + 1)
        groups.pop()

    visit(1)
    return visited, best, count


def main():
    for sizes in [(3, 3, 3), (3, 3, 4)]:
        visited, best, count = all_set_partitions(sizes)
        expected = sum(sizes) - 3
        assert (best, count) == (expected, predicted(sizes)), (sizes, best, count)
        print('full_bell', sizes, 'partitions', visited, 'maximum_blocks', best, 'optimal_count', count)
    for sizes in [
        (3, 3, 3), (3, 3, 4), (3, 4, 4), (4, 4, 4),
        (3, 3, 5), (3, 4, 5), (4, 4, 5), (3, 5, 6), (4, 5, 5),
    ]:
        got = near_singletons(sizes)
        assert got == [0, 0, 0, predicted(sizes)], (sizes, got, predicted(sizes))
        print('near_singletons', sizes, 'valid_by_defect', got, 'predicted', predicted(sizes))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
