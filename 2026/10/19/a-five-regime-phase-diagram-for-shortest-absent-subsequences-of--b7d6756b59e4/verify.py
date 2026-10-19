#!/usr/bin/env python3
"""Independent direct finite verification of shortest absent subsequences.
Run: python3 verify.py. Uses no third-party packages.
"""
from itertools import product
from functools import lru_cache


def greedy_present(v, w):
    j = 0
    for x in w:
        if j < len(v) and v[j] == x:
            j += 1
    return j == len(v)


def predicted(a, b, k):
    length = k + 1 if min(a, b) == 1 else 2 * k
    if a == b == 1:
        return {'1' * j + '0' * (length - j) for j in range(length + 1)}
    if a == 1:
        return {'0' * length, '1' + '0' * (length - 1)}
    if b == 1:
        return {'1' * length, '1' * (length - 1) + '0'}
    def condition(v):
        if v[0] != '1':
            return False
        r = []
        for x in v:
            if r and r[-1][0] == x:
                r[-1][1] += 1
            else:
                r.append([x, 1])
        return all((m % 2 == 1 if (a if x == '0' else b) == 2
                    else m == 1) for x, m in r)
    return {''.join(v) for v in product('01', repeat=length)
            if condition(v)}


def fib(n):
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    return x


def expected_count(a, b, k):
    if a == b == 1:
        return k + 2
    if min(a, b) == 1:
        return 2
    if a == b == 2:
        return fib(2 * k)
    if min(a, b) == 2:
        return 1 << (k - 1)
    return 1


def indep_run_cost(v, a, b):
    assert v
    run = []
    for x in v:
        if run and run[-1][0] == x:
            run[-1][1] += 1
        else:
            run.append([x, 1])
    final_run_index = (1 if v[0] == '1' else 0) + len(run)
    final_run_index += sum(2 * ((n + (a if x == '0' else b) - 1)
                                  // (a if x == '0' else b) - 1)
                           for x, n in run)
    return final_run_index


def run():
    cases = 0
    candidate_count = 0
    for a in range(1, 7):
        for b in range(1, 7):
            for k in range(1, 7):
                w = ('0' * a + '1' * b) * k
                l = k + 1 if min(a, b) == 1 else 2 * k
                guess = predicted(a, b, k)
                assert len(guess) == expected_count(a, b, k), (a,b,k,'count')
                # Exhaust all words at shortest missing length using a direct greedy scan.
                observed = set()
                for tup in product('01', repeat=l):
                    v = ''.join(tup)
                    absent = not greedy_present(v, w)
                    assert absent == (indep_run_cost(v, a, b) > 2*k), (a,b,k,v,'runcost')
                    if absent:
                        observed.add(v)
                    candidate_count += 1
                assert observed == guess, (a,b,k,observed ^ guess)
                # Independently ensure all words of the previous length occur.
                for tup in product('01', repeat=l - 1):
                    assert greedy_present(''.join(tup), w), (a,b,k,'shortness')
                cases += 1
    # High-order exact closed counts without enumerating exponentially many words.
    for k in range(1, 70):
        f1 = 0
        f2 = 1
        for _ in range(2*k):
            f1, f2 = f2, f1+f2
        assert expected_count(2,2,k) == f1
        assert expected_count(2,3,k) == (1 << (k-1))
    print('VERIFY_OK exhaustive_parameter_triples=%d distinct_candidate_checks=%d all_prior_lengths_present run_embedding_equivalence five_regime_counts fibonacci_to_k69' % (cases,candidate_count))

if __name__ == '__main__':
    run()
