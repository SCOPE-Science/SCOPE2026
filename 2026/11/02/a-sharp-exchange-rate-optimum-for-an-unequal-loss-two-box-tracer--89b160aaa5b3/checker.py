"""Standalone exact-algebra and high-precision checks for a two-box tracer theorem.

Dependencies: Python 3, sympy, mpmath. The theorem's proof is in RESULT.md;
finite numerical checks are corroboration, not a proof of global uniqueness.
Run: python checker.py
"""
import math
import random
import sympy as sp
import mpmath as mp

checks = 0

def check(statement, context):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(context)

# At a stationary point of y exp(-y) sinh(z)/z, z=sqrt(y^2+r),
# eliminate coth(z) using D(y,r)=0 and csch^2(z)=coth^2(z)-1.
y, r = sp.symbols('y r', positive=True)
z2 = y*y + r
coth2 = z2 / y**2 * (1-r/(y*z2))**2
Dy_at_zero = (-r/(y*y*z2) - 2*r/z2**2
              + r/(y*z2)*(1-r/(y*z2))
              - y*y/z2*(coth2-1))
target = -r*(y*y-3*y+3)/(y*y*(y*y+r))
check(sp.cancel(Dy_at_zero-target) == 0, 'stationary logarithmic-curvature identity')
# Hyperbolic positivity: z*sinh(z)*cosh(z)+z^2-2*sinh(z)^2
# has coefficient (n-2)*2^(2n-1)/(2n)! for every n>=3.
z = sp.symbols('z', real=True)
H = z*sp.sinh(z)*sp.cosh(z)+z*z-2*sp.sinh(z)**2
series = sp.series(H, z, 0, 32).removeO().expand()
for n in range(16):
    coeff=sp.factor(series.coeff(z,2*n))
    expected=0 if n<=2 else sp.Rational((n-2)*2**(2*n-1),math.factorial(2*n))
    check(coeff == expected, f'hyperbolic series coefficient {n}')

mp.mp.dps = 75

def d(yv,rv):
    zv = mp.sqrt(yv*yv+rv)
    return rv/(yv*(yv*yv+rv)) + yv/zv*mp.coth(zv)-1

def response(yv,rv):
    zv = mp.sqrt(yv*yv+rv)
    return yv*mp.exp(-yv)*mp.sinh(zv)/zv

def root(rv):
    lo,hi=mp.mpf(1),mp.mpf(2)
    while d(hi,rv)>0:
        hi *= 2
        check(hi<1000000, 'finite root upper bracket')
    for _ in range(260):
        mid=(lo+hi)/2
        if d(mid,rv)>0:lo=mid
        else:hi=mid
    check(abs(d((hi+lo)/2,rv)) < mp.mpf('1e-65'), 'root residual')
    return (lo+hi)/2

rng=random.Random(20261029)
rs = [mp.mpf(10)**mp.mpf(-6 + 12*j/80) for j in range(81)]
ys = [root(rv) for rv in rs]
for j in range(len(ys)-1):
    check(ys[j]>ys[j+1]>1, 'strict decrease of optimum with contrast')
for rv, yv in zip(rs,ys):
    check(d(yv*mp.mpf('0.999'),rv)>0, 'positive gradient immediately before optimum')
    check(d(yv*mp.mpf('1.001'),rv)<0, 'negative gradient immediately after optimum')
    derivative=mp.diff(lambda v:d(v,rv),yv)
    exact=-rv*(yv*yv-3*yv+3)/(yv*yv*(yv*yv+rv))
    check(abs(derivative-exact)<mp.mpf('1e-60'), 'critical curvature formula')
    check(derivative<0, 'negative curvature')
    for scale in (mp.mpf('.02'),mp.mpf('.1'),mp.mpf('.5'),mp.mpf('.8'),mp.mpf('1.5'),mp.mpf('2.0'),mp.mpf('10')):
        check(response(yv,rv)>response(yv*scale,rv), 'sampled global optimum')
    check(response(yv,rv)>mp.mpf('.5'), 'strict above perfect mixing')

# Several examples computed directly from the two-box matrix exponential.
for j in range(100):
    p=mp.mpf(rng.randint(0,100))/20
    q=mp.mpf(rng.randint(0,100))/20
    T=mp.mpf(rng.randint(1,10))/4
    K=mp.mpf(rng.randint(1,60))/15
    mat=mp.matrix([[-K-p,K],[K,-K-q]])
    direct=mp.expm(mat*T)[1,0]
    delta=(p-q)/2
    S=mp.sqrt(K*K+delta*delta)
    formula=K/S*mp.exp(-(K+(p+q)/2)*T)*mp.sinh(S*T)
    check(abs(direct-formula)<mp.mpf('1e-63'), 'matrix exponential equality')
    swapped=mp.expm(mp.matrix([[-K-q,K],[K,-K-p]])*T)[1,0]
    check(abs(direct-swapped)<mp.mpf('1e-63'),'receiver invariance under swapped losses')

# Strictly unequal examples, in physical units.
for ell1,ell2,T in [(0,2,1),(0,10,1),(0,1,2),(3,1,3)]:
    rv=(mp.mpf(T)*(ell1-ell2)/2)**2
    kstar=root(rv)/T
    receiver=mp.exp(-mp.mpf(T)*(ell1+ell2)/2)*response(kstar*T,rv)
    large=mp.exp(-mp.mpf(T)*(ell1+ell2)/2)/2
    check(receiver>large,'optimum beats infinite mixing')
    print('losses=',ell1,ell2,'horizon=',T,'optimal_exchange=',mp.nstr(kstar,18),'max_receiver=',mp.nstr(receiver,18),'perfect_mix_limit=',mp.nstr(large,18))

print('PASS',checks,'checks')
