"""Reproduce finite-circle random sequential adsorption calculations.

Unit-length rods arrive at unit intensity per unit circumference.  This
checks the exact low-capacity gap formulas and constructive witnesses.
The all-circumference theorem is proved analytically in RESULT.md.
"""
import math
import random


def available_length(positions, L):
    pts = sorted(p % L for p in positions)
    if len(pts) == 0:
        return L
    if len(pts) == 1:
        return max(0.0, L - 2.0)
    gaps = [pts[i + 1] - pts[i] for i in range(len(pts) - 1)]
    gaps.append(L - pts[-1] + pts[0])
    return sum(max(0.0, g - 2.0) for g in gaps)


def conditional_tail(L, y, t):
    rate = max(0.0, y - 2.0) + max(0.0, L - y - 2.0)
    return math.exp(-rate * t) if rate > 0 else 0.0


def exact_tail(L, t):
    a = L - 3.0
    if t == 0:
        return 2.0 * a / (L - 2.0)
    return -2.0 * math.expm1(-a * t) / ((L - 2.0) * t)


def midpoint_integral(f, a, b, n=12000):
    dx = (b - a) / n
    return dx * sum(f(a + (i + 0.5)*dx) for i in range(n))


def check_tail_and_gap():
    rng = random.Random(20261013)
    for L in (3.02, 3.25, 3.7, 4.0):
        for t in (0.0, 0.2, 1.0, 5.0, 20.0, 100.0):
            integral = (midpoint_integral(lambda y: conditional_tail(L, y, t), 1.0, L-2.0) + midpoint_integral(lambda y: conditional_tail(L, y, t), 2.0, L-1.0))/(L-2.0)
            analytic = exact_tail(L, t)
            assert abs(integral-analytic) < 1.0e-7, (L,t,integral,analytic)
        # Independently compute admissible area from the two cyclic gaps.
        for _ in range(400):
            y = 1.0 + (L-2.0)*rng.random()
            observed = available_length([0.0,y],L)
            expected = max(0.0,y-2.0)+max(0.0,L-y-2.0)
            assert abs(observed-expected)<1.0e-12
        for t in (1.0, 10.0):
            n=120000
            observed=sum(conditional_tail(L,1+(L-2)*rng.random(),t) for _ in range(n))/n
            predicted=exact_tail(L,t)
            assert abs(observed-predicted)<0.008, (L,t,observed,predicted)
        for t in (1.0e5,1.0e6):
            assert abs(t*exact_tail(L,t)-2.0/(L-2.0))<1.e-12
    print('PASS: exact two-gap rates, integrated survival laws, sampled survival, tails')


def check_general_witness():
    for L in (4.0001,4.01,4.37,4.99,5.0,5.99,6.0,6.8,9.0,100.3):
        k = math.floor(L/2)+1
        assert k+1<L<2*k
        eps = min(0.01,(L-k-1)/4,(2*k-L)/4)
        g0=2.0+eps
        other=(L-g0)/(k-1)
        assert 1<other<2 and g0>2
        positions=[0.0]
        for gap in [g0]+[other]*(k-2):
            positions.append(positions[-1]+gap)
        gaps=[positions[i+1]-positions[i] for i in range(k-1)]+[L-positions[-1]]
        assert abs(sum(gaps)-L)<1.e-10
        assert all(g>1 for g in gaps)
        assert sum(g>2 for g in gaps)==1
        assert abs(available_length(positions,L)-eps)<1.e-9
    print('PASS: near-pinched positive-volume k-center witnesses for L>4')


def check_first_stage():
    for L in (1.0,1.5,2.0,2.01,2.75,3.0,3.1,3.9):
        assert available_length([],L)==L
        assert abs(available_length([0.5],L)-max(0,L-2))<1.e-12
        if L<=3.0:
            predicted=1/L+(1/(L-2) if L>2 else 0)
            assert math.isfinite(predicted)
    print('PASS: finite first and second waiting-stage rates and endpoint cases')


if __name__ == '__main__':
    check_first_stage()
    check_tail_and_gap()
    check_general_witness()
