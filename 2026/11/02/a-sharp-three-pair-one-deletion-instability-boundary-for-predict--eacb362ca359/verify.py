"""Exact finite verification for a rank-window stable-matching boundary.

Usage: python3 verify.py
This code uses integer comparisons only and has no external dependencies.
"""
from itertools import permutations, product


def ranks(order):
    return tuple(tuple(row.index(i) for i in range(len(row))) for row in order)


def stable(matching, hospital_rank, resident_rank):
    n = len(matching)
    partner = [None] * n
    for h, r in enumerate(matching):
        if r is not None:
            partner[r] = h
    for h in range(n):
        for r in range(n):
            if matching[h] == r:
                continue
            if ((matching[h] is None or hospital_rank[h][r] < hospital_rank[h][matching[h]])
                and (partner[r] is None or resident_rank[r][h] < resident_rank[r][partner[r]])):
                return False
    return True


def deferred_acceptance(hospital_orders, resident_rank, permitted):
    n = len(hospital_orders)
    next_choice = [0] * n
    resident_partner = [None] * n
    free = list(range(n))
    while free:
        h = free.pop(0)
        while next_choice[h] < n and hospital_orders[h][next_choice[h]] not in permitted[h]:
            next_choice[h] += 1
        if next_choice[h] == n:
            continue
        r = hospital_orders[h][next_choice[h]]
        next_choice[h] += 1
        other = resident_partner[r]
        if other is None:
            resident_partner[r] = h
        elif resident_rank[r][h] < resident_rank[r][other]:
            resident_partner[r] = h
            free.append(other)
        else:
            free.append(h)
    result = [None] * n
    for r, h in enumerate(resident_partner):
        if h is not None:
            result[h] = r
    return tuple(result)


def all_stable(hospital_rank, resident_rank):
    n = len(hospital_rank)
    return [m for m in permutations(range(n)) if stable(m, hospital_rank, resident_rank)]


def test_small_market():
    cases = 0
    for n in (1, 2):
        orders = list(permutations(range(n)))
        for hs in product(orders, repeat=n):
            hr = ranks(hs)
            for rs in product(orders, repeat=n):
                rr = ranks(rs)
                for mu in all_stable(hr, rr):
                    # Every reciprocal edge-subset that retains the benchmark.
                    alternatives = [[frozenset({mu[h]} | {r for r in range(n) if r != mu[h] and (bits & (1 << r))})
                                     for bits in range(1 << n)] for h in range(n)]
                    for keep in product(*alternatives):
                        nu = deferred_acceptance(hs, rr, keep)
                        assert None not in nu
                        assert stable(nu, hr, rr)
                        cases += 1
    return cases


def test_example():
    hospitals = ((0, 1, 2), (1, 0, 2), (0, 1, 2))
    residents = ((1, 2, 0), (0, 1, 2), (0, 1, 2))
    hr, rr = ranks(hospitals), ranks(residents)
    mu = (1, 0, 2)
    assert all_stable(hr, rr) == [mu]
    # Accurate predictions at ranks (2,2,3), with common radius 1.
    center = tuple(hr[h][mu[h]] for h in range(3))
    permitted = tuple(frozenset(r for r in range(3) if abs(hr[h][r] - center[h]) <= 1)
                      for h in range(3))
    assert permitted == (frozenset((0, 1, 2)), frozenset((0, 1, 2)), frozenset((1, 2)))
    assert sum(3 - len(k) for k in permitted) == 1
    assert deferred_acceptance(hospitals, rr, (frozenset(range(3)),) * 3) == mu
    nu = deferred_acceptance(hospitals, rr, permitted)
    assert nu == (0, 1, 2)
    assert not stable(nu, hr, rr)
    # Verify that the sole blocking pair is exactly the sole removed edge.
    assert hr[2][0] < hr[2][nu[2]]
    assert rr[0][2] < rr[0][0]
    return mu, nu


def test_below_benchmark_deletions():
    n = 3
    orderings = list(permutations(range(n)))
    counter = 0
    for hs in product(orderings, repeat=n):
        hr = ranks(hs)
        for rs in product(orderings, repeat=n):
            rr = ranks(rs)
            for mu in all_stable(hr, rr):
                options = []
                for h in range(n):
                    mandatory = frozenset(r for r in range(n) if hr[h][r] <= hr[h][mu[h]])
                    tail = [r for r in range(n) if hr[h][r] > hr[h][mu[h]]]
                    options.append(tuple(mandatory | frozenset(tail[j] for j in range(len(tail)) if mask & (1 << j))
                                         for mask in range(1 << len(tail))))
                for keep in product(*options):
                    nu = deferred_acceptance(hs, rr, keep)
                    assert stable(nu, hr, rr)
                    # The original hospital-optimal stable matching is recovered.
                    full = deferred_acceptance(hs, rr, (frozenset(range(n)),) * n)
                    assert nu == full
                    counter += 1
    return counter


if __name__ == '__main__':
    print('all prunings with a surviving stable reference, n<=2:', test_small_market())
    print('single-edge three-by-three witness:', test_example())
    print('all below-benchmark prunings in three-by-three profiles:', test_below_benchmark_deletions())
    print('PASS')
