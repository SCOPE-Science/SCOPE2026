#!/usr/bin/env python3
"""Reproducibility checks for parallel vertex truncations of tetrahedra.

Only Python 3, numpy, scipy required. Geometry assertions are finite diagnostics,
not substitutes for the all-directions proof in RESULT.md.
"""
import math
import numpy as np
from scipy.spatial import ConvexHull


def faces_outward(V):
    normals=[]
    for i in range(4):
        ids=[j for j in range(4) if j!=i]
        a,b,c=V[ids]
        n=np.cross(b-a,c-a)
        if np.dot(n,V[i]-a)>0:n=-n
        n/=np.linalg.norm(n)
        normals.append(n)
    return np.asarray(normals)


def truncated(V,t):
    return np.array([(1-t[i])*V[i]+t[i]*V[j] for i in range(4) for j in range(4) if i!=j])


def solid_angle_at_vertex(V,i):
    E=np.array([V[j]-V[i] for j in range(4) if j!=i])
    E/=np.linalg.norm(E,axis=1)[:,None]
    a,b,c=E
    denominator=1+np.dot(a,b)+np.dot(a,c)+np.dot(b,c)
    numerator=abs(np.linalg.det(E))
    return 2*math.atan2(numerator,denominator)


def projected_vertex_count(V,u):
    # Independent numerical convex-hull reconstruction; does not use face normals.
    axis=np.eye(3)[int(np.argmin(abs(u)))]
    x=np.cross(u,axis); x/=np.linalg.norm(x)
    y=np.cross(u,x)
    return len(ConvexHull(np.column_stack((V@x,V@y))).vertices)


def test(V,tsets,orientations=2300):
    assert abs(np.linalg.det(np.column_stack((V[1:]-V[0]))))>1.e-9
    normal=faces_outward(V)
    p9=sum(solid_angle_at_vertex(V,i) for i in range(4))/(2*math.pi)
    assert 0<p9<1
    truncations=[truncated(V,np.array(t,float)) for t in tsets]
    for T in truncations:
        H=ConvexHull(T)
        assert len(H.vertices)==12 and len(H.simplices)>0
    counts={8:0,9:0}
    for k in range(orientations):
        height=1-2*(k+.25)/orientations
        phi=k*math.pi*(3-math.sqrt(5))+.136
        u=np.array([math.sqrt(1-height*height)*math.cos(phi),math.sqrt(1-height*height)*math.sin(phi),height])
        sign=normal@u
        if np.min(abs(sign))<1.e-8:continue
        pos=int(np.sum(sign>0))
        assert pos in (1,2,3)
        nt=pos*(4-pos)
        assert projected_vertex_count(V,u)==nt
        for T in truncations:
            nc=projected_vertex_count(T,u)
            assert nc==12-nt, (nt,nc,pos)
        counts[12-nt]+=1
    empirical=counts[9]/sum(counts.values())
    # Low discrepancy sample count error, not an exact theorem.
    assert abs(empirical-p9)<0.026,(empirical,p9)
    return p9,counts



def exact_rational_tests():
    """Exact projected-hull checks on a finite set of integer directions."""
    from fractions import Fraction as F
    from itertools import product
    def cross(a,b):
        return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
    def dot(a,b):return sum(x*y for x,y in zip(a,b))
    def sub(a,b):return tuple(x-y for x,y in zip(a,b))
    def hull_count(points):
        P=sorted(set(points))
        def turn(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
        lo=[]
        for p in P:
            while len(lo)>=2 and turn(lo[-2],lo[-1],p)<=0:lo.pop()
            lo.append(p)
        hi=[]
        for p in reversed(P):
            while len(hi)>=2 and turn(hi[-2],hi[-1],p)<=0:hi.pop()
            hi.append(p)
        return len(lo[:-1]+hi[:-1])
    def projected_count(V,u):
        e=(-u[1],u[0],0) if (u[0],u[1])!=(0,0) else (1,0,0)
        f=cross(u,e)
        return hull_count([(dot(v,e),dot(v,f)) for v in V])
    sample=[
        [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)],
        [(0,0,0),(3,0,0),(1,4,0),(1,1,2)]
    ]
    levels=[(F(1,3),)*4,(F(1,11),F(2,11),F(3,11),F(4,11))]
    checked=0
    for V in sample:
        normals=[]
        for i in range(4):
            a,b,c=[V[j] for j in range(4) if j!=i]
            n=cross(sub(b,a),sub(c,a))
            if dot(n,sub(V[i],a))>0:n=tuple(-z for z in n)
            normals.append(n)
        for t in levels:
            W=[tuple((1-t[i])*V[i][k]+t[i]*V[j][k] for k in range(3))
               for i in range(4) for j in range(4) if i!=j]
            for u in product(range(-3,4),repeat=3):
                if u==(0,0,0):continue
                signs=[dot(n,u) for n in normals]
                if 0 in signs:continue
                p=sum(z>0 for z in signs)
                Nt=projected_count(V,u)
                Nc=projected_count(W,u)
                assert Nt==p*(4-p),(V,t,u,Nt,p)
                assert Nc==12-Nt,(V,t,u,Nc,Nt)
                checked+=1
    print(f'EXACT_RATIONAL_HULL_CHECKS_OK {checked}')

def main():
    tetrahedra=[
        np.array([(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)],float),
        np.array([(0,0,0),(3,0,0),(1,4,0),(.5,.8,2)],float),
        np.array([(0,0,0),(1,0,0),(0,1,0),(.25,.3,.1)],float),
        np.array([(0,0,0),(1,0,0),(1,1,0),(0,1,.15)],float),
    ]
    tsets=[(.33333333333,)*4,(.12,.15,.19,.25),(.74,.07,.1,.08)]
    for i,V in enumerate(tetrahedra):
        prob,counts=test(V,tsets)
        print(f'TETRA_{i} P9={prob:.12f} counts={counts}')
    exact_regular=6*math.acos(1/3)/math.pi-2
    prob_regular=sum(solid_angle_at_vertex(tetrahedra[0],i) for i in range(4))/(2*math.pi)
    assert abs(exact_regular-prob_regular)<2e-14
    print(f'REGULAR P8={1-exact_regular:.12f} P9={exact_regular:.12f}')
    exact_rational_tests()
    print('VERIFY_OK')

if __name__=='__main__':main()
