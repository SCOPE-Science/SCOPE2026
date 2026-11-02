"""Standalone checks and constructive witness generator for binary run-two circular covers.

Usage: python3 VERIFY.py
No dependencies beyond Python's standard library.
"""
from collections import Counter, defaultdict
from itertools import product


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def valid(word):
    return "000" not in word and "111" not in word


def target_words(k):
    return ["".join(p) for p in product("01", repeat=k) if valid("".join(p))]


def extra_words(targets):
    return [
        w for w in targets
        if w[0] != w[1] and w[-2] != w[-1]
        and any(w[i] == w[i + 1] for i in range(len(w) - 1))
    ]


def potential(v):
    # One-based location of the first equal adjacent pair; len(v) is the sentinel.
    return -next((i + 1 for i in range(len(v) - 1) if v[i] == v[i+1]), len(v))


def witness(k):
    targets = target_words(k)
    extras = extra_words(targets)
    out = defaultdict(list)
    for w in targets + extras:
        out[w[:-1]].append(w[1:])
    for v in out:
        out[v].sort(reverse=True)
    start = min(out)
    stack = [start]
    tour = []
    while stack:
        v = stack[-1]
        if out[v]:
            stack.append(out[v].pop())
        else:
            tour.append(stack.pop())
    tour.reverse()
    assert len(tour) == len(targets) + len(extras) + 1
    assert tour[0] == tour[-1]
    return "".join(v[0] for v in tour[:-1]), targets, extras


def check(k):
    word, targets, extras = witness(k)
    target_set = set(targets)
    extra_set = set(extras)
    assert len(targets) == 2 * fibonacci(k+1)
    assert len(extras) == 2 * (fibonacci(k-1) - 1)
    assert len(word) == 2 * (fibonacci(k-1) + fibonacci(k+1)) - 2
    assert valid(word + word[:2]), "The witness must satisfy the cyclic run constraint"
    observed = Counter((word + word[:k-1])[i:i+k] for i in range(len(word)))
    assert set(observed) == target_set
    assert all(observed[w] == 1 + (w in extra_set) for w in targets)
    assert sum(observed.values()) == len(word)
    mandatory_balance = defaultdict(int)
    residual_balance = defaultdict(int)
    for w in targets:
        mandatory_balance[w[:-1]] += 1
        mandatory_balance[w[1:]] -= 1
    for w in extras:
        residual_balance[w[:-1]] += 1
        residual_balance[w[1:]] -= 1
    assert all(mandatory_balance[v] + residual_balance[v] == 0 for v in set(mandatory_balance)|set(residual_balance))
    dual_value = sum(b*potential(v) for v,b in mandatory_balance.items())
    assert dual_value == len(extras)
    assert all(potential(w[1:]) - potential(w[:-1]) == 1 for w in extras)
    if k <= 14:
        assert all(
            potential(w[1:]) - potential(w[:-1]) <= 1
            for p in product("01", repeat=k)
            for w in ["".join(p)]
        )
    return len(targets), len(extras), len(word), word


def main():
    for k in range(3,19):
        num_required, repeated, optimum, example = check(k)
        print(f"k={k:2d}: required={num_required:6d}, additional={repeated:6d}, minimum={optimum:6d}")
        if k <= 6:
            print(" witness:", example)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
