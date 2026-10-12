#!/usr/bin/env python3
import itertools, hashlib, json, collections

q=3
rows=3
V=list(itertools.product(range(q), repeat=rows))
index={v:i for i,v in enumerate(V)}

pairings=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]

def four_bad(c4):
    w=[V[i] for i in c4]
    for A,B in pairings:
        separated=False
        for r in range(rows):
            sa={w[A[0]][r],w[A[1]][r]}
            sb={w[B[0]][r],w[B[1]][r]}
            if sa.isdisjoint(sb):
                separated=True
                break
        if not separated:
            return True
    return False

forbidden={c for c in itertools.combinations(range(len(V)),4) if four_bad(c)}
assert len(forbidden)==16092

def good(C):
    return not any(tuple(e) in forbidden for e in itertools.combinations(C,4))

maxima=[c for c in itertools.combinations(range(len(V)),5) if good(c)]
assert len(maxima)==54
assert not any(good(c) for c in itertools.combinations(range(len(V)),6))
maxset=set(maxima)

canonical=tuple(sorted(index[x] for x in [(0,0,0),(0,1,1),(1,0,1),(1,1,0),(2,2,2)]))
assert canonical in maxset

for C in maxima:
    words=[V[i] for i in C]
    singleton_positions=[]
    for r in range(rows):
        cnt=collections.Counter(w[r] for w in words)
        assert sorted(cnt.values())==[1,2,2]
        singleton_symbol=next(a for a,m in cnt.items() if m==1)
        pos=next(j for j,w in enumerate(words) if w[r]==singleton_symbol)
        singleton_positions.append(pos)
    assert singleton_positions[0]==singleton_positions[1]==singleton_positions[2]
    s=singleton_positions[0]
    core=[w for j,w in enumerate(words) if j!=s]
    # Map the two repeated symbols in each coordinate to 0,1 in sorted order.
    mapped=[]
    for w in core:
        bits=[]
        for r in range(rows):
            vals=sorted({u[r] for u in core})
            assert len(vals)==2
            bits.append(vals.index(w[r]))
        mapped.append(tuple(bits))
    parities={sum(b)%2 for b in mapped}
    assert len(parities)==1 and len(set(mapped))==4
    hd=collections.Counter(sum(a!=b for a,b in zip(words[i],words[j])) for i in range(5) for j in range(i+1,5))
    assert hd==collections.Counter({2:6,3:4})

s3=list(itertools.permutations(range(3)))
coord_perms=list(itertools.permutations(range(3)))

def transform_word(v,sps,cp):
    tmp=[sps[r][v[r]] for r in range(rows)]
    out=[None]*rows
    for r in range(rows):
        out[cp[r]]=tmp[r]
    return tuple(out)

group=[]
for sps in itertools.product(s3, repeat=rows):
    for cp in coord_perms:
        group.append(tuple(index[transform_word(v,sps,cp)] for v in V))
assert len(group)==1296 and len(set(group))==1296

orbit={tuple(sorted(g[i] for i in canonical)) for g in group}
assert len(orbit)==54
assert orbit==maxset
stabilizer=sum(1 for g in group if tuple(sorted(g[i] for i in canonical))==canonical)
assert stabilizer==24

blob='\n'.join(','.join(''.join(map(str,V[i])) for i in C) for C in sorted(maxima)).encode()
digest=hashlib.sha256(blob).hexdigest()
print('VERIFY_OK vertices=27 forbidden4=16092 maximum=5 labeled_maxima=54 natural_group=1296 orbits=1 orbit_size=54 stabilizer=24 row_profile=2,2,1x3 hamming_profile=2x6,3x4 canonical=000,011,101,110,222 maxima_sha256='+digest)
