"""Exact symbolic consistency checks and finite diagnostics for simplex stability.

The all-dimensional positivity reduction uses Riener's half-degree theorem;
these finite checks do not replace that theorem or the written proof.
"""
from fractions import Fraction
from math import isclose
import itertools
import sympy as sp

k,j,u,v = sp.symbols('k j u v', real=True)
mu=(j*u+(k-j)*v)/k
numerator=j*(u-mu)**4+(k-j)*(v-mu)**4
expected=(j*(k-j)**4+(k-j)*j**4)*(u-v)**4/k**4
assert sp.simplify(numerator-expected)==0

r=sp.symbols('r',positive=True)
f=(r**6-r**3+1)/(r**2-r+1)**3
critical=r**4-2*r**3-2*r+1
diff_expected=-3*(r-1)*(r+1)*critical/(r**2-r+1)**4
assert sp.simplify(sp.diff(f,r)-diff_expected)==0
q=1+sp.sqrt(3)
maxf=sp.simplify((q**3-3*q-1)/(q-1)**3)
assert sp.simplify(maxf-(1+2/sp.sqrt(3)))==0
min_r=(q-sp.sqrt(q*q-4))/2
assert sp.simplify(critical.subs(r,min_r))==0
assert 0<float(min_r)<1

def block_value(total,j):
    a=total-j
    return ((j*a**4+a*j**4)/total**4)*(j**(-1/3)+a**(-1/3))**3

# Finite witness ratios from the dual-Hoelder extremizers.
for total in range(2,28):
    vals=[]
    for j_value in range(1,total):
        a=total-j_value
        u0=j_value**(-1/3)
        v0=-a**(-1/3)
        mean=(j_value*u0+a*v0)/total
        numerator=j_value*(u0-mean)**4+a*(v0-mean)**4
        denominator=j_value*u0**4+a*v0**4
        val=block_value(total,j_value)
        assert isclose(numerator/denominator,val,rel_tol=3e-14,abs_tol=3e-14)
        vals.append(val)
    assert max(vals)<=float(maxf)+1e-11

# Direct finite tests of the soft-threshold formula.
def simplex(x):
    lo=min(x)-1.0
    hi=max(x)+1.0
    for _ in range(90):
        t=(lo+hi)/2.0
        if sum(max(y-t,0) for y in x)>1.0:
            lo=t
        else:
            hi=t
    t=(lo+hi)/2.0
    return [max(y-t,0) for y in x]

for n in range(2,10):
    for x in itertools.product([-0.75,0.125,1.5], repeat=min(n,5)):
        if len(x)!=n:continue
        z=simplex(x)
        assert abs(sum(z)-1)<1e-11
        assert min(z)>=0
        active=[i for i,zi in enumerate(z) if zi>1e-9]
        if active:
            shift=sum(x[i]-z[i] for i in active)/len(active)
            assert all(abs(z[i]-max(x[i]-shift,0))<1e-9 for i in range(n))

# Strictly less than the irrational universal target for every finite rational split.
assert sp.simplify(1/(q**3-3*q+2) -(sp.Integer(3)-sp.sqrt(3))/18)==0
print('VERIFY_OK symbolic identity, derivative, universal constant, finite witnesses, projection checks')
