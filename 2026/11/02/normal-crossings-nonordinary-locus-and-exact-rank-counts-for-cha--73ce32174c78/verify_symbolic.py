#!/usr/bin/env python3
"""Exact characteristic-three Ciani-Hasse and divisor identities (SymPy)."""
import sympy as S
x,y,z,r,s,t=S.symbols('x y z r s t')
F=x**4+y**4+z**4+r*x**2*y**2+s*y**2*z**2+t*z**2*x**2
P=S.Poly(S.expand(F**2),x,y,z)
B=[(1,0,0),(0,1,0),(0,0,1)]
M=S.Matrix(3,3,lambda i,j: S.Poly(P.coeff_monomial(x**(2+3*B[i][0]-B[j][0])*y**(2+3*B[i][1]-B[j][1])*z**(2+3*B[i][2]-B[j][2])),r,s,t,modulus=3).as_expr())
H=[s+r*t,t+r*s,r+s*t]
assert all(S.Poly(M[i,j]-(2*H[i] if i==j else 0),r,s,t,modulus=3).is_zero for i in range(3) for j in range(3)),M
D=r*r+s*s+t*t-r*s*t-1
assert S.Poly(D.subs(s,-r*t)+(r*r-1)*(t*t-1),r,t,modulus=3).is_zero
assert S.Poly(D.subs(t,1)-(r+s)**2,r,s,modulus=3).is_zero
assert S.Poly(D.subs(t,-1)-(r-s)**2,r,s,modulus=3).is_zero
assert S.Poly(H[1].subs(s,-r*t)-t*(1-r*r),r,t,modulus=3).is_zero
J=S.Matrix([[S.diff(h,w) for w in (r,s,t)] for h in H]);assert int(J.subs({r:0,s:0,t:0}).det())%3 !=0
# Count-polynomial identities, and the geometric involution count of the discriminant surface.
q=S.symbols('q',integer=True)
Ssing=(q-2)**2+1-2*(q-2)
Ssmooth=(q-2)**3-Ssing
N0=1;N1=3*(q-3);N2=3*(q-3)*(q-5);N3=(q-3)*(q*q-7*q+18)
assert S.expand(Ssing-(q-3)**2)==0
assert S.expand(Ssmooth-N0-N1-N2-N3)==0
assert S.expand((q-2)**2-2*(q-3)-(q*q-6*q+10))==0
print('CHAR3_CIANI_EXACT_CARTIER_SNC_AND_COUNT_IDENTITIES_OK')
