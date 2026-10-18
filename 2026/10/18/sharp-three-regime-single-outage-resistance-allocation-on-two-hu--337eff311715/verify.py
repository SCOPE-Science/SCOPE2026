"""Independent finite checks of the symmetric K_(2,m) outage-resistance formulas.

Dependencies: Python 3, numpy, scipy, sympy. No external services.
"""
from fractions import Fraction as F
import math
import numpy as np
from numpy.linalg import pinv
import sympy as s

m,t,r,B=s.symbols('m t r B',positive=True)
A=m-1
lo=2*A/(m*m-3)
hi=A*A/2
H=2*(A+t*r)/B
f1=1+2/(m-2+r)
f2=1/r+2/A
assert s.factor(f1-f2)==s.factor((r-1)*((A*(m-2+r)-2*r)/(r*A*(m-2+r))))
assert s.simplify(s.diff((A+t*r)*f1,r)*(m-2+r)**2-(t*((m-2+r)**2+2*(m-2))-2*A))==0
assert s.simplify(s.diff((A+t*r)*f2,r)-(-(A/r**2)+2*t/A))==0
assert s.simplify((-m+2+s.sqrt(2*A/lo-2*(m-2))).subs(m,4))==1
assert s.simplify((A/s.sqrt(2*hi)).subs(m,4))==1

def optimum(mm, tt, BB=1.):
    lower=2*(mm-1)/(mm**2-3)
    upper=(mm-1)**2/2
    if tt<lower:
        ratio=-(mm-2)+math.sqrt(2*(mm-1)/tt-2*(mm-2))
    elif tt>upper:
        ratio=(mm-1)/math.sqrt(2*tt)
    else:
        ratio=1.
    a=BB/(2*(mm-1+tt*ratio))
    b=ratio*a
    value=max(1/a+2/((mm-2)*a+b),1/b+2/((mm-1)*a))
    return a,b,value

def observed(mm,w):
    nv=mm+2
    edge=[(0,i+2) for i in range(mm)]+[(1,i+2) for i in range(mm)]
    def res(i):
        L=np.zeros((nv,nv))
        for j,((v,z),conductance) in enumerate(zip(edge,w)):
            if i==j:continue
            vct=np.zeros(nv);vct[v]=1;vct[z]=-1
            L+=conductance*np.outer(vct,vct)
        v,z=edge[i]
        inv=pinv(L,rtol=1e-12)
        dr=np.zeros(nv);dr[v]=1;dr[z]=-1
        return float(dr@inv@dr)
    return max(res(i) for i in range(2*mm))

# Exactly rational three-regime data for the first overlapping-cycle case.
assert optimum(3,2/9)[0] == float(F(3,16))
assert optimum(3,2/9)[1] == float(F(9,16))
assert abs(optimum(3,2/9)[2]-8.)<1e-13
assert abs(optimum(3,1.)[2]-12.)<1e-13
assert abs(optimum(3,8.)[2]-36.)<1e-13
checks=5
for mm in [3,4,5,6,8]:
    Tlo=2*(mm-1)/(mm**2-3)
    Thi=(mm-1)**2/2
    for tt in [Tlo/10,Tlo*0.97,Tlo,(Tlo+Thi)/2,Thi,Thi*1.03,Thi*12]:
        a,b,target=optimum(mm,tt)
        assert a>0 and b>0
        ww=np.array([a]*(mm-1)+[b]+[a]*(mm-1)+[b])
        assert abs(2*(mm-1)*a+2*tt*b-1)<2e-12
        actual=observed(mm,ww)
        assert abs(actual-target)/target <1e-9,(mm,tt,target,actual)
        checks+=1
        cost=np.array([1]*(mm-1)+[tt]+[1]*(mm-1)+[tt])
        def obj(z):
            w=np.exp(z)/np.dot(cost,np.exp(z))
            return observed(mm,w)
        # Unrestricted asymmetric feasible competitors, not a proof of globality.
        if mm<=6 and tt in [Tlo/10,(Tlo+Thi)/2,Thi*12]:
            rng=np.random.default_rng(mm*100+int(tt*1000))
            for j in range(14):
                raw=ww*np.exp(rng.normal(0,0.8,size=2*mm))
                feasible=raw/np.dot(cost,raw)
                observed_value=observed(mm,feasible)
                assert observed_value>=target*(1-3e-8),(mm,tt,j,observed_value,target)
                checks+=1
print('PASS',checks,'independent spectral / unrestricted competitor checks plus symbolic identities')
