"""Independent numerical consistency tests for axial ellipsoid formulas.
Run: python verify_lens.py ; this does not certify originality or replace the proof.
"""
import math
import random

def ellipsoid(n,R,r,d):
    assert n>=2 and R>=r>0 and R-r<d<R+r
    l=d-r; u=R; t=(d*d+R*R-r*r)/(2*d)
    h2=max(0,R*R-t*t)
    d0=-r/n+math.sqrt(R*R-r*r*(1-1/n**2))
    if d<=d0:
        return d,r,r,'smaller'
    if d<n*(R-r):
        return (l+n*t)/(n+1), n*(t-l)/(n+1), n*math.sqrt(h2)/math.sqrt(n*n-1),'pole+rim'
    k=(R-r)/d
    return (l+u)/2, (u-l)/2, math.sqrt(h2/(1-k*k)),'two_poles+rim'

rng=random.Random(311029)
case_count=0; max_error=0.0; max_certificate_error=0.0
for n in (2,3,4,5,10):
    for _ in range(250):
        r=0.2+2*rng.random();R=r*(1+2.5*rng.random());d=R-r+2*r*(0.0001+0.9998*rng.random())
        c,A,B,phase=ellipsoid(n,R,r,d)
        l=d-r;u=R;t=(d*d+R*R-r*r)/(2*d)
        for j in range(60):
            x=l+(u-l)*j/59
            h2=min(R*R-x*x,r*r-(x-d)**2)
            q=((x-c)/A)**2 + max(h2,0)/(B*B)
            max_error=max(max_error,q-1)
            assert q<=1+3e-9,(n,R,r,d,phase,q)
        assert A<=B+1e-9
        if phase=='smaller':
            nx=-1/n; w=n/(n+1)
            mean=(1-w)*(-1)+w*(1/n)
            xx=(1-w)+w/n**2
            yy=w*(1-1/n**2)/(n-1)
        elif phase=='pole+rim':
            w=n/(n+1)
            mean=(1-w)*(-1)+w/n
            xx=(1-w)+w/n**2
            yy=w*(1-1/n**2)/(n-1)
        else:
            k=(R-r)/d;w=(n-1)/(n*(1-k*k))
            pm=(1-w+w*k)/2;pp=(1-w-w*k)/2
            assert min(pm,pp,w)>=-1e-12
            mean=-pm+pp+w*k
            xx=pm+pp+w*k*k
            yy=w*(1-k*k)/(n-1)
        max_certificate_error=max(max_certificate_error,abs(mean),abs(xx-1/n),abs(yy-1/n))
        assert max_certificate_error<2e-12
        case_count+=1
print('cases=',case_count,'maximum containment excess=',max_error,'maximum moment residual=',max_certificate_error)
for n in (2,3,5):
    for R,r in ((1.,1.),(2.,1.),(4.,1.)):
        # compare shared boundaries from both sides
        ds=[-r/n+math.sqrt(R*R-r*r*(1-1/n**2)),n*(R-r)]
        for d in ds:
            if R-r+1e-7<d<R+r-1e-7:
                ellipsoid(n,R,r,d*(1-1e-9));ellipsoid(n,R,r,d*(1+1e-9))
print('phase-boundary probes passed')
