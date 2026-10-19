"""Exact finite sanity checks for regularity in the finite binary-operation monoid.

No additional Python packages required; this checks finite cases only.
"""

from itertools import product
from math import exp, factorial, sqrt


def exact_diagonal_distribution(n):
    """Numbers of functions [n]->[n] with exactly d distinct image values."""
    dist = [0] * (n + 1)
    dist[0] = 1
    for used in range(n):
        new = [0] * (n + 1)
        for d in range(used + 1):
            new[d] += d * dist[d]
            new[d + 1] += (n - d) * dist[d]
        dist = new
    assert sum(dist) == n**n
    return dist


def exact_data(n):
    dist = exact_diagonal_distribution(n)
    unordered_pairs = n * (n - 1) // 2
    weights = [count * (n*n - n + d)**unordered_pairs
               for d, count in enumerate(dist)]
    regular = sum(weights)
    assert regular > 0
    return regular, n**(n*n), weights


def from_table(table, n):
    """Predicate derived from diagonal-image equivariance."""
    diagonal = {table[a*n + a] for a in range(n)}
    return all(table[a*n+b] != table[b*n+a]
               or table[a*n+b] in diagonal
               for a in range(n) for b in range(a+1, n))


def compose(left, right, n):
    """Pairmorph composition corresponding to the magma-monoid product."""
    return tuple(right[left[a*n+b]*n + left[b*n+a]]
                 for a in range(n) for b in range(n))


def independently_brute_force():
    for n in (2, 3):
        brute = sum(from_table(t, n)
                    for t in product(range(n), repeat=n*n))
        count, total, _ = exact_data(n)
        assert (brute, total) == ((14, 16) if n == 2 else (14619, 19683))
        assert brute == count, (n, brute, count)
        print(f"enumerated n={n}: regular={count} total={total}")
    n = 2
    all_ops = list(product(range(n), repeat=n*n))
    for a in all_ops:
        independent = any(compose(compose(a, b, n), a, n) == a
                          for b in all_ops)
        assert independent == from_table(a, n)
    print("direct inner-inverse enumeration n=2: complete")


def constants():
    z = exp(-0.5)
    lo, hi = 0.0, 1.0
    for _ in range(100):
        x = (lo + hi) / 2
        if (1-x)*exp(x) > 1-z:
            lo = x
        else:
            hi = x
    x = (lo+hi)/2
    f = exp(x) - 1 + z
    assert abs(f-x*exp(x)) < 1e-14
    theta = z / f
    rho = exp(x-1)
    variance = theta*(1-theta)-theta*theta/x
    constant = exp(theta/2-theta*theta/4)/sqrt(x)
    assert 0 < x < 1 and 0 < theta < 1 and 0 < variance
    return x, rho, theta, variance, constant


def exact_asymptotic_checks():
    x, rho, theta, var, constant = constants()
    print("saddle x=%.15f rho=%.15f theta=%.15f variance=%.15f prefactor=%.15f" %
          (x, rho, theta, var, constant))
    for n in (5, 10, 20, 40, 80, 160, 320):
        reg, total, weights = exact_data(n)
        probability = reg / total
        predicted = constant * rho**n
        ratio = probability / predicted
        omissions = sum((n-d)*w for d, w in enumerate(weights)) / reg
        omission_sq = sum((n-d)**2 *w for d, w in enumerate(weights)) / reg
        scaled_variance = (omission_sq - omissions**2)/n
        print("n=%3d probability=%.12g ratio=%.12f zero_fraction=%.9f var_per_n=%.9f" %
              (n, probability, ratio, omissions/n, scaled_variance))
        if n >= 20:
            assert abs(ratio-1) < 0.002
        if n >= 160:
            assert abs(omissions/n-theta) < 0.002
            assert abs(scaled_variance-var) < 0.002


if __name__ == "__main__":
    independently_brute_force()
    exact_asymptotic_checks()
    print("CHECK_OK")
