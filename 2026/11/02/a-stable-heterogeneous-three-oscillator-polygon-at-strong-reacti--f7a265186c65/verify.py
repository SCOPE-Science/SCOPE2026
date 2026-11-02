"""Exact orbit and transverse Hurwitz test for a three-site cubic oscillator network.

Requires Python 3 and SymPy. No numerical solver and no external files.
"""
import sympy as S
I=S.I
Cr=S.Rational(1,4); Ci=S.Integer(1); C=Cr+I*Ci
beta=(S.Rational(7,4), S.Rational(9,4), S.Rational(11,4))
w=(S.Integer(1),(-1+I*S.sqrt(23))/4,(-3-I*S.sqrt(23))/4)
assert S.simplify(sum(w))==0
assert [S.simplify(v*S.conjugate(v)) for v in w]==[1,S.Rational(3,2),2]
assert all(S.simplify(beta[j]-3*Cr-w[j]*S.conjugate(w[j]))==0 for j in range(3))
x=S.symbols('x0:3',real=True)
y=S.symbols('y0:3',real=True)
z=[x[j]+I*y[j] for j in range(3)]
Z=sum(z)
# Rotating at omega - 3*Ci, so the co-rotating vector field is
# (beta_j - 3*Cr - |z_j|^2)z_j + C * sum(z).
f=[(beta[j]-3*Cr-x[j]**2-y[j]**2)*z[j]+C*Z for j in range(3)]
coords=[h for j in range(3) for h in (x[j],y[j])]
field=[h for j in range(3) for h in (S.re(S.expand_complex(f[j])),S.im(S.expand_complex(f[j])))]
J=S.Matrix(field).jacobian(coords)
values={x[j]:S.re(w[j]) for j in range(3)}
values.update({y[j]:S.im(w[j]) for j in range(3)})
J=S.simplify(J.subs(values))
t=S.symbols('t')
char=S.factor(J.charpoly(t).as_expr())
target=t*(64*t**5+480*t**4+1556*t**3+3544*t**2+5325*t+3519)/64
assert S.cancel(char-target)==0
pol=S.Poly(S.cancel(char/t),t)
a=pol.all_coeffs()
H=S.zeros(5)
for i in range(1,6):
 for j in range(1,6):
  k=2*j-i
  if 0<=k<=5:H[i-1,j-1]=a[k]
D=[S.factor(H[:k,:k].det()) for k in range(1,6)]
expected=[S.Rational(15,2),S.Rational(4063,32),S.Rational(353677,128),S.Rational(2996769579,32768),S.Rational(10545632148501,2097152)]
assert D==expected and all(z>0 for z in D)
assert S.simplify(J*S.Matrix([S.re(I*v) if k%2==0 else S.im(I*v) for k,v in enumerate([w[0],w[0],w[1],w[1],w[2],w[2]])]))==S.zeros(6,1)
print('EXACT_POLYGON_AND_ROTATING_VECTOR_FIELD_PASS')
print('EXACT_JACOBIAN_AND_CHARACTERISTIC_PASS')
print('HURWITZ_MINORS',*(str(a) for a in D))
print('FIVE_NONZERO_EIGENVALUES_STRICT_LEFT_HALF_PLANE_PASS')
print('WEAK_COUPLING_AND_NONLINEAR_ORBITAL_STABILITY_REQUIRE_ANALYTICAL_ARGUMENT')
