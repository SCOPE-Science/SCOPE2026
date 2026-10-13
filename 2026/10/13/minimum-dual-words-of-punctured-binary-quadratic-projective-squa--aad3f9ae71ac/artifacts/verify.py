from itertools import combinations
from math import comb

def columns(v):
    edges=list(combinations(range(v),2))
    subs=[]; masks=[]
    for r in range(2,v+1):
        for S in combinations(range(v),r):
            s=set(S); mask=0
            for j,e in enumerate(edges):
                if e[0] in s and e[1] in s: mask |= 1<<j
            subs.append(tuple(S)); masks.append(mask)
    return subs,masks

def expected(v):
    out=set()
    for T in combinations(range(v),3):
        a,b,c=T
        ss=[tuple(sorted(x)) for x in ((a,b),(a,c),(b,c),T)]
        out.add(tuple(sorted(ss)))
    for U in combinations(range(v),4):
        ss=[tuple(x) for x in combinations(U,3)]
        out.add(tuple(sorted(ss)))
    return out

for v in range(3,7):
    subs,masks=columns(v)
    assert all(masks)
    assert len(set(masks))==len(masks)
    # no weight-three dual word
    for I in combinations(range(len(masks)),3):
        assert masks[I[0]] ^ masks[I[1]] ^ masks[I[2]] != 0
    got=set()
    for I in combinations(range(len(masks)),4):
        if masks[I[0]] ^ masks[I[1]] ^ masks[I[2]] ^ masks[I[3]] == 0:
            got.add(tuple(sorted(subs[i] for i in I)))
    exp=expected(v)
    assert got==exp, (v,len(got),len(exp),got^exp)
    assert len(got)==comb(v,3)+comb(v,4)==comb(v+1,4)
print('VERIFY_OK')
