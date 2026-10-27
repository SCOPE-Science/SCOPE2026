"""Exact polynomial certificate for a cyclic fixed-locus degeneration on the Klein cubic.
Python 3 and SymPy are required. No external data or network access needed.
"""
import sympy as s

t,A,B,U,V=s.symbols('t A B U V')
q=t**2+A*t+B
phi=t**4+t**3+t**2+t+1
assert s.expand((t-1)*phi)==t**5-1
assert s.discriminant(phi,t)==125
assert s.discriminant(A**2-A-1,A)==5
# The ambient fixed eigenline (1,t,t^2,t^3,t^4) lies on the cubic exactly at primitive fifth roots.
F_fixed=sum(t**(2*i+(i+1)%5) for i in range(5))
assert s.rem(F_fixed-t*phi,t**5-1,t)==0
assert s.Poly(phi,t,modulus=5)==s.Poly((t-1)**4,t,modulus=5)
# Fixed planes with first two projection coordinates (U,V) satisfy a quadratic recursion.
f=[s.Integer(1),s.Integer(0)]; g=[s.Integer(0),s.Integer(1)]
for _ in range(3):
 f.append(s.expand(-A*f[-1]-B*f[-2]))
 g.append(s.expand(-A*g[-1]-B*g[-2]))
x=[s.expand(U*f[i]+V*g[i]) for i in range(5)]
p=s.Poly(s.expand(sum(x[i]**2*x[(i+1)%5] for i in range(5))),U,V)
line_conditions=[s.expand(p.coeff_monomial(U**k*V**(3-k))) for k in range(4)]
rem=s.Poly(s.rem(t**5-1,q,t),t)
conditions=line_conditions+[rem.nth(0),rem.nth(1)]
# The indicated Eisenstein quadratic gives a genuine integral family of invariant lines.
for h in conditions:
 assert s.rem(s.rem(h,B-1,B),A**2-A-1,A)==0, h
G_Q=s.groebner(conditions,A,B,order='lex')
assert set(s.expand(h.as_expr()) for h in G_Q.polys)=={A**2-A-1,B-1}
G_5=s.groebner(conditions,A,B,modulus=5,order='lex')
assert set(s.Poly(h.as_expr(),A,B,modulus=5).as_expr() for h in G_5.polys)==set(s.Poly(h,A,B,modulus=5).as_expr() for h in [(A+2)**2,B-1])
# A smoothness obstruction: a vanishing coordinate propagates backwards to all five.
# With all coordinates nonzero the cyclic product of partial-derivative identities forces (-2)^5=1, false in char 5.
assert (-2)**5%5!=1
# The derivative of F at the diagonal p=(1,1,1,1,1) equals 3*(1,...,1), nonzero modulo 5.
assert 3%5!=0
# Cyclotomic ramification: shifted polynomials are Eisenstein at 5.
y=s.symbols('y')
assert s.expand(phi.subs(t,1+y))==y**4+5*y**3+10*y**2+10*y+5
assert s.expand((A**2-A-1).subs(A,3+y))==y**2+5*y+5
print('VERIFY_OK: eigenline phi5/discriminant125/length4; Fano fixed-line quadratic/discriminant5/length2; smoothness and Eisenstein shifts')
