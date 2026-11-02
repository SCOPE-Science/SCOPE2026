"""Independent finite checks for the paperfolding dyadic 2-Abelian spectrum.

Python 3, standard library only. Finite checks are not a proof of all levels.
"""
from collections import Counter


def bit_from_odd_part(position_one_based):
    assert position_one_based >= 1
    while position_one_based % 2 == 0:
        position_one_based //= 2
    return (position_one_based % 4) // 2


def paperfolding_by_recurrence(length):
    a = [0] * length
    for t in range(length):
        if t % 2 == 0:
            a[t] = (t // 2) % 2
        else:
            a[t] = a[t // 2]
    return ''.join(map(str, a))


def cyclic_skeleton(length, x, y):
    a = list(paperfolding_by_recurrence(length))
    a[length // 2 - 1] = str(y)
    a[length - 1] = str(x)
    return ''.join(a)


def spectrum_signature(word):
    pairs = Counter(word[i:i + 2] for i in range(len(word) - 1))
    return (word[0], word[-1], *(pairs[t] for t in ('00','01','10','11')))


def cyclic_pair_counts(word):
    pairs = Counter(word[i] + word[(i + 1) % len(word)] for i in range(len(word)))
    return tuple(pairs[t] for t in ('00','01','10','11'))


def test_level(k):
    n = 2 ** k
    q = n // 4
    samples = paperfolding_by_recurrence(64 * n + n)
    actual = {samples[i:i + n] for i in range(64 * n + 1)}
    catalog = set()
    count_by_signature = Counter()
    for x in (0,1):
        for y in (0,1):
            c = cyclic_skeleton(n,x,y)
            h=x+y
            assert cyclic_pair_counts(c) == (q+1-h,q,q,q-1+h)
            for shift in range(n):
                word = c[shift:] + c[:shift]
                assert word not in catalog, ('duplicate canonical factor',k,x,y,shift)
                catalog.add(word)
                count_by_signature[spectrum_signature(word)] += 1
    assert len(catalog) == 4*n
    assert actual == catalog, (k,len(actual),len(catalog),len(actual.symmetric_difference(catalog)))
    assert len(count_by_signature) == 12
    multiplicities = Counter(count_by_signature.values())
    assert multiplicities == Counter({q-1:2,q:4,q+1:2,2*q:4}), (k,multiplicities)
    # Exact endpoint and high-marker sum specification.
    expected = Counter()
    for a in '01':
        for b in '01':
            for h in (0,1,2):
                key = (a,b,
                       (q+1-h if h!=1 else q)-int(b=='0' and a=='0'),
                       (q if h!=1 else q)-int(b=='0' and a=='1'),
                       (q if h!=1 else q)-int(b=='1' and a=='0'),
                       (q-1+h if h!=1 else q)-int(b=='1' and a=='1'))
                # For h=1 the two skeletons have identical signature but
                # their circular pair COUNTS ARE q, not 2q.
                expected[key] = (2 if h==1 else 1)*(q + (1-h if b=='0' and a=='0' else h-1 if b=='1' and a=='1' else 0))
    assert count_by_signature == expected, (k, count_by_signature-expected,expected-count_by_signature)
    return (n,len(catalog),len(count_by_signature),sorted(multiplicities.items()))


if __name__ == '__main__':
    for k in range(4,11):
        print(test_level(k))
    print('PASS: independent recurrence, canonical rotations, occurrence set, and exact 2-Abelian multiplicities.')
