#!/usr/bin/env python3
"""Reproduce finite checks for the geometric-block Lyapunov theorem.

This program checks finite instances, not the infinite-time proof.
It uses only the Python standard library.
"""
import math
from fractions import Fraction


def full_block(gamma, base, j):
    return base * (gamma**j - 1) // (gamma - 1)


def sign_end(gamma, base, j):
    # Geometric sum of signed block lengths, no floating point.
    return base * (1 - (-gamma)**j) // (1 + gamma)


def exact_partial(gamma, base, n):
    cumulative = 0
    j = 0
    while True:
        width = base * gamma**j
        if n < cumulative + width:
            return sign_end(gamma, base, j) + (-1)**j * (n-cumulative)
        cumulative += width
        j += 1


def constants(gamma):
    gg = float(gamma)
    D = (gg-1)/(gg+1) - 2*gg*math.log(gg)/(gg+1)**2
    R = 2*gg**(gg/(gg+1))/(gg+1)-1
    star = gg**(-gg/(gg+1))
    return D, R, star


def profile(gamma, z):
    D, _, _ = constants(gamma)
    return (D-1+z+2*math.log(1/z)/(gamma+1))/z


def direct_scan(gamma, base, j_max):
    end = full_block(gamma, base, j_max)
    n = 0
    S = 0
    raw_sum = 0.0
    harmonic_sum = 0.0
    selected = set([full_block(gamma, base, j) for j in range(1, j_max+1)])
    if j_max >= 3:
        D, R, star = constants(gamma)
        for j in range(3,j_max+1):
            selected.add(round(star*full_block(gamma,base,j)))
    recorded = {}
    for j in range(j_max):
        direction = 1 if j % 2 == 0 else -1
        for _ in range(base * gamma**j):
            n += 1
            S += direction
            L = S/n
            raw_sum += L
            harmonic_sum += L/n
            if n in selected:
                recorded[n] = (raw_sum/n, harmonic_sum/(sum(1/k for k in range(1,n+1)) if n < 100 else math.log(n)+0.5772156649015329))
        assert n == full_block(gamma,base,j+1)
        assert S == sign_end(gamma,base,j+1)
        assert S == exact_partial(gamma,base,n)
    assert n == end and len(recorded)==len(selected)
    D,R,star = constants(gamma)
    for j in range(max(5,j_max-3),j_max+1):
        N = full_block(gamma,base,j)
        sample = recorded[N][0]
        target = (-1)**(j-1)*D
        assert abs(sample-target)<0.015, (gamma,j,sample,target)
        zN = round(star*N)
        sampled = recorded[zN][0]
        target = (-1)**j*R
        assert abs(sampled-target)<0.02, (gamma,j,sampled,target)
    return (gamma,base,n, D,R,recorded[end][0],recorded[end][1])


def signed_step_check(gamma,base,n_max):
    # Independently propagate multiplicative axis counts of the given
    # alternating diagonal expansion: log lambda_1=3, log lambda_2=1.
    # After each geometric block the tracked original axis swaps.
    j=0
    remaining=base
    score1=0
    score2=0
    for n in range(1,n_max+1):
        if remaining == 0:
            j+=1
            remaining=base*gamma**j
        if j%2==0:
            score1+=3
            score2+=1
        else:
            score1+=1
            score2+=3
        remaining-=1
        signed=exact_partial(gamma,base,n)
        assert score1==2*n+signed
        assert score2==2*n-signed


def exact_rational_check():
    for gamma in (2,3,4,5,7):
        for base in (1,2,9):
            for j in range(1,14):
                N = full_block(gamma,base,j)
                S = sign_end(gamma,base,j)
                fraction = Fraction(S,N)
                assert abs(float(fraction) - ((-1)**(j-1))*(gamma-1)/(gamma+1)) <= 3*gamma**(-j)
                assert S==exact_partial(gamma,base,N)
    for gamma in (2,3,4,5,7):
        D,R,z = constants(gamma)
        assert 0<D<R<(gamma-1)/(gamma+1)<1
        assert 1/gamma < z < 1
        assert abs(profile(gamma,1)-D)<1e-12
        assert abs(profile(gamma,1/gamma)+D)<1e-12
        assert abs(profile(gamma,z)+R)<1e-12
        for t in [1/gamma + (1-1/gamma)*i/100 for i in range(101)]:
            assert -R-1e-12 <= profile(gamma,t) <= D+1e-12
    for gamma,base in [(2,3),(3,2),(4,1)]:
        signed_step_check(gamma,base,6000)


def main():
    exact_rational_check()
    results = [direct_scan(2,3,15),direct_scan(3,2,11),direct_scan(4,1,10)]
    for gamma,base,total,D,R,endB,endQ in results:
        print(f'PASS gamma={gamma}, base={base}, steps={total}, '
              f'D={D:.10f}, R={R:.10f}, terminal_signed_Cesaro={endB:.10f}, '
              f'logarithmic_mean={endQ:.10f}')
    print('ALL_CHECKS_PASSED; finite checks only')

if __name__=='__main__':
    main()
