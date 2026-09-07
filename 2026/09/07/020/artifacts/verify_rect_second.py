#!/usr/bin/env python3
"""Second independent crossing counter using rational parametric intersection.
Different code path from orientation predicates: solves for t,s in (0,1).
"""
import json, pathlib
from fractions import Fraction
base=pathlib.Path(__file__).parent
d=json.loads((base/"coords_K57_rect.json").read_text())
A=[tuple(p) for p in d["A"]]; B=[tuple(p) for p in d["B"]]
pts=A+B
edges=[(A[i],B[j],i,j) for i in range(5) for j in range(7)]
def seg_int(a,b,c,dd):
    # return True iff segments ab and cd intersect at interior point (excluding endpoints)
    # solve a + t(b-a) = c + s(d-c), t,s in (0,1), exact Fractions
    x1,y1=a; x2,y2=b; x3,y3=c; x4,y4=dd
    dx1=x2-x1; dy1=y2-y1; dx2=x4-x3; dy2=y4-y3
    den=dx1*dy2-dy1*dx2
    if den==0: return None  # parallel (should not happen for crossing candidates given general position? could be parallel distinct)
    # t = ((x3-x1)*dy2 - (y3-y1)*dx2)/den? check sign: a+t*dx1 = c+s*dx2
    t=Fraction((x3-x1)*dy2-(y3-y1)*dx2, den)
    s=Fraction((x3-x1)*dy1-(y3-y1)*dx1, den) if False else Fraction((x3-x1)*dy2-(y3-y1)*dx2, den)  # placeholder
    # correct s: from x: x1+t dx1 = x3 + s dx2 => s = (x1+t dx1 - x3)/dx2 if dx2!=0 else (y1+t dy1 - y3)/dy2
    # compute s via Cramer's second:
    # |dx1 -dx2| |t| = |x3-x1|
    # |dy1 -dy2| |s|   |y3-y1|  => det = -dx1*dy2+dy1*dx2 = -den
    # t = ((x3-x1)(-dy2)-( -dx2)(y3-y1))/(-den) = (-(x3-x1)dy2+dx2(y3-y1))/(-den)=((x3-x1)dy2-dx2(y3-y1))/den OK
    # s = (dx1(y3-y1)-dy1(x3-x1))/(-den) = (dy1(x3-x1)-dx1(y3-y1))/den
    s=Fraction(dy1*(x3-x1)-dx1*(y3-y1), den)
    # for den<0 inequalities flip? No, Fraction comparison is exact, t in (0,1) check directly
    # But derivation assumed den as above; t,s formulas exact regardless of sign.
    return (Fraction(0)<t<Fraction(1)) and (Fraction(0)<s<Fraction(1))

cnt=0
for e1 in range(35):
    for e2 in range(e1+1,35):
        a,b,i1,j1=edges[e1]; c,dd,i2,j2=edges[e2]
        if i1==i2 or j1==j2: continue
        r=seg_int(a,b,c,dd)
        if r: cnt+=1
print(f"parametric rational count: {cnt}")
assert cnt==36
print("PASS second method")
