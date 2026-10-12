#!/usr/bin/env python3
import hashlib
from collections import Counter

N=6
MASK=(1<<N)-1
WORDS=list(range(1<<N))

def bits(x): return format(x, f'0{N}b')
def rotl(x,k):
    s=bits(x)
    return int(s[k:]+s[:k],2)
def rots(x): return tuple(rotl(x,k) for k in range(N))
def primitive(x): return len(set(rots(x)))==N

def splice(x,y,k):
    sx,sy=bits(x),bits(y)
    return int(sx[k:]+sy[:k],2)

def comma_free(C):
    S=set(C)
    return all(splice(x,y,k) not in S for x in S for y in S for k in range(1,N))

prim=[x for x in WORDS if primitive(x)]
necklaces=[]; seen=set()
for x in prim:
    if x in seen: continue
    cl=tuple(sorted(set(rots(x))))
    assert len(cl)==N
    necklaces.append(cl); seen.update(cl)
necklaces=tuple(sorted(necklaces))
assert len(prim)==54 and len(necklaces)==9 and len(seen)==54

# A partial comma-free set remains impossible after extension, so this DFS
# exhausts all choices of one representative from each of the nine necklaces.
nodes=0; sols=[]
def can_add(chosen,w):
    T=set(chosen); T.add(w)
    # direct from-definition check on the enlarged partial code
    return all(splice(x,y,k) not in T for x in T for y in T for k in range(1,N))
def dfs(i,chosen):
    global nodes
    nodes += 1
    if i==len(necklaces):
        sols.append(tuple(sorted(chosen))); return
    for w in necklaces[i]:
        if can_add(chosen,w):
            dfs(i+1, chosen+(w,))
dfs(0,tuple())
sols=tuple(sorted(set(sols)))
assert len(sols)==1972
assert all(len(C)==9 and comma_free(C) for C in sols)
solset=set(sols)

def comp_word(x): return x ^ MASK
def rev_word(x): return int(bits(x)[::-1],2)
def transform(C, c=False, r=False):
    out=[]
    for x in C:
        if c: x=comp_word(x)
        if r: x=rev_word(x)
        out.append(x)
    return tuple(sorted(out))

group=[(False,False),(True,False),(False,True),(True,True)]
assert all(transform(C,*g) in solset for C in sols for g in group)
seenC=set(); orbits=[]
for C in sols:
    if C in seenC: continue
    orb={transform(C,*g) for g in group}
    seenC |= orb; orbits.append(tuple(sorted(orb)))
assert len(orbits)==493
orbit_sizes=Counter(map(len,orbits))
assert orbit_sizes==Counter({4:493})
fixed={g:sum(transform(C,*g)==C for C in sols) for g in group[1:]}
assert all(v==0 for v in fixed.values())

# Every maximum takes one word from each necklace; hence its weight spectrum is fixed.
expected_weights=tuple(sorted(bin(cl[0]).count('1') for cl in necklaces))
assert expected_weights==(1,2,2,3,3,3,4,4,5)
assert all(tuple(sorted(bin(x).count('1') for x in C))==expected_weights for C in sols)

canon=min(sols)
assert comma_free(canon)
lines=[' '.join(bits(x) for x in C) for C in sols]
blob=('\n'.join(lines)+'\n').encode('ascii')
digest=hashlib.sha256(blob).hexdigest()
print('VERIFY_OK')
print(f'primitive_words={len(prim)} necklaces={len(necklaces)} upper_bound=9 dfs_nodes={nodes}')
print(f'maximum=9 labeled_maxima={len(sols)} symmetry_group=4 orbits={len(orbits)} orbit_sizes=4x{len(orbits)}')
print('fixed_nonidentity=' + ','.join(str(fixed[g]) for g in group[1:]))
print('weight_multiset=' + ','.join(map(str,expected_weights)))
print('canonical=' + ','.join(bits(x) for x in canon))
print('census_sha256=' + digest)
