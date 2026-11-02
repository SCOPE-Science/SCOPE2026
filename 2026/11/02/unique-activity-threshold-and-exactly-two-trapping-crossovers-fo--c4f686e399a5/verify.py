"""Reproduce rational moment and phase-boundary checks for a resetting ABP.

Run with Python 3 and its standard library: python verify.py
The finite checks corroborate, but do not replace, the analytic proof.
"""
from fractions import Fraction as Q
from math import sqrt, log, exp


def coeffs(b, r):
    a = r*(r+1)*(r+2)+r*(1+3*r)*b-(14+r)*b*b-6*b*b*b
    bb = 2*r*(b+r+1)*(2*b+r+4)*(5*b+2*r+1)
    c = 2*r*(b+r+1)**2*(2*b+r+4)*(3*b+r+1)
    return a, bb, c


def moments(b, r, p):
    peq = p/(b+r+1)
    m2 = (4+2*peq)/(2*b+r)
    w = (2*peq+2+2*m2)/(2*b+r+4)
    ph = (p*(2*w+m2)+8*peq)/(3*b+r+1)
    m4 = (16*m2+4*ph)/(4*b+r)
    return m2, m4


def kurtosis(b,r,p):
    m2,m4=moments(b,r,p)
    return m4/(2*m2*m2)-1


def rational_kurtosis(b,r,p):
    a,bb,c=coeffs(b,r)
    return 2*(a*p*p+bb*p+c)/((4*b+r)*(2*b+r+4)*(3*b+r+1)*(2*b+p+2*r+2)**2)


count=0
for rn in [Q(1,10),Q(1),Q(3),Q(10)]:
    for bn in [Q(1,5),Q(1),Q(2),Q(8)]:
        for pn in [Q(0),Q(1,4),Q(1),Q(8),Q(100)]:
            assert kurtosis(bn,rn,pn)==rational_kurtosis(bn,rn,pn)
            count+=1


def root_of_a(r):
    left,right=0.,max(5.,r*4.)
    while coeffs(right,r)[0]>0: right*=2
    for _ in range(110):
        mid=(left+right)/2
        if coeffs(mid,r)[0]>0:left=mid
        else:right=mid
    return (left+right)/2


def activity_threshold(b,r):
    a,bb,c=coeffs(b,r)
    assert a<0
    return (bb+sqrt(bb*bb-4*a*c))/(-2*a)


def cusp(r):
    edge=root_of_a(r)
    # Minimize the analytically proven single-well threshold in log(b).
    lo,hi=log(edge*1.00001),log(max(40.,edge*200.))
    phi=(sqrt(5)-1)/2
    u=hi-phi*(hi-lo);v=lo+phi*(hi-lo)
    fu=activity_threshold(exp(u),r);fv=activity_threshold(exp(v),r)
    for _ in range(150):
        if fu>fv:
            lo=u;u=v;fu=fv;v=lo+phi*(hi-lo);fv=activity_threshold(exp(v),r)
        else:
            hi=v;v=u;fv=fu;u=hi-phi*(hi-lo);fu=activity_threshold(exp(u),r)
    bstar=exp((hi+lo)/2)
    return bstar,activity_threshold(bstar,r)


bcrit,pcrit=cusp(1.)
assert abs(bcrit-7.1619074838)<1.e-5
assert abs(pcrit-7.94071433834)<1.e-5
assert rational_kurtosis(1.,1.,8.)>0
assert rational_kurtosis(7.16,1.,8.)<0
assert rational_kurtosis(50.,1.,8.)>0
assert rational_kurtosis(0.5,1.,100.)>0
assert rational_kurtosis(1.,1.,100.)<0
assert rational_kurtosis(5000.,1.,100.)>0

# Numerical recovery of the two strict sign transitions at Pe=10 and r=1.
def zero_bracket(l,h,r,p):
    fl=coeffs(l,r)[0]*p*p+coeffs(l,r)[1]*p+coeffs(l,r)[2]
    for _ in range(120):
        mid=(l+h)/2
        a,bb,c=coeffs(mid,r);fm=a*p*p+bb*p+c
        if fl*fm<=0:h=mid
        else:l=mid;fl=fm
    return (l+h)/2

left=zero_bracket(.2,5.,1.,100.)
right=zero_bracket(10.,6000.,1.,100.)
assert abs(left-.768947514)<1e-6
assert abs(right-4828.57539)<.005

# Independent asymptotic numerics (the report supplies the proof).
def weak_g(b):return 2*(b+1)**2*(b+2)*(3*b+1)/(b*b*(3*b+7))
lo,hi=.5,3.
for _ in range(120):
    x=lo+(hi-lo)/3;y=hi-(hi-lo)/3
    if weak_g(x)>weak_g(y):lo=x
    else:hi=y
bw=(lo+hi)/2
cw=sqrt(weak_g(bw))
assert abs(bw-1.37627805407)<1e-7
assert abs(cw-3.04585809626)<1e-8
assert abs(cusp(1e-8)[1]/1e-4-cw)<.002
assert abs(cusp(1e4)[1]/1e4-7.04348401862)<.001
print('PASS: %d exact rational moment identities; finite phase brackets; critical activity and weak/strong limits.'%count)
print('r=1: beta_c=%.11f, Pe_c^2=%.11f'%(bcrit,pcrit))
print('r=1, Pe=10: two zeros beta=%.9f, %.6f'%(left,right))
