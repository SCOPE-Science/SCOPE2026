"""Standalone independent checks for the central-section type law of equilateral triangular prisms."""
import numpy as np
from math import acos,asin,atan,pi,sqrt

def predicted(t):
    g=acos((t*t-0.5)/(t*t+1.))
    v=2*atan(t)
    p3=1-6/pi*asin(1/(2*sqrt(1+t*t)))
    avg=(6*g+3*v)/pi
    p5=avg-4+p3
    return np.array((p3,1-p3-p5,p5)),avg

def test(t, count=500_000):
    rng=np.random.default_rng(489230+round(100*t))
    u=rng.normal(size=(count,3));u/=np.linalg.norm(u,axis=1)[:,None]
    phi=np.arange(3)*2*pi/3
    vv=np.stack((np.cos(phi),np.sin(phi),np.zeros(3)*phi),axis=1)
    vtx=np.concatenate((vv+np.array([0,0,t]),vv-np.array([0,0,t])),axis=0)
    edges=[(i,(i+1)%3) for i in range(3)] + [(i+3,((i+1)%3)+3) for i in range(3)] + [(i,i+3) for i in range(3)]
    s=u@vtx.T
    k=np.zeros(count,dtype=np.int8)
    for a,b in edges:k+=((s[:,a]*s[:,b])<0)
    assert np.all((k>=3)&(k<=5)),(t,np.unique(k,return_counts=True))
    empirical=np.bincount(k,minlength=6)[3:6]/count
    pred,avg=predicted(t)
    assert np.max(abs(empirical-pred))<0.005,(t,empirical,pred)
    assert abs(np.mean(k)-avg)<.01
    return np.round(empirical,6),np.round(pred,6)

if __name__=='__main__':
    for t in (0.08,.25,.5,1,2,5,20):
        a,b=test(t)
        print('t=',t,' empirical=',a,' exact=',b)
    # independent quadrature of rotational normal cone area
    from scipy.integrate import quad
    for t in (.2, .5, 1, 3):
        def M(phi):return max(abs(np.cos(phi-2*pi*j/3)) for j in range(3))
        p3=quad(lambda x: (1-M(x)/np.sqrt(t*t+M(x)**2))/(2*pi),0,2*pi,epsabs=5e-12,points=np.linspace(0,2*pi,13))[0]
        assert abs(p3-predicted(t)[0][0])<1e-10,(t,p3,predicted(t))
    print('ROTATION_CONE_QUADRATURE_PASSED')
    from scipy.optimize import brentq
    hfun=lambda t:1-2*sqrt(3)*t/sqrt(1+4*t*t)+t/sqrt(3+4*t*t)
    tm=brentq(hfun, .01, 5)
    assert .52<tm<.54
    assert abs(predicted(tm)[0][2]-0.38515580567417673)<3e-14
    assert hfun(.05)>0 and hfun(5)<0
    print('UNIQUE_PENTAGON_MAXIMIZER_CHECK_PASSED',repr(tm))
    for t in (.04,.18,.7,1.8,18.):
        p3=predicted(t)[0][0]
        tr=sqrt(1/(4*np.sin(pi*(1-p3)/6)**2)-1)
        assert abs(tr-t)/t<3e-12,(t,tr)
    print('SHARP_ASPECT_RATIO_INVERSION_PASSED')
    print('DIRECT_EDGE_CROSSING_MONTE_CARLO_PASSED')
    print('ALL_CHECKS_PASSED')
