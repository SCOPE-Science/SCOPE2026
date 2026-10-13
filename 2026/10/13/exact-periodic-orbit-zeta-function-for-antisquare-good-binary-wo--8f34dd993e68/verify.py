#!/usr/bin/env python3
"""Exact, dependency-free checks for the antisquare-good periodic-orbit formula.

Run with Python 3 from any directory. Uses only Python's standard library.
The finite matrix identities are exact, not floating-point approximations.
"""
from itertools import product
from math import comb

F = ("0011", "1100", "0110", "1001", "010101", "101010", "001011", "110100")
G = ("010", "101", "11111", "01110")
H = (1, -1, 0, 0, -1, 0, -1)  # det(I-zA) = 1-z-z^4-z^6


def avoids(word, forbidden):
    return all(pattern not in word for pattern in forbidden)


def graph(forbidden):
    m = max(map(len, forbidden))
    names = ["".join(s) for s in product("01", repeat=m-1)
             if avoids("".join(s), forbidden)]
    index = {name: i for i, name in enumerate(names)}
    matrix = [[0]*len(names) for _ in names]
    edges = {}
    for name in names:
        row = []
        for letter in "01":
            longer = name + letter
            if avoids(longer, forbidden):
                nxt = longer[1:]
                matrix[index[name]][index[nxt]] += 1
                row.append((letter, nxt))
        edges[name] = row
    return names, matrix, edges


def matmul(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            a = A[i][k]
            if a:
                for j in range(n):
                    if B[k][j]:
                        C[i][j] += a * B[k][j]
    return C


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def traces(A, N):
    cur = identity(len(A))
    ans = []
    for _ in range(N):
        cur = matmul(cur, A)
        ans.append(sum(cur[i][i] for i in range(len(A))))
    return ans


def determinant_polynomial_from_traces(A):
    # Exact Newton identities for det(I-zA) (degree at most dimension).
    d = len(A)
    power_sums = traces(A, d)
    coefficients = [1]
    for k in range(1, d+1):
        numerator = sum(coefficients[k-j] * power_sums[j-1]
                        for j in range(1, k+1))
        assert numerator % k == 0
        coefficients.append(-numerator // k)
    return coefficients, power_sums


def poly_product(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def has_cyclic_forbidden(w, forbidden):
    if not w:
        raise ValueError('nonempty required')
    maxlen = max(map(len, forbidden))
    extension = (w * (1 + (maxlen-1 + len(w)-1)//len(w)))
    return any(extension[i:i+len(bad)] == bad
               for i in range(len(w)) for bad in forbidden)


def pansiot(w):
    return ''.join(str(int(w[i] != w[(i+1) % len(w)]))
                   for i in range(len(w)))


def is_periodic_antisquare_good(w, order_cap):
    # Independent direct period-by-period antisquare check.
    n = len(w)
    extension = w*((2*order_cap+n)//n+2)
    for order in range(2, order_cap+1):
        for i in range(n):
            u = extension[i:i+order]
            v = extension[i+order:i+2*order]
            if all(u[j] != v[j] for j in range(order)):
                return False
    return True


def is_primitive(w):
    n = len(w)
    return all(w != w[:d]*(n//d) for d in range(1, n)
               if n % d == 0)


names, A, edges = graph(G)
assert names == ["0000", "0001", "0011", "0110", "0111",
                 "1000", "1001", "1100", "1110", "1111"]
assert edges == {
    '0000': [('0', '0000'), ('1', '0001')],
    '0001': [('1', '0011')],
    '0011': [('0', '0110'), ('1', '0111')],
    '0110': [('0', '1100')],
    '0111': [('1', '1111')],
    '1000': [('0', '0000'), ('1', '0001')],
    '1001': [('1', '0011')],
    '1100': [('0', '1000'), ('1', '1001')],
    '1110': [('0', '1100')],
    '1111': [('0', '1110')],
}
polya, tr = determinant_polynomial_from_traces(A)
assert polya == list(H)+[0]*(len(A)-len(H)+1), polya
assert tr == [1, 1, 1, 5, 6, 13, 15, 21, 28, 46]

binary_names, B, _ = graph(F)
poly_b, tr_binary = determinant_polynomial_from_traces(B)
assert len(binary_names) == 20
assert poly_b == poly_product(H, H)+[0]*(len(B)+1-len(poly_product(H, H)))

# Exact finite traces from two different graph presentations agree.
trace_a = traces(A, 40)
trace_b = traces(B, 40)
assert all(trace_b[i] == 2*trace_a[i] for i in range(40))
assert trace_b[:12] == [2,2,2,10,12,26,30,42,56,92,134,202]

# A direct cyclic-word enumeration, independent of transfer matrices.
for n in range(1, 17):
    cyclic_binary_good = 0
    cyclic_code_good = 0
    for bits in product('01', repeat=n):
        w = ''.join(bits)
        if not has_cyclic_forbidden(w, F):
            cyclic_binary_good += 1
            assert not has_cyclic_forbidden(pansiot(w), G)
        if not has_cyclic_forbidden(w, G):
            cyclic_code_good += 1
            assert w.count('1') % 2 == 0
    assert cyclic_binary_good == trace_b[n-1], (n, cyclic_binary_good, trace_b[n-1])
    assert cyclic_code_good == trace_a[n-1], (n, cyclic_code_good, trace_a[n-1])

# Direct antisquare check through a large multiple of each tested period.
for n in range(1, 11):
    for bits in product('01', repeat=n):
        w = ''.join(bits)
        assert is_periodic_antisquare_good(w, 2*n+6) == (not has_cyclic_forbidden(w, F)), (n, w)

# The unique 1-block in the cyclic code 11 0^(n-2) forces full period n;
# the even-parity Pansiot lift has the same least period.
for n in range(4, 301):
    c = '11' + '0'*(n-2)
    assert not has_cyclic_forbidden(c, G)
    assert is_primitive(c)
    bits = [0]
    for i in range(n-1):
        bits.append(bits[-1] ^ int(c[i]))
    w = ''.join(map(str,bits))
    assert (bits[-1] ^ int(c[-1])) == bits[0]
    assert not has_cyclic_forbidden(w, F)
    assert is_primitive(w)

print('VERIFY_OK code_states=10 binary_states=20 '
      'det_code=1-z-z4-z6 det_binary=(1-z-z4-z6)^2 '
      'exact_trace_identity_n<=40 cyclic_enumeration_n<=16 '
      'direct_antisquares_n<=10_order<=2n+6 primitive_witness_n=4..300')
