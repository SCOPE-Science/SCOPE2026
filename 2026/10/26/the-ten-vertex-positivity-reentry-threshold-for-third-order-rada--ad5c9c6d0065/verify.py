"""Exact rational certificate for two-stage Radau IIA diffusion on unit cycles.

Run from this directory: python verify.py
Requires SymPy; all calculations are symbolic, with integer coefficients.
"""
import json
from pathlib import Path
import sympy as sp

h = sp.symbols('h')


def laplacian(n):
    L = sp.zeros(n)
    for i in range(n):
        j = (i + 1) % n
        L[i, i] += 1
        L[j, j] += 1
        L[i, j] -= 1
        L[j, i] -= 1
    return L


def ascending(poly):
    return [int(c) for c in reversed(sp.Poly(poly, h).all_coeffs())]


def exact_entry(n, d, inv=None, L=None):
    if L is None:
        L = laplacian(n)
    A = 6*sp.eye(n) + 4*h*L + h*h*(L**2)
    B = 6*sp.eye(n) - 2*h*L
    if inv is None:
        inv = A.inv(method='DM')
    v = sp.factor(sp.cancel(sum(B[0, j] * inv[j, d] for j in range(n))))
    num, den = sp.fraction(v)
    return ascending(num), ascending(den), v


def full_certificate():
    entries = []
    for n in range(3, 11):
        L = laplacian(n)
        A = 6*sp.eye(n) + 4*h*L + h*h*(L**2)
        inv = A.inv(method='DM')
        for d in range(n//2 + 1):
            nums, dens, v = exact_entry(n, d, inv, L)
            # The domain-matrix inverse and reduction are performed exactly.
            assert all(x > 0 for x in dens)
            if n <= 9 or d < 5:
                assert all(x >= 0 for x in nums)
                assert any(x > 0 for x in nums)
            entries.append({'n':n,'distance':d,'numerator_ascending':nums,'denominator_ascending':dens})
    return {'schema_version':1,'polynomial_variable':'h','entries':entries}


def main():
    certificate = json.loads(Path(__file__).with_name('coefficients.json').read_text(encoding='utf-8'))
    rebuilt = full_certificate()
    assert rebuilt == certificate
    x = sp.symbols('x')
    f = (6-2*x)/(6+4*x+x*x)
    assert sp.expand(sp.series(f, x, 0, 6).removeO()).coeff(x,5) == sp.Rational(1,108)
    P = 10*h**5+255*h**4+936*h**3+954*h**2+216*h-36
    D=(8*h*h+8*h+3)*(h**4+12*h**3+58*h*h+72*h+36)*(25*h**4+100*h**3+170*h*h+120*h+36)
    row = [x for x in rebuilt['entries'] if x['n']==10 and x['distance']==5][0]
    numerator = sum(c*h**i for i,c in enumerate(row['numerator_ascending']))
    denominator = sum(c*h**i for i,c in enumerate(row['denominator_ascending']))
    assert sp.factor(numerator*D-denominator*2*h**5*P)==0
    assert len([c for c in sp.Poly(P,h).all_coeffs() if c < 0]) == 1
    assert P.subs(h,sp.Rational(1,10))<0<P.subs(h,sp.Rational(1,9))
    # At h=1/10, the diameter-five kernel is exactly negative.
    assert sp.cancel((2*h**5*P/D).subs(h,sp.Rational(1,10))) == -sp.Rational(3544,384641341535)
    print('VERIFY_OK',len(rebuilt['entries']),'exact rational cycle-distance entries; C10 quintic; fifth-order sign')


if __name__=='__main__':
    main()
