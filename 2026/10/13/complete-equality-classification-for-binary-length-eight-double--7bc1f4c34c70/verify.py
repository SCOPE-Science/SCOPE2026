#!/usr/bin/env python3
from collections import Counter, deque
from hashlib import sha256
import json

N=8
WORDS=1<<N
FULLMASK=(1<<WORDS)-1

def delta(x,y):
    a=(x & ~y & 0xff).bit_count()
    b=(y & ~x & 0xff).bit_count()
    return max(a,b)

adj=[0]*WORDS
for x in range(WORDS):
    m=0
    for y in range(x+1, WORDS):
        if delta(x,y)>=3:
            m |= 1<<y
    adj[x]=m

best=7
maxima=[]
nodes=0

def expand(chosen, cand):
    global best, maxima, nodes
    nodes += 1
    if len(chosen)+cand.bit_count() < best:
        return
    if not cand:
        s=len(chosen)
        if s>best:
            best=s; maxima=[tuple(chosen)]
        elif s==best:
            maxima.append(tuple(chosen))
        return
    while cand:
        if len(chosen)+cand.bit_count() < best:
            return
        lb=cand & -cand
        v=lb.bit_length()-1
        cand ^= lb
        expand(chosen+[v], cand & adj[v])

expand([], FULLMASK)
assert best==7, best
assert len(maxima)==181440, len(maxima)
maxset=set(maxima)
assert len(maxset)==len(maxima)

# Direct channel check: two downward Z-errors have intersecting balls iff Delta<=2.
def downball2(x):
    ones=[i for i in range(N) if (x>>i)&1]
    out={x}
    for i in range(len(ones)):
        out.add(x & ~(1<<ones[i]))
        for j in range(i+1,len(ones)):
            out.add(x & ~(1<<ones[i]) & ~(1<<ones[j]))
    return out
for x in range(WORDS):
    bx=downball2(x)
    for y in range(x+1,WORDS):
        assert bool(bx & downball2(y)) == (delta(x,y)<=2)

# Adjacent coordinate transpositions generate S8; global complement adds C2.
def swapcoords_word(w,i):
    a=(w>>i)&1; b=(w>>(i+1))&1
    return w if a==b else w ^ ((1<<i)|(1<<(i+1)))
def swap_code(c,i): return tuple(sorted(swapcoords_word(w,i) for w in c))
def comp_code(c): return tuple(sorted((w^0xff) for w in c))

def orbits(include_complement):
    unseen=set(maxset); obs=[]
    while unseen:
        seed=min(unseen)
        q=deque([seed]); orb={seed}; unseen.remove(seed)
        while q:
            c=q.popleft()
            imgs=[swap_code(c,i) for i in range(7)]
            if include_complement: imgs.append(comp_code(c))
            for d in imgs:
                assert d in maxset
                if d not in orb:
                    orb.add(d); q.append(d); unseen.discard(d)
        obs.append((min(orb),len(orb)))
    obs.sort()
    return obs
sobs=orbits(False)
fobs=orbits(True)
assert sorted(s for _,s in sobs)==[20160,40320,40320,40320,40320]
assert sorted(s for _,s in fobs)==[20160,80640,80640]
assert sum(s for _,s in fobs)==181440

def bits(w): return format(w,'08b')
def invariants(c):
    weights=Counter(w.bit_count() for w in c)
    ds=Counter(); hs=Counter()
    for i in range(len(c)):
        for j in range(i+1,len(c)):
            ds[delta(c[i],c[j])]+=1
            hs[(c[i]^c[j]).bit_count()]+=1
    coord=sorted(sum((w>>i)&1 for w in c) for i in range(N))
    return {'weights':dict(sorted(weights.items())), 'asymmetric_distances':dict(sorted(ds.items())), 'hamming_distances':dict(sorted(hs.items())), 'coordinate_one_counts':coord}

# Stable census hash: sorted decimal code tuples, one per line.
h=sha256()
for c in sorted(maxima):
    h.update((','.join(map(str,c))+'\n').encode())

report={
 'n':8,'minimum_asymmetric_distance':3,'maximum_size':best,
 'labeled_maxima':len(maxima),'search_nodes':nodes,
 'coordinate_group_order':40320,
 'coordinate_orbits':[{'representative':[bits(w) for w in r],'orbit_size':s,'stabilizer':40320//s,'invariants':invariants(r)} for r,s in sobs],
 'full_isometry_group_order':80640,
 'full_isometry_orbits':[{'representative':[bits(w) for w in r],'orbit_size':s,'stabilizer':80640//s,'invariants':invariants(r)} for r,s in fobs],
 'census_sha256':h.hexdigest(),
}
print(json.dumps(report,sort_keys=True,separators=(',',':')))
print('VERIFY_OK maximum=7 labeled_maxima=181440 coordinate_orbits=5 full_isometry_orbits=3 full_orbit_sizes=20160,80640,80640')
