"""Independent numerical consistency checks for a logarithmic Hankel symbol.
The paper proof, not finite truncations, establishes the infinite statements.
"""
import cmath
import math


def variance_coefficients(w, cutoff=12000):
    eta = (1 - w.conjugate()) / (1 - w)
    return sum(abs((-eta)**n - w.conjugate()**n)**2 / (n*n)
               for n in range(1, cutoff + 1))


def variance_radial_formula(r, cutoff=12000):
    return math.pi**2 / 6 + 2 * sum(r**n / (n*n) for n in range(1, cutoff + 1))


def hilbert_rayleigh(n):
    # Quadratic form on vector ((k+1)^(-1/2))_{k=1}^n.
    # Uses O(n^2) arithmetic only for a small reproducibility witness.
    v = [1 / math.sqrt(k + 1) for k in range(1, n + 1)]
    norm2 = sum(x*x for x in v)
    return sum(v[j]*v[k]/(j+k+3) for j in range(n) for k in range(n)) / norm2


def main():
    for w in [0j, 0.25+0.15j, -0.4+0.3j, 0.3+0.4j, 0.8+0j]:
        v = variance_coefficients(w)
        assert v <= math.pi**2/2 + 0.0001
        if abs(w.imag) < 1e-14 and w.real >= 0:
            assert abs(v - variance_radial_formula(w.real)) < 0.0002
        print('w=', w, 'variance=', format(v,'.11f'))
    print('limiting_garsia=', math.pi / math.sqrt(2))
    for n in [20, 60, 160]:
        q = hilbert_rayleigh(n)
        assert q < math.pi
        print('N=', n, 'Hilbert lower Rayleigh=', format(q,'.11f'))
    print('PASS: finite tests support explicit formulas, not infinite certification')


if __name__ == '__main__':
    main()
