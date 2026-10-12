#!/usr/bin/env python3
"""Independent finite and constructive checks of the digit-sum reflection theorem."""
from math import gcd
from itertools import product

def digit_sum(n, base):
    s = 0
    while n:
        n, r = divmod(n, base)
        s += r
    return s

def word(base, mod, size):
    return tuple(digit_sum(n, base) % mod for n in range(size))

def finite_factors(w, length):
    return {w[i:i+length] for i in range(len(w)-length+1)}

def all_two_factors(base, mod):
    increments = {(1-(base-1)*r)%mod for r in range(mod)}
    return {(a,(a+d)%mod) for a in range(mod) for d in increments}

def reflection_count(F):
    return len({min(w,w[::-1]) for w in F})

def predicted_two(base, mod):
    g = gcd(base-1, mod)
    if g == 1:
        return mod*(mod+1)//2
    if g == 2:
        assert mod%2 == 0
        return mod*mod//4
    return mod*mod//g

def high_part_for_sum(base,a):
    # The base-b expansion has a ones in pairwise-distinct positions.
    return sum(base**k for k in range(1,a+1))

f2_cases = 0
pal_witnesses = 0
for base, mod in product(range(2,10),range(1,13)):
    g = gcd(base-1,mod)
    F2 = all_two_factors(base,mod)
    assert len(F2) == mod*mod//g
    assert reflection_count(F2) == predicted_two(base,mod)
    for r in range(mod):
        for a in range(mod):
            # n has r trailing (b-1)-digits. The separated high part
            # changes only its initial digit sum, with no carry.
            h = high_part_for_sum(base,a)
            n = h*(base**r)+(base**r-1)
            pair = (digit_sum(n,base)%mod,digit_sum(n+1,base)%mod)
            assert pair in F2
            assert ((pair[1]-pair[0])%mod) == ((1-(base-1)*r)%mod)
    # Every abstract pair is realized by selecting a suitable a,r,
    # with a shifted by the r-dependent trailing digit sum.
    for pair in F2:
        a,d=pair[0],(pair[1]-pair[0])%mod
        rr=next(r for r in range(mod) if (1-(base-1)*r)%mod == d)
        t=(a-rr*(base-1))%mod
        h=high_part_for_sum(base,t)
        n=h*(base**rr)+(base**rr-1)
        assert (digit_sum(n,base)%mod,digit_sum(n+1,base)%mod)==pair
    if mod >= 3:
        if g in (1,2):
            rr=next(r for r in range(1,mod+1) if ((base-1)*r-2)%mod == 0)
            n=base**rr-2
            for a in range(mod):
                h=high_part_for_sum(base,a)
                k=rr+2
                pos = h*base**k+n
                triple=tuple(digit_sum(pos+i,base)%mod for i in range(3))
                assert triple[0] == triple[2]
                assert (triple[1]-triple[0])%mod == 1
                pos = h*base**k+(base**rr-1)
                triple=tuple(digit_sum(pos+i,base)%mod for i in range(3))
                assert triple[0] == triple[2]
                assert (triple[1]-triple[0])%mod == mod-1
                pal_witnesses += 2
        else:
            assert all(w[::-1] not in F2 for w in F2)
    f2_cases += 1

# Direct finite prefix tests check the independent digit-sum definition.
# They are not presented as exhaustive infinite-language enumerations.
finite_cases=0
for base,mod in product(range(2,9),range(1,10)):
    w=word(base,mod,36000)
    F={j:finite_factors(w,j) for j in range(1,7)}
    assert F[2].issubset(all_two_factors(base,mod))
    if mod == 1:
        assert all(reflection_count(F[j])==1 for j in range(1,7))
    elif mod == 2:
        assert all(w0[::-1] in F[j] for j in range(1,7) for w0 in F[j])
    else:
        g=gcd(base-1,mod)
        for u in F[3]:
            if u[::-1] in F[3]:
                assert u==u[::-1]
        for j in range(4,7):
            assert all(u[::-1] not in F[j] for u in F[j])
        if g>=3:
            assert all(u[::-1] not in F[2] for u in F[2])
    finite_cases+=1

# A genuine combinatorial case split on the three consecutive differences
# validates that none of the binary-base length-4 patterns reverses.
for mod in range(3,30):
    patterns=set()
    for v,w in product(range(mod),repeat=2):
        patterns.add((1,v,1))
        if v==0:
            patterns.add((v,1,w))
            patterns.add((w,1,v))
    for x in patterns:
        reflected=tuple(-t%mod for t in x[::-1])
        assert reflected not in patterns

print('VERIFY_OK',
      'symbolic_pairs=96',
      'finite_prefix_cases=63',
      'finite_prefix_length=36000',
      'finite_factor_lengths=1..6',
      'palindromic_witnesses='+str(pal_witnesses),
      'binary_difference_patterns_mod_3..29')
