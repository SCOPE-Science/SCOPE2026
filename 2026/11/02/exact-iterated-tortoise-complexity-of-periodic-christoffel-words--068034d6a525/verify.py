#!/usr/bin/env python3
"""Finite checks for all-iterate tortoise complexity of rational mechanical words.

The exhaustive ranges do not replace the unbounded structural proof.
"""
from collections import defaultdict
from math import gcd


def one_positions_after_tortoise(word, k):
    n = len(word)
    ones = [j for j, value in enumerate(word) if value == 1]
    removed = min(k, len(ones))
    return tuple([j - removed for j in ones[removed:]] +
                 list(range(n - removed, n)))


def mechanical_period(p, q):
    return tuple(((j + 1) * p // q) - (j * p // q) for j in range(q))


def predicted(p, q, k, n):
    H = (k * q - 1) // p
    lower = max(1, n - q + 1)
    upper = min(n - 1, H)
    eligible = 0 if upper < lower else (upper - lower + 1 -
                                        (upper // q - (lower - 1) // q))
    return min(q, n + 1) - eligible, eligible


def run(max_q=28, max_k=6):
    cases = phase_factors = positive_edge_checks = injection_checks = direct_replays = 0
    for q in range(2, max_q + 1):
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            period = mechanical_period(p, q)
            inverse = pow(p, -1, q)
            for k in range(1, max_k + 1):
                H = (k * q - 1) // p
                assert H % q != 0, (p, q, k, 'H-divisibility')
                for n in range(1, q + H + 3):
                    cases += 1
                    factors = {
                        tuple(period[(s + j) % q] for j in range(n))
                        for s in range(q)
                    }
                    predictions, edges = predicted(p, q, k, n)
                    images = {one_positions_after_tortoise(w, k) for w in factors}
                    if q <= 15:
                        for w in factors:
                            direct = list(w)
                            for _ in range(k):
                                if 1 in direct:
                                    direct.remove(1)
                                    direct.append(1)
                            reconstructed = tuple(i for i, b in enumerate(direct) if b == 1)
                            assert reconstructed == one_positions_after_tortoise(w, k), (p, q, k, n, 'direct')
                            direct_replays += 1
                    assert len(images) == predictions, (p, q, k, n, 'count', len(images), predictions)
                    assert len(factors) == min(q, n + 1), (p, q, k, n, 'factor')
                    # Independently sort by rational rotation phase x=j/q.
                    words = list(dict.fromkeys(
                        tuple(period[((phase * inverse) % q + i) % q] for i in range(n))
                        for phase in range(q)
                    ))
                    assert len(words) == len(factors) and set(words) == factors
                    outputs = [one_positions_after_tortoise(w, k) for w in words]
                    phase_factors += len(words)
                    places = defaultdict(list)
                    for idx, out in enumerate(outputs):
                        places[out].append(idx)
                    assert all(ii[-1] - ii[0] + 1 == len(ii) for ii in places.values()), (p, q, k, n, 'fibers')
                    adjacent = sum(outputs[i] == outputs[i + 1] for i in range(len(outputs)-1))
                    assert adjacent == edges, (p, q, k, n, 'edges', adjacent, edges)
                    positive_edge_checks += adjacent
                    if n >= q:
                        injection_checks += 1
                        assert (n < q + H or len(outputs) == len(set(outputs))), (p, q, k, n, 'eventual')
                        if n == q + H - 1:
                            assert len(outputs) > len(set(outputs)), (p, q, k, n, 'sharpness')
    print('VERIFY_OK')
    print(f'coprime_q_range=2..{max_q}')
    print(f'iteration_range=1..{max_k}')
    print(f'parameter_iteration_length_cases={cases}')
    print(f'phase_factors_crosschecked={phase_factors}')
    print(f'eligible_neighbor_edges_crosschecked={positive_edge_checks}')
    print(f'eventual_injectivity_tests={injection_checks}')
    print(f'direct_operator_iteration_replays={direct_replays}')
    print('checks: independent circular factors, phase ordering, image counts, fiber contiguity, modular edge formula, sharp injectivity')


if __name__ == '__main__':
    run()
