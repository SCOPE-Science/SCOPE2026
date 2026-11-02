#!/usr/bin/env python3
"""Independent finite verification for maximal independent sets in P_l x K_q.

Only the Python standard library is required. These finite checks do not
replace the all-parameter structural proof or the analytic limit argument.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb, sqrt, log, exp


def brute_graph_polynomial(length, colors):
    """Check independence and domination in the original graph by bitmasks."""
    vcount = length * colors
    edges = []
    for i in range(length):
        for c in range(colors):
            nb = 0
            for j in (i-1, i+1):
                if 0 <= j < length:
                    for d in range(colors):
                        if c != d:
                            nb |= 1 << (j * colors + d)
            edges.append(nb)
    full = (1 << vcount) - 1
    result = Counter()
    for mask in range(1 << vcount):
        uncovered = full ^ mask
        remaining = mask
        valid = True
        while remaining:
            bit = remaining & -remaining
            remaining ^= bit
            idx = bit.bit_length() - 1
            if mask & edges[idx]:
                valid = False
                break
            uncovered &= ~edges[idx]
        if valid and uncovered == 0:
            result[mask.bit_count()] += 1
    return result


def fiber_polynomial(length, colors):
    """Check each fiber against the local selection and domination predicate."""
    result = Counter()
    full_symbol = colors + 1
    for word in product(range(colors+2), repeat=length):
        valid = True
        for i, state in enumerate(word):
            nbrs = []
            if i: nbrs.append(word[i-1])
            if i+1 < length: nbrs.append(word[i+1])
            if state == full_symbol:
                valid = all(nbr == 0 for nbr in nbrs)
            elif state:
                valid = all(nbr in (0, state) for nbr in nbrs) and state in nbrs
            else:
                valid = (full_symbol in nbrs or
                         len({nbr for nbr in nbrs if 1 <= nbr <= colors}) >= 2)
            if not valid: break
        if valid:
            weight = sum(colors if s == full_symbol else (s != 0) for s in word)
            result[weight] += 1
    return result


def transfer_polynomial(length, colors):
    """Count via full-fiber nodes and colored runs, using no graph predicate."""
    # State F=0, C=1. A colored run's actual color is summed in its factor.
    counts = defaultdict(int)
    if length >= 1:
        counts[(1, colors, 0)] += 1
    if length >= 2:
        counts[(2, colors, 0)] += 1  # optional leading empty fiber
    for r in range(2, length+1):
        counts[(r, r, 1)] += colors
    for size in range(1, length+1):
        layer = [(w, typ, v) for (n, w, typ), v in list(counts.items()) if n == size]
        for weight, typ, ways in layer:
            # Append an entire full fiber.
            for gap in ((1, 2) if typ == 0 else (1,)):
                newsize = size + gap + 1
                if newsize <= length:
                    counts[(newsize, weight+colors, 0)] += ways
            # Append a monochromatic run of length at least two.
            factor = colors if typ == 0 else colors-1
            for r in range(2, length-size):
                newsize = size+1+r
                counts[(newsize, weight+r, 1)] += factor*ways
    result = Counter()
    for (n,w,typ),v in counts.items():
        if n == length: result[w] += v
        if n == length-1 and typ == 0: result[w] += v  # trailing empty fiber
    return +result


def minimum_count(length, colors):
    if length == 1: return colors, 1
    if length == 2: return 2, colors
    k = (length+1)//3
    patterns = {2:1, 0:k, 1:comb(k+1, 2)}[length % 3]
    number = colors * (colors-1)**(k-1) * patterns
    if length == 3 and colors == 3: number += 1
    return (2*(length+1)+2)//3, number


def dominant_radius(colors, bias=1.):
    """Bisection using Perron root of the 2x2 positive node transition."""
    def rho(t):
        a = t*bias**colors
        b = (t*bias)**2 / (1-t*bias)
        aa = (t+t*t)*a
        bb = t*colors*b
        cc = t*a
        dd = t*(colors-1)*b
        return (aa+dd+sqrt((aa-dd)**2+4*bb*cc))/2
    low, high = 0., 0.999/bias
    for _ in range(100):
        mid=(low+high)/2
        if rho(mid)<1: low=mid
        else: high=mid
    return (low+high)/2


def moments(colors):
    h = 1.e-4
    r0 = dominant_radius(colors)
    def psi(s): return log(r0/dominant_radius(colors, exp(s)))
    m = (psi(-2*h)-8*psi(-h)+8*psi(h)-psi(2*h))/(12*h)
    v = (-psi(2*h)+16*psi(h)-30*psi(0)+16*psi(-h)-psi(-2*h))/(12*h*h)
    return r0,m,v


def main():
    cases = [(n,3) for n in range(2,8)] + [(n,4) for n in range(2,6)] + [(n,5) for n in range(2,5)]
    checked_masks=0
    for n,q in cases:
        fiber = fiber_polynomial(n,q)
        transfer = transfer_polynomial(n,q)
        assert fiber == transfer, (n,q,fiber,transfer)
        if n*q <= 18:
            direct = brute_graph_polynomial(n,q)
            checked_masks += (1 << (n*q))
            assert direct == fiber, (n,q,direct,fiber)
        mm = min(fiber)
        assert (mm,fiber[mm]) == minimum_count(n,q)
        print('PASS',n,q,dict(sorted(fiber.items())))
    assert sum(fiber_polynomial(3,3).values()) == 5
    for q,intervals in [(3,((.52099,.52102),(.927,.930),(.198,.204))),
                        (4,((.48646,.48650),(.989,.992),(.540,.548))),
                        (5,((.46028,.46032),(1.033,1.038),(.976,.990)))]:
        r,m,v=moments(q)
        assert all(lo < x < hi for x,(lo,hi) in zip((r,m,v),intervals))
        print('PER-RUN ASYMPTOTIC',q,'r=',r,'mu=',m,'sigma2=',v)
    print('VERIFIED cases=',len(cases),'directly examined masks=',checked_masks)

if __name__=='__main__':
    main()
