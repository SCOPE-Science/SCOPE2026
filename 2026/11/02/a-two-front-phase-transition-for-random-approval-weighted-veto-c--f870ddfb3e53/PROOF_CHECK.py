"""Verifier for the independent-approval phase transition of AWVC.

Only Python standard library is needed for exhaustive equivalence tests; NumPy
is optional and used solely for sampling the critical limit.
"""
from itertools import product
from math import asin, pi, sqrt

def direct_block(profile):
    """Literal finite AWVC blocking criterion for candidate zero."""
    n, m = len(profile), len(profile[0])
    a = sum(v[0] for v in profile)
    if a == 0:
        return True
    d = [v for v in profile if not v[0]]
    for mask in range(1, 1 << len(d)):
        sub = [d[i] for i in range(len(d)) if mask >> i & 1]
        better = sum(all(row[j] for row in sub) for j in range(1,m))
        if m * len(sub) > a * (m - better):
            return True
    return False

def subset_block(profile):
    """Exact reduced criterion with at most 2**(m-1) tests."""
    m = len(profile[0]); a = sum(row[0] for row in profile)
    if a == 0:
        return True
    for target in range(1 << (m-1)):
        size = target.bit_count()
        count = sum((not row[0]) and all(row[j+1] for j in range(m-1) if target>>j&1) for row in profile)
        if m * count > a * (m-size):
            return True
    return False

def phase_boundary(m,q):
    return max(0.5, m*q**(m-1)/(1 + m*q**(m-1)))

def critical_probability(m):
    return 0.25 + asin(sqrt(2/(m+1)))/(2*pi)

def run():
    cases=0
    for m,n in ((3,4),(3,5),(4,3)):
        for rows in product(range(1<<m),repeat=n):
            prof = [[(row>>j)&1 for j in range(m)] for row in rows]
            assert direct_block(prof)==subset_block(prof), (m,n,rows)
            cases+=1
    assert cases==40960
    print('exhaustive agreement on',cases,'approval profiles')
    # Validate the convexity endpoint inequality at a dense rational grid.
    for m in range(2,31):
        for qi in range(1,200):
            q=qi/200
            strongest=max(q**k/(m-k) for k in range(m))
            extreme=max(1/m,q**(m-1))
            assert abs(strongest-extreme)<1e-12,(m,qi)
    print('endpoint maximum checked on 5771 grid cases')
    for m in (2,3,4,5,9):
        qc=m**(-1/(m-1))
        assert abs(phase_boundary(m,qc)-.5)<1e-12
    print('critical boundaries checked')
    try:
        import numpy as np
    except ImportError:
        print('NumPy unavailable; sampling skipped')
        return
    rng=np.random.default_rng(20261031)
    for m in (3,4,6):
        q=m**(-1/(m-1)); p=.5; n=4000
        # Categorize each voter: approves c, or disapproves c and
        # approves every rival, or disapproves c without full approval.
        outcomes=rng.multinomial(n,[.5,1/(2*m),.5-1/(2*m)],size=30000)
        X=outcomes[:,0]; Z=outcomes[:,1]
        survives=(2*X>=n)&(X>=m*Z)
        observed=float(survives.mean()); predicted=critical_probability(m)
        print('critical sampling m=',m,'predicted=',round(predicted,5), 'observed=',round(observed,5))
        assert abs(observed-predicted)<.02
    assert abs(critical_probability(3)-.375)<1e-14
    print('ALL TESTS PASSED')

if __name__=='__main__':run()
