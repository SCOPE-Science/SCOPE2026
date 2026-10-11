#!/usr/bin/env python3
"""Reconstructs exact moments and independently quadratures spherical tangent cones."""
import math, itertools
import numpy as np
from numpy.polynomial.legendre import leggauss

def geom(V):
    V = np.asarray(V,float)
    assert V.shape == (4,3) and abs(np.linalg.det(V[1:]-V[0])) > 1e-8
    normals,areas=[],[]
    for i in range(4):
        j,k,l=[x for x in range(4) if x!=i]
        cross=np.cross(V[k]-V[j],V[l]-V[j]); length=np.linalg.norm(cross)
        n=cross/length
        if np.dot(n,V[i]-V[j]) > 0: n=-n
        normals.append(n);areas.append(length/2)
    normals=np.asarray(normals);areas=np.asarray(areas)
    p=0.; m1=0.;m2=0.; data=[]
    for i in range(4):
        others=[j for j in range(4) if j!=i]
        E={j:(V[j]-V[i])/np.linalg.norm(V[j]-V[i]) for j in others}
        a,b,c=[E[j] for j in others]
        Omega=2*math.atan2(abs(np.linalg.det(np.column_stack([a,b,c]))),1+np.dot(a,b)+np.dot(b,c)+np.dot(c,a))
        t1=t2=0.
        for j,k in itertools.combinations(others,2):
            missing=next(z for z in others if z not in (j,k))
            theta=math.acos(np.clip(np.dot(E[j],E[k]),-1,1))
            t1 += theta*np.dot(normals[i],normals[missing])
            t2 += np.dot(normals[i],normals[missing])*math.tan(theta/2)*np.dot(normals[i],E[j]+E[k])
        I1=-t1/2
        I2=Omega/3-t2/3
        data.append((Omega,I1,I2,areas[i],normals[i],[a,b,c]))
        p+=Omega/(2*math.pi)
        m1+=areas[i]*I1/(2*math.pi)
        m2+=areas[i]**2*I2/(2*math.pi)
    mean=sum(areas)/4
    cross=0.
    for i,j in itertools.combinations(range(4),2):
        c=float(np.dot(normals[i],normals[j]))
        cross+=areas[i]*areas[j]*(math.sqrt(max(0,1-c*c))+c*math.asin(c))
    second=sum(areas*areas)/12+cross/(3*math.pi)
    return p,m1,m2,mean,second,data,normals,areas

def numeric_cone(a,b,c,n,N=80):
    # Independent barycentric radial area quadrature, not the boundary Green identity.
    x,w=leggauss(N);x=(x+1)/2;w=w/2
    a,b,c=map(np.asarray,(a,b,c))
    det=abs(np.linalg.det(np.column_stack((a,b,c))))
    z0=z1=z2=0.
    for i,t in enumerate(x):
        for j,s in enumerate(x):
            v=t*a+(1-t)*s*b+(1-t)*(1-s)*c
            q=v/np.linalg.norm(v)
            jac=det*(1-t)*w[i]*w[j]/np.linalg.norm(v)**3
            h=np.dot(n,q)
            z0+=jac;z1+=jac*h;z2+=jac*h*h
    return z0,z1,z2

canonical=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)
alpha=math.asin(1/3); omega=math.pi/2-3*alpha
ptri=1-6*alpha/math.pi
assert ptri>0
Mtri=math.pi/(math.sqrt(3)*omega)
Mquad=2*math.pi/(3*math.sqrt(3)*alpha)
S2tri=4+8*math.sqrt(2)/(3*omega)
S2quad=16/3+16*math.sqrt(2)/(9*alpha)
assert Mtri < Mquad

p,m1,m2,mu,ss,data,normals,areas=geom(canonical)
assert abs(p-ptri)<1e-13
assert abs(m1/p-Mtri)<1e-13
assert abs((mu-m1)/(1-p)-Mquad)<1e-13
assert abs(m2/p-S2tri)<1e-13
assert abs((ss-m2)/(1-p)-S2quad)<1e-13
assert abs(mu-2*math.sqrt(3))<1e-13
assert abs(ss-(4+8/math.pi*(2*math.sqrt(2)+alpha)))<1e-13

all_tetras=[canonical,canonical@np.array([[1.2,.2,.0],[.0,.85,.2],[.0,.0,1.7]]),
np.array([[0,0,0],[1,0,0],[.2,1,0],[.3,.1,1.3]],float)]
worst=0.
for V in all_tetras:
    p,m1,m2,mu,ss,data,normals,areas=geom(V)
    for Om,I1,I2,A,n,edges in data:
        calc=numeric_cone(*edges,n)
        err=max(abs(Om-calc[0]),abs(I1-calc[1]),abs(I2-calc[2]))
        worst=max(worst,err)
        assert err<5e-12,(V,err,calc,(Om,I1,I2))
    assert 0<p<1 and 0<m1<mu and 0<m2<ss

# Independent spherical random directions with geometric 2D convex hull for a subset.
rng=np.random.default_rng(20261008)
N=600_000
U=rng.normal(size=(N,3));U/=np.linalg.norm(U,axis=1)[:,None]
for V in [canonical,all_tetras[2]]:
    p,m1,m2,mu,ss,_,normals,areas=geom(V)
    lengths=np.abs(U@normals.T)*areas[None,:]
    b=lengths.sum(axis=1)/2
    t=(np.abs(np.max(lengths,axis=1)-b)<5e-12)
    assert abs(t.mean()-p)<0.003
    assert abs(np.mean(b*t)-m1)<0.015
    assert abs(np.mean(b*b*t)-m2)<0.10
    assert abs(np.mean(b)-mu)<0.015
    assert abs(np.mean(b*b)-ss)<0.10

# Convex hull projected to a random perpendicular orthonormal basis for a separate event check.
from scipy.spatial import ConvexHull
for V in [canonical,all_tetras[2]]:
    _,_,_,_,_,_,normals,areas=geom(V)
    for u in U[:1400]:
        a=np.cross(u,[0,0,1.]) if abs(u[2])<0.9 else np.cross(u,[0,1.,0])
        a/=np.linalg.norm(a); b=np.cross(u,a)
        xy=np.stack((V@a,V@b),axis=1)
        hull=ConvexHull(xy)
        area=hull.volume
        lin=np.abs(normals@u)*areas
        ba=np.sum(lin)/2
        tr=np.isclose(ba,np.max(lin),atol=1e-10)
        assert len(hull.vertices)==(3 if tr else 4)
        assert abs(area-ba)<1e-10
print('VERIFY_OK')
print('spherical_cone_quadrature_max_abs_error',format(worst,'.3g'))
print('stochastic_directions',N,'and_convex_hull_projections',2*1400)
print('canonical p_triangle',format(ptri,'.15g'))
print('canonical conditional first moments',format(Mtri,'.15g'),format(Mquad,'.15g'))
print('canonical conditional second moments',format(S2tri,'.15g'),format(S2quad,'.15g'))
