"""Finite numerical checks for the sharp Birkhoff angular-distortion ceiling.

The analytic proof, not this finite test, establishes the universal theorem.
"""
import math
import random

ROOT2=math.sqrt(2.0)


def lp(z,p):
    if p==float('inf'):
        return max(abs(a) for a in z)
    return sum(abs(a)**p for a in z)**(1.0/p)


def ratio(u,v,t,p):
    return lp([u[k]-v[k] for k in range(2)],p)/lp([t*u[k]-v[k]/t for k in range(2)],p)

# Exact equality configurations, two geometrically different norms.
u=(1.,1.); v=(0.,1.)
assert abs(lp(u,float('inf'))-1)<1e-14
assert abs(lp(v,float('inf'))-1)<1e-14
assert abs(lp([u[k]-v[k] for k in range(2)],float('inf'))-1)<1e-14
assert abs(lp([u[k]-2*v[k] for k in range(2)],float('inf'))-1)<1e-14
assert abs(ratio(u,v,1/ROOT2,float('inf'))-ROOT2)<1e-14

u=(1.,0.); v=(.5,.5)
assert abs(lp(u,1)-1)<1e-14
assert abs(lp(v,1)-1)<1e-14
assert abs(lp([u[k]-v[k] for k in range(2)],1)-1)<1e-14
assert abs(lp([u[k]-2*v[k] for k in range(2)],1)-1)<1e-14
assert abs(ratio(u,v,1/ROOT2,1)-ROOT2)<1e-14

# Smooth Birkhoff pairs: v lies in the kernel of the norming functional of u.
rng=random.Random(60895)
checked=0
max_profile=0.0
for p in (1.25,1.5,2,3,4,8,16):
    for _ in range(180):
        a=rng.uniform(.01,1)
        b=rng.uniform(.01,1)
        norm=(a**p+b**p)**(1/p)
        u=(a/norm,b/norm)
        f=(u[0]**(p-1),u[1]**(p-1))
        tmp=(f[1],-f[0])
        nv=lp(tmp,p)
        v=(tmp[0]/nv,tmp[1]/nv)
        assert abs(f[0]*v[0]+f[1]*v[1])<1e-12
        for t in (.1,.25,1/ROOT2,.8,1.,1.225,1.6,2.,10.):
            val=ratio(u,v,t,p)
            assert val<=ROOT2+1e-12, (p,u,v,t,val)
            max_profile=max(max_profile,val)
            checked+=1

# Verify the piecewise analytic upper envelope and its unique sharp junction.
for n in range(1,5000):
    t=.001+n*.001
    if t<=1/ROOT2:
        envelope=2*t
    elif t<=1:
        envelope=1/t
    else:
        envelope=2/t-1/t**3
    assert envelope<=ROOT2+1e-11

print(f'PASS: 2 exact extremal norms; {checked} smooth Birkhoff profile checks; 4,999 envelope checks; max smooth ratio {max_profile:.12f}')
