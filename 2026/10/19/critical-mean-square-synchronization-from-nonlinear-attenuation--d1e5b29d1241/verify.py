"""Exact one-step verification of a three-agent noise-modulated consensus recurrence.

Requires Python 3 and the standard library only. This is supplementary to the proof.
"""
from fractions import Fraction as Q
from itertools import product


def state_update(x, gam, kap, signs):
    out=[]
    for i in range(3):
        j,k=[z for z in range(3) if z!=i]
        mod=kap/(1+(x[j]-x[k])**2)
        deterministic=x[i]+2*gam*((x[j]-x[i])+(x[k]-x[i]))
        noisy=2*gam*mod*((x[j]-x[i])*signs[2*i]+(x[k]-x[i])*signs[2*i+1])
        out.append(deterministic+noisy)
    return out


def dispersion(x):
    mean=sum(x)/3
    return sum((z-mean)**2 for z in x)


def conditional_formula(x,gam,kap):
    s=dispersion(x)
    lam=1-6*gam
    h=2*gam*kap
    total=Q(0)
    for i in range(3):
        j,k=[z for z in range(3) if z!=i]
        a=(x[j]-x[k])**2
        b=(x[i]-x[j])**2+(x[i]-x[k])**2
        total+=b/(1+a)**2
    return lam**2*s+Q(2,3)*h**2*total

checks=0
for gam,kap in [(Q(3,13),Q(1)),(Q(1,10),Q(1,2)),(Q(3,10),Q(2)),(Q(1,7),Q(3,2))]:
    for x in [(Q(0),Q(1),Q(2)),(Q(-2),Q(3),Q(3)),(Q(4,3),Q(-1,7),Q(5,2)),(Q(0),Q(0),Q(0)),(Q(7),Q(7),Q(9)),(Q(-1),Q(0),Q(4))]:
        e=sum((dispersion(state_update(x,gam,kap,ss)) for ss in product([-1,1],repeat=6)),Q(0))/64
        assert e == conditional_formula(x,gam,kap), (gam,kap,x,e,conditional_formula(x,gam,kap))
        checks+=1
        lam=1-6*gam; h=2*gam*kap
        rho=lam**2+4*h**2
        assert e<=rho*dispersion(x)
        checks+=1
        if gam==Q(3,13) and kap==1:
            s=dispersion(x)
            assert e<=s-3*h**2*s*s/(1+2*s)
            checks+=1
for x in [(Q(0),Q(1),Q(2)),(Q(-2),Q(3),Q(3)),(Q(0),Q(0),Q(0))]:
    a=(x[0]-x[1])**2;b=(x[0]-x[2])**2;c=(x[1]-x[2])**2
    s=dispersion(x)
    assert a*b+b*c+c*a==Q(9,4)*s*s
    checks+=1
# Critical identity of linearized variance amplification.
gam=Q(3,13);kap=Q(1)
assert (1-6*gam)**2+16*gam**2*kap**2==1
checks+=1
print(f'PASS: {checks} exact rational assertions')
