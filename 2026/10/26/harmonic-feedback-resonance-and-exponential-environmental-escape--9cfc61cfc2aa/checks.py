"""Standalone verification for a logistic environmental boundary law.

Standard-library only. Finite checks support, but do not replace, the proof.
"""
from fractions import Fraction as F
from math import exp, log
import random


def fractions_check():
    rng = random.Random(20261024)
    for k in range(180):
        th1, th2, th12 = [F(rng.randint(1, 18), rng.randint(1, 12)) for _ in range(3)]
        x, y = F(rng.randint(1, 99), 100), F(rng.randint(1, 99), 100)
        a1, a2, a12 = 1/(1+th1), 1/(1+th2), 2/(1+th12)
        drift = a1*((1+th1)*x-1)+a2*((1+th2)*y-1)-a12*((1+th12)*(x+y)/2-1)
        assert drift == a12-a1-a2, ('log-odds identity', k)
        hmean = F(2, 1)/(a1+a2)-1
        if th12 == hmean:
            assert a12-a1-a2 == 0
        elif a12-a1-a2 == 0:
            raise AssertionError('resonance algebra')
    return 180


def ode(t, s, theta, delta):
    x, y, n1, n2, n12 = s
    t1,t2,t12=theta
    # Admissible games A(0)=[[3,2],[1,0]], A(1)=[[1,0],[3,2]].
    # Cooperation payoff minus defection payoff = 2-4*n per edge.
    dx = x*(1-x)*(2-4*((1-delta)*n1+delta*n12))
    dy = y*(1-y)*(2-4*((1-delta)*n2+delta*n12))
    return (
        dx, dy,
        n1*(1-n1)*((1+t1)*x-1),
        n2*(1-n2)*((1+t2)*y-1),
        n12*(1-n12)*((1+t12)*(x+y)/2-1),
    )


def rk4(s, h, theta, delta):
    k1 = ode(0,s,theta,delta)
    k2 = ode(0,[a+h*b/2 for a,b in zip(s,k1)],theta,delta)
    k3 = ode(0,[a+h*b/2 for a,b in zip(s,k2)],theta,delta)
    k4 = ode(0,[a+h*b for a,b in zip(s,k3)],theta,delta)
    return [a+h*(b+2*c+2*d+e)/6 for a,b,c,d,e in zip(s,k1,k2,k3,k4)]


def hlog(s,theta):
    t1,t2,t12=theta
    w1,w2,w12=1/(1+t1),1/(1+t2),2/(1+t12)
    n1,n2,n12=s[2:]
    return w1*log(n1/(1-n1))+w2*log(n2/(1-n2))-w12*log(n12/(1-n12))


def logistic_geometry_check():
    rng=random.Random(73124)
    for k in range(250):
        theta=[rng.uniform(.1,9) for _ in range(3)]
        n=[rng.uniform(.02,.98) for _ in range(3)]
        w1,w2,w12=1/(1+theta[0]),1/(1+theta[1]),2/(1+theta[2])
        W=w1+w2+w12
        L=[log(q/(1-q)) for q in n]
        H=w1*L[0]+w2*L[1]-w12*L[2]
        Bplus=min(1-n[0],1-n[1],n[2])
        Bminus=min(n[0],n[1],1-n[2])
        assert Bplus <= 1/(1+exp(H/W))+1e-14
        assert Bminus <= 1/(1+exp(-H/W))+1e-14
        # Every pointwise envelope is sharp for environmental coordinates
        # with equal signed logits.
        u=rng.uniform(-7,7)
        q=1/(1+exp(-u))
        ns=[q,q,1-q]
        hs=w1*log(ns[0]/(1-ns[0]))+w2*log(ns[1]/(1-ns[1]))-w12*log(ns[2]/(1-ns[2]))
        assert abs(hs/W-u)<2e-12
        assert abs(min(1-ns[0],1-ns[1],ns[2])-1/(1+exp(hs/W)))<1e-14
    return 250


def trajectory_check():
    theta=(1.0,3.0,1.0)
    delta=0.37
    s=[0.37,0.62,0.31,0.47,0.65]
    h0=hlog(s,theta)
    w=1/(1+theta[0])+1/(1+theta[1])+2/(1+theta[2])
    drift=2/(1+theta[2])-1/(1+theta[0])-1/(1+theta[1])
    maxerr=0.0
    for i in range(3001):
        t=i*.01
        ht=hlog(s,theta)
        maxerr=max(maxerr,abs(ht-(h0+drift*t)))
        if ht>0:
            target=min(1-s[2],1-s[3],s[4])
            assert target<=exp(-ht/w)+2e-14, (t,target,ht)
        if i<3000:
            s=rk4(s,.01,theta,delta)
            assert all(0<v<1 for v in s)
    assert abs(drift-.25)<1e-13
    assert maxerr < 3e-8,maxerr
    return maxerr


def resonance_check():
    # Fully asymmetric, exact harmonic resonance, admissible games.
    theta=(1.0,3.0,5/3)
    s=[1/2,1/4,1/2,1/2,1/2]
    deriv=ode(0,s,theta,0.37)
    assert max(map(abs,deriv))<1e-14, deriv
    assert abs(hlog(s,theta))<1e-14
    return max(map(abs,deriv))


def source_example_check():
    theta=(3,5,8)
    drift=2/(1+theta[2])-1/(1+theta[0])-1/(1+theta[1])
    w=2/(1+theta[2])+1/(1+theta[0])+1/(1+theta[1])
    assert drift < 0
    assert F(2,9)-F(1,4)-F(1,6)==-F(7,36)
    assert F(7,36)/(F(2,9)+F(1,4)+F(1,6))==F(7,23)
    return drift,-drift/w


if __name__=='__main__':
    print('exact rational cancellation cases:',fractions_check())
    print('exact logistic boundary-envelope and attainment cases:',logistic_geometry_check())
    print('30-unit coupled ODE RK4 maximum logit drift residual:',trajectory_check())
    print('asymmetric resonant interior equilibrium residual:',resonance_check())
    print('published five-variable example drift, exponential boundary rate:',source_example_check())
    print('PASS')
