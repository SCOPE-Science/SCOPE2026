from itertools import combinations
from collections import Counter
from math import comb


def partitions(n):
    def rec(rem, last, acc):
        if rem == 0:
            yield tuple(acc)
            return
        for x in range(last, rem + 1):
            acc.append(x)
            yield from rec(rem - x, x, acc)
            acc.pop()
    yield from rec(n, 1, [])


def build(parts):
    part_of = []
    for i, a in enumerate(parts):
        part_of.extend([i] * a)
    n = len(part_of)
    closed = []
    for v in range(n):
        closed.append({u for u in range(n) if u == v or part_of[u] != part_of[v]})
    return part_of, closed


def irredundant(selected, closed):
    selected = set(selected)
    for v in selected:
        if not any((closed[w] & selected) == {v} for w in range(len(closed))):
            return False
    return True


def criterion(selected, parts, part_of):
    selected = set(selected)
    support = Counter(part_of[v] for v in selected)
    if len(support) <= 1:
        return True
    if len(support) == 2:
        i, j = sorted(support)
        return support[i] == support[j] == 1 and parts[i] >= 2 and parts[j] >= 2
    return False


def predicted_counts(parts):
    counts = Counter()
    for a in parts:
        for k in range(1, a + 1):
            counts[k] += comb(a, k)
    non_singletons = [i for i, a in enumerate(parts) if a >= 2]
    counts[2] += sum(parts[i] * parts[j] for i, j in combinations(non_singletons, 2))
    return counts


profiles = subset_checks = irredundant_sets = maximal_sets = 0
for n in range(2, 10):
    for parts in partitions(n):
        if len(parts) < 2:
            continue
        profiles += 1
        part_of, closed = build(parts)
        literal_sets = []
        counts = Counter()
        for mask in range(1, 1 << n):
            selected = [v for v in range(n) if (mask >> v) & 1]
            subset_checks += 1
            literal = irredundant(selected, closed)
            structural = criterion(selected, parts, part_of)
            if literal != structural:
                raise AssertionError(("classification", parts, selected, literal, structural))
            if literal:
                fs = frozenset(selected)
                literal_sets.append(fs)
                counts[len(selected)] += 1
                irredundant_sets += 1
        if counts != predicted_counts(parts):
            raise AssertionError(("polynomial", parts, counts, predicted_counts(parts)))

        literal_family = set(literal_sets)
        vertices = set(range(n))
        maximal = []
        for selected in literal_sets:
            if all(frozenset(set(selected) | {v}) not in literal_family for v in vertices - set(selected)):
                maximal.append(selected)

        blocks = []
        offset = 0
        for a in parts:
            blocks.append(list(range(offset, offset + a)))
            offset += a
        predicted_maximal = [frozenset(block) for block in blocks]
        for i, j in combinations(range(len(parts)), 2):
            if parts[i] >= 2 and parts[j] >= 2:
                for u in blocks[i]:
                    for v in blocks[j]:
                        predicted_maximal.append(frozenset((u, v)))
        if set(maximal) != set(predicted_maximal):
            raise AssertionError(("maximal", parts, len(maximal), len(predicted_maximal)))

        maximal_sets += len(maximal)
        if max(map(len, literal_sets)) != max(parts):
            raise AssertionError(("upper", parts))
        expected_lower = 1 if min(parts) == 1 else 2
        if min(map(len, maximal)) != expected_lower:
            raise AssertionError(("lower", parts))

print(f"VERIFY_OK profiles={profiles} subset_checks={subset_checks} irredundant_sets={irredundant_sets} maximal_sets={maximal_sets} max_order=9")
