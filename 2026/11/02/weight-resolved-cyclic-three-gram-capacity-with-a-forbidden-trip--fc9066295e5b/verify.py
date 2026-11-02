#!/usr/bin/env python3
"""Exact checks for weight-refined cyclic binary three-gram spectra with 111 excluded.

Uses only the Python standard library. This is finite corroboration of the
mathematical proof, not certification for infinitely many lengths.
"""
from collections import defaultdict
from itertools import product


def formula(n, weight):
    if n < 1 or not 0 <= weight <= n:
        return 0
    if weight == 0:
        return 1
    return sum(
        max(0, min(weight-y, n-2*weight+y)) + int(n == 2*weight-y)
        for y in range(weight//2+1)
    )


def profile(word):
    n = len(word)
    counts = [0]*8
    for i in range(n):
        j = (word[i] << 2) | (word[(i+1)%n] << 1) | word[(i+2)%n]
        counts[j] += 1
    return tuple(counts)


def constructed(weight, y, x, b):
    """Produce a cyclic word with exactly y double-1 runs and x long 0 runs."""
    assert weight >= 1 and 0 <= y <= weight//2
    a = weight-2*y
    t = a+y
    assert 0 <= x <= t and b >= 0 and (x != 0 or b == 0)
    ones = [2]*y + [1]*a
    zeros = [2]*x + [1]*(t-x)
    if x:
        zeros[0] += b
    out = []
    for l1,l0 in zip(ones,zeros):
        out.extend([1]*l1)
        out.extend([0]*l0)
    return tuple(out)


def generating_function(max_length):
    """Independently truncate the bivariate rational generating function."""
    coeff = defaultdict(int)
    for n in range(1,max_length+1):
        coeff[n,0] = 1
    # U=1/((1-u z^2)(1-u^2 z^3)); V=1/((1-u z^3)(1-u^2 z^4)).
    # G(z,u)=z/(1-z)+(U-1)+z/(1-z)^2*(U-V).
    diff = defaultdict(int)
    for a in range(max_length+1):
        for y in range(max_length+1):
            w=a+2*y
            pa=2*a+3*y
            pb=3*a+4*y
            if pa<=max_length:
                diff[pa,w] += 1
                if pa>=1: coeff[pa,w] += 1  # U - 1
            if pb<=max_length:
                diff[pb,w] -= 1
    for (p,w), c in diff.items():
        if c:
            for n in range(p+1,max_length+1):
                coeff[n,w] += c*(n-p)
    return coeff


def verify():
    max_literal_n=16
    literal_words=0
    literal_profiles=0
    for n in range(1,max_literal_n+1):
        groups=defaultdict(set)
        for bits in product((0,1),repeat=n):
            prof=profile(bits)
            if prof[7]:
                continue
            literal_words += 1
            groups[sum(bits)].add(prof)
        for w in range(n+1):
            assert len(groups[w]) == formula(n,w), (n,w,len(groups[w]),formula(n,w))
        literal_profiles += sum(len(x) for x in groups.values())

    max_construct_n=70
    checked_profiles=0
    for n in range(1,max_construct_n+1):
        for weight in range(n+1):
            witness_profiles=set()
            if weight==0:
                witness_profiles.add(profile((0,)*n))
            else:
                for y in range(weight//2+1):
                    a=weight-2*y
                    t=a+y
                    if n == 2*weight-y:
                        candidate=constructed(weight,y,0,0)
                        assert len(candidate)==n
                        witness_profiles.add(profile(candidate))
                    for x in range(1, min(t,n-2*weight+y)+1):
                        b=n-2*weight+y-x
                        candidate=constructed(weight,y,x,b)
                        assert len(candidate)==n and sum(candidate)==weight
                        observed=profile(candidate)
                        assert observed == (b,x,a,y,x,t-x,y,0), (n,weight,y,x,b,observed)
                        witness_profiles.add(observed)
            assert len(witness_profiles)==formula(n,weight),(n,weight)
            checked_profiles += len(witness_profiles)

    gf=generating_function(max_construct_n)
    for n in range(1,max_construct_n+1):
        for w in range(n+1):
            assert gf[n,w]==formula(n,w),(n,w,gf[n,w],formula(n,w))
    # Saturation of constant-weight profile classes once n >= 3w (w>=2).
    for w in range(2,40):
        m=w//2
        plateau=(m+1)*w-m*(m+1)//2
        assert formula(3*w,w)==plateau
        assert formula(3*w-1,w)==plateau-1
        assert formula(4*w+7,w)==plateau
    print('VERIFY_OK',f'literal_max_n={max_literal_n}',
          f'literal_words={literal_words}',
          f'literal_profiles={literal_profiles}',
          f'constructive_max_n={max_construct_n}',
          f'constructed_distinct_profiles={checked_profiles}',
          'bivariate_gf_verified=True',
          'constant_weight_saturation_verified=True')


if __name__=='__main__':
    verify()
