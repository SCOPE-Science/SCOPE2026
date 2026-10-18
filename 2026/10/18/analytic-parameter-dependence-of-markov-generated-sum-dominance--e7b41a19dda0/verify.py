#!/usr/bin/env python3
"""Finite checks for the local analytic fringe-probability theorem.
Only finite arithmetic and combinatorics are tested; analyticity follows from proof.
"""
from fractions import Fraction
from itertools import product


def path_probs(k, p, q):
    trans = ((p, 1-p), (1-q, q))
    stationary = ((1-q)/(2-p-q), (1-p)/(2-p-q))
    return [stationary[t[0]] * __import__('math').prod(
        trans[t[i]][t[i+1]] for i in range(k))
        for t in product((0,1), repeat=k+1)]


def score(bits_l, bits_r, k):
    L = tuple(i for i in range(k+1) if bits_l & (1 << i))
    R = tuple(i for i in range(k+1) if bits_r & (1 << i))
    sums_ll = {a+b for a in L for b in L}
    sums_rr = {a+b for a in R for b in R}
    sums_lr = {a+b for a in L for b in R}
    d = sum((int(j in sums_ll) + int(j in sums_rr) - 2*int(j in sums_lr))
            for j in range(k+1))
    return d, sums_ll, sums_rr, sums_lr


def fringe_probabilities(k,p,q):
    ws = path_probs(k,p,q)
    assert sum(ws) == 1
    bit_states = [sum(v << i for i,v in enumerate(t))
                  for t in product((0,1), repeat=k+1)]
    totals = [Fraction(0), Fraction(0), Fraction(0)]
    change_nonzero = 0
    for ix, left in enumerate(bit_states):
        for iy, right in enumerate(bit_states):
            d, LL, RR, LR = score(left,right,k)
            w = ws[ix]*ws[iy]
            totals[(0 if d>0 else 1 if d<0 else 2)] += w
            if k:
                previous = score(left & ((1<<k)-1), right & ((1<<k)-1), k-1)[0]
                if previous != d:
                    assert (k not in LL) or (k not in RR) or (k not in LR)
                    change_nonzero += 1
    assert sum(totals) == 1
    return tuple(totals), change_nonzero


def middle_lemma(k,n):
    count=0
    for mask in range(1<<(n+1)):
        a={i for i in range(n+1) if mask & (1<<i)}
        s={x+y for x in a for y in a}
        d={x-y for x in a for y in a}
        if all(t in s for t in range(k+1,2*n-k)) and all(t in d for t in range(k+1-n,n-k)):
            L=sum((1<<i) for i in a if i<=k)
            R=sum((1<<(n-i)) for i in a if i>=n-k)
            gap=score(L,R,k)[0]
            assert len(s)-len(d)==gap
            count+=1
    return count


def main():
    params=((Fraction(1,2),Fraction(1,2)),
            (Fraction(2,5),Fraction(3,5)),
            (Fraction(3,4),Fraction(2,3)))
    for p,q in params:
        for k in range(0,6):
            triple,changes=fringe_probabilities(k,p,q)
            print(f'p={p} q={q} K={k} rho_plus={triple[0]} rho_minus={triple[1]} rho_zero={triple[2]} changed_pairs={changes}')
    # A seventh fringe length (2^14 pairs) under the symmetric reference law.
    triple,changes=fringe_probabilities(6,Fraction(1,2),Fraction(1,2))
    print(f'p=1/2 q=1/2 K=6 triple={triple} changed_pairs={changes}')
    for n,k in ((8,2),(10,3),(12,4)):
        count=middle_lemma(k,n)
        print(f'n={n} K={k}: {count} full-middle configurations verified')
    print('PASS finite fringe identities; no numerical check is an infinite analyticity proof')

if __name__=='__main__':
    main()
