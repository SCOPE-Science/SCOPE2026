#!/usr/bin/env python3
"""Exact symbolic facet/volume verification for a two-apex cubical convex family.
Scientific input: vertices and half-space duality. Dependencies: sympy, scipy, numpy.
The floating-point hulls choose candidate triangulations only; EVERY
supporting-plane and volume identity is checked exactly for whole chambers.
"""
from itertools import product
from collections import Counter
import sympy as s
import numpy as np
from scipy.spatial import ConvexHull
T,U=s.symbols('t u',positive=True)
C=[s.Matrix(p) for p in product([-1,1],repeat=3)]
V=C+[s.Matrix(p) for p in [(1+T,1,1),(1,1+T,1),(-1-T,-1,-1),(-1,-1-T,-1)]]

def val(expr,t0):return float(s.cancel(expr).subs(T,t0))
def simple_sign(expr,ch):
    ex=s.cancel(expr)
    if ex==0:return 0
    sub=2*U/(1+U) if ch==0 else 2+U
    r=s.cancel(ex.subs(T,sub)); num,den=r.as_numer_denom()
    pn=s.Poly(s.expand(num),U);pd=s.Poly(s.expand(den),U)
    # positive rational functions by coefficient positivity
    sign_num=1 if all(c>=0 for c in pn.all_coeffs()) else -1 if all(c<=0 for c in pn.all_coeffs()) else None
    sign_den=1 if all(c>=0 for c in pd.all_coeffs()) else -1 if all(c<=0 for c in pd.all_coeffs()) else None
    if sign_num is None or sign_den is None:
       raise AssertionError(f'Sign undecided chamber {ch}: {s.factor(ex)} => {s.factor(r)}')
    return sign_num*sign_den

def facet_triangulation(points,tval,ch,name):
    sample=np.array([[val(x,tval) for x in p] for p in points]);h=ConvexHull(sample)
    tris=[]
    for tri0 in h.simplices:
        i,j,k=map(int,tri0); a,b,c=points[i],points[j],points[k]
        n=(b-a).cross(c-a); off=s.factor(n.dot(a))
        if val(off,tval)<0:j,k=k,j;n=-n;off=-off
        assert simple_sign(off,ch)==1, (name,'origin outside')
        for l,q in enumerate(points):
            gap=s.factor(off-n.dot(q))
            assert simple_sign(gap,ch)>=0,(name,tri0,l,gap)
        tris.append((i,j,k))
    edgecounts=Counter(tuple(sorted((a,b))) for i,j,k in tris for a,b in ((i,j),(j,k),(k,i)))
    assert len(tris)>0 and all(z==2 for z in edgecounts.values()),(name,'not closed triangulation')
    # Every original point is either interior or a vertex; no holes since
    # this is a closed triangulated supporting surface with positive offsets.
    vol=s.factor(sum(s.Matrix.hstack(points[i],points[j],points[k]).det()/6 for i,j,k in tris))
    assert simple_sign(vol,ch)==1
    return vol,tris

def chamber(ch):
    tv=s.Rational(1) if ch==0 else s.Rational(3)
    vp,tri=facet_triangulation(V,tv,ch,'primal')
    W=[]
    for i,j,k in tri:
        a,b,c=V[i],V[j],V[k];n=(b-a).cross(c-a);off=s.factor(n.dot(a)); p=s.Matrix([s.factor(z/off) for z in n])
        if p not in W:W.append(p)
    for p in W:
        for v in V:assert simple_sign(1-p.dot(v),ch)>=0
    vw,dualtri=facet_triangulation(W,tv,ch,'polar')
    # Every facet of the polar is exposed by a generating primal point,
    # proving no polar facets are missing.
    for i,j,k in dualtri:
        a,b,c=W[i],W[j],W[k];n=(b-a).cross(c-a);off=s.factor(n.dot(a));u=s.Matrix([s.factor(x/off) for x in n])
        assert u in V,('missing primal vertex',list(u))
    predicted_v=8+s.Rational(16,3)*T+s.Rational(2,3)*T**2 if ch==0 else s.Rational(4,3)*(T+2)**2
    predicted_w=-2*(T**3-28*T-32)/(3*(T+2)**2*(T+4)) if ch==0 else 8*(3*T**3+12*T**2+12*T-16)/(3*T**2*(T+2)**2*(T+4))
    assert s.factor(vp-predicted_v)==0,(vp,predicted_v)
    assert s.factor(vw-predicted_w)==0,(vw,predicted_w)
    print(f'chamber {ch}: primal vertices={len(V)}, supported triangles={len(tri)}, polar vertices={len(W)}, polar triangles={len(dualtri)}; exact formulas PASS')
    print(' primal volume:',vp,'polar volume:',vw)
    return vp,vw

def main():
    p1,w1=chamber(0);p2,w2=chamber(1)
    P1=s.factor(p1*w1);P2=s.factor(p2*w2)
    assert s.simplify(P1.subs(T,2)-P2.subs(T,2))==0
    assert s.factor(s.factor(P1-s.Rational(32,3))--4*T*(T**3+6*T**2-4*T-56)/(9*(T+2)*(T+4)))==0
    assert s.factor(s.factor(P2-s.Rational(32,3))-128*(3*T-4)/(9*T**2*(T+4)))==0
    assert s.factor(s.factor(s.diff(P1,T))--8*(T*T+2*T-4)*(T**3+10*T*T+36*T+56)/(9*(T+2)**2*(T+4)**2))==0
    assert s.factor(s.factor(s.diff(P2,T))--256*(3*T*T-16)/(9*T**3*(T+4)**2))==0
    assert simple_sign(P1-s.Rational(32,3),0)==1
    assert simple_sign(P2-s.Rational(32,3),1)==1
    assert s.limit(P2,T,s.oo)==s.Rational(32,3)
    assert s.factor(P1.subs(T,s.sqrt(5)-1)-P2.subs(T,s.Rational(4,1)/s.sqrt(3)))>0
    print('Mahler positivity, critical points, endpoint continuity, global maximum comparison: PASS')
    print('P_low =',P1);print('P_high =',P2)
    print('Peak low at',s.sqrt(5)-1,'value=',s.simplify(P1.subs(T,s.sqrt(5)-1)))
    print('Peak high at',s.Rational(4,1)/s.sqrt(3),'value=',s.simplify(P2.subs(T,4/s.sqrt(3))))
if __name__=='__main__':main()
