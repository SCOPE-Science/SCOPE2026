"""Verify complete finite transposition paths for up-down permutations.
Run as: python3 verify_primary.py [certificate path].
"""
from itertools import permutations
from collections import Counter
from pathlib import Path
import struct,sys
EXPECTED={4:5,6:61,8:1385,10:50521}
blob=Path(sys.argv[1] if len(sys.argv)>1 else 'gray_paths_u16le.bin').read_bytes()
assert len(blob)==2*sum(EXPECTED.values())
off=0
for n,expected in EXPECTED.items():
    valid=[p for p in permutations(range(n)) if all((p[i]<p[i+1])==(i%2==0) for i in range(n-1))]
    assert len(valid)==expected
    inds=struct.unpack_from('<'+str(expected)+'H',blob,off)
    off+=2*expected
    assert len(set(inds))==expected and min(inds)==0 and max(inds)==expected-1
    for i,j in zip(inds,inds[1:]):
        a,b=valid[i],valid[j]
        dif=[k for k in range(n) if a[k]!=b[k]]
        assert len(dif)==2 and b[dif[0]]==a[dif[1]] and b[dif[1]]==a[dif[0]]
    evens=sum(sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))%2==0 for p in valid)
    assert evens==(expected+1)//2
    print('PRIMARY_PASS',n,'states',expected,'transitions',expected-1,'even',evens,'odd',expected-evens)
assert off==len(blob)
print('ALL_PATHS_VERIFIED')
