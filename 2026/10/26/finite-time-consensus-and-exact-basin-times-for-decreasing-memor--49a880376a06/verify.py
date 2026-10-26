"""Exhaustive finite checks for monotone-memory binary threshold dynamics.
The theorem has a separate proof; these tests are not its proof.
"""
from itertools import combinations_with_replacement
from math import comb

def step(state,weights):
    score=sum(x*w for x,w in zip(state,weights))
    new=1 if score>0 or(score==0 and state[0]==1) else -1
    return (new,)+state[:-1],new

def check_one(weights):
    length=len(weights)
    counts=[0]*(length+1)
    for code in range(1<<length):
        state=tuple(1 if code>>j&1 else -1 for j in range(length))
        old=state
        score=sum(x*w for x,w in zip(state,weights))
        selected=1 if score>0 or(score==0 and state[0]==1) else -1
        earliest=next((j for j,x in enumerate(old) if x!=selected),None)
        expected=0 if earliest is None else length-earliest
        for t in range(1,length+1):
            state,emitted=step(state,weights)
            assert emitted==selected, (weights,old,t,emitted,selected)
            if t<expected:assert state!=(selected,)*length
            if t>=expected:assert state==(selected,)*length
        counts[expected]+=1
    assert sum(counts)==1<<length
    assert sum(counts[1:])== (1<<length)-2
    return counts

def uniform_formula(length):
    m=length//2
    out=[0]*(length+1)
    out[0]=2
    for j in range(length):
        remain=length-j-1
        if length%2:
            low=m+1-j
        else:
            low=(m+1 if j==0 else m-j)
        out[length-j]=2*sum(comb(remain,k) for k in range(max(0,low),remain+1))
    return out

tests=0
for length in range(1,9):
    for seq in combinations_with_replacement(range(5),length):
        w=seq[::-1]
        actual=check_one(w)
        tests+=1
    assert check_one((1,)*length)==uniform_formula(length), (length,check_one((1,)*length),uniform_formula(length))
    print(f'length={length} weights_checked={comb(length+4,4)} uniform_histogram={uniform_formula(length)}')
print('CHECKS_PASS',tests)
