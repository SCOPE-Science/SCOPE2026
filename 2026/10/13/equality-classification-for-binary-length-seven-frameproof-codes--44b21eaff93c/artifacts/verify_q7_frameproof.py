#!/usr/bin/env python3
import hashlib,itertools,json
from collections import Counter

N_DIM=7
N=1<<N_DIM

def between(a,b,c):
    # c is on a shortest a-b path in the binary Hamming cube.
    return ((c^a)&(c^b)) == 0

def bad3(a,b,c):
    return between(a,b,c) or between(a,c,b) or between(b,c,a)

def good_code(C):
    return all(not bad3(a,b,c) for a,b,c in itertools.combinations(C,3))

# For each selected pair, mask all third vertices that would make a bad triple.
badpair=[[0]*N for _ in range(N)]
for a in range(N):
    for b in range(a+1,N):
        m=0
        for c in range(N):
            if c!=a and c!=b and bad3(a,b,c):
                m |= 1<<c
        badpair[a][b]=badpair[b][a]=m

def enumerate_origin(target, collect=False):
    sols=[]
    nodes=0
    def rec(S,cand):
        nonlocal nodes
        nodes+=1
        need=target-len(S)
        if need==0:
            if collect: sols.append(tuple(S))
            return 1
        if cand.bit_count()<need:
            return 0
        cnt=0
        cm=cand
        while cm:
            if cm.bit_count()<need:
                break
            lsb=cm & -cm
            v=lsb.bit_length()-1
            cm-=lsb
            rm=0
            for u in S:
                rm |= badpair[u][v]
            cnt += rec(S+[v], cm & ~rm)
        return cnt
    cnt=rec([0], ((1<<N)-1)^1)
    return cnt,sols,nodes

count9, maxima, nodes9 = enumerate_origin(9, collect=True)
count10, _, nodes10 = enumerate_origin(10, collect=False)
assert count9==7560
assert count10==0
assert all(good_code(C) for C in maxima)
maxset=set(maxima)

# A nonzero translation is a fixed-point-free involution, hence cannot stabilize
# an odd-cardinality set. Consequently each translation orbit of a 9-set has
# size 128 and has exactly 9 members containing 0.
assert all(tuple(sorted(x^t for x in C)) != C for C in maxima[:50] for t in range(1,N))
labeled_total=count9*N//9
assert labeled_total==107520

perms=list(itertools.permutations(range(N_DIM)))
def perm_word(x,p):
    y=0
    for i in range(N_DIM):
        if (x>>i)&1:
            y |= 1<<p[i]
    return y
pmaps=[[perm_word(x,p) for x in range(N)] for p in perms]

remaining=set(maxima)
orbits=[]
while remaining:
    rep=min(remaining)
    normalized=set()
    for mp in pmaps:
        pc=tuple(mp[x] for x in rep)
        for t in pc:
            D=tuple(sorted(x^t for x in pc))
            assert 0 in D
            assert D in maxset
            normalized.add(D)
    remaining -= normalized
    full_size=len(normalized)*N//9
    stabilizer=(N*len(perms))//full_size
    dist=Counter((a^b).bit_count() for a,b in itertools.combinations(rep,2))
    coord=[]
    for j in range(N_DIM):
        ones=sum((x>>j)&1 for x in rep)
        coord.append(tuple(sorted((ones,9-ones))))
    orbits.append({
        'rep':rep,
        'normalized_origin':len(normalized),
        'full_size':full_size,
        'stabilizer':stabilizer,
        'distance_profile':dict(sorted(dist.items())),
        'coordinate_profiles':sorted(coord),
        'min_distance':min(dist),
    })

orbits.sort(key=lambda x:x['full_size'], reverse=True)
assert len(orbits)==2
assert [x['full_size'] for x in orbits]==[80640,26880]
assert [x['stabilizer'] for x in orbits]==[8,24]
assert sum(x['full_size'] for x in orbits)==labeled_total
assert sorted(x['normalized_origin'] for x in orbits)==[1890,5670]
assert {tuple(sorted(x['distance_profile'].items())) for x in orbits} == {
    ((2,1),(3,10),(4,17),(5,8)),
    ((3,15),(4,17),(5,3),(6,1)),
}

# Canonical serialization hash of every normalized maximum containing 0.
serial='\n'.join(','.join(f'{x:07b}' for x in C) for C in sorted(maxima))+'\n'
sha=hashlib.sha256(serial.encode()).hexdigest()

print('VERIFY_OK',
      f'vertices={N}',
      f'maximum=9',
      f'origin_maxima={count9}',
      f'target10={count10}',
      f'labeled_maxima={labeled_total}',
      f'natural_group={N*len(perms)}',
      f'orbits={len(orbits)}',
      'orbit_sizes='+','.join(str(x['full_size']) for x in orbits),
      'stabilizers='+','.join(str(x['stabilizer']) for x in orbits),
      f'nodes9={nodes9}',
      f'nodes10={nodes10}',
      f'normalized_sha256={sha}')
for i,x in enumerate(orbits,1):
    print('ORBIT',i,
          'rep='+','.join(f'{v:07b}' for v in x['rep']),
          f'normalized_origin={x["normalized_origin"]}',
          f'full_size={x["full_size"]}',
          f'stabilizer={x["stabilizer"]}',
          'distance_profile='+','.join(f'{d}x{c}' for d,c in x['distance_profile'].items()),
          'coordinate_profiles='+','.join(f'{a}-{b}' for a,b in x['coordinate_profiles']))
