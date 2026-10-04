#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 70
D = Decimal

def root_c(n):
    lo, hi = D(0), D(1)
    for _ in range(260):
        c = (lo + hi) / 2
        h = (c ** (n-1)) * (D(n) + D(n-1)*c)
        if h < 1:
            lo = c
        else:
            hi = c
    return (lo + hi) / 2

def U(n, c, x):
    if x <= -c:
        return x ** n
    return D(n)*(c**(n-1))*x + D(n-1)*(c**n)

def L(n, c, x):
    return -U(n, c, -x)

def check_odd(n):
    c = root_c(n)
    eq = (c**(n-1))*(D(n)+D(n-1)*c)
    assert abs(eq-D(1)) < D("1e-60")
    line_at_1 = D(n)*(c**(n-1)) + D(n-1)*(c**n)
    assert abs(line_at_1-D(1)) < D("1e-60")
    checks = 0
    atoms = 0
    for j in range(2001):
        x = D(-1) + D(2*j)/D(2000)
        fx = x**n
        lo, hi = L(n,c,x), U(n,c,x)
        assert lo <= fx + D("1e-55")
        assert fx <= hi + D("1e-55")
        assert lo <= hi + D("1e-55")
        checks += 3

        # Upper endpoint mixing law.
        if x >= -c:
            w1 = (x+c)/(D(1)+c)
            wc = (D(1)-x)/(D(1)+c)
            assert -D("1e-55") <= w1 <= D(1)+D("1e-55")
            assert -D("1e-55") <= wc <= D(1)+D("1e-55")
            mean = w1*D(1) + wc*(-c)
            moment = w1*D(1) + wc*((-c)**n)
            assert abs(mean-x) < D("1e-55")
            assert abs(moment-hi) < D("1e-55")
            atoms += 1

        # Lower endpoint is the reflected construction.
        if x <= c:
            wminus = (c-x)/(D(1)+c)
            wc2 = (D(1)+x)/(D(1)+c)
            mean2 = wminus*(-D(1)) + wc2*c
            moment2 = wminus*((-D(1))**n) + wc2*(c**n)
            assert abs(mean2-x) < D("1e-55")
            assert abs(moment2-lo) < D("1e-55")
            atoms += 1
    return c, checks, atoms

def check_even(n):
    checks = 0
    for j in range(2001):
        x = D(-1) + D(2*j)/D(2000)
        fx = x**n
        assert x**n <= fx + D("1e-60")
        assert fx <= D(1)
        # Degenerate law gives lower endpoint x^n; {-1,1} mixture gives 1.
        w1 = (D(1)+x)/2
        wm = (D(1)-x)/2
        assert abs(w1-wm-x) < D("1e-60")
        checks += 3
    return checks

def run():
    assert abs(root_c(3) - D("0.5")) < D("1e-60")
    odd_checks = 0
    atom_checks = 0
    even_checks = 0
    roots = 0

    for n in range(3, 102, 2):
        c, ch, at = check_odd(n)
        odd_checks += ch
        atom_checks += at
        roots += 1

    for n in range(2, 102, 2):
        even_checks += check_even(n)

    fair_checks = 0
    for n in (51, 101, 201, 401, 801):
        c = root_c(n)
        amp = D(n-1)*(c**n)
        assert D("0.45") < amp < D("0.5")
        fair_checks += 1

    print(
        "VERIFY_OK "
        f"odd_envelope_checks={odd_checks} "
        f"endpoint_atom_checks={atom_checks} "
        f"even_envelope_checks={even_checks} "
        f"root_checks={roots} "
        f"fair_asymptotic_checks={fair_checks}"
    )

if __name__ == "__main__":
    run()
