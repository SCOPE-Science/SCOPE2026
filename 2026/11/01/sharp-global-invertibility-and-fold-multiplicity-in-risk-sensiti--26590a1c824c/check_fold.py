"""Standalone reproducibility diagnostics for the risk-feedback learning map.
No external files required; Python 3 standard library plus mpmath.
"""
import math
import mpmath as mp
mp.mp.dps=70

def F(x,q,a,b,c,k,p0,p1):
    L=mp.log(x/(1-x))-a*(x-b+c*q)
    xp=1/(1+mp.exp(-L))
    qp=(1-k)*q+k*(p0+p1*x)
    return xp,qp

def jacobian(x,q,a,b,c,k,p0,p1):
    xp,_=F(x,q,a,b,c,k,p0,p1)
    j11=xp*(1-xp)*(1/(x*(1-x))-a)
    j12=-a*c*xp*(1-xp)
    j21=k*p1
    j22=1-k
    return j11*j22-j12*j21

p0=mp.mpf(0);p1=mp.mpf(1)/1000;c=mp.mpf(500);b=mp.mpf(1)/2;k=mp.mpf(2)/5;a=6*mp.log(3)
triples=[(mp.mpf(1)/4,mp.mpf(1)/1500),(mp.mpf(1)/2,mp.mpf(1)/2000),(mp.mpf(3)/4,mp.mpf(1)/3000)]
y=(1/(1+3*mp.sqrt(3)),mp.mpf(1)/2000)
for x,q in triples:
    xx,qq=F(x,q,a,b,c,k,p0,p1)
    assert mp.almosteq(xx,y[0],rel_eps=mp.mpf('1e-65')) and mp.almosteq(qq,y[1],rel_eps=mp.mpf('1e-65'))
    print('preimage',mp.nstr(x,7),mp.nstr(q,15),'target',mp.nstr(xx,25),mp.nstr(qq,15),'J',mp.nstr(jacobian(x,q,a,b,c,k,p0,p1),15))

B=(1-k-c*k*p1)/(1-k)
Lambda=a*B
assert Lambda > 4
s=mp.sqrt(1-4/Lambda)
lower=(1-s)/2; upper=(1+s)/2

def H(x):return mp.log(x/(1-x)) - Lambda*x
width=H(lower)-H(upper)
assert width>0 and mp.almosteq(width,Lambda*s-4*mp.atanh(s))
print('beta',mp.nstr(B,30),'Lambda',mp.nstr(Lambda,30),'folds',mp.nstr(lower,20),mp.nstr(upper,20),'width',mp.nstr(width,20))
for d in [mp.mpf('0.01'),mp.mpf('0.001'),mp.mpf('0.0001'),mp.mpf('0.00001')]:
    sd=mp.sqrt(d/(4+d))
    wd=4*(sd/(1-sd**2)-mp.atanh(sd))
    print('delta',d,'width/delta^1.5',mp.nstr(wd/d**mp.mpf('1.5'),20))
    assert abs(wd/d**mp.mpf('1.5')-mp.mpf(1)/3)<2*d

# Verify no Jacobian zeros when k above the critical coupling.
for kk in [mp.mpf(2)/3,mp.mpf(7)/10,mp.mpf(9)/10,mp.mpf(1)]:
    for aa in [mp.mpf(1),mp.mpf(10),mp.mpf(100)]:
        for xx in [mp.mpf(1)/10,mp.mpf(1)/2,mp.mpf(9)/10]:
            assert jacobian(xx,mp.mpf(1)/2000,aa,b,c,kk,p0,p1)>0
print('ALL EXACT / HIGH-PRECISION ASSERTIONS PASSED')
