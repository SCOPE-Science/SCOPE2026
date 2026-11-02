#!/usr/bin/env python3
"""Independent finite diagnostics and exact recurrence-coordinate identity.
Not a substitute for the infinite-time proof in RESULT.md.
"""
from fractions import Fraction


def original(x, y, a, c, d):
    return x + a*x/(1+y*y), y + c*x + d

def normalized(u, y, a, d):
    return u*(1+a/(1+y*y)), y+d*(1-u)

def exact_coordinate_check():
    a=Fraction(2,3);c=Fraction(5,4);d=Fraction(3,2)
    x=Fraction(-1,4); y=Fraction(0);u=-c*x/d
    for _ in range(12):
        assert -c*x/d==u
        xn,yn=original(x,y,a,c,d)
        un,zn=normalized(u,y,a,d)
        assert yn==zn and -c*xn/d==un
        x,y,u=xn,yn,un
    print('PASS: twelve exact rational conjugacy iterates')

def trajectory(u0, steps, a=1., d=1.):
    u,y=u0,0.
    for n in range(steps):
        u1=u*(1.+a/(1.+y*y)); y+=d*(1.-u);u=u1
        if u>=1.:
            return float('-inf'),u,y,n+1
    return (1.-u)**2*y,u,y,steps

def critical_shooting(steps):
    # A finite-horizon diagnostic, imposing the asymptotic invariant w^2*y=2a/d.
    low,high=0.089,0.089318
    for _ in range(39):
        mid=(low+high)/2.
        statistic,u,y,n=trajectory(mid,steps)
        if statistic>2.:low=mid
        else:high=mid
    trial=(low+high)/2.
    statistic,u,y,n=trajectory(trial,steps)
    A=(4.5)**(1./3.);B=2*A/3
    yr=y/(A*steps**(2./3.))
    wr=(1-u)/(B*steps**(-1./3.))
    assert n==steps and abs(statistic-2.)<1.e-7
    assert abs(yr-1.)<.035 and abs(wr-1.)<.02
    print('PASS: finite-horizon critical shooting',steps,'u0=',format(trial,'.15g'), 'y/leading=',format(yr,'.8f'),'w/leading=',format(wr,'.8f'))

def ballistic_checks():
    n,u,y,_=trajectory(.05,60000)
    assert u<.5 and .4<y/60000<1.
    n,u,y,j=trajectory(.2,60000)
    assert n==float('-inf') and u>1
    print('PASS: distinct signs of asymptotic escape detected (finite observations only)')

if __name__=='__main__':
    exact_coordinate_check()
    ballistic_checks()
    for N in (5000,20000,50000):critical_shooting(N)
