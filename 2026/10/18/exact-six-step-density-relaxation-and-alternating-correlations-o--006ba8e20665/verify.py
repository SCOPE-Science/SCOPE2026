"""Exact symbolic checks for the golden-mean tent map (SymPy required).

The accompanying proof establishes the functional invariant space and the
transfer formula. This program independently checks every algebraic identity.
"""
import sympy as s

sqrt5 = s.sqrt(5)
phi = (1 + sqrt5)/2
lo, mid, hi = (phi-1)/2, s.Rational(1,2), phi/2
simp = lambda z: s.simplify(s.radsimp(z))
P = s.Matrix([[0, 1/phi, 0, 1/phi],
              [1/phi, 1/phi, 0, 1/phi],
              [0, 0, 0, -1/phi**2],
              [0, 0, 1/phi**2, -1/phi**2]])
J = s.Matrix([mid-lo, hi-mid, (mid**2-lo**2)/2, (hi**2-mid**2)/2])
r = 2/(3-phi)
R = s.Matrix([r, phi*r, 0, 0])
assert all(simp(v)==0 for v in P*R-R)
assert simp((J.T*R)[0]-1)==0
assert all(simp(v)==0 for v in J.T*P-J.T)
assert all(simp(v)==0 for v in P**6-phi**(-12)*s.eye(4)-(1-phi**(-12))*R*J.T)
assert all(simp(v)==0 for v in P**6*P-P*P**6)

z = s.Symbol('z')
char_expected = (z-1)*(z+phi**(-2))*(z**2+phi**(-2)*z+phi**(-4))
assert simp(P.charpoly(z).as_expr()-char_expected)==0

mean = simp((s.Matrix([(mid**2-lo**2)/2,(hi**2-mid**2)/2,(mid**3-lo**3)/3,(hi**3-mid**3)/3]).T*R)[0])
assert simp(mean - (s.Rational(1,4) + 3*sqrt5/20))==0
v=s.Matrix([-mean*r,-mean*phi*r,r,phi*r])
assert simp((J.T*v)[0])==0
H=s.Matrix([(mid**2-lo**2)/2-mean*(mid-lo),
            (hi**2-mid**2)/2-mean*(hi-mid),
            (mid**3-lo**3)/3-mean*(mid**2-lo**2)/2,
            (hi**3-mid**3)/3-mean*(hi**2-mid**2)/2])
a=(3-sqrt5)/40
b=(7-3*sqrt5)/60
cycle=[a,-s.Rational(1,30),s.Rational(1,30),-a,b,-b]
for n in range(18):
    val=simp((H.T*(P**n)*v)[0])
    assert simp(val-phi**(-2*n)*cycle[n%6])==0,(n,val)
assert all(simp(x)==0 for x in P**6*v-phi**(-12)*v)
assert a>0 and b>0
print('PASS: 4x4 Perron-Frobenius matrix, stationarity, mass, sixth-step exact projection, eigenpolynomial, mean, 18 exact covariance coefficients, six-sign cycle.')
