"""Exact symbolic checks for the normalized Holling-II predator-prey Hopf period invariant.
Run with: python rm_check.py (requires sympy).
"""
import sympy as S

h,w,x,y,delta=S.symbols('h w x y delta', real=True)
f=x*(1-x)-x*y/(h+x)
g=y*(x/(h+x)-delta)
d=(1-h)/(1+h)
x0=(1-h)/2
y0=(1+h)**2/4
omega2=h*d
subs={x:x0,y:y0,delta:d}
J=S.Matrix([f,g]).jacobian([x,y])
A=S.simplify(J.subs(subs))
assert all(S.simplify(v)==0 for v in (A-S.Matrix([[0,-d],[h,0]])))
assert S.simplify(S.det(A)-omega2)==0
assert S.simplify(f.subs(subs))==0 and S.simplify(g.subs(subs))==0
# d/d(delta) trace at the coexistence equilibrium, evaluated at Hopf.
x_eq=h*delta/(1-delta)
y_eq=(1-x_eq)*(h+x_eq)
trace_at_equilibrium=S.simplify(S.trace(J).subs({x:x_eq,y:y_eq}))
assert S.simplify(S.diff(trace_at_equilibrium,delta).subs(delta,d)+(1-h)*(1+h)/(2*h))==0

Fxx=S.diff(f,x,2).subs(subs); Fxy=S.diff(f,x,y).subs(subs)
Gxx=S.diff(g,x,2).subs(subs); Gxy=S.diff(g,x,y).subs(subs)
Fxxx=S.diff(f,x,3).subs(subs); Fxxy=S.diff(f,x,2,y).subs(subs)
Gxxx=S.diff(g,x,3).subs(subs); Gxxy=S.diff(g,x,2,y).subs(subs)
expected=[-2*d,-4*h/(1+h)**2,-4*h/(1+h),4*h/(1+h)**2,-24*h/(1+h)**2,16*h/(1+h)**3,24*h/(1+h)**2,-16*h/(1+h)**3]
for actual, target in zip([Fxx,Fxy,Gxx,Gxy,Fxxx,Fxxy,Gxxx,Gxxy],expected):
    assert S.simplify(actual-target)==0
q=S.Matrix([1,-S.I*w/d]); qb=S.Matrix([1,S.I*w/d])
p=S.Matrix([[S.Rational(1,2),S.I*d/(2*w)]])

def B(u,v):
    return S.Matrix([Fxx*u[0]*v[0]+Fxy*(u[0]*v[1]+u[1]*v[0]),Gxx*u[0]*v[0]+Gxy*(u[0]*v[1]+u[1]*v[0])])

def C(u,v,z):
    zyx=u[0]*v[0]*z[1]+u[0]*v[1]*z[0]+u[1]*v[0]*z[0]
    return S.Matrix([Fxxx*u[0]*v[0]*z[0]+Fxxy*zyx,Gxxx*u[0]*v[0]*z[0]+Gxxy*zyx])

Ainv=S.Matrix([[0,1/h],[-1/d,0]])
resonant_inverse=S.Matrix([[2*S.I*w,-d],[h,2*S.I*w]])/(-3*d*h)
# This inverse is (2 i w I - A)^(-1) provided w^2=h d.
assert all(S.simplify(v.subs(w**2,omega2))==0 for v in (2*S.I*w*S.eye(2)-A)*resonant_inverse-S.eye(2))
G21=S.cancel((p*(C(q,q,qb)+B(qb,resonant_inverse*B(q,q))-2*B(q,Ainv*B(q,qb))))[0])

def mod_dispersion(value):
    """Reduce a polynomial numerator in w modulo w^2=h*d."""
    num,den=S.fraction(S.together(value))
    result=S.Poly(S.expand(num),w).rem(S.Poly(w*w-omega2,w)).as_expr()/den
    return S.factor(result)

real_G=S.re(G21)
imag_G=S.im(G21)
real_reduced=mod_dispersion(real_G)
imag_reduced=mod_dispersion(imag_G)
expected_real=-4/(1+h)
expected_imag=-4*(h**5-7*h**4+4*h**3-5*h-1)/(3*w*(h-1)*(1+h)**4)
assert S.simplify(real_reduced-expected_real)==0
assert S.simplify(imag_reduced-expected_imag)==0

coef=(1+5*h-4*h**3+7*h**4-h**5)/(6*h*(1-h)**2*(1+h)**3)
assert S.simplify(mod_dispersion(-expected_imag/(8*w)-coef))==0
numerator=S.factor(S.diff(coef,h)*6*h**2*(h-1)**3*(h+1)**4)
polynomial=h**7-15*h**6+23*h**5-25*h**4-17*h**3-h**2+h+1
assert S.simplify(numerator-polynomial)==0
z=S.symbols('z',positive=True)
changed=S.factor((1+z)**7*polynomial.subs(h,z/(1+z)))
assert S.expand(changed)== -32*z**7-104*z**6-128*z**5-48*z**4+28*z**3+26*z**2+8*z+1
min_h=S.nsolve(polynomial,S.Rational(2,5))
assert abs(float(min_h)-0.372462737190824)<1e-12
assert abs(float(coef.subs(h,min_h))-1.2232816447053)<1e-10
assert S.simplify(polynomial.subs(h,0))==1 and S.simplify(polynomial.subs(h,1))==-32
print('PASS: Hopf data, normal-form coefficient, amplitude normalization, and unique minimizer')
print('minimizer h =',S.N(min_h,16))
print('minimum C =',S.N(coef.subs(h,min_h),16))
