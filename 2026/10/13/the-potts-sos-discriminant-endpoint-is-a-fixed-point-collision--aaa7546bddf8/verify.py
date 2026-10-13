#!/usr/bin/env python3
import sympy as sp

th, z = sp.symbols('th z')
f = ((2 + th*z)/(2*th + z))**2
N = th**2*z**2 - 4*th**2*z - 4*th*z**2 + 4*th*z - z**3 + 4
P = 3*th**4 + 10*th**3 + 6*th**2 - 1
Q = th**4 + 5*th**3 + 4*th**2 - 1
H = th**2*(th + 2)**2*z**2 + 4*Q*z + 4*th**2*(2*th + 1)**2

num = sp.factor(sp.together(f.subs(z, f) - z).as_numer_denom()[0])
assert sp.expand(num - N*H) == 0
assert sp.expand(sp.together(f-z).as_numer_denom()[0] - N) == 0
assert sp.factor(sp.discriminant(H, z) + 16*(th-1)**2*(th+1)**2*P) == 0
assert sp.factor(sp.resultant(N, H, z) - 256*(th-1)**6*(th+1)**6*P) == 0
assert sp.expand(Q - (P - th**2*(th+2)*(2*th+1))) == 0

# Endpoint fixed-point identity: the double root of H at P=0 is also a fixed point.
zc = -2*Q/(th**2*(th+2)**2)
num_endpoint = sp.factor(sp.together(N.subs(z, zc)).as_numer_denom()[0])
assert sp.rem(sp.Poly(num_endpoint, th), sp.Poly(P, th)) == 0
fp_plus_one = sp.factor(sp.together(sp.diff(f,z).subs(z,zc)+1).as_numer_denom()[0])
assert sp.rem(sp.Poly(fp_plus_one, th), sp.Poly(P, th)) == 0

# The critical polynomial has exactly one positive root, because P' > 0 for th>0.
assert sp.factor(sp.diff(P, th)) == 6*th*(2*th+1)*(th+2)
root = [r for r in sp.nroots(P, n=70, maxsteps=200) if abs(sp.im(r)) < sp.Rational(1,10)**50 and sp.re(r) > 0]
assert len(root) == 1
thc = sp.N(sp.re(root[0]), 60)
assert thc > 0 and thc < 1
zc_num = sp.N(zc.subs(th, thc), 60)
assert zc_num > 0

# A rational sample below threshold has two positive nonfixed H-roots swapped by f.
q = sp.Rational(1,4)
Hq = sp.Poly(H.subs(th,q),z)
rts = sorted([sp.N(r,50) for r in sp.nroots(Hq, n=80, maxsteps=200)], key=lambda x: float(sp.re(x)))
assert len(rts) == 2 and all(abs(sp.im(r)) < sp.Rational(1,10)**40 and sp.re(r)>0 for r in rts)
r1,r2 = map(lambda x: sp.re(x), rts)
fq = sp.lambdify(z, f.subs(th,q), 'mpmath')
import mpmath as mp
mp.mp.dps=60
assert abs(fq(mp.mpf(str(r1))) - mp.mpf(str(r2))) < mp.mpf('1e-45')
assert abs(fq(mp.mpf(str(r2))) - mp.mpf(str(r1))) < mp.mpf('1e-45')

# Above threshold, e.g. th=1/3, the discriminant is negative.
assert sp.N(sp.discriminant(H,z).subs(th,sp.Rational(1,3)),40) < 0

amp = 4*(1-thc**2)*sp.sqrt(sp.diff(P,th).subs(th,thc))/(thc**2*(thc+2)**2)
print('VERIFY_OK')
print('theta_c=' + str(sp.N(thc,50)))
print('z_c=' + str(sp.N(zc_num,50)))
print('separation_amplitude=' + str(sp.N(amp,50)))
print('factorization=1 endpoint_fixed=1 flip_derivative=1')
