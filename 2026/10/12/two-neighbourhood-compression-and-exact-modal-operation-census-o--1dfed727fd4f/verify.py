#!/usr/bin/env python3
"""Independent finite sanity checks for chain constructive-neighbourhood signatures.
No external dependencies.  Run: python3 verify.py
"""
from itertools import combinations, product
from collections import defaultdict
from math import comb
from random import Random

def subsets(n):
    w = list(range(n))
    return [frozenset(c) for k in range(n+1) for c in combinations(w,k)]

def families(n):
    ss = subsets(n)
    return [tuple(ss[i] for i in range(len(ss)) if bits>>i&1)
            for bits in range(1<<len(ss))]

def local_truth(fam, n, t):
    upset = set(range(t,n))
    box = any(a.issubset(upset) for a in fam)
    diamond = all(bool(a & upset) for a in fam)
    return box,diamond

def signature(fam, n):
    bt = [t for t in range(n+1) if local_truth(fam,n,t)[0]]
    dt = [t for t in range(n+1) if local_truth(fam,n,t)[1]]
    return max(bt,default=-1),max(dt,default=-1)

def local_states(n):
    return {(-1,n),(n,-1)} | set(product(range(n),repeat=2))

def compress(state,n):
    b,d=state
    if (b,d)==(-1,n): return tuple()
    if (b,d)==(n,-1): return (frozenset(),)
    if b<=d: return (frozenset(range(b,d+1)),)
    return (frozenset((b,)),frozenset((d,)))

def sig_frame(fams,n):
    s=[signature(f,n) for f in fams]
    return tuple((min(s[j][0] for j in range(i,n)),
                  min(s[j][1] for j in range(i,n))) for i in range(n))

def continual(states,n):
    return all(states[i] == (-1,n) or states[j] != (-1,n)
               for i in range(n) for j in range(i,n))

def count_dp(n):
    positive=local_states(n)-{(-1,n)}
    dp={s:1 for s in positive}
    f=[0,sum(dp.values())]
    for m in range(2,n+1):
        nd=defaultdict(int)
        for q,num in dp.items():
            for p in {(min(x,q[0]),min(y,q[1])) for (x,y) in positive}:
                nd[p]+=num
        dp=dict(nd)
        f.append(sum(dp.values()))
    return 1+sum(f[1:]),f[1:]

def closed_count(n):
    terms=[]
    for m in range(1,n+1):
        c=comb(n+m-1,m)
        h=comb(n+m-1,m-1)
        terms.append(c*c+comb(n+m-2,m-1)*(h-1)+h)
    return 1+sum(terms),terms

def force(form,fams,val,n):
    kind=form[0]
    if kind=='p': return set(val[form[1]])
    if kind=='bottom': return set()
    if kind=='and': return force(form[1],fams,val,n)&force(form[2],fams,val,n)
    if kind=='or': return force(form[1],fams,val,n)|force(form[2],fams,val,n)
    if kind=='imp':
        a=force(form[1],fams,val,n);b=force(form[2],fams,val,n)
        return {i for i in range(n) if all(j not in a or j in b for j in range(i,n))}
    a=force(form[1],fams,val,n)
    ans=set()
    for i in range(n):
        if kind=='box':
            ok=all(any(s<=a for s in fams[j]) for j in range(i,n))
        else:
            ok=all(all(bool(s & a) for s in fams[j]) for j in range(i,n))
        if ok:ans.add(i)
    return ans

def rnd_formula(rng,depth):
    if depth==0 or rng.randrange(5)==0:
        return ('p',rng.randrange(2)) if rng.randrange(3) else ('bottom',)
    op=rng.choice(['and','or','imp','box','diamond'])
    return (op,rnd_formula(rng,depth-1)) if op in ('box','diamond') else (op,rnd_formula(rng,depth-1),rnd_formula(rng,depth-1))

def run():
    rng=Random(190713)
    for n in range(1,4):
        observed=set()
        for fam in families(n):
            s=signature(fam,n)
            observed.add(s)
            canon=compress(s,n)
            assert len(canon)<=2 and signature(canon,n)==s
            for t in range(n+1):
                assert local_truth(canon,n,t)==local_truth(fam,n,t)
        assert observed==local_states(n), (n,observed,local_states(n))
        print('LOCAL_OK',n,len(observed),len(families(n)))
    for n in range(1,5):
        states=local_states(n)
        profiles={sig_frame([compress(s,n) for s in word],n)
                  for word in product(states,repeat=n) if continual(word,n)}
        total,subtotal=count_dp(n)
        assert len(profiles)==total,(n,len(profiles),total)
        print('PROFILE_OK',n,total,subtotal)
    tests=0
    for n in range(1,5):
        ss=subsets(n)
        for _ in range(1200):
            k=rng.randrange(n+1)
            fams=[tuple() if i<k else tuple(s for s in ss if rng.randrange(2)) for i in range(n)]
            # The random nonempty segment needs nonempty families at all its worlds.
            for i in range(k,n):
                if not fams[i]:fams[i]=(ss[rng.randrange(len(ss))],)
            canon=[compress(signature(f,n),n) for f in fams]
            val=[set(range(rng.randrange(n+1),n)) for _ in range(2)]
            form=rnd_formula(rng,4)
            assert force(form,fams,val,n)==force(form,canon,val,n)
            tests+=1
    print('NESTED_OK',tests)
    for n in range(1,9):
        assert count_dp(n)==closed_count(n)
        print('COUNT',n,*count_dp(n))
    print('VERIFY_OK')
if __name__=='__main__': run()
