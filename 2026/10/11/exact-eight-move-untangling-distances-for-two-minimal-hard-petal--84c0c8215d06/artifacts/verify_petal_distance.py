#!/usr/bin/env python3
from functools import lru_cache

ALPHA=(0,2,4,1,5,7,3,8,6)
BETA=(0,2,5,3,8,1,7,4,6)
TRIV=(0,)
ALPHA_PATH=[
(0,2,4,1,5,7,3,8,6),
(0,2,4,1,7,9,3,5,6,10,8),
(0,2,4,1,6,10,3,5,7,9,8),
(0,2,4,1,6,8,3,5,7),
(0,7,8,3,5,6,1,2,4),
(0,3,5,6,1,2,4),
(0,3,1,2,4),
(0,1,2),
(0,)]
BETA_PATH=[
(0,2,5,3,8,1,7,4,6),
(0,2,6,7,5,3,10,1,9,4,8),
(0,2,6,8,4,3,10,1,9,5,7),
(0,2,4,6,8,1,7,3,5),
(0,2,3,7,8,1,6,4,5),
(0,5,6,1,4,2,3),
(0,1,4,2,3),
(0,1,2),
(0,)]
PATH_TYPES=('+','x','-','x','-','-','-','-')

def cyc(p):
    p=tuple(p); return min(p[i:]+p[:i] for i in range(len(p)))

def rot(p,k):
    n=len(p); return tuple((v+k)%n for v in p)

def halfturn(p):
    n=len(p); return tuple(n-1-v for v in p[::-1])

@lru_cache(None)
def sym_orbit(p):
    p=tuple(p); n=len(p); out=set()
    for k in range(n):
        q=rot(p,k)
        out.add(cyc(q)); out.add(cyc(halfturn(q)))
    return tuple(sorted(out))

def symcanon(p): return min(sym_orbit(tuple(p)))

def tplus(p):
    n=len(p); out=set()
    for j in range(n):
        for m in range(n+1):
            q=tuple(v if v<m else v+2 for v in p)
            for pair in ((m,m+1),(m+1,m)):
                out.add(cyc(q[:j+1]+pair+q[j+1:]))
    return out

def tminus(p):
    n=len(p); out=set()
    if n<=1: return out
    for j in range(n):
        q=p[j:]+p[:j]
        if abs(q[0]-q[1])!=1: continue
        m=min(q[0],q[1])
        out.add(cyc(tuple(v if v<m else v-2 for v in q[2:])))
    return out

def xmove(p):
    n=len(p); out=set()
    if n<5: return out
    for b in range(n):
        pairs=[]
        for r in range((n-1)//2):
            i=(b+1+2*r)%n; j=(b+2+2*r)%n
            pairs.append(frozenset((p[i],p[j])))
        for m in range(n):
            for w in range(m+2,n-1):
                A=frozenset((m,w+1)); B=frozenset((m+1,w))
                if A not in pairs or B not in pairs: continue
                ia=pairs.index(A); ib=pairs.index(B)
                if ia==ib: continue
                interval=set(range(m+2,w))
                ok=True
                for idx,P in enumerate(pairs):
                    if idx in (ia,ib): continue
                    if P & interval and not P <= interval:
                        ok=False; break
                if ok:
                    trans={m:m+1,m+1:m,w:w+1,w+1:w}
                    out.add(cyc(tuple(trans.get(v,v) for v in p)))
    return out

def raw_neighbors(p,typ):
    return tplus(p) if typ=='+' else tminus(p) if typ=='-' else xmove(p)

@lru_cache(None)
def relaxed_neighbors(state,typ):
    out=set()
    for rep in sym_orbit(state):
        for q in raw_neighbors(rep,typ): out.add(symcanon(q))
    return tuple(sorted(out))

def check_path(path):
    assert len(path)==9
    for a,b,t in zip(path,path[1:],PATH_TYPES):
        assert cyc(b) in raw_neighbors(cyc(a),t), (a,b,t)
    assert path[-1]==TRIV

def exact_short_obstruction(start):
    # A path from 9 petals to 1 with <=7 counted moves satisfies
    # d-a=4 and length=2a+4+p. Hardness forces a>=1, hence a=1
    # and p<=1. We strengthen the search by charging R,S zero and
    # permitting at most one X. If even this relaxation cannot reach
    # the trivial word, no true path of length <=7 exists.
    states={(0,0,0):{symcanon(start)}}
    for total in range(1,8):
        for a in range(2):
            for d in range(6):
                for x in range(2):
                    if a+d+x!=total: continue
                    cur=set()
                    if a:
                        for s in states.get((a-1,d,x),()): cur.update(relaxed_neighbors(s,'+'))
                    if d:
                        for s in states.get((a,d-1,x),()): cur.update(relaxed_neighbors(s,'-'))
                    if x:
                        for s in states.get((a,d,x-1),()): cur.update(relaxed_neighbors(s,'x'))
                    states[(a,d,x)]=cur
    target=symcanon(TRIV)
    assert target not in states.get((1,5,0),set())
    assert target not in states.get((1,5,1),set())
    return {
      'after_one_addition':len(states[(1,0,0)]),
      'one_addition_one_deletion':len(states[(1,1,0)]),
      'one_addition_one_exchange':len(states[(1,0,1)]),
      'one_addition_one_deletion_one_exchange':len(states[(1,1,1)]),
      'one_addition_two_deletions':len(states[(1,2,0)]),
      'terminal_without_exchange':len(states[(1,5,0)]),
      'terminal_with_one_exchange':len(states[(1,5,1)]),
    }

check_path(ALPHA_PATH); check_path(BETA_PATH)
a=exact_short_obstruction(ALPHA)
b=exact_short_obstruction(BETA)
assert a['terminal_without_exchange']==a['terminal_with_one_exchange']==0
assert b['terminal_without_exchange']==b['terminal_with_one_exchange']==0
print('VERIFY_OK alpha_distance=8 beta_distance=8')
print('alpha_counts',a)
print('beta_counts',b)
