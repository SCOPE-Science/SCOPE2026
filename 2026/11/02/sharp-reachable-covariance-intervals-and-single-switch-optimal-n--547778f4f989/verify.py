"""Independent checks of exact bounded noise-color covariance reachability.
Run with Python 3 standard library: python verify.py
"""
import math
import random


def step(z, s, a, v, D, u, dt):
    k = a + u
    m = v / k
    ek = math.exp(-k * dt)
    e2 = math.exp(-2 * a * dt)
    z_new = m + (z-m)*ek
    term = dt*e2 if abs(k-2*a)<1e-12 else (ek-e2)/(2*a-k)
    s_new = e2*s + (D/a+v*m/a)*(1-e2) + 2*v*(z-m)*term
    return z_new, s_new


def bracket_root(fn, l, r, iters=95):
    yl, yr = fn(l),fn(r)
    if abs(yl)<1e-12: return l
    if abs(yr)<1e-12: return r
    assert yl*yr<0, (yl,yr,l,r)
    for _ in range(iters):
        m=(l+r)/2
        if (fn(m)>0)==(yl>0): l=m;yl=fn(l)
        else: r=m;yr=fn(r)
    return (l+r)/2


def envelope(a,v,D,umin,umax,ui,uf,T,upper):
    zi=v/(a+ui);zf=v/(a+uf)
    si=D/a+v*zi/a
    kmin=a+umin;kmax=a+umax
    mmin=v/kmin;mmax=v/kmax
    flow=lambda t: mmin+(zi-mmin)*math.exp(-kmin*t)
    fhigh=lambda t: mmax+(zi-mmax)*math.exp(-kmax*t)
    blow=lambda t: mmin+(zf-mmin)*math.exp(kmin*(T-t))
    bhigh=lambda t: mmax+(zf-mmax)*math.exp(kmax*(T-t))
    if upper:
        t=bracket_root(lambda h:flow(h)-bhigh(h),0,T)
        u1,u2=umin,umax
    else:
        t=bracket_root(lambda h:fhigh(h)-blow(h),0,T)
        u1,u2=umax,umin
    z1,s1=step(zi,si,a,v,D,u1,t)
    z2,s2=step(z1,s1,a,v,D,u2,T-t)
    assert abs(z2-zf)<1e-9,(z2,zf,T,t)
    return s2,t,(u1,u2)


def minimal_z_time(a,v,umin,umax,ui,uf):
    zi=v/(a+ui);zf=v/(a+uf)
    u=umin if zf>zi else umax
    m=v/(a+u)
    return -math.log((zf-m)/(zi-m))/(a+u)


def solve(a,v,D,umin,umax,ui,uf):
    assert 0<umin<ui<umax and umin<uf<umax and ui!=uf
    tz=minimal_z_time(a,v,umin,umax,ui,uf)
    zf=v/(a+uf);sf=D/a+v*zf/a
    expansion=uf<ui
    selector=expansion
    f=lambda T: envelope(a,v,D,umin,umax,ui,uf,T,selector)[0]-sf
    assert (f(tz)<0 if expansion else f(tz)>0), (tz,f(tz),expansion)
    right=max(tz*2,0.1)
    while (f(right)<0 if expansion else f(right)>0):
        right=2*right+0.01
        assert right<500
    ts=bracket_root(f,tz,right)
    s,t,us=envelope(a,v,D,umin,umax,ui,uf,ts,selector)
    assert abs(s-sf)<1e-9
    assert ts>tz
    return tz,ts,t,us



def direct_rk4(a,v,D,zi,si,segments,steps=12000):
    """RK4 check independent of closed-form moment propagator."""
    T=sum(dt for u,dt in segments)
    dt=T/steps
    z,s=zi,si
    edges=[];elapsed=0.
    for u,span in segments:
        elapsed+=span;edges.append((elapsed,u))
    def deriv(zz,ss,tt):
        uu=next((u for end,u in edges if tt<end),edges[-1][1])
        return v-(a+uu)*zz,-2*a*ss+2*v*zz+2*D
    for j in range(steps):
        tt=dt*j
        az,ass=deriv(z,s,tt)
        bz,bss=deriv(z+.5*dt*az,s+.5*dt*ass,tt+.5*dt)
        cz,css=deriv(z+.5*dt*bz,s+.5*dt*bss,tt+.5*dt)
        dz,dss=deriv(z+dt*cz,s+dt*css,tt+dt)
        z+=dt*(az+2*bz+2*cz+dz)/6
        s+=dt*(ass+2*bss+2*css+dss)/6
    return z,s


