#!/usr/bin/env python3
"""Finite diagnostic tests for a projection-relaxation Markov maximal norm."""
import cmath
import math
import random


def lam(b):
    return (1 + b + math.sqrt(max(0.0, (1-b)*(1+3*b)))) / 2


def profile_ratio(b):
    z = lam(b) - b*b
    if not (0 < b < 1 and z > 0):
        raise ValueError('interior probability needed')
    return b*(1-b)/z


def q_ratio(b):
    r=profile_ratio(b)
    mean=(1-b)+b*r
    return ((1-b)+b*mean**2)/((1-b)+b*r*r)


def random_check(groups, rng, cases=1500):
    n=sum(len(g) for g in groups)
    vals=[lam(k/len(g)) for g in groups for k in range(len(g)+1)]
    bound=max(vals)
    assert set(k for g in groups for k in g)==set(range(n))
    for _ in range(cases):
        z=[complex(rng.uniform(-2,2), rng.uniform(-2,2)) for _ in range(n)]
        out=z[:]
        for g in groups:
            avg=sum(z[k] for k in g)/len(g)
            for k in g:
                out[k]=max(abs(z[k]),abs(avg))
        inp=sum(abs(t)**2 for t in z)
        mx=sum(t*t for t in out)
        assert mx <= (bound+1e-11)*inp, (groups,mx/inp,bound)


def run():
    rng=random.Random(20261017)
    checks=0
    for n in range(2,151):
        vals=[(lam(k/n),k) for k in range(n+1)]
        best,j=max(vals)
        nearest=(2*n+1)//3   # floor(2n/3+1/2), all n integral
        assert j==nearest, (n,j,nearest)
        assert abs(best - lam(nearest/n))<1e-12
        if n%3==0:
            assert abs(best-4/3)<1e-12
        else:
            assert best < 4/3
        b=j/n
        assert abs(q_ratio(b)-best)<1e-12
        checks+=4
    for k in range(1,100):
        b=k/100
        alpha=1-b
        trace=1+b
        determinant=b*b
        L=lam(b)
        assert abs(L*(trace-L)-determinant)<1e-12
        assert abs(q_ratio(b)-L)<1e-12
        checks+=2
    assert abs(lam(2/3)-4/3)<1e-14
    assert abs(profile_ratio(2/3)-.25)<1e-14
    checks+=2
    # Complex-valued finite-atom and conditional-block probability tests.
    random_check([list(range(3))], rng, 1000)
    random_check([list(range(2)),list(range(2,5)),list(range(5,9))],rng,2500)
    random_check([list(range(2)),list(range(2,4)),list(range(4,6))],rng,2500)
    random_check([list(range(5)),list(range(5,10))],rng,2500)
    checks+=8500
    print('PASS: %d deterministic diagnostic assertions (plus vector consistency checks)'%checks)


if __name__=='__main__':
    run()
