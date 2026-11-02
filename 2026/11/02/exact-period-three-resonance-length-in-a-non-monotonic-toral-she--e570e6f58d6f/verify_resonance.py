"""Exact rational cell certificate for a period-three toral shear resonance.

Requires Python 3.11 or later; no third-party packages.
Every arithmetic decision in the finite cell census uses Fraction.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product

ZERO = Q(0)
ONE = Q(1)
ETA = Q(1, 3)
ID = (ONE, ZERO, ZERO, ONE)


def matmul(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def matvec(a, v):
    return (a[0]*v[0]+a[1]*v[1], a[2]*v[0]+a[3]*v[1])


def torus_step(point):
    x, y = point
    f = y/(1-ETA) if y <= 1-ETA else (1-y)/ETA
    xx = (x+f) % 1
    yy = (y+xx) % 1
    return xx, yy


def cut(poly, a, b, c):
    """Clip a rational polygon to ax+by<=c, retaining boundary."""
    if not poly:
        return []
    out = []
    for P, R in zip(poly, poly[1:]+poly[:1]):
        p = a*P[0] + b*P[1] - c
        r = a*R[0] + b*R[1] - c
        if p <= 0:
            out.append(P)
        if (p < 0 < r) or (r < 0 < p):
            lam = p/(p-r)
            out.append((P[0]+lam*(R[0]-P[0]),
                        P[1]+lam*(R[1]-P[1])))
    return [v for i, v in enumerate(out) if v != out[i-1]]


def restricted_segment(arcs, a, b, c):
    """Solve a*x+b*y=c and intersect all three cells exactly."""
    if b:
        base = (ZERO, c/b)
        direct = (ONE, -a/b)
    else:
        base = (c/a, ZERO)
        direct = (ZERO, ONE)
    lo, hi = Q(-100), Q(100)

    def impose(p, s, low, high):
        nonlocal lo, hi
        if s == 0:
            if not low <= p <= high:
                lo, hi = ONE, ZERO
        else:
            u, v = (low-p)/s, (high-p)/s
            lo = max(lo, min(u, v))
            hi = min(hi, max(u, v))

    for A, w, side in arcs:
        p = matvec(A, base)
        s = matvec(A, direct)
        impose(p[0]+w[0], s[0], ZERO, ONE)
        impose(p[1]+w[1], s[1], ZERO if side == 0 else ONE-ETA,
               ONE-ETA if side == 0 else ONE)
    if lo >= hi:
        return None
    P = tuple(base[j]+lo*direct[j] for j in range(2))
    R = tuple(base[j]+hi*direct[j] for j in range(2))
    return P, R


def restricted_polygon(arcs):
    poly = [(ZERO, ZERO), (ONE, ZERO), (ONE, ONE), (ZERO, ONE)]
    for A, w, side in arcs:
        a, b, c, d = A
        wx, wy = w
        for u, v, z in [(-a, -b, wx), (a, b, ONE-wx),
                        (-c, -d, wy-(ONE-ETA if side else ZERO)),
                        (c, d, (ONE if side else ONE-ETA)-wy)]:
            poly = cut(poly, u, v, z)
    return poly


def certificate():
    matrix = [(ONE, ONE/(ONE-ETA), ONE, ONE+ONE/(ONE-ETA)),
              (ONE, -ONE/ETA, ONE, ONE-ONE/ETA)]
    const = [(ZERO, ZERO), (ONE/ETA, ONE/ETA)]
    segments = []
    rankzero_consistent = []
    singular_cells = 0

    for choices in product(range(8), repeat=3):
        A, w = ID, (ZERO, ZERO)
        arcs = []
        for code in choices:
            side, remainder = divmod(code, 4)
            m, n = divmod(remainder, 2)
            arcs.append((A, w, side))
            T = (const[side][0]-m, const[side][1]-m-n)
            Z = matvec(matrix[side], w)
            w = (Z[0]+T[0], Z[1]+T[1])
            A = matmul(matrix[side], A)
        p, s, t, r = ONE-A[0], -A[1], -A[2], ONE-A[3]
        if p*r-s*t != 0:
            continue
        singular_cells += 1
        if (p, s, t, r) == (0, 0, 0, 0):
            if w == (ZERO, ZERO):
                rankzero_consistent.append(choices)
                # RRR with identical wraps at all three steps is an
                # affine order-three rotation about c=(n,1-m/3).
                # Since all y_j lie in [2/3,1], while their average is
                # c_y on the boundary of that interval, each y_j=c_y.
                # Then y_{j+1}=y_j+x_{j+1}-n forces x_j=n.
                # Thus this cell has at most this single point, never
                # a nondegenerate fixed segment or a two-dimensional set.
                assert all(code == choices[0] for code in choices)
                assert all(code >= 4 for code in choices)
                m, n = divmod(choices[0] % 4, 2)
                centre = (Q(n), ONE-Q(m,3))
                assert ZERO <= centre[0] <= ONE
                assert ONE-ETA <= centre[1] <= ONE
                for A0, w0, side in arcs:
                    z0 = matvec(A0, centre)
                    z0 = (z0[0]+w0[0], z0[1]+w0[1])
                    assert ZERO <= z0[0] <= ONE
                    assert ONE-ETA <= z0[1] <= ONE
            continue
        if p*w[1] != t*w[0] or s*w[1] != r*w[0]:
            continue
        a, b, c = (p, s, w[0]) if p or s else (t, r, w[1])
        result = restricted_segment(arcs, a, b, c)
        if result is not None:
            P, R = result
            assert P != R
            midpoint = tuple((u+v)/2 for u, v in zip(P, R))
            z = torus_step(torus_step(torus_step(midpoint)))
            assert z == midpoint, (choices, midpoint, z)
            assert torus_step(midpoint) != midpoint
            segments.append((choices, P, R))

    assert singular_cells == 256, singular_cells
    assert len(rankzero_consistent) == 4
    assert len(segments) == 12, len(segments)
    squared = Counter(sum((R[j]-P[j])**2 for j in range(2))
                      for _, P, R in segments)
    assert squared == Counter({Q(1,81): 4, Q(2,81): 4, Q(5,81): 4}), squared
    # Ensure segments have disjoint relative interiors. Their directions
    # and supporting lines differ except for adjacent intervals.
    for i, (_, P, R) in enumerate(segments):
        for _, S, T in segments[i+1:]:
            v = (R[0]-P[0], R[1]-P[1])
            u = (T[0]-S[0], T[1]-S[1])
            cross = v[0]*u[1]-v[1]*u[0]
            if cross == 0 and v[0]*(S[1]-P[1])-v[1]*(S[0]-P[0]) == 0:
                axis = 0 if v[0] else 1
                l1, h1 = sorted((P[axis], R[axis]))
                l2, h2 = sorted((S[axis], T[axis]))
                assert max(l1,l2) >= min(h1,h2)
    # Torus endpoint identifications merge the twelve itinerary arcs into
    # precisely six maximal connected straight segments, two per length.
    endpoint_to_edges = {}
    for index, (_, P, R) in enumerate(segments):
        for pt in (P, R):
            key = tuple(coord % 1 for coord in pt)
            endpoint_to_edges.setdefault(key, []).append(index)
    assert Counter(len(v) for v in endpoint_to_edges.values()) == Counter({1: 12, 2: 6})
    adjacency = [set() for _ in segments]
    for js in endpoint_to_edges.values():
        for a in js:
            adjacency[a].update(js)
    groups, seen = [], set()
    for i in range(len(segments)):
        if i in seen:
            continue
        todo, group = [i], set()
        while todo:
            j = todo.pop()
            if j in group:
                continue
            group.add(j)
            todo.extend(adjacency[j] - group)
        seen.update(group)
        groups.append(group)
    assert len(groups) == 6
    assert sorted(len(g) for g in groups) == [2]*6
    combined = Counter()
    for group in groups:
        pair = list(group)
        _, P, R = segments[pair[0]]
        _, S, T = segments[pair[1]]
        v = (R[0]-P[0], R[1]-P[1])
        u = (T[0]-S[0], T[1]-S[1])
        assert v[0]*u[1]-v[1]*u[0] == 0
        # Endpoint coincidence may be through an integer torus translation.
        endpoints = {tuple(t % 1 for t in q) for q in (P, R)}
        assert endpoints.intersection(tuple(t % 1 for t in q) for q in (S,T))
        sq1 = sum(z*z for z in v)
        sq2 = sum(z*z for z in u)
        assert sq1 == sq2
        combined[4*sq1] += 1
    assert combined == Counter({Q(4,81):2, Q(8,81):2, Q(20,81):2})

    # The six maximal segments are permuted in two primitive three-cycles.
    def contained_on_torus_segment(point, P, R):
        v = (R[0]-P[0], R[1]-P[1])
        for dx, dy in product((-1,0,1), repeat=2):
            w = (point[0]+dx-P[0], point[1]+dy-P[1])
            if v[0]*w[1]-v[1]*w[0] != 0:
                continue
            t = w[0]/v[0] if v[0] else w[1]/v[1]
            if ZERO <= t <= ONE:
                return True
        return False

    origin_group = {j: k for k, group in enumerate(groups) for j in group}
    permutation = []
    for group in groups:
        destination_groups = set()
        for j in group:
            _, P, R = segments[j]
            mid = tuple((a+b)/2 for a,b in zip(P,R))
            next_point = torus_step(mid)
            matches = {origin_group[k] for k, (_, S,T) in enumerate(segments)
                       if contained_on_torus_segment(next_point,S,T)}
            assert len(matches) == 1
            destination_groups.update(matches)
        assert len(destination_groups) == 1
        permutation.append(next(iter(destination_groups)))
    assert sorted(permutation) == list(range(6))
    assert all(permutation[i] != i for i in range(6))
    assert all(permutation[permutation[permutation[i]]] == i for i in range(6))
    def cross(a,b):
        return a[0]*b[1]-a[1]*b[0]
    # No unnoticed crossing between non-collinear line interiors, including
    # copies translated across opposite unit-square sides.
    for i, (_, P, R) in enumerate(segments):
        v = (R[0]-P[0], R[1]-P[1])
        for _, S, T in segments[i+1:]:
            u = (T[0]-S[0], T[1]-S[1])
            den = cross(v,u)
            if not den:
                continue
            for dx, dy in product((-1,0,1), repeat=2):
                w = (S[0]+dx-P[0], S[1]+dy-P[1])
                l = cross(w,u)/den
                m = cross(w,v)/den
                if ZERO <= l <= ONE and ZERO <= m <= ONE:
                    assert l in (ZERO, ONE) and m in (ZERO, ONE), (i,l,m)
    print('maximal connected straight components:',len(groups))
    print('six-component two-three-cycle permutation:',permutation)
    print('maximal squared lengths:',dict(combined))
    print('EXACT CERTIFICATE PASS')
    print('cells:', 8**3, 'singular derivative cells:', singular_cells)
    print('identity-affine boundary singleton cells:', len(rankzero_consistent), rankzero_consistent)
    print('nondegenerate line pieces:', len(segments))
    print('squared lengths:', dict(squared))
    print('Hausdorff 1-measure: 4*(1+sqrt(2)+sqrt(5))/9')
    for word, P, R in segments:
        print(''.join('L' if ch < 4 else 'R' for ch in word),
              ''.join(str(ch) for ch in word), str(P), str(R))


if __name__ == '__main__':
    certificate()
