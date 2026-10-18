"""Numerical corroboration for weighted orthogonal-disc Minkowski sums.

Uses direct support-function maximization on a simplex, an exhaustive finite
face-stationarity candidate enumeration, and deterministic random probing.
This is numerical corroboration, not a proof for all dimensions or weights.
"""
import itertools
import math
import random

rng = random.Random(20261014)


def support(weights, u):
    return sum(w * math.sqrt(max(0.0, 1.0 - t*t)) for w, t in zip(weights, u))


def formula(weights):
    n = len(weights)
    sorted_pairs = sorted(enumerate(weights), key=lambda p: p[1])
    ordered = [x[1] for x in sorted_pairs]
    for k in range(2, n+1):
        threshold = math.sqrt(sum(w*w for w in ordered[:k])/(k-1))
        if (ordered[k-1] < threshold + 1e-12 and
                (k == n or threshold <= ordered[k] + 1e-12)):
            s = [0.0]*n
            for index,w in sorted_pairs[:k]:
                s[index] = max(0.0, 1.0-(w/threshold)**2)
            radius = sum(ordered[k:])+math.sqrt((k-1)*sum(x*x for x in ordered[:k]))
            return radius, k, s, threshold
    raise AssertionError('No active set found')


def independent_candidates(weights):
    """Enumerate stationarity candidates on all simplex faces, including edges."""
    n = len(weights)
    candidates=[]
    for k in range(2,n+1):
        for subset in itertools.combinations(range(n),k):
            threshold = math.sqrt(sum(weights[i]**2 for i in subset)/(k-1))
            s=[0.0]*n
            for i in subset:
                s[i]=1-(weights[i]/threshold)**2
            if min(s[i] for i in subset) < -1e-10:
                continue
            u=[math.sqrt(max(0.0,si)) for si in s]
            candidates.append((support(weights,u), s))
    return max(candidates, key=lambda x:x[0])

cases=0
for n in range(3,9):
    for repeat in range(65):
        weights=[10**rng.uniform(-1,1) for _ in range(n)]
        if repeat==0: weights=[1.0]*n
        if repeat==1: weights=[1.0]*(n-1)+[math.sqrt(n-1)]
        R,k,s,lam = formula(weights)
        assert abs(sum(s)-1)<1e-9
        assert 2<=k<=n
        assert all(si>=-1e-12 for si in s)
        assert abs(R-support(weights,[math.sqrt(si) for si in s]))<1e-9
        independent_R,_=independent_candidates(weights)
        assert abs(R-independent_R)<1e-9*(1+R)
        r=sum(weights)-max(weights)
        assert R/r +1e-10>=math.sqrt(n/(n-1))
        for attempt in range(350):
            v=[rng.gauss(0,1) for _ in range(n)]
            norm=math.sqrt(sum(x*x for x in v))
            v=[x/norm for x in v]
            assert support(weights,v)<=R+1e-9
            assert support(weights,v)+1e-9>=r
        cases+=1
print('PASS:', cases, 'positive weight profiles (dimension 3 through 8),',cases*350,
      'random direct support evaluations plus face-stationarity comparison.')
for weights in [(1,1,1),(1,1,math.sqrt(2)),(1,1,2),(1,2,2),(1,2,math.sqrt(5)),(1,2,3)]:
    R,k,s,lam = formula(weights)
    print('tridisc',weights,'active',k,'R',round(R,12),'s',tuple(round(x,8) for x in s))
