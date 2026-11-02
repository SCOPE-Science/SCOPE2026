"""Standalone checks for a two-spin Ising annealing passivity threshold.

Standard-library only. The analytic monotonicity proof is in the theorem statement;
finite diagnostics supplement rather than replace that proof.
"""
from fractions import Fraction as F
import math


def exact_witness():
    # Energies (++),(+-),(-+),(--) = 0,4,4,5; initial beta = log(20/19).
    w = [F(1), F(19,20)**4, F(19,20)**4, F(19,20)**5]
    z = sum(w)
    p0 = [x/z for x in w]
    energies = [0,4,4,5]
    neighbors = {0:[1,2],1:[0,3],2:[0,3],3:[1,2]}
    # Rate for transition source -> target equals 1/(1+(3/2)^(Etarget-Esource)).
    p1 = [F(0) for i in range(4)]
    for src in range(4):
        total = F(0)
        for dest in neighbors[src]:
            delta = energies[dest]-energies[src]
            acc = F(1)/(1 + F(3,2)**delta)
            jump = p0[src]*acc/2
            p1[dest] += jump
            total += jump
        p1[src] += p0[src]-total
    y,z0 = w[1],w[3]
    Z = sum(w)
    f,g = F(16,97),F(2,5)
    H = (3*g-1)*(y+z0)-f*(1+y)
    assert H == F(293719,16000000)
    assert p1[3] == g*(y+z0)/Z
    assert p1[1] == (y*(1+f-g)+f+z0*(1-g))/(2*Z)
    assert p1[1] == p1[2]
    assert p1[3]-p1[1] == H/(2*Z) == F(293719,108889390)
    # beta2=log2, tanh((beta2/2)*(4-5)) = -1/3.
    local = sum(-F(1,3)*(p1[3]-p1[j]) for j in (1,2))
    assert local == F(-293719,163334085)
    assert sum(p0) == sum(p1) == 1
    # Current Glauber activity at beta2, for this special example.
    activity=F(0)
    for src in range(4):
        for dst in neighbors[src]:
            acc=F(1)/(1+F(2)**(energies[dst]-energies[src]))
            activity+=p1[src]*acc/2
    assert activity < F(1,2)  # No activity-conjecture counterexample is claimed.
    return {'p0':p0, 'p1':p1,'H':H,'P_last':local,'activity':activity}


def threshold_function(A,B,beta0,beta1):
    y=math.exp(-beta0*A)
    z=math.exp(-beta0*B)
    f=1/(1+math.exp(beta1*A))
    g=1/(1+math.exp(beta1*(B-A)))
    return (3*g-1)*(y+z)-f*(1+y)


def threshold(A,beta0,beta1):
    assert A>0 and 0<=beta0<beta1
    lo=A
    hi=A+math.log(2)/beta1
    assert threshold_function(A,lo,beta0,beta1)>0
    assert threshold_function(A,hi,beta0,beta1)<0
    for _ in range(90):
        mid=(lo+hi)/2
        if threshold_function(A,mid,beta0,beta1)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def diagnostics():
    import random
    random.seed(51022023)
    checks=0
    for _ in range(1000):
        A=random.uniform(.2,5)
        beta0=random.uniform(0,1.2)
        beta1=beta0+random.uniform(.0001,1.3)
        star=threshold(A,beta0,beta1)
        assert A<star<A+math.log(2)/beta1
        left=(A+star)/2
        right=star+(A+math.log(2)/beta1-star)/2
        assert threshold_function(A,left,beta0,beta1)>0
        assert threshold_function(A,right,beta0,beta1)<0
        # In ferromagnetic range B<2A there is always an open violation interval.
        B=A+min((star-A)/2,A/2)
        assert A<B<2*A and threshold_function(A,B,beta0,beta1)>0
        checks+=5
    return checks

if __name__=='__main__':
    e=exact_witness()
    checks=diagnostics()
    print('exact stationary and transition identities: PASS')
    print('P_(--):',e['P_last'],'approximately',float(e['P_last']))
    print('next-step activity:',e['activity'],'approximately',float(e['activity']))
    print('parameter diagnostics:',checks,'PASS')
    print('nominal example B_star:',threshold(4,math.log(20/19),math.log(1.5)))
