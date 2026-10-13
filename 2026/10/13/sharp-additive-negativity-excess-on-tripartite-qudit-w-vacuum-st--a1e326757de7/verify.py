#!/usr/bin/env python3
"""Direct matrix tests for trace-norm negativity on balanced W-vacuum states.
Dependencies: Python 3, SymPy. Not a substitute for the analytic dimension-uniform proof.
"""
from fractions import Fraction
from math import sqrt
import sympy as sp

def state(D,w,a,b):
    # Labels: |A B C>; all coefficients are exact.
    entries={(0,0,0):w}
    for j in range(1,D):
        entries[(j,0,j)]=a
        entries[(j,j,0)]=b
    assert sp.simplify(sum(c*c for c in entries.values())-1)==0
    return entries

def reduction_pt(state,D,keep):
    # keep=1 is AB; keep=2 is AC.
    M=sp.zeros(D*D)
    for (A,B,C),amp in state.items():
        x=B if keep==1 else C
        z=C if keep==1 else B
        for (Ap,Bp,Cp),amp2 in state.items():
            xp=Bp if keep==1 else Cp
            zp=Cp if keep==1 else Bp
            if z==zp:
                M[Ap*D+x,A*D+xp]+=amp*amp2 # transpose A
    return M

def negativity(M):
    vals=M.eigenvals()
    return sp.simplify(sum(mult*(abs(v)-v) for v,mult in vals.items()))

def formulas(D,w,a,b):
    r=D-1
    s=a*a+b*b
    nab=sp.simplify(r*(sp.sqrt(a**4+4*b*b*w*w)-a*a)+r*(r-1)*b*b)
    nac=sp.simplify(r*(sp.sqrt(b**4+4*a*a*w*w)-b*b)+r*(r-1)*a*a)
    na=sp.simplify(2*r*w*sp.sqrt(s)+r*(r-1)*s)
    return nab,nac,na

cases=[(3,sp.Rational(3,5),sp.Rational(2,5),sp.Rational(2,5)),
       (4,sp.Rational(1,2),sp.Rational(3,10),sp.Rational(2,5)),
       (5,sp.Rational(1,3),sp.Rational(1,3),sp.Rational(1,3)),
       (2,sp.Rational(3,5),sp.Rational(4,5),sp.Rational(0))]
for D,w,a,b in cases:
    st=state(D,w,a,b)
    nab=negativity(reduction_pt(st,D,1))
    nac=negativity(reduction_pt(st,D,2))
    expected=formulas(D,w,a,b)
    assert sp.simplify(nab-expected[0])==0, (D,nab,expected[0])
    assert sp.simplify(nac-expected[1])==0, (D,nac,expected[1])
    r=D-1;s=a*a+b*b
    assert sp.simplify(w*w+r*s-1)==0
    print('D',D,'pair_N',str(nab),str(nac),'global_N',str(expected[2]))

r=sp.symbols('r',integer=True,positive=True)
t,k=sp.symbols('t k',positive=True,real=True)
f=sp.sqrt(t*t+4*(1-t)*k)
assert sp.simplify(sp.diff(f,t,2) - (4*k*(1-k))/f**3)==0
assert sp.simplify((t+2*(1-t)*sp.sqrt(k))**2 - f**2-4*t*(1-t)*sp.sqrt(k)*(1-sp.sqrt(k)))==0
assert sp.simplify((sp.Rational(16,1)*sp.sqrt(10)-24*sp.sqrt(2)-16)/25 -(2*formulas(3,sp.Rational(3,5),sp.Rational(2,5),sp.Rational(2,5))[0]-formulas(3,sp.Rational(3,5),sp.Rational(2,5),sp.Rational(2,5))[2]))==0

def F(z): return sqrt(1+8*z)-1-2*sqrt(z)
def Fp(z): return 4/sqrt(1+8*z)-1/sqrt(z)
def Fpp(z): return -16/(1+8*z)**1.5 + 1/(2*z**1.5)
for rr in (1,2,3,10,100,10000):
    def H(z):return (rr+z)*Fp(z)-F(z)
    lo,hi=1.,max(4.,rr*2.)
    while H(hi)>0: hi*=2
    for _ in range(100):
        mi=(lo+hi)/2
        if H(mi)>0:lo=mi
        else:hi=mi
    opt=(lo+hi)/2
    M=rr/(rr+opt)*F(opt)
    assert opt>1 and M>0 and Fpp(opt)<0
    assert M<=((2**.5)-1)*sqrt(rr)+1.e-10
    print('r',rr,'k_opt',round(opt,7),'M',round(M,7),'scaled',round(M/sqrt(rr),7))
print('VERIFY_OK exact_partial_transposes=4 concavity_identity=passed scale_envelopes=6')
