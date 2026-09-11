"""Corrected brute-force #C(Fp) and #C(Fp^2) for C4: y^2=x^5-5x^3+4x^2+x-1.
Fp2 = Fp[t]/(t^2+t+c) with c chosen so the polynomial is irreducible mod p.
Includes the coordinate-bug fix: the constant -1 belongs to the Fp-component only.
Stdlib only. Run: python3 point_counts.py
"""
import math

F_COEFFS = [1, 0, -5, 4, 1, -1]  # x^5..x^0


def f_aff(x, p):
    return (pow(x, 5, p) - 5 * pow(x, 3, p) + 4 * pow(x, 2, p) + x - 1) % p


def N1(p):
    n = 1  # one point at infinity (odd-degree model)
    for x in range(p):
        v = f_aff(x, p)
        if v == 0:
            n += 1
        elif pow(v, (p - 1) // 2, p) == 1:
            n += 2
    return n


def irr_const(p):
    for c in range(p):
        if not any((t * t + t + c) % p == 0 for t in range(p)):
            return c
    raise AssertionError(p)


def N2(p):
    c = irr_const(p)

    def mul(u, v):
        return ((u[0] * v[0] - c * u[1] * v[1]) % p,
                (u[0] * v[1] + u[1] * v[0] - u[1] * v[1]) % p)

    def pw(u, e):
        r = (1, 0)
        b = u
        while e:
            if e & 1:
                r = mul(r, b)
            b = mul(b, b)
            e >>= 1
        return r

    n = 1
    for x0 in range(p):
        for x1 in range(p):
            X = (x0, x1)
            x2 = mul(X, X)
            x3 = mul(x2, X)
            x5 = mul(x3, x2)
            fx = ((x5[0] - 5 * x3[0] + 4 * x2[0] + X[0] - 1) % p,
                  (x5[1] - 5 * x3[1] + 4 * x2[1] + X[1]) % p)
            if fx == (0, 0):
                n += 1
            elif pw(fx, (p * p - 1) // 2) == (1, 0):
                n += 2
    return n


def jacobian_order(p, n1, n2):
    s1 = p + 1 - n1
    sumsq = p * p + 1 - n2
    assert (s1 * s1 - sumsq) % 2 == 0, (p, s1, sumsq)
    b2 = (s1 * s1 - sumsq) // 2
    return 1 + s1 + b2 + s1 * p + p * p, s1, b2


if __name__ == "__main__":
    for p in [11, 23, 41]:
        n1, n2 = N1(p), N2(p)
        JV, s1, b2 = jacobian_order(p, n1, n2)
        print(f"p={p} #C(Fp)={n1} #C(Fp^2)={n2} s1={s1} b2={b2} #J(Fp)={JV}")
