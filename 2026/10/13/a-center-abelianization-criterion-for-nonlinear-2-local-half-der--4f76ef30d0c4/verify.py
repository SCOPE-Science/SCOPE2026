from itertools import product

P = 5
ELEMENTS = list(product(range(P), repeat=3))

def add(x, y):
    return tuple((a+b) % P for a,b in zip(x,y))

def scale(c, x):
    return tuple((c*a) % P for a in x)

def bracket(x, y):
    a,b,_ = x
    d,e,_ = y
    return (0,0,(a*e-b*d) % P)

def f(u,v):
    return u % P if v % P == 0 else 0

def Delta(x):
    a,b,c = x
    return (a,b,(c+f(a,b)) % P)

def D(alpha,beta,x):
    a,b,c = x
    return (a,b,(c + alpha*a + beta*b) % P)

def half_rhs(alpha,beta,x,y):
    inv2 = pow(2,-1,P)
    u = bracket(D(alpha,beta,x), y)
    v = bracket(x, D(alpha,beta,y))
    return scale(inv2, add(u,v))

# Every D_{alpha,beta} is a half-derivation of H_3(F_5).
for alpha,beta in product(range(P), repeat=2):
    for x in ELEMENTS:
        for y in ELEMENTS:
            lhs = D(alpha,beta,bracket(x,y))
            rhs = half_rhs(alpha,beta,x,y)
            assert lhs == rhs, (alpha,beta,x,y,lhs,rhs)

# For every pair, some D_{alpha,beta} interpolates Delta on both points.
for x in ELEMENTS:
    for y in ELEMENTS:
        ok = False
        for alpha,beta in product(range(P), repeat=2):
            if D(alpha,beta,x) == Delta(x) and D(alpha,beta,y) == Delta(y):
                ok = True
                break
        assert ok, (x,y)

# Delta is not additive.
x = (1,0,0)
y = (0,1,0)
assert Delta(add(x,y)) != add(Delta(x),Delta(y))

print(f"field=F_{P}")
print(f"elements={len(ELEMENTS)}")
print("half_derivations_checked=25")
print(f"ordered_pairs_interpolated={len(ELEMENTS)**2}")
print("nonadditive=yes")
print("CHECK_OK")
