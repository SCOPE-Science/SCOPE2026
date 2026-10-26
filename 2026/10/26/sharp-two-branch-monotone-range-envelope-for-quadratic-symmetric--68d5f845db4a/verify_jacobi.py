"""Independent algebraic and numerical tests for the quadratic Jacobi range envelope.

Dependencies: sympy, numpy, scipy. This finite script is not a substitute
for the exact calculus argument in the associated theorem.
"""
import numpy as np
import sympy as sp
from scipy.special import betainc, gammaln

q, z, a = sp.symbols('q z a', real=True)
K = 1 + q*z*a + q**2*(q+2)/(2*(q-1))*(z*z-1/q)*(a*a-1/q)
zs = -1/((q+2)*a)
factor = -q*((q+2)*a*a-2*a-1)*((q+2)*a*a+2*a-1)/(2*a*a*(q-1)*(q+2))
assert sp.factor(K.subs(z,zs)-factor) == 0
assert sp.factor(K.subs(z,1) - q*((q+2)*a*a+2*a-1)/2) == 0
r=sp.sqrt(6)
au=1/(r+1)
ad=-1/(r-1)
x=(au+1)/2
s=(ad+1)/2
F=(1-s)*(1+3*(2*x-1)*s+5*(6*x*x-6*x+1)*s*(2*s-1))
assert sp.simplify(F-(sp.Rational(27,50)+6*r/25)) == 0
s=(au+1)/2
x=sp.Integer(1)
F=(1-s)*(1+3*(2*x-1)*s+5*(6*x*x-6*x+1)*s*(2*s-1))
assert sp.simplify(F-(27+3*r)/25) == 0


def response(Q, x, threshold):
    alpha=(Q-3)/2
    c=np.exp(gammaln(alpha+1.5)-0.5*np.log(np.pi)-gammaln(alpha+1))
    H=1-betainc(alpha+1,alpha+1,(threshold+1)/2)
    T=c*max(0.0,1-threshold*threshold)**(alpha+1)
    return H+T/(Q-1)*(Q*x+Q*(Q+2)*threshold*(x*x-1/Q)/2)


def branches(Q):
    R=np.sqrt(Q+3)
    u=1/(R+1)
    v=-1/(R-1)
    return response(Q,1,u),response(Q,u,v),u,v

for Q in [1.01,1.05,1.2,1.5,1.8,2,3,4,10,30]:
    E,I,u,v=branches(Q)
    exact=max(E,I)
    # Exhaustive structural candidate search by numerical sampling of thresholds.
    grid=np.linspace(-1+1e-6,1-1e-6,1101)
    values=[]
    for aa in grid:
        xx=1 if aa>=-1/(Q+2) else -1/((Q+2)*aa)
        values.append(response(Q,xx,aa))
    assert max(values) <= exact+0.00002, (Q, max(values),exact)
    assert response(Q,1,u) >= response(Q,1,-1+1e-6)-1e-9
    print(f'q={Q:g}, E={E:.9f}, I={I:.9f}, max={exact:.9f}, '+('endpoint' if E>I else 'interior'))

# Cross-check closed step response using direct adaptive quadrature of the kernel.
from scipy.integrate import quad
for Q in [1.3,2,3,5,12]:
    alpha=(Q-3)/2
    c=np.exp(gammaln(alpha+1.5)-0.5*np.log(np.pi)-gammaln(alpha+1))
    for x,a0 in [(-0.7,-0.8),(.33,-0.6),(.9,.4)]:
        def kernel(x,y):
            return 1+Q*x*y+Q**2*(Q+2)/(2*(Q-1))*(x*x-1/Q)*(y*y-1/Q)
        integrand=lambda y: c*(1-y*y)**alpha*kernel(x,y)
        integ=quad(integrand,a0,1,epsabs=1e-10,epsrel=1e-10,limit=200)[0]
        assert abs(integ-response(Q,x,a0))<1e-8,(Q,x,a0,integ,response(Q,x,a0))
print('All algebraic identities and numerical cross-checks passed.')
