from itertools import combinations
from math import comb


def profiles(total, lo=1, pref=()):
    if total == 0:
        if len(pref) >= 2:
            yield pref
        return
    for x in range(lo, total + 1):
        yield from profiles(total - x, x, pref + (x,))


def parts_of(profile):
    parts = []
    part_index = []
    start = 0
    for i, n in enumerate(profile):
        vs = list(range(start, start + n))
        start += n
        parts.append(vs)
        part_index += [i] * n
    return parts, part_index


def super_literal(profile, mask):
    _, part_index = parts_of(profile)
    order = sum(profile)
    selected = {v for v in range(order) if mask >> v & 1}
    outside = set(range(order)) - selected
    for u in outside:
        witnessed = False
        for v in selected:
            if part_index[v] == part_index[u]:
                continue
            outside_neighbors = {w for w in outside if part_index[w] != part_index[v]}
            if outside_neighbors == {u}:
                witnessed = True
                break
        if not witnessed:
            return False
    return True


def super_criterion(profile, mask):
    _, part_index = parts_of(profile)
    order = sum(profile)
    outside = [v for v in range(order) if not (mask >> v & 1)]
    if len(outside) <= 1:
        return True
    if len(outside) != 2:
        return False
    u, v = outside
    return (part_index[u] != part_index[v]
            and profile[part_index[u]] >= 2
            and profile[part_index[v]] >= 2)


def formula_coeffs(profile):
    order = sum(profile)
    pair_count = sum(
        profile[i] * profile[j]
        for i in range(len(profile))
        for j in range(i + 1, len(profile))
        if profile[i] >= 2 and profile[j] >= 2
    )
    result = {order: 1, order - 1: order}
    if pair_count:
        result[order - 2] = pair_count
    return result


subset_checks = 0
criterion_checks = 0
valid_sets = 0
coefficient_checks = 0
gamma_checks = 0
special_checks = 0
profiles_count = 0

for order in range(2, 11):
    for profile in profiles(order):
        profiles_count += 1
        counts = {}
        for mask in range(1 << order):
            literal = super_literal(profile, mask)
            structural = super_criterion(profile, mask)
            subset_checks += 1
            criterion_checks += 1
            if literal != structural:
                raise AssertionError((profile, mask, literal, structural))
            if literal:
                valid_sets += 1
                size = mask.bit_count()
                counts[size] = counts.get(size, 0) + 1

        formula = formula_coeffs(profile)
        for size in set(counts) | set(formula):
            coefficient_checks += 1
            if counts.get(size, 0) != formula.get(size, 0):
                raise AssertionError(("coefficient", profile, size, counts.get(size, 0), formula.get(size, 0)))

        actual_gamma = min(counts)
        non_singleton_parts = sum(n >= 2 for n in profile)
        expected_gamma = order - 2 if non_singleton_parts >= 2 else order - 1
        gamma_checks += 1
        if actual_gamma != expected_gamma:
            raise AssertionError(("gamma", profile, actual_gamma, expected_gamma))

        actual_min_count = counts[actual_gamma]
        pair_count = sum(
            profile[i] * profile[j]
            for i in range(len(profile))
            for j in range(i + 1, len(profile))
            if profile[i] >= 2 and profile[j] >= 2
        )
        expected_min_count = pair_count if non_singleton_parts >= 2 else order
        if actual_min_count != expected_min_count:
            raise AssertionError(("minimum count", profile, actual_min_count, expected_min_count))

        if all(n == 1 for n in profile):
            special_checks += 1
            assert actual_gamma == order - 1 and actual_min_count == order
        if len(profile) == 2 and min(profile) == 1:
            special_checks += 1
            assert actual_gamma == order - 1 and actual_min_count == order
        if len(profile) == 2 and min(profile) >= 2:
            special_checks += 1
            assert actual_gamma == order - 2 and actual_min_count == profile[0] * profile[1]

print(
    "VERIFY_OK "
    f"profiles={profiles_count} "
    f"subset_checks={subset_checks} "
    f"criterion_checks={criterion_checks} "
    f"valid_sets={valid_sets} "
    f"coefficient_checks={coefficient_checks} "
    f"gamma_checks={gamma_checks} "
    f"special_checks={special_checks} "
    "max_order=10"
)
