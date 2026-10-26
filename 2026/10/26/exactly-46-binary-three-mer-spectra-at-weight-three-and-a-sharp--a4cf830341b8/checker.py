"""Reproduce finite certificates for binary three-mer spectra at weight three.

All arithmetic is exact. The theorem for unbounded lengths uses the
symbolic gap formulas and a finite exhaustive set of 3^4 signatures,
not extrapolation from finite word samples.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb
import csv
import os


def signature(gaps):
    return tuple(min(x, 2) for x in gaps)


def fingerprint(t):
    a, b, c, d = t
    return (
        int(a >= 2) + int(b >= 2) + int(c >= 2),           # 001
        int(a > 0 and b > 0) + int(b > 0 and c > 0) + int(c > 0 and d > 0),  # 010
        int(b == 0 and a > 0) + int(c == 0 and b > 0),       # 011
        int(b == 1) + int(c == 1),                            # 101
        int(b == 0 and c > 0) + int(c == 0 and d > 0),       # 110
        int(b >= 2) + int(c >= 2) + int(d >= 2),           # 100
        int(b == 0 and c == 0),                              # 111
    )


def direct_profile(gaps):
    a, b, c, d = gaps
    s = '0' * a + '1' + '0' * b + '1' + '0' * c + '1' + '0' * d
    return tuple(sum(s[i:i+3] == t for i in range(len(s)-2))
                 for t in ('001', '010', '011', '101', '110', '100', '111'))


def groups():
    out = defaultdict(list)
    for t in product(range(3), repeat=4):
        out[fingerprint(t)].append(t)
    return dict(out)


def fiber_count(ts, N):
    answer = 0
    for t in ts:
        r, m = t.count(2), sum(t)
        if N < m:
            continue
        if r == 0:
            answer += int(N == m)
        else:
            answer += comb(N-m+r-1, r-1)
    return answer


def main():
    buckets = groups()
    assert len(buckets) == 59
    assert sum(len(ts) for ts in buckets.values()) == 81
    permanent = {p:ts for p,ts in buckets.items() if any(2 in t for t in ts)}
    transient = {p:ts for p,ts in buckets.items() if not any(2 in t for t in ts)}
    assert len(permanent) == 46 and len(transient) == 13
    assert Counter(min(sum(t) for t in ts if 2 in t) for ts in permanent.values()) == {
        2:4,3:10,4:12,5:9,6:7,7:3,8:1}
    assert Counter(sum(ts[0]) for ts in transient.values()) == {0:1,1:4,2:5,3:2,4:1}
    assert all(len({sum(t) for t in ts}) == 1 for ts in transient.values())

    # Exhaust all gap signatures and many genuine words, using an
    # independently specified direct substring-count definition.
    for gaps in product(range(7), repeat=4):
        assert direct_profile(gaps) == fingerprint(signature(gaps))
    initial = (1, 4, 9, 16, 27, 35, 42, 45)
    for N in range(0, 40):
        count = sum(fiber_count(ts, N) > 0 for ts in buckets.values())
        assert count == (initial[N] if N < len(initial) else 46)
        if N <= 25:
            observed = defaultdict(int)
            for a in range(N+1):
                for b in range(N-a+1):
                    for c in range(N-a-b+1):
                        d = N-a-b-c
                        observed[direct_profile((a,b,c,d))] += 1
            calculated = {p:fiber_count(ts,N) for p,ts in buckets.items()
                          if fiber_count(ts,N) > 0}
            assert dict(observed) == calculated

    main_f = fingerprint((2,2,2,2))
    assert buckets[main_f] == [(2,2,2,2)]
    rivals = [ts for p,ts in permanent.items() if p != main_f]
    assert len(rivals) == 45
    bounds = [10, 23, 8, 1]
    diffs_by_rival = []
    for ts in rivals:
        vals = [comb(N-5,3)-fiber_count(ts,N) for N in range(15,19)]
        diffs = []
        while vals:
            diffs.append(vals[0]); vals = [y-x for x,y in zip(vals, vals[1:])]
        diffs_by_rival.append(diffs)
    assert [min(v[i] for v in diffs_by_rival) for i in range(4)] == bounds
    # Each difference is a cubic for N >= 15 and its Newton differences
    # at N=15 are strictly positive; all future differences are positive.
    assert all(all(x > 0 for x in v) for v in diffs_by_rival)
    assert max(fiber_count(ts, 14) for ts in buckets.values()) == 90
    assert comb(14-5,3) == 84
    for N in range(15, 80):
        counts = [(p,fiber_count(ts,N)) for p,ts in buckets.items()]
        assert max(v for p,v in counts) == comb(N-5,3)
        assert [p for p,v in counts if v == comb(N-5,3)] == [main_f]

    # Certificate A is a complete finite table of the 81 truncated-gap states.
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, 'signature_certificate.csv'),'w',newline='',encoding='utf-8') as fp:
        writer=csv.writer(fp)
        writer.writerow(['a','b','c','d','001','010','011','101','110','100','111','minimal_zeros'])
        for t in product(range(3),repeat=4):
            writer.writerow([*t,*fingerprint(t),sum(t)])

    # Certificate B groups equal fingerprints and lists the exact
    # finite-difference data used in the all-length extremal proof.
    with open(os.path.join(here, 'profile_certificate.csv'),'w',newline='',encoding='utf-8') as fp:
        writer=csv.writer(fp)
        writer.writerow(['fingerprint_001_010_011_101_110_100_111',
                         'truncated_gap_signatures','persistent','threshold_N',
                         'fiber_N15','difference_0','difference_1','difference_2','difference_3'])
        for p,ts in sorted(buckets.items()):
            live=any(2 in t for t in ts)
            threshold=min(sum(t) for t in ts if 2 in t) if live else sum(ts[0])
            if p==main_f:
                diffs=['MAIN']*4
            elif not live:
                diffs=['TRANSIENT']*4
            else:
                vals=[comb(N-5,3)-fiber_count(ts,N) for N in range(15,19)]
                diffs=[]
                while vals:
                    diffs.append(vals[0]);vals=[y-x for x,y in zip(vals,vals[1:])]
            writer.writerow(['.'.join(map(str,p)), ';'.join(''.join(map(str,t)) for t in ts),
                             int(live),threshold,fiber_count(ts,15),*diffs])
    print('PASS: 81 signatures, 59 fingerprints, 46 persistent, 13 transient')
    print('PASS: exhaustive direct substring checks for all gap quadruples in [0,6]^4')
    print('PASS: independently enumerated words through length 28')
    print('PASS: exact finite-difference certificate; unique maximum for n>=18')
    print('PASS: sharp cutoff: n=17 has maximum 90 versus deep-gap fiber 84')

if __name__=='__main__':
    main()
