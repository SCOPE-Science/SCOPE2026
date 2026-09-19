import sympy as sp

# Exact symbolic check of the coefficient cancellations in the endpoint expansion.
x = sp.symbols('x', real=True)
r3 = sp.sqrt(3)
A1 = sp.Rational(1,2)
D = sp.Rational(3,8)
K0 = sp.Rational(39,2) + 45*r3/4

# If G=1-A1*e+B*e^2+C*e^3+O(e^4) and
# P=1-D*e^2+E*e^3+F*e^4+O(e^5), then the coefficients of
# r=1-P as a series in y=1-G are obtained by series reversion.
def boundary_coeffs(B,C,E,F):
    b = -B
    c = -C
    f = -E
    g = -F
    q2 = D/A1**2
    q3 = sp.expand((f-q2*2*A1*b)/A1**3)
    q4 = sp.expand((g-q2*(b*b+2*A1*c)-q3*(3*A1**2*b))/A1**4)
    return sp.factor(q3), sp.factor(q4)

# Lower-half piece: theta=N+x, fixed 0<=x<1/2.
BL = x**2-sp.Rational(3,8)-r3/4
CL = -2*x**3+(sp.Rational(1,2)-r3/3)*x**2+(1+2*r3/3)*x+sp.Rational(31,32)+9*r3/16
EL = sp.Rational(3,2)*x**2-sp.Rational(1,4)-3*r3/16
FL = -4*x**3-7*r3*x**2/8+(sp.Rational(3,2)+r3)*x+sp.Rational(165,128)+3*r3/4
q3L,q4L=boundary_coeffs(BL,CL,EL,FL)

# Upper-half piece: theta=N+x, fixed 1/2<x<1.
BR = -x**2+2*x-sp.Rational(7,8)-r3/4
CR = 2*x**3+(-sp.Rational(5,2)+r3/3)*x**2+35*r3/48+sp.Rational(55,32)
ER = -sp.Rational(3,2)*x**2+3*x-1-3*r3/16
FR = 4*x**3+(-sp.Rational(9,2)+7*r3/8)*x**2+(-sp.Rational(3,2)-3*r3/4)*x+sp.Rational(373,128)+19*r3/16
q3R,q4R=boundary_coeffs(BR,CR,ER,FR)

A = (5+3*r3)/2
print('q3 lower:', sp.simplify(q3L))
print('q3 upper:', sp.simplify(q3R))
print('q3 target checks:', sp.simplify(q3L+A), sp.simplify(q3R+A))
print('q4 lower target check:', sp.simplify(q4L-(K0+16*x**3-24*x**4)))
u=sp.symbols('u', real=True)
q4R_u=sp.expand(q4R.subs(x,1-u))
print('q4 upper target check:', sp.simplify(q4R_u-(K0+16*u**3-24*u**4)))
print('K0:', sp.simplify(K0))
print('K(1/2)-K0:', sp.simplify((K0+16*sp.Rational(1,2)**3-24*sp.Rational(1,2)**4)-K0))

# Direct high-precision evaluation of equations (16)--(19).
import mpmath as mp
mp.mp.dps = 60

def exact_GP(theta):
    th=mp.mpf(theta); s=1/th; N=int(mp.floor(th))
    L=1/(2*mp.mpf(N)); R=1/(2*mp.mpf(N+1))
    ell=L if s>=L+R else R
    delta=s-2*ell
    p=1-2*N*(N+1)*abs(delta)
    m=ell+N*(N+1)*delta*abs(delta)
    q=ell*(2*m-ell)+mp.mpf(2)/3*N*(N+1)*abs(delta)**3
    c=(ell**2-s*ell-ell*p*delta)/2
    alpha=(1+mp.sqrt(1+2*th**2*c))/2
    t=1/(th+alpha); a=alpha*t; z=th*t
    G=1-2*a*a-z*z*m
    P=1-2*a**3-mp.mpf(3)/2*z**3*q
    return G,P

A_mp=(5+3*mp.sqrt(3))/2
K0_mp=mp.mpf(39)/2+45*mp.sqrt(3)/4
for phase in (mp.mpf('0'),mp.mpf('0.25'),mp.mpf('0.5'),mp.mpf('0.75')):
    N=10000
    G,P=exact_GP(mp.mpf(N)+phase)
    y=1-G; r=1-P
    R4=(r-mp.mpf(3)/2*y*y+A_mp*y**3)/y**4
    u=min(phase,1-phase)
    target=K0_mp+16*u**3-24*u**4
    print('phase', phase, 'R4', mp.nstr(R4,15), 'target', mp.nstr(target,15))
