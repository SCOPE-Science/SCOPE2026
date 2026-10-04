from fractions import Fraction as F
from itertools import product

# Exact arithmetic in Q(sqrt(5)): pair (r,s) means r+s*sqrt(5).
def q(r=0, s=0):
    return (F(r), F(s))

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def neg(x):
    return (-x[0], -x[1])

def mul(x, y):
    return (x[0]*y[0] + 5*x[1]*y[1], x[0]*y[1] + x[1]*y[0])

def smul(a, x):
    return (F(a)*x[0], F(a)*x[1])

def mm(A, B):
    n, m, k = len(A), len(B), len(B[0])
    out = [[q() for _ in range(k)] for _ in range(n)]
    for i in range(n):
        for j in range(k):
            z = q()
            for t in range(m):
                z = add(z, mul(A[i][t], B[t][j]))
            out[i][j] = z
    return out

# Enumerate all Seidel matrices by six independent edge signs.  Normalize the
# first-row signs using diagonal switching and count the residual negatives.
counts = {0: 0, 1: 0, 2: 0, 3: 0}
for s01, s02, s03, s12, s13, s23 in product((-1, 1), repeat=6):
    d = (1, s01, s02, s03)
    a1 = d[1]*d[2]*s12
    a2 = d[1]*d[3]*s13
    a3 = d[2]*d[3]*s23
    t = (a1 < 0) + (a2 < 0) + (a3 < 0)
    counts[t] += 1
assert counts == {0: 8, 1: 24, 2: 24, 3: 8}

# For t=0,3 the spectra are {3,-1,-1,-1} and {1,1,1,-3}; for t=1,2
# the characteristic polynomial is x^4-6x^2+5=(x^2-1)(x^2-5).
assert counts[1] + counts[2] == 48

sqrt5 = q(0, 1)
a = q(F(1, 4), F(1, 20))
b = q(F(3, 4), F(-1, 20))
c = q(0, F(1, 10))
zero = q()
P = [
    [a, a, c, c],
    [a, a, c, c],
    [c, c, b, neg(a)],
    [c, c, neg(a), b],
]
assert mm(P, P) == P
trace = q()
for i in range(4):
    trace = add(trace, P[i][i])
assert trace == q(2, 0)

# Ordered absolute off-diagonal sum: two a entries from the (1,2) pair,
# two a entries from the (3,4) pair, and eight c entries.
tc = add(smul(4, a), smul(8, c))
assert tc == add(q(1, 0), sqrt5)

# Explicit-frame scalar identities with d=(5-sqrt(5))/20.
dval = q(F(1, 4), F(-1, 20))
assert add(a, dval) == q(F(1, 2), 0)
assert mul(a, dval) == mul(c, c)

print('VERIFY_OK seidel=64 middle=48 projection_exact=1 tc=1+sqrt(5)')
