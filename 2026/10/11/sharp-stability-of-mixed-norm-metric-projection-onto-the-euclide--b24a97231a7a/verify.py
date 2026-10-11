"""Reproducible finite sanity checks for a sharp two-dimensional metric projection.
The general theorem and the exact maximum are proved analytically in RESULT.md.
Only the Python standard library is needed.
"""
from math import sin,cos,pi,sqrt
from random import Random

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def add(a,b):
    return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)) for i in range(max(len(a),len(b)))]

def scale(a,r):return [r*x for x in a]

def der(a):return [i*a[i] for i in range(1,len(a))]
N=[1,0,0,-1,0,0,1]
D=[1,-1,1]
L=add(mul(der(N),D),scale(mul(N,der(D)),-3))
R=scale(mul(mul([-1,1],[1,1]),[1,-2,0,-2,1]),-3)
assert L[:len(R)]==R and all(v==0 for v in L[len(R):]),(L,R)

def mod4(x):return sum(abs(v)**4 for v in x)**.25

def project(x):
    if sum(v*v for v in x)<=1:return x
    lo,hi=0,pi/2
    g=(sqrt(5)-1)/2
    aa=hi-g*(hi-lo);bb=lo+g*(hi-lo)
    def obj(th):return (x[0]-cos(th))**4+(x[1]-sin(th))**4
    fa,fb=obj(aa),obj(bb)
    for _ in range(120):
        if fa>fb:
            lo=aa; aa=bb;fa=fb;bb=lo+g*(hi-lo);fb=obj(bb)
        else:
            hi=bb;bb=aa;fb=fa;aa=hi-g*(hi-lo);fa=obj(aa)
    th=(lo+hi)/2
    return cos(th),sin(th)

root=(1+sqrt(3)-sqrt((1+sqrt(3))**2-4))/2
t=root**(9/4)
a=1/sqrt(1+t*t);b=t*a
C=(1+2/sqrt(3))**.25
assert abs((1+t**4)**.25*(1+t**(4/9))**.75/(1+t**(4/3))-C)<1e-12
random=Random(47823)
for _ in range(200):
    x=(random.random()*3,random.random()*3)
    y=(random.random()*3,random.random()*3)
    px,py=project(x),project(y)
    ratio=mod4((px[0]-py[0],px[1]-py[1]))/mod4((x[0]-y[0],x[1]-y[1]))
    assert ratio<C+1e-5,(ratio,x,y)
for s in [0.1,0.025,0.002]:
    w=(a**(1/3),b**(1/3));x=(a+s*w[0],b+s*w[1])
    d=(-w[1]**(1/3),w[0]**(1/3)); c=mod4(d);d=(d[0]/c,d[1]/c)
    e=1e-4
    p0,p1=project(x),project((x[0]+e*d[0],x[1]+e*d[1]))
    observed=mod4((p1[0]-p0[0],p1[1]-p0[1]))/e
    # The maximum derivative at the designated point uses the inverse Jacobian.
    q=4/3
    denom=(a**q+b**q)+s*(q-1)*(a**(q-2)*b**q+a**q*b**(q-2))
    target=(a**4+b**4)**.25*(a**(q*(q-1))+b**(q*(q-1)))**(1/q)/denom
    assert abs(observed-target)<0.007,(s,observed,target)
print('VERIFY_OK polynomial_identity=1 random_pairs=200 tangential_derivatives=3 exact_constant=',C)
