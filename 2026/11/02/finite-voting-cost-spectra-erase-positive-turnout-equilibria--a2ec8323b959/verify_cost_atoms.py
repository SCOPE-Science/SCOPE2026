"""Exact-arithmetic checks for the finite-cost spatial voting theorem.

Run with Python 3 using only the standard library. The universal proof is
mathematical; this script tests its algebra on representative finite families.
"""
from fractions import Fraction as F
from itertools import combinations


def costs(records):
    assert records and sum((w for _, w in records), F(0)) == 1
    assert all(c >= 0 and w > 0 for c, w in records)
    return sorted(records)


def voter_cdf(x, shape):
    assert 0 <= x <= 1
    if shape == 1:
        return x
    if shape == 2:
        return x*x
    if shape == 3:
        return (x + 2*x*x)/3
    raise ValueError(shape)


def vote_mass(me, other, records, shape):
    if me == other:
        return F(0)
    delta = abs(me-other)
    if me < other:
        return sum((weight*voter_cdf((me+other-c)/2, shape)
                    for c, weight in records if c < delta), F(0))
    return sum((weight*(1-voter_cdf((me+other+c)/2, shape))
                for c, weight in records if c < delta), F(0))


def test_exact_phase():
    examples = [
        costs([(F(1, 4), F(1))]),
        costs([(F(1, 3), F(2, 5)), (F(2, 3), F(3, 5))]),
        costs([(F(1, 2), F(1, 2)), (F(5, 6), F(1, 2))]),
        costs([(F(3, 4), F(1))]),
        costs([(F(3, 5), F(1, 3)), (F(4, 5), F(2, 3))]),
        costs([(F(1), F(1))]),
        costs([(F(5, 4), F(1))]),
    ]
    grid = [F(i, 12) for i in range(13)]
    active_checks = zero_checks = no_deviation_checks = 0
    for records in examples:
        smallest = records[0][0]
        lo, hi = max(F(0), 1-smallest), min(F(1), smallest)
        for shape in (1, 2, 3):
            for a in grid:
                for b in grid:
                    gap = abs(a-b)
                    wa = vote_mass(a,b,records,shape)
                    wb = vote_mass(b,a,records,shape)
                    if gap > smallest:
                        assert wa > 0 and wb > 0
                        left, right = sorted((a,b))
                        active = [c for c, _ in records if c < gap]
                        eps = min([gap] + [gap-c for c in active]) / 2
                        assert eps > 0
                        assert [c for c, _ in records if c < gap-eps] == active
                        assert vote_mass(left+eps,right,records,shape) > vote_mass(left,right,records,shape)
                        active_checks += 1
                    elif lo <= a <= hi and lo <= b <= hi:
                        assert wa == wb == 0
                        for dev in grid:
                            assert vote_mass(dev,b,records,shape) == 0
                            assert vote_mass(dev,a,records,shape) == 0
                            no_deviation_checks += 2
                    else:
                        assert wa == wb == 0
                        # At least one opposing position admits a positive-vote endpoint deviation.
                        can_a = max(vote_mass(F(0),b,records,shape),
                                    vote_mass(F(1),b,records,shape)) > 0
                        can_b = max(vote_mass(F(0),a,records,shape),
                                    vote_mass(F(1),a,records,shape)) > 0
                        assert can_a or can_b
                        zero_checks += 1
    return active_checks, zero_checks, no_deviation_checks


def test_uniform_continuum():
    a, b = F(1, 4), F(3, 4)
    # Exact integral of turnout probability K(t)=t over uniformly distributed ideals.
    def continuum_mass(me, other):
        if me == other:
            return F(0)
        d = abs(me-other)
        if me < other:
            return d*me + d*d/4
        return d*(1-me) + d*d/4
    optimum = continuum_mass(a,b)
    assert optimum == F(3,16)
    for j in range(1001):
        t = F(j,1000)
        assert continuum_mass(t,b) <= optimum
        assert continuum_mass(t,a) <= optimum
    # Derivative of the left-candidate quadratic vanishes at b/3=a.
    assert b/3 == a
    assert (2+a)/3 == b
    # Opposite-side best-response candidate gets only 1/48.
    assert continuum_mass(F(11,12),b) == F(1,48)
    return 2002


def test_discretization():
    cases = 0
    for m in range(2, 101):
        costs_grid = [(F(j,m+1), F(1,m)) for j in range(1,m+1)]
        assert costs_grid[0][0] < F(1,2)
        # For a finite empirical CDF it suffices to check jump locations and left limits.
        max_gap = F(0)
        for j in range(1,m+1):
            t = F(j,m+1)
            max_gap = max(max_gap, abs(F(j,m)-t), abs(F(j-1,m)-t))
        assert max_gap <= F(1,m+1)
        cases += 1
    return cases


if __name__ == '__main__':
    a,b,c = test_exact_phase()
    u = test_uniform_continuum()
    d = test_discretization()
    print(f'VERIFY_OK active_strict_improvements={a} zero_turnout_profitable_deviations={b} no_deviation_checks={c} continuum_best_response_samples={u} empirical_cost_distributions={d}')
