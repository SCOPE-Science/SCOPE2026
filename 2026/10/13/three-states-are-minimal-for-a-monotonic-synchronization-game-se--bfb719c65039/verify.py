#!/usr/bin/env python3
from itertools import combinations_with_replacement, permutations
from collections import deque, Counter
import json
from pathlib import Path

def maps(n):
    return list(combinations_with_replacement(range(n), n))

def image(mask,t,n):
    out=0
    for q in range(n):
        if mask>>q & 1:
            out |= 1<<t[q]
    return out

def synchronizing(ts,n):
    start=(1<<n)-1
    seen={start}
    q=deque([start])
    while q:
        s=q.popleft()
        if s & (s-1)==0:
            return True
        for t in ts:
            u=image(s,t,n)
            if u not in seen:
                seen.add(u); q.append(u)
    return False

# Engine A: solve the game on all active subsets.
def alice_full(ts,n):
    masks=range(1,1<<n)
    W={(s,turn) for s in masks if s&(s-1)==0 for turn in (0,1)}
    changed=True
    while changed:
        changed=False
        for s in masks:
            if s&(s-1)==0:
                continue
            if (s,0) not in W and any((image(s,t,n),1) in W for t in ts):
                W.add((s,0)); changed=True
            if (s,1) not in W and all((image(s,t,n),0) in W for t in ts):
                W.add((s,1)); changed=True
    return (((1<<n)-1,0) in W)

# Engine B: use only endpoint pairs. For monotone maps this is equivalent,
# because every image of an interval's endpoints brackets the image of every
# intermediate state.
def alice_pairs(ts,n):
    pairs=[(i,j) for i in range(n) for j in range(i,n)]
    W={(i,j,turn) for i,j in pairs if i==j for turn in (0,1)}
    changed=True
    while changed:
        changed=False
        for i,j in pairs:
            if i==j:
                continue
            succ=[]
            for t in ts:
                x,y=t[i],t[j]
                if x>y: x,y=y,x
                succ.append((x,y))
            if (i,j,0) not in W and any((x,y,1) in W for x,y in succ):
                W.add((i,j,0)); changed=True
            if (i,j,1) not in W and all((x,y,0) in W for x,y in succ):
                W.add((i,j,1)); changed=True
    return (0,n-1,0) in W

def reverse_chain(t):
    n=len(t)
    return tuple(n-1-t[n-1-i] for i in range(n))

expected={
  1:Counter(sync_alice=1,sync_bob=0,nonsync=0),
  2:Counter(sync_alice=8,sync_bob=0,nonsync=1),
  3:Counter(sync_alice=77,sync_bob=4,nonsync=19),
}
bad_expected={
 ((0,0,1),(0,2,2)),
 ((0,0,2),(1,2,2)),
 ((0,2,2),(0,0,1)),
 ((1,2,2),(0,0,2)),
}

for n in (1,2,3):
    ms=maps(n)
    assert len(ms)=={1:1,2:3,3:10}[n]
    cnt=Counter(sync_alice=0,sync_bob=0,nonsync=0)
    bad=set()
    for a in ms:
        for b in ms:
            ts=(a,b)
            sync=synchronizing(ts,n)
            A=alice_full(ts,n)
            B=alice_pairs(ts,n)
            assert A==B
            if not sync:
                cnt["nonsync"]+=1
            elif A:
                cnt["sync_alice"]+=1
            else:
                cnt["sync_bob"]+=1
                bad.add((a,b))
    assert cnt==expected[n],(n,cnt)
    if n==3:
        assert bad==bad_expected

a=(0,0,1); b=(0,2,2)
# aa is a reset word.
assert tuple(a[a[q]] for q in range(3))==(0,0,0)

# Bob's stationary response b restores the active endpoints {0,2}
# after either possible Alice move.
full=(1<<3)-1
def step(mask,t): return image(mask,t,3)
for alice in (a,b):
    assert step(step(full,alice),b)==0b101
for alice in (a,b):
    assert step(step(0b101,alice),b)==0b101

# The four exceptional normalized presentations are one orbit under
# letter swap and chain reversal.
orb={(a,b),(b,a),(reverse_chain(a),reverse_chain(b)),
     (reverse_chain(b),reverse_chain(a))}
assert orb==bad_expected

# The three-state illustrative non-A-automaton in the 2024 paper has
# b swapping states 1 and 2. Directly check that no linear order makes
# both displayed letter maps nondecreasing.
lit_a=(0,0,2); lit_b=(0,2,1)
def nondecreasing_in_order(t,order):
    pos={q:i for i,q in enumerate(order)}
    vals=[pos[t[q]] for q in order]
    return vals==sorted(vals)
assert not any(nondecreasing_in_order(lit_a,o) and nondecreasing_in_order(lit_b,o)
               for o in permutations(range(3)))

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text())
assert cert["normalized_ordered_pair_census"]["3"]["synchronizing_bob_win"]==4
assert cert["three_state_bob_win_orbits"]==1
assert cert["representative"]["reset_word"]=="aa"
print("VERIFY_OK maps=1,3,10 n1=1/0/0 n2=8/0/1 n3=77/4/19 "
      "bad3=4 orbit3=1 engines=full-subset+endpoint-pair reset=aa bob=always-b "
      "literature_3state_example_nonmonotone=1")
