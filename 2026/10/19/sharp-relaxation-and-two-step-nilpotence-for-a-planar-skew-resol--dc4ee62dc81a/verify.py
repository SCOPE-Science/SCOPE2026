"""Reproduce the planar skew-resolvent spectral identities and critical tuning.

Requires only the Python standard library. Finite numerical tests do not replace
analytical stability and uniqueness arguments in the accompanying result.
"""
from fractions import Fraction as Q
import cmath
import math
import random


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def matrix(q, c, tau, rho):
    h, s = tau * q, tau * c
    den = 1 + s*s
    D = [[(s*s+h)/den, -s/den], [s*(1-h)/den, s*s/den]]
    return [[(1 if i == j else 0)-rho*D[i][j] for j in range(2)] for i in range(2)]


def spectral(q, c, tau, rho):
    h, s = tau*q, tau*c
    t = (2*s*s+h)/(1+s*s)
    d = s*s/(1+s*s)
    delta = t*t-4*d
    mu = [(t+cmath.sqrt(delta))/2, (t-cmath.sqrt(delta))/2]
    return max(abs(1-rho*m) for m in mu), (t, d, delta)


def critical(q, c):
    if not 0 < q < 2*c:
        return None
    tau = (4*c*c-q*q)/(4*c*c*q)
    rho = (4*c*c+q*q)/(4*c*c-q*q)
    return tau, rho


def check_exact():
    q,c = Q(3,2),Q(1)
    tau,rho=critical(q,c)
    assert tau==Q(7,24) and rho==Q(25,7)
    K=matrix(q,c,tau,rho)
    assert K==[[Q(-18,25),Q(24,25)], [Q(-27,50),Q(18,25)]]
    assert mul(K,K)==[[Q(0),Q(0)],[Q(0),Q(0)]]
    assert K!=[[Q(0),Q(0)],[Q(0),Q(0)]]
    assert rho>2
    # A second rational instance, including a different parameter ratio.
    q,c=Q(1),Q(1)
    tau,rho=critical(q,c)
    K=matrix(q,c,tau,rho)
    assert tau==Q(3,4) and rho==Q(5,3)
    assert mul(K,K)==[[Q(0),Q(0)],[Q(0),Q(0)]]
    return 9


def check_grids():
    rng=random.Random(20260930)
    checked=0
    for _ in range(5000):
        q=10**rng.uniform(-1,1)
        c=10**rng.uniform(-1,1)
        tau=10**rng.uniform(-2,1)
        rho=10**rng.uniform(-2,1)
        h,s=q*tau,c*tau
        r,(t,d,disc)=spectral(q,c,tau,rho)
        K=matrix(q,c,tau,rho)
        tr=K[0][0]+K[1][1]
        determinant=K[0][0]*K[1][1]-K[0][1]*K[1][0]
        assert abs(tr-(2-rho*t))<1e-9*max(1,abs(tr))
        assert abs(determinant-(1-rho*t+rho*rho*d))<1e-9*max(1,abs(determinant))
        assert abs(disc-(h*h+4*s*s*(h-1))/(1+s*s)**2)<1e-8*max(1,abs(disc))
        root_disc=(tr*tr-4*determinant)
        assert abs(r-max(abs((tr+cmath.sqrt(root_disc))/2),abs((tr-cmath.sqrt(root_disc))/2)))<5e-7*max(1,r)
        if disc>=1e-10:
            cap=4/(t+math.sqrt(disc))
            optim=2/t
            ropt=math.sqrt(disc)/t
        elif disc<=-1e-10:
            cap=t/d
            optim=t/(2*d)
            ropt=math.sqrt(max(0,1-t*t/(4*d)))
        else:
            checked+=4
            continue
        assert (r<1)==(rho<cap) or abs(r-1)<2e-10
        r_check=spectral(q,c,tau,optim)[0]
        assert abs(r_check-ropt)<1e-7
        for fac in (0.65,0.95,1.05,1.35):
            alternate=spectral(q,c,tau,optim*fac)[0]
            assert alternate+1e-8>=r_check
        checked+=10
    return checked


def check_exact_rationals():
    checks=0
    for qi in range(1,12):
        for ci in range(1,8):
            q,c=Q(qi,4),Q(ci,2)
            vals=critical(q,c)
            if vals is None: continue
            tau,rho=vals
            K=matrix(q,c,tau,rho)
            assert mul(K,K)==[[Q(0),Q(0)],[Q(0),Q(0)]]
            assert K!=[[Q(0),Q(0)],[Q(0),Q(0)]]
            checks+=2
    return checks

if __name__=='__main__':
    a=check_exact();b=check_grids();c=check_exact_rationals()
    print('PASS exact rational cases:',a)
    print('PASS random matrix, phase and rate checks:',b)
    print('PASS rational two-step families:',c)
    print('PASS total:',a+b+c)
