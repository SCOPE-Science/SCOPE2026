"""Exact-rational finite checks for symmetric negative-doubling escape laws.

Uses inverse branches and interval intersection, independently of the four-block
transfer recursion. It checks finite instances, not the universal proof.
"""
from fractions import Fraction as F


def normalized(intervals):
    ans = []
    for left, right in sorted(intervals):
        if left >= right:
            continue
        if ans and left <= ans[-1][1]:
            ans[-1] = (ans[-1][0], max(right, ans[-1][1]))
        else:
            ans.append((left, right))
    return ans


def intersect(a, b):
    return normalized((max(x, u), min(y, v)) for x, y in a for u, v in b)


def step(surviving, a):
    inverse = []
    for lo, hi in surviving:
        inverse.append(((1-hi)/2, (1-lo)/2))
        inverse.append((1-hi/2, 1-lo/2))
    return intersect(inverse, [(F(0),a),(1-a,F(1))])


def measure(intervals):
    return sum((r-l for l,r in intervals), F(0))


def prediction(a,n):
    return (2*a+2*n*max(F(0),3*a-1))/2**n

checks=0
for a in [F(1,17),F(1,4),F(3,10),F(1,3),F(17,50),F(7,20),
          F(3,8),F(39,100),F(2,5)]:
    intervals=[(F(0),a),(1-a,F(1))]
    for n in range(35):
        assert measure(intervals)==prediction(a,n),(a,n,measure(intervals),prediction(a,n))
        checks+=1
        intervals=step(intervals,a)

# The second-survival formula changes immediately beyond the sharp upper edge.
sharp_checks=0
for a in [F(41,100),F(5,12),F(9,20),F(49,100)]:
    intervals=[(F(0),a),(1-a,F(1))]
    for i in range(2):intervals=step(intervals,a)
    assert measure(intervals)==6*a-2
    assert measure(intervals)-prediction(a,2)==(5*a-2)/2>0
    sharp_checks+=1

print('VERIFY_OK closed_form_cases=',checks,
      'upper_edge_cases=',sharp_checks,
      'max_exact_horizon=34')
