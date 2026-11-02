"""Supplementary numerical checks for the sharp Erlang Gabor bounds.

The analytic proof of global optimization is in RESULT.md; finite tests
are consistency tests only and do not establish universal statements.
"""
import cmath
import math


def exact(a):
    r=math.exp(-a)
    u=1+r*r
    t=1-r*r
    d=math.sqrt(u*u-4*a*a*r*r)
    x=(u+2*a*r*r-d)/(2*a*u)
    y=(u+d-2*a*r*r*(3+r*r)/t)/(2*a*u)
    amin=2*math.exp(-2*a*x)*(x*x+r*r*(1-x)**2)/u**2
    bmax=math.exp(-2*a*y)*(
        (r+(1-r)*y)**2/(1-r)**4
        +(y-(1-y)*r)**2/(1+r)**4
    )
    return amin,bmax,x,y


def fibre(a,x,omega):
    r=math.exp(-a)
    z=r*cmath.exp(-2j*math.pi*omega)
    Z=math.exp(-a*x)*(x+(1-x)*z)/(1-z)**2
    Z2=math.exp(-a*x)*(x-(1-x)*z)/(1+z)**2
    return abs(Z)**2+abs(Z2)**2


def check():
    n=0
    for a in [.025,.08,.25,.5,1.,1.65,2.4,3.1,4.5,8.,12.]:
        A,B,x,y=exact(a)
        assert 0<x<1 and 0<y<1 and A>0 and B>=A
        n+=4
        assert abs(fibre(a,x,.25)-A)<1e-8*max(1,A)
        assert abs(fibre(a,y,0)-B)<1e-8*max(1,B)
        n+=2
        # A grid has strictly weaker resolution than the theorem.
        for ix in range(81):
            z=ix/80
            for iw in range(81):
                w=iw/80
                v=fibre(a,z,w)
                assert A-1e-9*max(1,A)<=v<=B+1e-9*max(1,B)
                n+=1
        # Verify the closed rational Zak formula against its defining series.
        for ix in [1,13,53,77]:
            z=ix/100
            for iw in [0,9,21,38]:
                w=iw/50
                k=sum((z+j)*math.exp(-a*(z+j))*cmath.exp(-2j*math.pi*j*w) for j in range(5000))
                r=math.exp(-a)*cmath.exp(-2j*math.pi*w)
                rhs=math.exp(-a*z)*(z+(1-z)*r)/(1-r)**2
                assert abs(k-rhs)<1e-7*max(1,abs(rhs))
                n+=1
    for a in [.001,.002,.005,.01]:
        A,B,x,y=exact(a)
        assert abs(4*a**4*(B/A)-16)<1 # equivalent to a^4 condition number -> 4
        n+=1
    for a in [10.,12.,15.,20.]:
        A,B,x,y=exact(a)
        ratio=(B/A)*a*a*math.exp(-2*a)
        assert abs(ratio-math.exp(-2))<.005
        n+=1
    print('PASS',n,'assertions')
    for a in [.1,1.,1.8,2.,5.]:
        A,B,x,y=exact(a)
        print('a=',a,'A=',round(A,12),'B=',round(B,12),'kappa=',round(B/A,8),
              'xmin=',round(x,8),'xmax=',round(y,8))


if __name__=='__main__':
    check()
