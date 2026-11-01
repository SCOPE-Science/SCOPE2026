"""Exact checks for stationary dyadic-depth correlations of a random interval map.
Run with Python 3 and SymPy: python verify.py
"""
import sympy as S

q,z=S.symbols('q z', positive=True)
N=S.symbols('N', integer=True, positive=True)
k=S.symbols('k', integer=True, nonnegative=True)
a=1-q
mu=2/(1+q)
pi0=q/(1+q)
pi=lambda j: 2**(-j)/(1+q)
p=lambda j: 2**(-j-1)
E=lambda expr: S.simplify(pi0*expr.subs(k,0)+S.summation(pi(k)*expr,(k,1,S.oo)))
var=S.factor(E((k-mu)**2))
assert S.simplify(E(k)-mu)==0
assert S.simplify(var-2*(3*q+1)/(1+q)**2)==0
# Transition kernel P on a function f, with geometrically distributed reinjection at 0.
h=(k*(k+1)/2-mu*k)/q
P_h0=S.summation(p(k)*h,(k,0,S.oo))
assert S.simplify(-P_h0+mu)==0
assert S.simplify(h-(a*h+q*h.subs(k,k-1))-(k-mu))==0
v0=-1/(1+q)
v=lambda j: pi(j)
w0=-mu*pi0
w=lambda j: pi(j)*(j-mu)
s=1-q/2
r=(1-q)/2
d=q*(1-mu)/2
# Signed left row-vectors; column index j=0 or j>=1.
assert S.simplify(v0*p(0)+q*v(1)-r*v0)==0
assert S.simplify(v0*p(k)+a*v(k)+q*v(k+1)-r*v(k))==0
assert S.simplify(w0*p(0)+q*w(1)-s*w0-d*v0)==0
assert S.simplify(w0*p(k)+a*w(k)+q*w(k+1)-s*w(k)-d*v(k))==0
assert S.simplify(S.summation(k*v(k),(k,1,S.oo))-mu)==0
B=2*q*(1-q)/(1+q)**2
assert S.simplify(var-2-B)==0
assert S.simplify(2*d*mu+B)==0
sigma2=S.factor(2*(1+s)/(1-s)+B*(1+r)/(1-r))
assert S.simplify(sigma2-(8/q-2+2*q*(1-q)*(3-q)/(1+q)**3))==0
R=lambda t:N*(1+t)/(1-t)-2*t*(1-t**N)/(1-t)**2
# Symbolic finite-lag summation, at several N and rational parameters.
for qq in [S.Rational(1,5),S.Rational(1,2),S.Rational(3,4),S.Integer(1)]:
    for nn in [1,2,4,9,17]:
        direct=2*nn+B.subs(q,qq)*nn
        direct=nn*var.subs(q,qq)+2*sum((nn-j)*(2*s.subs(q,qq)**j+B.subs(q,qq)*r.subs(q,qq)**j) for j in range(1,nn))
        formula=(2*R(s)+B*R(r)).subs({q:qq,N:nn})
        assert S.simplify(direct-formula)==0
assert S.limit(q*sigma2,q,0,dir='+')==8
assert sigma2.subs(q,1)==6
print('PASS: stationary moments, signed-row eigenrelation including boundary,')
print('quadratic Poisson equation, every-lag covariance, Green–Kubo variance,')
print('20 exact rational finite-time sums, and critical variance limit.')
