"""Independent exhaustive finite check of the sequential critical bi-threshold theorem.

Run: python3 verify.py. No third-party packages are required.
"""
from collections import Counter
from itertools import product
from math import comb
from random import Random


def sweep(bits, n, up, order):
    """Update a Boolean complete graph one vertex at a time, including self in the count."""
    current = list(bits)
    for vertex in order:
        total = sum(current)
        if current[vertex] == 0:
            current[vertex] = int(total >= up)
        else:
            current[vertex] = int(total >= up + 2)
    return tuple(current)


def periodic_states(n, up, order):
    fixed = {tuple([0] * n), tuple([1] * n)}
    if n % 2 == 1 and up == (n - 1) // 2:
        a = [0] * n
        for j, i in enumerate(order):
            a[i] = j % 2
        a = tuple(a)
        b = tuple(1 - v for v in a)
        assert sweep(a, n, up, order) == b
        assert sweep(b, n, up, order) == a
        return fixed | {a, b}
    return fixed


def prediction(n, up, state, order):
    ordered = [state[i] for i in order]
    m = sum(state)
    is_alt = n % 2 == 1 and up == (n - 1) // 2 and all(
        ordered[i] != ordered[i+1] for i in range(n-1)
    )
    if m in (0, n) or is_alt:
        return 0
    signature = ((m == up and ordered[:2] == [0, 1]) or
                 (m == up + 1 and ordered[:2] == [1, 0]))
    return 2 if signature else 1


def verify():
    random = Random(29017)
    total = 0
    comparisons = 0
    for n in range(3, 15):
        for up in range(1, n-1):
            order = tuple(range(n))
            fixed_or_cycle = periodic_states(n, up, order)
            shells = Counter()
            cycles = set()
            for x in product((0, 1), repeat=n):
                total += 1
                z = x
                observed = None
                for t in range(4):
                    if z in fixed_or_cycle:
                        observed = t
                        break
                    z = sweep(z, n, up, order)
                assert observed is not None, (n, up, x)
                assert observed == prediction(n, up, x, order), (n, up, x, observed)
                shells[observed] += 1
            delta = int(n % 2 == 1 and up == (n - 1)//2)
            exact = (2 + 2*delta, 2**n - 2 - comb(n-1, up),
                     comb(n-1, up) - 2*delta)
            assert tuple(shells[t] for t in range(3)) == exact, (n, up, shells, exact)
            for state in fixed_or_cycle:
                fstate = sweep(state, n, up, order)
                assert fstate in fixed_or_cycle
            comparisons += 1
            if n <= 9:
                for _ in range(7):
                    perm = list(range(n)); random.shuffle(perm)
                    perm = tuple(perm)
                    pset = periodic_states(n, up, perm)
                    observed_shells = Counter()
                    for x in product((0, 1), repeat=n):
                        z=x
                        for t in range(4):
                            if z in pset: break
                            z = sweep(z, n, up, perm)
                        else: raise AssertionError('unsettled randomized permutation')
                        assert t == prediction(n, up, x, perm)
                        observed_shells[t] += 1
                    assert tuple(observed_shells[t] for t in range(3)) == exact
    print('SEQ_BITHRESHOLD_ALL_CHECKS_PASSED')
    print('identity_order_configurations_checked', total)
    print('dimension_threshold_pairs', comparisons)
    print('additional_permutation_checks', sum((n-2)*7 for n in range(3, 10)))
    print('all_infinite_size_claims_derive_from_proof_not_enumeration')

if __name__ == '__main__':
    verify()
