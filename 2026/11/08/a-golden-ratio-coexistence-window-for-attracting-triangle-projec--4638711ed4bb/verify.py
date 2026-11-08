"""Exact-rational checks for low-period orbits of the triangular farthest-projection map.

Requires only Python 3's standard library. Finite tests supplement the proof.
"""
from fractions import Fraction as Q
from itertools import product


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def scale(c, a):
    return (c * a[0], c * a[1])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def line_endpoints(h):
    a, b, c = (Q(0), h), (Q(-1), Q(0)), (Q(1), Q(0))
    return [(a, b), (b, c), (c, a)]


def project(x, line):
    a, b = line
    u = sub(b, a)
    return add(a, scale(dot(sub(x, a), u) / dot(u, u), u))


def squared_dist(a, b):
    return dot(sub(a, b), sub(a, b))


def branch_projection(x, source, target, lines):
    assert target != source
    other = ({0, 1, 2} - {source, target}).pop()
    y = project(x, lines[target])
    z = project(x, lines[other])
    return y, squared_dist(x, y) - squared_dist(x, z)


def enumerate_cycles(h, period):
    lines = line_endpoints(h)
    found = {}
    for itinerary in product(range(3), repeat=period):
        if any(itinerary[k] == itinerary[(k + 1) % period]
               for k in range(period)):
            continue
        first = itinerary[0]
        a, b = lines[first]
        u = sub(b, a)

        def composed(t):
            x = add(a, scale(t, u))
            for j in itinerary[1:] + (first,):
                x = project(x, lines[j])
            return dot(sub(x, a), u) / dot(u, u)

        b0, b1 = composed(Q(0)), composed(Q(1))
        slope = b1 - b0
        if slope == 1:
            continue
        t = b0 / (1 - slope)
        x = add(a, scale(t, u))
        pts = []
        valid = True
        for k in range(period):
            source = itinerary[k]
            target = itinerary[(k + 1) % period]
            pts.append((source, x))
            next_x, difference = branch_projection(x, source, target, lines)
            if difference <= 0:
                valid = False
                break
            x = next_x
        if not valid or x != pts[0][1]:
            continue
        if len(set(pts)) != period:
            continue
        # One entry per physical periodic cycle, disregarding starting phase.
        key = min(tuple(pts[k:] + pts[:k]) for k in range(period))
        found[key] = slope
    return found


def main():
    trials = set(Q(k, 30) for k in range(1, 111))
    trials.update([Q(1), Q(11, 10), Q(5, 4), Q(4, 5), Q(13, 10),
                   Q(6, 5), Q(3, 2), Q(2), Q(5, 2), Q(3), Q(7, 2)])
    cases = checks = 0
    counts = {}
    for h in sorted(trials):
        a = h * h
        expected3 = 2 if 1 < a and a * a - 6*a - 3 < 0 else 0
        expected4 = 1 if a * a - a - 1 < 0 else 0
        cycles3 = enumerate_cycles(h, 3)
        cycles4 = enumerate_cycles(h, 4)
        assert len(cycles3) == expected3, (h, '3', len(cycles3), expected3)
        assert len(cycles4) == expected4, (h, '4', len(cycles4), expected4)
        checks += 2
        for multiplier in cycles3.values():
            assert multiplier == (1-a)/(1+a)**2
            assert abs(multiplier) < 1
            checks += 2
        for multiplier in cycles4.values():
            assert multiplier == Q(1)/(1+a)**2
            assert abs(multiplier) < 1
            checks += 2
        # The direct-orbit enumeration uses an entirely different construction
        # than the closed candidate coordinates in the proof.
        counts[(expected3, expected4)] = counts.get((expected3, expected4), 0) + 1
        cases += 1
    print('CHECK_OK:', cases, 'exact-rational triangle shapes;', checks,
          'assertions; period-(3,4) regimes:', sorted(counts.items()))


if __name__ == '__main__':
    main()
