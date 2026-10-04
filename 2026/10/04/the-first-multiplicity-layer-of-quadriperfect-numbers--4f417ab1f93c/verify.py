#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations

TARGET = Fraction(4, 1)

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def next_prime(n):
    x = n + 1
    while not is_prime(x):
        x += 1
    return x

def first_primes(count, after=1):
    out = []
    p = next_prime(after)
    while len(out) < count:
        out.append(p)
        p = next_prime(p)
    return out

def abundancy_prime_power(p, e):
    return Fraction(p**(e+1)-1, p**e * (p-1))

def partitions(n, largest=None):
    if n == 0:
        yield ()
        return
    if largest is None or largest > n:
        largest = n
    for a in range(largest, 0, -1):
        for rest in partitions(n-a, a):
            yield (a,) + rest

def distinct_permutations(values):
    return set(permutations(values))

def max_for_partition(pattern):
    ps = first_primes(len(pattern))
    best = Fraction(0, 1)
    for assignment in distinct_permutations(pattern):
        value = Fraction(1, 1)
        for p, e in zip(ps, assignment):
            value *= abundancy_prime_power(p, e)
        if value > best:
            best = value
    return best

expected_lower = {
    1: Fraction(3,2),
    2: Fraction(2,1),
    3: Fraction(12,5),
    4: Fraction(14,5),
    5: Fraction(16,5),
    6: Fraction(192,55),
    7: Fraction(208,55),
}

global_maxima = {}
for total in range(1, 9):
    best = Fraction(0, 1)
    for pattern in partitions(total):
        best = max(best, max_for_partition(pattern))
    global_maxima[total] = best

assert {k:global_maxima[k] for k in range(1,8)} == expected_lower
assert all(global_maxima[k] < TARGET for k in range(1,8))

viable = {}
for pattern in partitions(8):
    bound = max_for_partition(pattern)
    if bound >= TARGET:
        viable[pattern] = bound

expected_viable = {
    (3,2,1,1,1): Fraction(312,77),
    (3,1,1,1,1,1): Fraction(576,143),
    (2,2,1,1,1,1): Fraction(224,55),
}
assert viable == expected_viable, viable

def max_future(last_prime, remaining):
    if not remaining:
        return Fraction(1, 1)
    ps = first_primes(len(remaining), after=last_prime)
    best = Fraction(0, 1)
    for assignment in distinct_permutations(remaining):
        value = Fraction(1, 1)
        for p, e in zip(ps, assignment):
            value *= abundancy_prime_power(p, e)
        best = max(best, value)
    return best

def search_pattern(pattern):
    solutions = []
    stats = {"nodes":0, "candidate_tests":0, "bound_breaks":0}

    def recurse(last_prime, remaining, product, chosen):
        stats["nodes"] += 1
        if not remaining:
            if product == TARGET:
                solutions.append(tuple(chosen))
            return

        for e in sorted(set(remaining), reverse=True):
            rest = list(remaining)
            rest.remove(e)
            rest = tuple(rest)
            p = next_prime(last_prime)

            while True:
                stats["candidate_tests"] += 1
                product2 = product * abundancy_prime_power(p, e)

                if rest:
                    upper = product2 * max_future(p, rest)
                    if upper < TARGET:
                        stats["bound_breaks"] += 1
                        break
                    if product2 < TARGET:
                        recurse(p, rest, product2, chosen + [(p,e)])
                else:
                    if product2 == TARGET:
                        solutions.append(tuple(chosen + [(p,e)]))
                    if product2 < TARGET:
                        stats["bound_breaks"] += 1
                        break

                p = next_prime(p)

    recurse(1, tuple(pattern), Fraction(1,1), [])
    solutions = list(dict.fromkeys(solutions))
    return solutions, stats

search_results = {}
for pattern in expected_viable:
    solutions, stats = search_pattern(pattern)
    search_results[pattern] = (solutions, stats)

expected_solution = ((2,3),(3,2),(5,1),(7,1),(13,1))
assert search_results[(3,2,1,1,1)][0] == [expected_solution]
assert search_results[(3,1,1,1,1,1)][0] == []
assert search_results[(2,2,1,1,1,1)][0] == []

def sigma_from_factorization(factors):
    out = 1
    n = 1
    omega = 0
    for p,e in factors:
        n *= p**e
        omega += e
        out *= (p**(e+1)-1)//(p-1)
    return n, out, omega

n, sig, omega = sigma_from_factorization(expected_solution)
assert n == 32760
assert omega == 8
assert sig == 4*n == 131040

print("VERIFY_OK")
print("lower_maxima=" + ",".join(f"{m}:{global_maxima[m]}" for m in range(1,8)))
print("viable=" + ";".join(f"{pattern}:{bound}" for pattern,bound in viable.items()))
for pattern,(solutions,stats) in search_results.items():
    print(f"pattern={pattern} solutions={solutions} stats={stats}")
print(f"n={n} sigma={sig} Omega={omega}")
