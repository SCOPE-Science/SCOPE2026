#!/usr/bin/env python3
"""Reproduce the two-vector shift-invert exponential projection results (stdlib only)."""
import math
import random
from fractions import Fraction as F

CHECKS = 0

def check(pred, context):
    global CHECKS
    if not pred: raise AssertionError(context)
    CHECKS += 1

def close(a, b, tol=2e-9):
    check(abs(a-b) <= tol*(1+abs(a)+abs(b)), ('mismatch',a,b))

def analytic(lam, b, g):
    norm2=sum(x*x for x in b)
    p=[x*x/norm2 for x in b]
    r=[1/(1+g*x) for x in lam]
    mu=sum(x*y for x,y in zip(p,r))
    var=sum(x*(y-mu)**2 for x,y in zip(p,r))
    if var < 1e-22: raise ValueError('degenerate active spectrum')
    s=math.sqrt(var)
    nu=sum(x*y*(y-mu)**2 for x,y in zip(p,r))/var
    delta=math.hypot(mu-nu,2*s)
    eta_hi=(mu+nu+delta)/2
    eta_lo=(mu+nu-delta)/2
    q=(eta_hi-mu)/var
    alpha2=1/(1+q*q*var)
    c=[alpha2*(1+q*(x-mu)) for x in r]
    theta_s=(1/eta_hi-1)/g
    theta_f=(1/eta_lo-1)/g
    return r,mu,var,nu,eta_hi,eta_lo,c,theta_s,theta_f

def direct(lam,b,g,t):
    """Direct orthogonalized two-dimensional SAI Ritz-matrix method, not c_i formula."""
    n=len(lam)
    norm=math.sqrt(sum(x*x for x in b))
    v0=[x/norm for x in b]
    r=[1/(1+g*x) for x in lam]
    v1=[x*y for x,y in zip(v0,r)]
    proj=sum(x*y for x,y in zip(v0,v1))
    v1=[x-proj*y for x,y in zip(v1,v0)]
    u=math.sqrt(sum(x*x for x in v1))
    v1=[x/u for x in v1]
    j00=sum(x*x*y for x,y in zip(v0,r))
    j01=sum(x*y*z for x,y,z in zip(v0,v1,r))
    j11=sum(x*x*y for x,y in zip(v1,r))
    det=j00*j11-j01*j01
    h00=(j11/det-1)/g
    h01=-j01/det/g
    h11=(j00/det-1)/g
    # 2x2 symmetric exponential, computed via explicit Cayley-Hamilton formula.
    mid=(h00+h11)/2
    gap=math.hypot(h00-h11,2*h01)
    lam1=mid-gap/2
    lam2=mid+gap/2
    e1=math.exp(-t*lam1)
    e2=math.exp(-t*lam2)
    d=(e1-e2)/(lam1-lam2)
    m00=e2+d*(h00-lam2)
    m10=d*h01
    return [norm*(m00*x+m10*y) for x,y in zip(v0,v1)]

