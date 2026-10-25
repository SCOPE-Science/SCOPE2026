#!/usr/bin/env python3
"""Reproducible symbolic and high-precision checks for the triangle flip-saddle theorem.

Requirements: Python 3.10+, SymPy 1.10+ (includes mpmath). All statements of
validity for an interval, and the existence/uniqueness proof, are analytical;
these computations verify coefficients and finite examples only.
"""
import sympy as sp
import mpmath as mp


def symbolic_checks():
    t, d = sp.symbols('t d', real=True)
    m2, m4, h2, h4 = sp.symbols('m2 m4 h2 h4', real=True)
    alpha = 2 * sp.pi / 3
    delta = sp.sin(alpha + 2 * t) - sp.sin(alpha - t)
    poly = sp.series(delta, t, 0, 7).removeO().expand()
    assert sp.simplify(poly + sp.Rational(3, 2) * t
                       + 3 * sp.sqrt(3) * t**2 / 4
                       - sp.Rational(3, 4) * t**3
                       - 5 * sp.sqrt(3) * t**4 / 16
                       + sp.Rational(11, 80) * t**5
                       + 7 * sp.sqrt(3) * t**6 / 160) == 0

    m = m2 * d**2 + m4 * d**4
    h = sp.Rational(4, 3) + h2 * d**2 + h4 * d**4
    p = sp.series(poly.subs(t, m + d) + poly.subs(t, m - d), d, 0, 6).removeO().expand()
    q = sp.series(h * (poly.subs(t, m + d) - poly.subs(t, m - d)) + 4*d,
                  d, 0, 6).removeO().expand()
    first = sp.solve([p.coeff(d, 2), q.coeff(d, 3)], [m2, h2], dict=True)[0]
    second = sp.solve([p.subs(first).expand().coeff(d, 4),
                       q.subs(first).expand().coeff(d, 5)], [m4, h4], dict=True)[0]
    coefficients = {**first, **second}
    assert coefficients == {m2: -sp.sqrt(3)/2,
                            h2: sp.Rational(8, 3),
                            m4: -11*sp.sqrt(3)/12,
                            h4: sp.Rational(392, 45)}
    m = m.subs(coefficients)
    h = h.subs(coefficients)
    def tangent(a):
        return 1 + h * (2 * sp.cos(alpha + 2*a) + sp.cos(alpha - a))
    def transverse(a):
        return 1 + 3*h*sp.cos(alpha - a)
    par = sp.series(tangent(m+d)*tangent(m-d), d, 0, 5).removeO().expand()
    per = sp.series(transverse(m+d)*transverse(m-d), d, 0, 5).removeO().expand()
    assert sp.simplify(par - (1 - 16*d**2 - sp.Rational(848, 15)*d**4)) == 0
    assert sp.simplify(per - (1 + sp.Rational(224, 5)*d**4)) == 0
    assert sp.simplify(sp.Rational(224, 5) * (sp.Rational(3, 8)**2)
                       - sp.Rational(63, 10)) == 0
    print('PASS: exact Taylor, branch, and two multiplier expansions')


def numeric_checks():
    mp.mp.dps = 70
    alpha = 2*mp.pi/3
    for eps in ['0.00001','0.0001','0.001','0.005','0.01','0.025','0.05']:
        eps = mp.mpf(eps)
        h = mp.mpf(4)/3 + eps
        d0 = mp.sqrt(3*eps/8)
        m0 = -mp.sqrt(3)*d0*d0/2
        def gap(a): return mp.sin(alpha+2*a)-mp.sin(alpha-a)
        # Explicit two-cycle equations; two independent unknowns.
        m,d = mp.findroot((lambda mm,dd: gap(mm+dd)+gap(mm-dd),
                           lambda mm,dd: h*(gap(mm+dd)-gap(mm-dd))+4*dd),
                          (m0, d0), solver='mdnewton', tol=mp.mpf('1e-55'))
        a,b = m+d,m-d
        f=lambda x: x+h*gap(x)
        assert abs(f(a)-b) < mp.mpf('1e-52')
        assert abs(f(b)-a) < mp.mpf('1e-52')
        assert a!=b
        # Verify the full three-coordinate map, rather than only the ray.
        X=mp.matrix([alpha+2*a,alpha-a,alpha-a])
        Y=mp.matrix([alpha+2*b,alpha-b,alpha-b])
        def F(z):
            s=[mp.sin(z[i]) for i in range(3)]
            S=sum(s)
            return mp.matrix([z[i]+h*(3*s[i]-S) for i in range(3)])
        assert max(abs(F(X)[i]-Y[i]) for i in range(3))<mp.mpf('1e-52')
        assert max(abs(F(Y)[i]-X[i]) for i in range(3))<mp.mpf('1e-52')
        def t_mult(x): return 1+h*(2*mp.cos(alpha+2*x)+mp.cos(alpha-x))
        def s_mult(x): return 1+3*h*mp.cos(alpha-x)
        p=t_mult(a)*t_mult(b)
        q=s_mult(a)*s_mult(b)
        assert 0<p<1 and q>1, (eps, p, q)
        if eps < mp.mpf('.01'):
            assert abs((h-mp.mpf(4)/3)/d**2-mp.mpf(8)/3) < 1
        if eps <= mp.mpf('.001'):
            assert abs((q-1)/eps**2-mp.mpf(63)/10) < mp.mpf('.05')
            assert abs((p-1)/eps+6) < mp.mpf('.01')
        print('PASS',mp.nstr(eps,6),'m',mp.nstr(m,12),'d',mp.nstr(d,12),
              'parallel',mp.nstr(p,14),'transverse',mp.nstr(q,14))
    print('PASS: 7 exact-equation numerical cases, full-map and multipliers')


if __name__ == '__main__':
    symbolic_checks()
    numeric_checks()
