"""Finite diagnostic checks for the two-observation weighted Gaussian NPMLE phase law.
Analytical proof, including the Kearns--Saul lemma, is in RESULT.md.
No finite grid is presented as an infinite-dimensional certificate.
"""
import math


def critical(q):
    return 1.0 if q == 0.5 else math.sqrt(math.log((1.0-q)/q)/(2.0*(1.0-2.0*q)))


def certificate(theta, a, q):
    z = a*(1.0-2.0*q)
    t = theta-z
    return math.exp(-t*t/2.0)*(q*math.exp(-2.0*a*(1.0-q)*t)+(1.0-q)*math.exp(2.0*a*q*t))


def derivative(theta, a, q):
    z = a*(1.0-2.0*q)
    return sum((w*math.exp(-((theta-x)**2-(z-x)**2)/2.0)*(x-theta)) for w,x in ((q,-a),(1.0-q,a)))


def curvature(theta, a, q):
    z = a*(1.0-2.0*q)
    return sum(w*math.exp(-((theta-x)**2-(z-x)**2)/2.0)*((theta-x)**2-1.0) for w,x in ((q,-a),(1.0-q,a)))


def singleton_loglik(a,q):
    z=a*(1-2*q)
    return -0.5*(q*(z+a)**2+(1-q)*(z-a)**2)


def mixture_loglik(a,q,theta,eps):
    z=a*(1-2*q)
    def val(x):
        return math.log((1-eps)*math.exp(-0.5*(x-z)**2)+eps*math.exp(-0.5*(x-theta)**2))
    return q*val(-a)+(1-q)*val(a)


def run():
    checks=0
    for q in (0.035,0.12,0.2,0.32,0.4,0.47,0.5,0.53,0.6,0.8,0.965):
        ac=critical(q)
        local=1/(2*math.sqrt(q*(1-q)))
        if q==.5:assert abs(ac-local)<1e-12
        else:assert ac<local
        checks+=1
        for mult in (0.5,0.93,1.0):
            a=ac*mult; z=a*(1-2*q)
            assert abs(certificate(z,a,q)-1)<3e-12
            assert abs(derivative(z,a,q))<3e-12
            for k in range(-450,451):
                theta=4*a*k/450
                assert certificate(theta,a,q)<=1+1e-10,(q,a,theta,certificate(theta,a,q))
                checks+=1
        a=ac; z=a*(1-2*q)
        if q!=.5:
            assert abs(certificate(-z,a,q)-1)<3e-12
            assert abs(derivative(-z,a,q))<3e-12
            assert curvature(-z,a,q)<0
            assert curvature(z,a,q)<0
            checks+=4
        else:
            assert abs(curvature(z,a,q))<3e-12
            checks+=1
        for mult in (1.015,1.1):
            a=ac*mult; z=a*(1-2*q)
            if q!=.5:
                assert certificate(-z,a,q)>1+1e-8
                assert mixture_loglik(a,q,-z,1e-5)>singleton_loglik(a,q)
                checks+=2
            else:
                assert curvature(z,a,q)>0
                assert certificate(z+0.05,a,q)>1
                checks+=2
        if q!=.5:
            a=(ac+local)*0.5
            z=a*(1-2*q)
            assert curvature(z,a,q)<0
            assert certificate(-z,a,q)>1
            checks+=2
    return checks

if __name__=='__main__':
    print('PASSED deterministic diagnostics:',run())
