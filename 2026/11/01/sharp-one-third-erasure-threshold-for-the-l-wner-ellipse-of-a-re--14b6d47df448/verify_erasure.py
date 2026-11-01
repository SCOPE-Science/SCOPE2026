#!/usr/bin/env python3
"""Numerical reproduction of the moment certificates.

Pure Python 3 standard library; run: python verify_erasure.py
These finite tests are diagnostics, NOT a proof for all polygon orders.
"""
import math


def weights_after_deletion(n, k):
    if not (n >= 6 and 1 <= k <= n - 3 and 3 * (k + 1) <= n):
        raise ValueError('Must have n>=6 and 1<=k<=floor(n/3)-1')
    surviving = list(range(k, n))
    partner = lambda j: (k-1-j) % n
    orbits = []
    unseen = set(surviving)
    for j in surviving:
        if j not in unseen:
            continue
        p = partner(j)
        assert p in unseen
        inds = sorted(set((j,p)))
        unseen.difference_update(inds)
        phi = math.pi * (k-1) / n
        c = math.cos(2*math.pi*j/n - phi)
        orbits.append((c, inds))
    assert not unseen
    lo = min(range(len(orbits)), key=lambda i: orbits[i][0])
    hi = max(range(len(orbits)), key=lambda i: orbits[i][0])
    cmin = orbits[lo][0]
    cmax = orbits[hi][0]
    assert cmin < 0 < cmax
    # Maximal E(c^2) subject to E(c)=0 uses the two endpoints.
    extreme = {lo: cmax/(cmax-cmin), hi: -cmin/(cmax-cmin)}
    vmax = -cmin*cmax
    closest_zero = min(range(len(orbits)), key=lambda i: abs(orbits[i][0]))
    if abs(orbits[closest_zero][0]) < 1e-13:
        middle = {closest_zero: 1.0}
        vmin = 0.0
    else:
        lower = max((i for i in range(len(orbits)) if orbits[i][0] < 0),
                    key=lambda i: orbits[i][0])
        upper = min((i for i in range(len(orbits)) if orbits[i][0] > 0),
                    key=lambda i: orbits[i][0])
        a,b = orbits[lower][0], orbits[upper][0]
        middle = {lower: b/(b-a), upper: -a/(b-a)}
        vmin = -a*b
    assert vmax >= 0.5 - 2e-12, (n,k,vmax)
    assert vmin < 0.5
    t = (0.5-vmin)/(vmax-vmin)
    assert -1e-10 <= t <= 1+1e-10, (n,k,t)
    masses = {i: t*extreme.get(i,0) + (1-t)*middle.get(i,0)
              for i in range(len(orbits))}
    weights = {}
    for i,(c,inds) in enumerate(orbits):
        for j in inds:
            weights[j] = masses[i]/len(inds)
    return weights


def checks():
    total=0
    positives=0
    for n in range(6,351):
        max_k = (n // 3) - 1
        for k in range(1,n-2):
            total += 1
            # Direct angular obstruction is computed independently of the integer rule.
            B = 1.0 if (n+k) % 2 else math.cos(math.pi/n)
            C = math.cos(math.pi*(k+1)/n)
            formula = B*C >= 0.5 - 1e-12
            assert formula == (k <= max_k), (n,k,B*C,max_k)
            if not formula:
                continue
            positives += 1
            w = weights_after_deletion(n,k)
            assert len(w) <= n-k
            assert min(w.values()) >= -1e-12
            assert abs(sum(w.values())-1)<1e-10
            for h in (1,2):
                s = sum(v * complex(math.cos(h*2*math.pi*j/n),
                                    math.sin(h*2*math.pi*j/n))
                        for j,v in w.items())
                assert abs(s) < 1e-10, (n,k,h,s)
    print('PASS:',total,'parameter pairs;',positives,'explicit isotropic certificates')
    print('PASS: all angular-obstruction thresholds agree with k_max=floor(n/3)-1')

if __name__=='__main__':
    checks()
