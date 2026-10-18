"""Exhaustive checks of Peirce-right-fiber spectra for layered finite posets."""
from collections import Counter
from itertools import product


def compositions(n):
    for separators in range(1 << (n-1)):
        widths, current = [], 1
        for j in range(n-1):
            if separators & (1 << j):
                widths.append(current)
                current = 1
            else:
                current += 1
        yield tuple(widths + [current])


def verify(widths, crosscheck_residual):
    levels = tuple(k for k, width in enumerate(widths) for _ in range(width))
    n = len(levels)
    whole = (1 << n) - 1
    masks = [sum(1 << j for j, level in enumerate(levels) if level == k)
             for k in range(len(widths))]
    ascending = [mask for mask in range(1 << n)
                 if all(not(mask & (1 << i)) or (mask & (1 << j))
                        for i in range(n) for j in range(n) if levels[i] < levels[j])]
    is_upset = set(ascending)
    a = [(1 << v) - 1 for v in widths]
    N = 1+sum(a)
    assert len(ascending) == N
    up = [sum(1 << j for j in range(n) if i == j or levels[i] < levels[j])
          for i in range(n)]

    def implication(u, v):
        return sum(1 << i for i in range(n) if not (up[i] & u & ~v))

    hist = Counter()
    failed = 0
    checks = 0
    for u in ascending:
        if u == 0 or u == whole:
            threshold = 0
        else:
            first_level = next(i for i, mask in enumerate(masks) if u & mask)
            partial = (u & masks[first_level]) != masks[first_level]
            threshold = sum(masks[first_level+1:]) if partial else sum(masks[first_level:])
        actual = set()
        for v in ascending:
            pass_peirce = implication(implication(u, v), u) == u
            if pass_peirce:
                actual.add(v)
            assert pass_peirce == ((v & threshold) == threshold), (widths,u,v,threshold)
            failed += not pass_peirce
            checks += 1
            if crosscheck_residual:
                # Independent implication calculation via the residuation maximum.
                f = 0
                for w in ascending:
                    if (w & u) & ~v == 0:
                        f |= w
                assert f == implication(u,v)
        hist[len(actual)] += 1
    predicted = Counter({1+sum(a[:i+1]):a[i] for i in range(len(a)-1)})
    predicted[N] = a[-1]+1
    assert hist == predicted, (widths,hist,predicted)
    assert failed == sum(a[i]*a[j] for i in range(len(a)) for j in range(i+1,len(a)))

    # Decode the entire ordered level-size sequence from the univariate polynomial.
    coefficients = [hist[k] for k in sorted(hist)]
    decoded = []
    for count in coefficients[:-1]:
        assert count + 1 > 0 and (count+1).bit_count() == 1
        decoded.append((count+1).bit_length()-1)
    assert coefficients[-1].bit_count() == 1
    decoded.append(coefficients[-1].bit_length()-1)
    assert tuple(decoded) == widths
    return checks


def main():
    families = pairs = direct = 0
    for n in range(1,9):
        for widths in compositions(n):
            cross = n <= 5
            pairs += verify(widths, cross)
            families += 1
            direct += int(cross)
    for widths in [(8,1,1),(2,7,2),(3,4,1,2),(1,1,7),(6,4)]:
        pairs += verify(widths, False)
        families += 1
    print('VERIFY_OK families=%d peirce_pairs=%d direct_residuation_families=%d' % (families,pairs,direct))

if __name__=='__main__':
    main()
