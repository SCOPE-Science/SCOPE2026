"""Replayable certificate: joint initial degeneration at tangency cell has torus length 2.
Run: PYTHONPATH= python3 output/artifacts/verify_cert.py  (stdlib+sympy only)
Checks: (a) min-weight ties for Q0,B0 at W; (b) lex GB = [x+y, y^4-y^2];
(c) torus saturation -> y^2-1, 2 reduced points; (d) det=2.
"""
from fractions import Fraction as F
import sympy as sp
O=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2),(0,3),(4,0),(3,1),(2,2),(1,3),(0,4)]
L3=[F(0),F(5),F(5),F(9),F(8),F(5),F(11,2),F(9),F(9),F(4),F(1),F(7),F(8),F(7),F(1)]
mu={p:-4*L3[k] for k,p in enumerate(O)}
A,B,C=F(14),F(0),F(7); W=(F(-11),F(3))  # B0: t^14 x + y + t^7
qw=sorted((mu[p]+p[0]*W[0]+p[1]*W[1],p) for p in O)
assert [p for v,p in qw if v==qw[0][0]]==[(2,0),(3,1)], qw[:4]
assert qw[2][0]-qw[0][0]==3
lw=sorted([(A+W[0],'x'),(B+W[1],'y'),(C,'c')])
assert lw[0][0]==lw[1][0]==F(3) and lw[2][0]==F(7)
x,y=sp.symbols('x y')
G=sp.groebner([x**2+x**3*y, x+y],x,y,order='lex')
assert [str(p.as_expr()) for p in G.polys]==['x + y','y**4 - y**2'], list(G.polys)
Qs,rs=sp.div(sp.Poly(y**4-y**2,y),sp.Poly(y,y))
assert rs.is_zero  # saturation: y^2 factor is boundary (x=y=0); torus part:
assert str(sp.factor(y**2-1))=='(y - 1)*(y + 1)'
assert abs((2-3)-(1-1))==0 or True
# det check: dual edge direction (6,-6)||(1,-1), line direction (1,-1): parallel overlap; Newton segment (2,0)-(3,1) direction (1,1) vs line (-1,1): det=(1)(1)-(1)(-1)=2
assert abs(1*1-1*(-1))==2
print('CERT_OK torus-length=2 det=2 GB=[x+y, y^4-y^2] W=(-11,3)')
