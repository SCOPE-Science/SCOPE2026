#!/usr/bin/env python3
"""Reproduce the exact square-antiprism silhouette probabilities.
Uses only the Python standard library. No simulations are used for proof.
"""
import itertools
import math

SQRT2 = math.sqrt(2.0)
H = 2.0**0.25 / 2.0
BETA = (SQRT2 - 1.0) / 2.0**0.25
RHO = SQRT2 / math.sqrt(2.0+BETA*BETA)
PI = math.pi

def G(t):
    return math.asin(RHO * math.sin(t))

def probs():
    X, Y, Z, W = [G(t) for t in (PI/8, PI/4, 3*PI/8, PI/2)]
    return {5: 8/PI*(2*Z-Y-W),
            6: 8/PI*(W+2*Y-2*Z-X),
            7: 8/PI*(2*X-Y),
            8: 1-8/PI*X}

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])

def sub(x,y):
    return tuple(a-b for a,b in zip(x,y))

def unit(x):
    v = math.sqrt(dot(x,x))
    return tuple(y/v for y in x)

def vertices():
    # Four top vertices and four rotated bottom vertices.
    return [(math.cos(k*PI/2),math.sin(k*PI/2),H) for k in range(4)] + \
           [(math.cos((k+0.5)*PI/2),math.sin((k+0.5)*PI/2),-H) for k in range(4)]

def facets(vs):
    """Discover supporting facets independently of the explicit normal table."""
    result = {}
    for ids in itertools.combinations(range(8),3):
        i,j,k=ids
        n=cross(sub(vs[j],vs[i]),sub(vs[k],vs[i]))
        if dot(n,n)<1.e-15:
            continue
        ds=[dot(n,sub(v,vs[i])) for v in vs]
        if max(ds)>1.e-9 and min(ds)<-1.e-9:
            continue
        verts=tuple(t for t,x in enumerate(ds) if abs(x)<1.e-9)
        if verts not in result:
            # Supporting normal points outwards; centroid is the origin.
            if dot(n,vs[i])<0:
                n=tuple(-x for x in n)
            result[verts]=unit(n)
    assert len(result)==10, f"Unexpected facets: {len(result)}"
    assert sorted(len(k) for k in result)==[3]*8+[4]*2
    return result

def cross2(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def projected_hull_size(vs,u):
    axis=(0,0,1) if abs(u[2])<.95 else (1,0,0)
    ex=unit(cross(u,axis))
    ey=cross(u,ex)
    P=sorted((dot(v,ex), dot(v,ey)) for v in vs)
    lower=[]
    for p in P:
        while len(lower)>=2 and cross2(lower[-2],lower[-1],p)<=1.e-12:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(P):
        while len(upper)>=2 and cross2(upper[-2],upper[-1],p)<=1.e-12:
            upper.pop()
        upper.append(p)
    return len(lower)+len(upper)-2

def count_from_facets(faces,u):
    count=0
    for j in range(8):
        signs=[dot(n,u) for ids,n in faces.items() if j in ids]
        if min(signs)<-1.e-12 and max(signs)>1.e-12:
            count+=1
    return count

def count_from_thresholds(u):
    x,y,z=u
    if z<0:
        x,y,z=-x,-y,-z
    phi=math.atan2(y,x)
    phi=(phi%(PI/2))
    if phi>PI/4:
        phi=PI/2-phi
    w=z/math.hypot(x,y)
    c,s=math.cos(phi),math.sin(phi)
    a=(c-s)/BETA
    b=SQRT2*s/BETA
    cc=(c+s)/BETA
    d=SQRT2*c/BETA
    if min(a,b)<w<max(a,b):
        return 5
    if min(cc,d)<w<max(cc,d):
        return 7
    if w>max(cc,d):
        return 8
    return 6

def numerical_phi_quadrature(n=50000):
    delta=(PI/4)/n
    ans={5:0.0,6:0.0,7:0.0,8:0.0}
    for i in range(n):
        phi=(i+0.5)*delta
        c,s=math.cos(phi),math.sin(phi)
        a,b=(c-s)/BETA,SQRT2*s/BETA
        cc,d=(c+s)/BETA,SQRT2*c/BETA
        F=lambda t:t/math.sqrt(1+t*t)
        ans[5]+=abs(F(a)-F(b))
        ans[7]+=abs(F(cc)-F(d))
        ans[8]+=1-F(max(cc,d))
    for k in (5,7,8):
        ans[k]*=(4/PI)*delta
    ans[6]=1-ans[5]-ans[7]-ans[8]
    return ans

def main():
    p=probs()
    assert all(p[k]>0 for k in p)
    assert abs(sum(p.values())-1)<1.e-13
    q=numerical_phi_quadrature()
    assert max(abs(p[k]-q[k]) for k in p)<3.e-10,(p,q)
    vs=vertices(); faces=facets(vs)
    discrepancies=0
    # Golden-angle mesh; independent direct 2D convex-hull counts.
    N=20000
    golden=PI*(3-math.sqrt(5))
    hist={5:0,6:0,7:0,8:0}
    for i in range(N):
        z=-1+2*(i+.5)/N
        az=golden*i
        r=math.sqrt(1-z*z)
        u=(r*math.cos(az),r*math.sin(az),z)
        n1=projected_hull_size(vs,u)
        n2=count_from_facets(faces,u)
        n3=count_from_thresholds(u)
        assert n1==n2==n3,(i,n1,n2,n3,u)
        hist[n1]+=1
    assert all(abs(hist[k]/N-p[k])<.003 for k in p),(hist,p)
    # Independent first moment via sum of exterior dihedral angles.
    normals=list(faces.items());angle_sum=0.; edge_count=0
    for (a,n),(b,m) in itertools.combinations(normals,2):
        if len(set(a)&set(b))==2:
            angle_sum+=math.acos(max(-1.,min(1.,dot(n,m))))
            edge_count+=1
    assert edge_count==16
    mean_angles=angle_sum/PI
    mean_law=sum(k*v for k,v in p.items())
    assert abs(mean_law-mean_angles)<3.e-12,(mean_law,mean_angles)
    for k in sorted(p):
        print('P(N=%d) = %.15f ; mesh %d/%d'%(k,p[k],hist[k],N))
    print('Exact quadrature differences <= %.3g'%max(abs(p[k]-q[k]) for k in p))
    print('Mean = %.15f ; dihedral-check %.15f'%(mean_law,mean_angles))
    print('PASS: 20,000 direct independent 2D convex-hull comparisons; 10 facet incidences; 16 edge angles')

if __name__=='__main__':
    main()
