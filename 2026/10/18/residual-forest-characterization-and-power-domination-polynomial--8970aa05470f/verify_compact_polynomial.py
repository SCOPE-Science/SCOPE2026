"""Exact bounded coefficient checks for the compact multipartite formula."""
from itertools import combinations, combinations_with_replacement, product
from math import comb, prod


def compact(parts):
    total = sum(x * y for x, y in combinations(parts, 2))
    answer = [0] * (total + 1)
    for u in product(*(range(a + 1) for a in parts)):
        positive = [x for x in u if x > 0]
        gamma = 1 - len(positive) + sum(x + y - x * y for x, y in combinations(positive, 2))
        signed_mult = (-1)**sum(u) * gamma * prod(comb(a, x) for a, x in zip(parts, u))
        exponent = sum(x * y for x, y in combinations([a - x for a, x in zip(parts, u)], 2))
        for k in range(exponent + 1):
            answer[k] += signed_mult * comb(exponent, k)
    if len(parts) == 2 and min(parts) == 1:
        answer[0] -= 1
    return answer


def direct(parts):
    labels = [p for p, a in enumerate(parts) for _ in range(a)]
    edges = [(i, j) for i, j in combinations(range(len(labels)), 2) if labels[i] != labels[j]]
    n = len(edges)
    closed = [sum(1 << j for j, f in enumerate(edges) if set(e).intersection(f)) for e in edges]
    full = (1 << n) - 1
    coeff = [0] * (n + 1)
    for selected in range(full + 1):
        seen = 0
        for j, neighborhood in enumerate(closed):
            if selected & (1 << j):
                seen |= neighborhood
        while seen != full:
            forces = 0
            for j, neighborhood in enumerate(closed):
                if seen & (1 << j):
                    unseen = neighborhood & ~seen
                    if unseen.bit_count() == 1:
                        forces |= unseen
            if not forces:
                break
            seen |= forces
        if seen == full:
            coeff[selected.bit_count()] += 1
    return coeff


if __name__ == '__main__':
    profiles = selections = 0
    for r in range(2, 6):
        for parts in combinations_with_replacement(range(1, 5), r):
            e = sum(x * y for x, y in combinations(parts, 2))
            if e > 13:
                continue
            got = compact(parts)
            assert got == direct(parts), parts
            assert got[0] == 0 and got[-1] == 1, parts
            profiles += 1
            selections += 1 << e
    mixed = compact((1, 2, 3))
    assert mixed[1:3] == [2, 49], mixed
    for b in range(1, 13):
        assert compact((1, b)) == [0] + [comb(b, k) for k in range(1, b + 1)]
    print(f'VERIFY_OK: {profiles} profiles, {selections} selections; mixed profile (1, 2, 3): {mixed}')
