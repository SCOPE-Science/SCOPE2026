"""Check rotated scaled ellipse overlap numerically by direct polar quadrature.
The checks provide finite corroboration, not a universal proof.
"""
from math import sin,cos,tan,pi,sqrt,atan,asin

def area_formula(a,b,k,theta):
    d=(a*a-b*b)/(a*b)*abs(sin(theta))
    lam=(d+sqrt(d*d+4))/2
    if lam<=k:
        return pi*a*b
    phi=atan(sqrt((k*k-lam**-2)/(lam*lam-k*k)))
    return 2*a*b*(phi+k*k*(pi/2-atan(lam*lam*tan(phi))))

def area_numeric(a,b,k,theta,n=32768):
    C=cos(theta);S=sin(theta)
    total=0.0
    for j in range(n):
        v=(j+0.5)*2*pi/n
        x=cos(v);y=sin(v)
        q0=x*x/a**2+y*y/b**2
        xx=C*x+S*y;yy=-S*x+C*y
        q1=(xx*xx/a**2+yy*yy/b**2)/k**2
        total+=1/max(q0,q1)
    return pi*total/n

count=0;errmax=0
for a,b in ((2,1),(3,1),(7,2),(1.5,1)):
    for k in (1.02,1.25,(1+a/b)/2,1.05*a/b):
        for th in (0,.15,.5,.9,1.2,pi/2):
            direct=area_numeric(a,b,k,th)
            pred=area_formula(a,b,k,th)
            err=abs(direct-pred)
            assert err<2e-6,(a,b,k,th,pred,direct,err)
            errmax=max(errmax,err);count+=1
        if k<a/b:
            d=(a*a-b*b)/(a*b)
            tc=asin((k-1/k)/d)
            assert abs(area_formula(a,b,k,tc)-pi*a*b)<1e-9
            for i in range(1,12):
                t=tc+(pi/2-tc)*i/12
                assert area_formula(a,b,k,t)<area_formula(a,b,k,t-1e-5)
            count+=12
# Directly test the predicted three-halves tangency coefficient on both sides
# of the narrow crossing region; these tests are not an infinite proof.
for a,b in ((2,1),(3,1),(7,2),(1.5,1)):
    k=(1+a/b)/2
    q=(a*a-b*b)/(a*b)
    tc=asin((k-1/k)/q)
    L=q*k*k*cos(tc)/(1+k*k)
    K=4*a*b/3*(2*L/k)**1.5/sqrt(1-k**-4)
    for t in (0.001,0.0005):
        ratio=(pi*a*b-area_formula(a,b,k,tc+t))/(K*t**1.5)
        assert abs(ratio-1)<0.04,(a,b,k,t,ratio)
        count+=1
print(f'SCALED_ELLIPSE_CHECK_OK comparisons={count} max_abs_discrepancy={errmax:.3g}')
