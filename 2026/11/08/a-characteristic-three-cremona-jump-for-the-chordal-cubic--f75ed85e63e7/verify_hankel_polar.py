#!/usr/bin/env python3
"""Exact finite-field corroboration of the Hankel cubic polar map."""
from itertools import product
from collections import Counter

def normalize(v,p):
    for a in v:
        if a%p:
            inv=pow(a,-1,p)
            return tuple((x*inv)%p for x in v)
    return None

def plucker(x,p):
    u=x[:4];v=x[1:]
    return tuple((u[i]*v[j]-u[j]*v[i])%p for i,j in ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)))

def polar(x,p):
    a,b,c,d,e,f=plucker(x,p)
    return ((f)%p,(-2*e)%p,(c+3*d)%p,(-2*b)%p,a%p)

def rational_normal(x,p):
    a,b,c,d,e,f=plucker(x,p)
    return not any((a,b,c,d,e,f))

def projective_pts(n,p):
    for pivot in range(n):
        for tail in product(range(p),repeat=n-1-pivot):
            yield (0,)*pivot+(1,)+tail

def test(p):
    counts=Counter()
    p0=(0,0,1,0,0)
    image=Counter()
    for x in projective_pts(5,p):
        a,b,c,d,e,f=plucker(x,p)
        assert (a*f-b*e+c*d)%p==0, ('Plucker',p,x)
        grad=polar(x,p)
        direct=((x[2]*x[4]-x[3]**2)%p,
                (2*x[2]*x[3]-2*x[1]*x[4])%p,
                (x[0]*x[4]+2*x[1]*x[3]-3*x[2]**2)%p,
                (2*x[1]*x[2]-2*x[0]*x[3])%p,
                (x[0]*x[2]-x[1]**2)%p)
        assert grad==direct,('gradient',p,x)
        if all(y==0 for y in grad):
            assert rational_normal(x,p) or (p==3 and x==p0),(p,x)
            counts['base']+=1
        else:
            image[normalize(grad,p)]+=1
        if rational_normal(x,p): counts['curve']+=1
    counts['domain']=sum(1 for _ in projective_pts(5,p))
    counts['image']=len(image)
    assert counts['curve']==p+1,counts
    assert counts['base']==p+1+(p==3),counts
    c=(0,0,(-3)%p,1,0,0)
    assert (c[0]*c[5]-c[1]*c[4]+c[2]*c[3])%p==(-3)%p
    print('prime',p,'total',counts['domain'],'quartic',counts['curve'],'base',counts['base'],'polar_image',counts['image'],'projection_center_on_Klein',(p==3))

for p in (3,5,7): test(p)
print('HANKEL_POLAR_EXACT_CHECKS_PASSED')
