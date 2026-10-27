#!/usr/bin/env python3
"""Reproduce exact binary scattered-01 threshold automaton calculations."""
from collections import defaultdict, deque
from itertools import product


def pairs01(word):
    zeros = pairs = 0
    for char in word:
        if char == '0':
            zeros += 1
        else:
            pairs += zeros
    return pairs


def profile(word):
    return word.count('0'), pairs01(word)


def name(k,z,p):
    if p >= k:
        return ('accept',)
    if z == 0:
        return ('initial',)
    if p + z >= k:
        return ('one',)
    d = k - p - z
    return ('small',d,z) if z < d else ('large',d)


def residual(k,z,p,suffix):
    u_ones=suffix.count('1')
    return p+z*u_ones+pairs01(suffix) >= k


def reachable_and_minimized(k):
    # Explicit bounded counters, independent of the predicted quotient.
    start=(0,0)
    all_states={start}
    queue=deque([start]); nxt={}
    while queue:
        z,p=queue.popleft()
        results=[]
        for c in '01':
            zz,pp=(min(k,z+1),p) if c=='0' else (z,min(k,p+z))
            if pp>=k: zz,pp=k,k
            pair=zz,pp
            results.append(pair)
            if pair not in all_states:
                queue.append(pair)
                all_states.add(pair)
        nxt[(z,p)] = tuple(results)
    groups=[{s for s in all_states if s[1]<k}, {s for s in all_states if s[1]>=k}]
    groups=[g for g in groups if g]
    while True:
        ind={s:i for i,g in enumerate(groups) for s in g}
        refine=[]
        for g in groups:
            buckets=defaultdict(set)
            for s in g:
                buckets[tuple(ind[t] for t in nxt[s])].add(s)
            refine.extend(buckets.values())
        if len(refine)==len(groups): break
        groups=refine
    return all_states, groups


def run():
    checked_states=0; checked_samples=0; checks=0
    for k in range(1,41):
        states, classes=reachable_and_minimized(k)
        expected=k*k//4+3
        assert len(classes)==expected,(k,len(classes),expected)
        # Independently compare each quotient name to exhaustive DFA minimization.
        indexed={s:i for i,g in enumerate(classes) for s in g}
        seen={}
        for z,p in states:
            label=name(k,z,p)
            if label in seen:
                assert indexed[(z,p)]==indexed[seen[label]],(k,z,p,label)
            seen[label]=(z,p)
        assert len(seen)==len(classes)
        checked_states+=len(states)
        checks+=1
    # Evaluate every short prefix/suffix directly, rather than relying on the quotient counter.
    words=[''.join(w) for length in range(10) for w in product('01',repeat=length)]
    suffixes=[''.join(w) for length in range(7) for w in product('01',repeat=length)]
    for k in range(1,13):
        for word in words:
            z,p=profile(word)
            label=name(k,z,p)
            for suffix in suffixes:
                direct = pairs01(word+suffix)>=k
                assert direct==residual(k,z,p,suffix),(k,word,suffix)
                checked_samples+=1
            # A short fixed representative for each label, built by z,p counts.
            if label==('accept',):
                representative='0'*k+'1'
            elif label==('initial',):
                representative=''
            else:
                representative='0'+'1'*p+'0'*(z-1)
            assert name(k,*profile(representative))==label
    print('VERIFY_OK minimized_thresholds=40 bounded_automaton_states=%d direct_prefix_suffix_tests=%d' % (checked_states,checked_samples))

if __name__=='__main__': run()
