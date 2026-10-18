#!/usr/bin/env python3
"""Independent finite checks of beta-Hausdorff row probabilities and energy.

The proofs of the asymptotic limits are analytical. These finite tests do not
certify infinite statements or bibliographic novelty.
"""
from fractions import Fraction
from math import comb, gamma, lgamma, exp, log, pi

def rising(x, n):
    z = Fraction(1)
    for j in range(n):
        z *= x+j
    return z

def exact_row(a,b,n):
    return [Fraction(comb(n,k))*rising(a,k)*rising(b,n-k)/rising(a+b,n)
            for k in range(n+1)]

def row_energy(n,a,b):
    # First probability computed through log gamma; following ones by exact ratio.
    p = exp(lgamma(n+b)-lgamma(b)+lgamma(a+b)-lgamma(n+a+b))
    energy=p*p
    for k in range(n):
        p*=((n-k)*(k+a))/((k+1)*(n-k+b-1))
        energy+=p*p
    return energy

def phi(u):
    if abs(u)<1e-8:
        return .5-u/3+u*u/6
    from math import expm1
    return (2*u+expm1(-2*u))/(4*u*u)

def profile(u,v):
    return (phi(u)+phi(v))/(pi*pi)

def main():
    cases=[(Fraction(1),Fraction(1)), (Fraction(1,2),Fraction(1,2)),
           (Fraction(1,4),Fraction(3,2)), (Fraction(2),Fraction(3)),
           (Fraction(2,3),Fraction(5,4))]
    checked=0
    for a,b in cases:
        for n in range(16):
            p=exact_row(a,b,n)
            assert sum(p)==1
            assert all(x>0 for x in p)
            assert p[0]==rising(b,n)/rising(a+b,n)
            assert exact_row(b,a,n)==p[::-1]
            checked+=1
    for n in range(16):
        p=exact_row(Fraction(1),Fraction(1),n)
        assert sum(x*x for x in p)==Fraction(1,n+1)
    for a,b in [(0.25,1.5),(0.5,0.5),(0.6,0.6),(1,1),(2,3)]:
        for n in (1,2,4,8,15):
            p=exact_row(Fraction(str(a)), Fraction(str(b)),n)
            s=float(sum(x*x for x in p))
            assert abs(row_energy(n,a,b)-s) <= 1e-9
    print('Exact-rational normalization, reflection, endpoint, and Cesaro checks:',checked+16)
    print('Floating recurrence versus exact finite energy: 25 checks')
    for u,v in [(0.,0.),(1.,0.),(-1.,.7),(.5,2.)]:
        N=2200; L=log(N)
        a=.5+u/L; b=.5+v/L
        E=sum(row_energy(n,a,b) for n in range(N))
        pred=L*L*profile(u,v)
        print(f'cross-window u={u:+.2f},v={v:+.2f}: E={E:.8f}, leading={pred:.8f}, remainder/logN={(E-pred)/L:.6f}')
        assert E>0 and pred>0 and abs(E-pred)<12*L
    # At the uniform-measure point, each row has mass 1/(n+1).
    N=2200
    E=sum(row_energy(n,1,1) for n in range(N))
    H=sum(1/(n+1) for n in range(N))
    assert abs(E-H)<1e-8
    print('Finite Cesaro harmonic identity and crossover diagnostics passed.')
if __name__=='__main__':
    main()
