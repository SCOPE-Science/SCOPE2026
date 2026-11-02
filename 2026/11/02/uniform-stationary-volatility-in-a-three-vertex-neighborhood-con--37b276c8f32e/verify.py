"""Exact-rational checks for the three-vertex neighborhood-DW reduction.

Usage: python verify.py
The proof in RESULT.md covers arbitrary admissible parameters. This script
checks independent finite instances and exact finite-time distributions.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product

EDGES = ((0, 1), (1, 2))
NEIGHBORS = ((1,), (0, 2), (1,))


def full_step(x, edge_index, sigma, eps, rho):
    """Direct implementation of the asymmetric equation (3) on a path."""
    old = tuple(x)
    i, j = EDGES[edge_index]
    out = list(old)
    for receiver, donor in ((i, j), (j, i)):
        mean_donor_neighborhood = sum(old[k] for k in NEIGHBORS[donor]) / len(NEIGHBORS[donor])
        direct = abs(old[receiver] - old[donor])
        transitive = abs(old[receiver] - mean_donor_neighborhood)
        if sigma * direct + (1-sigma) * transitive < eps:
            out[receiver] = old[receiver] + rho * (old[donor] - old[receiver])
    return tuple(out)


def reduced_step(y, endpoint, rho):
    return (1-rho) * y + rho * endpoint


def grid_law(a, b, y0, t):
    n = 2**t
    return {a + (y0 - a + k * (b - a)) / n: Q(1, n) for k in range(n)}


def quantile_w1_from_discrete_uniform(law, a, b):
    """Exact integral of the distance between quantile functions."""
    positions = sorted(law.items())
    total = Q(0)
    left = Q(0)
    for atom, mass in positions:
        right = left + mass
        split = (atom-a)/(b-a)
        split = min(right, max(left, split))
        def primitive(t):
            return (b-a)*t*t/Q(2) + (a-atom)*t
        # Integrating |a+(b-a)u-atom| across the quantile interval.
        total += -(primitive(split)-primitive(left)) + (primitive(right)-primitive(split))
        left = right
    assert left == 1
    return total


def test_parameter_wedge():
    tested = 0
    configurations = [
        (Q(0), Q(1), Q(0), Q(1,4), Q(1,2)),
        (Q(0), Q(1), Q(1,4), Q(3,10), Q(1,2)),
        (Q(1,8), Q(7,8), Q(1,5), Q(1,4), Q(1,3)),
        (Q(0), Q(1), Q(1,3)-Q(1,300), Q(1,3), Q(1,4)),
    ]
    for a,b,sigma,eps,rho in configurations:
        d=b-a
        assert 0 <= sigma < Q(1,3)
        assert sigma*d < eps <= (1-sigma)*d/2
        for k in range(101):
            y=a + d*Q(k,100)
            for edge_index in (0,1):
                result = full_step((a,y,b),edge_index,sigma,eps,rho)
                assert result[0] == a and result[2] == b
                donor=a if edge_index==0 else b
                assert result[1] == reduced_step(y,donor,rho)
                tested += 1
    return tested


def test_path_distribution():
    tested=0
    for a,b,y0 in ((Q(0),Q(1),Q(1,2)),(Q(1,8),Q(7,8),Q(1,4)),(Q(0),Q(3,4),Q(0))):
        for t in range(0,9):
            law=Counter({y0:Q(1)})
            for _ in range(t):
                nxt=Counter()
                for y,p in law.items():
                    nxt[(y+a)/2] += p/2
                    nxt[(y+b)/2] += p/2
                law=nxt
            assert dict(law)==grid_law(a,b,y0,t)
            expected=((y0-a)**2+(b-y0)**2)/(2*(b-a)*2**t)
            assert quantile_w1_from_discrete_uniform(law,a,b)==expected
            tested+=1
    return tested


def test_stationary_moments():
    # For affine recursion Y'=(1-rho)Y+rho Z, with Z equal endpoints.
    tested=0
    for rho in (Q(1,10),Q(1,4),Q(1,3),Q(1,2)):
        for a,b in ((Q(0),Q(1)),(Q(1,7),Q(5,7))):
            mean=(a+b)/2
            var=rho*(b-a)**2/(4*(2-rho))
            assert mean==(1-rho)*mean+rho*(a+b)/2
            assert var == (1-rho)**2*var + rho**2*(b-a)**2/4
            tested+=1
    return tested


if __name__=='__main__':
    print('Direct mixed-confidence update checks:',test_parameter_wedge())
    print('Exact finite laws and Wasserstein integrals:',test_path_distribution())
    print('Stationary mean/variance identities:',test_stationary_moments())
    print('All tests passed')
