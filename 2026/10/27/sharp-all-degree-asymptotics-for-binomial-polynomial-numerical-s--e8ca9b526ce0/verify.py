"""Exact finite cross-checks for binomial-polynomial numerical semigroups.

Stdlib only. The asymptotic theorem is proved symbolically, not by this script.
"""
from math import comb, gcd, factorial
from heapq import heappop, heappush


def generators(a, b, degree):
    # Stop once all later strictly increasing generators exceed a coarse
    # Apéry upper bound from the coprime pair (a, degree*a+b).
    bound = (a - 1) * (degree * a + b)
    seq = []
    i = 1
    while True:
        val = a * i + b * (comb(i, degree) if i >= degree else 0)
        if val > bound:
            break
        seq.append(val)
        i += 1
    return seq


def direct_apery(a, b, degree):
    gens = generators(a, b, degree)
    dist = [10**80] * a
    dist[0] = 0
    heap = [(0, 0)]
    while heap:
        val, r = heappop(heap)
        if val != dist[r]:
            continue
        for t in gens:
            residue = (r + t) % a
            if val + t < dist[residue]:
                dist[residue] = val + t
                heappush(heap, (val+t, residue))
    return dist


def min_costs(degree, maximum):
    vals = [comb(i, degree) for i in range(degree, maximum + degree + 2)
            if comb(i, degree) <= maximum]
    costs = [i for i in range(degree, maximum + degree + 2)
             if comb(i, degree) <= maximum]
    out = [0] + [10**80] * maximum
    for n in range(1, maximum+1):
        out[n] = min(out[n-v] + c for v, c in zip(vals, costs) if v <= n)
    return out


def ap_from_envelope(a, b, degree, costs):
    # Enough j's by a universal Apéry bound via generators (a, degree*a+b).
    bound = (a - 1) * (degree * a + b)
    out = []
    for r in range(a):
        rr = min((a*costs[r+j*a] + b*(r+j*a)
                  for j in range((bound-b*r)//(a*b)+1)), default=10**80)
        out.append(rr)
    return out


def check():
    cases = 0
    for degree in (2,3,4,5):
        for a in range(2, 51):
            for b in (1,2,3,5,7,11):
                if gcd(a,b)!=1:
                    continue
                direct = direct_apery(a,b,degree)
                bound = (a - 1) * (degree*a+b)
                maximum = bound//b + a
                costs = min_costs(degree,maximum)
                envelope = ap_from_envelope(a,b,degree,costs)
                assert sorted(direct) == sorted(envelope), (degree,a,b,'Ap mismatch')
                f = max(direct)-a
                # Exact integer genus identity: 2ag = 2sum Ap - a(a-1).
                gnum = 2*sum(direct)-a*(a-1)
                assert gnum % (2*a)==0
                genus = gnum//(2*a)
                assert f >= 0 and genus >= 0
                cases+=1
        print(f'degree {degree}: finite Apéry envelope matches independent Dijkstra, total cumulative cases {cases}')
    print('VERIFIED: all',cases,'independent finite comparisons; no extrapolation')


if __name__=='__main__':
    check()
