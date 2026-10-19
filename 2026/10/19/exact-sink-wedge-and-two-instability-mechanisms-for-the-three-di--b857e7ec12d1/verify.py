"""Exact algebra and finite supplementary checks for a three-dimensional quadratic map.

Requires Python 3 and SymPy. Algebraic identities hold symbolically;
finite spectral tests illustrate, but do not establish, the continuum claim.
"""
import sympy as sp

S, D, T, A = sp.symbols('S D T A', real=True)
L = sp.Symbol('lam')
Q = 1 + S + D
alpha_star = -Q * (3 + 3*S - D) / 4
u = -Q / 2 + T
v = -Q / 2 - T
alpha = alpha_star - T**2
F = lambda p: sp.Matrix([D*p[2] + alpha - S*p[1] + p[0]**2, p[0], p[1]])
J = lambda r: sp.Matrix([[2*r, -S, D], [1, 0, 0], [0, 1, 0]])
p = sp.Matrix([u, v, u]); q = sp.Matrix([v, u, v])
assert all(sp.simplify(x) == 0 for x in F(p)-q)
assert all(sp.simplify(x) == 0 for x in F(q)-p)
M = sp.expand(J(v)*J(u))
E = S**2 + 2*D*Q
trace = 1 + E - D**2 - 4*T**2
poly = L**3 - trace*L**2 + E*L - D**2
assert sp.simplify(M.charpoly(L).as_expr() - poly) == 0
assert sp.simplify(M.det()-D**2) == 0
assert sp.factor(poly.subs(T, 0).subs(L, 1)) == 0
assert sp.simplify(E - ((S + D)**2 + 2*D + D**2)) == 0

# The Schur-reduced quadratic has leading A2, linear B2 and constant C2.
A2=1-D**4
B2=-trace+D**2*E
C2=E-D**2*trace
assert sp.simplify(A2+B2+C2-4*(1+D**2)*T**2) == 0
assert sp.simplify(A2-B2+C2-(1-D**2)*(2+2*E-4*T**2)) == 0
assert sp.factor(A2-C2 - ((1-D**2)*(1+S)*(1-S-2*D)-4*D**2*T**2)) == 0
assert sp.simplify((A2-C2).subs(T,0)-(1-D**2)*(1+S)*(1-S-2*D)) == 0

Wflip=(1+E)/2
Wns=(1-D**2)*(1+S)*(1-S-2*D)/(4*D**2)
assert sp.simplify(A2-B2+C2-4*(1-D**2)*(Wflip-T**2)) == 0
assert sp.simplify(A2-C2-4*D**2*(Wns-T**2)) == 0
assert sp.simplify(E-(1-2*D**2)-((S+D)**2+(3*D-1)*(D+1)))==0

# At the simultaneous boundary the squared return has two multipliers -1.
# One rational instance is the unique tangency at D=1/3, S=-1/3.
assert sp.simplify(poly.subs({D:sp.Rational(1,3),S:sp.Rational(-1,3),T:sp.sqrt(sp.Rational(8,9))})-(L+1)**2*(L-sp.Rational(1,9))) == 0

samples=[(sp.Rational(1,20),sp.Rational(-2913,10000)),
         (sp.Rational(7,10),sp.Rational(-815,1000)),
         (sp.Rational(1,3),sp.Rational(-1,3)),
         (sp.Rational(1,10),sp.Rational(0)),
         (sp.Rational(1,5),sp.Rational(-9,10)),
         (sp.Rational(1,2),sp.Rational(-9,10)),
         (sp.Rational(4,5),sp.Rational(-9,10))]
checks=0
for d,s in samples:
  ed=E.subs({D:d,S:s}); wf=Wflip.subs({D:d,S:s}); wn=Wns.subs({D:d,S:s})
  stable_strip = (-1<s<1-2*d)
  for r in (sp.Rational(1,10000), sp.Rational(1,100), sp.Rational(1,5), sp.Rational(1,2), sp.Rational(1), sp.Rational(3)):
    pp=sp.Poly(poly.subs({D:d,S:s,T:sp.sqrt(r)}),L)
    eigs = [complex(z) for z in pp.nroots(maxsteps=100)]
    predicted=bool(stable_strip and r<min(wf,wn))
    observed=all(abs(x)<1-1e-9 for x in eigs)
    assert predicted==observed,(d,s,r,eigs,predicted)
    checks+=1
  # Verify exact two-point recurrence at a nonzero rational amplitude.
  pval=p.subs({D:d,S:s,T:sp.Rational(1,7)})
  qval=q.subs({D:d,S:s,T:sp.Rational(1,7)})
  assert F(p).subs({D:d,S:s,T:sp.Rational(1,7)}) == qval
  assert F(q).subs({D:d,S:s,T:sp.Rational(1,7)}) == pval
  checks+=2

for d in [sp.Rational(1,100),sp.Rational(1,5),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(7,10),sp.Rational(9,10)]:
  left=E.subs({D:d,S:-1}); right=E.subs({D:d,S:1-2*d})
  assert left==right==1+2*d*d
  low=E.subs({D:d,S:-d})
  assert low==2*d+d*d
  checks+=2

print('PASS: exact map recurrence, return polynomial, Schur reductions, boundary factorizations;')
print('PASS:',checks,'rational-parameter recurrence and finite spectral checks')
