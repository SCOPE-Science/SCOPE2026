#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, permutations
from collections import Counter, defaultdict
import hashlib


def compositions_pos(total, s):
    if s == 1:
        yield (total,)
        return
    for bars in combinations(range(1,total), s-1):
        prev=0; out=[]
        for b in bars+(total,):
            out.append(b-prev); prev=b
        yield tuple(out)


def hamilton_fraction(pop,h):
    P=sum(pop)
    qs=[Fraction(h*x,P) for x in pop]
    fl=[q.numerator//q.denominator for q in qs]
    left=h-sum(fl)
    rem=[qs[i]-fl[i] for i in range(len(pop))]
    order=sorted(range(len(pop)),key=lambda i: rem[i],reverse=True)
    if left and left < len(pop) and rem[order[left-1]]==rem[order[left]]:
        return None
    a=fl[:]
    for i in order[:left]: a[i]+=1
    return tuple(a)


def hamilton_integer(pop,h):
    P=sum(pop)
    fl=[(h*x)//P for x in pop]
    res=[(h*x)%P for x in pop]
    left=h-sum(fl)
    order=sorted(range(len(pop)),key=lambda i:res[i],reverse=True)
    if left and left < len(pop) and res[order[left-1]]==res[order[left]]:
        return None
    a=fl[:]
    for i in order[:left]: a[i]+=1
    return tuple(a)


def events(old,new,h=2):
    ao=hamilton_fraction(old,h); an=hamilton_fraction(new,h)
    assert ao==hamilton_integer(old,h)
    assert an==hamilton_integer(new,h)
    if ao is None or an is None: return ()
    out=[]
    for i in range(len(old)):
        if an[i]>=ao[i]: continue
        for j in range(len(old)):
            if an[j]<=ao[j]: continue
            if Fraction(new[i],old[i]) > Fraction(new[j],old[j]):
                out.append((i,j))
    return tuple(out)


def relabel_pair(old,new,sigma):
    ro=[0]*3; rn=[0]*3
    for i in range(3):
        ro[sigma[i]]=old[i]; rn[sigma[i]]=new[i]
    return tuple(ro),tuple(rn)


def canonical(old,new):
    return min(relabel_pair(old,new,s) for s in permutations(range(3)))

# Precompute every positive 3-state census through total 43; larger totals cannot occur
# in a two-census pair whose combined total is at most 46.
profiles={}
for total in range(3,44):
    L=[]
    for p in compositions_pos(total,3):
        a=hamilton_fraction(p,2)
        assert a==hamilton_integer(p,2)
        L.append((p,a))
    profiles[total]=L

bad=[]
counts=Counter()
for combined in range(6,47):
    for t0 in range(3,combined-2):
        t1=combined-t0
        if t1<3 or t1< t0: # all populations nondecrease coordinatewise => total cannot fall
            continue
        for old,ao in profiles[t0]:
            if ao is None: continue
            for new,an in profiles[t1]:
                if an is None: continue
                if new[0]<old[0] or new[1]<old[1] or new[2]<old[2]:
                    continue
                ev=[]
                for i in range(3):
                    if an[i]>=ao[i]: continue
                    for j in range(3):
                        if an[j]<=ao[j]: continue
                        if new[i]*old[j] > new[j]*old[i]:
                            ev.append((i,j))
                if ev:
                    bad.append((old,new,tuple(ev)))
                    counts[combined]+=1

assert sum(counts[t] for t in range(6,46))==0
assert counts[46]==6
bad46=[x for x in bad if sum(x[0])+sum(x[1])==46]
assert len(bad46)==6

orbits=Counter(canonical(o,n) for o,n,_ in bad46)
assert len(orbits)==1
assert Counter(orbits.values())==Counter({6:1})
rep=((1,4,14),(4,5,18))
assert set(orbits)=={rep}
assert hamilton_fraction(rep[0],2)==(0,0,2)
assert hamilton_fraction(rep[1],2)==(0,1,1)
assert events(rep[0],rep[1],2)==((2,1),)
assert Fraction(18,14) > Fraction(5,4)
assert all(len(ev)==1 for _,_,ev in bad46)

# Extra finite cross-checks for the analytic safe boundaries.
# h=1 on up to six states and modest totals; s=2 on a wide range of h and totals.
for s in range(2,7):
    for total in range(s,min(22,s+12)):
        for p in compositions_pos(total,s):
            assert hamilton_fraction(p,1)==hamilton_integer(p,1)
for h in range(1,21):
    for total in range(2,41):
        for p in compositions_pos(total,2):
            assert hamilton_fraction(p,h)==hamilton_integer(p,h)

digest=hashlib.sha256("\n".join(f"{o}|{n}" for o,n,_ in sorted(bad46)).encode('ascii')).hexdigest()
print('VERIFY_OK')
print('minimal_combined_total',46)
print('labeled_minimal_pairs',6)
print('candidate_relabel_classes',1)
print('orbit_size_hist',{6:1})
print('canonical_representative',rep)
print('old_allocation',hamilton_fraction(rep[0],2))
print('new_allocation',hamilton_fraction(rep[1],2))
print('loser_growth','9/7')
print('gainer_growth','5/4')
print('minimal_pair_set_sha256',digest)
