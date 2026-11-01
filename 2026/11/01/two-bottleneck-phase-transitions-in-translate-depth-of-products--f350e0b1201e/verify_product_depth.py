"""Exact-arithmetic diagnostics for product-simplex translate-depth formulas.

This program checks finite cases; the general theorem is proved analytically.
Requires only Python 3 standard library.
"""
from fractions import Fraction as F
from math import factorial


def pos(x):
    return max(F(0), x)


def bary(y):
    return (1 - sum(y),) + tuple(y)


def overlap_from_facet_thresholds(d, t, a):
    assert len(a) == d + 1 and sum(a) == 1 - t
    return pos(1 - sum(pos(x) for x in a)) ** d


def clip(poly, f):
    if not poly:
        return []
    out = []
    prev = poly[-1]
    pv = f(prev)
    for cur in poly:
        cv = f(cur)
        if (pv < 0 <= cv) or (pv >= 0 > cv):
            h = pv / (pv - cv)
            out.append(tuple(prev[j] + h * (cur[j] - prev[j]) for j in range(2)))
        if cv >= 0:
            out.append(cur)
        prev, pv = cur, cv
    return out


def shoelace(poly):
    if len(poly) < 3:
        return F(0)
    s = sum(poly[i][0] * poly[(i+1) % len(poly)][1] -
            poly[(i+1) % len(poly)][0] * poly[i][1]
            for i in range(len(poly)))
    return abs(s) / 2


def planar_overlap(t, sx, sy):
    poly = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1))]
    for f in (lambda p: p[0] - sx, lambda p: p[1] - sy,
              lambda p: sx + sy + t - p[0] - p[1]):
        poly = clip(poly, f)
    return 2 * shoelace(poly)


def interval_overlap(t, s):
    return pos(min(F(1), s+t) - max(F(0), s))


def independent_overlap(d, t, a):
    if d == 1:
        return interval_overlap(t, a[1])
    if d == 2:
        return planar_overlap(t, a[1], a[2])
    raise ValueError('The independent geometric checker handles d=1,2.')


def optimal_missing_factor(d, t, y):
    m = min(bary(y))
    theta = min(t, F(1))
    return min(theta, 1 - pos(m)) ** d


def predicted_depth(dims, t, points):
    theta = min(t, F(1))
    D = sum(dims)
    return 1 - max(theta ** (D-d) * optimal_missing_factor(d, t, y)
                   for d, y in zip(dims, points))


def witness_a(t, y, eps=F(1, 100000)):
    lams = bary(y)
    j = min(range(len(lams)), key=lambda k: lams[k])
    a = [F(0)] * len(lams)
    a[j] = max(F(0), lams[j] + eps)
    for k in range(len(lams)):
        if k != j:
            a[k] = (1 - t - a[j]) / (len(lams)-1)
    assert a[j] > lams[j] and sum(a) == 1-t
    return a


def mass_witness(dims, t, points):
    theta = min(t, F(1))
    D = sum(dims)
    i = max(range(len(dims)), key=lambda j:
            theta ** (D-dims[j]) * optimal_missing_factor(dims[j], t, points[j]))
    a = []
    for j, d in enumerate(dims):
        if i == j:
            a.append(witness_a(t, points[j]))
        else:
            a.append([F(1-t, d+1)]*(d+1))
    assert any(any(a[j][k] > bary(points[j])[k] for k in range(dims[j]+1))
               for j in range(len(dims)))
    result = F(1)
    for d, aa in zip(dims, a):
        result *= independent_overlap(d, t, aa)
    return result


def max_miss(dims, t):
    theta = min(t, F(1))
    D = sum(dims)
    return max(theta ** (D-d) * min(theta, F(d, d+1)) ** d for d in dims)


def prism_phase(t):
    if t <= F(2,3):
        return 1-t**3
    if t <= F(8,9):
        return 1-F(4,9)*t
    if t <= 1:
        return 1-F(1,2)*t**2
    return F(1,2)


def run():
    n = 0
    tests = [(F(x,7), F(y,7), F(z,7)) for x in range(1,13)
             for y in range(-4,9,3) for z in range(-4,9,3)]
    for t, sx, sy in tests:
        a = [1-t-sx-sy, sx, sy]
        assert planar_overlap(t, sx, sy) == overlap_from_facet_thresholds(2, t, a)
        n += 1
    for t in (F(1,3), F(2,3), F(4,5), F(1), F(9,8), F(2)):
        for s in (F(-1), F(-1,5), F(0), F(1,4), F(2,3), F(7,6)):
            assert interval_overlap(t, s) == overlap_from_facet_thresholds(1, t, [1-t-s,s])
            n += 1
    pts = [([F(1,2)], [F(1,3),F(1,3)]),
           ([F(1,4)], [F(1,6),F(1,6)]),
           ([F(-1,5)], [F(1,3),F(1,3)]),
           ([F(1,2)], [F(-1,6),F(0)]),
           ([F(0)], [F(0),F(0)])]
    for t in (F(1,3),F(2,3),F(7,10),F(5,6),F(8,9),F(19,20),F(1),F(5,4)):
        for point in pts:
            mass = mass_witness([1,2], t, point)
            pred = 1-predicted_depth([1,2],t,point)
            assert 0 <= mass <= pred and pred - mass < F(1,1000), (t,point,mass,pred)
            n += 1
    for t in (F(1,5),F(1,2),F(2,3),F(7,10),F(5,6),F(8,9),F(9,10),F(1),F(5,4)):
        assert prism_phase(t) == 1-max_miss([1,2],t)
        n += 1
    for dims in ([1,2,4],[1,3,5],[2,4],[2,2],[1,1,3],[1,3,3],[2,3,7]):
        p,q=min(dims),max(dims)
        for t in (F(1,3),F(3,4),F(9,10),F(19,20),F(99,100),F(1),F(7,6)):
            B=max_miss(dims,t)
            theta=min(t,F(1))
            if t > F(q,q+1):
                extreme=max(theta ** (sum(dims)-d) * min(theta,F(d,d+1)) ** d for d in (p,q))
                assert B==extreme
            n+=1
    # At the triangular-prism crossover, both factor minima force centroid.
    t=F(8,9); B=1-prism_phase(t)
    c1=1-B/t**2
    assert c1==F(1,2)
    assert B/t == F(4,9)
    print(f'PASS {n} exact assertions; independent interval/triangle clipping,')
    print('boundary-approach translate witnesses, full prism phases, extreme-factor envelopes.')

if __name__ == '__main__':
    run()
