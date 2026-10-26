"""Finite-dimensional numerical checks for the explicit Cantor Fourier determinant."""
import cmath
import itertools
import math


def logabsdet(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    logdet = 0.0
    for j in range(n):
        k = max(range(j, n), key=lambda r: abs(a[r][j]))
        if abs(a[k][j]) < 1e-12:
            raise ArithmeticError('numerically singular matrix')
        a[j], a[k] = a[k], a[j]
        piv = a[j][j]
        logdet += math.log(abs(piv))
        for i in range(j+1, n):
            t = a[i][j]/piv
            a[i][j] = 0j
            for l in range(j+1, n):
                a[i][l] -= t * a[j][l]
    return logdet


def matrix(b, n):
    patterns = tuple(itertools.product((0, 1), repeat=n))
    x = [2*sum(v[j]/(b**(j+1)) for j in range(n)) for v in patterns]
    freq = [b/4*sum(v[j]*(b**j) for j in range(n)) for v in patterns]
    size = 1 << n
    return [[cmath.exp(2j*math.pi*y*l)/math.sqrt(size)
             for l in freq] for y in x]


def main():
    checked = 0
    for b in (3, 4, 5, 6, 7, 9, 10):
        for n in range(1, 6):
            actual = logabsdet(matrix(b,n))
            expected = ((n-1)*(2**(n-1))*math.log(math.cos(math.pi/(2*b)))) if b%2 else 0.0
            if abs(actual-expected) > 1e-7:
                raise AssertionError((b,n,actual,expected))
            checked += 1
    for b in range(3,12):
        for n in range(1,7):
            # Both normalized-branch factors are determined by parity of b.
            for v in itertools.product((0,1), repeat=n):
                lam = b/4*sum(v[j]*b**j for j in range(n))
                c = cmath.exp(4j*math.pi*lam)
                target = (-1)**sum(v) if b%2 else 1
                assert abs(c-target) < 1e-7
            checked += 1
    print('VERIFY_OK direct_determinants=35 parity_block_checks=54')

if __name__ == '__main__':
    main()
