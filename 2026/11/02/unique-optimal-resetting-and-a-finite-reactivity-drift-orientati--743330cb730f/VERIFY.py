"""Numerical cross-checks of an analytic drifted delta-sink resetting theorem.

Run: python VERIFY.py (Python 3.9+, no third-party dependencies).
Finite checks are not proofs of uniqueness or uniform asymptotics.
"""
from math import exp, e, isclose

count = 0

def check(condition, description):
    global count
    count += 1
    if not condition:
        raise AssertionError(description)


def stationary_numerator(y, m, eta, sign):
    if not (y > 0 and m >= 0 and eta > 0 and sign in (-1, 1)):
        raise ValueError('domain')
    q = exp(-(sign+1)*m)
    A = (1 + eta*(m+y))*exp(y) - q
    Ap = (1 + eta*(m+y+1))*exp(y)
    return y*(2*m+y)*Ap - 2*(y+m)*A


def optimum(m, eta, sign):
    lo, hi = 1e-6, 4.0
    check(stationary_numerator(lo,m,eta,sign)<0, 'negative left derivative')
    check(stationary_numerator(hi,m,eta,sign)>0, 'positive right derivative')
    for _ in range(85):
        mid = (lo+hi)/2
        if stationary_numerator(mid,m,eta,sign)>0:
            hi=mid
        else:
            lo=mid
    y=(hi+lo)/2
    return y, y*(y+2*m)


def scaled_objective(y,m,eta,sign):
    q=exp(-(sign+1)*m)
    return ((1+eta*(m+y))*exp(y)-q)/(y*(y+2*m))


def run():
    for eta in (0.15, 0.3, 1., 2., 8., 25.):
        for m in (0.0, 0.1, 0.5, 1., 2., 5., 20., 100., 1000.):
            for s in (-1, 1):
                y,z2=optimum(m,eta,s)
                check(y>0 and z2>0,'positive optimizer')
                for step in (0.02, 0.1, 0.2):
                    ymin=max(y-step, y*0.6)
                    check(scaled_objective(y,m,eta,s)<scaled_objective(ymin,m,eta,s),'left objective')
                    check(scaled_objective(y,m,eta,s)<scaled_objective(y+step,m,eta,s),'right objective')
            if m>0:
                minus=optimum(m,eta,-1)[1]
                plus=optimum(m,eta,1)[1]
                check(plus>minus,'away/toward rate ordering')
        for m in (200., 500., 1000., 2000.):
            yp,zp=optimum(m,eta,1)
            yn,zn=optimum(m,eta,-1)
            check(abs((yp-1)*m+0.5)<3.5/m*(1+1/eta)**2,
                  'away first-order optimizer expansion')
            check(abs((yn-1)*m+0.5+1/(e*eta))<12./m*(1+1/eta)**2,
                  'toward first-order optimizer expansion')
            limit=2/(e*eta)
            check(abs((zp-zn)-limit)<18./m*(1+1/eta)**2,
                  'constant orientation gap')
    yminus,zminus=optimum(0.5,1,-1)
    yplus,zplus=optimum(0.5,1,+1)
    check(abs(zminus-1.50)<0.01, 'benchmark toward drift')
    check(abs(zplus-2.06)<0.01, 'benchmark away drift')
    print('PASS:',count,'finite assertions; analytic statements require the accompanying proof')

if __name__=='__main__':
    run()
