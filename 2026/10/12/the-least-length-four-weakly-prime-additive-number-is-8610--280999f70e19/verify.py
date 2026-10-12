from itertools import combinations, product

LIMIT = 8610

spf = list(range(LIMIT + 1))
for i in range(2, int(LIMIT**0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, LIMIT + 1, i):
            if spf[j] == j:
                spf[j] = i


def distinct_prime_divisors(n):
    out = []
    while n > 1:
        p = spf[n]
        out.append(p)
        while n % p == 0:
            n //= p
    return out


def powers(p, n):
    out = []
    value = p
    exponent = 1
    while value < n:
        out.append((exponent, value))
        if value > (n - 1) // p:
            break
        value *= p
        exponent += 1
    return out


def representations(n, terms):
    primes = distinct_prime_divisors(n)
    answer = []
    if len(primes) < terms:
        return answer
    for chosen in combinations(primes, terms):
        pools = [powers(p, n) for p in chosen]
        for choice in product(*pools):
            if sum(value for _, value in choice) == n:
                answer.append(tuple((p, exponent, value)
                                    for p, (exponent, value) in zip(chosen, choice)))
    return answer


first = None
first_representations = None
for n in range(2, LIMIT + 1):
    four = representations(n, 4)
    if not four:
        continue
    three = representations(n, 3)
    if not three:
        first = n
        first_representations = four
        break

assert first == 8610, first
three = representations(8610, 3)
four = representations(8610, 4)
expected = ((3, 8, 6561), (5, 2, 25), (7, 3, 343), (41, 2, 1681))
assert three == [], three
assert four == [expected], four
assert sum(value for _, _, value in expected) == 8610
assert distinct_prime_divisors(8610) == [2, 3, 5, 7, 41]
print('VERIFY_OK first_length4=8610 three_reps=0 four_reps=1 '
      'factor_primes=2,3,5,7,41 witness=3^8+5^2+7^3+41^2')
