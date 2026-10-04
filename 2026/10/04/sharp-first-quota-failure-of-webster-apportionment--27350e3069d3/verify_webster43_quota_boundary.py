#!/usr/bin/env python3
from fractions import Fraction
from itertools import product


def compositions(total, k):
    if k == 1:
        yield (total,)
        return
    for x in range(1, total-k+2):
        for tail in compositions(total-x, k-1):
            yield (x,) + tail


def webster_priority(pop, h):
    a = [0]*len(pop)
    for _ in range(h):
        best = None
        ties = []
        for i,p in enumerate(pop):
            if best is None:
                best = i; ties=[i]
                continue
            lhs = p*(2*a[best]+1)
            rhs = pop[best]*(2*a[i]+1)
            if lhs > rhs:
                best=i; ties=[i]
            elif lhs == rhs:
                ties.append(i)
        if len(ties) != 1:
            return None
        a[best] += 1
    return tuple(a)


def divisor_interval(pop, a):
    # Webster rounding-to-nearest divisor interval, with half-ties excluded.
    lo = Fraction(0,1)
    hi = None
    for p,x in zip(pop,a):
        if x == 0:
            lo = max(lo, Fraction(2*p,1))
        else:
            lo = max(lo, Fraction(2*p, 2*x+1))
            cand = Fraction(2*p, 2*x-1)
            hi = cand if hi is None else min(hi,cand)
    return (hi is None) or (lo < hi)


def quota_violations(pop,h,a):
    P=sum(pop); out=[]
    for i,(p,x) in enumerate(zip(pop,a)):
        lo=(h*p)//P
        up=(h*p + P-1)//P
        if x < lo: out.append((i,'lower',lo))
        if x > up: out.append((i,'upper',up))
    return out


def chamber(pop):
    P=sum(pop); hit=[]
    for i,a in enumerate(pop):
        if 3*a <= 2*P and all(i==j or 5*pop[j] < a for j in range(4)):
            hit.append(i)
    return tuple(hit)

# Check every positive integer profile through total 40 for all coordinatewise predecessor cells.
for s in range(1,5):
    for h in range(1,4):
        if (s,h)==(4,3):
            continue
        for P in range(s,41):
            for pop in compositions(P,s):
                a=webster_priority(pop,h)
                if a is None:
                    continue
                assert divisor_interval(pop,a)
                assert not quota_violations(pop,h,a), (s,h,pop,a,quota_violations(pop,h,a))

# Exact chamber test at the first violating cell.
violating=[]
for P in range(4,41):
    for pop in compositions(P,4):
        a=webster_priority(pop,3)
        if a is None:
            continue
        assert divisor_interval(pop,a)
        v=quota_violations(pop,3,a)
        ch=chamber(pop)
        assert bool(v) == bool(ch), (pop,a,v,ch)
        if v:
            assert len(v)==1 and v[0][1]=='upper'
            i=v[0][0]
            assert ch==(i,)
            assert a[i]==3 and sum(a[j] for j in range(4) if j!=i)==0
            violating.append((pop,a,i))

# Least-total positive-integer witness and uniqueness up to labels.
least=min(sum(pop) for pop,_,_ in violating)
assert least==9
least_sorted={tuple(sorted(pop, reverse=True)) for pop,_,_ in violating if sum(pop)==least}
assert least_sorted=={(6,1,1,1)}
least_labeled=[pop for pop,_,_ in violating if sum(pop)==least]
assert len(least_labeled)==4

# Exact uniform-simplex probability. For a fixed violating label x in (5/8,2/3],
# conditional cap t=x/[5(1-x)] gives P(max of other three < t)=(3t-1)^2.
# The Dirichlet(1,1,1,1) marginal density of x is 3(1-x)^2.
# The integrand simplifies to 3(8x-5)^2/25.
a=Fraction(5,8); b=Fraction(2,3)
def F(x):
    # antiderivative of 3(8x-5)^2/25 = (192x^2-240x+75)/25
    return Fraction(64,25)*x**3 - Fraction(24,5)*x**2 + 3*x
fixed=F(b)-F(a)
assert fixed==Fraction(1,5400), fixed
total=4*fixed
assert total==Fraction(1,1350), total

# Display witness and cutoff priorities.
w=(6,1,1,1)
assert webster_priority(w,3)==(3,0,0,0)
assert quota_violations(w,3,(3,0,0,0))==[(0,'upper',2)]

print('VERIFY_OK')
print('first_cell', (4,3))
print('fixed_label_probability', fixed)
print('total_probability', total)
print('least_total', least)
print('least_sorted_witness', (6,1,1,1))
print('least_labeled_witnesses', len(least_labeled))
print('integer_profiles_checked_through_total', 40)
