"""Exact reproducibility checks for a two-client affine extragradient stability comparison."""
from fractions import Fraction as Q
from itertools import product

ZERO = Q(0)
ONE = Q(1)

def add(x, y):
    return tuple(a+b for a, b in zip(x,y))

def scale(a,x):
    return tuple(a*u for u in x)

def norm2(x):
    return sum((a*a for a in x), ZERO)

def skew(omegas):
    n=2*len(omegas)
    A=[[ZERO for _ in range(n)] for _ in range(n)]
    for i,w in enumerate(omegas):
        A[2*i][2*i+1]=-w
        A[2*i+1][2*i]=w
    return A

def matvec(A,x):
    return tuple(sum((a*b for a,b in zip(row,x)),ZERO) for row in A)

def stage(z, sign, J, v, eta, kap):
    F=add(matvec(J,z),scale(sign,v))
    look=add(z,scale(-kap*eta,F))
    return add(z,scale(-eta,add(matvec(J,look),scale(sign,v))))

def exact_mean_norm2(z0,J,v,eta,kap,k,rr):
    total=ZERO
    cases=list(product((-ONE,ONE),repeat=k if rr else 2*k))
    for signs in cases:
        z=z0
        if rr:
            for e in signs:
                z=stage(z,e,J,v,eta,kap)
                z=stage(z,-e,J,v,eta,kap)
        else:
            for e in signs:
                z=stage(z,e,J,v,eta,kap)
        total+=norm2(z)
    return total/len(cases)

def predicted(z0,v,omegas,eta,kap,k,rr):
    deterministic=ZERO
    noise=ZERO
    for i,omega in enumerate(omegas):
        t=eta*omega
        r2=(ONE-kap*t*t)**2+t*t
        assert ZERO<r2<ONE,(eta,kap,omega,r2)
        h=t*t*(ONE+kap*kap*t*t)
        vi=(v[2*i],v[2*i+1])
        zi=(z0[2*i],z0[2*i+1])
        deterministic+=r2**(2*k)*norm2(zi)
        g=eta*eta*(ONE+kap*kap*t*t)*norm2(vi)
        noise+=g*(ONE-r2**(2*k))/(ONE-r2)*(h/(ONE+r2) if rr else ONE)
    return deterministic+noise

checks=0
for eta,omegas in [(Q(1,5),(ONE,)),(Q(1,2),(ONE,)),(Q(3,5),(ONE,)),(Q(1,5),(ONE,Q(3)))]:
    J=skew(omegas)
    z0=tuple(Q(i+1,3) for i in range(2*len(omegas)))
    v=tuple(Q((-1)**i*(i+2),5) for i in range(2*len(omegas)))
    for k in range(1,5):
        for rr in [False, True]:
            lhs=exact_mean_norm2(z0,J,v,eta,Q(4),k,rr)
            rhs=predicted(z0,v,omegas,eta,Q(4),k,rr)
            assert lhs==rhs,(eta,omegas,k,rr,lhs,rhs)
            checks+=1

# Check the named rational witness, and the exact threshold at eta=1/2.
kap=Q(4)
t=Q(3,5)
s=t*t
r2=(ONE-kap*s)**2+s
ratio=s*(ONE+kap*kap*s)/(ONE+r2)
wr=(ONE+kap*kap*s)/(2*kap-1-kap*kap*s)
assert ratio==Q(1521,971)
assert wr==Q(169,31)
assert wr*ratio==Q(257049,30101)
assert (Q(1,2)**2)*(ONE+kap*kap*Q(1,2)**2)/(ONE+(ONE-kap*Q(1,2)**2)**2+Q(1,2)**2)==ONE
print('VERIFY_OK',checks,'exact uniform-history moments; source-ratio threshold; mixed-frequency and rational stationary witness')
