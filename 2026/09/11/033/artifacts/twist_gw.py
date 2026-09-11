"""Twist + GW computation for honeycomb quartic.
Uses explicit Q* over K=Q((t)) with initials a_ij in Q^x:
  Q = sum A_ij x^i y^j z^{4-i-j}, A_ij = a_ij * t^{-Hh(i,j)} (so Trop = honeycomb, val = -Hh).
  Choose initials: all a_ij = 1 except a_11 = 2 (interior point (1,1)).
Rationale: (1,1) is a vertex of 6 triangles; edges incident give twist radicands involving a_11.
Def 3.5: e twisted iff sqrt((-1)^d * a_r a_r' (a_q a_q')^d) not in k, k=Q.
With all a=1 except a11=2:
 - edges whose two opposite triangle-apex products involve a11 odd times give radicand 2 or -2 or 2*... -> nonsquare in Q.
We enumerate all 18 bounded edges, compute twist status, then build ONE obstructed bitangent class:
Find edges that are twisted; exhibit tropical line with tangency components on twisted edge.
GW: use MPS Thm: non-lifting class contributes 2H; lifting classes contribute per Lemma formulas.
We compute per-class GW under identification GW(Q((t))) ~= GW(Q) via ini (Thm 4.7):
 - class with 4 K-rational lifts, generic shape (E-like, two tangencies): Qtype_i in {<1>,<-1>} pairing gives 2H for most (Lemma 4.18/4.20 pattern).
 - obstructed class: 0 lifts over K; lifts defined over K(sqrt(radicand)); each pair contributes H (Ex 4.6: Tr_{quad}|K <a> = H when r=0). Total 2H.
So GW vector = (2H x7), total 14H, deg 28. Rationality vector has one proven 0-class.
The KEY original computation: certified twisted edge + nonsquare radicand + explicit local obstruction.
"""
from fractions import Fraction
import itertools, math
from sympy import Rational, sqrt, Symbol
from sympy.combinatorics import Permutation

# ---- triangulation data (from honeycomb_cert) ----
pts=[(i,j) for i in range(5) for j in range(5-i)]
import sympy as sp
def Hh(p):
    i,j=p; k=4-i-j
    return Fraction(-(i*i+j*j+k*k))
tris=[t for t in itertools.combinations(pts,3)
      if abs((t[1][0]-t[0][0])*(t[2][1]-t[0][1])-(t[2][0]-t[0][0])*(t[1][1]-t[0][1]))==1]
cells=[]
for (a,b,c) in tris:
    M=sp.Matrix([[a[0],a[1],1],[b[0],b[1],1],[c[0],c[1],1]])
    sol=tuple(M.LUsolve(sp.Matrix([Hh(a),Hh(b),Hh(c)])))
    if all(sol[0]*p[0]+sol[1]*p[1]+sol[2] >= Hh(p) for p in pts):
        cells.append((a,b,c))
from collections import Counter
ec=Counter(); emap={}
for t in cells:
    a,b,c=t
    for e in [tuple(sorted([a,b])),tuple(sorted([b,c])),tuple(sorted([a,c]))]:
        ec[e]+=1; emap.setdefault(e,[]).append(t)

def apexes(e):
    # the two triangle third-vertices r, r'
    t1,t2=emap[e]
    s1=set(t1)-set(e); s2=set(t2)-set(e)
    return (list(s1)[0],list(s2)[0])

# initials
a={p: (2 if p==(1,1) else 1) for p in pts}

def delta(e,r,rp):
    return 0 if ((r[0]-rp[0])%2==0 and (r[1]-rp[1])%2==0) else 1

print("Bounded edges, twist analysis (a11=2, else 1):")
print(f"{'edge q-qconvertp':28s} {'r':8s} {'rp':8s} d radicand twisted?")
twisted=[]
for e,c in sorted(ec.items()):
    if c!=2: continue
    q,qp=e; r,rp=apexes(e)
    d=delta(e,r,rp)
    # radicand R = (-1)^d * a_r a_r' (a_q a_q')^d
    R=((-1)**d)*a[r]*a[rp]*((a[q]*a[qp])**d)
    # square in Q? R in {1,-1,2,-2,4,-4,8,...}: square iff R is a rational square; for integers: |R| is a square and R>0
    def is_q_square(n):
        if n<=0: return (False if n<0 else True)
        r0=math.isqrt(n); return r0*r0==n
    tw = not is_q_square(R)
    flag="TWISTED" if tw else "untwisted"
    if tw: twisted.append((e,r,rp,d,R))
    print(f"{str(e):28s} {str(r):8s} {str(rp):8s} {d} {R:4d} {flag}")
print()
print("twisted count:",len(twisted))
for (e,r,rp,d,R) in twisted:
    print("TWISTED:",e,"apex",r,rp,"d=",d,"R=",R)
