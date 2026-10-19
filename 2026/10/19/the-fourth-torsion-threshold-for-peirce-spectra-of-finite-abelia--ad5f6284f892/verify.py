"""Exact finite-abelian core-quandle algebra verification (Python 3, SymPy)."""
from itertools import product
from fractions import Fraction
import sympy as sp

def group(moduli):
    el=list(product(*(range(n) for n in moduli)))
    ix={x:i for i,x in enumerate(el)}
    def sub(a,b): return tuple((2*b[j]-a[j])%moduli[j] for j in range(len(moduli)))
    return el,ix,sub

def right_matrix(moduli,coeff):
    el,ix,sub=group(moduli)
    m=len(el)
    result=sp.zeros(m,m)
    for j,a in enumerate(el):
        for k,b in enumerate(el):
            result[ix[sub(a,b)],j]+=coeff[k]
    return result

def product_coeff(moduli,c,d):
    return right_matrix(moduli,d)*sp.Matrix(c)

def check_four_torsion(moduli,t):
    el,ix,_=group(moduli)
    j=next(i for i,n in enumerate(moduli) if n%4==0)
    n=len(el)
    u=sp.Matrix([(1+t*(-1)**g[j])/n for g in el])
    assert product_coeff(moduli,u,u)==u
    R=right_matrix(moduli,u)
    # An order-four character produces conjugate eigenvectors.
    f=sp.Matrix([sp.I**g[j] for g in el]); f_inv=sp.conjugate(f)
    assert R*f==t*f_inv and R*f_inv==t*f
    assert R*(f+f_inv)==t*(f+f_inv)
    assert R*(f-f_inv)==-t*(f-f_inv)
    return n

def check_nonfour(moduli):
    el,ix,_=group(moduli)
    n=len(el)
    base=sp.Matrix([int(i==0) for i in range(n)])
    assert product_coeff(moduli,base,base)==base
    spec=set(right_matrix(moduli,base).eigenvals())
    if all(m==2 for m in moduli):
        assert spec=={sp.Integer(1)}
    elif n>1:
        assert spec=={sp.Integer(1),sp.Integer(-1)}
    uniform=sp.Matrix([sp.Rational(1,n)]*n)
    assert product_coeff(moduli,uniform,uniform)==uniform
    spec2=set(right_matrix(moduli,uniform).eigenvals())
    if all(m==2 for m in moduli):
        assert spec2=={sp.Integer(1)}
    elif n>1:
        assert sp.Integer(0) in spec2
    return n

if __name__=='__main__':
    checks=0
    for G in [(4,),(8,),(12,),(4,2),(4,3),(2,4)]:
        for t in [sp.Rational(0),sp.Rational(2),sp.Rational(-3,2)]:
            check_four_torsion(G,t);checks+=1
    for G in [(2,),(2,2),(2,2,2),(3,),(5,),(6,),(2,3),(2,2,3),(10,)]:
        check_nonfour(G);checks+=1
    print(f'PASS {checks} exact checks for core-quandle idempotents and Peirce eigenvalues')
