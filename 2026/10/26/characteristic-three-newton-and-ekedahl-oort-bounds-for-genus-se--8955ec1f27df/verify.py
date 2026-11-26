"""Exact checks for the new genus-two witnesses and the Cartier product order."""


# Use tuples of coefficients mod 3 in 1, a, a^2 for F_27, with a^3=a+1.
Z, ONE, A = (0, 0, 0), (1, 0, 0), (0, 1, 0)


def constant(n):
    return n % 3, 0, 0


def add(a, b):
    return tuple((x + y) % 3 for x, y in zip(a, b))


def mul(a, b):
    c = [0] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    for j in (4, 3):
        c[j - 2] += c[j]
        c[j - 3] += c[j]
    return tuple(x % 3 for x in c[:3])


def cube(a):
    return mul(mul(a, a), a)


def matmul(m, n):
    return tuple(tuple(add(mul(m[i][0], n[0][j]), mul(m[i][1], n[1][j]))
                       for j in range(2)) for i in range(2))


def twist(m):
    return tuple(tuple(map(cube, row)) for row in m)


def matrank(m):
    det = add(mul(m[0][0], m[1][1]), mul(constant(-1), mul(m[0][1], m[1][0])))
    return 2 if det != Z else int(m != ((Z, Z), (Z, Z)))


def polrem(f, g):
    f = list(f)
    while f and len(f) >= len(g):
        q = f[-1] * pow(g[-1], -1, 3)
        shift = len(f) - len(g)
        for i, c in enumerate(g):
            f[i + shift] = (f[i + shift] - q * c) % 3
        while f and not f[-1]:
            f.pop()
    return f


def squarefree(f):
    g = [i * f[i] % 3 for i in range(1, len(f))]
    while g and not g[-1]:
        g.pop()
    while g:
        f, g = g, polrem(f, g)
    return len(f) == 1


for rank, f in enumerate(((1, 0, 0, 0, 0, 1), (2, 0, 0, 0, 1, 1))):
    assert squarefree(f)
    m = tuple(tuple(constant(f[3 * i - j]) for j in (1, 2)) for i in (1, 2))
    assert matrank(m) == 1
    assert matrank(matmul(twist(m), m)) == rank

# The defining cubic is rootless over the prime field, hence irreducible.
assert all((i**3 - i - 1) % 3 for i in range(3))
assert cube(A) == add(A, ONE)
u = mul(constant(-1), cube(A))
m = ((u, mul(u, A)), (ONE, A))
assert matrank(matmul(twist(m), m)) == 0
assert matrank(matmul(m, twist(m))) == 1

# The former proposed rank-zero witness (3,19,25) has rank one.
roots = [Z, ONE, A, (1, 0, 2), (1, 2, 2)]
f = [ONE]
for root in roots:
    g = [Z] * (len(f) + 1)
    for j, c in enumerate(f):
        g[j] = add(g[j], mul(mul(constant(-1), root), c))
        g[j + 1] = add(g[j + 1], c)
    f = g
m = ((f[2], f[1]), (f[5], f[4]))
assert m == (((1, 1, 1), (2, 1, 1)), (ONE, (0, 0, 2)))
assert matmul(twist(m), m)[1][0] == (0, 2, 0)
assert matrank(matmul(twist(m), m)) == 1
assert matrank(matmul(m, twist(m))) == 0
print('CARTIER_WITNESSES_OK')
