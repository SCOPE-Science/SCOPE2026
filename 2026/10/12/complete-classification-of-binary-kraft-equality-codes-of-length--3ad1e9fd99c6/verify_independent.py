#!/usr/bin/env python3
"""Independent finite Sardinas-Patterson enumeration of Kraft-equality binary (3,4)-codes."""
from itertools import combinations
from collections import defaultdict
from math import comb

W3=tuple(format(i,'03b') for i in range(8))
W4=tuple(format(i,'04b') for i in range(16))

def test_ud(code):
    # Textbook Sardinas--Patterson sets, no bitmask-state automata.
    d={v[len(u):] for u in code for v in code if u!=v and v.startswith(u)}
    seen=set()
    while d:
        if any(x in code for x in d): return False
        key=frozenset(d)
        if key in seen: return True
        seen.add(key)
        nxt=set()
        for x in d:
            for w in code:
                if w.startswith(x):
                    t=w[len(x):]
                    if not t:return False
                    nxt.add(t)
                if x.startswith(w):
                    t=x[len(w):]
                    if not t:return False
                    nxt.add(t)
        d=nxt
    return True

def main():
    count=defaultdict(lambda:[0,0,0,0])
    examples=[]
    done=0
    for a in range(1,8):
        b=16-2*a
        for sh in combinations(range(8),a):
            ss=set(sh)
            short=frozenset(W3[i] for i in sh)
            prefix_B=tuple(i for i in range(16) if i//2 not in ss)
            suffix_B=tuple(i for i in range(16) if i%8 not in ss)
            for lg in combinations(range(16), b):
                done+=1
                pref=(lg==prefix_B)
                suff=(lg==suffix_B)
                if pref:count[a][0]+=1
                if suff:count[a][1]+=1
                if not pref and not suff:
                    code=short.union(W4[i] for i in lg)
                    if test_ud(code):
                        count[a][2]+=1
                        examples.append((sh,lg))
                count[a][3]+=1
    assert done == 1901636
    assert [sum(count[a][:3]) for a in range(1,8)] == [16,56,112,140,116,56,16]
    assert len(examples)==4
    print('complete', done)
    print('a,prefix,suffix,exception,total')
    for a in range(1,8):print(a,*count[a], 'UD',sum(count[a][:3]))
    print('EXCEPTIONS', len(examples));
    for sh,lg in examples:print(' '.join(W3[i] for i in sh), ' / ', ' '.join(W4[i] for i in lg))
if __name__=='__main__':main()
