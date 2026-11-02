#!/usr/bin/env python3
"""Exact small-network and asymptotic corroboration for a pinned, attenuated directed ring."""
from __future__ import annotations
from fractions import Fraction
from math import comb, isclose, sqrt, pi, exp
from itertools import combinations


def central(r: int) -> Fraction:
    return Fraction(comb(2*r,r),4**r)


def segment_cost(length: int, gain: Fraction) -> Fraction:
    return sum((Fraction(length-a,2)*central(a)*gain**(2*a) for a in range(length)),Fraction(0))


def covariance_block(length: int, gain: Fraction):
    # From A P + P A^T + I = 0 for A = -I + gain * lower-shift.
    p=[[Fraction(0) for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            p[i][j]= (Fraction(i==j,2)
                + Fraction(gain,2)*((p[i-1][j] if i else 0)+(p[i][j-1] if j else 0)))
    for i in range(length):
        for j in range(length):
            # Explicit residual for -2P + g (SP + PS^T) + I =0.
            residual=-2*p[i][j]+gain*((p[i-1][j] if i else 0)+(p[i][j-1] if j else 0)) + (i==j)
            assert residual == 0, (length,gain,i,j,residual)
    return p


def gaps_of_set(n, selected):
    a=sorted(selected)
    return tuple((a[(j+1)%len(a)]-a[j])%n-1 if j+1<len(a) else ((a[0]+n-a[-1])-1) for j in range(len(a)))


def best_cost(n,k,gain):
    q,r=divmod(n-k,k)
    return (k-r)*segment_cost(q,gain)+r*segment_cost(q+1,gain)


def check():
    stats={'lyapunov_blocks':0,'leader_sets':0,'optimum_sets':0,'critical_checks':0}
    gs=[Fraction(1,3),Fraction(3,5),Fraction(1)]
    for g in gs:
        for length in range(0,11):
            p=covariance_block(length,g)
            assert sum((p[i][i] for i in range(length)),Fraction(0))==segment_cost(length,g)
            stats['lyapunov_blocks']+=1
        for n in range(2,11):
            for k in range(1,n+1):
                target=best_cost(n,k,g)
                opt=0
                for subset in combinations(range(n),k):
                    gaps=gaps_of_set(n,subset)
                    actual=sum((segment_cost(l,g) for l in gaps),Fraction(0))
                    assert actual>=target,(n,k,g,subset,gaps,actual,target)
                    iff=max(gaps)-min(gaps)<=1
                    assert (actual==target)==iff,(n,k,g,subset,gaps,actual,target)
                    stats['leader_sets']+=1
                    if iff: opt+=1
                q,r=divmod(n-k,k)
                assert opt*k==n*comb(k,r),(n,k,g,opt)
                stats['optimum_sets']+=opt
        # Exact strict convexity, including l=0.
        for l in range(0,100):
            assert segment_cost(l+2,g)-2*segment_cost(l+1,g)+segment_cost(l,g)== Fraction(central(l+1)*g**(2*l+2),2)
    # Check the unattenuated closed form against exact combinatorics.
    for l in range(0,100):
        assert segment_cost(l,Fraction(1))==Fraction(l*(2*l+1),3)*central(l)
    # Check finite-size crossover against direct finite sum, including c=0.
    import scipy.integrate as si
    for k in (1,2,3,7):
        for c in (0.,0.7,3.,10.):
            target=(k/(2*sqrt(pi)))*si.quad(lambda u:(1./k-u)*exp(-2*c*u)/sqrt(u),0.,1./k,epsabs=1e-12)[0]
            vals=[]
            for n in (500,2000,8000):
                gain=1-c/n
                q,r=divmod(n-k,k)
                def floating_segment(l):
                    power=1.; coefficient=1.; total=0.
                    for j in range(l):
                        total+=0.5*(l-j)*coefficient*power
                        power*=gain*gain
                        coefficient*= (2*j+1)/(2*j+2)
                    return total
                calc=((k-r)*floating_segment(q)+r*floating_segment(q+1))/n**1.5
                vals.append(abs(calc-target))
            assert vals[2] < 0.006,(k,c,vals,target)
            assert vals[2] < vals[0]+1e-12,(k,c,vals)
            stats['critical_checks']+=1
    print('PASS',stats)


if __name__=='__main__':
    check()
