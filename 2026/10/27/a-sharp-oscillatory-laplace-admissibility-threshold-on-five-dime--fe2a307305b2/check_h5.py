"""Independent symbolic identities and numerical quadratures for a radial H^5 kernel.

Requirements: Python 3, sympy, mpmath.
All mathematical statements are in RESULT.md; this program checks identities and samples.
"""
import sympy as sp
import mpmath as mp

A, W, X, Z = sp.symbols('A W X Z', real=True)
R = A - sp.I * sp.symbols('omega', real=True)
omega = sp.symbols('omega', real=True)
D = (Z*Z+X)*((Z-2)**2+X)*((Z+2)**2+X)
S = (3-Z)/((Z-2)**2+X)+(-3-Z)/((Z+2)**2+X)+2*Z/(Z*Z+X)
assert sp.cancel(S-32*Z*(X+1)/D) == 0

C = (A*A-4)**2+(24-10*A*A)*W+5*W*W
P = A*(X**3+(3*A*A+3*W+8)*X**2 + (3*A**4-6*A*A*W-9*W*W+16)*X+(A*A+W)*C)
Dc = sp.prod(((R+k)**2+X) for k in (-2,0,2))
assert sp.expand(sp.re(sp.expand_complex(R*sp.conjugate(Dc))).subs(omega**2,W)-P) == 0
assert sp.simplify(P.subs(X,W-A*A+4)+8*A*(A*A-4)*(W+2)*(W+4))==0
assert sp.simplify(C.subs(W,A*A-4)+4*A*A*(A*A-4)) == 0
assert sp.simplify(C.subs(W,A*A/3)+16*(A*A-3)*(A*A+3)/9) == 0
assert sp.simplify(sp.discriminant(C,W)-16*(5*A**4-20*A*A+16)) == 0

mp.mp.dps = 50

def phi5(lam, r):
    if lam == 0:
        # Correct limit of -3/(1+lam^2)/sinh(r) * d/dr[sin(lam*r)/(lam*sinh(r))]
        return 3*(r*mp.cosh(r)-mp.sinh(r))/mp.sinh(r)**3
    return 3*(mp.sin(lam*r)*mp.cosh(r)/lam-mp.cos(lam*r)*mp.sinh(r))/((1+lam*lam)*mp.sinh(r)**3)

def transform_direct(a,omega,lam):
    integrand=lambda r: mp.exp(-a*r)*mp.cos(omega*r)*phi5(lam,r)*mp.sinh(r)**4
    return mp.quad(integrand,[mp.mpf('1e-6'),mp.mpf('.1'),1,3,8,20,mp.inf])

def transform_closed(a,omega,lam):
    z=mp.mpc(a,-omega); x=lam**2
    return mp.re(24*z/((z*z+x)*((z-2)**2+x)*((z+2)**2+x)))

count=0
worst=mp.mpf(0)
for a,omega,lam in ((5,0,0),(5,mp.mpf('0.5'),0.3),(5,mp.mpf('1.2'),1.4),
                    (5,mp.mpf('1.5'),0),(5,mp.mpf('1.8'),3),
                    (6,mp.sqrt(mp.mpf(16)/5),0),(6,mp.sqrt(mp.mpf(16)/5),1),
                    (6,mp.mpf('2.5'),.3),(6,10,7),
                    (10,1.2,0.5),(10,3,5),(10,9,11)):
    lhs=transform_direct(mp.mpf(a),mp.mpf(omega),mp.mpf(lam))
    rhs=transform_closed(mp.mpf(a),mp.mpf(omega),mp.mpf(lam))
    err=abs(lhs-rhs)
    worst=max(worst,err)
    assert err < mp.mpf('3e-17'),(a,omega,lam,err)
    count+=1
print('symbolic_identities PASS')
print('independent_numerical_integrals',count,'PASS; max_abs_error',mp.nstr(worst,9))
print('a=6 exact threshold omega^2=16/5')
print('a=5 threshold omega=',mp.nstr(mp.sqrt(25-mp.mpf(12)/5-mp.mpf(2)/5*mp.sqrt(5*5**4-20*5**2+16)),20))
