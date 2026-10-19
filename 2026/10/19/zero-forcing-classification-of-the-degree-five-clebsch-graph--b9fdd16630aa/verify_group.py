"""Exact zero-forcing and automorphism-orbit certificate for the 16-vertex folded five-cube."""
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
import csv

GEN=(1,2,4,8,15)
V=range(16)
ALL=(1<<16)-1
NEIGH={x:{x^g for g in GEN} for x in V}

def force(blue):
    colored={x for x in V if (blue>>x)&1}
    round_count=0
    first_wave=0
    while len(colored)<16:
        white=set(V)-colored
        adds={next(iter(t)) for x in colored if len(t:=NEIGH[x]&white)==1}
        if not adds:
            return False,round_count,first_wave
        if round_count==0: first_wave=len(adds)
        colored|=adds
        round_count+=1
    return True,round_count,first_wave

STAT=Counter();MIN=Counter();FORCED={};TIMES=Counter()
for s in range(1<<16):
    good,t,wave=force(s)
    FORCED[s]=good
    if good:
        size=s.bit_count();STAT[size]+=1;TIMES[(size,t)]+=1
assert [STAT[i] for i in range(17)]==[0]*10+[3872,3632,1760,560,120,16,1]
assert sum(STAT.values())==9961
for s,good in FORCED.items():
    if good and all(not FORCED[s&~(1<<i)] for i in V if (s>>i)&1):
        MIN[s.bit_count()]+=1
assert MIN=={10:3872}
assert TIMES[(10,2)]==3872
assert [TIMES[(11,1)],TIMES[(11,2)],TIMES[(12,1)],TIMES[(12,2)]]==[272,3360,1280,480]

# The five generators have the single linear dependency G_0+...+G_4=0;
# hence every permutation extends to an invertible linear map on F_2^4.
AUT=[]
for gs in permutations(GEN):
    linear=tuple(__import__('functools').reduce(int.__xor__,(gs[i] for i in range(4) if (x>>i)&1),0) for x in V)
    assert len(set(linear))==16
    for t in V:
        p=tuple(y^t for y in linear)
        assert all({p[x^g] for g in GEN}==NEIGH[p[x]] for x in V)
        AUT.append(p)
assert len(AUT)==1920 and len(set(AUT))==1920

def push(m,p):
    r=0
    for i in V:
        if (m>>i)&1:r|=1<<p[i]
    return r

unseen={sum(1<<x for x in c) for c in combinations(V,6)}
rows=[]
while unseen:
    white=min(unseen)
    orbit={push(white,p) for p in AUT}
    assert orbit<=unseen
    unseen-=orbit
    good,tm,fw=force(ALL^white)
    rows.append({
        'white_mask':white,
        'white_vertices':','.join(str(i) for i in V if white>>i&1),
        'orbit_size':len(orbit),
        'is_zero_forcing':int(good),
        'rounds_until_stall_or_finish':tm,
        'first_wave_size':fw,
    })
rows.sort(key=lambda r:(-r['is_zero_forcing'],-r['orbit_size'],r['white_mask']))
assert len(rows)==18 and sum(r['orbit_size'] for r in rows)==8008
assert sum(r['orbit_size'] for r in rows if r['is_zero_forcing'])==3872
assert [r['orbit_size'] for r in rows if r['is_zero_forcing']]==[960,960,480,480,480,320,192]
path=Path(__file__).with_name('six_white_orbit_certificate.csv')
assert path.is_file(), 'Missing mandatory orbit certificate'
with path.open(newline='',encoding='utf-8') as f:
    cert=list(csv.DictReader(f))
assert len(cert)==len(rows)
for c,r in zip(cert,rows):
    assert c=={k:str(v) for k,v in r.items()},(c,r)
print('VERIFY_GROUP_OK subsets=65536 zero_forcing=9961 minimum_sets=3872')
print('VERIFY_GROUP_OK 6-white-orbits=18 forcing_orbits=7 size_distribution=960,960,480,480,480,320,192')
print('VERIFY_GROUP_OK all_1920_maps_are_automorphisms=true minimum_all_two_rounds=true')
print('VERIFY_GROUP_OK inclusion_minimal_10=3872 no_larger_inclusion_minimal=true')
