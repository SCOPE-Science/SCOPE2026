from fractions import Fraction as Q

def ratio(a, t):
    return (1 - a*t)**2

def step(a, x, t, c0, c1, gamma, prev_t):
    xn = (1 - a*t)*x
    delta = xn - x
    A = a*delta*delta
    assert A == a*delta*delta
    if A > (c0/t)*delta*delta:
        tn = c1*delta*delta/A
        assert tn == c1/a
        branch = "reset"
    else:
        gp = gamma
        # All expansion checks below use t/prev_t >= 1, so the ratio cap is inactive.
        assert t/prev_t >= 1
        tn = (1 + gp)*t
        branch = "expand"
    return xn, tn, branch

a = Q(3)
c0 = Q(1, 2)
c1 = Q(1, 4)
x0 = Q(2)
t0 = c0/a

for gamma0 in [Q(1), Q(4), Q(20), Q(100)]:
    x1, t1, b0 = step(a, x0, t0, c0, c1, gamma0, t0)
    assert b0 == "expand"
    assert t1 == (1 + gamma0)*t0
    assert ratio(a, t0) == (1 - c0)**2

    # At k=1 the curvature condition fires because a*t1>c0.
    x2 = (1 - a*t1)*x1
    delta = x2 - x1
    A = a*delta*delta
    assert A > (c0/t1)*delta*delta
    t2 = c1*delta*delta/A
    assert t2 == c1/a
    assert ratio(a, t1) == (1 - c0*(1 + gamma0))**2

# Sharp expansion-safety boundary from a*t=c0.
gsafe = 2/c0 - 1
tsafe = (1 + gsafe)*t0
assert a*tsafe == 2
assert ratio(a, tsafe) == 1

gbad = gsafe + Q(1, 10)
tbad = (1 + gbad)*t0
assert a*tbad > 2
assert ratio(a, tbad) > 1

print("VERIFY_OK")
