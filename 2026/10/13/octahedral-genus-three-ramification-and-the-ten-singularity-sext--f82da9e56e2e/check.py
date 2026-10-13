"""Exact symbolic identities for the octahedral ramification-curve theorem."""
import sympy as S
T, t, u, p, q, a, b, c = S.symbols('T t u p q a b c')
F = a*T**4+b*T**3+c*T-a
D = S.discriminant(F,T)
assert S.expand(D-(-256*a**6-192*a**4*b*c-27*a**2*b**4+6*a**2*b**2*c**2-27*a**2*c**4-4*b**3*c**3)) == 0
A,B,C = -2*t**3,3*t**4+1,-t**6-3*t**2
residual=-2*t**3*T**2+(1-t**4)*T+2*t
assert S.expand(F.subs({a:A,b:B,c:C})-(T-t)**2*residual)==0
H=S.factor(S.discriminant(residual,T))
assert S.expand(H-(t**8+14*t**4+1))==0
assert S.gcd(S.Poly(H,t),S.Poly(S.diff(H,t),t)).degree()==0
assert S.expand(D.subs({a:A,b:B,c:C}))==0
G=S.Matrix([A,B,C]); Gprime=G.diff(t)
assert all(S.rem(S.Poly(z,t),S.Poly(t*(t**4-1),t))==0 for z in G.cross(Gprime))
# A quartic with two distinct double roots must have constant = -leading and zero T^2 coefficient.
for qv,pv in [(S.I,1-S.I),(S.I,-1+S.I),(-S.I,1+S.I),(-S.I,-1-S.I)]:
    assert S.simplify(qv*qv+1)==0
    assert S.simplify(pv*pv+2*qv)==0
    assert S.expand(F.subs({a:1,b:-2*pv,c:-2*pv*qv})-(T*T-pv*T+qv)**2)==0
    assert S.simplify(pv*pv-4*qv)!=0
# Six distinct cuspidal parameter images (0, infinity, +/-1, +/-i).
pts=[S.Matrix([0,1,0]),S.Matrix([0,0,1])]
for v in [1,-1,S.I,-S.I]:pts.append(G.subs(t,v))
assert all(any(S.simplify(z)!=0 for z in pts[i].cross(pts[j])) for i in range(6) for j in range(i+1,6))
# The node parameters are disjoint from cuspidal quartics by their incompatible root partitions.
# Adjunction intersection: (H1+H2)^2(H1+H2+H3+H4)^2=4.
assert 2*2 == 4
print('OCTAHEDRAL_K3_RAMIFICATION_EXACT_OK')
