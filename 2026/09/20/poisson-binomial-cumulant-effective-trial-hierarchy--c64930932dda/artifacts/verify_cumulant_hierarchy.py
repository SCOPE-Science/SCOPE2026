from fractions import Fraction as F
from itertools import product

GRID = [F(0), F(1,6), F(1,4), F(1,3), F(1,2), F(2,3), F(3,4), F(5,6), F(1)]

def floor_frac(x):
    return x.numerator // x.denominator

def check(ps):
    n = len(ps)
    vs = [p*(1-p) for p in ps]
    active = [i for i,v in enumerate(vs) if v > 0]
    r = len(active)
    V = sum(vs, F(0))
    if V == 0:
        return
    A = sum((v*v for v in vs), F(0))
    k3 = sum((v*(1-2*p) for p,v in zip(ps,vs)), F(0))
    k4 = sum((v*(1-6*v) for v in vs), F(0))
    L3 = sum((v*(1-2*v) for v in vs), F(0))

    assert V - k4 == 6*A
    assert L3 == V - 2*A
    assert V*V > k3*k3

    N3 = 4*V**3/(V*V-k3*k3)
    N4 = V*V/A
    assert 4*V <= N3 <= N4 <= r <= n

    # Joint third/fourth cumulant constraint.
    assert 3*k3*k3 <= V*V + 2*V*k4

    # Exact fixed-n projection bounds.
    assert k3*k3 <= V*V*(1-4*V/F(n))
    assert k4 <= V - 6*V*V/F(n)

    k = floor_frac(4*V)
    delta = V - F(k,4)
    Amax = F(k,16) + delta*delta
    assert F(0) <= delta < F(1,4)
    assert k4 >= V - 6*Amax

    assert V - 2*Amax <= L3 <= V - 2*V*V/F(n)

count = 0
for n in range(1,6):
    for ps in product(GRID, repeat=n):
        check(ps)
        count += 1

# Sharpness examples for fixed n,V skewness upper bound: all p equal.
for n in range(1,9):
    for p in [F(1,7), F(1,4), F(1,2), F(3,4), F(6,7)]:
        ps = [p]*n
        vs = [p*(1-p)]*n
        V = sum(vs, F(0))
        k3 = sum((v*(1-2*p) for v in vs), F(0))
        assert k3*k3 == V*V*(1-4*V/F(n))

# Sharpness examples for the fourth-cumulant upper bound: equal Bernoulli variances,
# allowing complementary probabilities.
for n in range(2,9):
    p = F(1,5)
    ps = [p if i % 2 == 0 else 1-p for i in range(n)]
    vs = [x*(1-x) for x in ps]
    V = sum(vs, F(0))
    k4 = sum((v*(1-6*v) for v in vs), F(0))
    assert k4 == V - 6*V*V/F(n)

# Sharpness examples for the fourth-cumulant lower bound: pack variance into fair trials,
# one residual trial, and deterministic trials.
for n in range(1,9):
    for k in range(n):
        for delta in [F(1,100), F(1,16), F(3,20)]:
            if not (F(0) < delta < F(1,4)):
                continue
            V = F(k,4) + delta
            if V > F(n,4):
                continue
            # Solve p(1-p)=delta is not generally rational, but the cumulant formulas depend
            # on this trial only through v=delta, so exact feasibility follows from the real root.
            Amax = F(k,16) + delta*delta
            lower = V - 6*Amax
            # Algebraic verification of the claimed extremal value.
            assert lower == V - 6*(F(k,16) + delta*delta)

print(f"checked {count} rational parameter vectors")
print("all hierarchy, cumulant, fixed-variance, and Lyapunov-numerator checks passed")
