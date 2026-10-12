import collections
import sympy as sp

families = ("A", "B", "C")
vertices = [(f, a, b) for f in families for a in range(4) for b in range(4)]

def adjacent(u, v):
    f, a, b = u
    g, c, d = v
    if f == g:
        return u != v and ((a == c) ^ (b == d))
    if (f, g) == ("A", "B"):
        return (a + d - b - c) % 4 == 0
    if (f, g) == ("B", "A"):
        return (c + b - d - a) % 4 == 0
    if (f, g) == ("A", "C"):
        return (c - a - b - d - 1) % 4 == 0
    if (f, g) == ("C", "A"):
        return (a - c - d - b - 1) % 4 == 0
    if (f, g) == ("B", "C"):
        return (a + b - c - d) % 4 == 0
    if (f, g) == ("C", "B"):
        return (c + d - a - b) % 4 == 0
    raise AssertionError((u, v))

n = len(vertices)
A = sp.zeros(n)
for i in range(n):
    for j in range(i + 1, n):
        if adjacent(vertices[i], vertices[j]):
            A[i, j] = A[j, i] = 1

degrees = [sum(int(A[i, j]) for j in range(n)) for i in range(n)]
assert degrees == [14] * 48
assert sum(degrees) // 2 == 336

t = sp.symbols("t")
actual = sp.factor(A.charpoly(t).as_expr())
expected = (t - 14) * (t - 2)**28 * (t + 2)**12 * (t + 6)**6 * (t + 10)
assert sp.expand(actual - expected) == 0

A2 = A * A
skew = collections.Counter()
adjacent_pairs = collections.Counter()
for i in range(n):
    for j in range(i + 1, n):
        common = int(A2[i, j])
        if A[i, j]:
            adjacent_pairs[common] += 1
        else:
            skew[common] += 1

assert skew == collections.Counter({2: 96, 4: 192, 6: 480, 10: 24})
assert sum(skew.values()) == 792
assert adjacent_pairs == collections.Counter({0: 192, 2: 144})

G = A - 2 * sp.eye(48)
assert G.rank() == 20

print(
    "VERIFY_OK lines=48 degree=14 edges=336 skew=792 "
    "profile=2:96,4:192,6:480,10:24 gram_rank=20 inertia=1,19,28"
)
