"""Deterministic checks for exact stationary chiral-tumble moments.

Run with Python 3 using only its standard library. The linear systems implement
stationarity of the Markov generator, independently of the complex-moment proof.
"""
from math import sqrt, isclose


def solve(matrix, rhs):
    n = len(rhs)
    a = [list(map(float, row)) + [float(y)] for row, y in zip(matrix, rhs)]
    for k in range(n):
        p = max(range(k, n), key=lambda r: abs(a[r][k]))
        a[k], a[p] = a[p], a[k]
        assert abs(a[k][k]) > 1e-14
        pivot = a[k][k]
        a[k] = [value / pivot for value in a[k]]
        for r in range(n):
            if r == k:
                continue
            multiplier = a[r][k]
            a[r] = [v - multiplier*w for v, w in zip(a[r], a[k])]
    return [row[-1] for row in a]


def moments(mu, speed, clockwise, anticlockwise):
    gamma = (clockwise + anticlockwise) / 2
    eta = (clockwise - anticlockwise) / 2
    w = speed / sqrt(2)
    # Sign monomials: 1, s, t, st; C[h,k] is the coefficient of k in Lh.
    C = [[0.0] * 4 for _ in range(4)]
    C[1][1] = -2*gamma; C[1][2] = -2*eta
    C[2][1] = 2*eta; C[2][2] = -2*gamma
    C[3][3] = -4*gamma
    out = {(0, 0, 0): 1.0, (0, 0, 1): 0.0,
           (0, 0, 2): 0.0, (0, 0, 3): 0.0}
    for d in range(1, 5):
        for i in range(d+1):
            j = d-i
            A = [[(d*mu if h == k else 0.0)-C[h][k]
                  for k in range(4)] for h in range(4)]
            b = [i*w*out[(i-1, j, h^1)] if i else 0.0 for h in range(4)]
            for h in range(4):
                if j:
                    b[h] += j*w*out[(i, j-1, h^2)]
            ans = solve(A, b)
            for h in range(4):
                out[(i, j, h)] = ans[h]
    return out


def formulas(mu, speed, a, b):
    G, E = a+b, a-b
    A, B = mu+G, 3*mu+G
    Q, R = A*A+E*E, B*B+E*E
    odd = 3*speed**4*E / (4*A*Q*R)
    even = speed**4*E**2*(E**2+5*G**2+14*G*mu+9*mu**2) / (4*mu*A*Q**2*R)
    variance = speed**2*A/(2*mu*Q)
    return odd, even, variance


def close(x, y):
    return isclose(x, y, rel_tol=3e-10, abs_tol=2e-12)


def main():
    checks = 0
    for mu in (0.3, 0.7, 1.8, 4.0):
        for speed in (0.5, 1.6):
            for a, b in ((0.2, 0.2), (1.0, 1.0), (0.2, 0.9), (0.9, 0.2),
                         (0.5, 2.7), (2.7, 0.5), (1.1, 3.6), (3.6, 1.1)):
                r = moments(mu, speed, a, b)
                odd, sqcov, var = formulas(mu, speed, a, b)
                for x, y in ((r[3,1,0], odd),
                             (r[1,3,0], -odd),
                             (r[2,0,0], var),
                             (r[0,2,0], var),
                             (r[1,1,0], 0.0),
                             (r[2,2,0]-r[2,0,0]*r[0,2,0], sqcov),
                             (r[1,0,0], 0.0),
                             (r[0,1,0], 0.0)):
                    assert close(x, y), (mu, speed, a, b, x, y)
                    checks += 1
                # Gaussian positional noise has no effect on these connected moments.
                for D in (0.0, 0.17, 3.7):
                    sigma2 = D/mu
                    mixed = r[3,1,0] + 3*sigma2*r[1,1,0]
                    cross2 = (r[2,2,0] + sigma2*(r[2,0,0]+r[0,2,0])
                              + sigma2**2)
                    centered = cross2-(r[2,0,0]+sigma2)*(r[0,2,0]+sigma2)
                    assert close(mixed, odd) and close(centered, sqcov)
                    checks += 2
                if a == b:
                    assert abs(odd) < 1e-14 and abs(sqcov) < 1e-14
                else:
                    assert odd*(a-b)>0 and sqcov>0
                checks += 2
    print(f"PASS {checks} independent deterministic moment checks")

if __name__ == '__main__':
    main()
