"""Exact identity checks for two-coordinate randomized SOR comparison.

Requires Python 3 and SymPy. This script tests polynomial identities over
rationals and verifies representative exact cases; general conclusions follow
from the accompanying algebraic proof.
"""
from fractions import Fraction
import sympy as sp

c, omega = sp.symbols('c omega', real=True)
C=sp.Matrix([[1,c],[c,1]])
U=sp.Matrix([[1-omega,-omega*c],[0,1]])
V=sp.Matrix([[1,0],[-omega*c,1-omega]])
def pullback(M):
    return M.T*C*M
Kp=(pullback(V*U)+pullback(U*V))/2
Kr=(pullback(U*U)+pullback(V*V)+pullback(U*V)+pullback(V*U))/4
Diff=sp.simplify(Kr-Kp)
assert sp.simplify(Diff[0,0]-Diff[1,1])==0
assert sp.simplify(Diff[0,1]-Diff[1,0])==0
for sign in (1,-1):
    e=sp.Matrix([1,sign])
    normalized=sp.factor((e.T*Diff*e)[0]/(e.T*C*e)[0])
    expected=omega**2*(1-c**2)*(2-omega)*(2-omega*(1+sign*c))/4
    assert sp.cancel(normalized-expected)==0
for j,M in enumerate((U,V)):
    col=sp.Matrix([[1,c]]) if j==0 else sp.Matrix([[c,1]])
    assert sp.simplify(M.T*C*M-C+omega*(2-omega)*col.T*col)==sp.zeros(2)
N=0
for den in (3,5,7,11):
    for k in range(0,den):
        cc=sp.Rational(k,den)
        if cc>=1: continue
        for j in range(1,2*den):
            w=sp.Rational(j,den)
            if w>=2: continue
            d=Diff.subs({c:cc,omega:w})
            evp=sp.factor(d[0,0]+d[0,1]); evm=sp.factor(d[0,0]-d[0,1])
            assert evm>0
            if w < 2/(1+cc): assert evp>0
            if w == 2/(1+cc): assert evp==0
            if w > 2/(1+cc): assert evp<0
            N+=1
cc=sp.Rational(1,2); w=sp.Rational(19,10)
ratios={}
for label,K in [('permuted',Kp),('independent',Kr)]:
    ratios[label]=[]
    for sgn in (1,-1):
        e=sp.Matrix([1,sgn]);ratios[label].append(sp.factor(((e.T*K*e)[0]/(e.T*C*e)[0]).subs({c:cc,omega:w})))
assert ratios['permuted']==[sp.Rational(137143,160000),sp.Rational(123501,160000)]
assert ratios['independent']==[sp.Rational(2047,2560),sp.Rational(53949,64000)]
assert max(ratios['permuted'])>max(ratios['independent'])
print('VERIFY_OK',N,'exact parameter instances; symbolic identities and worst-case counterexample')
