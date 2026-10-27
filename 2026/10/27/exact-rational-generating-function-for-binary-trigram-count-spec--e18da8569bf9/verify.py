#!/usr/bin/env python3
"""Exact arithmetic checks for the binary trigram-multiplicity enumerator.
Run with Python 3.9+; no external packages.
"""
from itertools import product

# H(z)=N(z)/Q(z), where z records the number of length-three windows.
N = [1, 5, -6, 5, -1, 6, 3, 1, -1, -2, 2]

def mult(a, b):
    v = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            v[i+j] += x*y
    return v

def denominator():
    q = [1]
    for v in [[1,-1]] * 5 + [[1,1],[1,0,1],[1,1,1]]:
        q = mult(q, v)
    return q


def coefficients(m):
    q = denominator()
    ans = []
    for t in range(m+1):
        a = (N[t] if t < len(N) else 0)
        a -= sum(q[j] * ans[t-j] for j in range(1, min(t, len(q)-1)+1))
        assert q[0] == 1
        ans.append(a)
    return ans

# Vertices are 00,01,10,11; coordinates of the non-loop edges are
# 001,010,011,100,101,110.  The endpoint imbalance is uniquely determined.
ENDPOINTS = {(0,0,0)}
for start in range(4):
    for end in range(4):
        if start != end:
            diff = [int(v == start) - int(v == end) for v in range(4)]
            ENDPOINTS.add((diff[0], diff[1], diff[3]))
assert len(ENDPOINTS) == 13


def flow_count(max_t):
    """Independent lattice-point enumeration with explicit loop allowances."""
    v = [0] * (max_t+1)
    for alpha,beta,delta in ENDPOINTS:
        E, D = max(0,-alpha), max(0,-delta)
        k, C = alpha+beta, 2*alpha+beta+delta
        for e in range(E, max_t+3):
            for f in range(max_t+3):
                for d in range(D, min(e+f+k,max_t+2)+1):
                    b,g,c = e+alpha,d+delta,e+f-d+k
                    if min(b,c,d,e,f,g) < 0:
                        continue
                    core = b+c+d+e+f+g
                    if core > max_t:
                        continue
                    if core == 0:
                        assert (alpha,beta,delta)==(0,0,0)
                        # One all-zero vector at t=0, two loop-only spectra
                        # (000... and 111...) at each positive t.
                        v[0] += 1
                        for t in range(1,max_t+1):v[t] += 2
                        continue
                    A = int(b+e>0)
                    Z = int(d+g>0)
                    for t in range(core,max_t+1):
                        if A and Z: v[t] += t-core+1
                        elif A or Z: v[t] += 1
                        elif t==core: v[t] += 1
    return v


def direct_words(n):
    spectra = set()
    for w in product((0,1), repeat=n):
        row = [0]*8
        for i in range(n-2):
            row[4*w[i]+2*w[i+1]+w[i+2]] += 1
        spectra.add(tuple(row))
    return len(spectra)

if __name__ == '__main__':
    q=denominator()
    assert len(q)==11, (len(q),q)
    calc=coefficients(55)
    by_flow=flow_count(30)
    assert calc[:31]==by_flow, [(i,a,b) for i,(a,b) in enumerate(zip(calc,by_flow)) if a!=b]
    print('FLOW_VS_RATIONAL_OK',len(by_flow))
    for n in range(3,18):
        val=direct_words(n)
        assert val==calc[n-2], (n,val,calc[n-2])
    print('WORD_ENUM_VS_RATIONAL_OK',15)
    print('FIRST',calc[:21])
    print('DENOM',q)
    print('VERIFY_OK')
