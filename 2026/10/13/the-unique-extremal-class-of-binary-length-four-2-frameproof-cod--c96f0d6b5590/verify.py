from itertools import combinations, permutations
from collections import Counter
import hashlib
V=range(16)
def bits(x): return tuple((x>>i)&1 for i in range(4))
def framed(x,y,z):
    bx,by,bz=bits(x),bits(y),bits(z)
    return all(bx[i] in (by[i],bz[i]) for i in range(4))
def fp(C):
    S=set(C)
    for y,z in combinations(C,2):
        for x in S-{y,z}:
            if framed(x,y,z): return False
    return True
valid=[]
for mask in range(1<<16):
    if mask.bit_count()<5: continue
    C=tuple(i for i in V if mask>>i&1)
    if fp(C): valid.append(C)
mx=max(map(len,valid)); M=sorted(C for C in valid if len(C)==mx)
assert mx==5 and len(M)==16
norm=[C for C in M if 0 in C]
assert len(norm)==5
C0=tuple(sorted([1,2,4,8,15]))
assert C0 in M
trans={tuple(sorted(c^t for c in C0)) for t in V}
assert trans==set(M) and len(trans)==16
# XOR-sum indexing
for t in V:
    C=tuple(sorted(c^t for c in C0))
    s=0
    for c in C:s^=c
    assert s==t
# distance profile
def hd(a,b): return (a^b).bit_count()
profiles={tuple(sorted(Counter(hd(a,b) for a,b in combinations(C,2)).items())) for C in M}
assert profiles=={((2,6),(3,4))}
# natural group translations + coordinate permutations, orbit/stabilizer of C0
perms=list(permutations(range(4)))
def pword(x,p):
    y=0
    for i in range(4):
        if x>>i&1: y |= 1<<p[i]
    return y
orbit=set(); stab=0
for t in V:
    for p in perms:
        D=tuple(sorted(pword(c,p)^t for c in C0))
        orbit.add(D)
        if D==C0: stab+=1
assert orbit==set(M) and stab==24
# normalized forms match analytic classification: all triples, or 3-edge star + opposite triple
def supp(x): return frozenset(i for i in range(4) if x>>i&1)
expected=[]
alltrip={0}|{sum(1<<i for i in S) for S in combinations(range(4),3)}
expected.append(tuple(sorted(alltrip)))
for i in range(4):
    W={0}
    for j in range(4):
        if j!=i: W.add((1<<i)|(1<<j))
    W.add(sum(1<<j for j in range(4) if j!=i))
    expected.append(tuple(sorted(W)))
assert set(norm)==set(expected)
# canonical list digest
text='\n'.join(','.join(f'{x:04b}' for x in C) for C in M)+'\n'
sha=hashlib.sha256(text.encode()).hexdigest()
print(f'VERIFY_OK vertices=16 maximum=5 labeled_maxima=16 normalized_maxima=5 translation_orbit=16 natural_group=384 stabilizer=24 hamming_profile=2x6,3x4 xor_index=true maxima_sha256={sha}')
