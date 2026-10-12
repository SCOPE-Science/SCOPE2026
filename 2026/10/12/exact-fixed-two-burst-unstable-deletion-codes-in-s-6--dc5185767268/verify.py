#!/usr/bin/env python3
from itertools import permutations
from collections import Counter, defaultdict
from functools import lru_cache
import json

N=6
S=2
EXPECTED_MAX=12
EXPECTED_COUNT=67163560
EXPECTED_HIST={16:100,17:3240,18:47958,19:415120,20:2283083,21:8134400,22:18331932,23:23922912,24:14024815}
WITNESS=[
(1,2,3,4,5,6),(1,3,2,4,6,5),(1,5,2,4,6,3),(2,1,3,6,5,4),
(3,4,2,5,1,6),(3,4,5,1,6,2),(3,6,2,5,1,4),(3,6,4,2,5,1),
(5,6,3,1,2,4),(5,4,3,2,1,6),(6,1,5,2,4,3),(6,4,5,2,1,3)]

def standardize(seq):
    order={v:i for i,v in enumerate(sorted(seq))}
    return tuple(order[v]+1 for v in seq)

def descendants(p):
    return {standardize(p[:i]+p[i+S:]) for i in range(N-S+1)}

words=list(permutations(range(1,N+1)))
outs=list(permutations(range(1,N-S+1)))
out_index={p:i for i,p in enumerate(outs)}
mask_to_words=defaultdict(list)
word_mask={}
for p in words:
    m=0
    for q in descendants(p):
        m |= 1<<out_index[q]
    word_mask[p]=m
    mask_to_words[m].append(p)
mult={m:len(v) for m,v in mask_to_words.items()}
masks=sorted(mult)
by_bit=[[] for _ in outs]
for m in masks:
    for b in range(len(outs)):
        if (m>>b)&1:
            by_bit[b].append(m)

@lru_cache(maxsize=None)
def solve(U):
    if U==0:
        return (0,1,((0,1),))
    b=(U & -U).bit_length()-1
    best,cnt,hist=solve(U & ~(1<<b))
    hist=dict(hist)
    for m in by_bit[b]:
        if m & ~U:
            continue
        sub_best,sub_cnt,sub_hist_t=solve(U ^ m)
        val=1+sub_best
        weighted=mult[m]*sub_cnt
        shifted={k+m.bit_count(): mult[m]*v for k,v in sub_hist_t}
        if val>best:
            best=val
            cnt=weighted
            hist=shifted
        elif val==best:
            cnt += weighted
            for k,v in shifted.items():
                hist[k]=hist.get(k,0)+v
    return (best,cnt,tuple(sorted(hist.items())))

full=(1<<len(outs))-1
best,count,hist_t=solve(full)
hist=dict(hist_t)
assert len(words)==720
assert len(outs)==24
assert len(mask_to_words)==610
assert Counter(map(len, map(descendants,words)))==Counter({3:302,4:258,2:96,5:54,1:10})
assert Counter(mult.values())==Counter({1:538,2:50,4:16,3:6})
assert best==EXPECTED_MAX, (best,EXPECTED_MAX)
assert count==EXPECTED_COUNT, (count,EXPECTED_COUNT)
assert hist==EXPECTED_HIST, (hist,EXPECTED_HIST)
assert sum(hist.values())==count
assert len(WITNESS)==EXPECTED_MAX and len(set(WITNESS))==EXPECTED_MAX
seen=0
for p in WITNESS:
    m=word_mask[p]
    assert (seen & m)==0
    seen |= m
assert seen.bit_count()==24
print("VERIFY_OK vertices=720 outputs=24 distinct_descendant_masks=610 maximum=12 labeled_maxima=67163560 perfect_maxima=14024815 footprint_hist=" + ",".join(f"{k}:{hist[k]}" for k in sorted(hist)) + f" states={solve.cache_info().currsize} witness_footprint={seen.bit_count()}")
