"""Exact finite-state induction certificate for upper-domination extrema of 2- and 3-row grids.
Run with Python 3.10+: python verify.py . No external packages are required.
"""
from collections import defaultdict
from functools import lru_cache
import hashlib, json

NIL = -1


def machine(h):
    alphabet=tuple(range(1<<h))
    @lru_cache(None)
    def good(word):
        a,b,c,d,e = word
        if c==NIL:
            return True
        def chosen(t,r):
            return 0<=t<5 and word[t]!=NIL and bool(word[t] & (1<<r))
        for r in range(h):
            near=[(2,r)]
            if r>0:near.append((2,r-1))
            if r+1<h:near.append((2,r+1))
            near += [(1,r),(3,r)]
            if not any(chosen(t,k) for t,k in near):return False
            if chosen(2,r):
                witness=False
                for t,j in near:
                    if word[t]==NIL:continue
                    block=[(t,j)]
                    if j>0:block.append((t,j-1))
                    if j+1<h:block.append((t,j+1))
                    block += [(t-1,j),(t+1,j)]
                    if sum(chosen(s,k) for s,k in block)==1:
                        witness=True
                        break
                if not witness:return False
        return True
    def step(prev, alphabet_to_add):
        nxt={}
        for (a,b,c,d),(weight,count) in prev.items():
            for v in alphabet_to_add:
                if c!=NIL and not good((a,b,c,d,v)):continue
                state=(b,c,d,v)
                newweight=weight+(v.bit_count() if v!=NIL else 0)
                if state not in nxt or newweight>nxt[state][0]:
                    nxt[state]=(newweight,count)
                elif newweight==nxt[state][0]:
                    nxt[state]=(newweight,nxt[state][1]+count)
        return nxt
    def finish(prev):
        for _ in range(2):prev=step(prev,(NIL,))
        assert prev
        best=max(w for w,c in prev.values())
        return best,sum(c for w,c in prev.values() if w==best)
    return alphabet,step,finish


def allword_check(h,n,words):
    present={(i,r) for i,w in enumerate(words) for r in range(h) if w>>r&1}
    neighbors={}
    for i in range(n):
        for r in range(h):
            v=(i,r)
            neighbors[v]={v}
            for j,k in ((i-1,r),(i+1,r),(i,r-1),(i,r+1)):
                if 0<=j<n and 0<=k<h:neighbors[v].add((j,k))
    return (all(neighbors[v]&present for v in neighbors) and
            all(any((neighbors[v]&present)=={u} for v in neighbors[u]) for u in present))


def simple_candidates(h,n):
    ans=[]
    # Both chessboard parities; when the board has odd cardinality, only the larger parity.
    for p in (0,1):
        s={ (i,r) for i in range(n) for r in range(h) if (i+r)%2==p}
        if len(s)==(h*n+1)//2:ans.append(s)
    if h==2:
        ans.extend([{(i,r) for i in range(n)} for r in range(h)])
    if n%2==0:
        for p in (0,1):
            ans.append({(i,r) for i in range(n) for r in range(h) if (i%4 in ((0,3) if p==0 else (1,2)))})
    return ans


def enumerate_direct(h,n):
    N=h*n
    closed=[]
    for i in range(n):
        for r in range(h):
            b=1<<(h*i+r)
            for j,k in ((i-1,r),(i+1,r),(i,r-1),(i,r+1)):
                if 0<=j<n and 0<=k<h:b|=1<<(h*j+k)
            closed.append(b)
    goal=(N+1)//2
    ans=0
    for mask in range(1<<N):
        if mask.bit_count()!=goal:continue
        if any(not mask&C for C in closed):continue
        if any(not any(((C&mask)==(1<<v)) for C in closed) for v in range(N) if mask>>v&1):continue
        ans+=1
    return ans


def proof(h,seed):
    alphabet,step,finish=machine(h)
    curr={(NIL,NIL,NIL,NIL):(0,1)}
    history={}
    for n in range(1,seed+12):
        curr=step(curr,alphabet)
        history[n]=curr
        expected=(4+2*(n%2==0) if h==2 and n>=2 else
                  1 if h==3 and n%2 else 4 if h==3 else 2)
        actual=finish(curr)
        assert actual==((h*n+1)//2,expected),(h,n,actual,expected)
    a=history[seed];b=history[seed+4];c=history[seed+8]
    assert a.keys()==b.keys()==c.keys()
    for s in a:
        assert b[s][0]==a[s][0]+2*h
        assert c[s][0]==a[s][0]+4*h
        assert c[s][1]-2*b[s][1]+a[s][1]==0
    # Four applications of 'step' define an eventually periodic max-plus transition.
    # With identical optimal transition matrices, T(c1-c0)=c2-c1=c1-c0.
    # Therefore counts for each state follow c_{seed+4q}=c_seed+q(c_{seed+4}-c_seed)
    # for every q>=0.  Applying up to three real steps and two terminal NIL
    # steps preserves linearity in q, because the maximizing paths depend only
    # on the translated state-score vector.  The terminal slope is zero in
    # each of the four residue classes, as certified by equal finish counts.
    for r in range(4):
        assert finish(history[seed+r])[1]==finish(history[seed+r+4])[1]
    for n in range(2,min(9,seed)):
        candidates=simple_candidates(h,n)
        assert len({frozenset(x) for x in candidates})==len(candidates)
        assert all(len(s)==(h*n+1)//2 for s in candidates)
        assert all(allword_check(h,n,[sum(1<<r for r in range(h) if (i,r) in s) for i in range(n)]) for s in candidates)
        assert enumerate_direct(h,n)==len(candidates)
    signature=hashlib.sha256(json.dumps(sorted((list(s),w,c) for s,(w,c) in a.items()),separators=(',',':')).encode()).hexdigest()
    return {'height':h,'seed':seed,'states':len(a),'weights_period_four_increment':2*h,
            'max_weight_at_seed':finish(a)[0],'count_at_seed':finish(a)[1],
            'vector_sha256_at_seed':signature, 'small_exhaustive_up_to_n':min(8,seed-1)}

if __name__=='__main__':
    for h,seed in ((2,12),(3,16)):
        out=proof(h,seed)
        print(json.dumps(out,sort_keys=True))
    print('VERIFY_OK')
