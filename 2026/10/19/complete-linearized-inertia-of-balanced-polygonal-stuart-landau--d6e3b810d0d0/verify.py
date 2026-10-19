"""Exact-rational tests for polygonal Stuart-Landau linearization.

Run: python3 verify.py
Only the Python standard library is required. The general theorem is proved
algebraically in RESULT.md; finite tests are independent consistency checks.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random


def inertia(A):
    """Signature of a symmetric rational matrix by congruence elimination."""
    A = [list(map(Q, row)) for row in A]
    p = m = z = 0
    while A:
        n = len(A)
        t = next((i for i in range(n) if A[i][i]), None)
        if t is None:
            edge = next(((i, j) for i in range(n) for j in range(i + 1, n)
                         if A[i][j]), None)
            if edge is None:
                z += n
                break
            i, j = edge
            # Congruence: replace basis vector e_i by e_i+e_j.
            a = [row[i] for row in A]
            b = [row[j] for row in A]
            for k in range(n):
                if k != i:
                    A[i][k] = A[k][i] = a[k] + b[k]
            A[i][i] = a[i] + 2 * a[j] + b[j]
            t = i
        if t:
            A[0], A[t] = A[t], A[0]
            for row in A:
                row[0], row[t] = row[t], row[0]
        pivot = A[0][0]
        if pivot > 0:
            p += 1
        else:
            m += 1
        A = [[A[i][j] - A[i][0] * A[0][j] / pivot
              for j in range(1, n)] for i in range(1, n)]
    return p, m, z


def jacobian(points, c, k):
    n = len(points)
    J = [[Q(0) for _ in range(2 * n)] for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            for d in (0, 1):
                J[2 * i + d][2 * j + d] += c
        x, y = points[i]
        for d, a in enumerate((x, y)):
            for e, b in enumerate((x, y)):
                J[2 * i + d][2 * i + e] -= 2 * k * a * b
    return J


def field(points, c, k, growth):
    X = sum(x for x, _ in points)
    Y = sum(y for _, y in points)
    return [(growth[j] - k * (x*x+y*y)) * x + c*X for j, (x,y) in enumerate(points)], [
        (growth[j] - k * (x*x+y*y)) * y + c*Y for j, (x,y) in enumerate(points)]


def check_finite_difference(points, c, k, rng):
    n = len(points)
    growth = [k * (x*x+y*y) for x, y in points]
    directions = [(Q(rng.randrange(-3,4)), Q(rng.randrange(-3,4))) for _ in points]
    if all(x == y == 0 for x, y in directions):
        return 0
    eps = Q(1, 17)
    pp = [(x+eps*dx, y+eps*dy) for (x,y),(dx,dy) in zip(points, directions)]
    pm = [(x-eps*dx, y-eps*dy) for (x,y),(dx,dy) in zip(points, directions)]
    px, py = field(pp,c,k,growth)
    mx, my = field(pm,c,k,growth)
    d = [t for xy in directions for t in xy]
    J = jacobian(points,c,k)
    Jd = [sum(row[j]*d[j] for j in range(2*n)) for row in J]
    # The central difference for a cubic vector field has an exactly known cubic error.
    for j, (dx,dy) in enumerate(directions):
        correction = k * eps**2 * (dx*dx+dy*dy)
        assert (px[j]-mx[j])/(2*eps)+correction*dx == Jd[2*j]
        assert (py[j]-my[j])/(2*eps)+correction*dy == Jd[2*j+1]
    return 2*n


def main():
    rng = Random(270821)
    tests = 0
    for n in range(3, 11):
        for _ in range(24):
            while True:
                P = [(Q(rng.randrange(-5,6)),Q(rng.randrange(-5,6))) for _ in range(n-1)]
                P.append((-sum(p[0] for p in P),-sum(p[1] for p in P)))
                if any(x == y == 0 for x,y in P):
                    continue
                if all(x*y0 == y*x0 for (x,y) in P for x0,y0 in P):
                    continue
                break
            c = Q(rng.randrange(1,7),rng.randrange(1,7))
            k = Q(rng.randrange(1,6),rng.randrange(1,6))
            assert inertia(jacobian(P,c,k)) == (2,n,n-2)
            assert sum(x for x,y in P) == sum(y for x,y in P) == 0
            growth = [k*(x*x+y*y) for x,y in P]
            fx,fy=field(P,c,k,growth)
            assert all(a==0 for a in fx+fy)
            tests += 3 + check_finite_difference(P,c,k,rng)
    for n in range(3,12):
        # Obtain an exact closure with n nonzero collinear entries.
        lengths = [Q(1)]*(n-1)
        lengths.append(-sum(lengths))
        P=[(x,Q(0)) for x in lengths]
        k=Q(1)
        s=sum(1/(k*x*x) for x in lengths)
        for factor in [Q(1,3),Q(1),Q(4)]:
            c=factor*2/s
            expected=((1,n,n-1) if factor<1 else
                      ((1,n-1,n) if factor==1 else (2,n-1,n-1)))
            assert inertia(jacobian(P,c,k))==expected
            assert sum(x for x,y in P)==0
            tests += 2+check_finite_difference(P,c,k,rng)
    print('VERIFY_OK: exact rational polynomial/Jacobian/inertia/closure assertions =',tests)

if __name__=='__main__':
    main()
