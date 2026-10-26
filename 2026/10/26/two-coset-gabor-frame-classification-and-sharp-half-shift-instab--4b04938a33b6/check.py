"""Standalone finite and symbolic checks for the odd-rational-window theorem.
All infinite-dimensional assertions are proved analytically in RESULT.md."""
import math
import cmath
import sympy as sp
import numpy as np
from scipy.optimize import minimize

q = math.exp(-2*math.pi)

def g(t):
    return t/((t*t+1)*(t*t+4))

def B(x,w):
    z=cmath.exp(2j*math.pi*x)
    r=math.exp(2*math.pi*w)
    return r*q*z/(1-q*z)-r*r*q*q*z/(1-q*q*z)-1/r/(1-q/z)+1/(r*r)/(1-q*q/z)

def Zak(x,w):
    return (1j*math.pi/3)*cmath.exp(2j*math.pi*w*x)*B(x,w).conjugate()

def direct_Z(x,w,N=4000):
    return sum(g(x-n)*cmath.exp(2j*math.pi*n*w) for n in range(-N,N+1))

for x,w in ((.21,.1),(.31,.37),(.7,.8),(.5,.5),(.125,.875)):
    assert abs(Zak(x,w)-direct_Z(x,w))<3e-8, (x,w)

Q,Y=sp.symbols('Q Y')
identity=sp.expand((Y+1)*(Q**4*Y**2+1)-Q*(Y**2+1)*(Q**2*Y+1))
assert sp.factor(identity)==(Q-1)*(Q*Y-1)*(Q**2*Y**2+Q**2*Y+2*Q*Y+Y+1)
a,b=sp.symbols('a b')
assert sp.factor((a+b)*(1+a*a*b*b)-(a*a+b*b)*(1+a*b))== (a-1)*(b-1)*(a*a*b+a*b*b+2*a*b+a+b)

c0=4*math.pi**4/9*((1-q)/(1+q))**2
ch=16*math.pi**4*q/9*(1-math.sqrt(q))**4/(1-q*q)**2
C=c0*ch/(c0+ch)
assert all(math.isfinite(z) and z>0 for z in (c0,ch,C))
for w,c in ((0,c0),(.5,ch)):
    h=1e-5
    dw=(Zak(0,w+h)-Zak(0,w-h))/(2*h)
    assert abs(abs(dw)**2/c-1)<2e-6,(w,dw,c)

for delta in (.2,.39,.52,.73):
    def ss(xx):
        x,w=xx
        return abs(Zak(x,w))**2+abs(Zak(x,w-delta))**2
    for x,w in ((0,0),(.5,0),(0,.5),(.123,.62)):
        assert ss((x,w))>=0
    if delta!=.5:
        # Finite sanity test only, not a uniform frame proof.
        vals=[ss((x,w)) for x in np.linspace(0,1,29) for w in np.linspace(0,1,31)]
        assert min(vals)>0

# Local constrained optimization after analytic global-zero classification.
for eps in (.02,.01,.005,.002):
    delta=.5+eps
    fun=lambda v: abs(Zak(v[0],v[1]))**2+abs(Zak(v[0],v[1]-delta))**2
    fit=minimize(fun,(0,ch/(c0+ch)*eps),method='BFGS',tol=2e-14,
                 options={'gtol':2e-12,'maxiter':100})
    ratio=fit.fun/(eps*eps)
    assert abs(ratio/C-1)<.07, (eps,ratio,C)
print('CHECK_OK: Fourier/Zak equality, exact algebraic zero obstructions, derivative constants and quadratic critical trend (finite sanity only)')
print('c0=',repr(c0),'ch=',repr(ch),'C=',repr(C))
