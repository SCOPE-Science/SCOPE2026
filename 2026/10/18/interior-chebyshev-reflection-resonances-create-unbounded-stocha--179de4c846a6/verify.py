"""Exact checks for interior Chebyshev-reflection noise resonance.

Run: python verify.py (requires SymPy). Exhaustive finite experiments are
supporting diagnostics; universal conclusions rely on the accompanying proof.
"""
from itertools import product
import sympy as sp


def main():
    count = 0
    def check(condition, label):
        nonlocal count
        assert bool(condition), label
        count += 1

    t, h, z, x, c = sp.symbols('t h z x c')
    root5 = sp.sqrt(5)
    lam = ((3-root5)/4, (3+root5)/4)
    centers = (-1,1)
    T5 = sp.chebyshevt(5, t)
    check(T5 == 16*t**5 - 20*t**3 + 5*t, 'Chebyshev polynomial')
    R = [T5.subs(t, 1-h*l/25) for l in lam]
    for i in (0,1):
        check(sp.simplify(R[i].subs(h,25)) == -1, 'reflection')
        check(sp.simplify(sp.diff(R[i],h).subs(h,25)) == 0, 'extremum')

    # Verify five-stage recurrence over a generic scalar curvature using z=h*lambda/25.
    prev2=x
    prev1=x-z*(x-c)
    for _ in range(2,6):
        prev2,prev1=prev1,sp.expand(2*prev1-prev2-2*z*(prev1-c))
    check(sp.expand(prev1-(c+T5.subs(t,1-z)*(x-c)))==0,'generic five-stage recurrence')

    check(sp.simplify(sum(lam)/2)==sp.Rational(3,4),'mean curvature')
    xstar=sp.simplify((lam[1]-lam[0])/(lam[0]+lam[1]))
    check(xstar==root5/3,'full-gradient minimizer')
    check(T5.subs(t,sp.Rational(1,4))==sp.Rational(61,64),'deterministic contraction')

    # Enumerate every iid two-sample sequence for finite horizons.
    for n in range(1,12):
        values=[]
        for path in product((0,1), repeat=n):
            state=0
            for i in path:
                state=-state+2*centers[i]
            values.append(state)
        check(sum(values)==0,'finite-horizon mean')
        check(sum(v*v for v in values)==(2**n)*4*n,'finite-horizon second moment')

    a,b=sp.symbols('a b',real=True)
    A,B=1-a,1-b
    m=(a-b)/(2-a-b)
    numerator=sp.expand(((A*(-1-m))**2+(B*(1-m))**2)/2)
    expected=4*A**2*B**2/(A+B)**2
    check(sp.cancel(numerator-expected)==0,'stationary centered noise variance')
    gamma=[]
    for i,l in enumerate(lam):
        derivative=sp.simplify(sp.diff(R[i],h,2).subs(h,25)/2)
        target=(sp.Rational(1,50)+(-1 if i==0 else 1)*root5/125)
        check(sp.simplify(derivative-target)==0,'quadratic curvature of reflection')
        gamma.append(derivative)
    check(sp.simplify(sum(gamma))==sp.Rational(1,25),'sum of quadratic coefficients')
    check(sp.simplify(4/sum(gamma))==100,'stationary variance pole coefficient')

    for step in (sp.Rational(249,10),sp.Rational(2499,100),sp.Rational(2501,100),sp.Rational(251,10)):
        ra,rb=[sp.N(ri.subs(h,step),45) for ri in R]
        aa,bb=1-ra,1-rb
        q=float((ra**2+rb**2)/2)
        var=float(4*aa*aa*bb*bb/((aa+bb)**2*(1-(ra**2+rb**2)/2)))
        check(0<q<1,'mean-square contraction near resonance')
        check(var>0,'positive invariant variance')
        check(abs(float((step-25)**2)*var-100)<0.20,'pole coefficient approach')
    print('PASS:',count,'exact symbolic and finite-enumeration checks')

if __name__=='__main__':
    main()
