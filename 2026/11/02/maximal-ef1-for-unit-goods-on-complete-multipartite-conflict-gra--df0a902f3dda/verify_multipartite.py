"""Exact finite checks of a complete-multipartite maximal EF1 construction.

This tests the defining graph constraints, not merely the integer inequalities
used in the mathematical proof. Finite tests do not establish the theorem.
"""
from itertools import combinations_with_replacement
from random import Random


def allocate(part_sizes, agents):
    assert agents >= 1 and all(x >= 1 for x in part_sizes)
    indexed_parts = [list(range(sum(part_sizes[:j]), sum(part_sizes[:j+1])))
                     for j in range(len(part_sizes))]
    indexed_parts.sort(key=lambda p: (-len(p), p[0]))
    total = sum(part_sizes)
    result = [[] for _ in range(agents)]
    if total <= agents:
        for i, vertex in enumerate(v for part in indexed_parts for v in part):
            result[i].append(vertex)
        return result
    if len(indexed_parts[0]) >= agents:
        # One largest part can give all agents balanced, nonempty shares.
        for i, vertex in enumerate(indexed_parts[0]):
            result[i % agents].append(vertex)
        return result
    chosen, number = [], 0
    for part in indexed_parts:
        chosen.append(part)
        number += len(part)
        if number >= agents:
            break
    quota = [(len(part) + 1)//2 for part in chosen]
    extra = agents - sum(quota)
    assert extra >= 0
    for i, part in enumerate(chosen):
        increment = min(extra, len(part) - quota[i])
        quota[i] += increment
        extra -= increment
    assert extra == 0 and sum(quota) == agents
    color = 0
    for part, q in zip(chosen, quota):
        pairs = len(part)-q
        sizes = [2]*pairs + [1]*(q-pairs)
        start = 0
        for size in sizes:
            result[color] = part[start:start+size]
            color += 1
            start += size
        assert start == len(part)
    assert color == agents
    return result


def verify(part_sizes, agents):
    parts = []
    for idx, count in enumerate(part_sizes):
        parts.extend([idx]*count)
    bundles = allocate(part_sizes, agents)
    taken = [v for b in bundles for v in b]
    assert len(taken) == len(set(taken))
    assert all(0 <= v < len(parts) for v in taken)
    assert all(len({parts[v] for v in b}) <= 1 for b in bundles)
    lengths = [len(b) for b in bundles]
    assert max(lengths) - min(lengths) <= 1
    unused = set(range(len(parts))) - set(taken)
    for v in unused:
        for b in bundles:
            # Cannot extend any bundle by an unused good without a conflict.
            assert any(parts[w] != parts[v] for w in b)
    if len(parts) > agents and max(part_sizes) < agents:
        assert agents <= len(taken) <= 2*agents - 2
    return len(unused) > 0


def main():
    checks = partial = 0
    for count_parts in range(1, 6):
        for sizes in combinations_with_replacement(range(1, 7), count_parts):
            if sum(sizes) > 20:
                continue
            for agents in range(1, sum(sizes)+4):
                partial += verify(sizes, agents)
                checks += 1
    random = Random(1729)
    for _ in range(1200):
        numparts = random.randrange(1, 12)
        sizes = [random.randrange(1, 16) for _ in range(numparts)]
        agents = random.randrange(1, sum(sizes)+25)
        partial += verify(sizes, agents)
        checks += 1
    print(f'PASS: {checks} graph/agent instances; {partial} leave goods unassigned')


if __name__ == '__main__':
    main()
