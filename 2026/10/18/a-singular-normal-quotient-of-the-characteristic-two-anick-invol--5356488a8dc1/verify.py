#!/usr/bin/env python3
"""Reproducible GF(2) polynomial checks for the characteristic-two Anick involution.
No nonstandard Python dependencies. These are finite symbolic identities, not
a replacement for the geometric normality/invariant-field proof.
"""
from itertools import product

N = 5
ZERO = frozenset()
ONE = frozenset({(0,) * N})

def v(i):
    e = [0] * N
    e[i] = 1
    return frozenset({tuple(e)})

def add(*args):
    out = set()
    for arg in args:
        out.symmetric_difference_update(arg)
    return frozenset(out)

def mul(a, b):
    out = set()
    for x in a:
        for y in b:
            m = tuple(x[i] + y[i] for i in range(N))
            if m in out:
                out.remove(m)
            else:
                out.add(m)
    return frozenset(out)

def power(p, e):
    out = ONE
    while e:
        if e & 1:
            out = mul(out, p)
        p = mul(p, p)
        e //= 2
    return out

def evaluate(p, values):
    s = ZERO
    for mon in p:
        product_term = ONE
        for i in range(N):
            product_term = mul(product_term, power(values[i], mon[i]))
        s = add(s, product_term)
    return s

def partial(p, i):
    return frozenset(
        tuple(mon[j] - (j == i) for j in range(N))
        for mon in p if mon[i] % 2
    )

x,y,z,t,D = [v(i) for i in range(5)]
delta = add(mul(x,z),mul(y,t))
X = add(x,mul(t,delta))
Y = add(y,mul(z,delta))
sigma = [X,Y,z,t,D]
assert evaluate(delta,sigma) == delta
assert evaluate(X,sigma) == x
assert evaluate(Y,sigma) == y
assert evaluate(z,sigma) == z and evaluate(t,sigma) == t
U = add(power(x,2),mul(mul(t,delta),x))
V = add(power(y,2),mul(mul(z,delta),y))
assert evaluate(U,sigma) == U
assert evaluate(V,sigma) == V
relation = add(mul(power(z,2),U),mul(power(t,2),V),
               mul(add(ONE,mul(z,t)),power(delta,2)))
assert relation == ZERO

# Jacobian of the quotient hypersurface, in independent coordinates (z,t,D,U,V)
zz,tt,dd,uu,vv = [v(i) for i in range(5)]
F = add(mul(add(ONE,mul(zz,tt)),power(dd,2)),
        mul(power(zz,2),uu),mul(power(tt,2),vv))
assert partial(F,0) == mul(tt,power(dd,2))
assert partial(F,1) == mul(zz,power(dd,2))
assert partial(F,2) == ZERO
assert partial(F,3) == power(zz,2)
assert partial(F,4) == power(tt,2)
# Scheme-theoretic Jacobian ideal is (z^2,t^2,d^2) modulo (F):
# F + z^2 U+t^2 V+z*(t*d^2)=d^2.
identity = add(F,mul(power(zz,2),uu),mul(power(tt,2),vv),
               mul(zz,partial(F,0)),power(dd,2))
assert identity == ZERO

# Pointwise involution test over F2, including nontrivial two-cycles.
def mod2_value(p, vec):
    return len([mon for mon in p if all(vec[i] or mon[i] == 0
                                       for i in range(N))]) & 1
fixed = 0
two_cycles = 0
for data in product((0,1), repeat=4):
    vec = (*data,0)
    inp = data
    out = (mod2_value(X,vec),mod2_value(Y,vec),data[2],data[3])
    nxt = (mod2_value(X,(*out,0)),mod2_value(Y,(*out,0)),out[2],out[3])
    assert nxt == inp
    if out == inp: fixed += 1
    else: two_cycles += 1
assert fixed + two_cycles == 16
assert two_cycles > 0 and two_cycles % 2 == 0
print("PASS: order-two action, invariant generators, quotient relation,")
print("      Jacobian ideal certificate and GF(2)-point orbit checks.")
print(f"      GF(2) affine points: {fixed} fixed, {two_cycles//2} two-cycles.")
