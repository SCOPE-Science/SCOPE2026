#!/usr/bin/env python3
from itertools import product, combinations

Q=range(3)
WORDS=list(product(Q, repeat=3))
INDEX={w:i for i,w in enumerate(WORDS)}

def inside_box(x,u,v):
    return all(x[j] in (u[j],v[j]) for j in range(3))

def pair_bad(indices, iu, iv):
    u=WORDS[iu]; v=WORDS[iv]
    X=[i for i in indices if inside_box(WORDS[i],u,v)]
    # An element is present in every parent set with the same descendant
    # iff some coordinate-symbol it carries occurs exactly once in X.
    for ix in X:
        x=WORDS[ix]
        if any(sum(WORDS[i][j]==x[j] for i in X)==1 for j in range(3)):
            return False
    return True

def smippc(indices):
    inds=sorted(indices)
    for iu,iv in combinations(inds,2):
        if pair_bad(inds,iu,iv):
            return False
    return True

def forbidden_masks():
    obs=set()
    for iu,iv in combinations(range(27),2):
        u,v=WORDS[iu],WORDS[iv]
        B=[i for i,x in enumerate(WORDS) if inside_box(x,u,v)]
        mid=[i for i in B if i not in (iu,iv)]
        base=(1<<iu)|(1<<iv)
        for bits in range(1<<len(mid)):
            inds=[iu,iv]
            mask=base
            for k,i in enumerate(mid):
                if bits>>k & 1:
                    inds.append(i); mask |= 1<<i
            if pair_bad(inds,iu,iv):
                obs.add(mask)
    mins=[]
    for m in sorted(obs,key=lambda z:(z.bit_count(),z)):
        if not any((k & m)==k for k in mins):
            mins.append(m)
    return mins

EDGES=forbidden_masks()
BYV=[[] for _ in range(27)]
for e in EDGES:
    for i in range(27):
        if e>>i & 1:
            BYV[i].append(e)

def compatible_add(mask,v):
    nm=mask | (1<<v)
    return all((e & nm) != e for e in BYV[v])

def no_target_with_rep(rep,target=12):
    z=INDEX[(0,0,0)]
    mask=(1<<z)|(1<<rep)
    assert smippc([z,rep])
    rest=[i for i in range(27) if i not in (z,rep)]
    nodes=0
    def dfs(pos,mask,count):
        nonlocal nodes
        nodes += 1
        if count>=target:
            return True
        if count + len(rest)-pos < target:
            return False
        for p in range(pos,len(rest)):
            if count + len(rest)-p < target:
                break
            v=rest[p]
            if compatible_add(mask,v) and dfs(p+1,mask|(1<<v),count+1):
                return True
        return False
    exists=dfs(0,mask,2)
    return (not exists),nodes

W=[(0,0,0),(0,0,1),(0,1,1),(0,1,2),(0,2,2),(1,0,0),(1,0,2),(1,2,1),(2,0,2),(2,1,0),(2,2,2)]
WI=[INDEX[x] for x in W]
assert len(W)==11 and len(set(W))==11
assert smippc(WI)
assert len(EDGES)==459, len(EDGES)
assert {e.bit_count() for e in EDGES}=={4,5}
res=[]
for w in [(1,0,0),(1,1,0),(1,1,1)]:
    no,nodes=no_target_with_rep(INDEX[w],12)
    assert no
    res.append((w,nodes))
# cross-check forbidden-mask criterion against direct definition for witness and selected small samples
wmask=sum(1<<i for i in WI)
assert all((e & wmask)!=e for e in EDGES)
print('VERIFY_OK maximum=11 witness=11 minimal_obstructions=%d sizes=4,5 symmetry_reps=3 nodes=%s' % (len(EDGES), ','.join(str(n) for _,n in res)))
