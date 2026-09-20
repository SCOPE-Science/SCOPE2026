from itertools import product


def distinct_total(word):
    n = len(word)
    return sum(len({word[i:i+k] for i in range(n-k+1)}) for k in range(1, n+1))


def longest_repeat(word):
    n = len(word)
    best = 0
    for k in range(1, n+1):
        seen = set()
        repeated = False
        for i in range(n-k+1):
            w = word[i:i+k]
            if w in seen:
                repeated = True
                break
            seen.add(w)
        if repeated:
            best = k
    return best


def maximum_formula(n, d):
    return sum(min(d**k, n-k+1) for k in range(1, n+1))


def check_maximum(n, d):
    values = [distinct_total(w) for w in product(range(d), repeat=n)]
    observed = max(values)
    predicted = maximum_formula(n, d)
    assert observed == predicted
    return observed


def check_collision(d, k, r):
    total = d ** (k + r)
    equal = 0
    for block in product(range(d), repeat=k+r):
        if block[:k] == block[r:r+k]:
            equal += 1
    assert equal * (d**k) == total
    return equal, total


def check_lipschitz(n, d, L):
    good = [w for w in product(range(d), repeat=n) if longest_repeat(w) < L]
    good_set = set(good)
    c = L * (L - 1) // 2
    max_jump = 0
    for w in good:
        dw = distinct_total(w)
        for i in range(n):
            for a in range(d):
                if a == w[i]:
                    continue
                v = w[:i] + (a,) + w[i+1:]
                if v in good_set:
                    jump = abs(dw - distinct_total(v))
                    max_jump = max(max_jump, jump)
                    assert jump <= c
    return len(good), max_jump, c


print("maximum checks")
for d, nmax in [(2, 8), (3, 6)]:
    for n in range(1, nmax + 1):
        print(d, n, check_maximum(n, d))

print("overlapping collision checks")
for d in (2, 3):
    for k in range(1, 6):
        for r in range(1, k + 1):
            equal, total = check_collision(d, k, r)
            print(d, k, r, equal, total)

print("good-set Lipschitz checks")
for params in [(7, 2, 3), (8, 2, 4), (6, 3, 3)]:
    print(params, check_lipschitz(*params))
