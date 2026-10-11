"""Numerical regression checks for scaled Lorentz-cone metric projections.

The proof is analytic; sampling does not establish an all-parameter theorem.
Requires Python standard library only.
"""
import math
import random


def norm(v, p):
    return sum(abs(z)**p for z in v)**(1/p)


def project_wedge(t, u, p, k):
    if t >= k*abs(u):
        return (t, u)
    sign = 1 if u >= 0 else -1
    q = p/(p-1)
    coeff = max(0., (k**(q-1)*t+abs(u))/(1+k**q))
    return (k*coeff, sign*coeff)


def norm_prediction(p, k):
    q=p/(p-1)
    return (1+k**p)**(1/p)*(1+k**(q*(q-1)))**(1/q)/(1+k**q)


def tangent_expansion(p, k, c, epsilon):
    s=math.sqrt(1-c*c)
    y=(k,c,s)
    f=(-1,k*c,k*s)
    q=p/(p-1)
    v=tuple(math.copysign(abs(t)**(q-1), t) for t in f)
    h=(k*c,1.,0.)
    delta_sign = (k*c)**(q-1)-(k*c)**(p-1)
    z=(k*math.sqrt((c+epsilon)**2+s*s),c+epsilon,s)
    # Choose the displacement large enough to register numerically yet small
    # enough to remain in the strict differentiability regime.
    delta=abs(epsilon)*.005
    x=tuple(a+delta*b for a,b in zip(y,v))
    out=norm(tuple(a-b for a,b in zip(y,z)),p)
    inn=norm(tuple(a-b for a,b in zip(x,z)),p)
    return out/inn, delta_sign


def run():
    rnd=random.Random(123456)
    tested=0
    for p in (1.5, 2., 3., 4., 6.):
        for k in (0.3,0.7,1.,1.5,3.):
            C=norm_prediction(p,k)
            assert C >= 1-1e-12
            for _ in range(150):
                a=(rnd.uniform(-3,3),rnd.uniform(-3,3))
                b=(rnd.uniform(-3,3),rnd.uniform(-3,3))
                pa=project_wedge(*a,p,k)
                pb=project_wedge(*b,p,k)
                assert norm((pa[0]-pb[0],pa[1]-pb[1]),p)<= C*norm((a[0]-b[0],a[1]-b[1]),p)+2e-11
                tested+=1
            if p==2 or k==1:
                assert abs(C-1)<1e-11
            else:
                assert C>1+1e-4
    # Explicit analytic normal directions have P(y+delta*v)=y.
    # Expansion of the two-point quotient confirms the orientation.
    expanded=0
    for p in (1.5,3.,4.,6.):
        for k in (0.35,1.,2.):
            c=.63 if abs(.63*k-1)>.05 else .43
            q=p/(p-1)
            diff=(k*c)**(q-1)-(k*c)**(p-1)
            eta=math.copysign(.03,diff)
            ratio, sgn=tangent_expansion(p,k,c,eta)
            assert diff*eta>0 and ratio>1+5e-7,(p,k,ratio)
            expanded+=1
    print(f'VERIFY_OK wedge_pairs={tested} curved_cone_expansions={expanded}')


if __name__=='__main__':
    run()
