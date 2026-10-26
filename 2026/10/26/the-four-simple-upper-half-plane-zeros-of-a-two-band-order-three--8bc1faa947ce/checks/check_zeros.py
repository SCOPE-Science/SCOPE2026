#!/usr/bin/env python3
"""Independent symbolic and numerical checks of the two-band zero theorem."""
import sympy as s
import mpmath as mp
z,a,y=s.symbols('z a y',real=True)
P=3*y**4+(a**2+10*a+1)*y**3-(9*a**3+12*a**2+9*a)*y**2+3*a*(a**4+a**3+a+1)*y+a**3*(a**2+a+1)
Q=a**10+326*a**9+669*a**8+1448*a**7+3682*a**6+6180*a**5+3682*a**4+1448*a**3+669*a**2+326*a+1
F=sum(((z-hi)**(-3)-(z-lo)**(-3))/3 for lo,hi in [(-1,-a),(a,1)])
assert s.cancel(F-2*(1-a)*P.subs(y,z*z)/(3*(z*z-a*a)**3*(z*z-1)**3))==0
assert s.factor(s.discriminant(P,y)+108*a**3*(a-1)**2*(a+1)**6*Q)==0
assert s.factor(P.subs(y,0)-a**3*(a*a+a+1))==0
assert s.factor(P.subs(y,-a)+3*a*a*(a+1)**4)==0
print('exact quartic identity: PASS')
print('exact discriminant factorization: PASS')
print('sign identities: PASS')
for frac in [s.Rational(1,20),s.Rational(1,5),s.Rational(1,2),s.Rational(4,5)]:
    roots=s.nroots(P.subs(a,frac),maxsteps=200)
    neg=[complex(t) for t in roots if abs(complex(t).imag)<1e-9 and complex(t).real<0]
    off=[complex(t) for t in roots if abs(complex(t).imag)>1e-9]
    assert len(neg)==2 and len(off)==2
    print(f'rho={frac}: two negative real y-roots and conjugate nonreal pair: PASS')
mp.mp.dps=55
maxerr=mp.mpf('0')
for aa in [mp.mpf('0.2'),mp.mpf('0.65')]:
    for zz in [mp.mpc('0.3','0.9'),mp.mpc('-1.1','0.7')]:
        direct=mp.quad(lambda x:(zz-x)**-4,[-1,-aa])+mp.quad(lambda x:(zz-x)**-4,[aa,1])
        endpoint=sum(((zz-hi)**-3-(zz-lo)**-3)/3 for lo,hi in [(-1,-aa),(aa,1)])
        err=abs(direct-endpoint)
        maxerr=max(maxerr,err)
        assert err<mp.mpf('1e-35')
print('numerical integral comparisons: 4 PASS')
print('maximum absolute error:',mp.nstr(maxerr,10))
print('ALL CHECKS PASS')
