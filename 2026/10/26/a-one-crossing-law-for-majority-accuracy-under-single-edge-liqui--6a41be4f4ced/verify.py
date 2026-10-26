"""Independent exact-rational checks of a single-delegation voting theorem.

Run: python3 verify.py
Uses only Python's standard library; no stochastic simulation.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import random


def exact_gain(competences):
    """Exact change in correct-majority probability after voter 0 delegates to 1.

    Under direct voting each has weight 1. Under delegation voter 0
    has weight 0 and voter 1 weight 2. The remaining weights are 1.
    """
    n = len(competences)
    assert n >= 3 and n % 2 == 1
    threshold = n // 2 + 1
    result = F(0)
    for x in product((0, 1), repeat=n):
        mass = F(1)
        for p, bit in zip(competences, x):
            mass *= p if bit else 1-p
        regular = sum(x) >= threshold
        delegated = 2*x[1] + sum(x[2:]) >= threshold
        result += mass * (int(delegated) - int(regular))
    return result


def boundary_gain(competences):
    """Independently convolve background voters; use two pivot masses."""
    n = len(competences)
    m = (n - 1) // 2
    pmf = [F(1)]
    for p in competences[2:]:
        next_pmf = [F(0)]*(len(pmf)+1)
        for k, prob in enumerate(pmf):
            next_pmf[k] += prob*(1-p)
            next_pmf[k+1] += prob*p
        pmf = next_pmf
    a, b = competences[:2]
    return b*(1-a)*pmf[m-1] - a*(1-b)*pmf[m]


def homogeneous_gain(m, a, b, q):
    return F(comb(2*m-1, m-1)) * (q*(1-q))**(m-1) * ((1-q)*b*(1-a) - q*a*(1-b))


def two_state(m, prior, a, b, q0, q1):
    return prior*homogeneous_gain(m, a, b, q0) + (1-prior)*homogeneous_gain(m, a, b, q1)


def main():
    random.seed(102761)
    n_tests = 0
    # Testing the pivotal formula against full enumeration, not the same
    # binomial simplification, for independently chosen rational competence
    # vectors. In particular, backgrounds need not be identical.
    choices = [F(1,5), F(2,5), F(1,2), F(3,5), F(4,5)]
    for n, trials in [(3,75), (5,70), (7,45), (9,20), (11,10)]:
        for _ in range(trials):
            p = [random.choice(choices) for _ in range(n)]
            assert exact_gain(p) == boundary_gain(p), (n, p)
            n_tests += 1
    n_binom = 0
    for m in range(1, 9):
        for a in [F(2,5), F(3,5), F(4,5)]:
            for b in [F(2,5), F(3,5), F(4,5)]:
                for q in [F(2,5), F(3,5), F(4,5)]:
                    if m <= 6:
                        assert exact_gain([a,b]+[q]*(2*m-1)) == homogeneous_gain(m,a,b,q)
                    else:
                        assert boundary_gain([a,b]+[q]*(2*m-1)) == homogeneous_gain(m,a,b,q)
                    n_binom += 1

    a, b, q0, q1, prior = F(3,5), F(4,5), F(3,5), F(4,5), F(1,3)
    outcomes = []
    for m in range(1, 21):
        x = two_state(m, prior, a, b, q0, q1)
        if m <= 6:
            raw = prior*exact_gain([a,b]+[q0]*(2*m-1)) + (1-prior)*exact_gain([a,b]+[q1]*(2*m-1))
            assert raw == x
        outcomes.append(x)
    assert outcomes[0] == -F(1,375), outcomes[0]
    assert outcomes[1] == F(2,625), outcomes[1]
    assert all(x > 0 for x in outcomes[1:])
    # Check that the claimed simplified rational formula matches all samples.
    for m, val in enumerate(outcomes, start=1):
        expected = F(comb(2*m-1,m-1),375) * (7*F(6,25)**(m-1) - 8*F(4,25)**(m-1))
        assert expected == val
    print('PASS: arbitrary-vector complete-exhaustion checks:', n_tests)
    print('PASS: homogeneous binomial comparisons:', n_binom)
    print('PASS: mixture exact/closed comparisons for n=3..11; 20 signs')
    print('n=3 exact ex-ante gain:', outcomes[0])
    print('n=5 exact ex-ante gain:', outcomes[1])
    print('All checks use rational numbers; no Monte Carlo.')

if __name__ == '__main__':
    main()
