from fractions import Fraction
from math import sqrt

def det4(a):
    # Exact Laplace expansion by permutations.
    import itertools
    total = 0
    for p in itertools.permutations(range(4)):
        inv = sum(p[i] > p[j] for i in range(4) for j in range(i+1,4))
        term = 1
        for i,j in enumerate(p):
            term *= a[i][j]
        total += (-1 if inv % 2 else 1) * term
    return total

def transpose(a):
    return [list(x) for x in zip(*a)]

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

N = [
    [1,0,1,0],
    [0,-1,0,1],
    [1,0,-1,0],
    [0,1,0,1],
]
assert matmul(transpose(N),N) == [[2 if i==j else 0 for j in range(4)] for i in range(4)]
assert det4(N) == 4
# Sector indices 0 and 2 have no coupling to complementary indices 1 and 3.
for i in (0,2):
    for j in (1,3):
        assert N[i][j] == 0 and N[j][i] == 0
assert [[N[i][j] for j in (0,2)] for i in (0,2)] == [[1,1],[1,-1]]

def walk(t, init):
    # Integer amplitudes after factoring out 2^{-t/2}.
    state = {(0,0): init[0], (0,1): init[1]}
    for _ in range(t):
        new = {}
        for (z,c),a in state.items():
            if c == 0:
                outs = ((z+1,0,a),(z-1,1,a))
            else:
                outs = ((z+1,0,a),(z-1,1,-a))
            for z2,c2,v in outs:
                new[(z2,c2)] = new.get((z2,c2),0) + v
        state = new
    den = 2**t
    probs = {}
    for (z,c),a in state.items():
        probs[z] = probs.get(z,0) + a*a
    assert sum(probs.values()) == den
    m1 = Fraction(sum(z*w for z,w in probs.items()), den)
    m2 = Fraction(sum(z*z*w for z,w in probs.items()), den)
    return m1,m2

for t in (2,4,8,16,32):
    m10,m20 = walk(t,(1,0))
    m11,m21 = walk(t,(0,1))
    assert m10 == -m11
    assert m20 == m21

I = 1 - 1/sqrt(2)
L0 = (1 + 3*I)/4
L1 = (1 - I)/4
assert abs(L0 - (1 - 3*sqrt(2)/8)) < 1e-15
assert abs(L1 - sqrt(2)/8) < 1e-15
assert abs((L0-L1) - I) < 1e-15
print('VERIFY_OK')
