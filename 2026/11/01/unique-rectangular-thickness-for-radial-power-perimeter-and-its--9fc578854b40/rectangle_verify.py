#!/usr/bin/env python3
"""Diagnostic checks for the radial weighted rectangle aspect phase law.

Requires mpmath; tests are numerical and do not substitute for the theorem proof.
"""
import mpmath as mp
mp.mp.dps = 65


def J(q):
    return mp.sqrt(mp.pi)*mp.gamma((q+1)/2)/(2*mp.gamma(1+q/2))


def I(q,t):
    if t >= 1:
        return J(q)-mp.quad(lambda v: v**q/(1+v*v)**(1+q/2), [0, 1/t])
    return mp.quad(lambda u: (1+u*u)**(-1-q/2), [0,t])


def H(q,t):
    return (1+t*t)**(-q/2) - q*I(q,t)


def root(q):
    q=mp.mpf(q)
    lo=-mp.mpf(20)
    hi=max(mp.mpf(20), mp.mpf(4)*abs(mp.log(q))/q+10)
    assert H(q,mp.exp(lo))>0 and H(q,mp.exp(hi))<0
    for _ in range(260):
        mid=(lo+hi)/2
        if H(q,mp.exp(mid))>0:lo=mid
        else:hi=mid
    return mp.exp((lo+hi)/2)


def F(p,a,b):
    return 4*(mp.quad(lambda x:(x*x+b*b)**(p/2),[0,a])+
              mp.quad(lambda y:(a*a+y*y)**(p/2),[0,b]))


def deriv(p,a,b):
    t=a/b
    return 4*b**p*H(-p,t)


def checks():
    n=0
    for q in map(mp.mpf,['0.05','0.1','0.25','0.5','0.9','1','1.5','2','5','10']):
        t=root(q)
        b=1/t
        assert abs(H(q,t)) < mp.mpf('1e-58')
        assert H(q,t/2)>0 and H(q,t*2)<0
        assert F(-q,1,b) < F(-q,1,b*mp.mpf('.6'))
        assert F(-q,1,b) < F(-q,1,b*mp.mpf('1.4'))
        n+=4
        print('q=',mp.nstr(q,4),' t=',mp.nstr(t,14),' b/a=',mp.nstr(b,10),
              'scale ratio=',mp.nstr(t**(-q)/q,13))
    assert abs(root(mp.mpf(1))-1)<mp.mpf('1e-55')
    n+=1
    for q in ['0.025','0.05','0.1']:
        q=mp.mpf(q);t=root(q)
        print('endpoint q=',q,' ratio=',mp.nstr(t**(-q)/q,20),
              ' vs pi/2=',mp.nstr(mp.pi/2,20))
        n+=1
    for q in ['10','30','80']:
        q=mp.mpf(q);t=root(q)
        print('large q=',q,' qt=',mp.nstr(q*t,17))
        n+=1
    for p,a,b in [(-mp.mpf('.5'),1,mp.mpf('.5')),
                  (-mp.mpf('2'),2,mp.mpf('.8')),
                  (mp.mpf('.8'),3,mp.mpf('2'))]:
        actual=mp.diff(lambda v:F(p,a,v),b)
        predicted=deriv(p,a,b) if p<0 else 4*(p*b*mp.quad(lambda x:(x*x+b*b)**(p/2-1),[0,a])+(a*a+b*b)**(p/2))
        assert abs(actual-predicted)<mp.mpf('1e-48')
        n+=1
    print('PASS:',n,'high-precision diagnostic assertions; endpoint values and derivative identities checked.')

if __name__=='__main__':checks()
