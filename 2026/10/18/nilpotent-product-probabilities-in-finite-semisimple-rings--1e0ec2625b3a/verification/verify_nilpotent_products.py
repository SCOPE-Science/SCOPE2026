"""Independent exhaustive checks of nilpotent products in small matrix rings.

Only prime field instances are enumerated, since the theorem's proof treats
all finite fields and all dimensions. Each product is counted with multiplicity.
"""
from collections import defaultdict
from itertools import product


def multiply(a, b, n, q):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n)) % q
                 for i in range(n) for j in range(n))


def is_nilpotent(a, n, q):
    power = tuple(1 if i == j else 0 for i in range(n) for j in range(n))
    for _ in range(n):
        power = multiply(power, a, n, q)
    return not any(power)


def run_case(n, q, longest):
    matrices = list(product(range(q), repeat=n*n))
    ident = tuple(int(i == j) for i in range(n) for j in range(n))
    counts = {ident: 1}
    nil_set = {mat for mat in matrices if is_nilpotent(mat, n, q)}
    print('n=%d q=%d nilpotents=%d expected=%d' %
          (n, q, len(nil_set), q**(n*n-n)))
    assert len(nil_set) == q**(n*n-n)
    for m in range(1, longest+1):
        next_counts = defaultdict(int)
        for left, weight in counts.items():
            for right in matrices:
                next_counts[multiply(left, right, n, q)] += weight
        counts = next_counts
        total = q**(m*n*n)
        observed = sum(weight for mat, weight in counts.items() if mat in nil_set)
        predicted = total - (q**n-1)**m*q**(m*n*(n-1))
        print('  m=%d observed=%d predicted=%d total=%d states=%d' %
              (m, observed, predicted, total, len(counts)))
        assert sum(counts.values()) == total
        assert observed == predicted


if __name__ == '__main__':
    run_case(1, 2, 4)
    run_case(2, 2, 4)
    run_case(2, 3, 3)
    run_case(3, 2, 3)
    print('All exhaustive checks passed.')
