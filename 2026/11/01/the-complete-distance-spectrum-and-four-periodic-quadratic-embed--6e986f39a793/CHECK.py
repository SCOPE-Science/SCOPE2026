"""Exact arithmetic checks for the folded-cube distance spectrum."""
from math import comb, factorial


def signed_eigenvalue(n, j):
    if j == 0:
        return n * 2 ** (n - 2) - n * comb(n - 1, (n - 1) // 2) // 2
    assert j >= 2 and j % 2 == 0
    a, r = j // 2, n // 2
    num = factorial(2 * a - 2) * factorial(n - 2 * a)
    den = factorial(a - 1) * factorial(r - a) * factorial((n - 1) // 2)
    assert num % den == 0
    return (-1) ** a * (num // den)


def independent_krawtchouk(n, j):
    total = 0
    for k in range(n + 1):
        kraw = 0
        for t in range(max(0, k - (n - j)), min(k, j) + 1):
            kraw += (-1) ** t * comb(j, t) * comb(n - j, k - t)
        total += min(k, n - k) * kraw
    assert total % 2 == 0
    return total // 2


def direct_walsh(n, a):
    # Each antipodal class has exactly one representative with final bit zero.
    size = 1 << (n - 1)
    return sum(min(y.bit_count(), n - y.bit_count()) *
               (-1 if ((a & y).bit_count() % 2) else 1)
               for y in range(size))


def qec(n):
    m = comb(n - 2, (n - 2) // 2)
    if n == 3:
        return -1
    if n % 4 == 0:
        return m
    if n % 2 == 0:
        assert m % (n - 3) == 0
        return m // (n - 3)
    assert m % (n - 2) == 0
    return m // (n - 2)


def run():
    assertions = 0
    for n in range(3, 71):
        s = 0
        positive, negative = 0, 0
        largest_nonconstant = None
        for j in range(0, n + 1, 2):
            v = signed_eigenvalue(n, j)
            w = independent_krawtchouk(n, j)
            assert v == w, (n, j, v, w)
            assertions += 1
            multiplicity = comb(n, j)
            s += multiplicity * v
            if v > 0:
                positive += multiplicity
            elif v < 0:
                negative += multiplicity
            else:
                raise AssertionError('Unpredicted zero eigenvalue')
            if j:
                largest_nonconstant = (v if largest_nonconstant is None
                                       else max(largest_nonconstant, v))
        assert s == 0, ('distance matrix trace', n, s)
        assert positive == sum(comb(n,j) for j in range(0,n+1,4))
        assert negative == sum(comb(n,j) for j in range(2,n+1,4))
        assert largest_nonconstant == qec(n), (n, largest_nonconstant, qec(n))
        assertions += 4
    for n in range(3, 11):
        for j in range(0, n + 1, 2):
            # Even-weight Walsh label with j-1 lower bits and final bit set.
            a = ((1 << (j - 1)) - 1) | (1 << (n - 1)) if j else 0
            assert a.bit_count() == j
            assert direct_walsh(n, a) == signed_eigenvalue(n, j)
            assertions += 1
    print('EXACT_FOLDED_CUBE_SPECTRA_OK', assertions)


if __name__ == '__main__':
    run()
