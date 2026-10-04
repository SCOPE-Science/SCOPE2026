from fractions import Fraction
from itertools import permutations

S = Fraction(2, 5)

def gram(a, b):
    d = sum(x != y for x, y in zip(a, b))
    return S ** d

def perm_sign(p):
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else 1

def alt_vector(N, k):
    support = set(range(k + 1))
    out = {}
    for a in permutations(range(N), k):
        aset = set(a)
        if len(aset) == k and aset <= support:
            missing = next(iter(support - aset))
            out[a] = Fraction(perm_sign(a + (missing,)), 1)
        else:
            out[a] = Fraction(0, 1)
    return out

def check_k_lt_N(N, k):
    tuples = list(permutations(range(N), k))
    f = alt_vector(N, k)
    target = (1 - S) ** k
    assert any(v != 0 for v in f.values())
    for a in tuples:
        lhs = sum(gram(a, b) * f[b] for b in tuples)
        rhs = target * f[a]
        assert lhs == rhs, (N, k, a, lhs, rhs)

def check_k_eq_N(N):
    tuples = list(permutations(range(N)))
    v = {p: Fraction(perm_sign(p), 1) for p in tuples}
    target = (1 - S) ** (N - 1) * (1 + (N - 1) * S)
    for a in tuples:
        lhs = sum(gram(a, b) * v[b] for b in tuples)
        rhs = target * v[a]
        assert lhs == rhs, (N, a, lhs, rhs)

def check_success_identity(N):
    lhs = (1 - S) ** N + N * S * (1 - S) ** (N - 1)
    rhs = (1 - S) ** (N - 1) * (1 + (N - 1) * S)
    assert lhs == rhs

for N in range(3, 7):
    for k in range(2, N):
        check_k_lt_N(N, k)
    check_k_eq_N(N)
    check_success_identity(N)

print('VERIFY_OK')
