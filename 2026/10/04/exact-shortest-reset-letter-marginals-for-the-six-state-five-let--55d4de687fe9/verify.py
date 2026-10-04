#!/usr/bin/env python3
from collections import deque, defaultdict

N=6
LETTERS={
    "a": (1,2,3,4,5,0),
    "b": (0,2,2,3,4,5),
    "c": (2,2,3,4,5,0),
    "d": (1,3,3,4,5,0),
    "e": (2,3,3,4,5,0),
}
EXPECTED_TOTAL=452984832
EXPECTED_LENGTH=20
EXPECTED_TARGET=3  # one-based

def step_mask(mask, trans):
    out=0
    for q in range(N):
        if mask & (1<<q): out |= 1<<trans[q]
    return out

def poly_mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return r

def poly_pow(p,n):
    r=[1]
    for _ in range(n): r=poly_mul(r,p)
    return r

def factor_poly(tracked):
    if tracked=='a':
        p=[64];
        for f,k in [([1,1],6),([2,1],3),([3,1],6)]: p=poly_mul(p,poly_pow(f,k))
        return p
    if tracked=='b': return [EXPECTED_TOTAL]
    if tracked in ('c','d'):
        p=[0,8]
        for f,k in [([1,1],3),([3,1],6),([7,4,1],3)]: p=poly_mul(p,poly_pow(f,k))
        return p
    if tracked=='e':
        p=[64]
        for f,k in [([1,1],3),([3,1],6),([5,1],3)]: p=poly_mul(p,poly_pow(f,k))
        return p
    raise KeyError(tracked)

def shortest_distances_mask():
    full=(1<<N)-1
    dist={full:0}; q=deque([full])
    while q:
        s=q.popleft(); d=dist[s]
        for t in LETTERS.values():
            u=step_mask(s,t)
            if u not in dist:
                dist[u]=d+1; q.append(u)
    return dist

def marginals_mask(dist, tracked):
    full=(1<<N)-1
    dp={full:{0:1}}
    for d in range(EXPECTED_LENGTH):
        nxt={}
        for s,hist in dp.items():
            assert dist[s]==d
            for ch,t in LETTERS.items():
                u=step_mask(s,t)
                if dist.get(u)!=d+1: continue
                out=nxt.setdefault(u,defaultdict(int))
                for k,v in hist.items(): out[k+(ch==tracked)]+=v
        dp=nxt
    total=defaultdict(int); targets=defaultdict(int)
    for s,hist in dp.items():
        if s and not (s&(s-1)):
            target=s.bit_length()
            for k,v in hist.items(): total[k]+=v; targets[target]+=v
    p=[0]*(max(total)+1)
    for k,v in total.items(): p[k]=v
    return p,dict(targets)

def step_set(S,trans): return frozenset(trans[q] for q in S)

def independent_set_dp(tracked):
    full=frozenset(range(N))
    # This implementation does not use the bit-mask distance table. It propagates
    # only the first occurrence layer of each subset, together with histograms.
    seen={full:0}; layer={full:{0:1}}
    for d in range(100):
        singles={s:h for s,h in layer.items() if len(s)==1}
        if singles:
            assert d==EXPECTED_LENGTH
            total=defaultdict(int); targets=defaultdict(int)
            for s,h in singles.items():
                target=next(iter(s))+1
                for k,v in h.items(): total[k]+=v; targets[target]+=v
            p=[0]*(max(total)+1)
            for k,v in total.items(): p[k]=v
            return p,dict(targets),len(seen)
        nxt={}
        for s,hist in layer.items():
            for ch,t in LETTERS.items():
                u=step_set(s,t)
                old=seen.get(u)
                if old is not None and old<d+1: continue
                if old is None: seen[u]=d+1
                out=nxt.setdefault(u,defaultdict(int))
                for k,v in hist.items(): out[k+(ch==tracked)]+=v
        layer=nxt
    raise AssertionError('no singleton')

def main():
    dist=shortest_distances_mask()
    L=min(dist[1<<q] for q in range(N))
    assert L==EXPECTED_LENGTH
    assert len(dist)==63
    for ch in LETTERS:
        p1,t1=marginals_mask(dist,ch)
        p2,t2,seen=independent_set_dp(ch)
        expected=factor_poly(ch)
        assert p1==p2==expected, (ch,p1,p2,expected)
        assert sum(p1)==EXPECTED_TOTAL
        assert t1==t2=={EXPECTED_TARGET:EXPECTED_TOTAL}
        if ch=='b': assert p1==[EXPECTED_TOTAL]
    print('VERIFY_OK length=20 total=452984832 target=3 reachable_subsets=63')
if __name__=='__main__': main()
