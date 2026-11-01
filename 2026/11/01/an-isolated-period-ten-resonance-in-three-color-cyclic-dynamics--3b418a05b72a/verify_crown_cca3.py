#!/usr/bin/env python3
"""Finite exhaustive certificate for three-color cyclic dynamics on crown graphs.

Run: python3 verify_crown_cca3.py
Only Python's standard library is required.
"""
from collections import Counter
from itertools import product

COLORS = range(3)
TYPES = tuple(product(COLORS, repeat=2))
BASE = tuple(3**i for i in range(9))
TOTAL = 3**9


def unpack(s):
    return tuple(s // BASE[i] % 3 for i in range(9))


def pack(v):
    return sum(v[i] * BASE[i] for i in range(9))


def signature_step(v):
    """Exact 0/1/at-least-2 profile update and each type's local image."""
    left = [sum(v[3*a+b] for b in COLORS) for a in COLORS]
    right = [sum(v[3*a+b] for a in COLORS) for b in COLORS]
    new = [0] * 9
    image = [0] * 9
    for k, (a,b) in enumerate(TYPES):
        na = (a + int(right[(a+1)%3] > int(b == (a+1)%3)))%3
        nb = (b + int(left[(b+1)%3] > int(a == (b+1)%3)))%3
        dest = 3*na + nb
        image[k] = dest
        new[dest] = min(2, new[dest] + v[k])
    return pack(new), tuple(image)


def classify(s, sig_next, class_next):
    """Trace all initially nonempty ordered-pair color types."""
    v = unpack(s)
    trace = tuple(i for i in range(9) if v[i] != 0)
    now = s
    seen = {}
    step = 0
    while (now,trace) not in seen:
        assert step < 70
        seen[(now,trace)] = step
        trace = tuple(class_next[now][k] for k in trace)
        now = sig_next[now]
        step += 1
    return seen[(now,trace)], step - seen[(now,trace)]


def direct_step(colors, n):
    left, right = colors[:n], colors[n:]
    output = []
    for i in range(n):
        a=left[i]; nxt=(a+1)%3
        output.append(nxt if any(right[j]==nxt for j in range(n) if j!=i) else a)
    for i in range(n):
        b=right[i]; nxt=(b+1)%3
        output.append(nxt if any(left[j]==nxt for j in range(n) if j!=i) else b)
    return tuple(output)


def micro_check(n, info):
    """Independent literal vertex-neighbor simulation; full labelled enumeration."""
    maxima = 0
    counts = Counter()
    for x in product(COLORS, repeat=2*n):
        v = [0]*9
        for a,b in zip(x[:n],x[n:]):
            v[3*a+b] += 1
        s = pack(tuple(min(2,z) for z in v))
        predicted = info[s]
        assert sum(v)==n
        current=x;seen={};t=0
        while current not in seen:
            seen[current]=t
            current=direct_step(current,n)
            t+=1
            assert t<=70
        observed = (seen[current], t-seen[current])
        assert predicted==observed, (n,x,predicted,observed)
        counts[observed[1]] += 1
        maxima = max(maxima, observed[0])
    return dict(sorted(counts.items())), maxima


def main():
    # Exhaustive enumeration of the complete finite exact factor, not a sample.
    precomputed = [signature_step(unpack(s)) for s in range(TOTAL)]
    sig_next = [x[0] for x in precomputed]
    type_next = [x[1] for x in precomputed]
    info = [classify(s,sig_next,type_next) for s in range(TOTAL)]
    assert Counter(p for d,p in info)=={3:15711,4:3519,1:397,6:50,10:6}
    assert Counter(d for d,p in info)=={0:13317,1:5016,2:1146,3:174,4:30}
    rare6 = [s for s,(d,p) in enumerate(info) if p==6]
    rare10 = [s for s,(d,p) in enumerate(info) if p==10]
    assert len(rare6)==50 and len(rare10)==6
    assert all(sum(unpack(s))==3 and set(unpack(s))<={0,1} for s in rare6)
    assert all(sum(unpack(s))==5 and set(unpack(s))<={0,1} for s in rare10)
    assert sum(info[s][0]==0 for s in rare6)==20
    assert all(info[s][0]==0 for s in rare10)
    # Strictly recurrent labelled period-10 points: 6 unordered type sets * 5! assignments.
    period10_points = len(rare10) * 120
    assert period10_points == 720
    assert period10_points//10==72
    # Realizability and sharpness for all n (repeat any signature component of size 2).
    for p in (3,4):
        assert any(pp==p and 2 in unpack(s) and sum(unpack(s))<=4
                   for s,(d,pp) in enumerate(info))
    assert any(d==4 and 2 in unpack(s) and sum(unpack(s))<=5
               for s,(d,p) in enumerate(info))
    # Absence of the exceptional periods in all n except 3 and 5 follows
    # from the fact that their signatures contain no component equal to 2.
    # Independent explicit graph-edge simulation for n<=6.
    for n in range(1,7):
        counts,maxdepth = micro_check(n,info)
        print('n=',n,'total=',3**(2*n),'basin_period_counts=',counts,'max_entry=',maxdepth)
        assert maxdepth == (0 if n==1 else 1 if n==2 else 3 if n in (3,4) else 4)
        assert set(counts)==({1} if n<=2 else {1,3,6} if n==3 else {1,3,4,10} if n==5 else {1,3,4})
        if n==5:assert counts[10]==720
    print('FINITE_SIGNATURES=19683; RARE_PERIOD6=50; RARE_PERIOD10=6')
    print('CROWN_CCA3_VERIFY_OK')


if __name__=='__main__':main()
