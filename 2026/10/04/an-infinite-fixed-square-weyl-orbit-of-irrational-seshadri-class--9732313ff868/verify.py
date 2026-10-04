from math import gcd

# Divisor vectors are [H,E1,...,E9] coefficients.
def add(x, y):
    return tuple(a+b for a,b in zip(x,y))

def scale(c, x):
    return tuple(c*a for a in x)

def dot(x, y):
    return x[0]*y[0] - sum(x[i]*y[i] for i in range(1,10))

H = (1,0,0,0,0,0,0,0,0,0)
delta = (3,-1,-1,-1,-1,-1,-1,-1,-1,-1)
alpha = (0,1,-1,0,0,0,0,0,0,0)
L = (9,-3,-3,-3,-3,-3,-2,-2,-2,-2)

assert dot(delta, delta) == 0
assert dot(alpha, delta) == 0
assert dot(alpha, alpha) == -2
assert dot(L, delta) == 4
assert dot(L, alpha) == 0
assert dot(L, L) == 20
assert gcd(*[abs(v) for v in L]) == 1

def T(x, root=alpha):
    c = dot(x, delta)
    rr = dot(root, root)
    xr = dot(x, root)
    # The parenthesis is integral for this affine E8 root action.
    q2 = c*rr
    assert q2 % 2 == 0
    q = q2//2 + xr
    return add(add(x, scale(c, root)), scale(-q, delta))

# T_{-alpha} is the exact integral inverse of T_alpha on the full lattice basis.
basis = []
for i in range(10):
    e = [0]*10
    e[i] = 1
    basis.append(tuple(e))
for e in basis:
    assert T(T(e, scale(-1, alpha)), alpha) == e
    assert T(T(e, alpha), scale(-1, alpha)) == e

# Closed formula and coefficient identities.
x = L
last_degree = -1
checks = 0
for m in range(0, 101):
    closed = add(add(L, scale(4*m, alpha)), scale(4*m*m, delta))
    assert x == closed
    a = 9 + 12*m*m
    b1 = 4*m*m - 4*m + 3
    b2 = 4*m*m + 4*m + 3
    b3 = 4*m*m + 3
    b6 = 4*m*m + 2
    expected = (a, -b1, -b2, -b3, -b3, -b3, -b6, -b6, -b6, -b6)
    assert x == expected
    assert dot(x, x) == 20
    assert dot(x, delta) == 4
    assert dot(H, x) == a
    if m > 0:
        assert a > last_degree
    last_degree = a
    checks += 6
    x = T(x)

print(f"exact_integer_checks={checks}")
print("translation_inverse=ok")
print("closed_formula=ok")
print("square_20=ok")
print("anticanonical_degree_4=ok")
print("plane_degree_growth=ok")
print("VERIFY_OK")
