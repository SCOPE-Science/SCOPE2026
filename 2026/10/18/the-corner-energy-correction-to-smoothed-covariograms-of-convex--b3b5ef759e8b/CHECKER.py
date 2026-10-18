#!/usr/bin/env python3
"""Numerical reproduction of the planar smoothed-covariogram corner law.
Requires only Python standard library. Tests are not substituted for proof.
"""
import math

def A(z):
    return max(0.0,-z)+math.log1p(math.exp(-abs(z)))-math.log(2.0)

def Ap(z):
    return -math.exp(-max(0.0,z))/(1.0+math.exp(-abs(z))) if z >= 0 else -1.0/(1.0+math.exp(z))

def simpson(f,a,b,eps=2e-12,depth=22):
    if a == b: return 0.0
    c=(a+b)/2.0; fa=f(a); fb=f(b); fc=f(c)
    s=(b-a)*(fa+4*fc+fb)/6
    def rec(a,b,fa,fc,fb,s,eps,d):
        c=(a+b)/2; l=(a+c)/2; r=(c+b)/2
        fl=f(l); fr=f(r)
        sl=(c-a)*(fa+4*fl+fc)/6; sr=(b-c)*(fc+4*fr+fb)/6
        if d<=0 or abs(sl+sr-s) <=15*eps:
            return sl+sr+(sl+sr-s)/15
        return rec(a,c,fa,fl,fc,sl,eps/2,d-1)+rec(c,b,fc,fr,fb,sr,eps/2,d-1)
    return rec(a,b,fa,fc,fb,s,eps,depth)

def polygon(vertices):
    v=list(vertices)
    area=sum(v[i][0]*v[(i+1)%len(v)][1]-v[i][1]*v[(i+1)%len(v)][0] for i in range(len(v)))
    if area<0: v.reverse()
    n=[]; h=[]; ell=[]
    for i,(x,z) in enumerate(v):
        x1,z1=v[(i+1)%len(v)]
        dx=x1-x; dz=z1-z; length=math.hypot(dx,dz)
        nx,nz=dz/length,-dx/length
        support=nx*x+nz*z
        assert support>0
        n.append((nx,nz)); h.append(support);ell.append(length)
    return v,n,h,ell

def target(data,y):
    v,n,h,ell=data; m=len(v)
    aa=[(y[0]*n[i][0]+y[1]*n[i][1])/h[i] for i in range(m)]
    phi=sum(h[i]*ell[i]*A(aa[i]) for i in range(m))
    B=sum(h[i]*ell[i]/2*(-aa[i]**2*Ap(aa[i])-2*A(aa[i])**2) for i in range(m))
    for i in range(m):
        j=(i+1)%m
        det=abs(n[i][0]*n[j][1]-n[i][1]*n[j][0])
        lo,hi=sorted((aa[i],aa[j]));gam=h[i]*h[j]/det
        B+=gam*simpson(lambda t: A(t)-A(hi),lo,hi)
    return phi,B

def exact_deficit(data,y,p):
    v,n,h,ell=data; d=(y[0]/p,y[1]/p)
    angles=[0,2*math.pi]
    for x,z in v:
        angles.extend([math.atan2(z,x)%(2*math.pi),math.atan2(z+d[1],x+d[0])%(2*math.pi)])
    angles=sorted(set(angles))
    def integrand(theta):
        ux,uy=math.cos(theta),math.sin(theta)
        projections=[n[i][0]*ux+n[i][1]*uy for i in range(len(h))]
        rs=[h[i]/proj for i,proj in enumerate(projections) if proj>1e-14]
        rt=[(h[i]+n[i][0]*d[0]+n[i][1]*d[1])/proj for i,proj in enumerate(projections) if proj>1e-14]
        r=min(rs); rx=min(rt)
        z=p*math.log(rx/r)
        return .5*p*r*r*(-math.expm1(-2*A(z)/p))
    return sum(simpson(integrand,a,b,eps=8e-12) for a,b in zip(angles,angles[1:]) if b>a)

def run():
    cases=[
        ([(-1.0,-.8),(2.0,0),(-.6,1.2)],(.6,-.3)),
        ([(1.3,0),(.5,1.1),(-.85,.6),(-.9,-.85),(.55,-1.3)],(.4,.9)),
        ([(-1,-1),(1,-1),(1,1),(-1,1)],(.6,.3)),
    ]
    checked=0
    for vertices,y in cases:
        data=polygon(vertices);phi,B=target(data,y)
        errs=[]
        for p in [64,256,1024]:
            Hp=exact_deficit(data,y,p)
            err=abs(p*(Hp-phi)-B)
            errs.append(err)
            if p==1024: assert err<.013, (vertices,err,B)
            checked+=1
        assert errs[2]<errs[1]<errs[0],errs
    tri=polygon([(-1,-1),(2,-1),(-1,2)])
    # The cubic odd correction equals -9 t^3/4 + O(t^5).
    ts=(.08,.04)
    odd=[]
    for t in ts:
        odd.append((target(tri,(t,t))[1]-target(tri,(-t,-t))[1])/t**3)
    assert abs(odd[-1]+9/4)<.012,odd
    assert abs(odd[-1]+9/4)<abs(odd[0]+9/4),odd
    print('VERIFY_OK polygons=3 angular_integrals=9 cubic_asymmetry=2')

if __name__=='__main__':run()
