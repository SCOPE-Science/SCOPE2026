#!/usr/bin/env python3
from array import array
from itertools import combinations, product
from collections import Counter

Q=6; NCOORD=8; R=4
POW=[Q**(NCOORD-1-i) for i in range(NCOORD)]
SPACE=Q**NCOORD
CODE_TEXT=r"""01430421
12541532
23052043
30103154
45214205
50325310
03405225
14510330
25021441
30132552
41243003
52354114
03134001
14245112
25350223
30401334
51512445
52010550
02442243
13553304
24004415
35115520
40220031
51331142
02303231
13414342
24525453
35030504
40141015
51252120
05143544
10254055
21305100
32410211
43521322
54032433
04301535
13432040
20543151
31054202
42105313
53210434
04043240
15154351
20205402
31310513
42421024
53532135
05111133
10222244
21333355
32444400
43555511
54000022
01045452
12150503
23201014
34312125
45423230
50534341
00544125
11055230
22100341
33211452
44322503
55433014
02231500
13342011
24453122
35504233
40015344
51120455
05223315
10334420
21445531
32550042
43001153
54112204
03411050
14542101
25033212
30144323
41255434
52300445
04450305
15501410
20012521
31123032
42234143
53345254
00052413
11103524
22214035
33324140
44430251
55541302
02115012
13220123
24331234
35442345
40553450
51004501
01024314
12135425
23240530
34351041
45402152
50513203
05352332
10413443
21514554
52025505
43130110
54241221
04205542
15315053
20420104
31531215
42042320
53153431
01213111
12324222
23435333
34540444
45051555
42131403
00300252
11411303
22522414
33033525
44104030
55255141
05535024
10040135
21151240
32202351
44313402
54424513
01500043
12051134
23122205
34233310
45344421
50455532
03314404
10402515
25530020
31021031
41132242
52243353
12005001
03402520
31455113
23344502
55203541
32515205
30325000
02023150
14021545
54142054
34124521
03523252
45250342
00522424
44553234
53044110"""
CODE=[tuple(map(int,s.strip())) for s in CODE_TEXT.splitlines() if s.strip()]
assert len(CODE)==166 and len(set(CODE))==166

def enc(w):
    return sum(a*p for a,p in zip(w,POW))
def dec(x):
    out=[]
    for p in POW:
        out.append((x//p)%Q)
    return tuple(out)
def dist(a,b):
    return sum(x!=y for x,y in zip(a,b))
def layer_ids(w,d):
    base=enc(w)
    if d==0:
        return [base]
    out=[]
    for pos in combinations(range(NCOORD),d):
        opts=[]
        for i in pos:
            old=w[i]
            opts.append([(v-old)*POW[i] for v in range(Q) if v!=old])
        for ds in product(*opts):
            out.append(base+sum(ds))
    return out
def ball_ids(w):
    out=[]
    for d in range(R+1):
        out.extend(layer_ids(w,d))
    return out

# Exact coverage multiplicities on all 6^8 ambient words.
cnt=array('H',[0])*SPACE
balls=[]
layers_all=[]
for c in CODE:
    ls=[layer_ids(c,d) for d in range(R+1)]
    layers_all.append(ls)
    b=[]
    for z in ls: b.extend(z)
    balls.append(b)
    for x in b: cnt[x]+=1
assert min(cnt)==1
assert sum(1 for v in cnt if v==1)==7173
hist=Counter(cnt)
expected_hist={1:7173,2:53598,3:184112,4:358580,5:434466,6:348893,7:192658,8:74593,9:20757,10:4099,11:606,12:79,13:2}
assert dict(sorted(hist.items()))==expected_hist

private=[]
private_by_layer=[]
for ls in layers_all:
    p=[]
    pl=[]
    for z in ls:
        q=[x for x in z if cnt[x]==1]
        pl.append(len(q)); p.extend(q)
    private.append(p); private_by_layer.append(pl)
pt=[len(p) for p in private]
assert min(pt)==8 and max(pt)==105 and sum(pt)==7173
assert [sum(row[d] for row in private_by_layer) for d in range(5)]==[25,194,859,2124,3971]

# Every deletion has radius exactly 5: all points private to c have
# second-nearest distance exactly 5; every nonprivate point retains a radius-4 cover.
for i,P in enumerate(private):
    assert P
    others=CODE[:i]+CODE[i+1:]
    for xid in P:
        x=dec(xid)
        m=min(dist(x,c) for c in others)
        assert m==5

# Exact one-for-one repair sets.
# A replacement y repairs deletion of c iff y is within radius 4 of every
# point private to c.  Thus it lies in B_4(p0) for any fixed p0 in P_c.
repair_sets=[]
for i,Pids in enumerate(private):
    P=[dec(x) for x in Pids]
    # choose a radius-4 private point when available; all codewords have one
    r4=[x for x in layers_all[i][4] if cnt[x]==1]
    assert r4
    start=dec(r4[0])
    cand=ball_ids(start)
    # process private points farthest from start first only for speed;
    # this changes no logical condition.
    P.sort(key=lambda p: dist(p,start), reverse=True)
    for p in P:
        cand=[y for y in cand if dist(dec(y),p)<=R]
        if not cand:
            raise AssertionError("repair intersection unexpectedly empty")
    repair_sets.append(sorted(cand))

orig_ids=[enc(c) for c in CODE]
sizes=Counter(map(len,repair_sets))
assert sizes==Counter({1:165,2:1})
for i,S in enumerate(repair_sets):
    assert orig_ids[i] in S
nontrivial=[]
for i,S in enumerate(repair_sets):
    for y in S:
        if y!=orig_ids[i]:
            nontrivial.append((i, ''.join(map(str,CODE[i])), ''.join(map(str,dec(y)))))
assert nontrivial==[(101,"51004501","51004441")]

# Directly verify the unique alternate replacement remains a radius-4 cover.
i=101
alt=enc((5,1,0,0,4,4,4,1))
cnt2=array('H',cnt)
for x in balls[i]: cnt2[x]-=1
for x in ball_ids(dec(alt)): cnt2[x]+=1
assert min(cnt2)>=1

print("SPACE",SPACE)
print("BALL",len(balls[0]))
print("SINGLY_COVERED",7173)
print("PRIVATE_PER_CODEWORD_MIN_MAX",min(pt),max(pt))
print("DELETION_RADIUS_ALL",5)
print("REPAIR_SET_SIZES",dict(sorted(sizes.items())))
print("UNIQUE_NONTRIVIAL_SWAP","51004501->51004441")
print("VERIFY_OK")
