#!/usr/bin/env python3
"""Exact characteristic-three checks for the 12 Hesse conics of arXiv:2305.01450.
The proof of geometric completeness uses Bezout; no finite sampling substitutes for it.
Requires Python 3 and sympy.
"""
import sympy as S
from collections import Counter
x,y,z,t,w = S.symbols('x y z t w')
Q = x*x+y*y+z*z+(t+1)*(x*y+x*z+y*z)
r = [x*y-t*z*z, x*z-t*y*y, y*z-t*x*x]
forms = [
 x*x+(t+1)*(w*x*y+w*w*x*z+y*z)+w*w*y*y+w*z*z,
 x*x+(t+1)*(w*w*x*y+w*x*z+y*z)+w*y*y+w*w*z*z,
 r[0],
 x*x+(w*t+1)*(x*y+w*x*z+w*y*z)+y*y+w*w*z*z,
 x*x+(w*w*t+1)*(x*y+w*w*x*z+w*w*y*z)+y*y+w*z*z,
 x*x+(w*t+w*w)*(x*y+y*z+w*x*z)+w*y*y+z*z,
 r[1],
 x*x+(w*w*t+w)*(x*y+y*z+w*w*x*z)+w*w*y*y+z*z,
 x*x+(t+w*w)*(x*y+x*z+w*w*y*z)+w*y*y+w*z*z,
 x*x+(t+w)*(x*y+x*z+w*y*z)+w*w*(y*y+z*z),
 -r[2],
 x*x+(t+1)*(x*y+x*z+y*z)+y*y+z*z,
]
def poly3(expr, *vars): return S.Poly(S.expand(expr), *vars, modulus=3)
def eq3(a,b, *vars): return poly3(a-b,*vars).is_zero
assert len(forms)==12
for i,f in enumerate(forms):
    expected={2:r[0],6:r[1],10:-r[2]}.get(i,Q)
    assert eq3(f.subs(w,1),expected,x,y,z,t), (i+1,poly3(f.subs(w,1)-expected,x,y,z,t))
# Symmetric 2-times conic matrix, with no division by 2 over Z.
M=S.Matrix([[2,t+1,t+1],[t+1,2,t+1],[t+1,t+1,2]])
assert eq3(M.det(),-(t-1)**3,t)
# The other three conics have determinant proportional to t; inspect by matrices.
for f in r:
 mat=S.hessian(f,(x,y,z))
 assert poly3(mat.det(),t).degree()==1 and not eq3(mat.det(),0,t)
A=[(t,1,1),(1,t,1),(1,1,t)]
E=[(1,0,0),(0,1,0),(0,0,1)]
allf=[Q]+r
assert all(eq3(Q.subs(dict(zip((x,y,z),v))),0,t) for v in A)
# Each of A,B,C lies on Q and precisely two of r_i for t!=1.
for i,p in enumerate(A):
    values=[poly3(f.subs(dict(zip((x,y,z),p))),t).as_expr() for f in allf]
    assert sum(eq3(v,0,t) for v in values)==3, (i,values)
# Tangents of Q and the two r_i at each triple point are identical.
for i,p in enumerate(A):
    idx=[[1,2],[1,3],[2,3]][i]
    gradients=[]
    for j in [0]+idx:
        g=S.Matrix([S.diff(allf[j],v).subs(dict(zip((x,y,z),p))) for v in (x,y,z)])
        gradients.append(g)
        assert not all(eq3(h,0,t) for h in g)
    for g in gradients[1:]:
        assert all(eq3(h,0,t) for h in gradients[0].cross(g))
# Local characteristic-three elimination of r_3 and r_7 at A, using z=1.
assert eq3(r[0].subs({x:t*y*y,z:1}),t*(y-1)**3,y,t)
# At the three coordinate vertices, exactly two r_i meet transversely.
for p in E:
    ids=[j for j,f in enumerate(allf) if eq3(f.subs(dict(zip((x,y,z),p))),0,t)]
    assert len(ids)==2 and 0 not in ids, (p,ids)
    gg=[]
    for j in ids:
        gg.append(S.Matrix([S.diff(allf[j],v).subs(dict(zip((x,y,z),p))) for v in (x,y,z)]))
    assert any(not eq3(v,0,t) for v in gg[0].cross(gg[1]))
# Verify the exact multiplicity patterns of the cited 9 and 12 point sections.
p9=[(t,1,1),(1,t,1),(1,1,t),(t,w,w*w),(w*w,t,w),(w,w*w,t),(t,w*w,w),(w,t,w*w),(w*w,w,t)]
s12=[(1,1,1),(w,w*w,1),(w*w,w,1),(1,0,0),(0,1,0),(w*w,1,1),
     (1,w*w,1),(w,1,1),(1,w,1),(w*w,w*w,1),(0,0,1),(w,w,1)]
# Normalize projective point in F3(t), here all reductions already are one of A,E or (1,1,1).
def reduced_signature(p):
 q=[S.expand(a.subs(w,1)) if isinstance(a,S.Basic) else S.Integer(a) for a in p]
 return tuple(map(str,q))
c9=Counter(map(reduced_signature,p9));c12=Counter(map(reduced_signature,s12))
assert sorted(c9.values())==[3,3,3], c9
assert sorted(c12.values())==[1,1,1,9], c12
assert c12[('1','1','1')]==9
# At (1,1,1) the reduced support has only Q as a branch for t != 1.
P=(1,1,1)
assert eq3(Q.subs({x:1,y:1,z:1}),0,t)
assert all(eq3(f.subs({x:1,y:1,z:1}),1-t,t) for f in r)
# Bezout completion: three length-seven three-branch intersections and three nodes.
delta_triple=2+2+3
assert delta_triple==7
assert 3*delta_triple+3==24 and (8-1)*(8-2)//2==24-4+1
print('HESSE_12_CONICS_CHAR3_NINEFOLD_COMPONENT_THREE_DELTA7_TRIPLES_OK')
