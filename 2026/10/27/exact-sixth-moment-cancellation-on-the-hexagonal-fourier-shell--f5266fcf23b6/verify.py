"""Independent exact checks of the six-mode hexagonal Fourier moment identity.
Requires Python 3, SymPy, NumPy. No external data or network is used.
"""
from collections import defaultdict
from itertools import product
import sympy as sp
import numpy as np

X=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
u,v,w=sp.symbols('u v w', nonzero=True)
a=(sp.Integer(1),sp.Integer(1),sp.Integer(1),u,v,w)
b=(sp.Integer(1),sp.Integer(1),sp.Integer(1),1/u,1/v,1/w)
triple=defaultdict(lambda:sp.Integer(0)); triplebar=defaultdict(lambda:sp.Integer(0))
for i,j,k in product(range(6),repeat=3):
    s=tuple(X[i][h]+X[j][h]+X[k][h] for h in (0,1))
    triple[s]+=a[i]*a[j]*a[k]
    triplebar[s]+=b[i]*b[j]*b[k]
assert len(triple)==37
M=sp.expand(sum(triple[s]*triplebar[s] for s in triple))
q=1+u/v+w/v
qbar=1+v/u+v/w
h=u*w/v
rhs=sp.expand(546+126*q*qbar+9*(1+q*qbar)*(2+h+1/h))
assert sp.cancel(M-rhs)==0, 'exact all-Laurent identity failed'
assert sp.expand(M).subs({u:1,v:1,w:1})==2040
omega=sp.Rational(-1,2)+sp.sqrt(3)*sp.I/2
p={u:-omega,v:-1,w:-omega**2}
assert sp.simplify(q.subs(p))==0
assert sp.simplify(h.subs(p))==-1
assert sp.simplify(M.subs(p))==546
p2={u:-omega**2,v:-1,w:-omega}
assert sp.simplify(M.subs(p2))==546
assert sp.Matrix([[1,*X[i]] for i in range(3)]).det()==1
# On the 31x31 torus, every nonzero Fourier mode of |P|^6 integrates exactly to zero.
# This independently checks Fourier normalization and enumeration in floating point.
angles=np.arange(31)*2*np.pi/31
T,S=np.meshgrid(angles,angles,indexing='ij')
phasesets=[(0,0,0),(np.pi/3,np.pi,-np.pi/3),(0.38,1.13,-2.1)]
fun=sp.lambdify((u,v,w),M,'numpy')
for ph in phasesets:
    cf=np.array([1,1,1,*np.exp(1j*np.array(ph))]); P=sum(cf[i]*np.exp(1j*(x*T+y*S)) for i,(x,y) in enumerate(X))
    qd=float(np.mean(abs(P)**6)); expected=float(np.real(fun(*cf[3:])))
    assert abs(qd-expected)<1e-9,(qd,expected)
print('PASS: 37 triple sums; exact all-coefficient Laurent identity; min 546/max 2040; roots and unimodular gauge; 3 exact-grid quadratures.')
