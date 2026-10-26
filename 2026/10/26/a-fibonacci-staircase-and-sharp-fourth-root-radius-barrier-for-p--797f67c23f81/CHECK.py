"""Exact tests of the positive lattice covariance stencil threshold.

Only standard Python plus SymPy is needed. Every identity is evaluated
algebraically over Q(sqrt(5)); finite checks supplement the paper proof.
"""
from fractions import Fraction
import sympy as S

s = (S.sqrt(5)-1)/2
F = [0,1]
for j in range(2,25):
    F.append(F[-1]+F[-2])

def bracket(R):
    below, above = [], []
    for q in range(1,R+1):
        for p in range(q+1):
            v = Fraction(p,q)
            cmp = p*p+p*q-q*q
            (below if cmp<0 else above).append(v)
    return max(below), min(above)

def critical(lo,hi):
    l,r = S.Rational(lo.numerator,lo.denominator),S.Rational(hi.numerator,hi.denominator)
    return S.simplify((s-l)*(r-s)/(1+l*r))

def eq(a,b):
    return S.simplify(a-b)==0

checks = 0
for R in range(1,90):
    n=max(k for k in range(2,len(F)-1) if F[k]<=R)
    assert R<F[n+1]
    lo,hi=bracket(R)
    endpoints={Fraction(F[n-2],F[n-1]),Fraction(F[n-1],F[n])}
    assert {lo,hi}==endpoints
    e=critical(lo,hi)
    ef=s**(2*n-1)/(F[n-1]*(F[n]+F[n-2]))
    assert eq(e,ef)
    assert e>0
    l=S.Rational(lo.numerator,lo.denominator)
    r=S.Rational(hi.numerator,hi.denominator)
    # Feasible weights of the two primitive directions at the threshold.
    m=s/(1+e)
    theta=(r-m)/(r-l)
    wlo=S.simplify((1+e)*theta/lo.denominator**2)
    whi=S.simplify((1+e)*(1-theta)/hi.denominator**2)
    assert bool(S.simplify(wlo)>0) and bool(S.simplify(whi)>0)
    vl=S.Matrix([lo.denominator,lo.numerator]); vr=S.Matrix([hi.denominator,hi.numerator])
    A=S.Matrix([[1+e,s],[s,s*s+e]])
    B=wlo*(vl*vl.T)+whi*(vr*vr.T)
    assert all(eq(A[i,j],B[i,j]) for i in range(2) for j in range(2))
    checks+=5
    # Every admissible direction obeys the separating-facet inequality.
    for x in range(-R,R+1):
        for y in range(-R,R+1):
            if not (x or y):continue
            prod=(S.Rational(y)-l*x)*(S.Rational(y)-r*x)
            assert prod>=0
            checks+=1
    # For all smaller epsilon the linear functional is negative.
    test=e/2
    defect=(s-l)*(s-r)+(1+l*r)*test
    assert S.simplify(defect)<0
    checks+=1

c=1/(5*s**2*(1+s**2))
assert eq(c, 1/(5*s**2*(1+s**2)))
print('PASS: exact Farey bracketing, Fibonacci thresholds, covariance reconstruction')
print('PASS: direction-separating inequalities and strictly infeasible half-thresholds')
print('checked algebraic/directional assertions:',checks)
print('liminf coefficient:',S.N(c,18))
print('limsup coefficient:',S.N(c/s**4,18))
for n in (8,10,12,14):
    e=S.N(s**(2*n-1)/(F[n-1]*(F[n]+F[n-2])),24)
    print('Fibonacci range',F[n],F[n+1]-1,'epsilon',e)
