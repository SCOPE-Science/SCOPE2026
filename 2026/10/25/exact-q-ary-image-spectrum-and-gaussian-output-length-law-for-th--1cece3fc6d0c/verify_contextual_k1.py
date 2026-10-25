"""Direct finite checks for the threshold-one contextual deletion channel.

Input convention: delete the first symbol of every maximal constant run
except the initial run, with positions determined on the original word.
"""
from itertools import product
from math import comb


def observation(x):
    if not x:
        raise ValueError('nonempty input required')
    return (x[0],) + tuple(x[i] for i in range(1, len(x)) if x[i] == x[i-1])


def changes(y):
    return sum(a != b for a, b in zip(y, y[1:]))


def expected_histogram(n, q):
    return {
        m: sum(q * (q-1)**j * comb(m-1, j)
               for j in range(min(m-1, n-m) + 1))
        for m in range(1, n+1)
    }


def direct_histogram(n, q):
    image = {observation(x) for x in product(range(q), repeat=n)}
    assert all(len(y)+changes(y) <= n for y in image)
    # For each possible received length, verify equality of the full image sets.
    predicted = {y for m in range(1,n+1)
                 for y in product(range(q),repeat=m)
                 if m+changes(y)<=n}
    assert image==predicted, (n,q, image ^ predicted)
    return {m: sum(len(y)==m for y in image) for m in range(1,n+1)}


if __name__ == '__main__':
    total_inputs=0
    cases=0
    for q, nmax in [(2, 12), (3, 9), (4, 7), (5, 6)]:
        for n in range(1,nmax+1):
            direct=direct_histogram(n,q)
            predicted=expected_histogram(n,q)
            assert direct==predicted, (n,q,direct,predicted)
            total_inputs += q**n
            cases += 1
        print('q', q, 'max_length', nmax, 'last_histogram', expected_histogram(nmax,q))
    print('verified_parameter_pairs',cases)
    print('source_words_examined',total_inputs)
    print('VERIFY_OK')
