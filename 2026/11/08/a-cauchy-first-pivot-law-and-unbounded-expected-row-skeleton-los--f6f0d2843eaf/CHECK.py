"""Deterministic independent checks for the planar Gaussian first-pivot law.
Only Python's standard library is required. Numeric enumeration is evidence, not a proof.
"""
from math import atan, pi, cos, sin, isclose
from fractions import Fraction

def theoretical_p(t):
    return 0.0 if t<=0.5 else 2*atan(2*t-1)/pi

def select(t,z1,z2):
    scores=(abs(z1),abs(z2),t*abs(z1+z2))
    return max(range(3),key=lambda i:scores[i])

def errors(t):
    rows=[(0.0+1,0.0),(0.0,1.0),(t,t)]
    v=[]
    for i in range(3):
        r=rows[i]; d=r[0]*r[0]+r[1]*r[1]
        loss=0.0
        for a in rows:
            s=a[0]*r[0]+a[1]*r[1]
            loss+=a[0]**2+a[1]**2-s*s/d
        v.append(loss)
    return v

for tt in (Fraction(1,5),Fraction(1,2),Fraction(1),Fraction(2),Fraction(7)):
    rows=[(Fraction(1),Fraction(0)),(Fraction(0),Fraction(1)),(tt,tt)]
    residual=[]
    for r in rows:
        norm=sum(a*a for a in r)
        residual.append(sum(sum(a*a for a in x)-sum(a*b for a,b in zip(x,r))**2/norm for x in rows))
    assert residual==[1+tt*tt,1+tt*tt,Fraction(1)]

N=120000
for t in (0.2,0.5,0.75,1,2,10,100):
    loss=errors(t)
    assert isclose(loss[0],1+t*t,rel_tol=1e-12)
    assert isclose(loss[1],1+t*t,rel_tol=1e-12)
    assert isclose(loss[2],1,rel_tol=1e-12)
    hits=sum(select(t,cos(2*pi*(j+0.5)/N),sin(2*pi*(j+0.5)/N))==2 for j in range(N))
    freq=hits/N
    assert abs(freq-theoretical_p(t))<2/N,(t,freq,theoretical_p(t))
    empirical=1+t*t*(1-freq)
    exact=1+t*t*(1-theoretical_p(t))
    assert abs(empirical-exact)<(2*t*t/N)

# Angular threshold only uses first Gaussian column, independently of how
# many additional columns would be supplied to a pivoting implementation.
for t in (0.7,2.0,13.0):
    for k in range(1,7):
        for j in range(100):
            a=cos(j*0.18+0.3); b=sin(j*0.17+0.4)
            extended=[(a,b)]+[(cos(h+j),sin(h-j)) for h in range(1,k)]
            assert select(t,*extended[0])==select(t,a,b)
print('PASS: exact rational projection identities, angular counts, and extra-column invariance')
