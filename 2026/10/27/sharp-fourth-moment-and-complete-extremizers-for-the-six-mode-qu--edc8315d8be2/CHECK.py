"""Reproducible exact-algebra and finite diagnostic checks for a six-mode Fourier norm.

Requires Python 3 and SymPy. Finite samples corroborate rather than prove sharpness.
"""
from collections import defaultdict
from itertools import product
from math import cos, pi, sin
import random
import sympy as sp

A,B,C,D,E,F=sp.symbols('A B C D E F', real=True)
coeffs=[A,B,C,D,E,F]
support=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
conv=defaultdict(lambda:sp.S(0))
for i,p in enumerate(support):
    for j,q in enumerate(support):
        conv[(p[0]+q[0],p[1]+q[1])]+=coeffs[i]*coeffs[j]
quartic=sp.expand(sum(x*x for x in conv.values()))
U=A*A+D*D+F*F
V=B*B+C*C+E*E
T=A*D*B**2+A*F*C**2+D*F*E**2
formula=2*U**2-(A**4+D**4+F**4)+2*V**2-(B**4+C**4+E**4)+4*U*V+4*T+8*(A+D+F)*B*C*E
assert sp.expand(quartic-formula)==0, 'Fourier convolution expansion'

Da=A**4+D**4+F**4-U**2/sp.Integer(3)
Db=B**4+C**4+E**4-V**2/sp.Integer(3)
sos=((A*A+E*E-(U+V)/3)**2+(D*D+C*C-(U+V)/3)**2
      +(F*F+B*B-(U+V)/3)**2
      +2*(B**2*(A-D)**2+C**2*(A-F)**2+E**2*(D-F)**2))
assert sp.expand(Da+Db+sp.Rational(4,3)*U*V-4*T-sos)==0, 'Exact SOS mass inequality'

x,t,K=sp.symbols('x t K',real=True)
equal=sp.factor(formula.subs({A:x,D:x,F:x,B:t*x,C:t*x,E:t*x})/ (3*x*x*(1+t*t))**2)
r=(5*t**4+8*t**3+16*t**2+5)/(3*(1+t*t)**2)
assert sp.factor(equal-r)==0,'Corner-edge equal amplitude reduction'
cubic=2*t**3+3*t*t-6*t-3
assert sp.factor(sp.diff(r,t)+4*t*cubic/(3*(1+t*t)**3))==0,'Stationarity cubic'
assert cubic.subs(t,sp.Rational(14022557,10000000))<0
assert cubic.subs(t,sp.Rational(14022559,10000000))>0
assert sp.factor(sp.resultant(cubic,3*K*(1+t*t)**2-(5*t**4+8*t**3+16*t**2+5),t)/100)==2700*K**3-15768*K**2+28359*K-15749
root=float(sp.nroots(cubic)[-1]); ratio=float(r.subs(t,root))
assert 2.94923561205<ratio<2.94923561206

# Direct complex Fourier coefficient convolution identity and sampled spatial mean.
def exact_moment(vals):
    cv=defaultdict(complex)
    for i,p in enumerate(support):
        for j,q in enumerate(support):
            cv[(p[0]+q[0],p[1]+q[1])]+=vals[i]*vals[j]
    return sum(abs(a)**2 for a in cv.values())
def grid_moment(vals,n,m):
    sm=0.
    for i in range(n):
        z=complex(cos(2*pi*i/n),sin(2*pi*i/n))
        for j in range(m):
            w=complex(cos(2*pi*j/m),sin(2*pi*j/m))
            sm+=abs(sum(a*z**p*w**q for a,(p,q) in zip(vals,support)))**4
    return sm/(n*m)
rng=random.Random(17329)
for _ in range(25):
    vals=[complex(rng.randrange(-3,4),rng.randrange(-3,4)) for i in range(6)]
    E4=exact_moment(vals)
    E2=sum(abs(z)**2 for z in vals)
    assert E4<=ratio*E2*E2+1e-6, 'Test sharp norm'
    for n,m in [(5,5),(5,6),(7,8)]:
        assert abs(grid_moment(vals,n,m)-E4)<1e-8*max(1,E4),'Finite-grid no aliasing'

for theta,phi in [(0,0),(0.21,-0.67),(2.1,1.3)]:
    import cmath
    vals=[1,root*cmath.exp(1j*theta),root*cmath.exp(1j*phi),
          cmath.exp(2j*theta),root*cmath.exp(1j*(theta+phi)),cmath.exp(2j*phi)]
    assert abs(exact_moment(vals)/(sum(abs(z)**2 for z in vals)**2)-ratio)<2e-12

print('PASS: exact convolution expansion, exact SOS, derivative and resultant identities,')
print('      rational root isolation, 75 discrete quadrature comparisons,')
print('      25 sample norm checks, 3 independent extremizing phase tests.')
print('t = %.15f, K = %.15f'%(root,ratio))
