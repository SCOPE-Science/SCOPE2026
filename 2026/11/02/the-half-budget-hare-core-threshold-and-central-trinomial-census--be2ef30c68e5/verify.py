"""Exact independent enumeration for a cyclic two-approval committee election.

Each voter i approves candidates i and (i+1) modulo n. The Hare core
condition is checked directly against every nonempty affordable proposal.
Only small finite instances are enumerated; the general theorem has an
analytical proof.
"""
from itertools import combinations
from math import comb, factorial


def utility_vector(mask, n):
    return tuple(((mask >> i) & 1) + ((mask >> ((i + 1) % n)) & 1)
                 for i in range(n))


def in_core_direct(winners, n, k, proposal_data):
    current = utility_vector(winners, n)
    for proposal_size, proposal_utility in proposal_data:
        supporters = sum(after > before for before, after in zip(current, proposal_utility))
        if supporters * k >= n * proposal_size:
            return False
    return True


def has_three_cyclic_vacancies(winners, n):
    return any(all(not (winners >> ((i + d) % n)) & 1 for d in range(3))
               for i in range(n))


def central_trinomial(k):
    return sum(factorial(k) // (factorial(j)**2 * factorial(k-2*j))
               for j in range(k//2 + 1))


def enumerate_case(n, k):
    proposals = []
    for t in range(1, k+1):
        for subset in combinations(range(n), t):
            mask = sum(1 << x for x in subset)
            proposals.append((t, utility_vector(mask, n)))
    total = 0
    stable = 0
    for subset in combinations(range(n), k):
        w = sum(1 << x for x in subset)
        direct = in_core_direct(w, n, k, proposals)
        if n == 2*k:
            predicted = not has_three_cyclic_vacancies(w, n)
        elif 2*k < n:
            predicted = True
        else:
            raise ValueError('Unclaimed regime')
        assert direct == predicted, (n, k, subset, direct, predicted)
        total += 1
        stable += direct
    if n == 2*k:
        assert stable == 2*central_trinomial(k), (n, k, stable)
    else:
        assert stable == comb(n,k)
    return stable, total


def main():
    for k in range(1, 7):
        n=2*k
        stable, total=enumerate_case(n,k)
        print(f'half quota: n={n} k={k} core={stable} total={total} central={central_trinomial(k)}')
    for n in range(3,10):
        for k in range(1,(n-1)//2+1):
            if 2*k>=n:
                continue
            stable,total=enumerate_case(n,k)
            print(f'below half: n={n} k={k} core={stable} total={total}')
    assert enumerate_case(6,3)==(14,20)
    print('All direct core tests and independent gap predictions agree.')

if __name__=='__main__':
    main()
