#!/usr/bin/env python3
"""Reproducibility checks for the high-dimensional confined persistent-particle theorem.
All numerical checks are finite supporting tests, not substitutes for proof.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def moments(alpha):
    a=F(alpha)
    den=(a+1)*(a+2)*(a+3)
    es=1/(a+1)
    es4=6/den
    es22=(a+6)/den
    return es, es4, es22


def stick(rng, alpha, remainder_cut=1e-11):
    left=1.0
    out=[]
    while left>remainder_cut:
        u=rng.random()
        v=1-(1-u)**(1.0/alpha)
        p=left*v
        out.append(p)
        left*=1-v
        if len(out)>10000:
            raise RuntimeError('unusually slow stick tail')
    return out


def draw_q(rng, weights, dimension):
    coord=[0.0]*dimension
    for p in weights:
        z=[rng.gauss(0,1) for _ in range(dimension)]
        norm=sqrt(sum(t*t for t in z))
        for j,t in enumerate(z):
            coord[j]+=p*t/norm
    return sum(x*x for x in coord)


def main():
    asserts=0
    for aa in [F(1,2),F(1),F(2),F(3),F(5),F(7,2)]:
        a=aa
        es,es4,es22=moments(a)
        var=es22-es*es
        target=2*a/((a+1)**2*(a+2)*(a+3))
        assert var==target
        asserts+=1
        for d in [2,3,4,5,8,16,128]:
            finitevar=var+2*(es22-es4)/d
            targetvar=2*a*(d+a+1)/(d*(a+1)**2*(a+2)*(a+3))
            assert finitevar==targetvar
            asserts+=1
        # Fixed point moment recursions for V~Beta(1,a).
        b20=F(2,1)/((a+1)*(a+2))
        b40=F(24,1)/((a+1)*(a+2)*(a+3)*(a+4))
        b04=a/(a+4)
        b22=2*a/((a+2)*(a+3)*(a+4))
        # EV^2+ E(1-V)^2 ES=ES
        assert b20 + a/(a+2)*es == es
        asserts+=1
        assert b40 + 2*b22*es + b04*es22 == es22
        asserts+=1
    # The d=2 radial law is Q ~ Beta(1,a), yielding Var(Q)=a/((a+1)^2(a+2)).
    for aa in [F(1), F(2), F(3), F(5)]:
        a=aa
        es,es4,es22=moments(a)
        finitevar=es22-es*es + (es22-es4)
        assert finitevar == a/((a+1)**2*(a+2))
        asserts+=1
    rng=Random(227041)
    a=1.0
    for d,nreps in [(2,2000),(8,1500),(32,600)]:
        data=[]
        errors=[]
        for _ in range(nreps):
            weights=stick(rng,a)
            s2=sum(p*p for p in weights)
            q=draw_q(rng, weights, d)
            data.append(q)
            errors.append((q-s2)**2)
        avg=sum(data)/len(data)
        centeredvar=sum((x-avg)**2 for x in data)/len(data)
        mse=sum(errors)/len(errors)
        want_var=2*a*(d+a+1)/(d*(a+1)**2*(a+2)*(a+3))
        want_mse=2*a/(d*(a+1)*(a+2)*(a+3))
        print('dimension',d,'mean',round(avg,6),'target',.5,'variance',round(centeredvar,6),'target',round(want_var,6),'conditional_MSE',round(mse,6),'target',round(want_mse,6))
        assert abs(avg-0.5)<0.035
        assert abs(centeredvar-want_var)<0.035
        assert abs(mse-want_mse)<0.025
        asserts+=3
    print('PASS:',asserts,'checks: exact rational moment identities, known 2D beta-law, and finite simulation comparisons')

if __name__=='__main__':
    main()
