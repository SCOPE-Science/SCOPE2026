"""Exact symbolic and rational checks for the negative-parameter ETM-3D fold window.

Requires Python 3 and SymPy. All sign and root-count statements are exact.
"""
import sympy as S

rho, x, u = S.symbols('rho x u', real=True)
Q = (8*x**4+8*rho*x**3+(-6*rho**2+10*rho+35)*x**2
     +(-4*rho**3+5*rho**2+15*rho)*x
     +2*rho**4-5*rho**3-20*rho**2+25*rho+50)
H = (594*rho**8-2076*rho**7-5948*rho**6+20050*rho**5
     +25505*rho**4-66100*rho**3-63325*rho**2+77500*rho+75000)
D = 2*x*x+rho*x+5-rho*rho
Y = 5*x/D
Z = x*(rho+x)/D
F = S.Matrix([-2*x-rho*Y+Y*Z, x-Y+rho*Z-2*x*Z, rho*Y-5*Z+x*Y])
assert S.factor(F[0]+x*Q/D**2)==0
assert S.factor(F[1])==0 and S.factor(F[2])==0
assert S.factor(S.discriminant(Q,x)-12000*H)==0
assert S.factor(Q.subs(x,0)-(rho**2-5)*(2*rho**2-5*rho-10))==0
assert S.factor(S.diff(Q,x,2)-(96*(x+rho/4)**2+70+20*rho-18*rho**2))==0
assert S.factor(S.diff(Q,rho)-(8*x**3+(-12*rho+10)*x**2+(-12*rho**2+10*rho+15)*x+8*rho**3-15*rho**2-40*rho+25))==0

# The critical negative fold is a uniquely isolated zero of H.
lo, hi=S.Rational(-164,125),S.Rational(-327,250)
assert lo == S.Rational(-1312,1000) and hi==S.Rational(-1308,1000)
root_boxes=[(-2011935,-2011934),(-1308661,-1308660),(2188758,2188759),(3355161,3355162)]
assert S.Poly(H,rho).count_roots(-S.oo,S.oo)==4
for a,b in root_boxes:
    assert S.Poly(H,rho).count_roots(S.Rational(a,10**6),S.Rational(b,10**6))==1
assert S.Poly(H,rho).count_roots(S.Rational(-131,100),S.Rational(-13,10))==1
rho_tc=(5-S.sqrt(105))/4
rho_box_left=S.Rational(-1308661,10**6)
rho_box_right=S.Rational(-1308660,10**6)
assert S.simplify(rho_tc-S.Rational(-1312,1000))>0
assert S.simplify(S.Rational(-131,100)-rho_tc)>0
assert S.Rational(-131,100)<rho_box_left<rho_box_right<S.Rational(-13,10)

# Parameter and state rectangles: strict convexity, monotone rho-dependence,
# positivity of the outer endpoints, and a positive transverse denominator.
assert 70+20*lo-18*lo**2>12
b_lower=-12*lo**2+10*lo+15
c_lower=8*lo**3-15*lo**2-40*hi+25
assert b_lower<0 and c_lower+b_lower/4>28
assert Q.subs({x:S.Rational(1,4),rho:lo})>0
assert 5-lo**2+lo/4>S.Rational(29,10)
assert (S.Rational(1,4)*(-lo))/S.Rational(29,10)<S.Rational(1,8)
# A rational test point between the fold and the origin crossing.
r_test=S.Rational(-131,100)
assert S.Poly(Q.subs(rho,r_test),x).count_roots(-S.oo,S.oo)==2
for a,b in [(34,35),(173,174)]:
    qa=Q.subs({rho:r_test,x:S.Rational(a,1000)})
    qb=Q.subs({rho:r_test,x:S.Rational(b,1000)})
    assert qa*qb<0
assert Q.subs({rho:S.Rational(-13,10),x:0})>0
assert S.Poly(Q.subs(rho,S.Rational(-13,10)),x).count_roots(-S.oo,S.oo)==0

# Weighted-energy certificate has a unique interior optimizer for rho<0.
phi=1/(8*u)-rho/4+rho**2*(3*u/40+S.Rational(1,5)+1/(20*(2-u)))
num_e=S.factor(S.together(phi-1).as_numer_denom()[0])
num_d=S.factor(S.together(S.diff(phi,u)).as_numer_denom()[0])
assert S.factor(S.resultant(num_e,num_d,u)+14400*rho**4*H)==0
assert phi.subs({rho:S.Rational(-13,10),u:S.Rational(4,5)})==S.Rational(7433,7500)
# The nonlinear term is orthogonal to every W=diag(u,1,2-u).
y,z=S.symbols('y z',real=True)
N=S.Matrix([y*z,-2*x*z,x*y]); vec=S.Matrix([x,y,z])
W=S.diag(u,1,2-u)
assert S.expand((vec.T*W*N)[0])==0
A=S.Matrix([[-2,-rho,0],[1,-1,rho],[0,rho,-5]])
L=S.factor((W*A+A.T*W)/2)
# For the key tridiagonal form, strict negativity is equivalent to phi<1.
assert S.factor(S.det(L) +10*u*(2-u)*(1-phi))==0

# Equilibrium Jacobian and the determinant sign distinguishing the two roots.
J=S.Matrix([[-2,-rho+Z,Y],[1-2*Z,-1,rho-2*x],[Y,rho+x,-5]])
assert S.factor((J.det()+x*S.diff(Q,x)/D)/Q - (rho**2+rho*x+6*x*x-5)/D**2)==0
assert S.factor(S.trace(J)+8)==0
# Explicit uniformly conservative Routh-Hurwitz bounds for all roots
# with rho in [-1.312,-1.308], x in [0,1/4].
y_bound=S.Rational(25,58)
z_bound=S.Rational(1,8)
assert y_bound<S.Rational(1,2)
a2_lower=17-(-lo)*(1+2*z_bound)-S.Rational(1,4)-(-lo+S.Rational(1,2))*(-lo)
assert a2_lower>12
px_upper=(S.Rational(1,2)+24*(-lo)/16
          +2*(6*lo**2+10*(-lo)+35)/4
          +4*(-lo)**3+5*lo**2+15*(-lo))
assert px_upper<70
assert S.Rational(1,4)*70/(S.Rational(29,10))<7
# The origin's linearization is Hurwitz throughout the bistable window.
assert 17+lo-lo**2>13
assert 126+3*lo-6*lo**2>100
assert S.simplify(2*rho_tc**2-5*rho_tc-10)==0

print('PASS: symbolic identities, exact Sturm isolation, equilibrium counts,')
print('      convexity and monotonicity bounds, quadratic energy cancellation,')
print('      fold and transcritical thresholds, and Routh-Hurwitz certificates.')
print('critical fold rho in:',rho_box_left,rho_box_right)
print('origin crossing:',S.N(rho_tc,18))
print('bistability width in:',S.N(rho_box_left-rho_tc,15),S.N(rho_box_right-rho_tc,15))
