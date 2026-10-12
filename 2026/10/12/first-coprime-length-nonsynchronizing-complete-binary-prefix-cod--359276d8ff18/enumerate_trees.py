#!/usr/bin/env python3
"""Exhaustive synchronization census for binary full prefix trees (Python standard library)."""
from functools import lru_cache
from math import gcd
from collections import Counter, deque
import json

@lru_cache(None)
def ordered_full_trees(leaves):
    if leaves == 1:
        return (None,)
    return tuple((left, right)
                 for i in range(1, leaves)
                 for left in ordered_full_trees(i)
                 for right in ordered_full_trees(leaves-i))

def codewords(tree, prefix=''):
    if tree is None:
        return (prefix,)
    return codewords(tree[0], prefix+'0') + codewords(tree[1], prefix+'1')

def decoder(tree):
    if tree is None:
        raise ValueError('The empty codeword is excluded')
    nodes=[('', tree)]
    for prefix, sub in nodes:
        assert sub is not None
        for bit, child in zip('01', sub):
            if child is not None:
                nodes.append((prefix+bit, child))
    states=[prefix for prefix, _ in nodes]
    indexes={s:i for i,s in enumerate(states)}
    steps=[]
    leaf_set=set(codewords(tree))
    for bit in '01':
        steps.append(tuple(indexes['' if s+bit in leaf_set else s+bit] for s in states))
    return states,tuple(steps)

def has_reset(steps):
    count=len(steps[0])
    initial=(1<<count)-1
    queue=deque((initial,)); seen={initial}
    while queue:
        current=queue.popleft()
        if current & (current-1)==0: return True
        for row in steps:
            following=0
            bits=current
            while bits:
                low=bits & -bits
                bits-=low
                following |= 1<<row[low.bit_length()-1]
            if following not in seen:
                seen.add(following);queue.append(following)
    return False

def main():
    counts=[]; exceptions=[]
    for size in range(2,10):
        kinds=Counter()
        for tree in ordered_full_trees(size):
            code=codewords(tree)
            length_gcd=0
            for word in code:
                length_gcd=gcd(length_gcd,len(word))
            sync=has_reset(decoder(tree)[1])
            kinds['total']+=1
            if not sync:
                kinds['non_synchronizing']+=1
                if length_gcd==1:
                    kinds['non_synchronizing_coprime']+=1
                    exceptions.append(list(code))
        counts.append(dict(size=size,total=kinds['total'],nonsynchronizing=kinds['non_synchronizing'],nonsynchronizing_coprime=kinds['non_synchronizing_coprime']))
    result={'counts':counts,'nine_word_exceptions':sorted(exceptions)}
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
