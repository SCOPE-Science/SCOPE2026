"""Exhaustive finite checks for the degree-two strict-core classification.

Run: python verify_degree_two.py
Only the Python standard library is required. The infinite-family result
is proved mathematically; this script tests small cases and is not a proof.
"""
from functools import lru_cache
from itertools import combinations


def partitions(n, capacity):
    blocks = []

    def recurse(vertex):
        if vertex == n:
            yield tuple(tuple(block) for block in blocks)
            return
        for block in blocks:
            if len(block) < capacity:
                block.append(vertex)
                yield from recurse(vertex + 1)
                block.pop()
        blocks.append([vertex])
        yield from recurse(vertex + 1)
        blocks.pop()

    yield from recurse(0)


def graphs_of_order(n):
    kinds = [("P", j) for j in range(1, n + 1)]
    kinds += [("C", j) for j in range(3, n + 1)]
    kinds.sort()

    def recurse(remain, lower, selected):
        if remain == 0:
            yield tuple(selected)
        for index in range(lower, len(kinds)):
            kind = kinds[index]
            if kind[1] <= remain:
                selected.append(kind)
                yield from recurse(remain - kind[1], index, selected)
                selected.pop()

    yield from recurse(n, 0, [])


def neighbor_masks(components):
    n = sum(size for _, size in components)
    masks = [0] * n
    start = 0
    for kind, size in components:
        for j in range(size - 1):
            a, b = start + j, start + j + 1
            masks[a] |= 1 << b
            masks[b] |= 1 << a
        if kind == "C":
            a, b = start, start + size - 1
            masks[a] |= 1 << b
            masks[b] |= 1 << a
        start += size
    return masks


def is_strict_core(partition, masks, capacity, candidate_sets):
    n = len(masks)
    current = [0] * n
    for block in partition:
        group = sum(1 << v for v in block)
        for v in block:
            current[v] = (masks[v] & group).bit_count()
    for group, members in candidate_sets:
        weak = True
        strict = False
        for v in members:
            updated = (masks[v] & group).bit_count()
            if updated < current[v]:
                weak = False
                break
            if updated > current[v]:
                strict = True
        if weak and strict:
            return False
    return True


def predicted_count(components, capacity):
    cyc = 0
    small = []
    for kind, order in components:
        if order > capacity:
            if order % capacity:
                return 0
            cyc += kind == "C"
        else:
            small.append(order)

    @lru_cache(None)
    def bell(mask):
        if not mask:
            return 1
        leading = mask & -mask
        rest = mask ^ leading
        indices = [j for j in range(len(small)) if rest >> j & 1]
        total = 0
        for r in range(len(indices) + 1):
            for subset in combinations(indices, r):
                if small[leading.bit_length() - 1] + sum(small[j] for j in subset) <= capacity:
                    chosen = leading | sum(1 << j for j in subset)
                    total += bell(mask ^ chosen)
        return total

    return capacity ** cyc * bell((1 << len(small)) - 1)


def main():
    checks = 0
    partitions_checked = 0
    for n in range(1, 9):
        for components in graphs_of_order(n):
            masks = neighbor_masks(components)
            for capacity in range(1, min(5, n) + 1):
                candidate_sets = []
                for size in range(1, capacity + 1):
                    for members in combinations(range(n), size):
                        candidate_sets.append((sum(1 << v for v in members), members))
                observed = 0
                for partition in partitions(n, capacity):
                    partitions_checked += 1
                    observed += is_strict_core(partition, masks, capacity, candidate_sets)
                expected = predicted_count(components, capacity)
                assert observed == expected, (n, components, capacity, observed, expected)
                checks += 1
    print(f"PASS: {checks} graph/capacity cases, {partitions_checked} partitions checked.")
    examples = [(("P", 4),), (("P", 6),), (("C", 6),), (("P", 2), ("P", 1), ("P", 1))]
    for example in examples:
        print(f"example={example} capacity=3 count={predicted_count(example, 3)}")


if __name__ == "__main__":
    main()
