"""Reproduce algebraic identities and numerical consistency checks for a two-fidelity GRE design.

Run: python checker.py
Requires Python 3 and SymPy. These finite checks complement, not replace, the proof.
"""
import math
import sympy as sp

checks = 0

def check(ok, msg):
    global checks
    if not ok:
        raise AssertionError(msg)
    checks += 1

x, y, rho = sp.symbols('x y rho', positive=True)
K = sp.Matrix([[x*x, x*y*rho], [x*y*rho, y*y]])
one = sp.Matrix([1, 1])
J = (one.T * K.inv() * one)[0]
formula = (x*x + y*y - 2*x*y*rho)/(x*x*y*y*(1-rho*rho))
check(sp.simplify(J-formula) == 0, 'covariance inverse')
u, v = sp.symbols('u v', positive=True)
Js = (u*u + v*v - 2*u*v*rho)/(1-rho*rho)
Jsplit = (u-v)**2/(1-rho*rho) + 2*u*v/(1+rho)
check(sp.simplify(Js-Jsplit) == 0, 'precision decomposition')
r, w, C, ell = sp.symbols('r w C ell', positive=True)
f = (r+1)**3/(r*(r-1))
root = 2+sp.sqrt(3)
check(sp.simplify(sp.diff(f,r) - (r+1)**2*(r*r-4*r+1)/(r*r*(r-1)**2)) == 0, 'ratio derivative')
check(sp.simplify(f.subs(r,root)-6*sp.sqrt(3)) == 0, 'optimal constant')
check(sp.simplify(((1+w)/(1-w)-root).subs(w,1/sp.sqrt(3))) == 0, 'ratio orientation')
check(sp.simplify(sp.diff(w*(1-w*w),w)-(1-3*w*w)) == 0, 'orientation derivative')
check(sp.simplify((w*(1-w*w)).subs(w,1/sp.sqrt(3))-2/(3*sp.sqrt(3))) == 0, 'orientation max')
xx = 2/(C*(1+w)); yy = 2/(C*(1-w))
check(sp.simplify(1/xx+1/yy-C) == 0, 'budget normalization')
check(sp.simplify(yy-xx-4*w/(C*(1-w*w))) == 0, 'separation normalization')

# Compute the variance through the original covariance and through the
# precision decomposition, independently for an array of valid designs.
def original_variance(C, w, ell):
    x = 2/(C*(1+w)); y = 2/(C*(1-w))
    d = y-x
    rho = math.exp(-d/ell)
    one_minus_rho2 = -math.expm1(-2*d/ell)
    return x*x*y*y*one_minus_rho2/(x*x+y*y-2*x*y*rho)

def inverse_precision_variance(C, w, ell):
    u = C*(1+w)/2; v = C*(1-w)/2
    d = 4*w/(C*(1-w*w))
    rho = math.exp(-d/ell)
    J = (u-v)**2/(-math.expm1(-2*d/ell)) + 2*u*v/(1+rho)
    return 1/J

for ellv in (0.4,1.0,2.5):
    for Cv in (10,30,100,500):
        for wv in (0.1,0.3,1/math.sqrt(3),0.7):
            xval = 2/(Cv*(1+wv)); yval = 2/(Cv*(1-wv))
            if yval > 1: continue
            a=original_variance(Cv,wv,ellv)
            b=inverse_precision_variance(Cv,wv,ellv)
            check(abs(a-b) <= 2e-9*max(a,b), 'two variance implementations')
            lb=1/(ellv*Cv**3/(12*math.sqrt(3))+Cv**2)
            check(a+1e-14 >= lb, 'finite-budget global bound')

# The sharp cubic coefficient converges at the asserted orientation.
for ellv in (0.4,1.0,2.5):
    for Cv in (10000,100000,1000000):
        V=inverse_precision_variance(Cv,1/math.sqrt(3),ellv)
        ratio=V*Cv**3*ellv/(12*math.sqrt(3))
        tolerance=1.0/Cv*300/ellv
        check(abs(ratio-1)<tolerance, 'sharp asymptotic coefficient')

print(f'PASS: {checks} symbolic and numerical consistency checks')
