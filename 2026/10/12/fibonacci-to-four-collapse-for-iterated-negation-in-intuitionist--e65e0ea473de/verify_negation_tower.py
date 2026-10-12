#!/usr/bin/env python3
from __future__ import annotations

NEG = {
    "T": ("F",),
    "U": ("U", "T"),
    "F": ("U", "T"),
}

checks = 0

def check(cond, msg="assertion failed"):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def initial_rows(n: int):
    rows = [("T",), ("F",)]
    for _ in range(n):
        rows = [row + (y,) for row in rows for y in NEG[row[-1]]]
    return rows

def supported(v, rows):
    tpos = tuple(i for i, x in enumerate(v) if x == "T")
    for i, x in enumerate(v):
        if x != "U":
            continue
        ok = False
        for w in rows:
            if w[i] == "F" and all(w[j] == "T" for j in tpos):
                ok = True
                break
        if not ok:
            return False
    return True

def prune(rows):
    cur = list(rows)
    cycles = 0
    while True:
        nxt = [v for v in cur if supported(v, cur)]
        if len(nxt) == len(cur):
            return cur, cycles
        cur = nxt
        cycles += 1

def A(n):
    return tuple("T" if i % 2 == 0 else "F" for i in range(n + 1))

def B(n):
    return ("F",) + ("U",) * n

def C(n):
    assert n >= 1
    return ("F", "U") + tuple("T" if i % 2 == 0 else "F" for i in range(2, n + 1))

def D(n):
    return tuple("F" if i % 2 == 0 else "T" for i in range(n + 1))

# Direct exhaustive generation plus the source's support-deletion test.
for n in range(0, 14):
    rows = initial_rows(n)
    check(len(set(rows)) == len(rows), f"duplicate initial row at n={n}")
    check(len(rows) == fib(n + 3), f"initial count at n={n}")

    if n >= 1:
        dist = {x: sum(r[-1] == x for r in rows) for x in "TUF"}
        check(dist["T"] == fib(n + 1), f"T count at n={n}")
        check(dist["U"] == fib(n + 1), f"U count at n={n}")
        check(dist["F"] == fib(n), f"F count at n={n}")

    final, cycles = prune(rows)
    expected_size = 2 if n == 0 else 3 if n == 1 else 4
    check(len(final) == expected_size, f"final size at n={n}")
    if n >= 2:
        expected = {A(n), B(n), C(n), D(n)}
        check(set(final) == expected, f"final rows at n={n}")
        check(cycles <= 2, f"too many pruning cycles at n={n}")

        first = [v for v in rows if supported(v, rows)]
        expected_first = {A(n), B(n), D(n)}
        for k in range(1, n):
            # F, followed by k U's, then the forced alternating tail.
            v = ("F",) + ("U",) * k
            for i in range(k + 1, n + 1):
                v += ("T" if (i - (k + 1)) % 2 == 0 else "F",)
            expected_first.add(v)
        check(set(first) == expected_first, f"first-prune normal form at n={n}")

# Pure recurrence checks far beyond the exhaustive window.
t, u, f = 1, 0, 1
for n in range(0, 201):
    check(t + u + f == fib(n + 3), f"recurrence total at n={n}")
    if n >= 1:
        check((t, u, f) == (fib(n + 1), fib(n + 1), fib(n)),
              f"recurrence distribution at n={n}")
    check(t + u + f <= 2 ** (n + 1), f"generic upper bound at n={n}")
    t, u, f = u + f, u + f, t

# Exact golden-ratio recurrence identity R_{n+1}=R_n+R_{n-1}.
R = [fib(n + 3) for n in range(0, 202)]
for n in range(1, 201):
    check(R[n + 1] == R[n] + R[n - 1], f"Fibonacci recurrence at n={n}")

print(f"VERIFY_OK {checks} exact assertions")
