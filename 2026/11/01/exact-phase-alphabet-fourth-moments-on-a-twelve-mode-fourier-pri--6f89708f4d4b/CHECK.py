#!/usr/bin/env python3
"""Exact exhaustive Fourier moment certificate for a 2 by 2 by 3 aperture.

Run with Python 3 standard library: python3 CHECK.py.
No floating-point arithmetic and no external dependencies are used.
"""
from collections import Counter
from itertools import product

S = list(product(range(2), range(2), range(3)))
WHERE = {s:i for i,s in enumerate(S)}
ANCHORS = [WHERE[s] for s in ((0,0,0),(1,0,0),(0,1,0),(0,0,1))]
FREE = [i for i in range(12) if i not in ANCHORS]
SUMS = {}
DIFFS = {}
for i,a in enumerate(S):
    for j,b in enumerate(S):
        SUMS.setdefault(tuple(x+y for x,y in zip(a,b)), []).append((i,j))
        DIFFS.setdefault(tuple(x-y for x,y in zip(a,b)), []).append((i,j))
SUMS = list(SUMS.values())
DIFFS = list(DIFFS.values())
assert len(SUMS) == len(DIFFS) == 45

# Exact quadratic integer representatives: zeta_6=e^(pi*i/3),
# |a+b*zeta_6|^2=a*a+a*b+b*b; zeta_4=i analogously.
Z6 = ((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
Z4 = ((1,0),(0,1),(-1,0),(0,-1))

def roots(q):
    if q==2: return ((1,0),(-1,0)), False
    if q==3: return (Z6[0],Z6[2],Z6[4]), True
    if q==4: return Z4, False
    if q==6: return Z6, True
    raise ValueError('unsupported alphabet')

def norm2(a,b,hexagonal):
    return a*a+a*b+b*b if hexagonal else a*a+b*b

def exact_moment(q, E, groups, diff=False):
    R, hexagonal = roots(q)
    total=0
    for pairs in groups:
        a=b=0
        for i,j in pairs:
            u,v=R[(E[i]-E[j] if diff else E[i]+E[j])%q]
            a+=u;b+=v
        total+=norm2(a,b,hexagonal)
    return total

def normalize(q,E):
    c0,cx,cy,cz=(E[i] for i in ANCHORS)
    return tuple((E[i]-c0-x*(cx-c0)-y*(cy-c0)-z*(cz-c0))%q
                 for i,(x,y,z) in enumerate(S))

def transform(q,E,swap,flips,conj):
    out=[]
    for x,y,z in S:
        if swap: x,y=y,x
        if flips[0]:x=1-x
        if flips[1]:y=1-y
        if flips[2]:z=2-z
        out.append(((-1 if conj else 1)*E[WHERE[(x,y,z)]])%q)
    return normalize(q,out)

# Representative strings are in lexicographic (i,j,k) ordering, k fastest.
# Orbit sizes refer to normalized representatives under all reflections, 
# the interchange of the two short axes, and conjugation.
EXPECTED={
  2: (220,228,27,[(4,'000001001101'),(8,'000001010011'),
                    (8,'000001010110'),(4,'000001011010'),
                    (1,'001001001110'),(2,'001001011100')]),
  3: (210,216,48,[(32,'000001012210'),(16,'000001021120')]),
  4: (188,196,6,[(4,'002002010232'),(2,'002010030022')]),
  6: (196,200,36,[(8,'002015045032'),(16,'002015052342'),
                    (4,'003003015342'),(4,'003003021354'),
                    (4,'003015045522')]),
}

def certify(q):
    expected_min,expected_second,expected_count,expected_orbits=EXPECTED[q]
    histogram=Counter(); winners=[]; minimum=10**9
    # Unique phase gauge: c_000=c_100=c_010=c_001=1. 
    # Exactly q^8 possibilities, each with q^4 distinct lifts.
    for d in product(range(q),repeat=len(FREE)):
        E=[0]*len(S)
        for idx,e in zip(FREE,d):E[idx]=e
        value=exact_moment(q,E,SUMS)
        histogram[value]+=1
        if value<minimum:
            minimum=value;winners=[]
        if value==minimum:winners.append(tuple(E))
    assert sum(histogram.values())==q**8
    assert minimum==expected_min, (q,minimum)
    assert sorted(histogram)[1]==expected_second, (q,sorted(histogram)[:2])
    assert len(winners)==expected_count, (q,len(winners))

    # All global minimum equality arrays: independently recompute via
    # difference autocorrelations (rather than square convolution).
    for E in winners:
        assert exact_moment(q,E,DIFFS,diff=True)==minimum
        assert normalize(q,E)==E
    # In addition, check exact correlation/convolution identity outside
    # the equality set along a deterministic exhaustive prefix and suffix.
    for d in list(product(range(q),repeat=3)):
        E=[0]*len(S)
        for idx,e in zip(FREE,d+(0,)*(len(FREE)-3)):E[idx]=e
        assert exact_moment(q,E,SUMS)==exact_moment(q,E,DIFFS,diff=True)
        E=[0]*len(S)
        for idx,e in zip(FREE,(q-1,)*(len(FREE)-3)+d):E[idx]=e
        assert exact_moment(q,E,SUMS)==exact_moment(q,E,DIFFS,diff=True)

    W=set(winners); orbits=[]
    while W:
        rep=min(W)
        orbit={transform(q,rep,swap,flips,conj)
               for swap in (False,True)
               for flips in product((False,True),repeat=3)
               for conj in (False,True)}
        assert orbit<=W, (q,rep,orbit-W)
        assert len(orbit)<=32
        orbits.append((len(orbit),''.join(map(str,min(orbit)))))
        W-=orbit
    assert sorted(orbits)==sorted(expected_orbits), (q,orbits)
    print('PASS q=%d searched=%d min=%d second=%d normalized=%d total=%d orbits=%d' %
          (q,q**8,minimum,expected_second,len(winners),len(winners)*q**4,len(orbits)),flush=True)
    return q**8

if __name__=='__main__':
    total=sum(certify(q) for q in (2,3,4,6))
    assert total==2**8+3**8+4**8+6**8==1751969
    print('CHECK_OK %d exact normalized arrays' % total,flush=True)
