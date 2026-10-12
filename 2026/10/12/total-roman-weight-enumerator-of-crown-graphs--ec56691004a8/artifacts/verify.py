from itertools import product
from collections import Counter
from math import comb


def valid(n, lab):
    # Vertices 0..n-1 are a_i and n..2n-1 are b_i; a_i b_i is the deleted matching.
    pos = [z > 0 for z in lab]
    for i in range(n):
        if lab[i] == 0 and not any(lab[n+j] == 2 for j in range(n) if j != i):
            return False
        if lab[n+i] == 0 and not any(lab[j] == 2 for j in range(n) if j != i):
            return False
    for i in range(n):
        if pos[i] and not any(pos[n+j] for j in range(n) if j != i):
            return False
        if pos[n+i] and not any(pos[j] for j in range(n) if j != i):
            return False
    return True


def mul(a, b):
    c = Counter()
    for i, ai in a.items():
        for j, bj in b.items():
            c[i+j] += ai*bj
    return c


def add(*arrs):
    c = Counter()
    for a in arrs:
        for k, v in a.items():
            c[k] += v
    return Counter({k:v for k,v in c.items() if v})


def sub(a, b):
    c = Counter(a)
    for k, v in b.items():
        c[k] -= v
    return Counter({k:v for k,v in c.items() if v})


def shift(a, s, m=1):
    return Counter({k+s:m*v for k,v in a.items()})


def binpoly(n):
    return Counter({k:comb(n,k) for k in range(n+1)})


def trinpoly(n):
    p = Counter({0:1})
    q = Counter({0:1,1:1,2:1})
    for _ in range(n):
        p = mul(p,q)
    return p


def formula(n):
    one = Counter({0:1})
    P = binpoly(n)
    A = sub(sub(P, one), Counter({1:n}))
    E = sub(binpoly(n-1), one)
    C = shift(E, 2)
    H = sub(sub(trinpoly(n), P), shift(binpoly(n-1), 2, n))
    diff = sub(trinpoly(n-1), binpoly(n-1))
    R = sub(mul(Counter({1:1,2:1}), diff), shift(binpoly(n-2), 3, n-1))
    return add(
        Counter({2*n:1}),
        shift(E, n+2, 2*n),
        shift(mul(A,A), n, 2),
        shift(mul(E,E), 4, n),
        shift(binpoly(2*n-4), 6, n*(n-1)),
        shift(mul(C,R), 0, 2*n),
        mul(H,H),
    )

labelings = valid_functions = coefficient_checks = minimum_checks = 0
for n in range(3,7):
    brute = Counter()
    for lab in product(range(3), repeat=2*n):
        labelings += 1
        if valid(n, lab):
            brute[sum(lab)] += 1
            valid_functions += 1
    closed = formula(n)
    coefficient_checks += len(set(brute) | set(closed))
    if brute != closed:
        raise SystemExit('POLYNOMIAL_MISMATCH n=%d brute=%r formula=%r' % (n, brute, closed))
    g = min(brute)
    expected_count = 31 if n == 3 else n*n*(n-1)
    if g != 6 or brute[g] != expected_count:
        raise SystemExit('MINIMUM_MISMATCH n=%d got=(%d,%d) expected=(6,%d)' % (n,g,brute[g],expected_count))
    minimum_checks += 1
print('VERIFY_OK n_range=3..6 labelings=%d valid_functions=%d coefficient_checks=%d minimum_checks=%d max_order=12' %
      (labelings, valid_functions, coefficient_checks, minimum_checks))
