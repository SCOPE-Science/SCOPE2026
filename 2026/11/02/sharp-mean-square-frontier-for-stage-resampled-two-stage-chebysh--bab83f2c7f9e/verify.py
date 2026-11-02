"""Exact checks for stage-resampled two-stage Chebyshev descent on scalar quadratics.

Run: python verify.py  (requires sympy; see requirements.txt)
These checks corroborate, but do not replace, the distribution-free proof.
"""
from fractions import Fraction as Q
from itertools import product
import random
import sympy as S

m, v, x, y = S.symbols('m v x y', real=True)
M = 1 - (x + y) / 2 + x*y/8
R = lambda t: 1-t+t*t/8
moment = S.Integer(0)
for (i,j), coeff in S.Poly(M**2,x,y).terms():
    moment += coeff * {0: 1, 1: m, 2: m*m+v}[i] * {0: 1, 1: m, 2: m*m+v}[j]
assert S.expand(moment - 1 - ((m*m-4*m+v)*(m*m-12*m+v+32))/64) == 0
assert S.expand(R(m) - (1-m+m*m/8)) == 0
assert S.simplify(moment.subs(m,4) - (1+v*v/64)) == 0
assert S.simplify(M.subs({x:m,y:m})-R(m))==0

for a in range(1,8):
    for b in range(1,8):
        p = [Q(1,8),Q(3,8),Q(1,2),Q(5,8),Q(7,8)]
        for t in p:
            mean = t*a+(1-t)*b
            variance = t*(a-mean)**2+(1-t)*(b-mean)**2
            exact = sum(wz*wt*(Q(1,1)-Q(z+u,2)+Q(z*u,8))**2 for (z,wz),(u,wt) in product(((a,t),(b,1-t)),repeat=2))
            factored = Q(1,1)+(mean*mean-4*mean+variance)*(mean*mean-12*mean+variance+32)/64
            assert exact==factored

# Direct stage-by-stage sample outcome certificates, with independent clients 1 or 6.
out={}
for a,b in product((Q(1),Q(6)), repeat=2):
    w0=Q(1)
    w1=w0-a*w0/4
    w2=2*w1-w0-b*w1/2
    out[(a,b)]=w2
    assert w2 == 1-(a+b)/2+a*b/8
assert out == {(Q(1),Q(1)):Q(1,8),(Q(1),Q(6)):Q(-7,4),(Q(6),Q(1)):Q(-7,4),(Q(6),Q(6)):Q(-1,2)}
assert sum(out.values(),Q(0))/4 == Q(-31,32)
assert sum((z*z for z in out.values()),Q(0))/4 == Q(409,256)
assert (R(Q(1))**2+R(Q(6))**2)/2 == Q(17,128)
# Exact logarithmic exponent: exp(4*E(log(abs M)))=7**2/4**4.
assert S.prod([S.Abs(S.Rational(z.numerator,z.denominator)) for z in out.values()]) == S.Rational(49,256)

# A few nontrivial exact generic curvature distributions: direct enumeration vs moments.
rng=random.Random(220112782)
for i in range(480):
    k=rng.randint(2,5)
    zs=[Q(rng.randint(1,63),8) for _ in range(k)]  # all in (0,8)
    counts=[rng.randint(1,13) for _ in range(k)]
    w=[Q(c,sum(counts)) for c in counts]
    mu=sum((z*p for z,p in zip(zs,w)),Q(0))
    vv=sum((p*(z-mu)**2 for z,p in zip(zs,w)),Q(0))
    e2=sum((w[i]*w[j]*(Q(1)-(zs[i]+zs[j])/2+zs[i]*zs[j]/8)**2 for i in range(k) for j in range(k)),Q(0))
    assert e2==1+(mu*mu-4*mu+vv)*(mu*mu-12*mu+vv+32)/64

print('VERIFY_OK: symbolic stage-product/moment factorization; 245 exact two-client probability grids; 480 finite-support certificates; two-client mean, mean-square and log-moment identities')
