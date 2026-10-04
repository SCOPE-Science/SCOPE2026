from collections import defaultdict
from itertools import product
from math import comb


def profile(w):
    out = [0, 0, 0, 0]
    index = {"00": 0, "01": 1, "10": 2, "11": 3}
    for i in range(len(w) - 1):
        out[index[w[i:i+2]]] += 1
    return tuple(out)


def q_formula(n):
    if n % 2 == 0:
        m = n // 2
        return 3*m*m - m + 2
    m = (n - 1) // 2
    return 3*m*m + 2*m + 2


def singleton_formula(n):
    return 2*n + (2 if n >= 4 and n % 2 == 0 else 0)


def feasible_profiles(n):
    N = n - 1
    ans = {(N, 0, 0, 0), (0, 0, 0, N)}
    # Equal transition counts, with at least one transition in each direction.
    for k in range(1, N // 2 + 1):
        rem = N - 2*k
        for a in range(rem + 1):
            ans.add((a, k, k, rem-a))
    # Start 0, end 1; and the reversed endpoint orientation.
    for k in range((N - 1) // 2 + 1):
        rem = N - (2*k + 1)
        for a in range(rem + 1):
            ans.add((a, k+1, k, rem-a))
            ans.add((a, k, k+1, rem-a))
    return ans


def predicted_class_size(p):
    a, b, c, d = p
    if b == c == 0:
        return 1
    if b == c:
        k = b
        # Start/end 0 plus start/end 1.
        return comb(a+k, k)*comb(d+k-1, k-1) + comb(a+k-1, k-1)*comb(d+k, k)
    if b == c + 1:
        k = c
        return comb(a+k, k)*comb(d+k, k)
    if c == b + 1:
        k = b
        return comb(a+k, k)*comb(d+k, k)
    return 0


def expected_singletons(n):
    ans = {"0"*n, "1"*n}
    for a in range(1, n):
        ans.add("0"*a + "1"*(n-a))
        ans.add("1"*a + "0"*(n-a))
    if n >= 4 and n % 2 == 0:
        ans.add("01"*(n//2))
        ans.add("10"*(n//2))
    return ans

words_checked = 0
profiles_checked = 0
for n in range(2, 17):
    classes = defaultdict(list)
    for bits in product("01", repeat=n):
        w = "".join(bits)
        classes[profile(w)].append(w)
        words_checked += 1
    observed = set(classes)
    generated = feasible_profiles(n)
    assert observed == generated
    assert len(observed) == q_formula(n)
    profiles_checked += len(observed)
    for p, ws in classes.items():
        assert len(ws) == predicted_class_size(p), (n, p, len(ws), predicted_class_size(p))
    singleton_words = {ws[0] for ws in classes.values() if len(ws) == 1}
    assert singleton_words == expected_singletons(n)
    assert len(singleton_words) == singleton_formula(n)

# A larger arithmetic-only check of the feasible-profile count.
for n in range(2, 201):
    assert len(feasible_profiles(n)) == q_formula(n)

print(f"VERIFY_OK exhaustive_words={words_checked} exhaustive_profiles={profiles_checked} n=2..16 arithmetic_n<=200")
