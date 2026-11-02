#!/usr/bin/env python3
"""Exact, standalone certificate checker for a seven-good sequential draft."""
from functools import lru_cache
import json
import sys

N = 3
M = 7
VALUATIONS = (
    (769, 2, 388, 520, 16, 672, 320),
    (513, 386, 388, 648, 272, 800, 704),
    (129, 258, 132, 264, 656, 416, 448),
)
BAD = (41, 68, 18)
FULL = (1 << M) - 1

sums = []
for row in VALUATIONS:
    sums.append([sum(row[g] for g in range(M) if mask & (1 << g))
                 for mask in range(1 << M)])
    assert len(set(sums[-1])) == 1 << M, 'Non-strict bundle preferences'

@lru_cache(None)
def backward(remaining):
    """All outcomes supported by some pure SPNE in the remaining-goods subgame."""
    if not remaining:
        return ((0, 0, 0),)
    i = (M - remaining.bit_count()) % N
    continuations = {}
    for g in range(M):
        b = 1 << g
        if remaining & b:
            possible = []
            for child in backward(remaining ^ b):
                out = list(child)
                out[i] |= b
                possible.append(tuple(out))
            continuations[g] = possible
    threshold = max(min(sums[i][x[i]] for x in outs)
                    for outs in continuations.values())
    ans = {x for outs in continuations.values() for x in outs
           if sums[i][x[i]] >= threshold}
    assert ans
    return tuple(sorted(ans))

# A second implementation, bottom-up, using a different control flow.
forward = {0: {(0, 0, 0)}}
for remaining in range(1, FULL + 1):
    i = (M - remaining.bit_count()) % N
    options = []
    for bit in range(M):
        b = 1 << bit
        if remaining & b:
            child_vals = forward[remaining ^ b]
            lifted = {x[:i] + (x[i] | b,) + x[i+1:] for x in child_vals}
            options.append(lifted)
    bound = max(min(sums[i][x[i]] for x in lifted) for lifted in options)
    forward[remaining] = set().union(*(set(x for x in lifted
                                         if sums[i][x[i]] >= bound)
                                      for lifted in options))
    assert forward[remaining] == set(backward(remaining)), remaining

# Explicit off-path continuation construction for an SPNE yielding BAD.
# At each history the chosen action leads to the requested outcome; all
# alternative actions lead to a continuation minimizing the mover's utility.
# Every resulting subgame action is checked against every one-shot deviation.
calls = [0]
def realize(remaining, requested):
    calls[0] += 1
    if not remaining:
        assert requested == (0, 0, 0)
        return
    i = (M - remaining.bit_count()) % N
    chosen = []
    for g in range(M):
        b = 1 << g
        if remaining & b and (requested[i] & b):
            child = tuple(requested[j] & ~b for j in range(N))
            if child in backward(remaining ^ b):
                chosen.append((g, child))
    assert chosen, ('requested outcome lacks equilibrium continuation', remaining)
    gchosen, childchosen = chosen[0]
    desired_payoff = sums[i][requested[i]]
    for g in range(M):
        b = 1 << g
        if not remaining & b:
            continue
        if g == gchosen:
            sub = childchosen
            payoff = desired_payoff
        else:
            sub = min(backward(remaining ^ b),
                      key=lambda a: sums[i][a[i] | b])
            payoff = sums[i][sub[i] | b]
        assert desired_payoff >= payoff, (remaining, g, desired_payoff, payoff)
        realize(remaining ^ b, sub)

assert len(backward(FULL)) == 2
assert BAD in backward(FULL)
realize(FULL, BAD)

other = (13, 96, 18)
assert set(backward(FULL)) == {BAD, other}
assert all((a[0] | a[1] | a[2]) == FULL and
           not (a[0] & a[1] or a[0] & a[2] or a[1] & a[2])
           for a in backward(FULL))

def violating_pairs(outcome):
    badpairs=[]
    for i in range(N):
        for j in range(N):
            if i == j or not outcome[j]:
                continue
            if all(sums[i][outcome[i]] < sums[i][outcome[j] ^ (1 << g)]
                   for g in range(M) if outcome[j] & (1 << g)):
                badpairs.append((i, j))
    return badpairs

assert violating_pairs(BAD) == [(1, 0)]
assert not violating_pairs(other)
assert sums[1][BAD[1]] == 1092
assert min(sums[1][BAD[0] ^ (1 << g)]
           for g in range(M) if BAD[0] & (1 << g)) == 1161

certificate = {
    'valuations': VALUATIONS,
    'bad_allocation_masks': BAD,
    'root_equilibrium_masks': [list(x) for x in backward(FULL)],
    'number_of_states': backward.cache_info().currsize,
    'state_counts': [len(backward(s)) for s in range(FULL + 1)],
    'equilibrium_branch_checks': calls[0],
    'violating_ordered_pairs_zero_based': violating_pairs(BAD),
    'envying_agent_own_utility': 1092,
    'minimum_envied_bundle_after_one_deletion': 1161,
}
if len(sys.argv)>1:
    with open(sys.argv[1],encoding='utf-8') as f:
        actual=json.load(f)
    assert actual == json.loads(json.dumps(certificate)), 'Certificate data differ from exact recomputation'
print('VERIFY_OK states=128 root_spne_outcomes=2 unfair=1 '
      f'explicit_strategy_nodes={calls[0]} gap=69')
