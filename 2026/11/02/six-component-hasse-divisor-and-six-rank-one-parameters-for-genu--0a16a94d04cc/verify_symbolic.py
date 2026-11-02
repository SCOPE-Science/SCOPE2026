"""Exact characteristic-five identities for the hyperelliptic Howe Hasse divisor.
Run with python verify_symbolic.py; requires sympy.
"""
import sympy as s
x,a,b,z=s.symbols('x a b z')
F=(x**4-a*x**2+1)*(x**4-b*x**2+1)
h=s.Poly(s.expand(F**2),x)
H=s.Matrix([[h.nth(5*i-j) for j in range(1,4)] for i in range(1,4)])
Q=a*a-a*b+b*b-1
P=Q+2*(a+b)
N=Q-2*(a+b)
R=a*a*b*b+2*a*a-2*a*b+2*b*b+1
mod=lambda f:s.Poly(s.expand(f),a,b,modulus=5).as_expr()
expected=s.Matrix([[Q,0,-2*(a+b)],[0,R,0],[-2*(a+b),0,Q]])
assert all(mod(H[i,j]-expected[i,j])==0 for i in range(3) for j in range(3))
assert mod(H.det()-P*N*R)==0
assert mod(P-((a+2)**2-(a+2)*(b+2)+(b+2)**2))==0
assert mod(N-((a-2)**2-(a-2)*(b-2)+(b-2)**2))==0
assert mod(R-((a*b+1)**2+2*(a-b)**2))==0
# Last identity in F_5[z]/(z^2-3): reduce first in z then modulo 5.
T=s.Poly(s.expand(R-((a-z)*(b+z)-1)*((a+z)*(b-z)-1)),z)
T=s.rem(T,s.Poly(z*z-3,z)).as_expr()
assert mod(T)==0
assert s.factor(s.resultant(P,R,b),modulus=5) == (a+2)**6*(a*a+2*a-2) or mod(s.resultant(P,R,b)-(a+2)**6*(a*a+2*a-2))==0
assert mod(s.resultant(N,R,b)-(a-2)**6*(a*a-2*a-2))==0
GPR=s.groebner([P,R,a*a+2*a-2],b,a,modulus=5)
GNR=s.groebner([N,R,a*a-2*a-2],b,a,modulus=5)
assert len(GPR.polys)==2 and len(GNR.polys)==2
assert s.Poly(GPR.reduce(a+b+2)[1],a,b,modulus=5).is_zero
assert s.Poly(GPR.reduce(a*a+2*a-2)[1],a,b,modulus=5).is_zero
assert s.Poly(GNR.reduce(a+b-2)[1],a,b,modulus=5).is_zero
assert s.Poly(GNR.reduce(a*a-2*a-2)[1],a,b,modulus=5).is_zero
assert mod((a+b+2).subs(b,-a-2))==0 and mod((a+b-2).subs(b,-a+2))==0
for U,V,relation,minpol,answer in [
 (P,R,-a-2,a*a+2*a-2,2*a+2),
 (N,R,-a+2,a*a-2*a-2,2-2*a),
 (P,N,-a,a*a-2,a)]:
 J=s.diff(U,a)*s.diff(V,b)-s.diff(U,b)*s.diff(V,a)
 residue=s.rem(s.Poly(J.subs(b,relation),a,modulus=5),s.Poly(minpol,a,modulus=5)).as_expr()
 assert s.Poly(residue-answer,a,modulus=5).is_zero
 assert s.gcd(s.Poly(residue,a,modulus=5),s.Poly(minpol,a,modulus=5)).degree()==0
assert s.groebner([P,N,R],a,b,modulus=5).polys[0].is_ground
print('HOWE_CHAR5_SYMBOLIC_HASSE_SIX_COMPONENTS_SIX_TRANSVERSE_POINTS_OK')
