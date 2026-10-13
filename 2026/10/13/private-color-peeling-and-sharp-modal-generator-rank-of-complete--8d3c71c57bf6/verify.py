#!/usr/bin/env python3
"""Reproduce finite tests for colored complete multipartite Kripke models.
Uses only the Python standard library; exhaustive checks are explicitly finite.
"""
from itertools import product, combinations
from collections import Counter
from math import ceil, log2
from random import Random


def peel(parts):
    R = set(range(len(parts)))
    layers=[]
    while True:
        cnt=Counter(c for i in R for c in parts[i])
        batch={i for i in R if any(cnt[c]==1 for c in parts[i])}
        if not batch: return R,layers
        layers.append(batch)
        R.difference_update(batch)


def modal_rounds(parts):
    states=[(i,c) for i,P in enumerate(parts) for c in sorted(P)]
    types={s:s[1] for s in states}
    out=[]
    for round_num in range(len(states)+2):
        out.append((len(set(types.values())),types.copy()))
        tuples={s:(types[s],frozenset(types[t] for t in states if s[0]!=t[0])) for s in states}
        uniq={v:i for i,v in enumerate(sorted(set(tuples.values()),key=repr))}
        nxt={s:uniq[tuples[s]] for s in states}
        if len(set(nxt.values()))==len(set(types.values())):return states,types,out
        types=nxt
    raise AssertionError('refinement failed to stabilize')


def predicted_classes(parts):
    core,_=peel(parts)
    return { (i,c):('core',c) if i in core else (i,c) for i,P in enumerate(parts) for c in P}


def test_equiv(parts):
    states,actual,history=modal_rounds(parts)
    pred=predicted_classes(parts)
    for x in states:
        for y in states:
            if (actual[x]==actual[y]) != (pred[x]==pred[y]):
                raise AssertionError((parts,x,y,actual,pred))
    if len(history)-1>max(0,len(parts)-1):
        raise AssertionError((parts,'depth bound',len(history)-1))
    return len(history)-1


exhaustive=0
for k in range(1,6):
    nonempty=[frozenset(i for i in range(3) if mask & (1<<i)) for mask in range(1,8)]
    for parts in product(nonempty,repeat=k):
        test_equiv(parts)
        exhaustive+=1

# Rank criterion checked against independent brute force over sets, not the
# peeling-order proof. All labelled classes of each size are considered.
rank_cases=0
for k in range(1,5):
    for sizes in product(range(1,4),repeat=k):
        target=max(n+i for i,n in enumerate(sorted(sizes,reverse=True)))
        # Exhaustive feasibility for every q below or at 4.
        for q in range(max(1,max(sizes)),5):
            sets=[list(map(frozenset,combinations(range(q),sz))) for sz in sizes]
            feasible=any(not peel(parts)[0] for parts in product(*sets))
            assert feasible == (q>=target),(sizes,q,feasible,target)
            rank_cases+=1

# Verify the claimed optimal modal-depth family and the one-class-per-round
# propagation for arbitrary numbers of parts in a concrete infinite family.
sharp=0
for k in range(2,15):
    parts=[{0,1}]+[{i,i+1} for i in range(1,k-1)]+[{k-1}]
    states,types,rounds=modal_rounds(parts)
    assert len(rounds)-1==k-1,(k,[r[0] for r in rounds])
    assert [r[0] for r in rounds]==[k+t for t in range(k)]
    assert not peel(parts)[0]
    sharp+=1

# Directly close the Boolean set algebra under diamond and compare the
# number of atoms with the predicted core-quotient atom count.
def full_algebra_atom_count(colored_parts):
    states=[(i,col) for i,P in enumerate(colored_parts) for col in P]
    n=len(states)
    full=(1<<n)-1
    gens=[]
    for color in set(c for P in colored_parts for c in P):
        gens.append(sum(1<<u for u,(_,c) in enumerate(states) if c==color))
    A={0,full}
    A.update(gens)
    changed=True
    while changed:
        prev=len(A)
        cur=list(A)
        for x in cur:
            A.add(x ^ full)
            witness_parts={states[j][0] for j in range(n) if x>>j & 1}
            A.add(sum(1<<i for i,(part,_) in enumerate(states) if any(p!=part for p in witness_parts)))
        cur=list(A)
        for a in cur:
            for b in cur:
                A.add(a & b)
                A.add(a | b)
        changed=len(A)!=prev
    return (len(A).bit_length()-1,len(A))

rng=Random(20261010)
direct=0
for k in range(1,5):
    for _ in range(150):
        # Actual vertex color lists allow repetition in one part.
        parts=[[rng.randrange(3) for _ in range(rng.randint(1,2))] for _ in range(k)]
        core,_=peel(list(map(set,parts)))
        expected=sum(len(set(parts[i])) for i in range(k) if i not in core)+len(set(c for i in core for c in parts[i]))
        assert full_algebra_atom_count(parts)==(expected,1<<expected),(parts,core,expected)
        direct+=1

print('VERIFY_OK exhaustive_support_cases',exhaustive,'rank_bruteforce_cases',rank_cases,'sharp_depth_cases',sharp,'direct_boolean_closures',direct)
