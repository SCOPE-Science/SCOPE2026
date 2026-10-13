#!/usr/bin/env python3
"""Independent enumeration of all binary three-dimensional linear subspaces."""
from itertools import combinations
from collections import Counter

expected={3:1,4:1,5:5,6:4,7:2}

def pw(x,n):
    full=(1<<n)-1
    x &= full
    return (x|(x>>1)|((x&1)<<(n-1))).bit_count()

for n,want in expected.items():
    spaces=set()
    for a,b,c in combinations(range(1,1<<n),3):
        vectors=frozenset((0,a,b,c,a^b,a^c,b^c,a^b^c))
        if len(vectors)!=8:continue
        spaces.add(vectors)
    fitting=[s for s in spaces if min(pw(x,n) for x in s if x)>=(n-1)]
    assert len(fitting)==want,(n,len(fitting))
    print(f'n={n}: 3D subspaces={len(spaces)} admissible={len(fitting)}')
print('VERIFY_OK: independent full 3D-subspace count.')
