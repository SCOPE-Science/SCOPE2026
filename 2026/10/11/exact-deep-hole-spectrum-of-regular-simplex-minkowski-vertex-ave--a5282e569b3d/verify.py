"""Self-contained finite consistency tests for the exact simplex-grid deep-hole theorem.
These are not a proof of its all-dimensional assertion.
"""
import itertools
import math
import random

def compositions(k,d):
    if d==1:
        yield (k,)
    else:
        for a in range(k+1):
            for v in compositions(k-a,d-1):
                yield (a,)+v

def nearest_sq(q, points):
    return min(sum((x-y)**2 for x,y in zip(q,m)) for m in points)

rng=random.Random(271828)
for d in range(2,9):
    for k in range(1,7):
        sites=list(compositions(k,d))
        admissible=range(1,min(k,d-1)+1)
        mval=max(r*(d-r) for r in admissible)
        maximizers=[r for r in admissible if r*(d-r)==mval]
        predicted=[]
        for r in maximizers:
            for b in compositions(k-r,d):
                q=tuple(x+r/d for x in b)
                predicted.append(q)
                dist2=nearest_sq(q,sites)
                assert math.isclose(dist2,mval/d,abs_tol=1e-9), (d,k,r,q,dist2)
        exact_count=sum(math.comb(k-r+d-1,d-1) for r in maximizers)
        assert len(predicted)==exact_count
        assert len({tuple(round(x,9) for x in q) for q in predicted})==exact_count
        for _ in range(150):
            w=[rng.expovariate(1.) for j in range(d)]
            q=[k*t/sum(w) for t in w]
            assert nearest_sq(q,sites)<=mval/d+1e-9
        if k<=d//2:
            assert len(predicted)==1
            assert all(abs(x-k/d)<1e-9 for x in predicted[0])
print('VERIFY_OK')
print('dimensions=2..8 coordinates (n=1..7)')
print('averaging_counts=1..6')
print('tested_all_predicted_deep_holes_and_random_interior_points')
