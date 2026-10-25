"""Exact finite-state certificate for four-letter cyclic RC2 avoidance.
Requires Python 3.9+ only. Recomputes 64 matrix traces, Newton identities,
its characteristic polynomial, short direct enumeration, and necklace counts.
"""
from itertools import product
from math import gcd

Q = 4
N = Q ** 3
FORBIDDEN = {(a, b, Q-1-b, Q-1-a) for a in range(Q) for b in range(Q)}
assert len(FORBIDDEN) == Q * Q
# Edge i=(a,b,c) -> j=(b,c,d), except if abcd is a reverse-complement square.
OUT = [[] for _ in range(N)]
for a, b, c in product(range(Q), repeat=3):
    i = (a * Q + b) * Q + c
    for d in range(Q):
        if (a,b,c,d) not in FORBIDDEN:
            OUT[i].append((b * Q + c) * Q + d)

# Compute trace(A^n) for 1 <= n <= 64 exactly, by right multiplication.
B = [[int(i == j) for j in range(N)] for i in range(N)]
traces = [0]
for k in range(1, N + 1):
    C = [[0]*N for _ in range(N)]
    for i in range(N):
        ci, bi = C[i], B[i]
        for j in range(N):
            v = bi[j]
            if v:
                for h in OUT[j]:
                    ci[h] += v
    B = C
    traces.append(sum(B[i][i] for i in range(N)))

# Newton's identities: characteristic polynomial = X^N + sum(c_k X^(N-k)).
c = [1]
for k in range(1, N + 1):
    t = -sum(c[k-j] * traces[j] for j in range(1, k+1))
    assert t % k == 0
    c.append(t // k)

def mul(p, q):
    out = [0] * (len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j] += a*b
    return out

# Coefficients ordered from leading to constant term.
asserted = [1]
for poly, exponent in [
    ([1, -1], 3), ([1, 1], 3), ([1, 0, 1], 2),
    ([1, -3, -2, -3], 1),
    ([1, -1, 1, -4, 2, -3], 2),
    ([1, 1, 1, 4, 2, 3], 1),
    ([1, 0], 36),
]:
    for _ in range(exponent):
        asserted = mul(asserted, poly)
assert len(asserted) == N+1
assert c == asserted, '64x64 characteristic polynomial mismatch'

# Independent direct enumeration of every word of lengths 1,...,7.
for n in range(1, 8):
    count = 0
    for w in product(range(Q), repeat=n):
        if all(tuple(w[(i+j)%n] for j in range(4)) not in FORBIDDEN
               for i in range(n)):
            count += 1
    assert count == traces[n], (n, count, traces[n])

# Trace from a second computation with a characteristic recurrence.
for n in range(N+1, 90):
    # Cayley-Hamilton on traces of matrix powers.
    nxt = -sum(c[k] * traces[n-k] for k in range(1,N+1))
    traces.append(nxt)

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]
def mobius(n):
    p = 2
    k = n
    out = 1
    while p*p <= k:
        if k % p == 0:
            k//=p
            out=-out
            if k%p == 0: return 0
            while k%p==0: k//=p
        p+=1
    return -out if k>1 else out
def totient(n):
    return sum(gcd(j,n)==1 for j in range(1,n+1))
for n in range(1,25):
    primitive_points = sum(mobius(d)*traces[n//d] for d in divisors(n))
    bracelets = sum(totient(d)*traces[n//d] for d in divisors(n))
    assert primitive_points % n == 0 and bracelets % n == 0
    assert primitive_points >= 0

print('RC2_Q4_CYCLIC_PASS', 'matrix=64', 'first10='+str(traces[1:11]),
      'charpoly_coefficients='+str(len(c)), 'direct_lengths=1..7', 'necklaces=1..24')
