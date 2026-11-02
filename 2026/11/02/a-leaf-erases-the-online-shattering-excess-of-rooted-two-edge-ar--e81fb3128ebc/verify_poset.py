#!/usr/bin/env python3
"""Independent direct poset-ideal enumeration and exact mistake-tree recurrence."""
from functools import lru_cache
from itertools import combinations

def poset(t,s):
    # order: root 0; t distinct root<a_i<b_i arms; s root<c_j leaves.
    n=1+2*t+s
    down=[1]
    for i in range(t):
        a,b=1+2*i,2+2*i
        down += [(1<<0)|(1<<a), (1<<0)|(1<<a)|(1<<b)]
    for j in range(s):
        x=1+2*t+j
        down.append(1|1<<x)
    assert len(down)==n
    return down

def ideals(down):
    n=len(down)
    return tuple(v for v in range(1<<n) if all(not(v>>x&1) or (v&down[x])==down[x] for x in range(n)))

def ldim(H,n):
    @lru_cache(None)
    def rec(state):
        best=0
        for i in range(n):
            a=tuple(h for h in state if h>>i&1)
            b=tuple(h for h in state if not h>>i&1)
            if a and b:
                best=max(best,1+min(rec(a),rec(b)))
        return best
    return rec(tuple(H))

def vcdim(H,n):
    best=0
    for k in range(n+1):
        for q in combinations(range(n),k):
            vals={tuple((h>>i)&1 for i in q) for h in H}
            if len(vals)==1<<k: best=max(best,k)
    return best

def expected(t,s):
    w=t+s if t+s else 1
    return w, t+s+int(s==0)

count=0
for t in range(5):
    for s in range(5):
        if 3**t*2**s>175: continue
        d=poset(t,s)
        H=ideals(d)
        assert len(H)==1+3**t*2**s,(t,s,len(H))
        vc=vcdim(H,len(d))
        ld=ldim(H,len(d))
        assert (vc,ld)==expected(t,s),(t,s,vc,ld,expected(t,s))
        count+=1
        print(f'POSET_DIRECT_PASS t={t} s={s} ideals={len(H)} VC={vc} Ldim={ld}')
print(f'POSET_ENUMERATION_ALL_PASS cases={count}')
