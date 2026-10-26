"""Independent finite symbolic/numerical checks of a circular Weyl-sampling theorem.
Run: python verify.py. SymPy, NumPy and SciPy are required.
These checks do not replace the proof for arbitrary cutoffs or radii.
"""
from fractions import Fraction
from math import factorial, sqrt, exp
import numpy as np
import sympy as s
from scipy.integrate import quad
from scipy.special import eval_hermite, eval_genlaguerre
x=s.symbols('x')

def block(n,m,nodes):
    return s.Matrix([[s.assoc_laguerre(j,m,t) for j in range(n-m+1)] for t in nodes])

def rank_from_modes(n,nodes):
    k=len(nodes)
    radial=s.Matrix([[s.laguerre(j,t) for j in range(n+1)] for t in [s.Integer(0)]+nodes])
    # Trace known is represented by the polynomial at radius zero.
    return radial.rank()+2*sum(block(n,m,nodes).rank() for m in range(1,n+1))

checks=0
for n in range(0,8):
    for k in range(n+1):
        for nodes in ([s.Rational(2*j+1,5) for j in range(k)],
                      [s.Rational(j+1,2)+s.Rational(j*j,7) for j in range(k)]):
            assert len(set(nodes))==k and all(t>0 for t in nodes)
            observed=rank_from_modes(n,nodes)
            expected=(n+1)**2-((n+1-k)**2-1)
            assert observed==expected,(n,k,observed,expected)
            checks+=1
print('exact Laguerre-block rank checks:',checks)

# Explicit density-matrix ambiguity at cutoff n=3 with k=2 distinct circles.
n=3
nodes=[s.Rational(1,2),s.Rational(7,3)]
Q=s.expand(x*s.prod(x-t for t in nodes))
cs=s.symbols('c0:4')
sol=s.solve(s.Poly(sum(cs[j]*s.laguerre(j,x) for j in range(4))-Q,x).coeffs(),cs)
h=s.Matrix.diag(*[sol[c] for c in cs]); assert s.trace(h)==0
assert all(sum(h[j,j]*s.laguerre(j,t) for j in range(n+1))==0 for t in nodes)
base=s.eye(4)/4
norm=float(max(abs(t) for t in list(h.diagonal())))
eps=s.Rational(1,1000)/(1+int(norm))
p=base+eps*h; m=base-eps*h
assert all(v>0 for v in p.diagonal()) and all(v>0 for v in m.diagonal())
assert p!=m and s.trace(p)==s.trace(m)==1
print('explicit two-circle indistinguishable positive states at cutoff three: PASS')

# Numerical independent quadrature for the Weyl matrix elements.
def hermite(j,t):
    return eval_hermite(j,t)*np.exp(-t*t/2)/(np.pi**.25*np.sqrt(2**j*factorial(j)))
def numeric_displacement(a,b,z):
    q=np.sqrt(2)*z.real
    momentum=np.sqrt(2)*z.imag
    def f(t):
        return hermite(a,t)*hermite(b,t-q)*np.exp(1j*momentum*(t-q/2))
    v=quad(lambda t:f(t).real,-12,12,epsabs=2e-11)[0]
    w=quad(lambda t:f(t).imag,-12,12,epsabs=2e-11)[0]
    return v+1j*w
errs=[]
for z in [0.4+0.2j,-0.3+0.6j,0.9-0.5j]:
    for a in range(5):
      for b in range(a+1):
        analytic=exp(-abs(z)**2/2)*sqrt(factorial(b)/factorial(a))*(z**(a-b))*eval_genlaguerre(b,a-b,abs(z)**2)
        numeric=numeric_displacement(a,b,z)
        errs.append(abs(analytic-numeric))
assert max(errs)<1e-8, max(errs)
print('independent Hermite-displacement integral comparisons:',len(errs),'max error %.3g'%max(errs))

# Angular sampling: half-circle samples plus symmetry recover each entire circle.
n=4
rho=np.array([[complex((i+1)*(j+2)/100,(i-j)/100) for j in range(n+1)] for i in range(n+1)])
rho=(rho+rho.conj().T)/2

def chi(z):
    total=0j
    for j in range(n+1):
      total+=rho[j,j]*eval_genlaguerre(j,0,abs(z)**2)
    for mm in range(1,n+1):
      for j in range(n-mm+1):
        v=rho[j,j+mm]*sqrt(factorial(j)/factorial(j+mm))*z**mm*eval_genlaguerre(j,mm,abs(z)**2)
        total+=v+((-1)**mm)*np.conjugate(v)
    return np.exp(-abs(z)**2/2)*total
r=1.13
M=2*n+2
half=[chi(r*np.exp(1j*2*np.pi*j/M)) for j in range(M//2)]
full=np.array(half+[np.conjugate(v) for v in half])
coeff=np.fft.fft(full)/M
# Trigonometric polynomial frequency support |m|<=n; m=M/2 is absent.
assert abs(coeff[M//2])<1e-10
for theta in np.linspace(0,2*np.pi,37):
    rekon=sum(coeff[j]*np.exp(1j*j*theta) for j in range(n+1))
    rekon+=sum(coeff[M-j]*np.exp(-1j*j*theta) for j in range(1,n+1))
    assert abs(rekon-chi(r*np.exp(1j*theta)))<1e-9
print('half-circle angular-grid reconstruction: PASS')
print('ALL CHECKS PASS')
