"""Symbolic checks for a quadratic flow's recurrence-obstruction proof.
Execute with Python 3 and SymPy: python verify.py.
The global assertions require the analytical proof in RESULT.md.
"""
import sympy as sp
x,y,z,a,b,L=sp.symbols('x y z a b L', real=True)
F=sp.Matrix([y, -x+y*z, z+a*x**2-y**2-b])
E=(x**2+y**2)/2
assert sp.expand(sp.diff(E,x)*F[0]+sp.diff(E,y)*F[1]-y**2*z)==0
assert sp.expand(F[2]-z-(a*x*x-y*y-b))==0
J=F.jacobian([x,y,z]); char=sp.factor((L*sp.eye(3)-J.subs({x:0,y:0,z:b})).det())
assert sp.simplify(char-(L-1)*(L**2-b*L+1))==0
# On a hypothetical z=0, y!=0 invariant arc, x' = y, y'=-x.
G=a*x*x-y*y-b
Gdot0=sp.expand(sp.diff(G,x)*y+sp.diff(G,y)*(-x))
assert sp.simplify(Gdot0-2*(a+1)*x*y)==0
assert sp.expand(G.subs({a:-1}) + x*x+y*y+b)==0
print('PASS: energy law, unstable-filter law, spectrum, invariant-subset algebra')
