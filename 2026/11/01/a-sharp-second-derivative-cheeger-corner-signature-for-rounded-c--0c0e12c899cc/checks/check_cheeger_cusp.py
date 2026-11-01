#!/usr/bin/env python3
"""Independent exact algebra and high-precision tests for a Cheeger profile theorem."""
import sympy as S
import mpmath as mp

p,tau,delta,e = S.symbols('p tau delta e', positive=True, real=True)
pi = S.pi
A=pi*tau**2
P=p
B0=P+2*pi*tau
alpha=-2*pi*tau/B0
beta0=S.simplify((-pi-2*pi*alpha)/B0)
beta=S.simplify(beta0+delta*alpha**2/B0)
s=alpha*e+beta*e**2
expr=S.expand(A-pi*(tau+e)**2-(P+2*pi*(tau+e))*s+delta*s*s)
assert S.simplify(expr.coeff(e,0))==0
assert S.simplify(expr.coeff(e,1))==0
assert S.simplify(expr.coeff(e,2))==0
rp=(A+P*(tau+e)+pi*(tau+e)**2)/(P+2*pi*(tau+e))
assert S.simplify((tau+e+alpha*e+beta0*e**2-S.series(rp,e,0,3).removeO()).coeff(e,2))==0
jump=S.simplify(2*delta*alpha**2/(B0*tau**2))
assert S.simplify(jump-8*pi*pi*delta/B0**3)==0
# Re-derive the curvature jump directly from the implicit equation.
r=S.symbols('r')
t=S.symbols('t')
F=(pi*tau**2 - (P)*(r-t)+ (delta+pi)*(r-t)**2 - pi*r**2)
F_r=S.diff(F,r); F_t=S.diff(F,t)
rprime=-F_t/F_r
rsecond=S.simplify(-(S.diff(F,t,2)+2*S.diff(F,t,r)*rprime+S.diff(F,r,2)*rprime**2)/F_r)
rsecond_minus=S.simplify(rsecond.subs({r:tau,t:tau}))
rplus=(pi*tau**2+P*t+pi*t**2)/(P+2*pi*t)
rsecond_plus=S.simplify(S.diff(rplus,t,2).subs(t,tau))
assert S.simplify(rsecond_minus-rsecond_plus-8*pi*pi*tau**2*delta/B0**3)==0
print('SYMBOLIC_IMPLICIT_EQUATION_AND_ONE_SIDED_HESSIAN_PASSED')

# Exact polygon inner-parallel area formula via elementary geometry.
# For a rectangle of side lengths U,V, C=4 and |K_-s|=(U-2s)(V-2s).
U,V,q=S.symbols('U V q',positive=True)
assert S.simplify((U-2*q)*(V-2*q)-(U*V-2*(U+V)*q+4*q**2))==0
# For an equilateral triangle of side L, inradius sqrt(3)L/6.
L=S.symbols('L',positive=True)
Ar=S.sqrt(3)*L**2/4; Cr=3*S.sqrt(3); Pr=3*L
r_in=S.sqrt(3)*L/6
assert S.simplify(Ar*(1-q/r_in)**2-(Ar-Pr*q+Cr*q*q))==0
print('INDEPENDENT_RECTANGLE_AND_TRIANGLE_INNER_PARALLEL_AREA_PASSED')

mp.mp.dps=80
for a,per,c,n in [(mp.mpf(4),mp.mpf(8),mp.mpf(4),4),
                 (mp.sqrt(3),mp.mpf(6),3*mp.sqrt(3),3),
                 (mp.mpf(12),mp.mpf(16),mp.mpf(4),4)]:
    t0=mp.sqrt(a/mp.pi); bb=per+2*mp.pi*t0; d=c-mp.pi
    assert d>0
    htail=lambda x:(per+2*mp.pi*x)/(a+per*x+mp.pi*x*x)
    def hleft(x):
        B=per+2*mp.pi*x; T=a-mp.pi*x*x
        # numerically stable small root of T-B*s+d*s*s=0
        z=2*T/(B+mp.sqrt(B*B-4*d*T))
        return 1/(x+z)
    target=8*mp.pi**2*d/bb**3
    for step in ['1e-3','1e-4','1e-5']:
        h=mp.mpf(step)
        # compare asymptotic second coefficient using exact right analytic extension
        est=2*(htail(t0-h)-hleft(t0-h))/h**2
        assert abs(est-target)<mp.mpf('0.08')*target if h==mp.mpf('1e-3') else abs(est-target)<mp.mpf('0.015')*target
    # direct check of quadratic formula against exact r equation
    for x in [t0-mp.mpf('0.01'),t0-mp.mpf('0.001')]:
        rr=1/hleft(x); zz=rr-x
        assert abs(a-per*zz+c*zz**2-mp.pi*rr**2)<mp.mpf('1e-70')
    assert abs(htail(t0)-1/t0)<mp.mpf('1e-70')
print('NUMERICAL_TRANSITION_AND_EXACT_CHEEGER_ROOTS_PASSED')

# Jensen's angular bound: each exterior half-angle beta_i>0, sum pi.
# A non-regular equiangular rectangle attains C=n*tan(pi/n).
assert S.simplify(4*S.tan(S.pi/4)-4)==0
assert S.simplify(3*S.tan(S.pi/3)-3*S.sqrt(3))==0
print('SHARP_ANGULAR_BOUND_ENDPOINTS_PASSED')
print('ALL_CHECKS_PASSED')
