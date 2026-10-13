from itertools import combinations


def integer_partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for first in range(lo, n + 1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def make_graph(parts):
    vertices = []
    part_of = {}
    for p, size in enumerate(parts):
        for j in range(size):
            v = len(vertices)
            vertices.append(v)
            part_of[v] = p
    return vertices, part_of


def adjacent(u, v, part_of):
    return u != v and part_of[u] != part_of[v]


def is_toids(S, vertices, part_of):
    S = set(S)
    # Total domination: every vertex has a neighbor in S.
    for v in vertices:
        if not any(adjacent(v, u, part_of) for u in S):
            return False
    # Outer independence.
    outside = [v for v in vertices if v not in S]
    for i, u in enumerate(outside):
        for v in outside[i + 1:]:
            if adjacent(u, v, part_of):
                return False
    return True


def predicted_toids(S, vertices, part_of):
    outside_parts = {part_of[v] for v in vertices if v not in S}
    return len(outside_parts) <= 1


def set_partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    first = items[0]
    for rest in set_partitions(items[1:]):
        yield [{first}] + [set(b) for b in rest]
        for i in range(len(rest)):
            blocks = [set(b) for b in rest]
            blocks[i].add(first)
            yield blocks


def coalition_partition(blocks, vertices, part_of):
    status = [is_toids(b, vertices, part_of) for b in blocks]
    if any(status):
        return False
    for i, b in enumerate(blocks):
        if not any(i != j and is_toids(b | blocks[j], vertices, part_of)
                   for j in range(len(blocks))):
            return False
    return True


def exact_number(parts):
    vertices, part_of = make_graph(parts)
    best = 0
    for blocks in set_partitions(vertices):
        if len(blocks) <= best:
            continue
        if coalition_partition(blocks, vertices, part_of):
            best = len(blocks)
    return best


def construction_works(parts):
    vertices, part_of = make_graph(parts)
    by_part = {}
    for v in vertices:
        by_part.setdefault(part_of[v], []).append(v)
    y = by_part[0][0]
    z = by_part[1][0]
    X = set(vertices) - {y, z}
    Y, Z = {y}, {z}
    return coalition_partition([X, Y, Z], vertices, part_of)


def main():
    profiles = 0
    subset_checks = 0
    partition_profiles = 0
    construction_profiles = 0
    for n in range(3, 9):
        for parts in integer_partitions(n):
            if len(parts) < 3 or max(parts) < 2:
                continue
            profiles += 1
            vertices, part_of = make_graph(parts)
            for mask in range(1 << n):
                S = {v for v in vertices if (mask >> v) & 1}
                assert is_toids(S, vertices, part_of) == predicted_toids(S, vertices, part_of), parts
                subset_checks += 1
            assert exact_number(parts) == 3, parts
            partition_profiles += 1
    for n in range(3, 31):
        for parts in integer_partitions(n):
            if len(parts) < 3 or max(parts) < 2:
                continue
            assert construction_works(parts), parts
            construction_profiles += 1
    print('ALL CHECKS PASSED')
    print(f'profiles_N_le_8={profiles}')
    print(f'toids_subset_checks={subset_checks}')
    print(f'exact_partition_profiles={partition_profiles}')
    print(f'construction_profiles_N_le_30={construction_profiles}')


if __name__ == '__main__':
    main()
