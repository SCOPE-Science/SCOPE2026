"""Exact symbolic and finite checks for the RK4 positivity theorem on Hamming graphs.
Run: python verify_hamming_rk4.py ; requires SymPy.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb
import sympy as sp

D, q, z = sp.symbols('D q z', integer=True, positive=True)
k = D*(q-1)
a = sum([1,-(q-1)*z,q*(q-1)*z**2/2,-q**2*(q-1)*z**3/6,q**3*(q-1)*z**4/24])
b = z-q*z**2/2+q**2*z**3/6-q**3*z**4/24
m=D-1; e=q-1
B1 = m*e+q/2
C1 = q**2/6+m*q*e+sp.binomial(m,2)*e**2
D1 = q**3/24+sp.Rational(7,12)*m*q*q*e+sp.Rational(3,2)*sp.binomial(m,2)*q*e**2+sp.binomial(m,3)*e**3
B2=(D-2)*e+q
C2=sp.Rational(7,12)*q*q+sp.Rational(3,2)*(D-2)*q*e+sp.binomial(D-2,2)*e**2
T=2*D*(q-1)-3*(q-2)
h3=2/T
f=1-B1*z+C1*z**2-D1*z**3
g=1-B2*z+C2*z**2
expected=[None,sp.expand(z*f),sp.expand(z**2*g),sp.expand(z**3*(1-z/h3)),z**4]
for r in (1,2,3,4):
    actual=sp.series(sp.exp((D-r)*sp.log(a))*b**r,z,0,5).removeO()
    assert sp.factor(sp.cancel(sp.expand_func(actual-expected[r])))==0, ('heat kernel',r)

x=sp.symbols('x'); E,Q=sp.symbols('E Q', integer=True, nonnegative=True)
def bernstein_coeffs(poly,degree):
    p=sp.Poly(sp.expand(poly.subs(z,h3*x)),x)
    return [sp.cancel(sum(p.nth(j)*sp.binomial(i,j)/sp.binomial(degree,j) for j in range(i+1))) for i in range(degree+1)]
fb=bernstein_coeffs(f,3);gb=bernstein_coeffs(g,2)
assert fb[0]==gb[0]==1
for name,lst,indices in [('f',fb,(1,2)),('g',gb,(1,2))]:
    for i in indices:
        numer,_=sp.fraction(sp.cancel(lst[i].subs({D:E+3,q:Q+2})))
        polynomial=sp.Poly(sp.expand_func(numer),E,Q)
        assert all(t>0 for t in polynomial.coeffs()),(name,i,polynomial)
N,den=sp.fraction(sp.factor(sp.cancel(sp.expand_func(fb[3]))))
assert sp.simplify(sp.expand_func(fb[3].subs(D,3)-(64-5*q)/(81*q)))==0
# The d>=4 positivity certificate for N follows from this polynomial
cert=8*E**3*(Q+1)**3+48*E**2*(Q+1)**2*(Q+2)+2*E*(Q+1)*(5*Q+12)*(9*Q+16)+(Q+2)*(45*Q**2+242*Q+256)
assert sp.expand_func(sp.expand(N.subs({D:E+4,q:Q+2})-cert))==0
assert sp.simplify(den-3*T**3)==0
assert all(t>0 for t in sp.Poly(sp.expand(cert),E,Q).coeffs())
# A strict sign variation of Bernstein coefficients (1,b1,b2,b3),
# converted using x=y/(1+y), proves a unique positive root in (0,1)
# when D=3,q>=13, and no root there for all other admitted parameters.

# Direct rational row checks independent of the Hamming-distance formula.
# Transition generator acts as Q=Adjacency-degree*I.
def dist(u,v): return sum(a!=b for a,b in zip(u,v))
def row_powers(d,q):
    zero=(0,)*d
    w={zero:1};rows=[w]
    for _ in range(4):
        out=defaultdict(int)
        for v,c in w.items():
            out[v]-=d*(q-1)*c
            for i in range(d):
                for j in range(q):
                    if j!=v[i]:
                        nxt=v[:i]+(j,)+v[i+1:]
                        out[nxt]+=c
        w={u:c for u,c in out.items() if c}
        rows.append(w)
    return rows

def exact_entry(d,q,r,h):
    ss={D:d,globals()['q']:q}
    p=[sp.Integer(1),f,g,1-z/h3,sp.Integer(1)][r]
    return Fraction(str(sp.cancel((z**r*p).subs(ss).subs(z,sp.Rational(h.numerator,h.denominator)))))

checks=0
for d,q0 in [(3,2),(3,3),(3,12),(3,13),(3,17),(4,2),(4,4),(4,6),(5,2),(5,3)]:
    powers=row_powers(d,q0)
    bound=Fraction(2,2*d*(q0-1)-3*(q0-2))
    for h in [Fraction(1,4*d*(q0-1)),bound,Fraction(11,10)*bound]:
        row=defaultdict(Fraction)
        for j,wi in enumerate(powers):
            for v,coeff in wi.items():row[v]+=h**j*Fraction(coeff,sp.factorial(j))
        assert sum(row.values())==1
        expected_by_distance={r:exact_entry(d,q0,r,h) for r in range(1,min(d,4)+1)}
        for v in product(range(q0),repeat=d):
            r=dist((0,)*d,v)
            if r==0:continue
            assert row[v]==expected_by_distance.get(r,Fraction(0)), (d,q0,r,h,row[v])
            checks+=1
        if h==bound and not (d==3 and q0>=13):
            assert all(val>=0 for val in row.values())
        if h>bound:
            assert any(val<0 for val in row.values())
        if h==bound and d==3 and q0>=13:
            assert any(val<0 for val in row.values())
assert f.subs({D:3,q:13,z:sp.Rational(51,1000)})>0
assert f.subs({D:3,q:13,z:sp.Rational(5124,100000)})<0
print('VERIFY_OK: symbolic Hamming heat-kernel coefficients r=1..4; Bernstein positivity and sharp q=13 crossover certificates; '+str(checks)+' exact rational transition-entry comparisons')
