#!/usr/bin/env python3
"""Exact finite-state verification for two temporal-period gaps of RESOCA 115.

Run with Python 3, without third-party packages.  The graph represents every
bi-infinite configuration of the given temporal period.  Its rooted strongly
connected component characterizes finite-support configurations.
"""
from collections import deque

RULE=115


def all_temporal_columns(p):
    """Exact S_p: b_t=0 implies b_(t-1) != b_(t+1)."""
    return [b for b in range(1 << p) if all(
        ((b >> t) & 1) or
        (((b >> ((t-1) % p)) & 1) != ((b >> ((t+1) % p)) & 1))
        for t in range(p))]


def background(p):
    return sum(1 << t for t in range(1, p, 3))


def prepare(p):
    words=all_temporal_columns(p)
    mask=(1<<p)-1
    q=[(((b>>1)|((b&1)<<(p-1))) ^ (((b<<1)&mask)|(b>>(p-1)))) for b in words]
    idx={w:i for i,w in enumerate(words)}
    return words,mask,q,idx


def edge(p, words, mask, q, a, b, c):
    # Complete Wolfram-115 truth table reduces to 1+b+a*b*(1+c) over F_2.
    x,y,z=words[a],words[b],words[c]
    return q[b]==(mask^y^(x&y&(mask^z)))


def edge_from_table(p, words, q, a, b, c):
    x,y,z=words[a],words[b],words[c]
    f=0
    for t in range(p):
        triple=4*((x>>t)&1)+2*((y>>t)&1)+((z>>t)&1)
        f|=((RULE>>triple)&1)<<t
    return q[b]==f


def brute_root_reachability(p, words, mask, q, idx, backwards):
    """Enumerate every possible next temporal column; no pruning heuristic."""
    start=(idx[background(p)],)*2
    visited={start}
    pending=deque([start])
    traversed=0
    while pending:
        u,v=pending.popleft()
        for w in range(len(words)):
            good=(edge(p,words,mask,q,w,u,v) if backwards
                  else edge(p,words,mask,q,u,v,w))
            if good:
                traversed+=1
                nxt=(w,u) if backwards else (v,w)
                if nxt not in visited:
                    visited.add(nxt)
                    pending.append(nxt)
    return visited,traversed


def bitset_root_reachability(p, words, mask, q, idx, backwards):
    """Independent candidate construction by necessary-and-sufficient bit masks."""
    n=len(words)
    allmask=(1<<n)-1
    ones=[0]*p
    for j,w in enumerate(words):
        for t in range(p):
            if (w>>t)&1:
                ones[t]|=1<<j
    zeros=[allmask^v for v in ones]
    def choices(needone,needzero):
        eligible=allmask
        while needone and eligible:
            bit=needone & -needone
            eligible &= ones[bit.bit_length()-1]
            needone-=bit
        while needzero and eligible:
            bit=needzero & -needzero
            eligible &= zeros[bit.bit_length()-1]
            needzero-=bit
        return eligible
    start=(idx[background(p)],)*2
    seen={start};todo=deque([start]);total=0
    while todo:
        u,v=todo.popleft()
        if backwards:
            b,c=words[u],words[v]
            Q=q[u]
            if b&Q&c:
                continue
            needone=b&Q
            needzero=b&(~Q)&(~c)&mask
        else:
            a,b=words[u],words[v]
            Q=q[v]
            if b&Q&(~a)&mask:
                continue
            needone=a&b&(~Q)&mask
            needzero=a&b&Q
        cand=choices(needone,needzero)
        while cand:
            bit=cand&-cand
            w=bit.bit_length()-1
            cand-=bit
            total+=1
            nxt=(w,u) if backwards else (v,w)
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return seen,total


def component(p):
    words,mask,q,idx=prepare(p)
    # The ANF reduction is checked against every one of the eight rule entries.
    for a in (0,1):
        for b in (0,1):
            for c in (0,1):
                assert ((RULE>>(4*a+2*b+c))&1)==(1^b^(a&b&(1^c)))
    if p==9:
        # Independent truth-table method verifies the complete small graph.
        assert all(edge(p,words,mask,q,a,b,c)==edge_from_table(p,words,q,a,b,c)
                   for a in range(len(words)) for b in range(len(words))
                   for c in range(len(words)))
    out,oe=brute_root_reachability(p,words,mask,q,idx,False)
    incoming,ie=brute_root_reachability(p,words,mask,q,idx,True)
    # Second construction checks that every traversed edge, including inverse
    # branches, was discovered and that the reachability sets are complete.
    out2,oe2=bitset_root_reachability(p,words,mask,q,idx,False)
    in2,ie2=bitset_root_reachability(p,words,mask,q,idx,True)
    assert out==out2 and incoming==in2 and (oe,ie)==(oe2,ie2)
    stats=(len(words),len(out),oe,len(incoming),ie,len(out&incoming),
           len({words[j] for v in out&incoming for j in v}))
    expected={3:(4,4,7,9,21,3,2),
              6:(10,46,121,45,159,27,10),
              9:(31,40,52,63,102,3,2),
              18:(973,5500,8590,8235,17484,27,10)}
    assert stats==expected[p],(p,stats)
    print('period',p,'stats',stats)
    return {(words[a],words[b]) for a,b in out&incoming}


def lift(w,small,big):
    return sum(w<<(k*small) for k in range(big//small))


def check_witness(p, exceptional):
    B=background(p);mask=(1<<p)-1
    def f(x,y,z):return mask^y^(x&y&(mask^z))
    def sh(v):return (((v>>1)|((v&1)<<(p-1)))^
                     (((v<<1)&mask)|(v>>(p-1))))
    for i in range(min(exceptional)-2,max(exceptional)+3):
        a=exceptional.get(i-1,B)
        b=exceptional.get(i,B)
        c=exceptional.get(i+1,B)
        assert sh(b)==f(a,b,c)


if __name__=='__main__':
    C3=component(3)
    C6=component(6)
    C9=component(9)
    C18=component(18)
    assert C9=={(lift(a,3,9),lift(b,3,9)) for a,b in C3}
    assert C18=={(lift(a,6,18),lift(b,6,18)) for a,b in C6}
    check_witness(3,{0:7})   # old/current both have a lone occupied site
    check_witness(6,{0:30,1:9,2:15}) # old empty, current two adjacent ones
    print('VERIFIED: no primitive finite-support period 9 or 18')
