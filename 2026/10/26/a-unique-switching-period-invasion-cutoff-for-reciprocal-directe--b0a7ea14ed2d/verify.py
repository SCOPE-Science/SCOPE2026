#!/usr/bin/env python3
"""Direct arithmetic checks for mirror-directed two-group linearized SIS switching."""
import math
import random


def exponent_formula(a,b,beta,mu,T):
    k=math.sqrt(a*b)
    g=(a+b)/(2*k)
    return -mu+(2/T)*math.asinh(g*math.sinh(beta*k*T/2))


def exponent_from_monodromy(a,b,beta,mu,T):
    k=math.sqrt(a*b)
    z=beta*k*T/2
    c,s=math.cosh(z),math.sinh(z)
    # E1=exp(beta*T*A1/2), E2=exp(beta*T*A2/2), in reverse orientations.
    E1=((c,s*a/k),(s*b/k,c))
    E2=((c,s*b/k),(s*a/k,c))
    M=((E2[0][0]*E1[0][0]+E2[0][1]*E1[1][0], E2[0][0]*E1[0][1]+E2[0][1]*E1[1][1]),
       (E2[1][0]*E1[0][0]+E2[1][1]*E1[1][0], E2[1][0]*E1[0][1]+E2[1][1]*E1[1][1]))
    tr=M[0][0]+M[1][1]
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    rad=max(0.0,tr*tr-4*det)
    rho=(tr+math.sqrt(rad))/2
    return math.log(rho)/T-mu, det


def critical_period(a,b,beta,mu):
    lo=1e-5
    hi=1.0
    while exponent_formula(a,b,beta,mu,hi)>0:
        hi*=2
        assert hi<1e4
    for _ in range(95):
        m=(lo+hi)/2
        if exponent_formula(a,b,beta,mu,m)>0:lo=m
        else:hi=m
    return (lo+hi)/2


def run():
    rng=random.Random(412677)
    for _ in range(300):
        a,b=(math.exp(rng.uniform(-1,1)) for _ in range(2))
        beta=rng.uniform(0.1,2)
        mu=rng.uniform(0.1,2)
        T=rng.uniform(0.05,3)
        f=exponent_formula(a,b,beta,mu,T)
        g,det=exponent_from_monodromy(a,b,beta,mu,T)
        assert abs(f-g)<2e-11*(1+abs(f))
        assert abs(det-1)<5e-7
    # A direct second-derivative identity verifies strict concavity for unequal contacts.
    for _ in range(250):
        a,b=(math.exp(rng.uniform(-1,1)) for _ in range(2))
        if abs(a-b)<1e-6:continue
        gamma=(a+b)/(2*math.sqrt(a*b))
        z=rng.uniform(.02,2)
        eps=1e-4
        h=lambda x:math.asinh(gamma*math.sinh(x))
        second=(h(z+eps)-2*h(z)+h(z-eps))/eps**2
        analytic=gamma*(1-gamma**2)*math.sinh(z)/(1+gamma**2*math.sinh(z)**2)**1.5
        assert analytic<0
        assert abs(second-analytic)<1e-5
    a,b,beta,mu=9.0,1.0,1.0,4.0
    Tc=critical_period(a,b,beta,mu)
    assert 0.9472132<Tc<0.9472133
    assert exponent_formula(a,b,beta,mu,0.5)>0
    assert exponent_formula(a,b,beta,mu,1.0)<0
    assert exponent_formula(a,b,beta,mu,Tc/2)>exponent_formula(a,b,beta,mu,Tc)
    assert exponent_formula(a,b,beta,mu,2*Tc)<exponent_formula(a,b,beta,mu,Tc)
    # Quadratic fast-switching onset, with parameters fixed and recovery tending to beta*(a+b)/2.
    c2=beta**3*(a*b)**1.5*((a+b)/(2*math.sqrt(a*b)))*(((a+b)/(2*math.sqrt(a*b)))**2-1)/24
    assert abs(c2-10/3)<1e-12
    for eps in [.02,.005,.001]:
        tcrit=critical_period(a,b,beta,5-eps)
        leading=math.sqrt(eps/c2)
        assert abs(tcrit/leading-1)<.03
    assert abs(exponent_formula(4,4,1,3,.1)-exponent_formula(4,4,1,3,2))<1e-12
    print('PASS: 300 independent matrix-exponential checks; 250 concavity checks; unique positive threshold bracket; fast-switching onset tests.')
    print('Example threshold in (0.9472132,0.9472133), computed',repr(Tc))

if __name__=='__main__':run()
