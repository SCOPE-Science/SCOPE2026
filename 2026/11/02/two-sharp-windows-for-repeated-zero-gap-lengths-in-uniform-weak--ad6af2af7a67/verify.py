"""Finite exact checks for repeated zero-gap lengths in uniform weak compositions.

Run with Python 3 standard library: python verify.py.
These checks are consistency tests; asymptotic theorems require the written proof.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb

checks = 0

def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def compositions(total, parts):
    if parts == 0:
        if total == 0:
            yield ()
        return
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest

def gap_lengths(word):
    gaps = []
    length = 0
    for term in word:
        if term == 0:
            length += 1
        else:
            if length:
                gaps.append(length)
            length = 0
    if length:
        gaps.append(length)
    return gaps

def repeated_pair_count(word):
    counts = Counter(gap_lengths(word))
    return sum(v * (v-1) // 2 for v in counts.values())

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def support_facts():
    total_cases = 0
    for n in range(2, 9):
        for m in range(1, 8):
            total = choose(n+m-1, m)
            support_count = Counter()
            zero_total = 0
            zero_pairs = 0
            y_total = 0
            for comp in compositions(m, n):
                total_cases += 1
                k = sum(x > 0 for x in comp)
                z = n-k
                support_count[k] += 1
                zero_total += z
                zero_pairs += z*(z-1)
                y_total += repeated_pair_count(comp)
            check(sum(support_count.values()) == total, ('total', n, m))
            check(Fraction(zero_total, total) == Fraction(n*(n-1), n+m-1), ('mean zeros', n, m))
            check(Fraction(zero_pairs, total) == Fraction(n*(n-1)*(n-1)*(n-2), (n+m-1)*(n+m-2)), ('factorial zeros', n, m))
            for k in range(1, min(n,m)+1):
                predicted = choose(n,k)*choose(m-1,k-1)
                check(support_count[k] == predicted, ('support', n, m, k))
                # Given k occupied positions, the zero gaps are a uniform weak
                # composition of n-k into k+1 nonnegative parts.
                denom = choose(n,k)
                pair_numer = sum(choose(n-k-2*t+k-2,k-2) for t in range(1,(n-k)//2+1)) if k>=2 else 0
                expected_y = Fraction(choose(k+1,2)*pair_numer,denom) if k>=2 else Fraction(1 if (n-k)%2==0 and n-k>=2 else 0, denom) if k==1 else Fraction(0)
                # Direct support-subset enumeration is independent of the weak-composition weights.
                actual = sum(repeated_pair_count(tuple(int(i in support) for i in range(n)))
                             for support in combinations(range(n), k))
                check(Fraction(actual,denom) == expected_y, ('pair gaps',n,m,k,actual,expected_y))
            check(y_total >= 0, ('nonnegative',n,m))
    return total_cases


def pair_formula():
    # Uniform weak composition into k parts: exact two specified positive
    # equal entries, including k=2 as a boundary case.
    for k in range(2, 8):
        for N in range(0, 14):
            total = choose(N+k-1,k-1)
            true_count = sum(1 for word in compositions(N,k) if word[0]==word[1] and word[0]>0)
            if k==2:
                calculated = int(N % 2 == 0 and N >= 2)
            else:
                calculated = sum(choose(N-2*t+k-3,k-3) for t in range(1,N//2+1))
            check(Fraction(true_count,total)==Fraction(calculated,total), ('pair',k,N))

if __name__ == '__main__':
    enumerated = support_facts()
    pair_formula()
    print(f'PASS: {checks} exact identities, {enumerated} weak compositions enumerated.')
