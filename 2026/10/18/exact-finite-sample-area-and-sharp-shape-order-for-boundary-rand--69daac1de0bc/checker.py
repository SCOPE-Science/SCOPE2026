"""Independent exact-multinomial, moment, and geometric-sampling checks."""
from fractions import Fraction as F
from math import factorial, comb
import numpy as np

def conditional_mean(k):
    active=[i for i,x in enumerate(k) if x>0]
    if len(active)==1: return F(0)
    if len(active)==2:
        return F(1)-sum((F(1,k[i]+1) for i in active),F(0))
    return F(1)-sum((F(1,(k[i]+1)*(k[(i+1)%3]+1)) for i in range(3)),F(0))

def multinomial(n,p):
    total=F(0)
    for a in range(n+1):
        for b in range(n+1-a):
            c=n-a-b
            total+=F(comb(n,a)*comb(n-a,b))*p[0]**a*p[1]**b*p[2]**c*conditional_mean((a,b,c))
    return total

def closed(n,p):
    m=n+2
    H=F(1)-sum(((1-x)**m for x in p),F(0))+sum((x**m for x in p),F(0))
    return F(1)-H/(m*(m-1)*p[0]*p[1]*p[2])

def moment(n,p):
    k=n-1
    total=F(0)
    for a in range(k+1):
        for b in range(k+1-a):
            c=k-a-b
            total+=F(comb(k,a)*comb(k-a,b),(a+1)*(b+1)*(c+1))*p[0]**a*p[1]**b*p[2]**c
    return F(1)-n*total

cases=[(F(1,3),F(1,3),F(1,3)),(F(1,4),F(5,12),F(1,3)),(F(2,5),F(3,10),F(3,10)),(F(1,49),F(24,49),F(24,49)),(F(1,4),F(1,4),F(1,2))]
checks=0
for p in cases:
    for n in range(1,16):
        A=multinomial(n,p);B=closed(n,p);C=moment(n,p)
        assert A==B==C,(p,n,A,B,C)
        checks+=1
print('exact rational identities:',checks)

# Deterministic finite-sample quadrature of normalized area of the hull in
# cyclic boundary order; points are sampled by Euclidean arclength.
rng=np.random.default_rng(702691)
verts=np.array([[0.0,0.0],[3.0,0.0],[0.0,4.0]])
lengths=np.array([3.0,5.0,4.0]);L=12.0
p=(F(1,4),F(5,12),F(1,3))
for n in [3,5,8,15]:
    batch=60000
    t=np.sort(rng.uniform(0,L,(batch,n)),axis=1)
    seg=np.searchsorted(np.cumsum(lengths),t,side='right')
    start=np.r_[0.0,np.cumsum(lengths)[:-1]]
    u=(t-start[seg])/lengths[seg]
    pts=verts[seg]*(1-u[...,None])+verts[(seg+1)%3]*u[...,None]
    nxt=np.roll(pts,-1,axis=1)
    sample=(pts[...,0]*nxt[...,1]-pts[...,1]*nxt[...,0]).sum(axis=1)/12.0
    expected=float(closed(n,p))
    stderr=sample.std(ddof=1)/np.sqrt(batch)
    z=abs(sample.mean()-expected)/stderr
    assert z<5,(n,sample.mean(),expected,z)
    print('geometry',n,'predicted',round(expected,8),'observed',round(float(sample.mean()),8),'z',round(float(z),3))

for n in range(3,25):
    upper=F(1)-(F(3)**(n+2)-3*F(2)**(n+2)+3)/((n+1)*(n+2)*F(3)**(n-1))
    lower=F(1)-(F(4)-F(2)**(2-n))/(n+1)
    assert upper==closed(n,cases[0])
    assert 0<lower<upper<1
print('sharp endpoint formulas:',22)
print('ALL CHECKS PASSED')
