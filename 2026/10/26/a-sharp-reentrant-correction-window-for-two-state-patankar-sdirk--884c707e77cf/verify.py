"""Reproducible checks for the two-state final-stage Patankar/SDIRK21 result.

Only the Python standard library is required. These finite checks corroborate,
but do not replace, the proof of the universal statements.
"""
import math
import random

GAMMA = 1.0 - 1.0 / math.sqrt(2.0)


def solve_2(mat, vec):
    (a, b), (c, d) = mat
    det = a*d - b*c
    assert det > 0
    return ((d*vec[0]-b*vec[1])/det, (-c*vec[0]+a*vec[1])/det)


def qmul(a, b, vec):
    return (-a*vec[0]+b*vec[1], a*vec[0]-b*vec[1])


def directly_staged(a, b, h, x, eps):
    y0=(x, 1-x)
    mat=((1+h*GAMMA*a,-h*GAMMA*b),
         (-h*GAMMA*a,1+h*GAMMA*b))
    y1=solve_2(mat,y0)
    q1=qmul(a,b,y1)
    rhs=(x+h*(1-GAMMA)*q1[0],1-x+h*(1-GAMMA)*q1[1])
    y2=solve_2(mat,rhs)
    r1=(1-GAMMA)*max(y1[0],0)/max(y2[0],eps)+GAMMA*max(y2[0],0)/max(y2[0],eps)
    r2=(1-GAMMA)*max(y1[1],0)/max(y2[1],eps)+GAMMA*max(y2[1],0)/max(y2[1],eps)
    qm=((1+h*a*r1,-h*b*r2),(-h*a*r1,1+h*b*r2))
    yy=solve_2(qm,y0)
    return y1,y2,yy


def derived(a,b,h,x,eps):
    s=h*(a+b)
    pi=b/(a+b)
    u=pi+(x-pi)/(1+GAMMA*s)
    r=(1+(2*GAMMA-1)*s)/(1+GAMMA*s)**2
    v=pi+(x-pi)*r
    L=(1-GAMMA)*u/max(v,eps)+GAMMA*max(v,0)/max(v,eps)
    M=(1-GAMMA)*(1-u)/max(1-v,eps)+GAMMA*max(1-v,0)/max(1-v,eps)
    out=(x+h*b*M)/(1+h*(a*L+b*M))
    return u,v,out


def approx(a,b,atol=1e-11):
    assert abs(a-b) <= atol*(1+abs(a)+abs(b)), (a,b)


if __name__ == '__main__':
    checks=0
    rng=random.Random(260215271)
    for _ in range(1800):
        a=10**rng.uniform(-1,1)
        b=10**rng.uniform(-1,1)
        h=10**rng.uniform(-2,1)
        x=rng.random()
        eps=10**rng.uniform(-8,-2)
        y1,y2,yy=directly_staged(a,b,h,x,eps)
        u,v,z=derived(a,b,h,x,eps)
        approx(y1[0],u)
        approx(y2[0],v)
        approx(yy[0],z)
        approx(yy[0]+yy[1],1)
        assert 0 <= yy[0] <= 1 and 0 <= yy[1] <= 1
        checks+=5
    # Sharp critical parameter and interior of the negative-predictor window.
    pi_star=3-2*math.sqrt(2)
    sstar=4+3*math.sqrt(2)
    minimum=(1+(2*GAMMA-1)*sstar)/(1+GAMMA*sstar)**2
    approx(minimum,(1-math.sqrt(2))/2)
    approx(pi_star+(1-pi_star)*minimum,0)
    checks+=2
    for pi in (0.01,0.03,0.1,pi_star*0.999,pi_star,pi_star*1.001,0.5):
        a=1-pi;b=pi
        s=sstar
        _,v,_=derived(a,b,s,1,1e-8)
        if pi<pi_star: assert v<0
        else: assert v>=-2e-15
        checks+=1
    for a,b,h,x in [(9.,1.,.8,1.),(1.,9.,.8,0.),(9.,1.,.01,.5),
                     (9.,1.,.8,.5),(9.,1.,5.,1.)]:
        u,v,z=derived(a,b,h,x,1e-12)
        want=min(1.,max(0.,v))
        approx(z,want,atol=1e-7)
        checks+=1
    a=9.;b=1.;h=.8;x=1.
    u,v,_=derived(a,b,h,x,1e-3)
    assert v<0
    factor=(x+h*b*((1-GAMMA)*(1-u)/(1-v)+GAMMA))/(h*a*(1-GAMMA)*u)
    for eps in (1e-5,1e-7,1e-9,1e-11):
        _,_,out=derived(a,b,h,x,eps)
        approx(out/eps,factor,atol=5e-4)
        checks+=1
    actual=.1+.9*math.exp(-8)
    assert actual>.1
    assert abs(derived(9,1,.8,1,1e-9)[2]-actual)>.1
    checks+=2
    print('PASS', checks, 'deterministic direct-stage, algebraic and singular-limit assertions')
    print('pi_star',pi_star,'sstar',sstar,'v8',v,'true_state8',actual)
