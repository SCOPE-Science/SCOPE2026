"""Exhaustive computational checks for shortest one-wildcard subsequence covers.

Usage: python verify.py
Requires only the Python 3 standard library.
"""
from itertools import combinations, permutations, product
from math import factorial


def matched_greedy(host, target):
    j = 0
    for a in host:
        if j < len(target) and (a == '?' or a == target[j]):
            j += 1
    return j == len(target)


def matched_dp(host, target):
    reachable = {0}
    for a in host:
        future = set(reachable)
        for j in reachable:
            if j < len(target) and (a == '?' or a == target[j]):
                future.add(j + 1)
        reachable = future
    return len(target) in reachable


def all_balanced_words(q, k):
    # Build exactly k-1 occurrences of each symbol, without duplicates.
    sym = ''.join(str(i) for i in range(q))
    counts = [k - 1] * q
    def rec(acc):
        if sum(counts) == 0:
            yield ''.join(acc)
            return
        for j in range(q):
            if counts[j]:
                counts[j] -= 1
                acc.append(sym[j])
                yield from rec(acc)
                acc.pop()
                counts[j] += 1
    yield from rec([])


def predicted(host, q):
    n = len(host)
    pos = host.index('?')
    k_minus_1, rem = divmod(n - 1, q)
    assert rem == 0
    if pos % q:
        return False
    ordinary = host.replace('?', '')
    return all(set(ordinary[i:i+q]) == set('0123456789'[:q])
               for i in range(0, len(ordinary), q))


def verify(q, k):
    alphabet = '0123456789'[:q]
    patterns = list(product(alphabet, repeat=k))
    n = q*(k-1)+1
    total = 0
    positive = 0
    for fixed in all_balanced_words(q, k):
        for pos in range(n):
            word = fixed[:pos] + '?' + fixed[pos:]
            total += 1
            actual = all(matched_greedy(word, pat) for pat in patterns)
            expected = predicted(word, q)
            assert actual == expected, (q, k, word, actual, expected)
            positive += actual
    correct = k * factorial(q)**(k-1)
    assert positive == correct, (q, k, positive, correct)
    return total, positive


def test_matcher_independence():
    checked=0
    for q,k in [(2,2),(2,3),(2,4),(3,2),(3,3)]:
        alphabet = '012'[:q]
        for host in product(alphabet+'?', repeat=q*k):
            if host.count('?') != 1:
                continue
            for p in product(alphabet,repeat=k):
                assert matched_greedy(host,p) == matched_dp(host,p)
                checked+=1
    return checked


def run():
    vals = []
    for q,ks in [(2,range(1,8)),(3,range(1,5)),(4,range(1,4)),(5,range(1,3)),(6,range(1,3))]:
        for k in ks:
            total,positive=verify(q,k)
            vals.append((q,k,total,positive))
            print('CHECK',q,k,total,positive)
    m=test_matcher_independence()
    print('VERIFY_OK parameter_cases=%d exhaustive_hosts=%d satisfying_hosts=%d matcher_agreement_cases=%d' %
          (len(vals),sum(x[2] for x in vals),sum(x[3] for x in vals),m))

if __name__=='__main__':
    run()
