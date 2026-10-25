#!/usr/bin/env python3
"""Exhaustive verification of exact 3-state permutation-automaton word-class spectrum."""
from itertools import permutations, product

EXPECTED = (2,4,8,15,26,41,60,84,108,133,148,159,162,162,162,162,162,162)

def signature(word):
    zeros = ones = a = b = c = 0
    for j,bit in enumerate(word):
        if bit == 0:
            b += 1 if ones%2 == 0 else -1
            c += 1 if j%2 == 0 else -1
            zeros += 1
        else:
            a += 1 if zeros%2 == 0 else -1
            ones += 1
    return (zeros%6,a%3,b%3,c%3)

def advance(states,n):
    result=set()
    for z,a,b,c in states:
        result.add(((z+1)%6,a,(b+(1 if (n-z)%2==0 else -1))%3,(c+(1 if n%2==0 else -1))%3))
        result.add((z,(a+(1 if z%2==0 else -1))%3,b,c))
    return result

def group_fingerprint(word):
    ps = list(permutations(range(3)))
    unit=(0,1,2)
    outs=[]
    for p in ps:
        for q in ps:
            r=unit
            for v in word:
                s=p if v==0 else q
                r=tuple(s[r[i]] for i in range(3))
            outs.append(r)
    return tuple(outs)

def verify():
    st={(0,0,0,0)}
    for n in range(1,19):
        st=advance(st,n-1)
        assert len(st)==EXPECTED[n-1],(n,len(st))
        if n<=8:
            classes={}
            for w in product((0,1),repeat=n):
                sig=signature(w);fp=group_fingerprint(w)
                old=classes.setdefault(sig,fp)
                assert old==fp,('not sufficient',n,w)
            assert len(classes)==len(set(classes.values()))==len(st), ('not injective',n)
        if n>=13:
            assert st == {(z,a,b,c) for z in range(6) for a in range(3) for b in range(3) for c in range(3)},n
    print('EXACT_PROFILE',','.join(map(str,EXPECTED)))
    print('ALL_162_SIGNATURES_REALIZED_IN_EACH_LENGTH_13_THROUGH_18')
    print('DIRECT_GROUP_BEHAVIOR_MATCHES_SIGNATURES_THROUGH_LENGTH_8')
    print('VERIFY_OK')
if __name__=='__main__':verify()
