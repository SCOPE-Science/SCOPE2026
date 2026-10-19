#!/usr/bin/env python3
"""Independent finite checks for the equal-priority matching model on complete multipartite graphs.

Python 3.10+ standard library only; run `python verify.py`.
The exact arguments for asymptotic convergence are mathematical, not computational.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from random import Random


def edge_types(state):
    return [(i, j, state[i]*state[j])
            for i in range(len(state)) for j in range(i+1, len(state))
            if state[i] and state[j]]


@lru_cache(None)
def final_law(state):
    """Exact probabilities by conditioning on the next accepted edge."""
    pairs = edge_types(state)
    total = sum(w for _, _, w in pairs)
    if not total:
        return {sum(state): Fraction(1)}
    law = Counter()
    for i, j, w in pairs:
        st = list(state)
        st[i] -= 1
        st[j] -= 1
        for remaining, probability in final_law(tuple(st)).items():
            law[remaining] += Fraction(w, total) * probability
    return dict(law)


def exhaustive_priority_law(sizes):
    """Independent edge-permutation implementation of the physical deposition model."""
    vertices = [i for i, size in enumerate(sizes) for _ in range(size)]
    edges = [(i, j) for i in range(len(vertices)) for j in range(i+1, len(vertices))
             if vertices[i] != vertices[j]]
    if len(edges) > 9:
        raise ValueError('exhaustive check intentionally restricted to <= 9 edges')
    counts = Counter()
    for priority in permutations(edges):
        occupied = set()
        for u, v in priority:
            if u not in occupied and v not in occupied:
                occupied.update((u, v))
        counts[len(vertices)-len(occupied)] += 1
    return {unmatched: Fraction(count, sum(counts.values()))
            for unmatched, count in counts.items()}


def product_densities(a, g):
    return [a[i] * prod(Fraction(1)-a[j]*g for j in range(len(a)) if j != i)
            for i in range(len(a))]


def prod(values):
    out = Fraction(1)
    for v in values:
        out *= v
    return out


def polynomial_ode_check(a, g):
    F = prod(1-ai*g for ai in a)
    x = product_densities(a, g)
    for i in range(len(a)):
        dxi_dg = -a[i]*sum((a[j]*prod(1-a[h]*g for h in range(len(a))
                             if h != i and h != j) for j in range(len(a)) if j != i), Fraction(0))
        assert dxi_dg * F == -x[i] * sum(x[j] for j in range(len(a)) if j != i)
    return True


def matching_trial(part_sizes, rng):
    st = list(part_sizes)
    while True:
        pairs = edge_types(st)
        W = sum(w for _, _, w in pairs)
        if not W:
            return tuple(st)
        z = rng.randrange(W)
        for i, j, w in pairs:
            if z < w:
                st[i] -= 1
                st[j] -= 1
                break
            z -= w


def predicted_unmatched(a):
    maximum = max(a)
    if a.count(maximum) > 1:
        return Fraction(0)
    k = a.index(maximum)
    return a[k] * prod(1-a[j]/maximum for j in range(len(a)) if j != k)


def main():
    checks = 0
    for state in [(1,1,1), (2,1,1), (2,2,1), (2,1,1,1)]:
        assert final_law(state) == exhaustive_priority_law(state)
        assert sum(final_law(state).values(), Fraction(0)) == 1
        checks += 2
    for state in [(2,2,2), (3,2,1), (4,3,2,1), (3,1,1,1,1)]:
        law = final_law(state)
        assert sum(law.values(), Fraction(0)) == 1
        assert all(u >= 0 and u % 2 == sum(state) % 2 for u in law)
        checks += 2
    for a in ((Fraction(2,5), Fraction(7,20), Fraction(1,4)),
              (Fraction(2,5), Fraction(2,5), Fraction(1,5)),
              (Fraction(7,20),Fraction(3,10),Fraction(1,5),Fraction(3,20)),
              (Fraction(1,3),Fraction(1,4),Fraction(1,5),Fraction(1,8),Fraction(11,120))):
        assert sum(a) == 1
        for g in (Fraction(0), Fraction(1,7), Fraction(1,2)):
            assert polynomial_ode_check(a, g)
            checks += 1
        amax = max(a)
        endpoint = Fraction(1, 1) / amax
        terminal = product_densities(a, endpoint)
        assert sum(terminal) == predicted_unmatched(a)
        assert sum(x != 0 for x in terminal) == (1 if a.count(amax)==1 else 0)
        checks += 2
    a = (Fraction(2,5), Fraction(7,20), Fraction(1,4))
    assert predicted_unmatched(a) == Fraction(3,160)
    checks += 1
    rng = Random(20261015)
    parts = [800, 700, 500]
    observations = [sum(matching_trial(parts, rng)) for _ in range(48)]
    average = sum(observations)/len(observations)/sum(parts)
    assert abs(average-float(predicted_unmatched(a))) < 0.006
    print(f'PASS: {checks} exact identities/checks and one seeded finite-size consistency check.')
    print(f'Exact asymptotic unmatched density for (2/5,7/20,1/4): {predicted_unmatched(a)}')
    print(f'Finite-size sample mean at N={sum(parts)}: {average:.8f}; sample range {min(observations)}..{max(observations)} unmatched vertices.')
    print('Finite exact calculations and simulations are NOT proofs of the large-system limit.')


if __name__ == '__main__':
    main()
