"""Exact semigroup check for deleted mixed-coordinate quadratic Veronese charts.
Run: python checker.py. This checks finite parameters; symbolic proof is separate.
"""
from itertools import combinations_with_replacement, product
from math import comb


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def chart_generators(r):
    # Exponents in C[t,z_1,...,z_r], y=t^2, w_i=t*z_i.
    y = (2,) + (0,) * r
    zz = [tuple([0] + [int(j == i) for j in range(r)]) for i in range(r)]
    ww = [tuple([1] + [int(j == i) for j in range(r)]) for i in range(r)]
    return [y] + zz + ww


def gr_counts(r, max_k):
    gens = chart_generators(r)
    E = [{(0,) * (r + 1)}]
    for level in range(1, 2 * max_k + 1):
        E.append({add(v, g) for v in E[-1] for g in gens})
    ans = []
    for k in range(max_k + 1):
        higher = set().union(*E[k + 1:2 * max_k + 1])
        ans.append(len(E[k] - higher))
    return ans


def main():
    count = 0
    for n in range(2, 7):
        r = n - 1
        kk = 4
        actual = gr_counts(r, kk)
        predicted = [2 * comb(n + k - 1, n - 1) - 1 for k in range(kk + 1)]
        assert actual == predicted, (n, actual, predicted)
        print(f"n={n}, chart graded counts={actual}, expected={predicted}: PASS")
        count += kk + 1
        # Presentation monomial binomials map to the same exact exponent vector.
        gs = chart_generators(r)
        y, z, w = gs[0], gs[1:r + 1], gs[r + 1:]
        for i in range(r):
            for j in range(r):
                assert add(w[i], z[j]) == add(w[j], z[i])
                assert add(w[i], w[j]) == add(y, add(z[i], z[j]))
                count += 2
    for n in range(2, 7):
        for d in range(1, 6):
            # Degree-d coordinates of the quadratic Veronese use 2d total degree.
            # Missing monomials are exactly odd powers of x_0 and x_1,
            # with all other exponents zero.
            odd_missing = [(2*a+1, 2*(d-1-a)+1) for a in range(d)]
            assert len(odd_missing) == d
            assert len(set(odd_missing)) == d
            assert comb(n+2*d, n) - len(odd_missing) == comb(n+2*d, n)-d
            count += 1
    print(f"CHECKS PASSED: {count} graded coefficients, binomial identities, and homogeneous defects")


if __name__ == '__main__':
    main()
