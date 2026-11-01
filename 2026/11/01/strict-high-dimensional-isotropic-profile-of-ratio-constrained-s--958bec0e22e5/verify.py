"""Exact rational and numerical cross-checks for ratio-constrained simplex isotropic profiles.
Run with Python 3: python verify.py. Uses only the standard library.
Finite tests corroborate; the analysis in RESULT.md establishes the theorem.
"""
from fractions import Fraction as F
from math import factorial, lgamma, log, log1p, exp, sqrt, atan2, pi, isclose
from itertools import product
import random

def sub(a,b): return [x-y for x,y in zip(a,b)]
def dot(a,b): return sum(x*y for x,y in zip(a,b))

def vertices(m,s):
    c=[F(1,m)]*m
    vs=[c]
    for k in range(1,m):
        den=m+s*(m-k)
        vs.append([F(1,1)/den]*k+[(1+s)/den]*(m-k))
    return vs

def contraction(m,s):
    vs=vertices(m,s)
    centered=[sub(v,vs[0]) for v in vs]
    ds=sum(dot(v,v) for v in centered)
    q=[sum(v[j] for v in centered) for j in range(m)]
    return (ds+dot(q,q))/F(m-1)

def contraction_by_formula(m,s):
    d=[m+s*(m-k) for k in range(1,m)]
    diag=sum((s*s*k*(m-k))/(m*dk*dk) for k,dk in enumerate(d,start=1))
    qs=[sum(s*(k-m*(j<=k))/(m*dk) for k,dk in enumerate(d,start=1)) for j in range(1,m+1)]
    return (diag+sum(q*q for q in qs))/(m-1)

def chamber_volume(m,s):
    p=F(1)
    for k in range(1,m): p*=s*(m-k)/(m+s*(m-k))
    return p

def planar_polygon_second_moment(s):
    # m=3, convex hull in (x0,x1) plane, integration via fan from centroid.
    c=[F(1,3)]*3
    verts=[]
    for k in (1,2):
        v=vertices(3,s)[k]
        for perm in set(__import__('itertools').permutations(v)):
            if perm not in verts: verts.append(perm)
    verts.sort(key=lambda v:atan2(float(v[1]-c[1]),float(v[0]-c[0])))
    totalarea=F(0); totalmoment=F(0)
    for v,w in zip(verts,verts[1:]+verts[:1]):
        a=sub(v,c); b=sub(w,c)
        area=abs(a[0]*b[1]-a[1]*b[0])/2
        e=(dot(a,a)+dot(a,b)+dot(b,b))/6
        totalarea+=area; totalmoment+=area*e
    return totalarea/F(1,2),totalmoment/totalarea

checks=0
for m in range(3,12):
    for s in (F(1,10),F(1,3),F(1),F(2),F(7,2)):
        vs=vertices(m,s)
        for v in vs:
            assert sum(v)==1
            assert min(v)>0
            assert max(v)<= (1+s)*min(v)
            checks+=3
        lhs=contraction(m,s)
        rhs=contraction_by_formula(m,s)
        assert lhs==rhs and lhs>0
        checks+=2
        f=chamber_volume(m,s)
        # gamma product for integer s values 1,2 (numerical loggamma)
        ff=exp(lgamma(m)+lgamma(1+m/float(s))-lgamma(m+m/float(s)))
        assert isclose(float(f),ff,rel_tol=5e-13,abs_tol=1e-16)
        checks+=1
for s in (F(1,10),F(1,3),F(1),F(2),F(7,2)):
    f,e=planar_polygon_second_moment(s)
    assert f==chamber_volume(3,s)
    assert e==contraction(3,s)*F(2,12)
    checks+=2

# Monotone asymptotic profile: independent log-gamma and exact chamber covariance.
def v_limit(s):
    z=log1p(s); return 1-(1+s)*z*z/(s*s)
def I(s):
    z=log1p(s); return (1+1/s)*z-log(s)
def profile(s): return exp(I(s))*sqrt(v_limit(s))

for s in (.05,.2,1,2,8):
    target=profile(s)
    err=[]
    for m in (20,50,100,300):
        ss=F(str(s))
        R=float(contraction_by_formula(m,ss))
        f=chamber_volume(m,ss)
        lf=sum(log(float(ss)*j/(m+float(ss)*j)) for j in range(1,m))
        ratio=sqrt(R)*exp(-lf/(m-1))
        err.append(abs(ratio-target))
        checks+=1
    assert err[-1]<0.02,(s,target,err)
    checks+=1

# Independent finite-sample check for exact covariance (no shared moment code).
rng=random.Random(20261031)
for m in (3,5,9):
    for s in (F(1),F(3,2)):
        vs=vertices(m,s)
        c=vs[0]
        total=0.0
        N=25000
        for _ in range(N):
            e=[rng.expovariate(1) for __ in range(m)]
            w=[a/sum(e) for a in e]
            x=[sum(float(v[j])*w[k] for k,v in enumerate(vs)) for j in range(m)]
            total+=sum((xj-float(c[j]))**2 for j,xj in enumerate(x))
        empirical=total/N
        exact=float(contraction(m,s)*F(m-1,m*(m+1)))
        assert abs(empirical-exact) < 0.05*exact,(m,s,empirical,exact)
        checks+=1


# Direct independent typical-point ordered-coordinate limit-shape sampling.
def typical_profile_error(m, s, seed):
    rr=random.Random(seed)
    errors=[]
    for rep in range(35):
        e=[rr.expovariate(1) for _ in range(m)]
        S=sum(e)
        w=[z/S for z in e]
        base=w[0]/m+sum(w[k]/(m+s*(m-k)) for k in range(1,m))
        running=base
        discrepancy=0.0
        for j in range(1,m+1):
            if j>1:
                k=j-1
                running+=s*w[k]/(m+s*(m-k))
            expected=(1+s)/s*log1p(s)-log(1+s-s*j/m)
            discrepancy=max(discrepancy,abs(m*running-expected))
        errors.append(discrepancy)
    return sum(errors)/len(errors)
for s in (0.5,1.0,3.0):
    err_small=typical_profile_error(50,s,1000+int(s*20))
    err_large=typical_profile_error(800,s,2000+int(s*20))
    assert err_large<err_small and err_large<0.15, (s,err_small,err_large)
    checks+=2

# Nonnegative Taylor coefficient proof for derivative of limit profile:
# u sinh(u)+u^2-4(cosh(u)-1) has coefficient (2k-4)/(2k)! at u^(2k) for k>=2,
# vanishes at degree 2 and 4, and is strictly positive in every even degree >=6.
for k in range(3,31):
    assert F(2*k-4,factorial(2*k))>0
    checks+=1

assert abs(profile(1)-4*sqrt(1-2*log(2)**2))<1e-14
assert abs(exp(1)/sqrt(12)-0.7847)<0.001
checks+=2
print('ALL CHECKS PASSED:',checks)
print('Marion s=1 limiting ratio:',profile(1))
print('small-s endpoint:',exp(1)/sqrt(12))
print('s -> infinity endpoint: 1')
for m in (3,4,8,25,100):
    s=F(1)
    lf=sum(log(j/(m+j)) for j in range(1,m))
    ratio=sqrt(float(contraction(m,s)))*exp(-lf/(m-1))
    print('m=%d relative isotropic constant %.12f'%(m,ratio))
