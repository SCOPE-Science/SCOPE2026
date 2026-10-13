#!/usr/bin/env python3
"""Independent finite checks supporting the friendship-graph transfer theorem.

No finite test is used as a proof of an asymptotic assertion.
Uses only the Python standard library.
"""
import cmath
import math
from fractions import Fraction


def adjacency(m):
    n = 2*m+1
    a = [[0]*n for _ in range(n)]
    for j in range(m):
        u, v = 2*j+1, 2*j+2
        for p,q in ((0,u),(0,v),(u,v)):
            a[p][q] = a[q][p] = 1
    return a


def mv(a, v):
    return [sum(row[j]*v[j] for j in range(len(v))) for row in a]


def amplitude(m,t):
    delta = math.sqrt(8*m+1)
    e = cmath.exp
    return (-e(-1j*t)/2
       +(m-1)*e(1j*t)/(2*m)
       +e(1j*t/2)*(math.cos(delta*t/2)+1j*math.sin(delta*t/2)/delta)/(2*m))


def independent_exponential_entry(a,t,u,v):
    # Taylor with a rigorous term bound for the finite tested sizes and t <= 0.6.
    # Max row sum is 2m, so the absolute entry remainder after K terms
    # is <= exp(2mt) * (2mt)^(K+1)/(K+1)!.
    n=len(a)
    x=[0j]*n; x[u]=1j*0+1
    res=x[v]
    for k in range(1,170):
        x=mv(a,x)
        x=[(1j*t/k)*e for e in x]
        res+=x[v]
    return res


def g(beta,z):
    return 1+z*z/2-math.cos(beta+z)/math.sqrt(2)


def root(beta):
    l,h=-1.,0.
    for _ in range(100):
        z=(l+h)/2
        if z+math.sin(beta+z)/math.sqrt(2)>0: h=z
        else: l=z
    return (l+h)/2


def torus(m, x, phi):
    d=math.sqrt(8*m+1)
    return abs(((m-1)/(2*m))*cmath.exp(1j*x)-.5*cmath.exp(-3j*x)
               +1/(2*m)*(math.cos(phi)+1j*math.sin(phi)/d))**2


def periodic(m, x):
    d=math.sqrt(8*m+1)
    return torus(m,x,d*x)


def check():
    exact_eigen=0; exp_checks=0; asym=0
    for m in range(2,11):
        a=adjacency(m); n=len(a)
        vec=[0]*n; vec[1]=1;vec[2]=-1
        assert mv(a,vec)==[-k for k in vec]
        exact_eigen+=1
        if m>=2:
            vec=[0]*n;vec[1]=vec[2]=1;vec[3]=vec[4]=-1
            assert mv(a,vec)==vec
            exact_eigen+=1
        # Two-dimensional invariant symmetric block: A hub=outer total; A outer total=2m hub+outer total.
        hub=[1]+[0]*(n-1)
        outer=[0]+[1]*(n-1)
        assert mv(a,hub)==outer
        assert mv(a,outer)==[2*m]+[1]*(n-1)
        exact_eigen+=2
        for t in (.1,.3,.5):
            independent=independent_exponential_entry(a,t,1,2)
            target=amplitude(m,t)
            assert abs(independent-target)<2e-10,(m,t,independent,target)
            exp_checks+=1
    eps=1e-9
    for beta in (math.pi/4,3*math.pi/4):
        z=root(beta); deriv=z+math.sin(beta+z)/math.sqrt(2)
        assert abs(deriv)<2e-15
        assert g(beta,z)<g(beta,0)
        assert all(g(beta,z)<=g(beta,z+shift)+1e-12 for shift in [-4,-1,-.5,.5,1,4])
    c_irr=1-1/math.sqrt(2)
    c_plus=g(math.pi/4,root(math.pi/4))
    c_minus=g(3*math.pi/4,root(3*math.pi/4))
    assert .29289<c_irr<.29290<c_plus<.41931<1.30529<c_minus<1.30532
    for D in (65,67,69,71,73,75,77,79,81,83,85,87):
        if (D*D-1)%8: continue
        m=(D*D-1)//8
        # Exact squared-discriminant recurrence; numerical tests check the
        # local asymptotic optimizer near four and only four base peaks.
        pmax=0.
        for j in range(4):
            base=math.pi/4+j*math.pi/2
            for h in range(-1200,1201):
                z=h*.0025
                pmax=max(pmax,periodic(m,base+z/D))
        deficit=m*(1-pmax)
        target=c_plus if D%8 in (1,7) else c_minus
        assert abs(deficit-target)<.045,(D,deficit,target)
        asym+=1
    for m in (120,121,122,300,301,302):
        d=math.isqrt(8*m+1)
        if d*d==8*m+1: continue
        # Lower bound on the torus supremum using the exact x=pi/4
        # and maximizing projection over the fast phase (not a full optimizer).
        x=math.pi/4
        rho=math.sqrt((1+1/(8*m+1))/2)
        phi=math.atan2(math.sin(x)/math.sqrt(8*m+1),math.cos(x))
        deficit=m*(1-torus(m,x,phi))
        assert abs(deficit-c_irr)<.02,(m,deficit)
        asym+=1
    print(f'VERIFY_OK exact_invariant_subspace_checks={exact_eigen} '
          f'independent_matrix_exponentials={exp_checks} '
          f'finite_asymptotic_tests={asym} '
          f'constants={c_irr:.12f},{c_plus:.12f},{c_minus:.12f}')


if __name__=='__main__':
    check()
