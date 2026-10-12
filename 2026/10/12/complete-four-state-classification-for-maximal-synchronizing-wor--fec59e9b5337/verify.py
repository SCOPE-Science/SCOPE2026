#!/usr/bin/env python3
from itertools import product, permutations
from collections import deque, Counter
from pathlib import Path
import json

N=4
FULL=(1<<N)-1

def image(mask,t):
    out=0
    for q in range(N):
        if mask>>q&1:
            out |= 1<<t[q]
    return out

# Engine A: construct the reachable subset automaton and minimize it by
# repeated partition refinement.
def sc_engine_A(a,b):
    letters=(a,b)
    reach=[FULL]
    seen={FULL}
    q=deque([FULL])
    while q:
        s=q.popleft()
        for t in letters:
            u=image(s,t)
            if u not in seen:
                seen.add(u); reach.append(u); q.append(u)
    P=[{s for s in reach if s.bit_count()!=1},
       {s for s in reach if s.bit_count()==1}]
    P=[B for B in P if B]
    while True:
        bid={s:i for i,B in enumerate(P) for s in B}
        new=[]
        changed=False
        for B in P:
            groups={}
            for s in B:
                sig=(bid[image(s,a)],bid[image(s,b)])
                groups.setdefault(sig,set()).add(s)
            new.extend(groups.values())
            if len(groups)>1: changed=True
        P=new
        if not changed:
            return len(P)

# Engine B: independently test the exact condition for maximal complexity:
# every non-singleton is reachable and every pair of reachable non-singletons
# is distinguishable with respect to eventual arrival in a singleton.
def maximal_engine_B(a,b):
    letters=(a,b)
    seen={FULL}
    q=deque([FULL])
    while q:
        s=q.popleft()
        for t in letters:
            u=image(s,t)
            if u not in seen:
                seen.add(u); q.append(u)
    nons=[s for s in range(1,1<<N) if s.bit_count()>=2]
    if any(s not in seen for s in nons):
        return False
    if not any(s.bit_count()==1 for s in seen):
        return False

    # Table-filling distinguishability on the full nonempty subset DFA.
    states=list(range(1,1<<N))
    marked=set()
    for i,x in enumerate(states):
        for y in states[i+1:]:
            if (x.bit_count()==1)!=(y.bit_count()==1):
                marked.add((min(x,y),max(x,y)))
    changed=True
    while changed:
        changed=False
        for i,x in enumerate(states):
            for y in states[i+1:]:
                p=(x,y)
                if p in marked: continue
                for t in letters:
                    u,v=image(x,t),image(y,t)
                    if u!=v and (min(u,v),max(u,v)) in marked:
                        marked.add(p); changed=True; break
    return all((min(x,y),max(x,y)) in marked
               for i,x in enumerate(nons) for y in nons[i+1:])

def is_cycle4(t):
    if len(set(t))!=4: return False
    q=0; seen=[]
    for _ in range(4):
        if q in seen: return False
        seen.append(q); q=t[q]
    return q==0 and len(seen)==4

def rank3_signature(a):
    if len(set(a))!=3: return None
    pre={}
    for q,x in enumerate(a):
        pre.setdefault(x,[]).append(q)
    double_image=next(x for x,v in pre.items() if len(v)==2)
    kernel=tuple(sorted(pre[double_image]))
    omitted=next(x for x in range(4) if x not in pre)
    return kernel,double_image,omitted

def antipodal(x,y):
    return (x-y)%4==2

def structural_good(a):
    sig=rank3_signature(a)
    if sig is None: return False
    kernel,double_image,omitted=sig
    bad=antipodal(*kernel) and antipodal(double_image,omitted)
    return not bad

def canonical_pair(a,b):
    best=None
    for p in permutations(range(4)):
        inv=[0]*4
        for i,x in enumerate(p): inv[x]=i
        def conj(t):
            return tuple(p[t[inv[q]]] for q in range(4))
        x,y=conj(a),conj(b)
        for pair in ((x,y),(y,x)):
            if best is None or pair<best: best=pair
    return best

dist=Counter()
maxpairs=[]
for vals in product(range(4),repeat=8):
    a=tuple(vals[:4]); b=tuple(vals[4:])
    sc=sc_engine_A(a,b)
    dist[sc]+=1
    mb=maximal_engine_B(a,b)
    assert mb==(sc==12),(a,b,sc,mb)
    if sc==12:
        maxpairs.append((a,b))
        # The complete classification says exactly one letter is a 4-cycle
        # and the other is rank 3.
        types=[is_cycle4(a),is_cycle4(b)]
        assert sum(types)==1
        singular=b if types[0] else a
        assert len(set(singular))==3

assert len(maxpairs)==1536
expected={1:14016,2:1552,3:11760,4:13392,5:9120,6:6096,7:2880,
          8:2592,9:1440,10:0,11:1152,12:1536}
for k in range(1,13):
    assert dist[k]==expected[k],(k,dist[k])

# Normalize the cycle and test the structural iff against the exact state
# complexity calculation for all 4^4 possible second letters.
cycle=(1,2,3,0)
rank3=good=bad=0
exceptions=[]
for a in product(range(4),repeat=4):
    sc=sc_engine_A(a,cycle)
    if len(set(a))==3:
        rank3+=1
        pred=structural_good(a)
        assert (sc==12)==pred,(a,sc,pred)
        if pred: good+=1
        else:
            bad+=1; exceptions.append(a)
    else:
        assert sc!=12
assert (rank3,good,bad)==(144,128,16)

# Count isomorphism classes under simultaneous state relabeling and letter swap.
classes={}
for a,b in maxpairs:
    c=canonical_pair(a,b)
    classes[c]=classes.get(c,0)+1
assert len(classes)==32
assert set(classes.values())=={48}

# Verify the source's published exceptional four-state example.
pub_a=(1,2,1,3)
assert sc_engine_A(pub_a,cycle)==12
sig=rank3_signature(pub_a)
assert sig==((0,2),1,0)
assert antipodal(0,2) and not antipodal(1,0)

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text())
assert cert["ordered_labeled_maximal_count"]==1536
assert cert["isomorphism_classes_mod_state_relabel_and_letter_swap"]==32
assert cert["normalized_maximal_rank3_maps"]==128
assert cert["normalized_nonmaximal_rank3_maps"]==16

print("VERIFY_OK total=65536 scmax=12 maximal=1536 classes=32 orbit48=32 "
      "normalized_rank3=144 good=128 exceptions=16 "
      "criterion=kernel-antipodal-and-image-antipodal engines=minimize+tablefill")
