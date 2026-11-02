#!/usr/bin/env python3
"""Exact affine-endpoint certificate for a family of greedy 2-sumfree sequences.

All arithmetic is integer arithmetic.  The finite family of affine endpoints,
not a finite sample of sequence parameters, controls the infinite assertion.
"""


def plus(x, y):
    return x[0] + y[0], x[1] + y[1]


def value(x, f):
    return x[0] * f + x[1]


def symbolic_intervals():
    # Each endpoint (a,b) means a*f+b; all intervals are inclusive.
    pre = [
        ((1, 0), (1, 0)),
        ((2, 4), (3, 3)),
        ((4, 4), (4, 8)),
        ((6, 6), (6, 7)),
        ((7, 12), (8, 8)),
        ((9, 11), (9, 15)),
    ]
    blocks = [
        ((11, 12), (11, 14)),
        ((12, 19), (13, 14)),
        ((14, 18), (14, 22)),
        ((16, 18), (16, 18)),
    ]
    mod = (5, 7)
    out = list(pre)
    for k in range(13):
        for j, (lo, hi) in enumerate(blocks):
            if j == 3 and k == 12:
                continue
            sh = (k * mod[0], k * mod[1])
            out.append((plus(lo, sh), plus(hi, sh)))
    assert len(out) == 57
    return out


def symbolic_distinct_sums(intervals):
    result = []
    for i, (lo, hi) in enumerate(intervals):
        if lo != hi:  # All nonsingleton widths >=2 for every f >=8.
            result.append(((2*lo[0], 2*lo[1]+1),
                           (2*hi[0], 2*hi[1]-1)))
        for lo2, hi2 in intervals[i+1:]:
            result.append((plus(lo, lo2), plus(hi, hi2)))
    return result


def merge(intervals, left, right):
    a = sorted((max(lo, left), min(hi, right))
               for lo, hi in intervals
               if max(lo, left) <= min(hi, right))
    result = []
    for lo, hi in a:
        if result and lo <= result[-1][1]+1:
            result[-1] = result[-1][0], max(result[-1][1], hi)
        else:
            result.append((lo, hi))
    return result


def intersect_nonempty(a, b):
    i = j = 0
    while i < len(a) and j < len(b):
        if max(a[i][0], b[j][0]) <= min(a[i][1], b[j][1]):
            return True
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return False


def finite_greedy_certificate(f, cand, sums):
    # The greedy sequence is initialized with f, 2f+4.  The requirement for
    # every later n is exactly: n belongs to candidate XOR to its 2-sumset.
    M = 5*f+7
    upper = 15*M
    lower = 2*f+5
    expanded = sorted((value(lo, f), value(hi, f)) for lo, hi in cand)
    assert expanded[0] == (f,f)
    assert expanded[1][0] == 2*f+4
    assert all(lo <= hi < upper+1 for lo,hi in expanded)
    assert all(expanded[i][1] < expanded[i+1][0]
               for i in range(len(expanded)-1))
    two_sums = [(value(lo,f), value(hi,f)) for lo,hi in sums]
    a = merge(expanded,lower,upper)
    b = merge(two_sums,lower,upper)
    assert not intersect_nonempty(a,b)
    assert merge(expanded+two_sums,lower,upper) == [(lower,upper)]
    return len(expanded), len(sums), len(b)


def endpoint_stability_certificate(cand, sums):
    # The truth of finite_greedy_certificate uses only ordering of affine
    # interval endpoints and adjacency, namely endpoint comparisons +/-1.
    endpoints = [p for interval in cand+sums for p in interval]
    endpoints += [(2,5),(75,105)]  # boundaries of [2f+5, 15(5f+7)]
    extreme = {}
    for slope, base in endpoints:
        for shift in (-1,0,1):
            x = base + shift
            if slope not in extreme:
                extreme[slope] = [x,x]
            else:
                extreme[slope][0] = min(extreme[slope][0], x)
                extreme[slope][1] = max(extreme[slope][1], x)
    # For slopes a<c, equality occurs at f=(b-d)/(c-a), and the largest
    # possible such f takes maximal b and minimal d.
    crossing_upper = (0,1)
    slopes = sorted(extreme)
    for i, a in enumerate(slopes):
        for c in slopes[i+1:]:
            numerator = extreme[a][1] - extreme[c][0]
            denominator = c-a
            if numerator * crossing_upper[1] > crossing_upper[0]*denominator:
                crossing_upper = numerator, denominator
    # Crossing upper <=14; all ordering and adjacency comparisons are
    # constant on integers f>=15.  A test at f=15 is then universal.
    assert crossing_upper[0] <= 14 * crossing_upper[1], crossing_upper
    return crossing_upper, len(endpoints)


def direct_greedy(f, count):
    g = 2*f+4
    terms = [f,g]
    forbidden = {f+g}
    v = g
    while len(terms) < count:
        v += 1
        while v in forbidden:
            v += 1
        for u in terms:
            forbidden.add(u+v)
        terms.append(v)
    return terms


def candidate_terms(f, count):
    M = 5*f+7
    C = symbolic_intervals()
    # Repeat symbolic tail sufficiently far for the independent small checks.
    q = [((11,12),(11,14)),((12,19),(13,14)),
         ((14,18),(14,22)),((16,18),(16,18))]
    for k in range(13, count+1):
        C += [(plus(lo,(k*5,k*7)),plus(hi,(k*5,k*7))) for lo,hi in q]
    result = []
    for lo,hi in sorted((value(x,f),value(y,f)) for x,y in C):
        result.extend(range(lo,hi+1))
        if len(result) >= count:
            break
    return result[:count]


def main():
    C = symbolic_intervals()
    S = symbolic_distinct_sums(C)
    upper, n_endpoints = endpoint_stability_certificate(C,S)
    info = []
    for f in range(8,16):
        info.append((f,finite_greedy_certificate(f,C,S)))
    # The source's four-block continuation theorem with block width 3M
    # extends the checked prefix to the infinite periodic candidate.
    # Full independent greedy calculation on a separate range corroborates.
    for f in range(8,41):
        assert direct_greedy(f,160) == candidate_terms(f,160),f
    print('VERIFY_OK affine_candidate_intervals=57 sum_intervals=%d'
          ' endpoint_expressions=%d crossing_upper=%d/%d'
          ' universal_f_ge_15=PASS finite_f=8..15=PASS'
          ' independent_greedy_f=8..40=PASS'
          ' uses_proved_four_block_continuation=YES' %
          (len(S),n_endpoints,upper[0],upper[1]))
    print('SMALL_PARAMETER_CERTIFICATES',info)


if __name__=='__main__':
    main()
