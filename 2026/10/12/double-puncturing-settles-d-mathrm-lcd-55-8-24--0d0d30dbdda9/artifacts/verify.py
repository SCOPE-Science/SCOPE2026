#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

HEX_ROWS = [
    '819775629AD4B88',
    '40CBBAB14D6A5D8',
    '217F84E44A2DC78',
    '11A59BCEC98E070',
    '08D2CDE764C7268',
    '046966F3B263880',
    '0234B379D931DC8',
    '808D2CDE764C608',
]

def bits(h):
    b=[]
    for ch in h:
        v=int(ch,16)
        b += [(v>>3)&1,(v>>2)&1,(v>>1)&1,v&1]
    assert b[57:] == [0,0,0]
    return b[:57]

G=[bits(h) for h in HEX_ROWS]

def rank(rows):
    a=[sum((x&1)<<j for j,x in enumerate(row)) for row in rows]
    r=0
    for c in range(len(rows[0])):
        p=next((i for i in range(r,len(a)) if (a[i]>>c)&1),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        for i in range(len(a)):
            if i!=r and ((a[i]>>c)&1): a[i]^=a[r]
        r+=1
        if r==len(a): break
    return r

def gram(rows):
    return [[sum(x*y for x,y in zip(a,b))&1 for b in rows] for a in rows]

def words(rows):
    n=len(rows[0]); out=[]
    for mask in range(1<<len(rows)):
        v=[0]*n
        for i,row in enumerate(rows):
            if (mask>>i)&1:
                v=[x^y for x,y in zip(v,row)]
        out.append(v)
    return out

def dist_and_enum(rows):
    ws=[sum(v) for v in words(rows)]
    return min(ws[1:]), Counter(ws)

def puncture(rows, S):
    S=set(S)
    return [[x for j,x in enumerate(row) if j not in S] for row in rows]

assert rank(G)==8
assert rank(gram(G))==8
d0,e0=dist_and_enum(G)
assert d0==25

good=[]; lcd=0
for S in combinations(range(57),2):
    H=puncture(G,S)
    if rank(H)!=8: continue
    if rank(gram(H))==8:
        lcd+=1
        d,e=dist_and_enum(H)
        if d==24:
            good.append((tuple(j+1 for j in S),e[24]))

assert lcd==756
assert good==[((9,18),49),((10,30),46),((34,48),48),((41,42),47)]
H=puncture(G,(8,17))
assert rank(H)==8 and rank(gram(H))==8
d,e=dist_and_enum(H)
assert d==24
assert dict(sorted(e.items()))=={0:1,24:49,26:98,28:53,30:9,32:10,34:28,36:7,38:1}
print('VERIFY_OK')
print('original_distance=25')
print('double_punctures=1596 lcd_double_punctures=756')
print('optimal_pairs_1_based=' + repr(good))
print('witness_weight_enumerator=' + repr(dict(sorted(e.items()))))
