"""Exact spectrum census for the four-block Paley harmonic-fusion Gram matrices.

Python 3, standard library only. All arithmetic is over integers; the
formal symbol i*sqrt(11) is represented by a pair of integer matrices.
"""
from collections import defaultdict
from itertools import combinations

P = 13
D = P - 2
QUARTET_COUNT = 715

def mm(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def madd(a, b, sign=1):
    return [[x + sign*y for x, y in zip(row1, row2)]
            for row1, row2 in zip(a, b)]


def scale(a, c):
    return [[c * v for v in row] for row in a]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def product(x, y, d):
    ar, ai = x
    br, bi = y
    return (madd(mm(ar, br), scale(mm(ai, bi), d), -1),
            madd(mm(ar, bi), mm(ai, br)))


def euler_characteristic_polynomial(points, modulus=P):
    """Coefficients from highest degree to constant of det(Y I - K K*).

    For this four-block case K=C+i sqrt(q-2) S, with C=J-I and
    S_{ij}=Legendre(points[j]-points[i]), S_{ii}=0.
    """
    n = len(points)
    residues = {x*x % modulus for x in range(1, modulus)}
    c = [[0 if i == j else 1 for j in range(n)] for i in range(n)]
    sign = [[0 if i == j else
             (1 if (points[j]-points[i]) % modulus in residues else -1)
             for j in range(n)] for i in range(n)]
    # K K* = (C^2+d*S^2) + i sqrt(d)*(S*C-C*S).
    r = madd(mm(c, c), scale(mm(sign, sign), modulus-2))
    im = madd(mm(sign, c), mm(c, sign), -1)
    h = (r, im)
    power = h
    traces = [None]
    for k in range(1, n+1):
        assert trace(power[1]) == 0
        traces.append(trace(power[0]))
        if k != n:
            power = product(power, h, modulus-2)
    # Newton identities: r*e_r=sum_{k=1}^r (-1)^(k-1) e_{r-k} tr(H^k).
    e = [1]
    for j in range(1, n+1):
        numerator = sum((-1)**(k-1)*e[j-k]*traces[k]
                        for k in range(1, j+1))
        assert numerator % j == 0
        e.append(numerator//j)
    return tuple((-1)**k*e[k] for k in range(n+1))


def mul_poly(a, b):
    z = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i+j] += x*y
    return tuple(z)


def check():
    # The degree-four polynomials in Y=lambda^2 for unnormalized 8x8 blocks.
    polynomials = {
        mul_poly(mul_poly((1,-12),(1,-12)), (1,-120,3408)): 390,
        # (Y-56)^2*(Y^2-32Y+64).
        mul_poly(mul_poly((1,-56),(1,-56)), (1,-32,64)): 195,
        mul_poly(mul_poly((1,-100),(1,-20)), mul_poly((1,-12),(1,-12))): 78,
        mul_poly((1,-108), mul_poly(mul_poly((1,-12),(1,-12)),(1,-12))): 52,
    }
    assert len(polynomials)==4
    classes=defaultdict(list)
    for points in combinations(range(P),4):
        classes[euler_characteristic_polynomial(points)].append(points)
    assert sum(map(len,classes.values())) == QUARTET_COUNT
    assert {k:len(v) for k,v in classes.items()} == polynomials, \
        (polynomials, [(k,len(v),v[0]) for k,v in classes.items()])
    expected_reps={390:(0,1,2,4),195:(0,1,2,6),78:(0,1,2,3),52:(0,1,3,9)}
    for polynomial, subsets in classes.items():
        c=len(subsets)
        assert expected_reps[c] in subsets
        print('FOUR_BLOCK',c,expected_reps[c],polynomial)
    # The same formal calculation for every triple gives universal spectrum.
    triple_poly=mul_poly((1,-48),mul_poly((1,-12),(1,-12)))
    for points in combinations(range(P),3):
        assert euler_characteristic_polynomial(points)==triple_poly
    # At q=5 the same quadratic construction exists and has universal triple profile.
    triple_poly_5=mul_poly((1,-16),mul_poly((1,-4),(1,-4)))
    for points in combinations(range(5),3):
        assert euler_characteristic_polynomial(points,5)==triple_poly_5
    # Check the four-block extremal representative is an affine image of {0,1,3,9}.
    exceptional={tuple(sorted((a*x+b)%P for x in (0,1,3,9)))
                 for a in range(1,P) for b in range(P)}
    assert len(exceptional)==52
    assert set(classes[next(p for p,c in polynomials.items() if c==52)])==exceptional
    print('CHECK_PASS 715 quartets, 286 triples, 10 five-field triples, four exact profiles')

if __name__ == '__main__':
    check()
