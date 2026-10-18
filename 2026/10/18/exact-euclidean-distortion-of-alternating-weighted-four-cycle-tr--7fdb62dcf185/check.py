"""Exact-rational arithmetic checks for the alternating weighted four-cycle."""
from fractions import Fraction as F
from itertools import product


def formula(t):
    s = max(t, 1/t)
    return (2*s+1)*(3*s-1)/((s+1)*(2*s-1))


def verify(t):
    assert t >= 1
    h = t/(2*t+1)
    a, b, c = 1/(1-h), 1/(t*t-h), 1/h
    # The two Euclidean-to-Lipschitz operator-norm constraints are exact.
    assert 1/a+1/c == 1
    assert (1/b+1/c)/(t*t) == 1
    vertices = []
    for e1, e2 in product((-1, 1), repeat=2):
        vertices.append((F(e1), t*e2, F(0)))
        vertices.append((F(0), (t-1)*e1, F(e2)))
    def N(u, v, w):
        return max(abs(u)+abs(w), (abs(v)+abs(w))/t)
    assert all(N(*v) == 1 for v in vertices)
    maxQ = max(a*u*u+b*v*v+c*w*w for u,v,w in vertices)
    A = a+b*t*t
    B = b*(t-1)**2+c
    assert maxQ == A == B == formula(t)
    # A finite grid is not used to prove continuous optimality.
    for k in range(1, 40):
        g = F(k, 40)
        if g != h:
            A_g = 1/(1-g)+t*t/(t*t-g)
            B_g = (t-1)**2/(t*t-g)+1/g
            assert max(A_g, B_g) > formula(t)
    return 1


if __name__ == '__main__':
    cases = [F(1), F(6,5), F(3,2), F(2), F(5,2), F(3), F(5), F(10)]
    assert sum(verify(t) for t in cases) == len(cases)
    for t in cases:
        assert formula(t) == formula(1/t)
    assert formula(F(1)) == F(3)
    assert formula(F(2)) == F(25,9)
    print('ALTERNATING_CYCLE_RATIONAL_CHECK_OK', len(cases))
