"""Finite binomial-kernel diagnostics for positive lazy backward shifts.

These tests sample finite matrix entries; they are not proofs of infinite-dimensional
operator-norm estimates, absence of prior results, or spectral conclusions.
"""
import math


def binomial_probabilities(n, delta):
    return [math.exp(math.lgamma(n + 1) - math.lgamma(k + 1)
                     - math.lgamma(n - k + 1) + k * math.log(delta)
                     + (n - k) * math.log1p(-delta)) for k in range(n + 1)]


def boundary_witness(n, p, alpha, delta):
    b = binomial_probabilities(n, delta)
    h = [0.0] * (n + 2)
    for k in range(n + 2):
        h[k] = (b[k] if k <= n else 0.0) - (b[k - 1] if k >= 1 else 0.0)
    mu = n * delta
    j_lo = math.ceil(mu + 2 * math.sqrt(n))
    j_hi = math.floor(mu + 3 * math.sqrt(n))
    i_lo = math.ceil(math.sqrt(n))
    i_hi = math.floor(1.5 * math.sqrt(n))
    if j_lo > j_hi or i_lo > i_hi or j_lo - i_hi <= mu:
        raise AssertionError("sample size too small for separated windows")
    js = range(j_lo, j_hi + 1)
    is_ = range(i_lo, i_hi + 1)
    height = (j_hi - j_lo + 1) ** (-1.0 / p)
    y_power = []
    y_diff = []
    for i in is_:
        val_power = 0.0
        val_diff = 0.0
        for j in js:
            k = j - i
            weight = (j / i) ** alpha * height
            val_power += weight * b[k]
            val_diff += weight * h[k]
        y_power.append(val_power)
        y_diff.append(delta * val_diff)
    power = sum(abs(v) ** p for v in y_power) ** (1.0 / p)
    difference = sum(abs(v) ** p for v in y_diff) ** (1.0 / p)
    total_variation = sum(abs(v) for v in h)
    assert abs(total_variation - 2 * max(b)) < 2e-10
    assert all(h[j - i] < 0 for i in is_ for j in js)
    assert power > 0 and difference > 0
    return power / n ** (alpha / 2), difference * n ** ((1 - alpha) / 2)


def main():
    for p, alpha, delta in [(2.0, 0.3, 0.4), (3.0, 0.2, 0.3), (1.5, 0.5, 0.55)]:
        assert 1 < p < math.inf and 0 < alpha * p < 1
        values = [boundary_witness(n, p, alpha, delta) for n in (256, 512, 1024)]
        print('p=', p, 'alpha=', alpha, 'delta=', delta,
              'scaled_power_and_difference=', values)
        assert all(math.isfinite(a) and math.isfinite(b) and a > 0 and b > 0
                   for a, b in values)
    print('FINITE_DIAGNOSTICS_OK')


if __name__ == '__main__':
    main()
