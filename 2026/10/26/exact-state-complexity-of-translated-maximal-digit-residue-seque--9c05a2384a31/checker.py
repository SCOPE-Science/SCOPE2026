#!/usr/bin/env python3
"""Exact-arithmetic checks for translated maximal-digit residue automata."""
from collections import deque
import random

def digit_count(n, base):
    assert n>=0
    ans=0
    while n:
        ans += int(n%base==base-1)
        n//=base
    return ans

def interval_residues(lo, hi, length, base, mod):
    """Digit DP returning residues attained on the interval [lo,hi)."""
    if hi<=lo: return set()
    assert 0<=lo<hi<=base**length
    low=[];high=[]
    val=hi-1
    for _ in range(length):
        low.append(lo%base);lo//=base
        high.append(val%base);val//=base
    states={(1,1,0)}
    for index in range(length-1,-1,-1):
        nexts=set()
        for lt,ut,res in states:
            for d in range(base):
                if lt and d<low[index]:continue
                if ut and d>high[index]:continue
                nexts.add((int(lt and d==low[index]),int(ut and d==high[index]),(res+(d==base-1))%mod))
        states=nexts
    return {z for _,_,z in states}

def exact_formula(c,base,mod):
    assert base>=3 and mod>=2 and c>=0
    if c==0:return mod
    h=1;d=0
    while base**d<=c:d+=1
    total=mod+len(interval_residues(0,c,d,base,mod))
    j=0
    while h<=c:
        q,r=divmod(c,h)
        if q>=2:
            total+=len(interval_residues(r,h,j,base,mod))
        if q>=1 and r:
            total+=len(interval_residues(0,r,j,base,mod))
        j+=1;h*=base
    return total

def build(c,base,mod):
    seen={(c,0)};queue=deque([(c,0)]);trans={}
    while queue:
        t,a=queue.popleft()
        successors=[]
        for d in range(base):
            z=t+d
            child=(z//base,(a+int(z%base==base-1))%mod)
            successors.append(child)
            if child not in seen:
                seen.add(child);queue.append(child)
        trans[t,a]=tuple(successors)
    return trans

def minimize(trans,base,mod):
    def output(s):
        t,a=s
        return int((a+digit_count(t,base))%mod==0)
    parts={s:output(s) for s in trans}
    while True:
        signatures={s:(parts[s],*(parts[nxt] for nxt in trans[s])) for s in trans}
        lookup={sig:i for i,sig in enumerate(sorted(set(signatures.values())))}
        new={s:lookup[signatures[s]] for s in trans}
        groups_old={frozenset(s for s in trans if parts[s]==i) for i in set(parts.values())}
        groups_new={frozenset(s for s in trans if new[s]==i) for i in set(new.values())}
        if groups_old==groups_new:return len(groups_new)
        parts=new

def test():
    tests=0
    for base in range(3,7):
        for mod in range(2,6):
            for c in range(0,240):
                tr=build(c,base,mod)
                formula=exact_formula(c,base,mod)
                mini=minimize(tr,base,mod)
                assert formula==mini==len(tr),(base,mod,c,formula,mini,len(tr))
                tests+=1
            for r in range(0,9):
                c=base**r
                assert exact_formula(c,base,mod)==mod+sum(min(mod,j+1) for j in range(r+1))
                if r>=mod:
                    assert exact_formula(c-1,base,mod)-exact_formula(c,base,mod)==r-mod
    rng=random.Random(20261019)
    for i in range(300):
        base=rng.choice((3,4,5,7,10))
        mod=rng.randrange(2,9)
        c=rng.randrange(0,10**10)
        tr=build(c,base,mod)
        assert len(tr)==minimize(tr,base,mod)==exact_formula(c,base,mod),(base,mod,c)
    direct=0
    for base,mod in ((3,2),(4,3),(5,4),(6,5)):
        for c in range(0,50):
            tr=build(c,base,mod)
            for n in range(0,200):
                state=(c,0)
                nn=n
                while nn:
                    state=tr[state][nn%base]
                    nn//=base
                t,a=state
                actual=int((a+digit_count(t,base))%mod==0)
                expected=int(digit_count(n+c,base)%mod==0)
                assert actual==expected,(base,mod,c,n)
                direct+=1
    print('all pass; exhaustive parameter/minimization checks',tests)
    print('all pass; random parameter/minimization checks',300)
    print('all pass; direct outputs',direct)
    print('all pass; dyadic-analogue and boundary-jump checks')
    print('sample base4 modulus3:')
    for r in range(2,9):
        print(r, exact_formula(4**r-1,4,3),exact_formula(4**r,4,3))

if __name__=='__main__':test()