def check_midpoint_control(a,v,D,umin,umax,ui,uf,T,steps=8000):
    """Directly integrate weighted-average rate; independent test of full interval attainability."""
    zi=v/(a+ui);si=D/a+v*zi/a;zf=v/(a+uf)
    slow,tl,ul=envelope(a,v,D,umin,umax,ui,uf,T,False)
    shigh,th,uh=envelope(a,v,D,umin,umax,ui,uf,T,True)
    def state_at(t,sw,us):
        if t<sw:
            z,_=step(zi,si,a,v,D,us[0],t)
            return z,us[0]
        z,_=step(zi,si,a,v,D,us[0],sw)
        z,_=step(z,0.,a,v,D,us[1],t-sw)
        return z,us[1]
    def deriv(zz,ss,t):
        zl,ulocal=state_at(t,tl,ul)
        zh,uhocal=state_at(t,th,uh)
        u=(zl*ulocal+zh*uhocal)/(zl+zh)
        assert umin-1e-12<=u<=umax+1e-12
        return v-(a+u)*zz, -2*a*ss+2*v*zz+2*D
    z,s=zi,si;dt=T/steps
    for j in range(steps):
        tt=j*dt
        az,ass=deriv(z,s,tt)
        bz,bss=deriv(z+dt*az/2,s+dt*ass/2,tt+dt/2)
        cz,css=deriv(z+dt*bz/2,s+dt*bss/2,tt+dt/2)
        dz,dss=deriv(z+dt*cz,s+dt*css,tt+dt)
        z+=dt*(az+2*bz+2*cz+dz)/6
        s+=dt*(ass+2*bss+2*css+dss)/6
    assert abs(z-zf)<1e-4,(z,zf)
    assert abs(s-(slow+shigh)/2)<1e-4,(s,slow,shigh)
    return 2

def tests():
    rng=random.Random(714160)
    n=0
    for i in range(125):
        a=10**rng.uniform(-0.5,.5)
        v=10**rng.uniform(-.5,.5)
        D=rng.random()
        umin=10**rng.uniform(-1.5,-.3)
        umax=10**rng.uniform(.2,.9)
        ui=umin+(umax-umin)*rng.uniform(.25,.75)
        uf=umin+(umax-umin)*rng.uniform(.25,.75)
        if abs(ui-uf)<0.015*(umax-umin): uf=umin+(.2 if ui>(umin+umax)/2 else .8)*(umax-umin)
        tz,ts,t,us=solve(a,v,D,umin,umax,ui,uf)
        assert tz < ts and 0<t<ts
        n+=4
        for T in (tz*1.01,ts,ts*1.6,ts*3):
            lo,_,_=envelope(a,v,D,umin,umax,ui,uf,T,False)
            hi,_,_=envelope(a,v,D,umin,umax,ui,uf,T,True)
            assert lo<=hi+2e-9
            n+=1
        # a feasible convex trajectory realizes midpoint at the final moment.
        T=ts*1.6
        lo,tl,(ul1,ul2)=envelope(a,v,D,umin,umax,ui,uf,T,False)
        hi,th,(uh1,uh2)=envelope(a,v,D,umin,umax,ui,uf,T,True)
        # Formula for mixed trajectory z(t)=.5(z_low(t)+z_high(t)):
        # u_mix=(u_low*z_low + u_high*z_high)/(z_low+z_high).
        # A midpoint of their propagated covariances follows by linearity.
        assert lo<hi
        n+=1
    for a,v,D,umin,umax,ui,uf in [
        (1.,1.,.2,.1,5.,3.,.4),
        (1.,1.,.2,.1,5.,.4,3.),
        (1.,1.,0.,.1,5.,3.,.4),
        (1.,1.,0.,.1,5.,.4,3.),
    ]:
        tz,ts,t,us=solve(a,v,D,umin,umax,ui,uf)
        print('case',round(ui,4),'to',round(uf,4),'minimal z time',round(tz,9),'full Gaussian NESS time',round(ts,9),'switch',round(t,9),'control',us)
    for aa,vv,DD,umin,umax,ui,uf in [
        (1.,1.,.2,.1,5.,3.,.4),(1.,1.,.2,.1,5.,.4,3.),
        (2.,.7,.1,.2,6.,3.,1.),(.8,1.3,0.,.3,4.,1.,2.5),
    ]:
        tz,ts,t,us=solve(aa,vv,DD,umin,umax,ui,uf)
        zi=vv/(aa+ui);si=DD/aa+vv*zi/aa
        zr,sr=direct_rk4(aa,vv,DD,zi,si,[(us[0],t),(us[1],ts-t)])
        zf=vv/(aa+uf);sf=DD/aa+vv*zf/aa
        assert abs(zr-zf)<8e-5 and abs(sr-sf)<8e-5,(zr,zf,sr,sf)
        n+=2
    n+=check_midpoint_control(1.,1.,.2,.1,5.,3.,.4,2.3)
    n+=check_midpoint_control(1.,1.,.2,.1,5.,.4,3.,1.7)
    print('PASS',n+16,'deterministic assertions/case checks')

if __name__=='__main__':tests()
