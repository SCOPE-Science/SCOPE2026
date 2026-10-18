#!/usr/bin/env python3
"""Exact state-closure proof for rank-two theories of binary-coloured directed cycles."""
from collections import Counter, deque

def capped(a): return min(4,a)

def seed(a,b):
    return (a,b,a,b, int(a==0)+int(b==0),int(a==1)+int(b==1),0)

def extend(s,c):
    a,b,p,q,z,o,mask=s
    return (a,b,q,c,capped(z+(c==0)),capped(o+(c==1)),mask | (1<<((p<<2)|(q<<1)|c)))

def signature(s):
    a,b,p,q,z,o,mask=s
    mask |= (1<<((p<<2)|(q<<1)|a)) | (1<<((q<<2)|(a<<1)|b))
    result=0
    for t in range(8):
        if not mask & (1<<t):continue
        pre=(t>>2)&1; own=(t>>1)&1; suc=t&1
        other = int(z-(pre==0)-(own==0)-(suc==0)>0) + 2*int(o-(pre==1)-(own==1)-(suc==1)>0)
        result |= 1 << (4*t+other)
    return result

def main():
    starts={seed(a,b):f'{a}{b}' for a in (0,1) for b in (0,1)}
    q=deque(starts); reach=dict(starts)
    while q:
        s=q.popleft()
        for c in (0,1):
            t=extend(s,c)
            if t not in reach:
                reach[t]=reach[s]+str(c)
                q.append(t)
    assert len(reach)==758, len(reach)
    assert max(map(len,reach.values()))==15
    all_theories={}
    for s,word in reach.items():
        if len(word)<3:continue
        sig=signature(s)
        if sig not in all_theories or len(word)<len(all_theories[sig]):
            all_theories[sig]=word
    dist=Counter(map(len,all_theories.values()))
    assert len(all_theories)==48
    assert dist == {3:4,4:6,5:6,6:9,7:10,8:9,9:4},dist
    assert len({s for s,w in all_theories.items() if '0' in w and '1' in w})==44
    print('STATES',len(reach),'MAX_SHORTEST_STATE_LEN',max(map(len,reach.values())))
    print('RANK2_THEORIES',len(all_theories),'MAX_MIN_REP',max(dist),'MIXED_THEORIES',44)
    print('MIN_REP_DISTRIBUTION',sorted(dist.items()))
    print('LONGEST_MINIMAL_WITNESSES',sorted(w for w in all_theories.values() if len(w)==9))
    print('SIGNATURE_LIST_BEGIN')
    for sig,w in sorted(all_theories.items()):print(f'{sig:08x} {len(w):2d} {w}')
    print('SIGNATURE_LIST_END')
    return reach, all_theories

if __name__=='__main__':main()
