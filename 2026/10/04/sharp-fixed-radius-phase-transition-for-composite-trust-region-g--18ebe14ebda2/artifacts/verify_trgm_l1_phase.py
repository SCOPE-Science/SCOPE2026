from fractions import Fraction as Q

def minimizers(x, eta, theta):
    lo = x - eta
    hi = x + eta
    if x > theta:
        return lo, lo
    if x < -theta:
        return hi, hi
    if -theta < x < theta:
        if lo <= 0 <= hi:
            return Q(0), Q(0)
        if lo > 0:
            return lo, lo
        return hi, hi
    if x == theta:
        if lo >= 0:
            return lo, lo
        return lo, Q(0)
    if x == -theta:
        if hi <= 0:
            return hi, hi
        return Q(0), hi
    raise AssertionError

theta = Q(1)

# Subcritical representative branching, including both endpoints and midpoints
# of every set-valued threshold subproblem.
for eta in [Q(1,4), Q(3,4), Q(5,4), Q(7,4)]:
    assert eta < 2 * theta
    for x0 in [Q(-11,3), Q(-2), Q(-1), Q(-2,3), Q(0), Q(2,3), Q(1), Q(2), Q(11,3)]:
        states = {x0}
        for _ in range(80):
            nxt = set()
            for x in states:
                lo, hi = minimizers(x, eta, theta)
                nxt.add(lo)
                nxt.add(hi)
                nxt.add((lo + hi) / 2)
                if lo <= 0 <= hi:
                    nxt.add(Q(0))
            states = nxt
            if states == {Q(0)}:
                break
        assert states == {Q(0)}

# Critical admissible two-cycle.
eta = Q(2)
assert minimizers(theta, eta, theta) == (-theta, Q(0))
assert minimizers(-theta, eta, theta) == (Q(0), theta)

# Supercritical unique two-cycles on the open band.
eta = Q(5,2)
for c in [Q(11,10), Q(5,4), Q(7,5)]:
    assert theta < c < eta - theta
    lo, hi = minimizers(c, eta, theta)
    assert lo == hi == c - eta
    lo2, hi2 = minimizers(c - eta, eta, theta)
    assert lo2 == hi2 == c

print("VERIFY_OK")
