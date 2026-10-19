"""Independent finite-field checks for split-octonion commuting-tuple formulas."""
from itertools import product
from collections import Counter


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def multiply(a, b):
    aa, u, v, ab = a[0], a[1:4], a[4:7], a[7]
    ba, x, y, bb = b[0], b[1:4], b[4:7], b[7]
    vy, ux = cross(v, y), cross(u, x)
    return (aa*ba+sum(u[i]*y[i] for i in range(3)),) + tuple(
        aa*x[i]+bb*u[i]-vy[i] for i in range(3)) + tuple(
        ba*v[i]+ab*y[i]+ux[i] for i in range(3)) + (ab*bb+sum(v[i]*x[i] for i in range(3)),)


def rank(a, p):
    a = [[v % p for v in row] for row in a]
    h = 0
    for j in range(len(a[0])):
        k = next((k for k in range(h, len(a)) if a[k][j]), None)
        if k is None: continue
        a[h], a[k] = a[k], a[h]
        inv = pow(a[h][j], -1, p)
        a[h] = [(v*inv) % p for v in a[h]]
        for k in range(h+1, len(a)):
            if a[k][j]:
                t = a[k][j]
                a[k] = [(z-t*v) % p for z, v in zip(a[k], a[h])]
        h += 1
        if h == len(a): break
    return h


def qint(n, q): return (q**n-1)//(q-1)


def test_field(q):
    basis = [tuple(int(i == j) for i in range(8)) for j in range(8)]
    observed = Counter()
    null = 0
    for coords in product(range(q), repeat=7):
        t = coords[0]
        a = (t,) + coords[1:] + ((-t) % q,)
        norm = (-t*t-sum(a[i]*a[i+3] for i in (1,2,3))) % q
        if norm == 0: null += 1
        prod1 = [multiply(a, b) for b in basis]
        prod2 = [multiply(b, a) for b in basis]
        mat = [[(prod1[j][i]-prod2[j][i]) % q for j in range(8)] for i in range(8)]
        r = rank(mat, q)
        observed[(norm == 0, r)] += 1
    assert null == q**6, (q, null)
    expect = Counter({(True, 0):1, (True, 4): q**6-1,
                      (False, 6):q**7-q**6})
    assert observed == expect, (q, observed, expect)
    pair_count = q * sum(n*q**(8-r) for (is_null,r),n in observed.items())
    formula = qint(6, q)*q**6-qint(5, q)*q**5
    assert pair_count == formula, (q, pair_count, formula)
    print('FIELD',q,'NULL',null,'ADJOINT',dict(observed),'COMMUTING_PAIRS',pair_count)


def test_heisenberg(q, m):
    # Coordinates per tuple entry are (a,b,c); bracket is (ab'-a'b)c.
    count = 0
    for z in product(range(q), repeat=2*m):
        if all((z[2*i]*z[2*j+1]-z[2*j]*z[2*i+1]) % q == 0
               for i in range(m) for j in range(i+1,m)):
            count += 1
    count *= q**m  # central coordinates
    expected = q**m * (1+(q**m-1)*(q+1))
    assert count == expected, (q,m,count,expected)
    print('HEISENBERG',q,m,count)


def test_closed_formula(q):
    for s in range(0,6):
        direct = q**s*(1 + qint(7,q)*(q**s-1)
                        + qint(6,q)*(q**s-1)*(q**s-q))
        expression = qint(6,q)*q**(3*s)-qint(5,q)*q**(2*s+1)
        assert direct == expression, (q,s,direct,expression)
    print('ALL_ARITY_IDENTITY',q,'OK')


if __name__ == '__main__':
    test_field(3)
    test_field(5)
    test_heisenberg(3, 2)
    test_heisenberg(3, 3)
    test_heisenberg(5, 2)
    for q in (3,5,7,9,11): test_closed_formula(q)
    print('VERIFY_OK')
