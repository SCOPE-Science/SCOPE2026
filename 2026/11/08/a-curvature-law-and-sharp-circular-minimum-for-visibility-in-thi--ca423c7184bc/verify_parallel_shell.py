"""Independent numerical diagnostics for thin inner-parallel convex shells.

The proof of the limiting theorem is analytic. This script uses the exact
circle visibility integral and chord clipping against supporting halfplanes
of an inner-parallel ellipse. It does not certify the limiting theorem.
"""
import math, random
from statistics import mean

PI=math.pi

def simpson(f,a,b,n=4096):
    h=(b-a)/n
    total=f(a)+f(b)
    for i in range(1,n): total+=(4 if i%2 else 2)*f(a+i*h)
    return h*total/3

def coefficient(a,b):
    def speed(t):return math.hypot(a*math.sin(t),b*math.cos(t))
    P=simpson(speed,0,2*PI)
    I=simpson(lambda t:speed(t)**2.5/math.sqrt(a*b),0,2*PI)
    return 8*math.sqrt(2)*I/(3*P*P), P

def exact_disk(eps):
    t=1-eps
    return 2*(math.acos(t)-t*math.sqrt(1-t*t))/(PI*(1-t*t))

def ellipse_sample(a,b,eps,rng):
    while True:
        t=2*PI*rng.random()
        speed=math.hypot(a*math.sin(t),b*math.cos(t))
        if rng.random()*a<=speed: break
    curvature=a*b/(speed**3)
    while True:
        u=eps*rng.random()
        if rng.random()<=1-curvature*u:break
    nx=(math.cos(t)/a);ny=(math.sin(t)/b)
    norm=math.hypot(nx,ny)
    return a*math.cos(t)-u*nx/norm,b*math.sin(t)-u*ny/norm

def halfplanes(a,b,eps,count):
    ans=[]
    for i in range(count):
        t=2*PI*i/count
        nx,ny=math.cos(t),math.sin(t)
        support=math.hypot(a*nx,b*ny)-eps
        ans.append((nx,ny,support))
    return ans

def chord_hits_inner(x,y,planes):
    px,py=x; vx,vy=y[0]-px,y[1]-py
    lo,hi=0.,1.
    for nx,ny,h in planes:
        u=nx*px+ny*py-h
        v=nx*vx+ny*vy
        if abs(v)<1e-15:
            if u>0:return False
        elif v>0:
            hi=min(hi,-u/v)
        else:
            lo=max(lo,-u/v)
        if lo>hi:return False
    return True

def check():
    c,p=coefficient(1,1)
    assert abs(c-4*math.sqrt(2)/(3*PI))<1e-11
    for eps in (0.08,0.02,0.005,0.001):
        observed=exact_disk(eps)/math.sqrt(eps)
        print('disk eps=',eps,'exact scaled=',round(observed,8),'limit=',round(c,8))
        assert abs(observed/c-1)<.04
    e,p=coefficient(2,1)
    lower=8/(3*math.sqrt(PI*p))
    print('ellipse a/b=2: perimeter=',p,'coefficient=',e,'circle fixed-perimeter bound=',lower)
    assert e>lower*1.19
    rng=random.Random(402619)
    for eps in (.02,.005):
        # Increasing the halfplane count makes the finite polygon approach the true eroded ellipse.
        planes=halfplanes(2,1,eps,720)
        n=60000
        visible=0
        for i in range(n):
            x=ellipse_sample(2,1,eps,rng)
            y=ellipse_sample(2,1,eps,rng)
            visible+=not chord_hits_inner(x,y,planes)
        estimate=visible/n
        predicted=e*math.sqrt(eps)
        se=math.sqrt(estimate*(1-estimate)/n)
        print('ellipse eps=',eps,'visible=',visible,'N=',n,'estimated=',round(estimate,7),'asymptotic=',round(predicted,7),'SE=',round(se,7))
        assert abs(estimate-predicted)<5*se+.004
    print('INNER_PARALLEL_SHELL_TESTS_OK')
if __name__=='__main__': check()
