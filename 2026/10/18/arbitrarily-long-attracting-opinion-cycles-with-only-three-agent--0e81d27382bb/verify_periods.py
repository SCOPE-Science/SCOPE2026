"""Exact rational checks for attracting cycles in symmetric set-confidence averaging."""
from fractions import Fraction

def fixture(period):
    assert period >= 2
    q = 2**period - 1
    xs = [Fraction(2**(period - 1 - i), q) for i in range(period)]
    selected = {Fraction(0), *xs[:-1], 1 - xs[-1]}
    rejected = {xs[-1], *(1-x for x in xs[:-1])}
    delta = Fraction(1, 100*q)
    assert selected.isdisjoint(rejected)
    assert min(abs(a-b) for a in selected for b in rejected) >= Fraction(1, q)
    # Symmetric open set: union of balls of radius delta about +-selected.
    centers = selected | {-a for a in selected}
    def conf(z):
        return any(abs(z-c) < delta for c in centers)
    def update(x):
        if conf(-x):
            neigh_left = [Fraction(0)]
        else: neigh_left = []
        if conf(1-x):
            neigh_right = [Fraction(1)]
        else: neigh_right = []
        return (x + sum(neigh_left) + sum(neigh_right))/(1+len(neigh_left)+len(neigh_right))
    # Read the actual update and check all p exact identities and itinerary.
    for i, x in enumerate(xs):
        assert conf(-x) == (i < period-1)
        assert conf(1-x) == (i == period-1)
        assert update(x) == xs[(i+1) % period]
    assert len(set(xs)) == period
    # Perturbed initial values remain in the same itinerary, converge by exact factor 2^-p per lap.
    for perturb in (-delta/4,delta/4):
        x = xs[0]+perturb
        for lap in range(4):
            for i in range(period):
                assert abs(x-xs[i]) < delta/2
                x = update(x)
            assert x-xs[0] == perturb/Fraction(2**(period*(lap+1)))
    return q, xs, centers

if __name__=='__main__':
    for period in range(2,41):
        q, xs, centers = fixture(period)
        if period in (2,3,4,8,16,40):
            print(f'period={period} denominator={q} orbit={xs if period<=4 else "omitted"} centers={len(centers)}')
    print('PASS exact-rational proof-ingredient checks for periods 2 through 40; 312 perturbed laps')
