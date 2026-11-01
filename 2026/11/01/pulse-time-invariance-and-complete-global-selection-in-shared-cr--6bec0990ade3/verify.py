#!/usr/bin/env python3
"""Exact-arithmetic regression checks for a periodically pulsed shared-crowding system.

These finite checks test the algebra used in the analytical proof; they do not
replace the proof of all-parameter statements.
"""
from fractions import Fraction as Q


def compose(first, second):
    """Return second∘first for diagonal linear-fractional maps."""
    m, c = first
    n, d = second
    return tuple(a * b for a, b in zip(m, n)), tuple(a + b * v for a, b, v in zip(c, m, d))


def apply(map_data, x):
    m, c = map_data
    den = 1 + sum(a * b for a, b in zip(c, x))
    return tuple(a * b / den for a, b in zip(m, x))


def flow(t, b):
    return tuple(Q(1) for _ in b), tuple(t * bi for bi in b)


def pulse(m):
    return tuple(m), tuple(Q(0) for _ in m)


def chain(maps):
    v = (tuple(Q(1) for _ in maps[0][0]), tuple(Q(0) for _ in maps[0][0]))
    for w in maps:
        v = compose(v, w)
    return v


def iterate(m, c, x, n):
    den = 1 + sum(c[j] * x[j] * sum(m[j]**q for q in range(n)) for j in range(len(m)))
    return tuple(m[j]**n * x[j] / den for j in range(len(m)))


F = chain((flow(Q(1,4),(Q(1),Q(1))),
           pulse((Q(2),Q(1))),
           flow(Q(1,2),(Q(1),Q(1))),
           pulse((Q(1),Q(3))),
           flow(Q(1,4),(Q(1),Q(1)))))
assert F == ((Q(2),Q(3)),(Q(7,4),Q(3,2))), F
x = (Q(1,3),Q(2,7))
for n in range(1, 13):
    w = x
    for _ in range(n):
        w = apply(F, w)
    assert w == iterate(*F, x, n)
    z = x
    for _ in range(n):
        z = apply(flow(Q(1,4),(Q(1),Q(1))), z)
        z = apply(pulse((Q(2),Q(1))), z)
        z = apply(flow(Q(1,2),(Q(1),Q(1))), z)
        z = apply(pulse((Q(1),Q(3))), z)
        z = apply(flow(Q(1,4),(Q(1),Q(1))), z)
    assert w == z

# Same doses and same total clock, different species-2 pulse timing.
F_early = chain((flow(Q(1,4),(Q(1),Q(1))),
                 pulse((Q(2),Q(3))),
                 flow(Q(3,4),(Q(1),Q(1)))))
assert F_early == ((Q(2),Q(3)),(Q(7,4),Q(5,2))), F_early
assert (F[0], F_early[0]) == ((Q(2),Q(3)),(Q(2),Q(3)))
assert (Q(3)-1)/F[1][1] == Q(4,3)
assert (Q(3)-1)/F_early[1][1] == Q(4,5)

# Tied winners form a genuinely non-isolated simplex of exact fixed states.
F_tie = chain((flow(Q(1,4),(Q(1),Q(1))),
               pulse((Q(2),Q(1))),
               flow(Q(1,2),(Q(1),Q(1))),
               pulse((Q(1),Q(2))),
               flow(Q(1,4),(Q(1),Q(1)))))
assert F_tie == ((Q(2),Q(2)),(Q(7,4),Q(5,4)))
star = (Q(1,4),Q(9,20))
assert apply(F_tie,star) == star
m,c = F_tie
v = (Q(0),Q(0))
J = tuple(tuple((Q(1) if i == j else Q(0)) - star[i]*c[j]/Q(2) for j in range(2)) for i in range(2))
tr = J[0][0]+J[1][1]
det = J[0][0]*J[1][1]-J[0][1]*J[1][0]
assert (tr,det) == (Q(3,2),Q(1,2))

# Other threshold regimes checked by finite exact iterates.
for m in ((Q(4,5),Q(3,4)),(Q(1),Q(1,2)),(Q(2),Q(3)),(Q(2),Q(2))):
    c=(Q(7,4),Q(3,2)); x=(Q(3,10),Q(7,20))
    for n in (0,1,2,3,5,10,40):
        direct=x
        for _ in range(n):
            direct=apply((m,c),direct)
        assert direct == iterate(m,c,x,n)
print('PASS: exact rational composition, iterate, timing and fixed-simplex checks')
