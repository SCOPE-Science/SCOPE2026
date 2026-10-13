#!/usr/bin/env python3
import sympy as sp

x,y,z,lam = sp.symbols('x y z lam')
Q = x*z-y**2
L1 = y
L2 = x-y
L3 = x-(1+lam)*y+lam*z
L4 = y-lam*z
F = sp.expand(Q*L1*L2*L3*L4)
Fx,Fy,Fz = [sp.diff(F,v) for v in (x,y,z)]

# Explicit quadratic Jacobian syzygy.
A = -x**2 + 2*(lam+1)*x*y - lam*x*z - 2*lam*y**2
B = x*y - lam*y*z
C = x*z + 2*y**2 - 2*(lam+1)*y*z + lam*z**2
assert sp.expand(A*Fx+B*Fy+C*Fz) == 0

# No linear Jacobian syzygy for lam != 0: a coefficient minor is 108*lam^2.
coeff = sp.symbols('a0:9')
lin = [coeff[0]*x+coeff[1]*y+coeff[2]*z,
       coeff[3]*x+coeff[4]*y+coeff[5]*z,
       coeff[6]*x+coeff[7]*y+coeff[8]*z]
E = sp.Poly(sp.expand(lin[0]*Fx+lin[1]*Fy+lin[2]*Fz),x,y,z)
terms = E.terms()
mon_to_expr = {m:e for m,e in terms}
chosen = [(4,2,0),(4,1,1),(3,3,0),(3,2,1),(3,1,2),(3,0,3),(2,4,0),(2,3,1),(2,2,2)]
M,_ = sp.linear_eq_to_matrix([mon_to_expr[m] for m in chosen], coeff)
assert sp.factor(M.det()) == 108*lam**2

# The four conic-line-line triple points and two opposite-side nodes.
Pinf = sp.Matrix([1,0,0])
P0   = sp.Matrix([0,0,1])
P1   = sp.Matrix([1,1,1])
Plam = sp.Matrix([lam**2,lam,1])
N13  = sp.Matrix([-lam,0,1])
N24  = sp.Matrix([lam,lam,1])

def ev(poly,P):
    return sp.factor(poly.subs({x:P[0],y:P[1],z:P[2]}))
for P, polys in [
    (Pinf,[Q,L1,L4]),
    (P0,[Q,L1,L2]),
    (P1,[Q,L2,L3]),
    (Plam,[Q,L3,L4]),
    (N13,[L1,L3]),
    (N24,[L2,L4]),
]:
    assert all(ev(f,P)==0 for f in polys)
assert ev(Q,N13) == -lam
assert sp.expand(ev(Q,N24)-lam*(1-lam)) == 0

# Every chord line has exactly its named pair as intersection with the conic.
t=sp.symbols('t')
param={x:t**2,y:t,z:1}
assert sp.factor(L1.subs(param)) == t
assert sp.factor(L2.subs(param)) == t*(t-1)
assert sp.factor(L3.subs(param)) == (t-1)*(t-lam)
assert sp.factor(L4.subs(param)) == t-lam
# P_infinity is the missing parameter point for L1 and L4, checked homogeneously above.

# Source example C6 has harmonic four-point set under the standard circle parametrization.
s,u=sp.symbols('s u')
X=4*(s**2-u**2); Y=8*s*u; Z=s**2+u**2
assert sp.expand(X**2+Y**2-16*Z**2)==0
# Parameters 0,1,infinity,-1 map to the four cardinal triple points.
assert [sp.Matrix([X.subs({s:1,u:v}),Y.subs({s:1,u:v}),Z.subs({s:1,u:v})]) for v in [0,1,-1]] == [sp.Matrix([4,0,1]),sp.Matrix([0,8,2]),sp.Matrix([0,-8,2])]
assert sp.Matrix([X.subs({s:0,u:1}),Y.subs({s:0,u:1}),Z.subs({s:0,u:1})]) == sp.Matrix([-4,0,1])

# Nearly-free numerical identity for degree 6, r=2, tau=4*4+2.
tau=18
assert 2**2-2*(6-1)+(6-1)**2 == tau+1
print('VERIFY_OK')
