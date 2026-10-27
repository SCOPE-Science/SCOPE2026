"""Exact exhaustive certificate for five-letter right-crucial Abelian-square avoidance.

Runs on Python 3 with the standard library only.
"""
from collections import Counter
from math import factorial

EXPECTED = (
    '0102343104303', '0120324023024', '0120324023204',
    '0120343020343', '0120343104303', '0121343014313',
    '0123243024323', '0123243034232', '0123423024323',
    '0123423034232', '0123424023424', '0123424043242',
    '0123432024323', '0123432034232',
)
EXPECTED_SPECTRA = {
    (1, 2, 3, 5, 7): 3,
    (1, 2, 3, 6, 7): 8,
    (1, 2, 5, 6, 7): 1,
    (1, 4, 5, 6, 7): 2,
}


def exhaustive(q):
    """First-occurrence canonical words; checks equality of Parikh-prefix vectors."""
    assert 3 <= q <= 5
    n = 4*q - 7
    word = [0]
    zero = (0,)*q
    first = list(zero)
    first[0] = 1
    prefix = [zero, tuple(first)]
    nodes = 0
    squarefree_five_symbol_leaves = 0
    output = []

    def suffix_witnesses(p):
        length = len(p)-1
        ans = []
        for h in range(1, length//2 + 1):
            left, mid, right = p[length-2*h], p[length-h], p[length]
            if all(mid[c] - left[c] == right[c] - mid[c] for c in range(q)):
                ans.append(h)
        return tuple(ans)

    def recurse(largest):
        nonlocal nodes, squarefree_five_symbol_leaves
        nodes += 1
        if len(word) == n:
            if largest != q-1:
                return
            squarefree_five_symbol_leaves += 1
            witnesses = []
            for x in range(q):
                pnext = list(prefix[-1])
                pnext[x] += 1
                h = suffix_witnesses(prefix + [tuple(pnext)])
                if not h:
                    return
                witnesses.append(h)
            output.append((''.join(map(str, word)), tuple(witnesses)))
            return
        for x in range(min(q-1, largest+1) + 1):
            word.append(x)
            pnext = list(prefix[-1])
            pnext[x] += 1
            prefix.append(tuple(pnext))
            if not suffix_witnesses(prefix):
                recurse(max(largest, x))
            prefix.pop()
            word.pop()

    recurse(0)
    return nodes, squarefree_five_symbol_leaves, output


def verify():
    for q, expected_orbits in [(3, 1), (4, 5), (5, 14)]:
        nodes, leaves, result = exhaustive(q)
        assert len(result) == expected_orbits, (q, len(result))
        if q == 5:
            assert nodes == 297588 and leaves == 205424
            assert tuple(word for word, witness in result) == EXPECTED
            assert all(len(h) == 1 for word, witnesses in result for h in witnesses)
            signature_counts = Counter(tuple(sorted(h[0] for h in witnesses))
                                       for word, witnesses in result)
            assert dict(signature_counts) == EXPECTED_SPECTRA
            assert factorial(q) * len(result) == 1680
        print('alphabet', q, 'canonical_nodes', nodes,
              'squarefree_full', leaves, 'crucial_orbits', len(result))
    print('PASS: 14 complete five-letter orbits, 1680 labeled words, four signatures')


if __name__ == '__main__':
    verify()
