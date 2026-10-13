#!/usr/bin/env python3
import math

PI = math.pi

def phi_entries(nu, R, a, mu, lam):
    if nu == 0.0:
        p11 = -mu/(4*PI)
        p12 = -1.0/(4*PI*a)
        p22 = 1.0/lam - 1.0/(4*PI*R)
        return p11, p12, p22
    p11 = (nu-mu)/(4*PI)
    p12 = -math.exp(-nu*a)*math.sinh(nu*R)/(4*PI*nu*a*R)
    p22 = 1.0/lam - math.exp(-nu*R)*math.sinh(nu*R)/(4*PI*nu*R*R)
    return p11, p12, p22

def det_phi(nu, R, a, mu, lam):
    p11,p12,p22 = phi_entries(nu,R,a,mu,lam)
    return p11*p22-p12*p12

def Dval(R,a,mu,lam):
    return mu/R - 4*PI*mu/lam - 1/(a*a)

def roots(R,a,mu,lam,hi=3.0,n=60000):
    xs=[]
    x0=0.0
    f0=det_phi(x0,R,a,mu,lam)
    for i in range(1,n+1):
        x1=hi*i/n
        f1=det_phi(x1,R,a,mu,lam)
        if f0 == 0.0:
            xs.append(x0)
        elif f0*f1 < 0.0:
            lo,hh=x0,x1
            flo=f0
            for _ in range(70):
                mid=(lo+hh)/2
                fm=det_phi(mid,R,a,mu,lam)
                if flo*fm <= 0:
                    hh=mid
                else:
                    lo=mid; flo=fm
            xs.append((lo+hh)/2)
        x0,f0=x1,f1
    # deduplicate
    out=[]
    for x in xs:
        if not out or abs(x-out[-1])>1e-7:
            out.append(x)
    return out

# Exact zero-energy determinant identity, checked numerically at representative points.
for R,a,mu,lam in [(1,2,1,10),(1,2,1,20),(1.3,2.7,.8,17.0)]:
    lhs=det_phi(0,R,a,mu,lam)
    rhs=Dval(R,a,mu,lam)/(16*PI*PI)
    assert abs(lhs-rhs) < 2e-14

r10=roots(1,2,1,10,hi=2.0,n=25000)
r20=roots(1,2,1,20,hi=2.0,n=25000)
assert len(r10)==1, r10
assert len(r20)==2, r20
assert Dval(1,2,1,10) < 0
assert Dval(1,2,1,20) > 0

# Generic onset: R=mu=1,a=2 predicts E/D^2 -> -16.
R=a0=mu=1.0
a0=2.0
lc=4*PI*mu*R*a0*a0/(mu*a0*a0-R)
eps=1e-4
lam=lc*(1+eps)
rr=roots(R,a0,mu,lam,hi=1.5,n=40000)
small=min(rr)
ratio_g=-(small*small)/(Dval(R,a0,mu,lam)**2)
assert abs(ratio_g+16.0) < 0.08, ratio_g

# Exceptional onset: R=1,a=2,mu=1/2 predicts E/D -> -4/3.
R=1.0; a0=2.0; mu=0.5
lc=4*PI*mu*R*a0*a0/(mu*a0*a0-R)
eps=1e-5
lam=lc*(1+eps)
rr=roots(R,a0,mu,lam,hi=1.5,n=60000)
small=min(rr)
ratio_e=-(small*small)/Dval(R,a0,mu,lam)
assert abs(ratio_e+4/3) < 0.012, ratio_e

print('VERIFY_OK one_roots=%d two_roots=%d generic_ratio=%.9f exceptional_ratio=%.9f' % (len(r10),len(r20),ratio_g,ratio_e))
