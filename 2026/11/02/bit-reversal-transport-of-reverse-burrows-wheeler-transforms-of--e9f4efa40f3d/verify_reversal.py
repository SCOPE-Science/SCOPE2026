#!/usr/bin/env python3
"""Exact binary de Bruijn reverse-BWT spectra, using two independent enumerators.

This program is public, self-contained and uses only the Python standard library.
Run: python3 verify_reversal.py.  It does not fetch external data.
"""
from collections import Counter

EXPECTED_DIFF = {-8: 4, -6: 44, -4: 216, -2: 436, 0: 648,
                  2: 436, 4: 216, 6: 44, 8: 4}
EXPECTED_JOINT = {
(20,22):4,(20,24):12,(20,26):20,(20,28):2,
(22,20):4,(22,22):102,(22,24):156,(22,26):140,(22,28):22,(22,30):2,
(24,20):12,(24,22):156,(24,24):366,(24,26):242,(24,28):62,(24,30):2,
(26,20):20,(26,22):140,(26,24):242,(26,26):170,(26,28):34,(26,30):2,
(28,20):2,(28,22):22,(28,24):62,(28,26):34,(28,28):10,
(30,22):2,(30,24):2,(30,26):2,
}

def reversal_bits(value, width):
    out = 0
    for _ in range(width):
        out = (out << 1) | (value & 1)
        value >>= 1
    return out

def word_from_feedback(order, mask):
    count = 1 << order
    state = 0
    seen = 0
    word = []
    for _ in range(count):
        if (seen >> state) & 1:
            return None
        seen |= 1 << state
        word.append(str(state >> (order-1)))
        suffix = state & ((count >> 1) - 1)
        next_bit = (state >> (order-1)) ^ ((mask >> suffix) & 1)
        state = ((state << 1) & (count - 1)) | next_bit
    if state != 0 or seen != (1 << count) - 1:
        return None
    return ''.join(word)

def bwt_direct(word):
    n = len(word)
    rotations = sorted(range(n), key=lambda i: word[i:] + word[:i])
    return ''.join(word[(i-1) % n] for i in rotations)

def bwt_symbolic(order, mask, reversed_word=False):
    half = 1 << (order-1)
    out = []
    for i in range(half):
        j = reversal_bits(i, order-1) if reversed_word else i
        bit = (mask >> j) & 1
        out.append(str(bit))
        out.append(str(1-bit))
    return ''.join(out)

def num_runs(w):
    return 1+sum(a != b for a,b in zip(w,w[1:]))

def mask_joint():
    order = 5
    result = Counter()
    words = set()
    for mask in range(1 << (1 << (order-1))):
        word = word_from_feedback(order,mask)
        if word is None:
            continue
        assert word.startswith('0'*order) and word not in words
        words.add(word)
        b1 = bwt_direct(word)
        b2 = bwt_direct(word[::-1])
        assert b1 == bwt_symbolic(order,mask)
        assert b2 == bwt_symbolic(order,mask,True)
        result[num_runs(b1),num_runs(b2)] += 1
    assert len(words)==2048
    return result,words

def euler_joint():
    # Edges of the order-four binary de Bruijn directed graph are labeled
    # by their unique five-bit factors (0..31). Root at edge 00000.
    order = 5
    m = 1 << (order-1)
    n = 1 << order
    edges = [0]
    words = set()
    joint = Counter()
    def dfs(vertex, seen):
        if len(edges)==n:
            if vertex == 0:
                w = ''.join(str(e >> (order-1)) for e in edges)
                assert w not in words
                words.add(w)
                joint[num_runs(bwt_direct(w)),num_runs(bwt_direct(w[::-1]))]+=1
            return
        for bit in (0,1):
            edge = 2*vertex+bit
            if not (seen >> edge) & 1:
                edges.append(edge)
                dfs(edge & (m-1),seen | (1<<edge))
                edges.pop()
    dfs(0,1)
    return joint,words

def verify_small_orders():
    for order in range(2,5):
        valid = 0
        for mask in range(1 << (1 << (order-1))):
            w = word_from_feedback(order,mask)
            if w is None: continue
            valid+=1
            assert bwt_direct(w) == bwt_symbolic(order,mask)
            assert bwt_direct(w[::-1])==bwt_symbolic(order,mask,True)
        assert valid == 1 << ((1 << (order-1))-order)

def main():
    verify_small_orders()
    a,awords=mask_joint()
    b,bwords=euler_joint()
    assert a == b == Counter(EXPECTED_JOINT), (a,b)
    assert awords==bwords
    assert len(a)==30
    assert sum(a.values())==2048
    diff=Counter({d:sum(v for (i,j),v in a.items() if j-i==d)
                  for d in EXPECTED_DIFF})
    assert diff==Counter(EXPECTED_DIFF)
    assert all(a[(i,j)]==a[(j,i)] for (i,j) in a)
    marginal1 = Counter()
    marginal2 = Counter()
    for (x,y),v in a.items():
        marginal1[x]+=v
        marginal2[y]+=v
    assert marginal1 == marginal2 == Counter({20:38,22:426,24:840,26:608,28:130,30:6})
    print('JOINT_TABLE',sorted((x,y,v) for (x,y),v in a.items()))
    print('DIFFERENCES',dict(sorted(diff.items())))
    print('NUMBER_OF_DE_BRUIJN_CYCLES',len(awords))
    print('MAX_ABSOLUTE_REVERSAL_DIFFERENCE',max(abs(d) for d in diff))
    print('NUMBER_AT_MAX_DIFFERENCE',diff[-8]+diff[8])
    print('VERIFY_OK')
if __name__=='__main__':
    main()
