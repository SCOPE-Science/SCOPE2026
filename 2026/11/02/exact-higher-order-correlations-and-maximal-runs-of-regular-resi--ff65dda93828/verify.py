#!/usr/bin/env python3
"""Exact finite corroboration of modular regular-residue pattern counts.

All arithmetic uses Python's standard library and integers; no network access.
The unbounded statements require the separate mathematical proof.
"""
import math
import random


def factor(n):
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            result.append((p, a))
        p += 1
    if n > 1:
        result.append((n, 1))
    return result


def regular(m, n):
    return math.gcd(m*m, n) == math.gcd(m, n)


def predicted(n, shifts):
    answer = 1
    for p, a in factor(n):
        q = p**a
        classes = {h % p for h in shifts}
        good = 0
        for c in classes:
            vals = {h % q for h in shifts if h % p == c}
            good += len(vals) == 1
        answer *= (p - len(classes))*p**(a-1) + good
    return answer


def direct(n, shifts):
    return sum(all(regular(m+h, n) for h in shifts) for m in range(n))


def predicted_consecutive(n, L):
    ans = 1
    for p, a in factor(n):
        if a == 1:
            c = p
        elif L <= p:
            c = (p-L)*p**(a-1)+L
        elif L <= 2*p:
            c = 2*p-L
        else:
            c = 0
        ans *= c
    return ans


def maximal(n):
    square_primes = [p for p, a in factor(n) if a >= 2]
    return None if not square_primes else 2*min(square_primes)-1


def main():
    random.seed(20261030)
    checks = 0
    run_checks = 0
    exact_run_checks = 0
    for n in range(2, 321):
        # Exhaust all contiguous lengths covering the theoretical boundary.
        B = maximal(n)
        upto = max(12, 2 + (B or 0)) if B else 12
        for L in range(1, upto + 1):
            expected = predicted_consecutive(n, L)
            observed = direct(n, range(L))
            assert observed == expected == predicted(n, range(L)), (n,L,observed,expected)
            if B is not None:
                assert (observed > 0) == (L <= B), (n,L,B,observed)
            else:
                assert observed == n, (n,L,observed)
            run_checks += 1
        if B is not None:
            for L in range(1, B + 1):
                # A maximal run is preceded and followed by a nonregular residue.
                count = 0
                for m in range(n):
                    if (not regular(m-1,n) and not regular(m+L,n)
                            and all(regular(m+i,n) for i in range(L))):
                        count += 1
                inferred = (predicted_consecutive(n,L)
                            - 2*predicted_consecutive(n,L+1)
                            + predicted_consecutive(n,L+2))
                assert inferred == count, (n,L,inferred,count)
                exact_run_checks += 1
        # Unstructured distinct and colliding offsets, including negative shifts.
        examples = [(-2, 0, 1, 4), (0, n, 2*n), (-n-3, -3, n-3),
                    (0, 1, 2, 3, 4, 5), (0,), (0, n+1, 2*n+2)]
        for _ in range(6):
            examples.append(tuple(random.sample(range(-3*n-3, 3*n+4), random.randrange(1, 9))))
        for shifts in examples:
            expected=predicted(n,shifts)
            actual=direct(n,shifts)
            assert actual==expected, (n,shifts,actual,expected)
            checks += 1
    examples={(4,3):1,(8,3):1,(9,5):1,(12,3):3,(36,3):3,(25,9):1}
    for (n,L),expected in examples.items():
        actual=direct(n,range(L))
        assert actual==expected,(n,L,actual,expected)
    print(f'VERIFY_OK moduli=319 arbitrary_patterns={checks} consecutive_patterns={run_checks} exact_run_histograms={exact_run_checks} example_cases={len(examples)} exact_integer=yes')

if __name__=='__main__':
    main()
