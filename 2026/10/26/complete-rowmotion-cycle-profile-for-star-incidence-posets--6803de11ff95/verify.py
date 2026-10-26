"""Independent exhaustive check of rowmotion cycle types for star incidence posets.

For each n, enumerate all ideals as bitmasks of the 2n+1-element
incidence poset and compute rowmotion directly from minimal complementary
elements. Does not use the ternary-word transition used in the proof.
"""
from collections import Counter


def poset(n):
    # center 0; leaves 1..n; edges n+1..2n
    lower = [0]*(2*n+1)
    for i in range(n):
        lower[n+1+i] = (1<<0) | (1<<(1+i))
    return lower


def rowmotion(I, lower, full):
    notI = full ^ I
    minimum = 0
    for j, below in enumerate(lower):
        if notI & (1<<j) and not(below & notI):
            minimum |= 1<<j
    D = minimum
    for j, below in enumerate(lower):
        if minimum & (1<<j):
            D |= below
    return D


def cycle_profile(n):
    lower=poset(n)
    full=(1<<(2*n+1))-1
    ideals = {I for I in range(full+1) if all(not(I&(1<<j)) or (I & below)==below for j,below in enumerate(lower))}
    seen=set()
    counts=Counter()
    for I in ideals:
        if I in seen: continue
        cur=I
        orbit=[]
        while cur not in seen:
            assert cur in ideals, 'rowmotion not an ideal'
            seen.add(cur);orbit.append(cur)
            cur=rowmotion(cur,lower,full)
        assert cur==I, 'rowmotion is not a permutation'
        counts[len(orbit)]+=1
    assert len(seen)==len(ideals)==3**n+2**n
    expected=Counter({2:1,3:1+(3**n-3*2**n+3)//3,8:2**(n-1)-1})
    expected={k:v for k,v in expected.items() if v}
    assert dict(counts)==expected,(n,counts,expected)
    assert sum(k*v for k,v in counts.items()) == len(ideals)
    return len(ideals),dict(counts)

if __name__=='__main__':
    for n in range(1,9):
        total,cycles=cycle_profile(n)
        print(f'n={n} ideals={total} cycles={cycles}')
    print('ALL CHECKS PASSED')
