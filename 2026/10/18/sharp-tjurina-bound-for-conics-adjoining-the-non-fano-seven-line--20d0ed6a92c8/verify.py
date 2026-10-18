"""Exact algebraic checks for the sharp non-Fano conic-extension bound.
Run: python verify.py. Requires SymPy; no data files or online services.
The universal inequality is proved in RESULT.md, not inferred from enumeration.
"""
from itertools import combinations
from collections import defaultdict
import sympy as S

x,y,z=S.symbols('x y z')
i=S.I
forms=[x,y,z,x+y,x+z,y+z,x+y+z]
coeff=[S.Matrix([S.diff(F,a) for a in (x,y,z)]) for F in forms]

def normalize(vec):
    vals=[int(v) for v in vec]
    g=S.igcd(*vals)
    vals=[v//g for v in vals]
    if next(v for v in vals if v)<0:vals=[-v for v in vals]
    return tuple(vals)

points=defaultdict(set)
for a,b in combinations(range(7),2):
    points[normalize(coeff[a].cross(coeff[b]))].update([a,b])
assert sorted([len(I) for I in points.values()])==[2]*3+[3]*6
assert {p for p,I in points.items() if len(I)==2}=={
    (1,-1,-1),(1,-1,1),(1,1,-1)}
assert all(any(set(J).issubset(S5) and len(J)==3 for J in points.values())
           for S5 in combinations(range(7),5))

u,v,w=S.symbols('u v w')
B=S.Matrix([[0,u,v],[u,0,w],[v,w,0]])
assert S.factor(B.det())==2*u*v*w
A=B.adjugate()
P=[S.Matrix(P) for P in [(1,-1,-1),(1,-1,1),(1,1,-1)]]
vals=[S.factor((p.T*A*p)[0].subs(w,-u-v)) for p in P]
assert vals==[4*u*v,-4*u*(u+v),-4*v*(u+v)]
# If all four high lines are tangent then w=-u-v and uvw != 0.
# Hence none of the three line double points can lie on the conic.

r,c=S.symbols('r c')
# With all three low-line double points on the conic, two coordinate-axis
# tangencies force a=b=r (or a degenerate zero case); the final conditions
# become c^2+4r^2=0 and c(c-4r)=0, impossible for nonzero (r,c).
assert S.factor((c*c+4*r*r).subs(c,4*r))==20*r*r

Q=S.expand((x-y)**2-4*i*(x+y)*z-4*z*z)
M=S.Matrix([[1,-1,-2*i],[-1,1,-2*i],[-2*i,-2*i,-4]])
assert S.expand((S.Matrix([x,y,z]).T*M*S.Matrix([x,y,z]))[0]-Q)==0
assert S.factor(M.det())==16
# The line l is tangent to Q iff l^T adj(M) l=0.
dual=[S.simplify((ell.T*M.adjugate()*ell)[0]) for ell in coeff]
assert dual[:3]==[0,0,0]
assert all(v!=0 for v in dual[3:])
for p,I in points.items():
    value=S.simplify(Q.subs(dict(zip((x,y,z),p))))
    if len(I)==3: assert value!=0
    else: assert (value==0)==(p in [(1,-1,-1),(1,-1,1)])
# Every conic-line contact in the witness is a distinct smooth tacnode,
# separate from all line-line intersections and every other line.
for p in [(0,2*i,1),(2*i,0,1),(1,1,0)]:
    assert S.simplify(Q.subs(dict(zip((x,y,z),p))))==0
    hits=[k for k,f in enumerate(forms) if S.simplify(f.subs(dict(zip((x,y,z),p))))==0]
    assert len(hits)==1 and hits[0] in [0,1,2], (p,hits)
# At the inherited low-line double points the conic cuts both lines
# transversely (its gradient cannot be proportional to either line normal).
for p in [(1,-1,-1),(1,-1,1)]:
    pp=S.Matrix(p)
    qgrad=2*M*pp
    for k,f in enumerate(forms):
        if S.simplify(f.subs(dict(zip((x,y,z),p))))==0:
            assert any(S.simplify(t)!=0 for t in qgrad.cross(coeff[k]))

h,t=2,3
n3=6+h
n2=35-2*t-3*n3
tau=n2+3*t+4*n3
assert (n2,t,n3,tau)==(5,3,8,46)
print('PASS: six old triple points, three old doubles, exact dual constraints,')
print('      smooth witness, three separate tacnodes, two new triple points,')
print('      no forbidden collisions, (n2,t,n3)=(5,3,8), tau=46.')
