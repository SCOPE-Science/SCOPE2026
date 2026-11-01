#!/usr/bin/env python3
"""Reproduce the three-block first-order wash-off order classification.

Requires only the Python standard library. The exact rational block uses
three positive rates 3, 2, 1 and equal duration log(2).
"""
from fractions import Fraction as F
from itertools import permutations
from math import exp, log
from random import Random

N = 0

def check(condition, message):
    global N
    N += 1
    if not condition:
        raise AssertionError(message)


def z(rate, duration):
    return -__import__('math').expm1(-rate * duration) / rate


def direct_score(perm, m, s, duration):
    """Compute the exposure by integrating the two linked ODEs segmentwise."""
    total = 3 * duration
    remaining = m
    retained_integral = 0.0
    for k in perm:
        u = exp(-k * duration)
        zz = (1 - u) / k
        retained_integral += remaining * zz + s * (duration - zz) / k
        remaining = remaining * u + s * zz
    return m * total + s * total * total / 2 - retained_integral


def expected_score(perm, m, s, duration):
    """Permutation-dependent part only; all omitted terms are shared."""
    k1, k2, k3 = perm
    z1, z2, z3 = (z(k, duration) for k in perm)
    u1 = exp(-k1*duration)
    u2 = exp(-k2*duration)
    U = z1 + u1*z2 + u1*u2*z3
    return -m*U + s*k2*z1*z2*z3


def exact_score(perm, m, s):
    rates = {3: (F(1,8), F(7,24)), 2: (F(1,4), F(3,8)), 1: (F(1,2), F(1,2))}
    a,b,c = perm
    u_a,z_a = rates[a]
    u_b,z_b = rates[b]
    _,z_c = rates[c]
    return -m*(z_a+u_a*z_b+u_a*u_b*z_c)+s*b*z_a*z_b*z_c


def classify(rates, m, s, duration):
    a,b,c = rates
    za,zc = z(a,duration), z(c,duration)
    mx = (b,a,c) if m < s*zc else (a,b,c)
    mn = (b,c,a) if m < s*za else (c,b,a)
    return mx,mn


def run():
    all_exact=list(permutations((3,2,1)))
    for m in [F(1,100),F(1,4),F(7,24),F(1,3),F(1,2),F(3,4),F(2,1)]:
        scores={p:exact_score(p,m,F(1)) for p in all_exact}
        maxes={p for p,v in scores.items() if v==max(scores.values())}
        mines={p for p,v in scores.items() if v==min(scores.values())}
        predmax={(2,3,1)} if m<F(1,2) else ({(2,3,1),(3,2,1)} if m==F(1,2) else {(3,2,1)})
        predmin={(2,1,3)} if m<F(7,24) else ({(2,1,3),(1,2,3)} if m==F(7,24) else {(1,2,3)})
        check(maxes==predmax, f'exact max {m}: {maxes} vs {predmax}')
        check(mines==predmin, f'exact min {m}: {mines} vs {predmin}')
        for p in all_exact:
            check(isinstance(scores[p],F), 'score not exact')
    # Exact differences at m/s=1/3, tau=ln2, rates 3>2>1.
    sc={p:exact_score(p,F(1,3),F(1)) for p in all_exact}
    check(sc[(2,3,1)]-sc[(3,2,1)]==F(7,384),'wrong maximum gap')
    check(sc[(2,1,3)]-sc[(1,2,3)]==F(1,128),'wrong minimum gap')
    random=Random(9417)
    for j in range(2200):
        c=10**random.uniform(-1,1)
        b=c+10**random.uniform(-1,1)
        a=b+10**random.uniform(-1,1)
        duration=10**random.uniform(-2,.6)
        s=10**random.uniform(-1,1)
        m=s*10**random.uniform(-2,1)
        perms=list(permutations((a,b,c)))
        scores=[direct_score(p,m,s,duration) for p in perms]
        simplified=[expected_score(p,m,s,duration) for p in perms]
        offset=scores[0]-simplified[0]
        for p,v,sm in zip(perms,scores,simplified):
            check(abs(v-(sm+offset))<1e-7*(1+abs(v)), 'segment integration mismatch')
        expected_max,expected_min=classify((a,b,c),m,s,duration)
        margin=1e-10*(1+max(map(abs,scores)))
        check(direct_score(expected_max,m,s,duration)>=max(scores)-margin,'max rule fails')
        check(direct_score(expected_min,m,s,duration)<=min(scores)+margin,'min rule fails')
        za,zb,zc=(z(k,duration) for k in (a,b,c))
        gapmax=(a-b)*za*zb*(s*zc-m)
        gapmin=(b-c)*zb*zc*(m-s*za)
        check(abs((direct_score((b,a,c),m,s,duration)-direct_score((a,b,c),m,s,duration))-gapmax)<margin,'max threshold identity fails')
        check(abs((direct_score((b,c,a),m,s,duration)-direct_score((c,b,a),m,s,duration))-gapmin)<margin,'min threshold identity fails')
    print('VERIFY_OK assertions='+str(N))

if __name__=='__main__':
    run()
