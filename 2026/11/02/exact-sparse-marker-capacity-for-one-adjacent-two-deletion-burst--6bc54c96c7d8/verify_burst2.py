#!/usr/bin/env python3
"""Standalone exact-two-consecutive-deletion verification for binary weight-two words.
Requires only Python standard library. Proof of the infinite theorem is in RESULT.md.
"""
from itertools import combinations
from functools import lru_cache

def parent_word(n, ij):
    i, j = ij
    return tuple(1 if k == i or k == j else 0 for k in range(n))

def ball(n, ij):
    x=parent_word(n, ij)
    return frozenset(x[:t]+x[t+2:] for t in range(n-1))

def make_code(n):
    if n == 2:
        return [(0,1)]
    m=n-2
    ans=[(0,1)]
    offset=1
    M=m-1
    q,r=divmod(M,4)
    for t in range(q):
        base=offset+4*t
        ans.extend([(base,base+2),(base+1,base+3),(base+2,base+5)])
    for s in range(min(r,2)):
        v=offset+4*q+s
        ans.append((v,v+2))
    return ans

def f(m):
    q,r=divmod(m,4)
    return 3*q+min(r,2)

def predicted_conflict(n,p,q):
    i,j=p; k,l=q
    m=n-2
    def markers(pair):
        a,b=pair
        if b-a>=2:
            return frozenset((a,b-2))
        s=[]
        if a>=1:s.append(a-1)
        if b<=n-2:s.append(a)
        return frozenset(s)
    if j==i+1 and l==k+1:return True
    if markers(p)&markers(q):return True
    if j==i+1 or l==k+1:return False
    ep=(i,j-2); eq=(k,l-2)
    return abs(ep[0]-eq[0])==2 and ep[1]-ep[0]==eq[1]-eq[0] and ep[0]-eq[0]==ep[1]-eq[1]

def exhaustive_optimum(n):
    words=list(combinations(range(n),2))
    balls=[ball(n,w) for w in words]
    G=[0]*len(words)
    for a in range(len(words)):
        for b in range(a+1,len(words)):
            if not balls[a].isdisjoint(balls[b]):
                G[a]|=1<<b
                G[b]|=1<<a
    calls=0
    @lru_cache(None)
    def mis(mask):
        nonlocal calls
        calls+=1
        if not mask:return 0
        # Branch on a maximum-degree vertex.
        tmp=mask; best=-1; bi=-1
        while tmp:
            b=tmp&-tmp; i=b.bit_length()-1; tmp-=b
            deg=(G[i]&mask).bit_count()
            if deg>best:best=deg;bi=i
        without=mask &~(1<<bi)
        return max(mis(without),1+mis(without &~G[bi]))
    return mis((1<<len(words))-1), calls

def main():
    pair_cases=0
    for n in range(2,21):
        words=list(combinations(range(n),2))
        bs={w:ball(n,w) for w in words}
        for a,p in enumerate(words):
            for q in words[a+1:]:
                assert (not bs[p].isdisjoint(bs[q]))==predicted_conflict(n,p,q), (n,p,q)
                pair_cases+=1
    count=0; maxsize=0
    for n in range(2,251):
        code=make_code(n)
        expect=1 if n==2 else 3*(n-1)//4
        assert len(code)==expect,(n,len(code),expect)
        assert len(code)==len(set(code))
        owners={}
        for p in code:
            assert 0<=p[0]<p[1]<n,(n,p)
            for y in ball(n,p):
                assert y not in owners,(n,p,owners.get(y),y)
                owners[y]=p
        count+=len(code); maxsize=max(maxsize,len(code))
    results=[]
    for n in range(2,11):
        val,calls=exhaustive_optimum(n)
        expected=1 if n==2 else 3*(n-1)//4
        assert val==expected,(n,val,expected)
        results.append((n,val,calls))
    for m in range(0,10001):
        l=( (m+1)//2 +1)//2+(m//2+1)//2
        assert (m+l)//2==f(m)
        if m>=1:assert max(f(m),1+f(m-1))==3*(m+1)//4
    print('VERIFY_OK', 'structural_pair_cases',pair_cases,'constructed_lengths',249,
      'total_constructed_words',count,'maximum_constructed_size',maxsize,
      'exhaustive_optima',results,'symbolic_residue_checks',10001)

if __name__=='__main__': main()
