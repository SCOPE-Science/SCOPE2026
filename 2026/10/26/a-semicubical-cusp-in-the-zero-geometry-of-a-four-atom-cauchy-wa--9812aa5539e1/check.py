"""Independent algebraic and numerical checks for symmetric four-atom Cauchy-wavelet zeros."""
import sympy as s
import numpy as np

w,q,t,z=s.symbols('w q t z')
P=s.expand((w+1)*(w-q)**2+t*(w+q)*(w-1)**2)
B=q**4+76*q**3-282*q**2+76*q+1
H=-8*(1+q)**3*t**2+B*t-8*q*(1+q)**3
assert s.simplify(s.discriminant(P,w)-t*(1-q)**2*H)==0
assert s.factor(s.discriminant(H,t))==(q-1)**2*(q**2-34*q+1)**3
assert s.simplify(P.subs(w,1)-2*(1-q)**2)==0
assert s.simplify(P.subs(w,q)-2*t*q*(1-q)**2)==0

r0=3-2*s.sqrt(2)
q0=s.expand(r0**2)
assert s.simplify(q0-(17-12*s.sqrt(2)))==0
assert s.simplify(P.subs({q:q0,t:r0})-(1+r0)*(w+r0)**3)==0
J=s.diff(P,q)*s.diff(P,w,t)-s.diff(P,t)*s.diff(P,w,q)
J0=s.simplify(J.subs({q:q0,t:r0,w:-r0}))
assert J0==12672-8960*s.sqrt(2) and J0>0

# Identity with the four positive pole terms on several independent points.
for qq,tt in [(s.Rational(1,100),s.Rational(1,10)),(s.Rational(1,25),s.Rational(1,5))]:
 r=s.sqrt(qq)
 R=1/(z-1)**2+1/(z+1)**2+tt/(z-r)**2+tt/(z+r)**2
 rational=2*P.subs({w:z*z,q:qq,t:tt})/((z*z-1)**2*(z*z-qq)**2)
 assert s.cancel(R-rational)==0

# Enumerate all six polynomial roots and classify the three in the upper half-plane.
# Tolerance is for numerical diagnostics only; analytical discriminant is proof.
def classify(qv,tv):
 coeff=[1+tv,1-2*qv+tv*(qv-2),qv*qv-2*qv+tv*(1-2*qv),qv*qv+tv*qv]
 roots=np.roots(coeff)
 zs=[]
 for W in roots:
  Z=np.sqrt(complex(W))
  zs.append(Z if Z.imag>0 else -Z)
 return sum(abs(Z.real)<1e-8 for Z in zs),sum(abs(Z.real)>=1e-8 for Z in zs),roots
for qv,tv,expected in [(0.01,0.1,(3,0)),(0.01,0.01,(1,2)),(0.04,0.2,(1,2)),(0.5,2,(1,2))]:
 a,b,_=classify(qv,tv)
 assert (a,b)==expected, (qv,tv,a,b)

# Exact boundary: roots t± for q=1/100 give a double and a simple negative w root.
qq=s.Rational(1,100)
tp=s.solve(H.subs(q,qq),t)
assert len(tp)==2
for T in tp:
 p1=s.Poly(P.subs({q:qq,t:T}),w)
 d=s.gcd(p1,p1.diff())
 assert d.degree()==1

# The symmetry cusp is an exact triple zero in w and consequently in z at i sqrt(r0).
cz=s.I*s.sqrt(r0)
R=s.factor(P.subs({w:z*z,q:q0,t:r0}))
assert all(s.simplify(s.diff(R,z,k).subs(z,cz))==0 for k in range(3))
assert s.simplify(s.diff(R,z,3).subs(z,cz))!=0

print('exact_discriminant_factorization: PASS')
print('exact_cusp_identity_and_transversality: PASS')
print('rational_wavelet_identity: PASS (2 parameter settings)')
print('upper_half_plane_root_regimes: PASS (4 parameter settings)')
print('two_double_root_boundary_checks: PASS')
print('triple_order_cusp: PASS')
print('critical_inner_radius:',s.sstr(r0))
print('critical_weight_ratio:',s.sstr(r0))
print('transversality_jacobian:',s.sstr(J0))
