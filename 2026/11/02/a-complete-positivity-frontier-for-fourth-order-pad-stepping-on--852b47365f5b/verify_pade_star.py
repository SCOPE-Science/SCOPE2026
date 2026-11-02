"""Exact and numerical checks for fourth-order Padé positivity on a weighted 3-spoke star.

Requires Python 3, sympy and numpy. No external inputs or network services.
"""
from itertools import permutations
import sympy as sp
import numpy as np

h, a, b, c = sp.symbols('h a b c', positive=True)
L = sp.Matrix([[a+b+c,-a,-b,-c],[-a,a,0,0],[-b,0,b,0],[-c,0,0,c]])
I = sp.eye(4)
D = I + h*L/2 + h**2*L**2/12
N = I - h*L/2 + h**2*L**2/12
P = D.inv()*N

def phi(x,y,z):
    return y*z*(3*y*z-x*(y+z))*h**4 + 12*y*z*(y+z-x)*h**3 + 12*(2*y*y+3*y*z+2*z*z-x*(y+z))*h**2 + 72*(y+z)*h + 144

def psi(x,y,z):
    return z*(3*z*(x+y)-x*y)*h**3 + 12*z*(x+y+z)*h**2 + 24*(x+y+2*z)*h + 72

assert sp.simplify(P*sp.ones(4,1)-sp.ones(4,1)) == sp.zeros(4,1)
assert sp.simplify(P-P.T) == sp.zeros(4)
for x,y,z in [(a,b,c),(b,a,c),(c,a,b)]:
    i = {a:1,b:2,c:3}[x]
    assert sp.cancel(432*D.det()*P[0,i] - 3*x*h*phi(x,y,z)) == 0
for i,j,k in [(1,2,3),(1,3,2),(2,3,1)]:
    x,y,z = [a,b,c][i-1],[a,b,c][j-1],[a,b,c][k-1]
    assert sp.cancel(432*D.det()*P[i,j] - 3*x*y*h*h*psi(x,y,z)) == 0
print('7 exact symbolic identities (row sums, symmetry, six offdiagonal numerators): PASS')

# Exact critical and unsafe examples, including the exact first crossing.
Pc = P.subs({a:sp.Rational(3,2),b:1,c:1})
Pu = P.subs({a:3,b:1,c:1})
assert sp.simplify(sp.limit(h*h*Pc[0,1],h,sp.oo)-3) == 0
assert sp.simplify(Pu[0,1].subs(h,1+sp.sqrt(5))) == 0
assert Pu[0,1].subs(h,4) < 0
assert Pu[0,1].subs(h,1) > 0
for i in range(4):
 for j in range(i+1,4):
  if (i,j)!=(0,1):
   num = sp.Poly(sp.together(Pu[i,j]).as_numer_denom()[0],h)
   # The claimed example has all other offdiagonal entries positive at every h>0.
   assert all(v>=0 for v in num.all_coeffs())
print('critical asymptotic and exact h=1+sqrt(5) crossing: PASS')

# Numerical direct matrix-evaluation comparisons over heterogeneous regimes.
rng=np.random.default_rng(271828)
checks=0
for k in range(90):
    w=np.exp(rng.uniform(-2.5,2.5,size=3))
    l=np.diag(np.r_[w.sum(),w]); l[0,1:]=-w; l[1:,0]=-w
    for step in (0.001,0.03,0.5,5.,50.,1000.):
        den=np.eye(4)+step*l/2+step**2*l@l/12
        nom=np.eye(4)-step*l/2+step**2*l@l/12
        mat=np.linalg.solve(den,nom)
        vals=[]
        for x,y,z in ((w[0],w[1],w[2]),(w[1],w[0],w[2]),(w[2],w[0],w[1])):
            vals.append(3*x*step*float(phi(x,y,z).subs(h,step))/(432*np.linalg.det(den)))
        assert np.allclose(mat[0,1:],vals,atol=2e-9,rtol=1e-7)
        assert np.allclose(mat.sum(axis=1),1,atol=5e-11)
        assert np.linalg.eigvalsh(mat).min()>-1e-12
        checks+=1
print(f'{checks} direct full-matrix, row-sum, and spectral comparisons: PASS')
print('All checks passed')
