from collections import defaultdict
from math import ceil

# Formal nonassociative polynomials with integer coefficients.
def var(x): return {x: 1}
def add(*ps):
    out = defaultdict(int)
    for p in ps:
        for m,c in p.items(): out[m] += c
    return {m:c for m,c in out.items() if c}
def scale(a,p): return {m:a*c for m,c in p.items() if a*c}
def mul(p,q):
    out = defaultdict(int)
    for m,a in p.items():
        for n,b in q.items(): out[(m,n)] += a*b
    return {m:c for m,c in out.items() if c}

def phi(a,b,c):
    return add(mul(a,mul(b,c)), scale(-1,mul(mul(a,b),c)), scale(-1,mul(mul(b,a),c)))
def q(a,b,c): return add(phi(a,b,c),phi(b,a,c))
def S(a,b,c,d):
    return add(
        scale(2,phi(mul(a,b),c,d)), scale(2,phi(mul(b,a),c,d)),
        phi(a,b,mul(c,d)), scale(-2,phi(a,c,mul(b,d))),
        scale(-2,mul(a,phi(b,c,d))), scale(-1,mul(c,phi(a,b,d)))
    )

a,b,c,d = map(var, 'abcd')
lhs = S(a,b,c,d)
rhs = add(q(mul(a,b),c,d), q(mul(b,a),c,d), scale(-1,q(a,c,mul(b,d))), scale(-1,mul(a,q(b,c,d))))
assert lhs == rhs, 'universal S/q expansion failed'

# The two scalar divisions used in the defect argument are available exactly
# outside characteristics 2 and 3.
for p in [5,7,11,13,17,19]:
    assert pow(2,-1,p) * 2 % p == 1
    assert pow(3,-1,p) * 3 % p == 1
for p in [2,3]:
    assert (2 % p == 0) or (3 % p == 0)

# Normal words use factors of original degree 1 or 3.  A homogeneous word of
# original degree d therefore has at least ceil(d/3) normal factors.
for d in range(1,250):
    best = 10**9
    for y in range(d//3 + 1):
        x = d - 3*y
        if x >= 0:
            best = min(best, x+y)
    assert best >= ceil(d/3)

# If dim A=n and A^(n+1)=0 in left-normed powers, then every homogeneous
# product of original degree at least 3n+1 expands into normal words with at
# least n+1 factors.
for n in range(1,80):
    for d in range(3*n+1, 3*n+7):
        assert ceil(d/3) >= n+1

print('VERIFY_OK')
