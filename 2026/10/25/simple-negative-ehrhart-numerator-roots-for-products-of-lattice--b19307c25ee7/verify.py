#!/usr/bin/env python3
"""Exact coefficient certificate for the polygon-product Ehrhart numerator theorem.

Requires Python 3.10+ and SymPy 1.12+. Run:
    python3 verify.py
The adjoining certificate is JSON containing all nonzero monomials in the
named discriminants and inequalities; every coefficient is an integer.
"""
import json
import sys
from pathlib import Path
import sympy as S

z, n = S.symbols('z n')
a, b, c, d = S.symbols('a b c d')
X, Y, U, V = S.symbols('X Y U V')


def product_numerator(A, B, C, D):
    c1 = A*(C+3) + 3*C + 4
    c2 = A*(4*C+3*D+3) + B*(3*C+D+6) + 3*C + 6*D + 1
    c3 = A*(C+3*D) + B*(3*C+4*D)
    c4 = B*D
    return S.expand(1 + c1*z + c2*z**2 + c3*z**3 + c4*z**4)


def check_product_formula():
    # Independent coefficient construction from the Ehrhart binomial basis.
    # Directly use the polynomial binomial, avoiding branch-sensitive symbolic binomial.
    p = ((n+2)*(n+1) + a*(n+1)*n + b*n*(n-1))/2
    q = ((n+2)*(n+1) + c*(n+1)*n + d*n*(n-1))/2
    pq = S.expand(p*q)
    derived = S.expand(sum(z**j*sum((-1)**k*S.binomial(5,k)*pq.subs(n,j-k)
                       for k in range(j+1)) for j in range(5)))
    assert S.expand(derived - product_numerator(a,b,c,d)) == 0


def spectral_certificate():
    rows = {}
    cases = {}
    F4 = product_numerator(X+Y+1,Y+1,U+V+1,V+1)
    p4 = S.expand(F4).coeff(z,1)
    q4 = S.expand(F4).coeff(z,2)
    r4 = S.expand(F4).coeff(z,3)
    s4 = S.expand(F4).coeff(z,4)
    cases['quartic_discriminant'] = (S.discriminant(F4,z), (X,Y,U,V),784)
    cases['quartic_root_witness_1'] = (p4**2-4*q4,(X,Y,U,V),36)
    cases['quartic_root_witness_2'] = (p4*r4-2*s4,(X,Y,U,V),36)
    F3 = product_numerator(X,0,U+V+1,V+1)
    cases['one_hollow_cubic_discriminant'] = (S.discriminant(F3,z),(X,U,V),75)
    F33 = product_numerator(X,0,U,0)
    cases['two_hollow_cubic_discriminant'] = (S.discriminant(F33,z),(X,U),25)
    Q1=product_numerator(0,0,U+V+1,V+1)
    cases['unimodular_times_interior_quadratic'] = (
        S.discriminant(Q1,z),(U,V),6)
    Q2=product_numerator(0,0,U,0)
    cases['unimodular_times_hollow_quadratic'] = (
        S.discriminant(Q2,z),(U,),3)
    for name,(expr,variables,expected) in cases.items():
        pp = S.Poly(S.expand(expr),*variables)
        entries = [[list(monomial),str(int(coefficient))] for monomial,coefficient in pp.terms()]
        assert len(entries) == expected,(name,len(entries),expected)
        assert all(int(value)>0 for _,value in entries),(name,'nonpositive coefficient')
        rows[name]={'variables':[str(q) for q in variables],'terms':entries}
    # The nontrivial sample has non-real individual factors but real product roots.
    tri = product_numerator(1,1,1,1)
    assert S.expand(tri-(1+11*z+30*z*z+11*z**3+z**4))==0
    # The integrality/positive-interior threshold matters: an artificial
    # continuous parameter below one permits a nonreal pair.
    artificial = product_numerator(S.Rational(1,100),S.Rational(1,100),67,4)
    assert S.discriminant(artificial,z)<0
    return rows


def main():
    check_product_formula()
    rows=spectral_certificate()
    dest=Path(__file__).with_name('coefficient_certificate.json')
    payload={'format':'positive-integer-monomial-expansions-v1',
             'claim':'Every recorded polynomial has exactly the displayed positive monomials.',
             'polynomials':rows}
    encoded=json.dumps(payload,indent=2,ensure_ascii=False,sort_keys=True)+'\n'
    if '--emit-certificate' in sys.argv:
        dest.write_text(encoded,encoding='utf-8')
    else:
        assert dest.read_text(encoding='utf-8')==encoded,'certificate differs from exact symbolic expansion'
    print('POLYGON_PRODUCT_CERTIFIED', 'monomial_counts=',
          ','.join('%s:%s'%(key,len(val['terms'])) for key,val in rows.items()))


if __name__=='__main__':
    main()
