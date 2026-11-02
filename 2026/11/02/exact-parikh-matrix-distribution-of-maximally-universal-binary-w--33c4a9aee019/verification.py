"""Self-contained finite tests of a weighted-arch enumeration identity.
Run with Python >=3.9: python verification.py
All integer calculations are exact. Finite tests do not prove infinite claims.
"""
from collections import Counter
from itertools import combinations
from math import comb


def arch_index(word):
    count = 0
    first = None
    for ch in word:
        if first is None:
            first = ch
        elif ch != first:
            count += 1
            first = None
    return count


def direct_histogram(k, s):
    n = 2*k+s
    histogram = Counter()
    for a_positions in combinations(range(n), k):
        word = ['b'] * n
        for i in a_positions:
            word[i] = 'a'
        if arch_index(word) != k:
            continue
        previous_a = 0
        pairs = 0
        for ch in word:
            if ch == 'a':
                previous_a += 1
            else:
                pairs += previous_a
        histogram[pairs] += 1
    return histogram


def formula_histogram(k, s):
    # Independently evaluate the formal product by coefficient convolution.
    state = Counter({(0, 0): 1})
    for j in range(1, k+1):
        new = Counter()
        for (used, pairs), count in state.items():
            new[(used, pairs+1)] += count                  # ab arch
            for h in range(s-used+1):
                new[(used+h, pairs+(j-1)*h)] += count     # b^(h+1)a arch
        state = new
    out = Counter()
    for (used, pairs), count in state.items():
        out[comb(k,2) + pairs + k*(s-used)] += count     # trailing b suffix
    return out


def unconditional_count(k, s):
    return sum(comb(k,j)*comb(s+j,j) for j in range(k+1))


def main():
    checks = 0
    for k in range(1,8):
        for s in range(5):
            actual = direct_histogram(k,s)
            predicted = formula_histogram(k,s)
            assert actual == predicted, (k,s,actual,predicted)
            assert sum(predicted.values()) == unconditional_count(k,s)
            assert all(predicted[c] == predicted[k*(k+s)-c] for c in predicted)
            assert min(predicted) == comb(k,2)
            assert max(predicted) == k*(k+s)-comb(k,2)
            checks += 1
    for k in range(1,41):
        for s in range(4):
            predicted = formula_histogram(k,s)
            assert sum(predicted.values()) == unconditional_count(k,s)
            assert all(predicted[c] == predicted[k*(k+s)-c] for c in predicted)
            checks += 1
    print('PASS: 35 exhaustive binary-word histogram checks, 160 large exact-polynomial checks')
    print('PASS: exact totals, palindrome symmetry and extremal ab-pair support')
    for k,s in [(1,1),(3,1),(4,2),(7,4)]:
        h=formula_histogram(k,s)
        print(f'example k={k},s={s}, #universal={sum(h.values())}, #all={comb(2*k+s,k)}, #nonzero C={len(h)}')


if __name__=='__main__':
    main()
