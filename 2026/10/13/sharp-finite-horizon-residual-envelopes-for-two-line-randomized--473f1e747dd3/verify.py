"""Exact small-instance checks for the two-line randomized-projection envelope.

Requires only the Python standard library. The continuum-parameter, all-horizon assertions and their proofs are
analytical, not certified by tests.
"""
from fractions import Fraction as Q
from itertools import product
from math import exp


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def mat_vec(M, x):
    return tuple(dot(row, x) for row in M)


def mat_sum(A, B):
    return tuple(tuple(a+b for a, b in zip(ar, br)) for ar, br in zip(A, B))


def project_matrix(u):
    return tuple(tuple((Q(i == j) - u[i]*u[j]) for j in range(2)) for i in range(2))


def projected_residual(x, H):
    return dot(x, mat_vec(H, x))


def check_one(m, n):
    # Rational unit-circle parameterization gives exact, nonparallel row normals.
    a = Q(m, n)
    c, s = (1-a*a)/(1+a*a), (2*a)/(1+a*a)
    assert c*c + s*s == 1
    u1, u2 = (Q(1), Q(0)), (c, s)
    P = [project_matrix(u1), project_matrix(u2)]
    H = tuple(tuple((u1[i]*u1[j]+u2[i]*u2[j])/2
                    for j in range(2)) for i in range(2))
    q = (1+c*c)/2
    cases = 0
    for e0 in [(Q(1), Q(0)), (Q(2), Q(-3)),
               (u1[0]-u2[0], u1[1]-u2[1])]:
        r0 = projected_residual(e0, H)
        e02 = dot(e0, e0)
        for t in range(1, 8):
            actual = Q(0)
            for picks in product((0, 1), repeat=t):
                e = e0
                for choice in picks:
                    e = mat_vec(P[choice], e)
                actual += projected_residual(e, H)
            actual /= 2**t
            expected = (1-c*c)/2 * q**(t-1) * (e02-r0)
            assert actual == expected, (m, n, e0, t, actual, expected)
            cases += 1
        if e0 == (u1[0]-u2[0], u1[1]-u2[1]):
            assert r0/e02 == (1-c)/2
            assert expected/e02 == ((1-c)*(1+c)**2/4)*q**6
            first_ratio = (1+c)**2/2
            actual_ratio = (1-c*c)/2 * (e02-r0)/r0
            assert first_ratio == actual_ratio
    return cases


def h(t, c):
    return 1+(2*t-5)*c+c*c-(2*t+1)*c**3


def unique_root_numerical(t):
    a, b = 0.0, 1.0
    for _ in range(100):
        c = (a+b)/2
        if h(t, c) > 0:
            a = c
        else:
            b = c
    return (a+b)/2


def main():
    total = 0
    for n in (2, 3, 4, 5, 7, 9, 11, 13, 17):
        for m in range(1, n+1):
            total += check_one(m, n)

    # Compare the factored derivative identity with its cubic numerator exactly.
    differential_cases = 0
    for t in range(1, 28):
        for k in range(1, 30):
            c = Q(k, 31)
            dlog = -1/(1-c)+2/(1+c)+2*(t-1)*c/(1+c*c)
            assert dlog*(1-c)*(1+c)*(1+c*c) == h(t, c)
            differential_cases += 1

    assert h(1, Q(1, 3)) == 0
    previous = 0.0
    for t in range(1, 501):
        c = unique_root_numerical(t)
        assert 0 < c < 1 and c > previous
        assert abs(h(t, c)) < 3e-10
        previous = c
    for t in (100, 1000, 10000, 100000):
        c = unique_root_numerical(t)
        q = (1+c*c)/2
        G = ((1-c)*(1+c)**2/4)*q**(t-1)
        assert abs(t*(1-c)-1) < 1e-2
        assert abs(t*G-1/exp(1)) < 1e-3
    print(f"VERIFY_OK {total} exact rational path tests; "
          f"{differential_cases} exact derivative identities; "
          "500 horizon roots; four asymptotic checks")


if __name__ == '__main__':
    main()
