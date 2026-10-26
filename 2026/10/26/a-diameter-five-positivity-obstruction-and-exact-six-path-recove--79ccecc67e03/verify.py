#!/usr/bin/env python3
"""Exact coefficient certificate for third-order Radau IIA heat steps on paths.

Run: python verify.py --build-certificate  (creates certificate)
     python verify.py                      (checks immutable certificate)
Requires SymPy 1.14.
"""
import argparse
import json
from pathlib import Path
import sympy as s

H = s.Symbol('h')
Z = s.Symbol('z')
ROOT = Path(__file__).resolve().parent
CERT = ROOT / 'certificates' / 'path_radau_coefficients.json'
Q5 = H**5 + 35*H**4 + 168*H**3 + 216*H**2 + 60*H - 12
D6 = ((H**2+4*H+6)*(2*H**2+4*H+3)*
      (3*H**2+4*H+2)*(H**4+16*H**3+100*H**2+96*H+36))

def laplacian(n, weights=None):
    L = s.zeros(n)
    if weights is None:
        weights = [s.Integer(1)]*(n-1)
    for j,w in enumerate(weights):
        L[j,j] += w; L[j+1,j+1] += w
        L[j,j+1] -= w; L[j+1,j] -= w
    return L

def coeffs(expr):
    p=s.Poly(s.expand(expr),H)
    if p.domain not in (s.ZZ,s.QQ):
        assert all(v.is_Rational for v in p.all_coeffs())
    return [str(v) for v in reversed(p.all_coeffs())]

def as_poly(expr):
    return s.Poly(s.cancel(expr),H).as_expr().expand()

def certificate():
    rows=[]
    for n in range(2,7):
        L=laplacian(n)
        A=6*s.eye(n)-2*H*L
        Q=6*s.eye(n)+4*H*L+H**2*(L**2)
        determinant=s.factor(Q.det(method='domain-ge'))
        assert all(c > 0 for c in s.Poly(determinant,H).all_coeffs())
        T = Q.inv(method='DM')*A
        assert all(s.cancel(sum(T[i,j] for j in range(n))-1)==0 for i in range(n))
        mat=[]
        for i in range(n):
            for j in range(i,n):
                numerator=as_poly(s.cancel(T[i,j]*determinant))
                assert s.simplify(numerator/determinant-T[i,j])==0
                cc=coeffs(numerator)
                if n==6 and (i,j)==(0,5):
                    assert s.simplify(T[i,j]-H**5*Q5/D6)==0
                    assert s.Poly(numerator,H).eval(0)==0
                else:
                    assert all(s.Rational(c)>=0 for c in cc)
                    assert any(s.Rational(c)>0 for c in cc)
                mat.append({'i':i,'j':j,'numerator_low_to_high':cc})
        rows.append({'n':n,'determinant_low_to_high':coeffs(determinant),
                     'upper_triangle':mat})
    return rows

def check_other_properties():
    rr=(1+Z/s.Integer(3))/(1-2*Z/s.Integer(3)+Z**2/s.Integer(6))
    polynomial=s.series(rr,Z,0,6).removeO().expand()
    assert s.expand(polynomial).coeff(Z,5)==-s.Rational(1,108)
    assert s.expand(polynomial).coeff(Z,4)==s.Rational(1,36)
    # P6 opposite-end pair has the promised exact threshold.
    assert s.Poly(Q5,H).count_roots(s.Rational(131359,1000000),s.Rational(131360,1000000))==1
    assert s.Poly(Q5,H).count_roots(0,s.oo)==1
    assert Q5.subs(H,0)<0
    assert s.limit(Q5,H,s.oo)>0
    # An independent rational matrix evaluation with nonuniform positive conductances.
    L=laplacian(6,[s.Rational(v) for v in (1,2,3,4,5)])
    h0=s.Rational(1,100)
    A=6*s.eye(6)-2*h0*L
    Q=6*s.eye(6)+4*h0*L+h0*h0*L**2
    T=Q.inv()*A
    assert T[0,5]<0
    assert all(sum(T[i,j] for j in range(6))==1 for i in range(6))
    return 'Radau coefficient, root-isolation and weighted-path checks'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--build-certificate',action='store_true')
    args=ap.parse_args()
    rows=certificate()
    if args.build_certificate:
        CERT.parent.mkdir(parents=True,exist_ok=True)
        CERT.write_text(json.dumps({'description':'Common-denominator exact polynomial certificate',
                                    'normalization':'T=(6I-2hL)(6I+4hL+h^2L^2)^-1',
                                    'path_orders':[2,3,4,5,6],
                                    'data':rows},ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    else:
        saved=json.loads(CERT.read_text(encoding='utf-8'))
        assert saved['data']==rows
    message=check_other_properties()
    print('VERIFY_OK 55 independent path entries, exact denominators, unique P6 root, '+message)

if __name__=='__main__':
    main()
