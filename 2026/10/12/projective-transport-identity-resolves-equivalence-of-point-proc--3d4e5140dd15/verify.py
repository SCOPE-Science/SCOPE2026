#!/usr/bin/env python3
"""Exact rational finite checks of the point-process transport identity."""
from fractions import Fraction as F
from itertools import combinations

# Configurations at three distinct sites; masses are nonnegative integers.
source = [((1, 0, 1), F(1, 2)), ((0, 1, 0), F(1, 2))]
target = [((0, 0, 1), F(1, 4)), ((1, 1, 0), F(3, 4))]

# In a 2-by-2 transport plan, t=pi[0,0] determines all entries.
def transport_2x2(cost):
    a = source[0][1]
    b = target[0][1]
    lo = max(F(0), a + b - 1)
    hi = min(a, b)
    def value(t):
        plan = (t, a - t, b - t, 1 - a - b + t)
        assert all(v >= 0 for v in plan)
        assert plan[0] + plan[1] == a
        assert plan[0] + plan[2] == b
        return sum(x*y for x, y in zip(plan, cost))
    return min(value(lo), value(hi))

def projected_cost(partition):
    costs = []
    for x, _ in source:
        for y, _ in target:
            costs.append(sum(abs(sum(x[i] - y[i] for i in cell)) for cell in partition))
    return transport_2x2(costs)

def variation_cost():
    costs=[]
    for x,_ in source:
        for y,_ in target:
            diffs=[u-v for u,v in zip(x,y)]
            costs.append(sum(abs(z) for z in diffs))
    return transport_2x2(costs)

def kr_cost():
    costs=[]
    for x,_ in source:
        for y,_ in target:
            diffs=[u-v for u,v in zip(x,y)]
            positive=sum(max(z,0) for z in diffs)
            negative=sum(max(-z,0) for z in diffs)
            costs.append(max(positive,negative))
    return transport_2x2(costs)

partitions=[
    ((0,1,2),),
    ((0,),(1,2)),
    ((1,),(0,2)),
    ((2,),(0,1)),
    ((0,),(1,),(2,)),
]
values=[projected_cost(p) for p in partitions]
full=variation_cost()
kr=kr_cost()
assert values[-1] == full == F(5,4), (values,full)
assert max(values) == full
assert kr == F(1)
assert F(1,2)*full <= kr <= full
assert values[0] == F(1,4)

# The two optimal comparison factors are attained by deterministic configurations.
def deterministic_costs(x,y):
    diff=[u-v for u,v in zip(x,y)]
    pos=sum(max(z,0) for z in diff)
    neg=sum(max(-z,0) for z in diff)
    return pos+neg,max(pos,neg)
assert deterministic_costs((0,0,0),(1,0,0))==(1,1)
assert deterministic_costs((1,0,0),(0,1,0))==(2,1)

# Exact signed-intensity benchmark on a finite space.
lam=(F(1),F(2),F(0))
eta=(F(2),F(0),F(1,2))
assert sum(abs(a-b) for a,b in zip(lam,eta))==F(7,2)

print(
    'VERIFY_OK '
    f'projective={float(full):.12f} '
    f'kr={float(kr):.12f} '
    f'partitions={len(partitions)}'
)
