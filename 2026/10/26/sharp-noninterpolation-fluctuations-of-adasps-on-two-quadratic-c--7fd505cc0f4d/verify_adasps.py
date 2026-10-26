"""Reproducible finite checks for the two-client AdaSPS fluctuation law.
This is a numerical consistency checker; the infinite-horizon proof is analytical.
Requires Python >=3.9 and NumPy.
"""
import math
import numpy as np


def direct_trial(signs, c):
    x, total, prev = 0.0, 0.0, math.inf
    xs = []
    for xi in signs:
        loss = 0.5 * (x-xi)**2
        grad = x-xi
        assert grad != 0
        total += loss
        raw = loss/(c*grad**2*math.sqrt(total))
        eta = min(raw, prev)
        closed = 1/(2*c*math.sqrt(total))
        assert math.isclose(eta, closed, rel_tol=1e-12, abs_tol=1e-14)
        assert -1 < x < 1
        xs.append((x, eta, total))
        x = x-eta*grad
        prev = eta
    return x, xs


def main():
    # All binary sampling paths of length 11 are checked against the actual
    # loss/gradient-based AdaSPS min, not only against the simplified recurrence.
    for c in (1.0, 2.0, 3.0):
        for mask in range(2**11):
            signs = [1 if mask & (1<<j) else -1 for j in range(11)]
            direct_trial(signs, c)
    rng = np.random.default_rng(20261024)
    npaths, n = 14000, 8192
    for c in (1.0, 2.0):
        x = np.zeros(npaths)
        S = np.zeros(npaths)
        for j in range(n):
            xi = rng.choice(np.array([-1., 1.]), size=npaths)
            S += 0.5*(x-xi)**2
            eta = 1/(2*c*np.sqrt(S))
            x += eta*(xi-x)
        predicted = 1/(2*math.sqrt(2)*c)
        observed = math.sqrt(n)*float(np.mean(x*x))
        assert abs(observed/predicted-1)<0.10, (c,observed,predicted)
        assert abs(float(np.mean(S/n))-0.5)<0.025
        print('SIM_CHECK c=',c,'n=',n,'paths=',npaths,'sqrt(n)Ex2=',round(observed,6),'limit=',round(predicted,6))
    print('VERIFY_OK full AdaSPS branch 6144 binary paths x 11 updates; stochastic tail checks')

if __name__=='__main__':
    main()
