from fractions import Fraction
import sympy as sp


def determinant_data(primes):
    r = len(primes)
    xs = [p * p for p in primes]
    W = sp.Matrix([[x ** e for x in xs] for e in range(1, r + 1)])
    det_w = abs(int(W.det()))
    deltas = []
    for j in range(r):
        cols = []
        for k, x in enumerate(xs):
            cols.append([1] * r if k == j else [x ** e for e in range(1, r + 1)])
        M = sp.Matrix.hstack(*[sp.Matrix(c) for c in cols])
        deltas.append(abs(int(M.det())))
    return xs, det_w, deltas


for r in range(2, 9):
    primes = list(sp.primerange(2, 100))[:r]
    xs, det_w, deltas = determinant_data(primes)
    dr = deltas[-1]

    ratio_w = Fraction(xs[-1], 1)
    for i in range(r - 1):
        ratio_w *= Fraction(xs[-1] - xs[i], xs[i] - 1)
    assert Fraction(det_w, dr) == ratio_w

    for j in range(r - 1):
        ratio = Fraction(xs[-1], xs[j]) * Fraction(xs[-1] - 1, xs[j] - 1)
        for i in range(r - 1):
            if i != j:
                ratio *= Fraction(abs(xs[-1] - xs[i]), abs(xs[j] - xs[i]))
        assert Fraction(deltas[j], dr) == ratio

    print(f"r={r}: exact Vandermonde ratios verified")
