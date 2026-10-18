"""Independent numerical checks of fixed-velocity resetting onset susceptibility.
Requires numpy, scipy, sympy. No external data or other files.
"""
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq
from scipy.sparse import diags, bmat, eye
from scipy.sparse.linalg import spsolve
from scipy.special import eval_hermitenorm
import sympy as sp

x=sp.symbols('x')
xcrit=float(1-1/sp.sqrt(5))
m0=x-x*x/2
s0=sp.Rational(2,3)*x-x**3/3+x**4/12
base=sp.expand(s0-2*m0*m0)
base_prime=float(sp.diff(base,x).subs(x,1-1/sp.sqrt(5)))
assert sp.simplify(base.subs(x,1-1/sp.sqrt(5))) == 0
assert sp.simplify(sp.diff(base,x).subs(x,1-1/sp.sqrt(5))+2*sp.sqrt(5)/15) == 0

# Exact zero-relaxation calculation via two Dirichlet/Neumann Poisson inverses.
m1_zero=x/sp.Integer(2)-x*x/sp.Integer(2)+x**3/6
h_zero=5*x/sp.Integer(12)-x*x/3+x**4/12-x**5/60
primitive=sp.integrate(m1_zero,x)
n_zero=sp.integrate(primitive.subs(x,1)-primitive,x)
g_zero=sp.expand(h_zero+2*n_zero-4*m0*m1_zero)
assert sp.simplify(g_zero.subs(x,1-1/sp.sqrt(5))-8*sp.sqrt(5)/1875)==0
assert sp.simplify(-g_zero.subs(x,1-1/sp.sqrt(5))/sp.diff(base,x).subs(x,1-1/sp.sqrt(5))-sp.Rational(4,125))==0


def response_green(eta,z):
    k=np.sqrt(eta)
    def G(t):
        a=min(z,t); b=max(z,t)
        return np.sinh(k*a)*np.cosh(k*(1-b))/(k*np.cosh(k))
    def R(fun):
        return quad(lambda t: G(t)*fun(t), 0,z,epsabs=1e-12)[0]+quad(lambda t:G(t)*fun(t),z,1,epsabs=1e-12)[0]
    m=R(lambda t:1-t)
    # A second resolvent integral: independent nested integration.
    def Rm(t):
        def g(y):
            return np.sinh(k*min(t,y))*np.cosh(k*(1-max(t,y)))/(k*np.cosh(k))
        return quad(lambda y:g(y)*(1-y),0,t,epsabs=1e-11)[0]+quad(lambda y:g(y)*(1-y),t,1,epsabs=1e-11)[0]
    s=R(lambda t:2/3-t*t+t**3/3+2*Rm(t))
    return - (s-4*(z-z*z/2)*m)/base_prime


def response_elementary(eta,z):
    """Closed elementary resolvent and derivative formula, checked independently."""
    k=np.sqrt(eta)
    # functions of k for central finite diff via complex-step differentiation
    def m(K):
        return ((1-z)/K**2 + np.sinh(K*z)/(K**3*np.cosh(K))
                -np.cosh(K*(1-z))/(K**2*np.cosh(K)))
    def h(K):
        return ((2/3-z*z+z**3/3)/K**2+(2*z-2)/K**4
             -(2/(3*K**2)-2/K**4)*np.cosh(K*(1-z))/np.cosh(K)
             +(1/K**3-2/K**5)*np.sinh(K*z)/np.cosh(K))
    dm=np.imag(m(k+1e-15j))/1e-15
    g=h(k)-dm/k-4*(z-z*z/2)*m(k)
    return -g/base_prime

# Quantities computed by a full two-dimensional moment-system discretization
# in a Hermite basis of the OU variable (not by differentiating the above formulas).
def root_from_full_equations(eta,alpha,M=220,N=7):
    dx=1/M
    d2=diags([np.ones(M-1),-2*np.ones(M),np.ones(M-1)],[-1,0,1],shape=(M,M),format='lil')/dx**2
    d2[M-1,M-2]=2/dx**2
    d1=diags([-np.ones(M-1),np.ones(M-1)],[-1,1],shape=(M,M),format='lil')/(2*dx)
    d1[M-1,:]=0
    A=[]
    for n in range(N):
        row=[]
        for p in range(N):
            if p==n: b=(-d2+n*eta*eye(M)).tocsr()
            elif p==n-1: b=(-alpha*d1).tocsr()
            elif p==n+1: b=(-alpha*(n+1)*d1).tocsr()
            else: b=None
            row.append(b)
        A.append(row)
    A=bmat(A,format='csc')
    rhs=np.zeros(M*N); rhs[:M]=1
    moment1=spsolve(A,rhs)
    moment2=spsolve(A,2*moment1)
    xx=np.arange(1,M+1)/M
    y0=1
    c=np.array([eval_hermitenorm(n,y0) for n in range(N)])
    mm=sum(c[n]*moment1[n*M:(n+1)*M] for n in range(N))
    ss=sum(c[n]*moment2[n*M:(n+1)*M] for n in range(N))
    gg=ss-2*mm*mm
    interp=PchipInterpolator(np.r_[0,xx],np.r_[0,gg])
    return brentq(interp,.35,.7,xtol=1e-11)

for eta in [0.05,0.1,0.3,1,3,10]:
    a=response_green(eta,xcrit)
    b=response_elementary(eta,xcrit)
    assert abs(a-b)<3e-10, (eta,a,b)
    print(f'green-versus-elementary eta={eta}: chi={a:.12g}, diff={a-b:.2e}')
for eta in [.05,1,10]:
    alpha=.018
    xp=root_from_full_equations(eta,alpha)
    xm=root_from_full_equations(eta,-alpha)
    fd=(xp-xm)/(2*alpha)
    true=response_green(eta,xcrit)
    print(f'full-Hermite eta={eta}, chi={true:.9g}, FD={fd:.9g}, error={fd-true:.3g}')
    assert abs(fd-true)<.00045
print('all checks passed')
