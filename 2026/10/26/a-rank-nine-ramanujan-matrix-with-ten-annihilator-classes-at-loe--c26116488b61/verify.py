"""Exact verification of a finite-ring Ramanujan-matrix rank statement.
Run with Python 3 standard library; no downloads or extra packages needed.
"""
from fractions import Fraction

# Basis bits: 1, x, y, z, u=x*x, v=y*y; z*z=u+v.
N = 64
ONE, X, Y, Z, U, V = (1 << i for i in range(6))
BASIS_PRODUCT = {
    (0, 0): ONE,
    (0, 1): X, (0, 2): Y, (0, 3): Z,
    (0, 4): U, (0, 5): V,
    (1, 1): U, (2, 2): V, (3, 3): U ^ V,
}

def multiply(a, b):
    out = 0
    for i in range(6):
        if (a >> i) & 1:
            for j in range(6):
                if (b >> j) & 1:
                    out ^= BASIS_PRODUCT.get((min(i, j), max(i, j)), 0)
    return out


def exact_rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    r, cols = 0, len(a[0])
    for j in range(cols):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        d = a[r][j]
        a[r] = [x / d for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][j]:
                c = a[i][j]
                a[i] = [v - c*w for v, w in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def validate():
    # Multiplication table independent of a polynomial CAS.
    for a in range(N):
        assert multiply(a, ONE) == a
        for b in range(N):
            assert multiply(a, b) == multiply(b, a)
    for i in range(6):
        for j in range(6):
            for k in range(6):
                assert multiply(multiply(1<<i,1<<j),1<<k) == multiply(1<<i,multiply(1<<j,1<<k))
    units = [a for a in range(N) if a & ONE]
    radical = [a for a in range(N) if not (a & ONE)]
    socle = {a for a in range(N) if all(multiply(a, b) == 0 for b in radical)}
    assert socle == {0, U, V, U ^ V}
    assert {multiply(a,b) for a in radical for b in radical} == {0,U,V,U^V}
    assert all(multiply(multiply(a,b),c)==0 for a in radical for b in radical for c in radical)

    orbits = {}
    reps = []
    for a in range(N):
        if a in orbits:
            continue
        idx = len(reps)
        reps.append(a)
        for b in {multiply(a, t) for t in units}:
            assert b not in orbits
            orbits[b] = idx
    assert len(orbits) == N and len(reps) == 15
    ann = {a: frozenset(b for b in range(N) if multiply(a,b)==0) for a in reps}
    assert len(set(ann.values())) == 10

    # From the defining quotient-totient/Moebius formula for C_R.
    matrix = []
    for a in reps:
        size_ideal = len({multiply(a,b) for b in range(N)})
        phi = 1 if a == 0 else size_ideal // 2
        row = []
        for b in reps:
            z = multiply(a,b)
            mu = 1 if z == 0 else (-1 if z in socle else 0)
            row.append(phi*mu)
        matrix.append(row)
    assert exact_rank(matrix) == 9
    rows = {a: matrix[orbits[a]] for a in (0, ONE, X,Y,Z,U,V,X+Y,X+Z,Y+Z,X+Y+Z)}
    relation = [rows[X+Y][j]+rows[X+Z][j]+rows[Y+Z][j]-rows[X+Y+Z][j]
                -2*(rows[X][j]+rows[Y][j]+rows[Z][j]) +2*(rows[0][j]+rows[U][j])
                for j in range(15)]
    assert relation == [0]*15
    print('VERIFY_OK order=64 classes=15 annihilator_types=10 rank=9 relation=zero')
    return reps, matrix

if __name__ == '__main__':
    validate()
