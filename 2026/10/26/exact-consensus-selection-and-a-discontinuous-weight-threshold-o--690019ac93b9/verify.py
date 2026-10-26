"""Reproduce finite star weighted-median consensus and sensitivity checks.

Only the Python standard library is required. These checks supplement the
analytic proof; finite numerical checks alone do not prove arbitrary size.
"""
from fractions import Fraction as Q
from math import exp


def median_bounds(leaves, weights):
    """Endpoints of the minimizing weighted-median interval."""
    pairs = sorted(zip(leaves, weights))
    assert all(w > 0 for _, w in pairs) and sum(weights) == 1
    total = Q(0)
    low = high = None
    for i, (value, weight) in enumerate(pairs):
        if total < Q(1, 2) <= total + weight:
            low = value
            if total + weight == Q(1, 2) and i + 1 < len(pairs):
                high = pairs[i + 1][0]
            else:
                high = value
            break
        total += weight
    assert low is not None and high is not None
    return low, high


def selected_consensus(hub, leaves, weights):
    low, high = median_bounds(leaves, weights)
    if hub < low:
        return (hub + low) / 2
    if hub > high:
        return (hub + high) / 2
    return hub


def trajectory(t, hub, leaves, weights):
    low, high = median_bounds(leaves, weights)
    if hub < low:
        center = (hub + low) / 2 + (hub - low) / 2 * exp(-2 * t)
        med = (hub + low) / 2 - (hub - low) / 2 * exp(-2 * t)
        vals = [med + (float(a - low)) * exp(-t) for a in leaves]
    elif hub > high:
        center = (hub + high) / 2 + (hub - high) / 2 * exp(-2 * t)
        med = (hub + high) / 2 - (hub - high) / 2 * exp(-2 * t)
        vals = [med + (float(a - high)) * exp(-t) for a in leaves]
    else:
        center = float(hub)
        vals = [center + float(a - hub) * exp(-t) for a in leaves]
    return center, vals


def selected_median(hub, leaves, weights):
    candidates = [hub] + leaves
    admissible = []
    for c in candidates:
        lo = sum(w for x, w in zip(leaves, weights) if x < c - 1e-10)
        hi = sum(w for x, w in zip(leaves, weights) if x > c + 1e-10)
        if lo <= .5 + 1e-10 and hi <= .5 + 1e-10:
            admissible.append(c)
    assert admissible
    return min(admissible, key=lambda x: abs(x - hub))


def check_one(hub, leaves, weights):
    c_star = float(selected_consensus(hub, leaves, weights))
    for t in (.03, .4, 2.0, 7.0):
        c, vals = trajectory(t, hub, leaves, weights)
        h = 1e-5
        cp, vp = trajectory(t+h, hub, leaves, weights)
        cm, vm = trajectory(t-h, hub, leaves, weights)
        med = selected_median(c, vals, [float(w) for w in weights])
        assert abs((cp-cm)/(2*h) - (med-c)) < 3e-7
        for i in range(len(leaves)):
            assert abs((vp[i]-vm[i])/(2*h) - (c-vals[i])) < 3e-7
    c, vals = trajectory(30., hub, leaves, weights)
    assert abs(c-c_star) < 2e-11
    assert all(abs(x-c_star)<2e-11 for x in vals)


if __name__ == '__main__':
    h = Q(2, 5)
    x = [Q(0), Q(1)]
    assert selected_consensus(h, x, [Q(1, 2), Q(1, 2)]) == Q(2, 5)
    for e in [Q(1, 10), Q(1, 1000), Q(1, 10**8)]:
        assert selected_consensus(h, x, [Q(1, 2)+e, Q(1, 2)-e]) == Q(1, 5)
        assert selected_consensus(h, x, [Q(1, 2)-e, Q(1, 2)+e]) == Q(7, 10)
    check_one(h, x, [Q(1, 2), Q(1, 2)])
    check_one(h, x, [Q(3, 5), Q(2, 5)])
    check_one(h, x, [Q(2, 5), Q(3, 5)])
    check_one(Q(9, 10), [Q(1,10), Q(1,2), Q(4,5), Q(11,10), Q(7,5)],
              [Q(1,10), Q(2,10), Q(4,10), Q(2,10), Q(1,10)])
    check_one(Q(-1), [Q(1,10), Q(1,2), Q(4,5), Q(11,10), Q(7,5)],
              [Q(1,10), Q(2,10), Q(4,10), Q(2,10), Q(1,10)])
    check_one(Q(9,10), [Q(1,10), Q(1,2), Q(4,5), Q(11,10)],
              [Q(1,4), Q(1,4), Q(1,4), Q(1,4)])
    print('PASS: exact rational sensitivity examples, closed-form trajectories,')
    print('and independently evaluated weighted-median differential equations.')
