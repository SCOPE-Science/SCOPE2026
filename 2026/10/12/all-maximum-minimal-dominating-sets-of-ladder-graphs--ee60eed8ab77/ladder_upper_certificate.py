#!/usr/bin/env python3
"""Finite-state proof certificate for minimum-size maximality and upper domination of ladders.
Standalone Python 3; no nonstandard modules or external inputs.
"""
from collections import deque
from itertools import product, combinations

PAD=4
ALPH=range(4)
STATES=list(product(range(5),repeat=4))
START=(PAD,)*4
BAD=-1000000

def closed(column,row,word):
    """Closed neighborhood of (column,row), in five real-or-padded columns."""
    return [(j,r) for j in range(max(0,column-1),min(4,column+1)+1)
            for r in range(2) if word[j]!=PAD and abs(j-column)+abs(r-row)<=1]

def selected(word,position):
    c,r=position
    return (word[c]!=PAD) and bool(word[c] & (1<<r))

def valid_center(word):
    """All vertices of center column are dominated and selected ones irredundant."""
    if word[2]==PAD:
        return True
    for row in range(2):
        nbr=closed(2,row,word)
        if not any(selected(word,p) for p in nbr):
            return False
        if selected(word,(2,row)):
            if not any(sum(selected(word,p) for p in closed(*w,word))==1
                       for w in nbr):
                return False
    return True


def arcs(s):
    for b in ALPH:
        if valid_center(s+(b,)):
            yield s[1:]+(b,),b.bit_count()-1,b

def final(s):
    for b in (PAD,PAD):
        if not valid_center(s+(b,)):
            return False
        s=s[1:]+(b,)
    return True

def calculate_potential():
    """R(s): maximum remaining (# selected - # columns), including option to stop."""
    r={s:(0 if final(s) else BAD) for s in STATES}
    rounds=0
    while True:
        rr={s:max([r[s]]+[g+r[t] for t,g,_ in arcs(s)]) for s in STATES}
        if rr==r:
            break
        rounds+=1
        assert rounds<=625, 'Positive-weight cycle or flawed state encoding'
        r=rr
    assert r[START]==0
    assert all(r[s]>=g+r[t] for s in STATES for t,g,_ in arcs(s))
    assert all(r[s]>=0 for s in STATES if final(s))
    return r,rounds

def target_update(mask,b,nmod4):
    """Six periodic proposed patterns: four singleton patterns, two double/empty."""
    patterns=((1,),(2,),(1,2),(2,1),(3,0,0,3),(0,3,3,0))
    return sum((1<<i) for i,p in enumerate(patterns)
               if mask&(1<<i) and p[nmod4%len(p)]==b)

def verify_language(r):
    """Prove infinite equality with six patterns by product-automaton exhaustion."""
    # States: (critical state, matching pattern mask, column count mod4, length category 0/1/>1)
    start=(START,63,0,0)
    q=deque([start]);visited={start};edgecount=0
    while q:
        s,mask,mod,cat=q.popleft()
        accepting=(cat>=1 and final(s) and r[s]==0)
        # For category >=2 only parity, and category 1 has exact length 1.
        expected=(bool(mask & 15) or (cat>=2 and mod%2==0 and bool(mask&48))) if cat else False
        assert accepting==expected,(s,mask,mod,cat,accepting,expected)
        for t,g,b in arcs(s):
            if r[s]!=g+r[t]:
                continue
            edgecount+=1
            next_state=(t,target_update(mask,b,mod),(mod+1)%4,min(2,cat+1))
            if next_state not in visited:
                visited.add(next_state)
                q.append(next_state)
    return len(visited),edgecount

def brute(n):
    """Independent graph-level census, not using the transfer machine."""
    N=2*n
    neighborhoods=[]
    for col in range(n):
        for row in range(2):
            hood=0
            for col2 in range(n):
                for row2 in range(2):
                    if abs(col-col2)+abs(row-row2)<=1:
                        hood|=1<<(col2*2+row2)
            neighborhoods.append(hood)
    seen=set()
    for comb in combinations(range(N),n):
        bs=sum(1<<i for i in comb)
        if any(not (bs&h) for h in neighborhoods):
            continue
        if any(not any((bs&h)==(1<<i) for h in neighborhoods if h&(1<<i)) for i in comb):
            continue
        masks=tuple(sum(1<<r for r in range(2) if bs>>(c*2+r)&1) for c in range(n))
        seen.add(masks)
    return seen

def main():
    r,rounds=calculate_potential()
    nodes,edges=verify_language(r)
    patterns=((1,),(2,),(1,2),(2,1),(3,0,0,3),(0,3,3,0))
    checked=0
    for n in range(1,11):
        expect={tuple(p[i%len(p)] for i in range(n)) for p in patterns[:4]}
        if n%2==0:expect.update(tuple(p[i%4] for i in range(n)) for p in patterns[4:])
        assert brute(n)==expect, (n,brute(n),expect)
        checked+=1
    print('ALL CHECKS PASSED')
    print(f'potential_rounds={rounds}; all_state_inequalities={len(STATES)}; ' 
          f'tight_product_states={nodes}; tight_product_edges={edges}; '
          f'independent_exact_censuses={checked}; n_range=1..10')
    print('Infinite conclusion: for n>=2, four singleton-column families; ' 
          'if n is even, two additional full-empty column families. ' 
          'Upper domination=n; optimal-set count=4 (odd), 6 (even).')
if __name__=='__main__': main()
