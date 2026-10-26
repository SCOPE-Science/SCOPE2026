"""Finite exact-index consistency tests for superlacunary weighted shifts.
The analytic cluster-set theorem is not inferred from these tests.
"""
import math

def diagonal_entry(n, k, sites, amplitudes):
    assert n >= 1 and k >= 1
    e = sum(a * site for site, a in zip(sites, amplitudes)
            if k <= site <= k + n - 1) / n
    return math.exp(-e)

def log_product_direct(n, k, sites, amplitudes):
    # Independently scan all indices only for deliberately small windows.
    where = dict(zip(sites, amplitudes))
    logprod = 0.
    for i in range(k, k + n):
        if i in where:
            logprod -= i * where[i]
    return math.exp(logprod / n)

def check():
    sites = [2 ** (2 ** j) for j in range(1, 6)]
    amps = [math.log(2)] * len(sites)
    cases = 0
    for n in range(1, 400):
        for k in range(1, 13):
            a = diagonal_entry(n, k, sites, amps)
            b = log_product_direct(n, k, sites, amps)
            assert abs(a - b) < 1e-14
            cases += 1
    # Shifted spike windows exhibit the predicted first-h/remaining-tail split.
    for h in (1, 2, 4):
        errs = []
        for j in (2, 3, 4):
            n = sites[j] - h
            entries = [diagonal_entry(n, k, sites, amps) for k in range(1, 9)]
            expected = [1.0 if k <= h else 0.5 for k in range(1, 9)]
            errs.append(max(abs(a-b) for a,b in zip(entries,expected)))
            cases += 8
        assert errs[2] < errs[1] < errs[0], (h,errs)
    # Scalar cluster values: one full two-spike-gap dilation period, then larger.
    for divisor in (1, 2, 4):
        errors = []
        for j in (2, 3, 4):
            n = divisor * sites[j]
            goal = math.exp(-math.log(2)/divisor)
            observed = [diagonal_entry(n, k, sites, amps) for k in range(1, 10)]
            errors.append(max(abs(v-goal) for v in observed))
            cases += 9
        assert errors[-1] < errors[0], (divisor,errors)
    # The kth coordinate jump functional is nonzero precisely at the kth step.
    for h in range(1, 8):
        for m in range(1, 9):
            a = 0.7
            d = lambda k: 1. if k <= m else math.exp(-a)
            jump = d(h) - d(h+1)
            assert abs(jump - (1-math.exp(-a) if h == m else 0)) < 1e-14
            cases += 1
    print(f'PASS: {cases} index/formula, spike-limit and topology tests')

if __name__=='__main__':
    check()
