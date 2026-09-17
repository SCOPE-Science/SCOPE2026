"""Independent occupation-count DP and elementary path-event bound."""
import itertools
import math


def distribution(n, a, q, p):
    zero = [0.0] * (n + 1)
    one = [0.0] * (n + 1)
    zero[0], one[1] = 1 - p, p
    for t in range(1, n):
        nz, no = [0.0] * (n + 1), [0.0] * (n + 1)
        for k in range(t + 1):
            nz[k] = zero[k] * (1 - a) + one[k] * q
            no[k + 1] = zero[k] * a + one[k] * (1 - q)
        zero, one = nz, no
    return [x + y for x, y in zip(zero, one)]


def check_small():
    a, q = 0.07, 0.21
    p = a / (a + q)
    for n in range(2, 11):
        brute = [0.0] * (n + 1)
        for path in itertools.product((0, 1), repeat=n):
            prob = p if path[0] else 1 - p
            for x, y in zip(path, path[1:]):
                prob *= ((1 - a, a), (q, 1 - q))[x][y]
            brute[sum(path)] += prob
        assert max(abs(x-y) for x, y in zip(brute, distribution(n, a, q, p))) < 1e-12
    # Compute matrix powers directly and compare with Section 4.4's formula.
    power = [[1.0, 0.0], [0.0, 1.0]]
    P = [[1-a, a], [q, 1-q]]
    pi = [1-p, p]
    for t in range(11):
        beta = sum(pi[i] * sum(abs(power[i][j]-pi[j]) for j in range(2))/2 for i in range(2))
        assert abs(beta-2*p*(1-p)*abs(1-a-q)**t) < 1e-12
        power = [[sum(power[i][k]*P[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


check_small()
print('Small-path enumeration and matrix-power formula checks passed.')
for n in (1000, 1001, 2000, 5000):
    p, q, a = 0.001, 250/n, 250/(999*n)
    m, L = n//2, n//500 + 1
    bound = (1-p) * (-math.expm1(m*math.log1p(-a))) * (1-q)**(L-1)
    dist = distribution(n, a, q, p)
    # Strict centered deviation > 1/1000 is exactly K > n/500.
    tail = sum(dist[n//500 + 1:])
    beta = 2*p*(1-p)*(1-a-q)
    assert abs(sum(dist)-1) < 1e-10
    assert beta < 0.01/math.e
    assert tail >= bound > 0.01
    print(f'n={n} beta(1)={beta:.12g} event_bound={bound:.12g} exact_DP_tail={tail:.12g}')
print('Uniform analytic bound:', .999*(1-math.exp(-.12))*math.exp(-2/3))
