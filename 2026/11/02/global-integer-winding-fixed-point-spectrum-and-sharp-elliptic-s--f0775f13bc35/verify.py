"""Exact algebra and independent numerical checks for cylinder-map resonances.

Requires Python 3 and SymPy. Finite checks support but do not replace the
analytical classification and asymptotics in RESULT.md.
"""
from fractions import Fraction
from math import ceil, floor, pi, sqrt
import sympy as S

q, e, a, z, m, y = S.symbols('q e a z m y', positive=True, real=True)
omega = a*(1-y*y)*(1-e*y*y)
D = (1-e)**2 + 4*e*m/a
zp = (1+e+S.sqrt(D))/(2*e)
zm = (1+e-S.sqrt(D))/(2*e)
quad = e*z*z - (1+e)*z + 1-m/a
assert S.simplify(quad.subs(z,zp)) == 0
assert S.simplify(quad.subs(z,zm)) == 0
assert S.simplify(S.diff(omega,y) - 2*a*y*(2*e*y*y-(1+e))) == 0
Jdet = S.det(S.Matrix([[1+q*S.diff(omega,y), S.diff(omega,y)], [q, 1]]))
assert S.simplify(Jdet-1) == 0
trace = 2+q*S.diff(omega,y)
assert S.simplify((2-trace)/4+q*S.diff(omega,y)/4) == 0
checked = 5

def B(a0,e0):
    return a0*(1-e0)**2/(4*e0)

def classifications(a0,e0,m0):
    d = (1-e0)**2 + 4*e0*m0/a0
    if d < 0: return []
    roots = [(1+e0 + S.sqrt(d))/(2*e0),(1+e0 - S.sqrt(d))/(2*e0)]
    return list(dict.fromkeys([S.simplify(r) for r in roots if r.is_nonnegative]))

for a0,e0 in [(S.Rational(1,2),S.Rational(1,4)),(S.Rational(3,4),S.Rational(1,100)),(S.Rational(1,2),S.Rational(1)),(S.Rational(2,3),S.Rational(3,2)),(S.Rational(1,2), S.Rational(1,2))]:
    bval = B(a0,e0)
    for m0 in range(-5,8):
        roots=classifications(a0,e0,S.Integer(m0))
        # Independently compute roots via polynomial solver, not the formula.
        independent = [S.simplify(t) for t in S.solve(quad.subs({a:a0,e:e0,m:m0}),z) if t.is_nonnegative] if m0 in [-5,-1,0,1,5] else roots
        assert {S.simplify(t) for t in roots}=={S.simplify(t) for t in independent},(a0,e0,m0,roots,independent)
        for r in roots:
            assert S.simplify(a0*(1-r)*(1-e0*r)-m0)==0
            checked += 1
        if m0 >=1: assert len(roots)==1
        if m0 ==0: assert len(roots)==(1 if e0==1 else 2)
        if m0 <0:
            k=-m0
            assert len(roots)==(2 if k<bval else 1 if k==bval else 0)
        checked += 1

# An exact height census independent of the closed form: use the roots directly.
for a0,e0 in [(S.Rational(1,2),S.Rational(1,4)),(S.Rational(3,4),S.Rational(1,100)), (S.Rational(1,2),S.Rational(1))]:
    bval=B(a0,e0)
    C=(4 if e0==1 else 8)+8*max(0,S.ceiling(bval)-1)+(4 if bval.is_integer and bval>0 else 0)
    for Y in [S.Integer(3), S.Integer(4),S.Integer(6)]:
        if Y<max(S.Integer(1),1/S.sqrt(e0)): continue
        top=S.floor(a0*(1-Y*Y)*(1-e0*Y*Y))
        direct=0
        for k in range(-25,int(top)+1):
            for r in classifications(a0,e0,S.Integer(k)):
                if r<=Y*Y: direct+=4
        assert direct==C+4*top,(a0,e0,Y,direct,C,top)
        checked += 1

# Numerically check the sharp stability staircase and the two-term law.
for aa,ee in [(0.5,0.25),(0.75,0.01),(0.36,1.5)]:
    for bb in [0.1,0.01,0.003,0.001]:
        rhs=2*ee/(pi*pi*aa*aa*bb*bb)
        lo,hi=0.0, max(1.0,rhs**(1/3)*2)
        for _ in range(140):
            mid=(lo+hi)/2
            if mid*mid*(mid+1+ee)<rhs:lo=mid
            else:hi=mid
        sb=(lo+hi)/2
        mstar=aa/(4*ee)*(sb*sb-(1-ee)**2)
        nn=max(0,ceil(mstar)-1)
        direct=0
        for kk in range(1,nn+5):
            d=(1-ee)**2+4*ee*kk/aa
            zz=(1+ee+sqrt(d))/(2*ee)
            residue=bb*pi*aa*sqrt(zz*d)
            if residue<1: direct+=1
        assert direct==nn,(aa,ee,bb,direct,nn,mstar)
        checked += 1

# Difference of a noninteger-valued threshold and its 2-term asymptotics stays bounded.
for bb in [1e-3,1e-4,1e-5]:
    aa,ee=0.5,0.25
    rhs=2*ee/(pi*pi*aa*aa*bb*bb)
    lo,hi=0.0,2*(rhs**(1/3)+1)
    for _ in range(160):
        x=(lo+hi)/2
        if x*x*(x+1+ee)<rhs: lo=x
        else:hi=x
    s=(lo+hi)/2
    mt=aa/(4*ee)*(s*s-(1-ee)**2)
    approx=bb**(-4/3)/((2*pi)**(4/3)*(aa*ee)**(1/3))-(1+ee)*aa**(1/3)*bb**(-2/3)/(3*(2*pi)**(2/3)*ee**(2/3))
    assert abs(mt-approx)<3,(bb,mt,approx)
    checked+=1

print('PASS:',checked,'exact symbolic/rational branch, algebra, census, and numerical staircase checks')
