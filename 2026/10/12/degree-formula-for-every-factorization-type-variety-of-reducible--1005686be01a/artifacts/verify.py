import math
from collections import Counter

def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for rest in partitions(n-first, first):
            yield (first,) + rest

def factor_dim(m, e):
    return math.comb(m+e-1, m-1) - 1

def degree_formula(m, lam):
    Ns = [factor_dim(m,e) for e in lam]
    D = sum(Ns)
    top = math.factorial(D)
    for N in Ns:
        top //= math.factorial(N)
    sym = 1
    for mult in Counter(lam).values():
        sym *= math.factorial(mult)
    assert top % sym == 0
    return top // sym, top, sym

checked = 0
for m in range(3,8):
    for d in range(2,11):
        for lam in partitions(d):
            if len(lam) < 2:
                continue
            deg, top, sym = degree_formula(m, lam)
            assert deg * sym == top
            checked += 1

            if all(e == 1 for e in lam):
                q = len(lam)
                known = math.factorial(q*(m-1)) // (
                    math.factorial(q) * math.factorial(m-1)**q
                )
                assert deg == known

        lam = (d-1,1)
        deg, _, _ = degree_formula(m, lam)
        if d == 2:
            closed = math.comb(2*m-2, m-1)//2
        else:
            D = math.comb(m+d-2, m-1) + m - 2
            closed = math.comb(D, m-1)
        assert deg == closed

assert degree_formula(3,(1,1))[0] == 3
assert degree_formula(4,(1,1))[0] == 10
assert degree_formula(3,(2,1))[0] == 21
assert degree_formula(4,(2,1))[0] == 220

print("VERIFY_OK", checked)
