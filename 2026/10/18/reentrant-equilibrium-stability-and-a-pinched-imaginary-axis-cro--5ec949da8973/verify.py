"""Exact algebraic and finite spectral checks for the Dong three-dimensional flow.

Requires Python 3, sympy and numpy.  No numerical sample substitutes for
Routh's exact cubic root-count theorem or the polynomial proof.
"""
import sympy as sp
import numpy as np

a,b,c=sp.symbols('a b c', positive=True)
t=sp.Symbol('lam')
# Only a,b,c>0 are required in the theorem.  k is unrestricted here.
k=sp.Symbol('k', real=True)
d=a-c*k
x=sp.sqrt(b*d/a)
y=b/x
z=-a*c/d
J=sp.Matrix([[-a+k*z,a,k*x],[-z,-c,-x],[y,x,0]])
P=sp.cancel(J.charpoly(t).as_expr())
Q=(a*a+a*c-c*c*k)/d
R=b*(a-(a+c)*k)/a
S=2*b*d
assert sp.factor(P-(t**3+Q*t**2+R*t+S))==0
Delta=sp.factor(Q*R-S)
assert sp.factor(Delta + b*(a*a-a*c+c*c*k)*(a+(a-c)*k)/(a*d))==0
assert sp.factor(Delta.subs(a,2*c)+b*c*(k+2)**2/(2*(2-k)))==0
assert sp.simplify(Q.subs({a:2*c,k:-2})-2*c)==0
assert sp.simplify(R.subs({a:2*c,k:-2})-4*b)==0
assert sp.simplify(S.subs({a:2*c,k:-2})-8*b*c)==0

# The coefficient of (k+2)^2 in Re(lambda_+) at a=2c.
# At a simple imaginary pair and small nonzero Delta,
# Re(lambda_+)=-Delta/[2(Q^2+R)]+O(Delta^2).
epsilon=sp.symbols('epsilon',real=True)
double_term=sp.limit((-Delta/(2*(Q**2+R))).subs({a:2*c,k:-2+epsilon})/epsilon**2,epsilon,0)
assert sp.simplify(double_term-b*c/(64*(b+c*c)))==0

cases=[
  (1.0,2.0,1.0,[-3.0,0.0,0.4,0.49]),
  (1.0,1.0,5.0,[-2.0,-0.2,0.0,0.4]),
  (3.0,1.0,4.0,[-9.0,-4.0,-2.0,0.0]),
  (2.0,1.0,1.0,[-4.0,-2.1,-1.9,0.0]),
  (10.0,11.2,100.0,[-0.2,0.01,0.3]),
]
count=0
for aa,cc,bb,ks in cases:
    for kk in ks:
        assert aa-cc*kk>0
        coeff=np.array([1.,float(Q.subs({a:aa,c:cc,k:kk})),float(R.subs({a:aa,b:bb,c:cc,k:kk})),float(S.subs({a:aa,b:bb,c:cc,k:kk}))])
        roots=np.roots(coeff)
        dd=float(Delta.subs({a:aa,b:bb,c:cc,k:kk}))
        if abs(dd)>1e-8:
            assert sum(r.real>1e-9 for r in roots)==(0 if dd>0 else 2)
        count+=1
print('PASS exact characteristic, Routh determinant, double tangency; numerical cases:',count)
