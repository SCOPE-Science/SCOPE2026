#!/usr/bin/env python3
"""Exact reachable-state proof checks for pair-eligible unit allocations."""
from itertools import combinations

def moves(state):
    for a,b in combinations(range(len(state)),2):
        candidate=list(state)
        candidate[a]-=1
        candidate[b]+=1
        yield tuple(sorted(candidate,reverse=True))

five=(0,0,0,0,0)
reachable={five}
while True:
    successor=reachable | {t for s in reachable for t in moves(s)}
    if successor == reachable: break
    reachable=successor
assert len(reachable)==9
assert all(max(s)<=2 for s in reachable)
assert all(sum(s)==0 for s in reachable)
assert all(t in reachable for s in reachable for t in moves(s))
print('five_agent_closed_invariant_states',len(reachable))

states={(0,)*6}
counts=[]
for t in range(8):
    counts.append(len(states))
    assert all(max(s)<=2 for s in states),(t,states)
    states={v for s in states for v in moves(s)}
assert counts==[1,1,3,6,9,10,11,13],counts
print('six_agent_states_depth_0_through_7',counts)

state=(0,)*6
trace=[state]
for level in (0,0,1,0,-1,0,1,2):
    indexes=[i for i,value in enumerate(state) if value==level]
    assert len(indexes)>=2,(state,level)
    cand=list(state);cand[indexes[0]]-=1;cand[indexes[1]]+=1
    state=tuple(sorted(cand,reverse=True));trace.append(state)
assert trace[-1]==(3,1,0,-1,-1,-2)
print('forced_equal_pair_trace')
for t,s in enumerate(trace): print(t,s)
print('CHECKS_OK')
