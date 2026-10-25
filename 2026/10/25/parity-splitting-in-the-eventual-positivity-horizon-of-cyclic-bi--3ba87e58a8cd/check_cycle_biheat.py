"""Reproducible numerical checks for cycle bi-Laplacian positivity asymptotics.

Python >=3.9 standard library only. Tests support, but do not replace,
analytic estimates in the accompanying result.
"""
import math

PI = math.pi
C = 16 * PI**4
SIGMA = 1 / 3000


def continuum(s, x=0.5, terms=16):
    return 1.0 + 2.0 * sum(
        math.exp(-s * C * k**4) * math.cos(2 * PI * k * x)
        for k in range(1, terms + 1)
    )


def cycle_kernel(n, s, j):
    """n times one entry of exp(-s*n**4*L**2), from the finite DFT."""
    ans = 1.0
    for k in range(1, (n - 1)//2 + 1):
        rho = (4 * n * n * math.sin(PI * k / n)**2)**2
        ans += 2.0 * math.exp(-s * rho) * math.cos(2 * PI * k * j / n)
    if n % 2 == 0:
        ans += math.exp(-16 * s * n**4) * (-1)**j
    return ans


def zero(fun, lower=SIGMA, upper=1/1500):
    assert fun(lower) < 0 < fun(upper)
    for _ in range(65):
        mid = (lower + upper) / 2
        if fun(mid) < 0:
            lower = mid
        else:
            upper = mid
    return (lower + upper) / 2


def multiply(A, B):
    n = len(A)
    out = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            a = A[i][k]
            if a:
                for j in range(n):
                    out[i][j] += a * B[k][j]
    return out


def exp_matrix(A):
    """Independent Taylor scaling-and-squaring matrix exponential."""
    n = len(A)
    row_norm = max(sum(abs(a) for a in row) for row in A)
    exponent = max(0, math.ceil(math.log2(row_norm * 4))) if row_norm else 0
    scale = 2**exponent
    B = [[a / scale for a in row] for row in A]
    ident = [[float(i == j) for j in range(n)] for i in range(n)]
    result = [row[:] for row in ident]
    term = [row[:] for row in ident]
    for k in range(1, 23):
        term = multiply(term, B)
        factor = 1.0 / k
        for i in range(n):
            for j in range(n):
                term[i][j] *= factor
                result[i][j] += term[i][j]
    for _ in range(exponent):
        result = multiply(result, result)
    return result


def laplacian_squared(n):
    L = [[(2.0 if i == j else 0.0)
          - (1.0 if ((j - i) % n in (1, n - 1)) else 0.0)
          for j in range(n)] for i in range(n)]
    return multiply(L, L)


def main():
    count = 0
    star = zero(lambda s: continuum(s))
    ex = lambda k: math.exp(-C * star * k**4)
    D = -2 * C * sum((-1)**k * k**4 * ex(k) for k in range(1, 12))
    Hxx = -8 * PI**2 * sum((-1)**k * k**2 * ex(k) for k in range(1, 12))
    G = (4 * PI**2 / 3) * C * star * sum(
        (-1)**k * k**6 * ex(k) for k in range(1, 12))
    even_coeff = -G / D
    odd_coeff = -(G + Hxx/8) / D
    assert 0.0004447 < star < 0.0004448
    assert D > 0 and Hxx > 0 and G < 0 and even_coeff > odd_coeff
    assert abs(continuum(star)) < 1e-13
    count += 3

    # Compare independent direct matrix exponential with cyclic DFT.
    for n in range(5, 11):
        L2 = laplacian_squared(n)
        for s in (0.0002, star, 0.0007):
            E = exp_matrix([[-s*n**4*z for z in row] for row in L2])
            for j in range(n):
                assert abs(n * E[0][j] - cycle_kernel(n, s, j)) < 3e-11, (n,s,j,E[0][j])
                count += 1

    # Verify antipodal location and the sign change on both sides.
    for n in (20,21,40,41,80,81,160,161,320,321):
        far = n // 2
        root = zero(lambda s: cycle_kernel(n,s,far))
        assert abs(cycle_kernel(n, root, far)) < 2e-13
        assert cycle_kernel(n,root-1e-7,far) < 0
        assert cycle_kernel(n,root+1e-7,far) > 0
        for j in range(n):
            assert cycle_kernel(n,root+1e-7,j) > -2e-13
            count += 1
        coeff = even_coeff if n%2==0 else odd_coeff
        assert abs(n*n*(root-star)-coeff)*n*n < .04
        count += 4

    # Derivative-dominance numerical margins at the continuum reference point.
    q = sum(k*k*math.exp(-C*SIGMA*(k**4-1)) for k in range(2,16))
    r = sum(k**4*math.exp(-C*SIGMA*(k**4-1)) for k in range(2,16))
    assert q < 0.01 and r < 0.1
    count += 2
    print('PASS',count,'checks')
    print('continuum horizon',format(star,'.17g'))
    print('even correction',format(even_coeff,'.17g'))
    print('odd correction',format(odd_coeff,'.17g'))
    print('parity gap',format(even_coeff-odd_coeff,'.17g'))


if __name__ == '__main__':
    main()