def run():
    # Exact-rational moments and a strict algebraic sign certificate.
    rr=[F(1,2),F(1,3),F(1,5)]
    mu=sum(rr)/3
    v=sum((x-mu)**2 for x in rr)/3
    nu=(sum(x*(x-mu)**2 for x in rr)/3)/v
    check(mu==F(31,90),'mu exact')
    check(v==F(61,4050),'variance exact')
    check(nu==F(991,2745),'nu exact')
    check(559*559*241 > 6989*6989,'exact negativity certificate')
    lam=[1.,2.,4.]; b=[1.,1.,1.]; g=1.
    r,mu,var,nu,ep,em,c,ts,tf=analytic(lam,b,g)
    close(ep,(1291+29*math.sqrt(241))/3660)
    close(em,(1291-29*math.sqrt(241))/3660)
    close(ts,(891-29*math.sqrt(241))/400)
    close(tf,(891+29*math.sqrt(241))/400)
    close(c[-1],.5-559*math.sqrt(241)/13978)
    check(c[-1]<0,'rightmost component negative slow coefficient')
    tstar=math.log((1-c[-1])/(-c[-1]))/(tf-ts)
    close(tstar,0.9895190863326178)
    for scale in [.01,.5,1,2,10]:
        vdir=direct(lam,b,g,tstar*scale)
        vform=[bb*(cc*math.exp(-ts*tstar*scale)+(1-cc)*math.exp(-tf*tstar*scale)) for bb,cc in zip(b,c)]
        for x,y in zip(vdir,vform):close(x,y)
    close(direct(lam,b,g,tstar)[-1],0,1e-8)
    check(direct(lam,b,g,.5*tstar)[-1]>0,'pre-horizon positive')
    check(direct(lam,b,g,2*tstar)[-1]<0,'post-horizon negative')
    rand=random.Random(416351)
    for n in (3,4,6,9):
      for _ in range(350):
        # Distinct well-separated positive spectral levels.
        lam=sorted(math.exp(rand.uniform(-2,2)+i*.08) for i in range(n))
        b=[math.exp(rand.uniform(-1,1)) for _ in range(n)]
        g=math.exp(rand.uniform(-3,3))
        r,mu,var,nu,ep,em,c,ts,tf=analytic(lam,b,g)
        for ri, ci in zip(r,c):close(ci,(ri-em)/(ep-em))
        check(0<em<ep<1,'inverse compressed eigenvalues')
        check(ts<tf,'sorted effective exponential decay eigenvalues')
        check(c[-1]<-1e-12,'uniform pole no-go')
        check(all(c[i]<c[i-1] for i in range(1,n)),'slow coefficients monotone')
        t=math.log((1-c[-1])/(-c[-1]))/(tf-ts)
        check(t>0 and math.isfinite(t),'finite onset')
        test_times=[0.,.2*t,t,.9*t,1.1*t,2*t]
        for tt in test_times:
            est=direct(lam,b,g,tt)
            expected=[bb*(cc*math.exp(-ts*tt)+(1-cc)*math.exp(-tf*tt)) for bb,cc in zip(b,c)]
            for ee,ff in zip(est,expected):close(ee,ff,4e-9)
        check(direct(lam,b,g,.5*t)[-1]>0,'early largest coordinate')
        check(direct(lam,b,g,1.5*t)[-1]<0,'late largest coordinate')
        # all coordinates positive strictly before the earliest threshold
        check(min(direct(lam,b,g,.5*t))>0,'global early positivity')
    # Independent polynomial-Lanczos Ritz benchmark and stiff-limit separation.
    sqrt79=math.sqrt(79)
    limiting=math.log((179+20*sqrt79)/21)/(4*sqrt79)
    close(limiting,0.0796717425124724)
    horizons=[]
    for L in [100.,1000.,10000.]:
        lam=[1.,2.,L]
        r,mu,var,nu,ep,em,c,ts,tf=analytic(lam,[1.,1.,1.],1.)
        t_sai=math.log((1-c[-1])/(-c[-1]))/(tf-ts)
        a=sum(lam)/3
        v=sum((x-a)**2 for x in lam)/3
        d=sum(x*(x-a)**2 for x in lam)/(3*v)
        delta=math.hypot(a-d,2*math.sqrt(v))
        thlo=(a+d-delta)/2
        thhi=(a+d+delta)/2
        t_poly=math.log((L-thlo)/(L-thhi))/(thhi-thlo)
        check(t_poly>0 and t_sai>0,'positive finite horizons')
        check(t_sai>limiting,'SAI limit approached from above')
        check(abs(t_sai-limiting)<3.3/L,'quantitative limiting horizon')
        check(abs(t_poly/(2*math.log(L)/L)-1)<0.5/math.log(L),'polynomial asymptotic')
        horizons.append((t_sai,t_poly))
    check(all(horizons[k][0]/horizons[k][1]<horizons[k+1][0]/horizons[k+1][1] for k in (0,1)), 'diverging relative positivity horizon')
    print('PASS',CHECKS,'stdlib exact-rational, direct projection, stiffness, and deterministic stress checks')
if __name__=='__main__':run()
