"""Symbolic replay of the boundary-triggered reset first-passage theorem.

Requires Python 3 and SymPy. This is a finite exact algebraic verification;
the analytic diffusion and renewal arguments are in RESULT.md.
"""
import sympy as s

x, L, D, tau, v = s.symbols('x L D tau v', positive=True)
q = x/L
u = x*(L-x)/(2*D)
h = x*(L**2-x**2)/(6*D*L)
u2 = x*(L-x)*(L**2 + L*x - x**2)/(12*D**2)
mR = x*(2*L-x)/(2*D)
mR2 = x*(2*L-x)*(4*L**2 + 2*L*x - x**2)/(12*D**2)
for value, source in [(u, -1), (h, -q), (u2, -2*u), (mR, -1), (mR2, -2*mR)]:
    assert s.cancel(D*s.diff(value,x,2)-source)==0
for value in [u,h,u2,mR,mR2]:
    assert value.subs(x,0)==0
for value in [u,h,u2]:
    assert value.subs(x,L)==0
for value in [mR,mR2]:
    assert s.cancel(s.diff(value,x).subs(x,L))==0
mS = s.factor((u+q*tau)/(1-q))
mS2 = s.factor((u2+2*h*(tau+mS)+q*(tau**2+v+2*tau*mS))/(1-q))
tau0 = (L-x)**2/(2*D)
assert s.cancel((mS-mR).subs(tau,tau0))==0
variance_gap = s.factor((mS2-mS**2-mR2+mR**2).subs(tau,tau0))
target_gap = x/(L-x)*(v-s.Rational(2,3)*tau0**2)
assert s.cancel(variance_gap-target_gap)==0

# Independent calculation: expansion of Laplace transforms at zero frequency.
z = s.symbols('z')  # z=s_Laplace/D
sinhc = lambda t: t+t**3*z/6+t**5*z*z/120
A = s.series(sinhc(L-x)/sinhc(L),z,0,3).removeO()
B = s.series(sinhc(x)/sinhc(L),z,0,3).removeO()
phi = 1-D*tau*z+D**2*(tau**2+v)*z*z/2
F = s.series(A/(1-B*phi),z,0,3).removeO()
H = s.series((1+(L-x)**2*z/2+(L-x)**4*z*z/24)/
             (1+L**2*z/2+L**4*z*z/24),z,0,3).removeO()
assert s.cancel(F.coeff(z,1)+D*mS)==0
assert s.cancel(F.coeff(z,2)-D**2*mS2/2)==0
assert s.cancel(H.coeff(z,1)+D*mR)==0
assert s.cancel(H.coeff(z,2)-D**2*mR2/2)==0

# Distinct rational geometries and waiting-law coefficients of variation.
for length,position,diffusion in [(s.Rational(2),s.Rational(1,2),s.Rational(3)),
                                  (s.Rational(5,3),s.Rational(1,7),s.Rational(2,5)),
                                  (s.Rational(7),s.Rational(11,4),s.Rational(5,2))]:
    meanwait = tau0.subs({L:length,x:position,D:diffusion})
    for cv2 in [s.Rational(0),s.Rational(2,3),s.Rational(1),s.Rational(4)]:
        args={L:length,x:position,D:diffusion,v:cv2*meanwait**2}
        actual=s.factor(variance_gap.subs(args))
        expected=s.factor((position/(length-position))*meanwait**2*(cv2-s.Rational(2,3)))
        assert actual==expected
print('PASS: boundary-value PDEs and boundary data')
print('PASS: geometric renewal moments and mean-neutral variance gap')
print('PASS: independent first-passage Laplace-transform moment expansion')
print('PASS: 12 exact rational model/holding-variability checks')
