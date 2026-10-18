#!/usr/bin/env python3
"""Reproducibility checks for a two-line Crofton angular signature of parallelograms.
This program is experimental corroboration and is not an infinite proof.
"""
import cmath, math, random

PI=math.pi

def predicted(a,b,phi,k):
    p=a/(a+b)
    return (1-4*p*(1-p)*math.sin(k*phi)**2)/((4*k*k-1)**2)

def reconstruct(t1,t2):
    A=9*t1; B=225*t2
    if not (0 <= A < 1 and (2*A-1)**2 <= B+1e-10 and B<=1+1e-10):
        raise ValueError('inadmissible exact data')
    q=1-A
    r=(1-B)/(4*q)
    r=max(0,min(1,r))
    phi=math.acos(math.sqrt(r))
    eta=q/(1-r)
    eta=max(0,min(1,eta))
    p=(1+math.sqrt(1-eta))/2
    return p/(1-p), phi

def width(a,b,phi,theta):
    return a*abs(math.sin(theta))+b*abs(math.sin(theta-phi))

def numerical_coeff(a,b,phi,k,n=8192):
    vals=[width(a,b,phi,(j+0.5)*PI/n) for j in range(n)]
    denom=sum(vals)
    z=sum(v*cmath.exp(2j*k*((j+0.5)*PI/n)) for j,v in enumerate(vals))/denom
    return abs(z)**2

def sample_angle(rng,a,b,phi):
    while True:
        theta=rng.random()*PI
        if rng.random()*(a+b) <= width(a,b,phi,theta):
            return theta

def monte_carlo(rng,a,b,phi,count):
    ss=[0.,0.]
    for _ in range(count):
        u=sample_angle(rng,a,b,phi)
        v=sample_angle(rng,a,b,phi)
        for k in (1,2):
            ss[k-1]+=math.cos(2*k*(u-v))
    return [z/count for z in ss]

def sample_line_direct(rng,a,b,phi):
    # Draw from an isotropic line window, reject unless the line meets the polygon.
    vx=(a/2,0); wy=(b*math.cos(phi)/2,b*math.sin(phi)/2)
    vertices=[(sx*vx[0]+sy*wy[0],sx*vx[1]+sy*wy[1])
              for sx in (-1,1) for sy in (-1,1)]
    radius=(a+b)/2
    while True:
        theta=rng.random()*PI
        t=(2*rng.random()-1)*radius
        nx,ny=math.cos(theta),math.sin(theta)
        vals=[x*nx+y*ny for x,y in vertices]
        if min(vals)<=t<=max(vals):
            return theta

def direct_monte_carlo(rng,a,b,phi,count):
    ss=[0.,0.]
    for _ in range(count):
        u=sample_line_direct(rng,a,b,phi)
        v=sample_line_direct(rng,a,b,phi)
        ss[0]+=math.cos(2*(u-v))
        ss[1]+=math.cos(4*(u-v))
    return [z/count for z in ss]

def run():
    rng=random.Random(1729)
    quadratures=0
    for a,b,phi in [(1,1,PI/2),(2,1,PI/2),(1,1,PI/4),(3,1,PI/3),(1.2,4,1.11)]:
        for k in (1,2,3,4):
            lhs=numerical_coeff(a,b,phi,k)
            rhs=predicted(a,b,phi,k)
            assert abs(lhs-rhs)<1e-7,(a,b,phi,k,lhs,rhs)
            quadratures+=1
    inverse_cases=0
    for _ in range(1500):
        a=math.exp(rng.uniform(-2,2));b=math.exp(rng.uniform(-2,2))
        phi=rng.uniform(0.08,PI/2)
        t1,t2=(predicted(a,b,phi,k) for k in (1,2))
        ratio,angle=reconstruct(t1,t2)
        assert abs(ratio-max(a,b)/min(a,b))<5e-9*max(1,ratio),(a,b,phi,ratio)
        assert abs(angle-phi)<2e-9,(a,b,phi,angle)
        A,B=9*t1,225*t2
        assert B+1e-10 >= (2*A-1)**2 and B<=1+1e-10
        inverse_cases+=1
    # Same first harmonic but demonstrably different shape and second harmonic.
    t1rect=predicted(2,1,PI/2,1)
    t1rhomb=predicted(1,1,math.asin(2*math.sqrt(2)/3),1)
    assert abs(t1rect-1/81)<1e-13 and abs(t1rect-t1rhomb)<1e-13
    assert abs(predicted(2,1,PI/2,2)-1/225)<1e-13
    assert abs(predicted(1,1,math.asin(2*math.sqrt(2)/3),2)-49/18225)<1e-13
    mc_cases=0
    for a,b,phi in [(2,1,PI/2),(1,1,PI/4),(3,1.5,1.22)]:
        values=monte_carlo(rng,a,b,phi,110000)
        for k in (1,2):
            assert abs(values[k-1]-predicted(a,b,phi,k))<0.013,(a,b,phi,k,values[k-1],predicted(a,b,phi,k))
        mc_cases+=1
    direct_cases=0
    for a,b,phi in [(1,1,PI/2),(2,1,PI/2),(1,1,PI/4)]:
        values=direct_monte_carlo(rng,a,b,phi,35000)
        for k in (1,2):
            assert abs(values[k-1]-predicted(a,b,phi,k))<0.027,(a,b,phi,k,values[k-1],predicted(a,b,phi,k))
        direct_cases+=1
    print('CROFTON_PAIR_ANGLE_OK quadratures=%d inverse_cases=%d width_weighted_shapes=%d direct_line_shapes=%d pairs_per_shape=110000'% (quadratures,inverse_cases,mc_cases,direct_cases))

if __name__=='__main__':run()
