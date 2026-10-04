#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement, permutations
from math import factorial

@lru_cache(maxsize=None)
def phi(vec):
    vec = tuple(v for v in vec if v > 0)
    if not vec:
        return Fraction(1, 1)
    s = len(vec)
    t = vec[-1]
    ans = Fraction(0, 1)
    for h, xh in enumerate(vec):
        ans += phi(tuple(v - xh for v in vec[h + 1:]))
    return ans / (s + t)

def edges(d):
    m = len(d)
    n = d[-1]
    A = tuple(('a', i + 1) for i in range(m))
    B = tuple(('b', j + 1) for j in range(n))
    E = set()
    for i, di in enumerate(d, 1):
        for j in range(1, di + 1):
            E.add((('a', i), ('b', j)))
            E.add((('b', j), ('a', i)))
    return A, B, E

def greedy(order, E):
    chosen = []
    chosen_set = set()
    for v in order:
        if all((v, u) not in E for u in chosen_set):
            chosen.append(v)
            chosen_set.add(v)
    return frozenset(chosen_set)

def corners(d):
    m = len(d)
    return [0] + [i for i in range(1, m) if d[i - 1] < d[i]] + [m]

def M_i(d, i):
    n = d[-1]
    di = 0 if i == 0 else d[i - 1]
    return frozenset([('a', h) for h in range(1, i + 1)] +
                     [('b', j) for j in range(di + 1, n + 1)])

def right_vec(d, i):
    m = len(d)
    n = d[-1]
    di = 0 if i == 0 else d[i - 1]
    out = []
    for j in range(n, di, -1):
        out.append(sum(1 for h in range(i, m) if d[h] >= j))
    return tuple(out)

def predicted_prob(d, i):
    left = phi(tuple(d[:i])) if i else Fraction(1, 1)
    right = phi(right_vec(d, i))
    return left * right

def all_connected_degree_sequences(m, n):
    # N(a_i)={b_1,...,b_{d_i}}; connected iff d_1>=1 and d_m=n.
    for d in combinations_with_replacement(range(1, n + 1), m):
        if d[-1] == n:
            yield d

def verify(limit_total=8):
    seq_count = 0
    perm_count = 0
    support_count = 0
    for total in range(2, limit_total + 1):
        for m in range(1, total):
            n = total - m
            for d in all_connected_degree_sequences(m, n):
                seq_count += 1
                A, B, E = edges(d)
                V = A + B
                brute = {}
                for order in permutations(V):
                    I = greedy(order, E)
                    brute[I] = brute.get(I, 0) + 1
                    perm_count += 1
                den = factorial(total)
                brute = {I: Fraction(c, den) for I, c in brute.items()}
                predicted = {M_i(d, i): predicted_prob(d, i) for i in corners(d)}
                if set(brute) != set(predicted):
                    raise AssertionError(("support", d, brute, predicted))
                for I, p in predicted.items():
                    if brute[I] != p:
                        raise AssertionError(("probability", d, I, brute[I], p))
                if sum(predicted.values(), Fraction(0, 1)) != 1:
                    raise AssertionError(("normalization", d, predicted))
                support_count += len(predicted)
    print(f"VERIFY_OK degree_sequences={seq_count} permutations={perm_count} support_points={support_count} max_total={limit_total}")

if __name__ == '__main__':
    verify()
