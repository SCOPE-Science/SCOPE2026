"""Supplementary algebraic and numerical cross-checks for a Bergman kernel transition.

Run with Python 3, sympy and mpmath. Finite checks supplement, not replace,
the all-parameter analytic proof in RESULT.md.
"""
import math
import sympy as sp
import mpmath as mp

u = sp.symbols('u')
u0 = (1 + sp.I*sp.sqrt(3))/2
w0 = 1-u0
G0 = sum(sp.binomial(5,k)*(-u)**k/sp.Integer(k+1) for k in range(6))
assert sp.simplify(G0 - (1-(1-u)**6)/(6*u)) == 0
assert sp.simplify(G0.subs(u,u0)) == 0
assert sp.simplify(sp.diff(G0,u).subs(u,u0)-1)==0

# d_s G at (s,alpha)=(1,4), evaluated at the boundary root.
Gs = sum(-sp.binomial(5,k)*(-u0)**k/sp.Integer((k+1)**2) for k in range(6))
assert sp.simplify(sp.expand_complex(Gs) - (-sp.Rational(119,360)+7*sp.I*sp.sqrt(3)/45)) == 0

# d_alpha G via an elementary logarithmic antiderivative.
Ga = sp.I*sp.pi/(18*u0)
assert sp.simplify(sp.expand_complex(Ga) - sp.pi*(sp.sqrt(3)+sp.I)/36)==0
rad_s = sp.simplify(sp.re(sp.expand_complex(-Gs/u0)))
rad_a = sp.simplify(sp.re(sp.expand_complex(-Ga/u0)))
assert sp.simplify(rad_s + sp.Rational(49,720))==0
assert sp.simplify(rad_a + sp.pi*sp.sqrt(3)/36)==0
slope = sp.simplify(-rad_s/rad_a)
assert sp.simplify(slope + 49*sp.sqrt(3)/(60*sp.pi))==0

# Exactly two of five polynomial product zeros have modulus one at base.
roots = [1-sp.exp(2*sp.pi*sp.I*j/6) for j in range(1,6)]
mods = [sp.simplify(sp.expand_complex(sp.Abs(x)**2)) for x in roots]
assert sorted(mods, key=lambda x: float(x))==[1,1,3,3,4]

mp.mp.dps=35
root0 = mp.e**(mp.j*mp.pi/3)
def g(s,a,z):
    return s*mp.quad(lambda t: t**(s-1)*(1-z*t)**(a+1), [0,1])
def gh(s,a,z):
    return mp.hyp2f1(-a-1,s,s+1,z)
for s,a,z in [(mp.mpf('0.91'),mp.mpf('3.85'),mp.mpc('0.32','0.12')),
              (mp.mpf('1.09'),mp.mpf('4.17'),mp.mpc('-0.71','0.18')),
              (mp.mpf('1.02'),mp.mpf('3.99'),mp.mpc('0.47','0.79'))]:
    assert abs(g(s,a,z)-gh(s,a,z))<mp.mpf('1e-26')
assert abs(g(1,4,root0))<mp.mpf('1e-27')

def boundary(s):
    # Solve two real equations for angular root and critical exponent.
    th,ac=mp.findroot(lambda th,ac:
                      (mp.re(g(s,ac,mp.e**(mp.j*th))),
                       mp.im(g(s,ac,mp.e**(mp.j*th)))),
                      (mp.pi/3,4+mp.mpf(str(float(s-1)))*mp.mpf(str(float(slope)))),
                      tol=mp.mpf('1e-28'))
    assert abs(g(s,ac,mp.e**(mp.j*th)))<mp.mpf('1e-24')
    return th,ac
th_m, ac_m = boundary(mp.mpf('.98'))
th_0, ac_0 = boundary(mp.mpf('1.0'))
th_p, ac_p = boundary(mp.mpf('1.02'))
assert abs(ac_0-4)<mp.mpf('1e-24')
assert abs((ac_p-ac_m)/mp.mpf('.04')-mp.mpf(str(float(slope))))<mp.mpf('.001')
for ss,aa,theta in [(mp.mpf('.98'),ac_m,th_m),
                    (mp.mpf('1.02'),ac_p,th_p)]:
    for shift,sign in [(-mp.mpf('.015'),1),(mp.mpf('.015'),-1)]:
        zz=mp.findroot(lambda z:g(ss,aa+shift,z),
                       (mp.mpf('.998')*mp.e**(mp.j*theta),
                        mp.mpf('1.002')*mp.e**(mp.j*theta)),
                       tol=mp.mpf('1e-27'))
        assert sign*(abs(zz)-1)>0
print('PASS: exact beta-moment transformation, root count, derivatives, tangent and finite numerical crossing checks.')
print('critical tangent:', sp.sstr(slope), '≈', mp.nstr(float(slope),14))
print('critical alpha(0.98), alpha(1.00), alpha(1.02):',
      mp.nstr(ac_m,16), mp.nstr(ac_0,16), mp.nstr(ac_p,16))
