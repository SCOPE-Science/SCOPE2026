import math
import numpy as np
from numpy.polynomial.legendre import leggauss

def wpp(delta, n=240):
    x,w=leggauss(n)
    th=(x+1)*math.pi/4
    ww=w*math.pi/4
    t0=1/(1+delta)
    t=t0*np.sin(th)
    dt=t0*np.cos(th)
    num=t*t*(1+(1-delta*delta)*t*t)
    den1=np.sqrt(2+(2-delta*delta)*t*t)
    den2=np.sqrt((1-(delta-1)**2*t*t)*(1-(delta+1)**2*t*t))
    return (4/math.pi)*np.sum(ww*num/den1/den2*dt)

def mean_width(delta, n_t=180, n_p=240):
    xt,wt=leggauss(n_t)
    xp,wp=leggauss(n_p)
    t=(xt+1)/2
    wt=wt/2
    phi=(xp+1)*math.pi
    wp=wp*math.pi
    total=0.0
    for ti,wi in zip(t,wt):
        s=math.sqrt(max(0.0,1-ti*ti))
        a=s*np.cos(phi); c=s*np.sin(phi)
        A=np.sqrt(a*a+ti*ti); B=np.sqrt(c*c+ti*ti)
        width=A+B+np.maximum(np.abs(A-B),delta*ti)
        total += wi*np.sum(wp*width)/(2*math.pi)
    return total

for d in [0.25,1.0,math.sqrt(2),2.0,4.0]:
    q=wpp(d)
    assert math.isfinite(q) and q>0, (d,q)
known=math.sqrt(2)+math.acos(1/3)
got=mean_width(2.0)
assert abs(got-known)<2e-5, (got,known)
print('VERIFY_OK')
