"""Exact finite checks for cyclic fair interval scheduling and its four-job boundary."""
from fractions import Fraction
from itertools import combinations_with_replacement, product


def disjoint(items):
    return all(a[1] <= b[0] or b[1] <= a[0] for i, a in enumerate(items)
               for b in items[i+1:])


def greedy(starts, length, machines):
    assigned = [[] for _ in range(machines)]
    count = 0
    for t in starts:
        # Existing accepted start times, not rejected intervals.
        previous = [a for lane in assigned for a in lane]
        active = sum(t < a+length for a in previous)
        if active < machines:
            lane = count % machines
            assert not assigned[lane] or assigned[lane][-1] + length <= t
            assigned[lane].append(t)
            count += 1
        sizes = [len(lane) for lane in assigned]
        assert max(sizes)-min(sizes) <= 1
        for lane in assigned:
            assert all(a+length <= b for a, b in zip(lane,lane[1:]))
    return count


def optimum(starts, length, machines):
    n = len(starts)
    best = 0
    for mask in range(1<<n):
        if mask.bit_count() <= best:
            continue
        chosen = [t for i,t in enumerate(starts) if mask>>i&1]
        if all(sum(s <= t < s+length for s in chosen) <= machines for t in chosen):
            best = len(chosen)
    return best

cases = 0
for m in range(1,4):
    for n in range(0,9):
        for starts in combinations_with_replacement(range(7),n):
            assert greedy(starts,3,m) == optimum(starts,3,m), (starts,m)
            cases += 1
print('equal_length_exhaustive_instances',cases)

for eps in [Fraction(1,1000),Fraction(1,13),Fraction(1,2),Fraction(1,1)]:
    d=eps/3
    jobs=[(Fraction(0),Fraction(1)),(Fraction(1),Fraction(2)),
          (Fraction(2),Fraction(3)),(Fraction(1)-d,Fraction(2)+d)]
    assert all(Fraction(1) <= b-a <= 1+eps for a,b in jobs)
    best_raw=0; best_fair=0
    for labels in product(range(3),repeat=4): # two machines and rejection
        lanes = [[jobs[j] for j in range(4) if labels[j]==i] for i in [0,1]]
        if not all(disjoint(lane) for lane in lanes):continue
        taken = sum(x!=2 for x in labels)
        best_raw=max(best_raw,taken)
        if abs(len(lanes[0])-len(lanes[1]))<=1:
            best_fair=max(best_fair,taken)
    assert (best_raw,best_fair)==(4,3)
print('exact_fractional_perturbations',4,'max_unrestricted',4,'max_ef1',3)

# For two machines and at most three jobs, a full feasible allocation
# always has an EF1 recoloring (or the optimum has two or fewer jobs).
from itertools import combinations_with_replacement
triple_checks=0
possible=[(Fraction(i),Fraction(i+j)) for i in range(4) for j in [1,2,3]]
for n in range(0,4):
  for jobs in combinations_with_replacement(possible,n):
    best_raw=0;best_fair=0
    for labels in product(range(3), repeat=n):
      lanes=[[jobs[j] for j in range(n) if labels[j]==i] for i in [0,1]]
      if not all(disjoint(lane) for lane in lanes):continue
      taken=sum(x!=2 for x in labels)
      best_raw=max(best_raw,taken)
      if abs(len(lanes[0])-len(lanes[1]))<=1:best_fair=max(best_fair,taken)
    assert best_raw==best_fair
    triple_checks+=1
print('three_job_minimality_checks',triple_checks)
