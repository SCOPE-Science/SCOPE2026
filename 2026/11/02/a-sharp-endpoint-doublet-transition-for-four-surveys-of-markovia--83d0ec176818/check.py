"""Standalone exact checks for a four-visit binary-availability detection theorem.
Uses only Python's standard library.  These tests corroborate, but do not replace, the proof.
"""
from fractions import Fraction as F
from random import Random

def mult(v, m):
    return [sum(v[j] * m[j][i] for j in range(2)) for i in range(2)]

def no_detection(pi, det, x, y, z):
    diag = [F(1), F(1)-det]
    v = [(1-pi)*diag[0], pi*diag[1]]
    for lag in [x,y,z]:
        mat = [[1-pi+pi*lag, pi*(1-lag)],
               [(1-pi)*(1-lag), pi+(1-pi)*lag]]
        v = mult(v,mat)
        v = [v[i]*diag[i] for i in range(2)]
    return sum(v)

def polynomial(pi, det, x, y, z):
    a = 1-pi*det
    b = 1-(1-pi)*det
    c = pi*(1-pi)*det*det
    return (a**4+c*a*a*y+c*a*(a+b*y)*(x+z)
            +c*(c+b*b*y)*x*z)

def h(pi,det,u,R):
    a=1-pi*det;b=1-(1-pi)*det;c=pi*(1-pi)*det*det
    return c*u**4+a*a*u**3-a*b*R*u-a*a*R

rng=Random(20261027)
N=0
for _ in range(750):
    def rf(): return F(rng.randrange(1,24),24)
    p,d,x,y,z=[rf() for i in range(5)]
    assert no_detection(p,d,x,y,z)==polynomial(p,d,x,y,z)
    N+=1
p=d=F(1,2)
u=F(3,4)
R=F(117,448)
y=F(13,28)
a=1-p*d;b=1-(1-p)*d;c=p*(1-p)*d*d
assert u*u*y==R
assert h(p,d,u,R)==0
assert polynomial(p,d,u,y,u)==F(6903,16384)
assert h(p,d,F(1),R)>0
assert h(p,d,R,R)<0
assert a*b-c==1-d
N+=6
R=F(2,3)
assert polynomial(p,d,1,R,1)==F(31,64)
assert h(p,d,1,R)<0
N+=2
print('PASS:',N,'exact-rational checks; theorem requires analytical proof')
