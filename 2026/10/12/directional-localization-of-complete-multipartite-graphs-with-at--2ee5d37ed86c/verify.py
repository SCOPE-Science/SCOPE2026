from itertools import combinations, product


def integer_partitions(n, start=1, prefix=()):
    if n == 0:
        yield prefix
        return
    for x in range(start, n + 1):
        yield from integer_partitions(n - x, x, prefix + (x,))


def parts_from_sizes(sizes):
    parts = []
    for i, size in enumerate(sizes):
        parts.extend([i] * size)
    return parts


def allowed_partial(probe, robber, parts):
    if probe == robber:
        return (probe,)
    if parts[probe] != parts[robber]:
        return (robber,)
    return tuple(v for v, p in enumerate(parts) if p != parts[probe])


def allowed_full(probe, robber, parts):
    if probe == robber:
        return ((probe,),)
    if parts[probe] != parts[robber]:
        return ((robber,),)
    return (tuple(v for v, p in enumerate(parts) if p != parts[probe]),)


def closed_neighborhood_union(mask, parts):
    n = len(parts)
    out = mask
    for v in range(n):
        if mask & (1 << v):
            for w in range(n):
                if w == v or parts[w] != parts[v]:
                    out |= 1 << w
    return out


def response_candidate_masks(mask, probes, parts, full):
    table = {}
    n = len(parts)
    for robber in range(n):
        if not (mask & (1 << robber)):
            continue
        choices = []
        for probe in probes:
            choices.append(
                allowed_full(probe, robber, parts)
                if full
                else allowed_partial(probe, robber, parts)
            )
        for vector in product(*choices):
            table[vector] = table.get(vector, 0) | (1 << robber)
    return tuple(table.values())


def full_state_is_winning(sizes, cops, full):
    parts = parts_from_sizes(sizes)
    n = len(parts)
    probe_sets = list(combinations(range(n), cops))
    winning = set()
    changed = True
    while changed:
        changed = False
        for mask in range(1, 1 << n):
            if mask.bit_count() == 1 or mask in winning:
                continue
            for probes in probe_sets:
                succeeds = True
                for candidates in response_candidate_masks(mask, probes, parts, full):
                    if candidates.bit_count() == 1:
                        continue
                    nxt = closed_neighborhood_union(candidates, parts)
                    if nxt not in winning:
                        succeeds = False
                        break
                if succeeds:
                    winning.add(mask)
                    changed = True
                    break
    return ((1 << n) - 1) in winning


def direct_partial_probe_check(sizes):
    parts = parts_from_sizes(sizes)
    n = len(parts)
    s = min(sizes)
    if s <= 2:
        target_part = sizes.index(s)
        probes = tuple(v for v, p in enumerate(parts) if p == target_part)
    else:
        probes = tuple(next(v for v, p in enumerate(parts) if p == j) for j in range(3))
    masks = response_candidate_masks((1 << n) - 1, probes, parts, full=False)
    return all(mask.bit_count() == 1 for mask in masks)


def main():
    graph_types = 0
    partial_solver_checks = 0
    full_solver_checks = 0
    direct_strategy_checks = 0
    for order in range(3, 9):
        for sizes in integer_partitions(order):
            if len(sizes) < 3:
                continue
            graph_types += 1
            expected = min(min(sizes), 3)
            got = None
            for cops in range(1, 4):
                partial_solver_checks += 1
                if full_state_is_winning(sizes, cops, full=False):
                    got = cops
                    break
            if got != expected:
                raise AssertionError((sizes, 'partial', got, expected))
            full_solver_checks += 1
            if not full_state_is_winning(sizes, 1, full=True):
                raise AssertionError((sizes, 'full', 1))
            direct_strategy_checks += 1
            if not direct_partial_probe_check(sizes):
                raise AssertionError((sizes, 'direct strategy'))
    print(
        'ALL CHECKS PASSED; '
        f'graph_types={graph_types}; '
        f'partial_solver_checks={partial_solver_checks}; '
        f'full_solver_checks={full_solver_checks}; '
        f'direct_strategy_checks={direct_strategy_checks}; '
        'total_order_range=3..8'
    )


if __name__ == '__main__':
    main()
