"""Reproduce finite checks for a sharp first-step compressed Armijo bound.

Uses Python's standard library only; numerical checks supplement the proof.
"""
import math
import random


def rmax(k):
    t=(k-1)/math.sqrt(2*k)
    return ((math.sqrt(t*t+4)+t)/2)**2


def kcrit(sigma):
    a=1+sigma*sigma/(1-sigma)
    return a+math.sqrt(a*a-1)


def make_q(k, phi):
    c,s=math.cos(phi),math.sin(phi)
    return (1+(k-1)*c*c,(k-1)*s*c,1+(k-1)*s*s)


def dot_q(q,v):
    a,b,d=q
    x,y=v
    return a*x*x+2*b*x*y+d*y*y


def test():
    rng=random.Random(827419)
    checked=0
    for k in (1., 1.01, 1.5, 2.,(3+math.sqrt(5))/2, 3., 10., 100.):
        R=rmax(k)
        for j in range(360):
            phi=(j+.317)*math.pi/180
            q=make_q(k,phi)
            # random gradient within top-1 selection cone
            theta=rng.random()*math.pi/4
            g=(math.cos(theta), math.sin(theta))
            r=q[0]/dot_q(q,g)
            assert r <= R+4e-13, (k,phi,theta,r,R)
            checked += 1
        # Independently search the rotation at a gradient tie.
        maximum=max(make_q(k,j*math.pi/100000)[0]/dot_q(make_q(k,j*math.pi/100000), (math.sqrt(.5),math.sqrt(.5))) for j in range(100000))
        assert abs(maximum-R)<1e-7, (k,maximum,R)
        checked += 1
    for sig in (.1,.5,.8):
        k=kcrit(sig)
        assert abs((1-sig)*rmax(k)-1)<1e-12
        checked += 1
    # direct comparison to the quadratic objective, on genuinely compressed steps
    for _ in range(1000):
        k=1+10**rng.uniform(-1,2)
        phi=rng.random()*2*math.pi
        q=make_q(k,phi)
        gx,gy=rng.uniform(-2,2),rng.uniform(-2,2)
        if gx*gx+gy*gy<1e-7:
            continue
        sig=.5
        alpha=2*(1-sig)*(gx*gx+gy*gy)/dot_q(q,(gx,gy))
        a=1/((1-sig)*rmax(k))
        i=0 if abs(gx)>=abs(gy) else 1
        dx=(-a*alpha*gx,0.) if i==0 else (0.,-a*alpha*gy)
        determinant=q[0]*q[2]-q[1]*q[1]
        x=((q[2]*gx-q[1]*gy)/determinant, (q[0]*gy-q[1]*gx)/determinant)
        def energy(y): return .5*dot_q(q,y)
        new=(x[0]+dx[0],x[1]+dx[1])
        delta=energy(new)-energy(x)
        assert delta<=1e-8*max(1,energy(x)),(q,x,delta)
        checked+=1
    # Construct a strict top-1 witness for k=3 and sigma=1/2.
    k=3.
    gradient=(math.cos(math.pi/4-1e-5),math.sin(math.pi/4-1e-5))
    best_r=-1.;best_phi=0.
    for j in range(100000):
        phi=2*math.pi*j/100000
        q=make_q(k,phi)
        r=q[0]/dot_q(q,gradient)
        if r>best_r: best_r=r;best_phi=phi
    assert best_r>2
    q=make_q(k,best_phi)
    sig=.5
    alpha=2*(1-sig)/dot_q(q,gradient)
    delta=-alpha*gradient[0]**2+.5*alpha**2*gradient[0]**2*q[0]
    assert delta>0
    checked+=1
    print('VERIFIED', checked, 'checks; golden threshold',kcrit(.5),'strict witness objective increase',delta)

if __name__=='__main__':test()
