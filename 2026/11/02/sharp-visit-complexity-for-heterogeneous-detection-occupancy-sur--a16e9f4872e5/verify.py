"""Exact rational checks for heterogeneous site detection designs.

Python 3 standard library only. Run: python verify.py
The general theorem is analytic; these checks test concrete boundary examples.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def solve(A, b):
    n = len(b)
    M = [[F(v) for v in row] + [F(b[i])] for i, row in enumerate(A)]
    for i in range(n):
        p = next(j for j in range(i, n) if M[j][i])
        M[i], M[p] = M[p], M[i]
        z = M[i][i]
        M[i] = [v / z for v in M[i]]
        for j in range(n):
            if i != j:
                z = M[j][i]
                M[j] = [M[j][h] - z * M[i][h] for h in range(n+1)]
    return [row[-1] for row in M]


def law(durations, nodes, masses):
    assert len(nodes) == len(masses)
    assert all(F(0) < x < F(1) for x in nodes)
    assert all(a > 0 for a in masses) and sum(masses) < 1
    out = {}
    for bits in product((0, 1), repeat=len(durations)):
        prob = (1-sum(masses)) if not any(bits) else F(0)
        for x, a in zip(nodes, masses):
            term = a
            for duration, bit in zip(durations, bits):
                z = x ** duration
                term *= (1-z) if bit else z
            prob += term
        out[bits] = prob
    assert sum(out.values()) == 1
    return out


def absence(law_dict, indices):
    return sum(p for bits, p in law_dict.items() if all(bits[i] == 0 for i in indices))


def moments_from_binary_law(law_dict, durations):
    values = {0: F(1)}
    for selection in product((0, 1), repeat=len(durations)):
        if not any(selection):
            continue
        S = tuple(i for i, b in enumerate(selection) if b)
        val = absence(law_dict, S)
        t = sum(durations[i] for i in S)
        if t in values:
            assert val == values[t]
        else:
            values[t] = val
    return values


def prony_coefficients(Fvals, k):
    # Finite differencing removes the known zero-rate/absent component.
    g = [Fvals[j]-Fvals[j+1] for j in range(2*k)]
    H = [[g[i+j] for j in range(k)] for i in range(k)]
    c = solve(H, [-g[k+i] for i in range(k)])
    return c + [F(1)], g


def evaluate(coefficients, x):
    return sum(c*x**j for j, c in enumerate(coefficients))


def test_exact_recovery(nodes, masses, durations):
    k = len(nodes)
    observed = law(durations, nodes, masses)
    vals = moments_from_binary_law(observed, durations)
    assert set(range(2*k+1)) <= set(vals)
    coeff, g = prony_coefficients(vals, k)
    assert all(evaluate(coeff, x) == 0 for x in nodes)
    recovered_b = solve([[x**j for x in nodes] for j in range(k)], g[:k])
    assert recovered_b == [a*(1-x) for x, a in zip(nodes, masses)]
    assert [b/(1-x) for b, x in zip(recovered_b, nodes)] == masses
    assert 1-sum(masses) > 0
    for j in range(2*k+1):
        assert vals[j] == 1-sum(masses)+sum(a*x**j for x,a in zip(nodes,masses))
    return len(observed), max(vals)


def main():
    for k, nodes, masses, durations in [
        (1, [F(2,5)], [F(3,4)], [1,1]),
        (2, [F(1,4),F(3,4)], [F(2,5),F(2,5)], [1,1,2]),
        (3, [F(1,5),F(1,2),F(4,5)], [F(1,10),F(1,5),F(1,4)], [1,2,4]),
        (4, [F(1,6),F(2,5),F(3,5),F(5,6)], [F(1,12),F(1,8),F(1,10),F(1,6)], [1,2,4,8]),
    ]:
        ncases, biggest = test_exact_recovery(nodes,masses,durations)
        print('Recovered', k, 'positive detection classes from', len(durations), 'visits;', ncases, 'binary histories; max subset duration', biggest)

    # Three equal visits do not identify occupancy, even for two detection classes.
    # x=1-p is the one-unit nondetection probability.
    A = law([1,1,1], [F(3,4), F(1,4)], [F(2,5),F(2,5)])
    B = law([1,1,1], [F(4,5),F(9,34)], [F(75,182),F(4913,11375)])
    assert A == B
    assert 1 - F(2,5) - F(2,5) != 1 - F(75,182) - F(4913,11375)
    print('Exact three-equal-visit nonidentifiability:', 'occupancies', F(4,5), F(211,250))

    # The extra fourth exposure sum from the unequal (1,1,2) design separates them.
    C = law([1,1,2], [F(3,4), F(1,4)], [F(2,5),F(2,5)])
    D = law([1,1,2], [F(4,5),F(9,34)], [F(75,182),F(4913,11375)])
    assert C != D
    assert absence(C, (0,1,2)) != absence(D, (0,1,2))
    print('Unequal-effort design separates the two exact models.')

    for k in range(1,11):
        from math import ceil, log2
        n = (2*k+1 - 1).bit_length()
        assert 2**(n-1)-1 < 2*k <= 2**n-1
        assert len({sum((1<<j) for j in range(n) if mask & (1<<j)) for mask in range(2**n)}) == 2**n
    print('Binary subset-sum visit bound checked for k=1,...,10.')
    print('ALL EXACT TESTS PASSED')

if __name__ == '__main__':
    main()
