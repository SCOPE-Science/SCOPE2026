#!/usr/bin/env python3
"""Exact integer tests for a signed complete-network opinion update."""
import itertools,random
from fractions import Fraction

def neg_from_mask(n,mask):
    return [(i,j) for k,(i,j) in enumerate(itertools.combinations(range(n),2)) if mask>>k&1]

def score(v,negative):
    z=[0]*len(v)
    for i,j in negative:
        s=1 if v[i]>v[j] or (v[i]==v[j] and i>j) else -1
        z[i]+=s;z[j]-=s
    return tuple(z)

def potential_integer(v,negative):
    return 2*sum(abs(v[i]-v[j]) for i,j in negative)-sum(t*t for t in v)

def source_update_full(x, negative, c):
    """Directly implement the signed self-inclusive averaging formula for full reception."""
    n=len(x)
    neg=set(negative)
    ans=[]
    for i in range(n):
        increment=Fraction(0)
        for j in range(n):
            if i==j:continue
            a,b=sorted((i,j))
            diff=x[j]-x[i]
            if (a,b) in neg:
                sij=1 if diff>0 or (diff==0 and j>i) else -1
                increment += diff - c*sij
            else:
                increment += diff
        ans.append(x[i]+increment/n)
    return tuple(ans)

def run():
    checks=0;converged=0;sharp=0;max_steps=0;example=None
    for n in range(2,6):
        pairs=list(itertools.combinations(range(n),2))
        for mask in range(1<<len(pairs)):
            neg=neg_from_mask(n,mask)
            degrees=[sum(i in e for e in neg) for i in range(n)]
            high=sorted(degrees,reverse=True)
            threshold=high[0]+high[1]<n
            rupture_seen=False
            for ordering in itertools.permutations(range(n)):
                x=score(ordering,neg)
                reception=max(x)-min(x)<n
                if not reception: rupture_seen=True
                if threshold!=reception and threshold:
                    raise AssertionError(('false preservation',n,mask,ordering))
                if threshold:
                    states={};steps=1
                    while True:
                        y=score(x,neg)
                        assert max(y)-min(y)<n
                        change=sum((a-b)**2 for a,b in zip(x,y))
                        increment=potential_integer(y,neg)-potential_integer(x,neg)
                        assert increment>=change,(n,mask,ordering,x,y,increment,change)
                        checks+=3
                        if y==x:
                            converged+=1
                            max_steps=max(max_steps,steps)
                            if steps>2 and example is None:
                                example=(n,tuple(neg),ordering,steps,y)
                            break
                        assert y not in states,(n,mask,ordering,steps)
                        states[y]=True
                        x=y;steps+=1
                        assert steps<=1<<len(neg)
                checks+=1
            if not threshold:
                assert rupture_seen,(n,mask)
                sharp+=1
                checks+=1
    # additional deterministic random instances, n=6,7,8
    rng=random.Random(61028)
    sample_checks=0
    for n in range(6,9):
        for _ in range(2000):
            pairs=list(itertools.combinations(range(n),2))
            neg=[e for e in pairs if rng.randrange(2)]
            deg=[sum(i in e for e in neg) for i in range(n)]
            ordering=list(range(n));rng.shuffle(ordering)
            x=score(ordering,neg)
            safe=sum(sorted(deg,reverse=True)[:2])<n
            if safe:
                assert max(x)-min(x)<n
                old=set()
                for t in range(1,100):
                    y=score(x,neg)
                    assert max(y)-min(y)<n
                    assert potential_integer(y,neg)-potential_integer(x,neg)>=sum((a-b)**2 for a,b in zip(x,y))
                    sample_checks+=2
                    if y==x:break
                    assert y not in old
                    old.add(y);x=y
                else:raise AssertionError(('not fixed',n,neg))
            sample_checks+=1
    direct_checks=0
    rng=random.Random(20230105)
    for n in range(2,9):
        pairs=list(itertools.combinations(range(n),2))
        for _ in range(400):
            neg=[e for e in pairs if rng.randrange(2)]
            c=Fraction(rng.randint(1,8),rng.randint(1,8))
            x=tuple(Fraction(rng.randint(-5,5),12)*c for i in range(n))
            assert max(x)-min(x)<c
            y=source_update_full(x,neg,c)
            mean=sum(x)/n
            predicted=tuple(mean+Fraction(c*s,n) for s in score(x,neg))
            assert y==predicted,(n,neg,x,y,predicted)
            direct_checks+=1
    # Explicit multi-step polarization within the degree-preserving class.
    h=[(0,2),(0,4),(0,5),(1,2),(1,5),(2,3),(3,5),(3,6)]
    x=(4,0,6,3,5,2,1)
    expected=[(-1,-2,3,1,1,-1,-1),(-3,-2,3,1,1,1,-1),
              (-3,-2,3,-1,1,3,-1),(-3,-2,3,-3,1,3,1)]
    for nxt in expected:
        x=score(x,h)
        assert x==nxt
    assert score(x,h)==x
    # Boundary equality produces immediate loss of full receptivity.
    star=[(0,i) for i in range(1,5)]
    initial=(4,0,1,2,3)
    z=score(initial,star)
    assert max(z)-min(z)==5
    print(f'DIRECT_UPDATE_OK cases={direct_checks}')
    print(f'EXACT_OK exhaust_checks={checks} qualifying_orders={converged} nonqualifying_signings={sharp} max_exact_updates_after_initial={max_steps} random_checks={sample_checks}')
    print('example',example)
if __name__=='__main__':run()
