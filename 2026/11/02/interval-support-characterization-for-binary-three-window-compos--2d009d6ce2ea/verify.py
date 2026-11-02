#!/usr/bin/env python3
"""Self-contained exact checks for binary length-three window-composition spectra."""
from itertools import product
from math import comb


def histogram(bits, width):
    h = [0] * (width + 1)
    for i in range(len(bits) - width + 1):
        h[sum(bits[i:i+width])] += 1
    return tuple(h)


def construct_three(profile):
    p = list(profile)
    positions = [i for i,x in enumerate(p) if x]
    assert positions and positions == list(range(positions[0],positions[-1]+1))
    if len(positions) == 1:
        j = positions[0]
        period = ('0' * (3 - j) + '1' * j)
        return (period * (p[j] + 2))[:p[j] + 2]
    if positions[0] >= 2 or positions == [1,2,3]:
        complement = tuple(reversed(p))
        return ''.join('1' if b=='0' else '0' for b in construct_three(complement))
    if positions == [0,1]:
        word = '0' * (p[0]-1) + '0001'
        for t in range(p[1]-1):
            word += '001'[t%3]
        return word
    if positions == [1,2]:
        word = '0011'
        for t in range(p[1]-1):word = '100'[t%3] + word
        for t in range(p[2]-1):word += '011'[t%3]
        return word
    if positions == [0,1,2]:
        word = '0'*(p[0]-1) + '00011'
        for t in range(p[1]-1):word = '100'[t%3] + word
        for t in range(p[2]-1):word += '011'[t%3]
        return word
    if positions == [0,1,2,3]:
        word = '0'*(p[0]-1) + '000111' + '1'*(p[3]-1)
        for t in range(p[1]-1):word = '100'[t%3] + word
        for t in range(p[2]-1):word += '011'[t%3]
        return word
    raise AssertionError('unsupported interval')


def interval(p):
    s = [i for i,x in enumerate(p) if x]
    return s == list(range(s[0],s[-1]+1))


def parts(m, r):
    if r == 1:
        yield (m,)
    else:
        for head in range(1,m-r+2):
            for tail in parts(m-head,r-1):
                yield (head,) + tail


cases = 0
for m in range(1,29):
    for r in range(1,min(4,m)+1):
        for start in range(5-r):
            for ps in parts(m,r):
                p = (0,)*start+ps+(0,)*(4-start-r)
                w = construct_three(p)
                assert len(w)==m+2, (p,w,len(w))
                assert histogram(tuple(map(int,w)),3)==p, (p,w)
                cases += 1

# Independent exact dynamic-programming state traversal, without using the witnesses.
states = {(a,b,(0,0,0,0)) for a,b in product((0,1),repeat=2)}
dp_profiles=0
for m in range(1,41):
    next_states = set()
    for a,b,p in states:
        for c in (0,1):
            v=list(p);v[a+b+c]+=1
            next_states.add((b,c,tuple(v)))
    states = next_states
    observed={p for a,b,p in states}
    predicted=(m**3+11*m+12)//6
    assert len(observed)==predicted, (m,len(observed),predicted)
    assert all(interval(p) for p in observed)
    dp_profiles+=len(observed)

# Independent literal enumeration for all short words.
literal_words=0
for n in range(3,17):
    all_p=set()
    for bits in product((0,1),repeat=n):
        all_p.add(histogram(bits,3));literal_words+=1
    m=n-2
    assert len(all_p)==(m**3+11*m+12)//6
    assert all(interval(p) for p in all_p)

# Sharp failure at width 4 and general extremal one-duplicate lemma.
boundary_cases=0
for width in range(3,9):
    extras=set()
    for bits in product((0,1),repeat=2*width+1):
        v=histogram(bits,width)
        if all(x>0 for x in v):
            assert sum(x-1 for x in v)==1
            extras.add(v.index(2))
        boundary_cases+=1
    predicted=set(range(width+1)) if width==3 else {0,1,width-1,width}
    assert extras==predicted,(width,extras,predicted)

print('VERIFY_OK', 'constructive_histograms='+str(cases), 'DP_degrees=1..40',
      'DP_distinct_profiles='+str(dp_profiles), 'literal_words='+str(literal_words),
      'boundary_binary_words='+str(boundary_cases), 'windows=3..8')
