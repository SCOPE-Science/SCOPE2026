#!/usr/bin/env python3
"""Check every optimum code and its four-element reversal/complement symmetry orbit."""
import sys
from collections import Counter
from itertools import combinations

path = sys.argv[1] if len(sys.argv)>1 else 'optimizers.txt'
with open(path,encoding='ascii') as stream:
    codes=[tuple(line.strip().split()) for line in stream if line.strip()]
assert len(codes)==4996 and len(set(codes))==4996


def reverse(code):
    return tuple(sorted(word[::-1] for word in code))


def complement(code):
    return tuple(sorted(''.join('1' if b=='0' else '0' for b in word) for word in code))

universe=set(codes)
seen=set()
orbits=Counter()
for code in codes:
    assert len(code)==13 and len(set(code))==13 and tuple(sorted(code))==code
    for word in code:
        assert len(word)==12 and word.count('1')==6
        assert all(word[:k]!=word[-k:] for k in range(1,12))
    smallest=12
    for a,b in combinations(code,2):
        distance=sum(x!=y for x,y in zip(a,b))
        smallest=min(smallest,distance)
        assert distance>=4
        assert all(a[:k]!=b[-k:] and b[:k]!=a[-k:] for k in range(1,12))
    assert smallest==4
    if code in seen:continue
    other=reverse(code)
    third=complement(code)
    fourth=complement(other)
    orbit={code,other,third,fourth}
    assert orbit<=universe
    seen.update(orbit)
    orbits[len(orbit)]+=1
assert seen==universe and orbits==Counter({4:1249}),orbits
print('validated_codes',len(codes),'orbits',dict(orbits),'distinct',len(seen))
