#!/usr/bin/env python3
from fractions import Fraction


def reachability(n, obs, start):
    # edge r -> j iff r is observed by j
    out = {r: set() for r in range(n)}
    for j, parents in obs.items():
        for r in parents:
            out[r].add(j)
    seen = {start}
    stack = [start]
    while stack:
        r = stack.pop()
        for j in out[r]:
            if j not in seen:
                seen.add(j)
                stack.append(j)
    return seen

# Strict extension beyond own-state-only feedback.
obs = {0: {0}, 1: {0, 1}, 2: {2}}
K = {0: {2}, 1: {2}, 2: {1}}
for i in range(3):
    R = reachability(3, obs, i)
    assert K[i].isdisjoint(R), (i, K[i], R)
assert 0 in obs[1] and 0 != 1

# Length-two sharpness witness i=0 -> 1 -> 2.
alpha = Fraction(1, 2)
delta = Fraction(1, 20)
C = Fraction(1, 1)
m = 2

# Simulate states x_{t+1}=a_t. Player 0 deviates at t=0; opponents copy one edge per period.
x = [Fraction(0), Fraction(0), Fraction(0)]
actions = []
for t in range(m + 1):
    a = [Fraction(0), Fraction(0), Fraction(0)]
    if t == 0:
        a[0] = delta
    if t == 1:
        a[1] = x[0]
    if t == 2:
        a[2] = x[1]
    actions.append(tuple(a))
    x = a[:]
assert actions[0][0] == delta
assert actions[1][1] == delta
assert actions[2][2] == delta

potential_change = -delta * delta * sum(alpha ** r for r in range(m + 1))
residual_change = (alpha ** m) * C * delta
gain = potential_change + residual_change
assert gain == Fraction(13, 1600), gain
assert gain > 0

threshold = (alpha ** m) * C / sum(alpha ** r for r in range(m + 1))
assert delta < threshold
print('VERIFY_OK')
