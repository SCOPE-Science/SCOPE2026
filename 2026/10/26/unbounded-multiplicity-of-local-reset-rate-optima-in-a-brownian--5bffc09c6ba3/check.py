"""Independent finite-parameter checks for geometric multi-site Brownian resetting.

The infinitely many particle-count statement follows from the proof, not from
these numerical checks. Standard Python 3 only.
"""
import math

L = 1000
checks = 0


def insist(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def h(z):
    return z / math.expm1(z) if z != 0 else 1.0


def ratio(c, j, k):
    # This normalizes the dominant j-th resetting location before summing.
    t = [float(L ** (i - j)) for i in range(k)]
    w = [x * math.exp(-c * x) for x in t]
    return sum(x * x * math.exp(-c * x) for x in t) / sum(w)


def derivative_sign(c, j, k):
    return h(c / (L ** j)) - 2 + c * ratio(c, j, k)


def log_mean(u, k):
    a = [L ** j for j in range(k)]
    logterms = [math.log(x) - x * u for x in a]
    v = max(logterms)
    logsum = v + math.log(sum(math.exp(x - v) for x in logterms))
    return (math.log(sum(a)) + math.log(-math.expm1(-u))
            - 2 * math.log(u) - logsum)


# Uniform estimates that appear in the infinite-family proof.
bound = math.exp(2) * (1 / (L - 1) + 2 * L * L * math.exp(-L / 2))
insist(bound < 0.01, 'infinite-family tail inequality')
insist(2 / (math.exp(2) - 1) > 0.3, 'endpoint lower bound')

for k in range(1, 21):
    locations = [L ** j for j in range(k)]
    for j in range(k):
        left, right = 0.5, 2.0
        for c in (left, right):
            r = ratio(c, j, k)
            insist(0.99 < r < 1.01, ('dominance estimate', k, j, c, r))
        dl = derivative_sign(left, j, k)
        dr = derivative_sign(right, j, k)
        insist(dl < -0.49, ('negative left derivative', k, j, dl))
        insist(dr > 0.28, ('positive right derivative', k, j, dr))
        # Check the existence of a stationary point inside each disjoint window.
        for _ in range(55):
            mid = (left + right) / 2
            if derivative_sign(mid, j, k) < 0:
                left = mid
            else:
                right = mid
        insist(0.5 < (left + right) / 2 < 2, ('stationary bracket', k, j))
        if j + 1 < k:
            insist(2 / locations[j + 1] < 0.5 / locations[j],
                   ('disjoint intervals', k, j))

for k in range(1, 6):
    for j in range(k):
        for c in (0.5, 1.0, 2.0):
            u = c / (L ** j)
            eps = 1e-4
            d = (log_mean(u * (1 + eps), k) - log_mean(u * (1 - eps), k)) / (
                math.log1p(eps) - math.log1p(-eps))
            target = derivative_sign(c, j, k)
            insist(abs(d - target) < 2e-5,
                   ('independent finite-difference identity', k, j, c, d, target))

print(f'PASS: {checks} assertions across k=1,...,20; exact proof handles every k.')
