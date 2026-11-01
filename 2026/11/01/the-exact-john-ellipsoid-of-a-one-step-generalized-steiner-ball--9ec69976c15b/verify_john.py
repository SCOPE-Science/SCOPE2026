#!/usr/bin/env python3
"""Independent finite diagnostics for the explicit John ellipsoid of split spheroids.
This script is not an infinite-dimensional proof; see the accompanying theorem.
Only Python's standard library is required.
"""
from decimal import Decimal, getcontext
from math import sqrt, exp

getcontext().prec = 65
D = lambda x: Decimal(str(x))


def axes(n, lam):
    n = Decimal(n)
    lam = D(lam)
    alpha = D(2)*(D(1)-lam)
    beta = D(2)*lam
    disc = ((n-D(1))*beta)**2 + D(4)*n*alpha**2
    b = (beta+disc.sqrt()/(n+D(1)))/D(2)
    c = b-beta
    a2 = ((n+D(1))*b*b-n*beta*b)/(alpha*alpha)
    return alpha,beta,a2,b,c


def chk_close(x,y,tol=D('2e-52')):
    assert abs(x-y) <= tol*max(D(1),abs(x),abs(y)),(x,y)

count=0
for n in [2,3,4,5,8,11,20,63,255,1024]:
 for lam in ['0','0.00001','0.02','0.12','0.25','0.49','0.5']:
    al,be,a2,b,c=axes(n,lam)
    nn=D(n)
    assert 0 < a2 <= D(1)+D('1e-55')
    assert be <= b <= al
    chk_close(c,b-be)
    chk_close(b*b-be*b,nn*(al*al-be*be)/(nn+D(1))**2)
    q=(D(1)-D(1)/nn**2)
    top_y=c+b/nn
    chk_close(q*a2+(top_y/al)**2,D(1))
    chk_close(al*al*a2,(nn+D(1))*b*b-nn*be*b)
    # John isotropic contact measure on top latitude and bottom pole.
    top_w=nn*nn/(nn+D(1)); bot_w=nn/(nn+D(1))
    chk_close(top_w/nn-bot_w,D(0))
    chk_close(top_w*(D(1)-D(1)/nn**2)/(nn-D(1)),D(1))
    chk_close(top_w/nn**2+bot_w,D(1))
    # Independently verify upper envelope and lower envelope over axial slices.
    for j in range(201):
        z=D(j)/D(100)-D(1)
        sq=a2*(D(1)-z*z)
        y=c+b*z
        if y>=0:
            v=sq+(y/al)**2
        elif be>0:
            v=sq+(y/be)**2
        else:
            raise AssertionError('flat side violated')
        assert v <= D(1)+D('3e-55'),(n,lam,z,v)
        count+=1
    # Volume ratio normalized by volume of split-spheroid.
    eff=(a2**((nn-D(1))/D(2)))*b
    assert eff<=D(1)+D('1e-45')
    count+=6
# Endpoint exact formula and two-scale asymptotics.
for n in [2,3,5,10,100,1000,10000]:
    al,be,a2,b,c=axes(n,'0')
    nn=D(n)
    chk_close(a2,nn/(nn+D(1)))
    chk_close(b,D(2)*nn.sqrt()/(nn+D(1)))
    vol=(a2**((nn-D(1))/D(2)))*b
    alt=D(2)/(nn+D(1)).sqrt()*(nn/(nn+D(1)))**(nn/D(2))
    chk_close(vol,alt)
    count+=3
for tau in ['0','0.25','1','2','4']:
    t=float(tau)
    lim=(t+sqrt(t*t+4))*exp(-((sqrt(t*t+4)-t)**2)/8)
    estimates=[]
    for n in [10000,100000,1000000]:
        lam=Decimal(tau)/Decimal(n).sqrt()
        al,be,a2,b,c=axes(n,lam)
        ln_a2=a2.ln()
        eff=((Decimal(n)-D(1))/D(2)*ln_a2).exp()*b
        estimates.append(float(eff*Decimal(n).sqrt()))
        count+=1
    assert abs(estimates[-1]-lim)< 0.004,(tau, estimates, lim)
    assert abs(estimates[-1]-lim)<abs(estimates[0]-lim),(tau,estimates,lim)
print('PASS:',count,'high-precision contact, inclusion, endpoint and crossover diagnostics')
