"""Direct matrix-generator test of stationary two-velocity transport cumulants."""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq


def exact_formula(a,b,c0,c1,t):
    r=a+b
    eta=(b-a)/r
    P=a*b/r**2
    u=r*t
    E=math.exp(-u)
    A=u-3+(u*u+4*u+6)*E/2
    B=u-2.5+2*(u+1)*E+E*E/2
    return 24*P*(c1-c0)**4/r**4*(eta*eta*A-P*B)


def direct_feynman_kac(a,b,c0,c1,t):
    r=a+b
    pi=np.array([b/r,a/r])
    avg=pi@np.array([c0,c1])
    Q=np.array([[-a,a],[b,-b]], dtype=float)
    V=np.diag([c0-avg,c1-avg])
    F=np.zeros((10,10))
    for j in range(5):
        F[2*j:2*j+2,2*j:2*j+2]=Q
        if j:
            F[2*j:2*j+2,2*j-2:2*j]=j*V
    y0=np.zeros(10)
    y0[:2]=1
    Y=expm(t*F)@y0
    ms=np.array([pi@Y[2*j:2*j+2] for j in range(5)])
    return ms[4]-4*ms[3]*ms[1]-3*ms[2]**2+12*ms[2]*ms[1]**2-6*ms[1]**4


def main():
    count=0
    worst=0.0
    for a,b in [(1.,1.),(1.,1.2),(1.,1.7),(1.,2.),(1.,3.),(1.,4.),(1.,8.),(.15,1.1),(4.,.25),(10.,10.)]:
        for c0,c1 in [(-1.,1.),(0.,1.),(-3.,2.)]:
            for u in [.15,.4,.8,1.5,2.,3.,5.,9.,18.]:
                t=u/(a+b)
                actual=direct_feynman_kac(a,b,c0,c1,t)
                expected=exact_formula(a,b,c0,c1,t)
                error=abs(actual-expected)
                worst=max(worst,error)
                assert error<1.e-9*max(1.,abs(expected)),(a,b,c0,c1,u,actual,expected,error)
                count+=1
    # Boundary and crossing tests, using more stable high-precision formula only for signs.
    import mpmath as mp
    mp.mp.dps=70
    def stable_form(alpha,u):
        p=(1-alpha)/4
        if u < mp.mpf('0.3'):
            # Integral quadrature avoids cancellation near zero.
            A=mp.quad(lambda s:(u-s)*s*s*mp.exp(-s)/2,[0,u])
            B=mp.quad(lambda s:(u-s)*2*mp.exp(-s)*(s-1+mp.exp(-s)),[0,u])
        else:
            A=u-3+(u*u+4*u+6)*mp.exp(-u)/2
            B=u-mp.mpf('2.5')+2*(u+1)*mp.exp(-u)+mp.exp(-2*u)/2
        return alpha*A-p*B
    for alpha in ['0.01','0.19','0.2','0.24','0.30','0.33333333333333333333333333333','0.34','0.5','0.9']:
        alpha=mp.mpf(alpha)
        for ut in ['0.0001','0.01','0.3','1','3','10','500']:
            v=stable_form(alpha,mp.mpf(ut))
            if alpha <= mp.mpf('0.2'): assert v < 0
            if alpha >= mp.mpf('0.33333333333333333333333333334'): assert v > 0
            count+=1
    alpha=mp.mpf('0.25')
    root=mp.findroot(lambda u:stable_form(alpha,u),(2,4))
    assert mp.mpf('3.0464') < root < mp.mpf('3.0466')
    assert stable_form(alpha,root-1)<0<stable_form(alpha,root+1)
    print('PASS',count,'analytic/matrix numerical and sign assertions; max abs matrix discrepancy',worst)
    print('example dimensionless crossing:',mp.nstr(root,25),'physical time for a=1 b=3:',mp.nstr(root/4,25))

if __name__=='__main__':main()
