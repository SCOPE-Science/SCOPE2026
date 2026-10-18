#!/usr/bin/env python3
"""Independent checks for the alternating-expansion circular-BWT identity."""
from itertools import product
from random import Random


def expand(w, h):
    return ''.join(('01' if c == '0' else '10') * h for c in w)


def bwt_direct(s):
    n = len(s)
    starts = sorted(range(n), key=lambda i: s[i:] + s[:i])
    return ''.join(s[(i-1) % n] for i in starts)


def bwt_cyclic_doubling(s):
    n = len(s)
    ranks = [ord(c) for c in s]
    order = list(range(n))
    k = 1
    while k < n:
        order.sort(key=lambda i: (ranks[i], ranks[(i+k) % n]))
        nxt = [0] * n
        for a, b in zip(order, order[1:]):
            nxt[b] = nxt[a] + int((ranks[a], ranks[(a+k) % n]) !=
                                   (ranks[b], ranks[(b+k) % n]))
        ranks = nxt
        k *= 2
    return ''.join(s[(i-1) % n] for i in order)


def formula(w, h):
    n = len(w)
    if not (h >= 2 and len(set(w)) == 2):
        raise ValueError('requires both symbols and h >= 2')
    # Compute parent rotation order independently of expanded BWT.
    order = sorted(range(n), key=lambda i: w[i:] + w[:i])
    layers = {'0': {}, '1': {}}
    for i in order:
        c = w[i]
        d = 1
        while w[(i+d) % n] == c:
            d += 1
        last = '1' if w[(i-1) % n] == '0' else '0'
        layers[c].setdefault(d, []).append(last)
    a = '1' * (h * w.count('1'))
    for d in sorted(layers['0'], reverse=True):
        a += ''.join(layers['0'][d])
        a += '1' * ((h-1)*len(layers['0'][d]))
    for d in sorted(layers['1']):
        a += '0' * ((h-1)*len(layers['1'][d]))
        a += ''.join(layers['1'][d])
    return a + '0' * (h * w.count('0'))


def runs(s):
    return sum(a != b for a,b in zip(s,s[1:])) + 1


def test():
    cases=0
    for n in range(2,10):
        for tup in product('01',repeat=n):
            w=''.join(tup)
            if len(set(w)) != 2: continue
            reference = None
            for h in (2,3,4):
                observed = bwt_direct(expand(w,h))
                assert observed == formula(w,h), (w,h,observed,formula(w,h))
                r = runs(observed)
                if reference is None: reference=r
                else: assert reference==r,(w,h,reference,r)
                cases+=1
    # Independent suffix-doubling implementation, including length > 1000.
    rng=Random(728164)
    independent=0
    for n in (11,17,35,75,151,305):
        for _ in range(10):
            w=''.join(rng.choices('01',k=n))
            if len(set(w))!=2:continue
            v=[]
            for h in (2,3,5):
                image=expand(w,h)
                observed=bwt_cyclic_doubling(image)
                if len(image)<=500: assert observed==bwt_direct(image)
                assert observed==formula(w,h),(n,h)
                v.append(runs(observed))
                independent+=1
            assert len(set(v))==1,(w,v)
    # The threshold h=2 is genuinely necessary.
    w='001'
    assert runs(bwt_direct(expand(w,1)))==4
    assert runs(bwt_direct(expand(w,2)))==6
    print('VERIFY_OK exhaustive_two_symbol_inputs_n_2_to_9_cases=%d independent_suffix_doubling_cases=%d h1_sharp_counterexample=001'%(cases,independent))

if __name__=='__main__':test()
