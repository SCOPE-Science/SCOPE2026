"""Reproducible checks for the one-hub equicorrelation scaling theorem.

Run: python3 VERIFY.py
Only Python standard-library modules are required.  These finite tests do not
replace the proof of optimality for arbitrary dimensions and parameters.
"""
from fractions import Fraction as F
from math import sqrt, exp, log, isclose
from random import Random


def construct(m, a, b):
    n = m + 1
    A = [[1.0 if i == j else float(b) for j in range(n)] for i in range(n)]
    for j in range(1, n):
        A[0][j] = A[j][0] = float(a)
    return A


def jacobi_eigenvalues(A):
    """Symmetric Jacobi rotations; independent of the closed-form eigenvalues."""
    n = len(A)
    B = [row[:] for row in A]
    for sweep in range(150 * n * n):
        p, q = max(((i, j) for i in range(n) for j in range(i+1, n)),
                   key=lambda t: abs(B[t[0]][t[1]]))
        if abs(B[p][q]) < 1e-12:
            break
        tau = (B[q][q] - B[p][p])/(2.0 * B[p][q])
        t = (1.0 if tau >= 0.0 else -1.0)/(abs(tau) + sqrt(1.0 + tau*tau))
        co = 1.0/sqrt(1.0+t*t)
        si = t*co
        pp, qq, pq = B[p][p], B[q][q], B[p][q]
        B[p][p] = pp - t*pq
        B[q][q] = qq + t*pq
        B[p][q] = B[q][p] = 0.0
        for k in range(n):
            if k == p or k == q:
                continue
            kp, kq = B[k][p], B[k][q]
            B[k][p] = B[p][k] = co*kp - si*kq
            B[k][q] = B[q][k] = si*kp + co*kq
    else:
        raise AssertionError('Jacobi rotations did not converge')
    return sorted(B[i][i] for i in range(n))


def optimal_x(m, a, b):
    c = 1 + (m-1)*b
    if a*a*c >= m*b*b:
        return c, 'strong'
    return b*(1-b)/(b-a*a), 'weak'


def eigen_formula(m, a, b, x):
    c = 1+(m-1)*b
    z = sqrt(float((x-c)*(x-c)+4*m*a*a*x))
    return (float(x+c)-z)/2.0, float(1-b), (float(x+c)+z)/2.0


def cond(m, a, b, x):
    lo, mid, hi = eigen_formula(m, a, b, x)
    return max(lo, mid, hi)/min(lo, mid, hi)


def scaled_condition(A, scales):
    n = len(A)
    vals = jacobi_eigenvalues([[scales[i]*A[i][j]*scales[j] for j in range(n)]
                               for i in range(n)])
    assert vals[0] > 0
    return vals[-1]/vals[0]


rng = Random(20261027)
checks = 0
cases = []
for m in (3, 4, 5, 6, 7, 9):
    # Fractions provide exact checks of the proposed eigenvalue crossings.
    for b in (F(-1, 8), F(-1, 12), F(0), F(1, 10), F(1, 4), F(1, 2)):
        c = 1+(m-1)*b
        if c <= 0:
            continue
        for a in (F(1, 20), F(1, 10), F(1, 5), F(3, 10), F(2, 5), F(1, 2)):
            if m*a*a >= c:
                continue
            x, branch = optimal_x(m, a, b)
            assert x > 0
            e = 1-b
            if branch == 'strong':
                assert a*a*c >= m*b*b
                assert x == c
            else:
                assert a*a*c < m*b*b
                assert b != 0
                assert (x-e)*(c-e)-m*a*a*x == 0
                assert (x+c-e) > 0
                assert (x+c-e-e)*b > 0
            checks += 5
            A = construct(m, a, b)
            optimum = cond(m, a, b, x)
            closed = ((sqrt(float(c))+sqrt(m)*float(a)) /
                      (sqrt(float(c))-sqrt(m)*float(a))) if branch == 'strong' else \
                     max(float((x+m*b)/e), float(e/(x+m*b)))
            assert isclose(optimum, closed, rel_tol=1e-10, abs_tol=2e-10)
            eig = jacobi_eigenvalues([[A[i][j]*(sqrt(float(x)) if i == 0 else 1.0)*
                                      (sqrt(float(x)) if j == 0 else 1.0)
                                      for j in range(m+1)] for i in range(m+1)])
            assert isclose(eig[-1]/eig[0], optimum, rel_tol=3e-10)
            checks += 2
            cases.append((m, a, b, x, optimum))

# Unrestricted positive diagonal variations; these numerical trials do not
# establish global optimality (the convex feasibility proof establishes it).
for m, a, b, x, optimum in cases:
    A = construct(m, a, b)
    for j in range(6):
        s = [sqrt(float(x))*exp(rng.uniform(-.4,.4))]
        s.extend(exp(rng.uniform(-.4,.4)) for _ in range(m))
        observed = scaled_condition(A, s)
        assert observed >= optimum - 3e-8, (m,a,b,j,observed,optimum)
        checks += 1

# Exact dimension transition: b=1/10, a=1/5 gives m_crit=6.
a, b = F(1,5), F(1,10)
for m in range(3, 16):
    x, label = optimal_x(m,a,b)
    assert (label == 'strong') == (m <= 6)
    assert x == (1+(m-1)*b if m <= 6 else F(3,2))
    checks += 2

# Jacobi optimality iff b=0 or a^2=b^2 (on each sampled SPD family).
for m,a,b,x,_ in cases:
    if x == 1:
        assert b == 0 or a*a == b*b
    if b == 0 or a*a == b*b:
        assert x == 1
    checks += 2

print('PASS:', checks, 'finite exact/numerical assertions;',
      len(cases), 'admissible parameter triples')
