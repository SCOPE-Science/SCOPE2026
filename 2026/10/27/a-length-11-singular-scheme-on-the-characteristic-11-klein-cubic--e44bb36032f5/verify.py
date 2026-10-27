#!/usr/bin/env python3
"""Exact verification of characteristic-eleven invariants for the Klein cubic."""
from itertools import product

P = 11

def f(x):
    return sum(x[i]**2 * x[(i + 1) % 5] for i in range(5)) % P

def grad(x):
    return [(x[(i - 1) % 5]**2 + 2*x[i]*x[(i + 1) % 5]) % P
            for i in range(5)]

def rank(A, p):
    b = [[v % p for v in row] for row in A]
    r = 0
    for j in range(len(b[0])):
        piv = next((i for i in range(r, len(b)) if b[i][j]), None)
        if piv is None:
            continue
        b[r], b[piv] = b[piv], b[r]
        z = pow(b[r][j], -1, p)
        b[r] = [(z * v) % p for v in b[r]]
        for i in range(len(b)):
            if i != r and b[i][j]:
                c = b[i][j]
                b[i] = [(v - c*w) % p for v, w in zip(b[i], b[r])]
        r += 1
    return r

def poly_add(a, b):
    return [(u + v) % P for u, v in zip(a, b)]

def poly_mul(a, b):
    c = [0] * 11
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            e = i + j
            c[e % 11] = (c[e % 11] + u*v*(4 if e >= 11 else 1)) % P
    return c

def const(c):
    a = [0] * 11
    a[0] = c % P
    return a

def monomial(c, e):
    a = [0] * 11
    a[e] = c % P
    return a

def sq(a):
    return poly_mul(a, a)

def verify_critical_scheme():
    # In R=F_11[s]/(s^11-4), the five homogeneous gradients
    # vanish at (1, 5s^2, 3s^9, 4s^6, s).  The accompanying
    # algebraic proof shows this is the *entire* singular scheme.
    a = [const(1), monomial(5, 2), monomial(3, 9),
         monomial(4, 6), monomial(1, 1)]
    for i in range(5):
        g = poly_add(sq(a[(i-1)%5]),
                     poly_mul(const(2), poly_mul(a[i], a[(i+1)%5])))
        assert g == const(0), (i, g)
    z = const(0)
    for i in range(5):
        z = poly_add(z, poly_mul(sq(a[i]), a[(i+1)%5]))
    assert z == const(0)
    # Every rational geometric solution has s=4, by s^11=4.
    pt = (1, 3, 9, 5, 4)
    assert f(pt) == 0 and grad(pt) == [0]*5
    H = [[18, 6, 0, 0], [6, 10, 18, 0],
         [0, 18, 8, 10], [0, 0, 10, 2]]
    assert rank(H, P) == 3
    assert rank([row[:3] for row in H[:3]], P) == 3

def projective_points(n):
    for first in range(n):
        for rest in product(range(P), repeat=n-1-first):
            yield (0,)*first + (1,) + rest

def verify_point_counts():
    X = sum(f(v) == 0 for v in projective_points(5))
    # The finite search covers exactly (11^5-1)/10 projective points.
    assert sum(1 for _ in projective_points(5)) == 16105
    assert X == 1464, X
    Q_count = Y_count = 0
    for a,b,c,d in projective_points(4):
        Q = -2*a*a-5*a*b+5*b*b-4*b*c+4*c*c-c*d+d*d
        C = a*a*b+b*b*c+c*c*d
        if Q % P == 0:
            Q_count += 1
            if C % P == 0:
                Y_count += 1
    assert Q_count == 133 and Y_count == 12, (Q_count, Y_count)
    # Projection from the unique singular point: 1+#P^3-#Q+11#Y.
    assert 1 + 1464 - Q_count + 11*Y_count == X
    return X, Q_count, Y_count

if __name__ == '__main__':
    verify_critical_scheme()
    print('X_Q_Y:', verify_point_counts())
    print('VERIFY_OK')
