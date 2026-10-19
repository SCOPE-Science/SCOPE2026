"""Finite-bit truncating stochastic rounding: independent exact-arithmetic tests.

No random number libraries or external dependencies are used.
"""
from fractions import Fraction as F
from math import floor, ceil
from collections import defaultdict



def step_distribution(x, eta, tau, b):
    y = (1 - eta) * x + eta * tau
    j = y.numerator // y.denominator
    q = (b * (y - j)).numerator // (b * (y - j)).denominator
    return {j: F(b - q, b), j+1: F(q,b)} if q else {j: F(1)}


def stationary(tau, eta, b):
    c = b * eta
    u = (c*tau).numerator // (c*tau).denominator
    val = c * (1-tau)
    d = (val.numerator + val.denominator - 1) // val.denominator
    return F(u,u+d), F(u,b), F(d,b)


def exact_distribution(init, steps, eta, tau, b):
    dist = {init:F(1)}
    for _ in range(steps):
        nd=defaultdict(F)
        for x,px in dist.items():
            for y,py in step_distribution(x,eta,tau,b).items():
                nd[y] += px*py
        dist=dict(nd)
    return dist


def main():
    count = 0
    for b in [2,4,8,16,32]:
      for i in range(1,10):
       tau = F(i,10)
       for j in range(1,10):
        eta = F(j,10)
        pi,up,down=stationary(tau,eta,b)
        up_direct=step_distribution(0,eta,tau,b).get(1,F(0))
        down_direct=step_distribution(1,eta,tau,b).get(0,F(0))
        assert up==up_direct and down==down_direct
        assert pi*down==(1-pi)*up
        assert pi <= tau
        traps=[x for x in range(-100,101) if step_distribution(x,eta,tau,b)=={x:F(1)}]
        expected=[x for x in range(-100,101) if x<=0 and eta*(tau-x)< F(1,b)]
        assert traps==expected, (b,tau,eta,traps,expected)
        n=max(0,ceil(F(1,b)/eta-tau))
        assert len(traps)==n if n<101 else len(traps)==101
        # finite-step Markov recurrence from upper adjacent lattice point
        dist=exact_distribution(1,7,eta,tau,b)
        assert set(dist)<={0,1}
        lam=1-up-down
        assert dist.get(1,F(0)) == pi + (1-pi)*lam**7
        count += 1
    # Integer bit-step product exact quantization and nonmonotone stationary bias.
    for b in [8,16,32,64]:
     for c in range(1,b):
      for i in range(1,50):
       tau=F(i,50)
       pi,_,_=stationary(tau,F(c,b),b)
       expect=F((c*tau).numerator // (c*tau).denominator,c)
       assert pi==expect
       count += 1
    vals=[stationary(F(2,5),F(c,8),8)[0] for c in [3,4,5]]
    assert vals==[F(1,3),F(1,4),F(2,5)]
    # A uniform truncating finite-bit rounding markov chain has a persistent suboptimal point.
    eta=F(1,64);tau=F(2,5);b=4
    traps=[x for x in range(-30,3) if step_distribution(x,eta,tau,b)=={x:F(1)}]
    assert traps==list(range(-15,1))
    # Upward grid point hits the lower one with geometric survival.
    dist=exact_distribution(1,12,eta,tau,b)
    _,u,d=stationary(tau,eta,b)
    assert u==0 and d==F(1,b)
    assert dist.get(1,F(0)) == F(3,4)**12
    print(f"PASS {count} exact-rational parameter sets and {len(traps)} absorbing levels; integer scaling, geometric law, and nonmonotone example verified")

if __name__=='__main__':
    main()
