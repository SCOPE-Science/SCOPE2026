"""Exact auxiliary identities for the quadratic harmonic Poisson fourth moment.

Usage: python CHECK.py. Requires SymPy 1.12 or later.
The analytic inequalities and uniqueness argument are supplied in RESULT.md.
"""
from itertools import product
import math
import random
import sympy as S

x, a, d, b, e, y, z, s, t = S.symbols('x a d b e y z s t', nonnegative=True)
coeff = {-2: e, -1: d, 0: x, 1: a, 2: b}
exact = sum(
    S.Rational(2, 2 + abs(i) + abs(j) + abs(k) + abs(l))
    * coeff[i]*coeff[j]*coeff[k]*coeff[l]
    for i, j, k, l in product(range(-2, 3), repeat=4)
    if i+j == k+l
)
A, B, p, q = a*a + d*d, b*b + e*e, a*d, b*e
claimed = (x**4 + 2*x*x*A + 2*x*x*p + S.Rational(4,3)*x*x*B
           + S.Rational(4,3)*x*x*q
           + S.Rational(4,3)*x*(a*a*b + d*d*e + 2*a*d*(b+e))
           + A*A/S.Integer(3) + S.Rational(2,3)*p*p
           + B*B/S.Integer(5) + S.Rational(2,5)*q*q + A*B + 2*p*q)
assert S.expand(exact-claimed) == 0
G = (x**4 + 3*x*x*y*y + 2*x*x*z*z + 2*S.sqrt(2)*x*y*y*z
     + y**4/2 + S.Rational(3,2)*y*y*z*z + S.Rational(3,10)*z**4)
assert S.simplify(exact.subs({a:y/S.sqrt(2),d:y/S.sqrt(2),b:z/S.sqrt(2),e:z/S.sqrt(2)})-G) == 0
F = (S.Rational(1,2)*t*t + (3 + 2*s + 3*s*s/4)*t
     + 1+s*s + 3*s**4/S.Integer(40))/(t+1+s*s/2)**2
assert S.simplify(G.subs({x:1,y:S.sqrt(t),z:s/S.sqrt(2)})/(1+t+s*s/2)**2-F) == 0
T = (9*s**4+40*s**3+10*s*s+80*s+40)/(10*(s*s+8*s+8))
B0, C0, A0 = 3+2*s+3*s*s/4, 1+s*s/2, 1+s*s+3*s**4/40
assert S.factor(S.diff(F,t) - ((C0-B0)*t+B0*C0-2*A0)/(t+C0)**3) == 0
assert S.factor(((B0*C0-2*A0)/(B0-C0))-T) == 0
R = ((33*s**4 + 240*s**3+520*s*s+960*s+560)
     /(8*(7*s**4+40*s**3+30*s*s+80*s+60)))
assert S.factor(F.subs(t,T)-R) == 0
P = 18*s**4+121*s**3+180*s*s-100*s-80
Rp = -5*(s*s+8*s+8)*P/(2*(7*s**4+40*s**3+30*s*s+80*s+60)**2)
assert S.factor(S.diff(R,s)-Rp) == 0
assert P.subs(s,S.Rational(7425,10000)) < 0 < P.subs(s,S.Rational(7426,10000))
assert S.factor(G.subs({x:0,y:S.sqrt(1-z*z)})-(S.Rational(1,2)+z*z/S.Integer(2)-S.Rational(7,10)*z**4)) == 0
assert S.Rational(33,56) < S.Rational(7,6)
assert S.factor(G.subs({z:0,x:S.sqrt(1-y*y)})-(1+y*y-S.Rational(3,2)*y**4))==0
assert S.Rational(7,6)<R.subs(s,S.Rational(3,4))
# Independent direct evaluation with arbitrary complex coefficients.
def moment(v):
    return sum((2/(2+sum(map(abs,ij))))*(v[ij[0]]*v[ij[1]]
             *v[ij[2]].conjugate()*v[ij[3]].conjugate())
             for ij in product(range(-2,3),repeat=4)
             if ij[0]+ij[1]==ij[2]+ij[3]).real
root = next(float(S.re(r)) for r in S.nroots(P, maxsteps=200)
            if abs(float(S.im(r)))<1e-10 and 0<float(S.re(r))<2)
opt_t=float(T.subs(s,root));opt_x=(1+opt_t+root**2/2)**(-.5)
v={-2:opt_x*root/2,-1:opt_x*math.sqrt(opt_t/2),0:opt_x,
   1:opt_x*math.sqrt(opt_t/2),2:opt_x*root/2}
k=float(R.subs(s,root))
assert abs(sum(abs(w)**2 for w in v.values())-1)<1e-13
assert abs(moment(v)-k)<1e-12
random.seed(261031)
for _ in range(768):
    v0={i:complex(random.gauss(0,1),random.gauss(0,1)) for i in range(-2,3)}
    norm=sum(abs(w)**2 for w in v0.values())
    assert moment(v0) <= (k+1e-11)*norm*norm
print(f'CHECK_OK exact-symbolic=12 random-complex=768 K4={k:.14f} root={root:.12f}')
