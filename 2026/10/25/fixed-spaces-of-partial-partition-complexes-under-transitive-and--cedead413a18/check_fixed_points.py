"""Finite checks for geometric fixed sets of transitive groups on the partial-partition complex.

The universal theorem requires a separate proof; this script checks exhaustive finite instances.
Pure Python 3 standard library only. Run: python3 check_fixed_points.py
"""
from itertools import permutations, product


def partitions_of_partial_set(n):
    """All partial set partitions: unlabeled nonempty blocks, possibly empty support."""
    def rec(i, blocks):
        if i == n:
            yield tuple(blocks)
            return
        yield from rec(i + 1, blocks)
        for k in range(len(blocks)):
            b = blocks[k]
            blocks[k] = b | (1 << i)
            yield from rec(i + 1, blocks)
            blocks[k] = b
        blocks.append(1 << i)
        yield from rec(i + 1, blocks)
        blocks.pop()
    yield from rec(0, [])


def apply(p, block):
    return sum(1 << p[i] for i in range(len(p)) if (block >> i) & 1)


def stable_partitions(n, generators):
    total = 0
    fixed = []
    for face in partitions_of_partial_set(n):
        total += 1
        if not face:
            continue
        face_set = frozenset(face)
        if all(frozenset(apply(g, b) for b in face) == face_set for g in generators):
            fixed.append(face)
            # For transitive actions each invariant face has full support and
            # is a single orbit of blocks: crucial to discreteness.
            assert sum(face) == (1 << n) - 1  # blocks are pairwise disjoint
            orb = {face[0]}
            frontier = [face[0]]
            while frontier:
                b = frontier.pop()
                for g in generators:
                    c = apply(g, b)
                    if c not in orb:
                        orb.add(c)
                        frontier.append(c)
            assert orb == face_set
    return total, len(fixed)


def group_table(elements, mul):
    where = {g: i for i, g in enumerate(elements)}
    return [[where[mul(a, b)] for b in elements] for a in elements]


def left_regular_generators(elements, table, generator_indices):
    return [tuple(table[g][k] for k in range(len(elements))) for g in generator_indices]


def all_subgroups(table):
    n = len(table)
    identity = next(i for i in range(n) if all(table[i][k] == k and table[k][i] == k for k in range(n)))
    groups = []
    for mask in range(1 << n):
        if not (mask & (1 << identity)):
            continue
        sub = [i for i in range(n) if mask & (1 << i)]
        if all(mask & (1 << table[i][j]) for i in sub for j in sub):
            groups.append(frozenset(sub))  # finite nonempty product-closed subset of a group is a subgroup
    return groups


def run_regular_group(name, elements, mul, gen):
    t = group_table(elements, mul)
    gi = [elements.index(g) for g in gen]
    actions = left_regular_generators(elements, t, gi)
    n = len(elements)
    reachable = {0}
    frontier = [0]
    while frontier:
        a = frontier.pop()
        for p in actions:
            b = p[a]
            if b not in reachable:
                reachable.add(b)
                frontier.append(b)
    assert len(reachable) == n, (name, reachable)
    faces, fixed = stable_partitions(n, actions)
    subgroup_sets = all_subgroups(t)
    sub = len(subgroup_sets)
    assert fixed == sub, (name, fixed, sub)
    # On a left regular action, the commuting right regular action must
    # act on fixed points as conjugation of the subgroup defining the cosets.
    for k in range(n):
        right = tuple(t[x][k] for x in range(n))
        for K in subgroup_sets:
            cosets = set()
            for g in range(n):
                cosets.add(frozenset(t[g][u] for u in K))
            image = {frozenset(right[x] for x in C) for C in cosets}
            block_at_identity = next(C for C in image if 0 in C)
            expected = next((L for L in subgroup_sets if L == block_at_identity), None)
            assert expected is not None
            expected_cosets = {frozenset(t[g][u] for u in expected) for g in range(n)}
            assert image == expected_cosets
    print(f'{name}: n={n}, examined_partial_partitions={faces}, fixed_points={fixed}, subgroups={sub}, commuting_right_action=verified')


def main():
    for n in range(2, 10):
        rot = tuple((i + 1) % n for i in range(n))
        total, fixed = stable_partitions(n, [rot])
        divisors = sum(n % d == 0 for d in range(1, n + 1))
        assert fixed == divisors, (n, fixed, divisors)
        print(f'Cyclic({n}): examined_partial_partitions={total}, fixed_points={fixed}, divisors={divisors}')
    v4 = list(range(4))
    run_regular_group('Klein four', v4, lambda a,b:a^b, [1, 2])
    s3 = list(permutations(range(3)))
    e3 = (0, 1, 2)
    t2 = (1, 0, 2)
    t3 = (1, 2, 0)
    run_regular_group('Symmetric three', s3, lambda a,b: tuple(a[b[k]] for k in range(3)), [t2,t3])
    d8 = [(a,b) for b in range(2) for a in range(4)]
    run_regular_group('Dihedral eight', d8, lambda x,y: ((x[0] + (-1)**x[1]*y[0])%4, (x[1]+y[1])%2), [(1,0),(0,1)])
    print('PARTIAL_PARTITION_TRANSITIVE_FIXED_VERIFIED')


if __name__ == '__main__':
    main()
