"""Independent symbolic verification of the complete quartic candidate certificate.
Requires SymPy. Does not import or use classify.py.
"""
import itertools, json
from pathlib import Path
import sympy as S
X,Y,Z=S.symbols('X Y Z')
variables=(X,Y,Z)
mon=[(i,j,4-i-j) for i in range(5) for j in range(5-i)]
forms=[X**i*Y**j*Z**k for i,j,k in mon]
certificate=json.loads(Path(__file__).with_name('classification.json').read_text())
candidates=certificate['zero_transverse_candidates']

def polynomial(m):return sum(forms[i] for i in range(15) if m & (1<<i))

def squarefree_binary(f):
    t=S.symbols('t')
    # Homogeneous binary form f(u,v), substitute v=1.
    p=S.Poly(f.subs({S.Symbol('v'):1,S.Symbol('u'):t}),t,modulus=2)
    if p.is_zero or p.degree()<3: return False
    return S.gcd(p,p.diff()).degree()==0

# Independently enumerate the seven line embeddings as 2D rational subspaces.
points=[p for p in itertools.product((0,1),repeat=3) if any(p)]
U,V=S.symbols('u v')
lines=[]
for linear in points:
    pts=[p for p in points if sum(a*b for a,b in zip(p,linear))%2==0]
    assert len(pts)==3
    lines.append((linear,pts[0],pts[1]))

for mask in candidates:
    F=polynomial(mask)
    has_point=[p for p in points if int(F.subs(dict(zip(variables,p))))%2==0]
    assert len(has_point) in (0,7)
    for linear,a,b in lines:
        expr=S.Poly(S.expand(F.subs({X:U*a[0]+V*b[0],Y:U*a[1]+V*b[1],Z:U*a[2]+V*b[2]}, simultaneous=True)),U,V,modulus=2).as_expr()
        assert not squarefree_binary(expr), (mask,linear,expr)
    for affine in variables:
        others=[w for w in variables if w!=affine]
        f=S.Poly(F.subs(affine,1),*others,modulus=2).as_expr()
        eq=[f]+[S.Poly(S.diff(F,w).subs(affine,1),*others,modulus=2).as_expr() for w in variables]
        g=S.groebner(eq,*others,modulus=2)
        assert len(g.polys)==1 and g.polys[0].as_expr()==1,(mask,affine,g)
print('independent symbolic checks PASS: 25 candidate restrictions, all 75 Jacobian/F chart unit-ideal tests')
for mask in [6438,20181]:
    print('representative',mask,'polynomial',polynomial(mask))
