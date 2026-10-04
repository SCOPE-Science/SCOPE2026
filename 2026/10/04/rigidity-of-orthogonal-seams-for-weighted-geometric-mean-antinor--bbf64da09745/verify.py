from math import sqrt, prod
import random

random.seed(1731)

def fval(p,x):
    out=1.0
    for pi,xi in zip(p,x):
        out *= (xi/sqrt(pi))**pi
    return out

def grad(p,x):
    f=fval(p,x)
    return [f*pi/xi for pi,xi in zip(p,x)]

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

# Every claimed pairwise seam has its gradient tangent to the seam.
for d in range(2,10):
    raw=[0.2+random.random() for _ in range(d)]
    sm=sum(raw)
    p=[v/sm for v in raw]
    for i in range(d):
        for j in range(i+1,d):
            a=[0.0]*d
            a[i]=sqrt(p[j])
            a[j]=-sqrt(p[i])
            for _ in range(20):
                x=[0.3+2*random.random() for _ in range(d)]
                x[i]=sqrt(p[i]/p[j])*x[j]
                # normalize to the antisphere; gradient is degree zero, but this also
                # checks the stated domain exactly.
                q=fval(p,x)
                x=[v/q for v in x]
                assert abs(fval(p,x)-1.0) < 2e-12
                assert abs(dot(a,x)) < 2e-12
                assert abs(dot(a,grad(p,x))) < 5e-12

# A mixed-sign hyperplane with at least two positive coefficients fails the
# reciprocal-balance identity required by everywhere orthogonality.  These
# deterministic samples stress the proof's key nonconstant-simplex step.
examples=[
    ([1.0,2.0,-3.0],[0.2,0.3,0.5]),
    ([1.0,1.0,-1.0,-1.0],[0.1,0.2,0.3,0.4]),
    ([2.0,1.0,3.0,-4.0],[0.15,0.25,0.1,0.5]),
]
for a,p0 in examples:
    sm=sum(p0); p=[v/sm for v in p0]
    P=[k for k,v in enumerate(a) if v>0]
    N=[k for k,v in enumerate(a) if v<0]
    assert len(P)>=2 or len(N)>=2
    # Build two positive points on a.x=0 by choosing positive side masses y,z
    # with common total one.  Vary two masses on a side with cardinality >=2.
    def build(yvals,zvals):
        x=[1.0]*len(a)
        for k,y in zip(P,yvals): x[k]=y/a[k]
        for k,z in zip(N,zvals): x[k]=z/(-a[k])
        assert abs(dot(a,x)) < 2e-12
        return x
    if len(P)>=2:
        y1=[1/len(P)]*len(P); y2=y1[:]
        eps=min(y2[0],y2[1])/3
        y2[0]+=eps; y2[1]-=eps
        z=[1/len(N)]*len(N)
        x1=build(y1,z); x2=build(y2,z)
    else:
        z1=[1/len(N)]*len(N); z2=z1[:]
        eps=min(z2[0],z2[1])/3
        z2[0]+=eps; z2[1]-=eps
        y=[1/len(P)]*len(P)
        x1=build(y,z1); x2=build(y,z2)
    # At least one of the two points has nonzero orthogonality defect.
    defects=[abs(dot(a,grad(p,x1))),abs(dot(a,grad(p,x2)))]
    assert max(defects) > 1e-5

print('VERIFY_OK weighted geometric-mean seam rigidity')
