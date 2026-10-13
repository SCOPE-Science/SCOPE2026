#!/usr/bin/env python3
import math

assertions = 0

def check(cond):
    global assertions
    assertions += 1
    if not cond:
        raise AssertionError(f"assertion {assertions} failed")

def atom_count(first_size, second_size):
    return 4 + first_size + second_size * second_size

# Exact formulas and the source-certified feasibility constraints.
for n in range(0, 21):
    R = 1 << (n + 1)
    p, u, q = R, R, R + 1
    a = atom_count(p, u)
    b = atom_count(q, u)
    check(a == R*R + R + 4)
    check(b == R*R + R + 5)
    check(b == a + 1)
    # Since the complex algebra cardinalities are 2^a and 2^b,
    # b=a+1 means the larger algebra is exactly twice as large.
    check((1 << b) == 2 * (1 << a) if b < 10000 else b == a + 1)
    check(p >= R and q >= R)
    check(p <= u < q)

    # Any source-certified representable/nonrepresentable pair with common
    # second parameter u' has max atom count at least the claimed optimum.
    for du in range(0, 7):
        up = R + du
        pp = R
        qq = up + 1
        check(pp <= up < qq)
        check(pp >= R and qq >= R)
        check(atom_count(qq, up) >= b)

# Exhaustive bounded parameter search for small n.
for n in range(0, 7):
    R = 1 << (n + 1)
    best = None
    minimizers = []
    for u in range(2, R + 9):
        for p in range(R, R + 9):
            for q in range(R, R + 9):
                if (p <= u < q) or (q <= u < p):
                    m = max(atom_count(p, u), atom_count(q, u))
                    if best is None or m < best:
                        best = m
                        minimizers = [(p, q, u)]
                    elif m == best:
                        minimizers.append((p, q, u))
    check(best == R*R + R + 5)
    normalized = {tuple(sorted((p, q))) + (u,) for p, q, u in minimizers}
    check(normalized == {(R, R+1, R)})

# The simple half-log-log lower bound for the optimal larger witness.
for n in range(1, 21):
    R = 1 << (n + 1)
    exponent = R*R + R + 5  # log_2 of the larger algebra's size
    lower = 0.5 * math.log2(exponent) - 0.5
    check((n + 1) + 1e-12 >= lower)

print(f"VERIFY_OK {assertions} exact assertions")
