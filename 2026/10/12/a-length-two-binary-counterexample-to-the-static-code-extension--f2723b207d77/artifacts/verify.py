#!/usr/bin/env python3
from itertools import permutations

F = (0, 1)
V2 = [(a,b) for a in F for b in F]
C = [(0,0),(1,0)]

def add(x,y):
    return tuple(a ^ b for a,b in zip(x,y))

def smul(a,x):
    return tuple(a*b for b in x)

def wt(x):
    return sum(x)

def f(x):
    a,_ = x
    return (a,a)

# C is the coordinate line F_2 x {0}, hence it satisfies the coordinate-split
# condition as well as being an F_2-vector space of dimension one.
assert C == [(0,0),(1,0)]

# Linearity and injectivity of f.
for x in C:
    for y in C:
        assert f(add(x,y)) == add(f(x),f(y))
for a in F:
    for x in C:
        assert f(smul(a,x)) == smul(a,f(x))
assert len({f(x) for x in C}) == len(C)

# The nonzero codeword changes Hamming weight from 1 to 2.
c = (1,0)
assert wt(c) == 1
assert wt(f(c)) == 2

# Over F_2 the only coordinate automorphism is multiplication by 1, so the
# monomial group in length two consists of the two coordinate permutations.
def monomial_images(x):
    return {tuple(x[i] for i in p) for p in permutations(range(2))}
assert f(c) not in monomial_images(c)

# Exhaust all three linear embeddings of this one-dimensional code into F_2^2:
# the generator can be sent to any nonzero vector. Exactly two preserve weight,
# and exactly those two are restrictions of monomial transformations.
nonzero = [x for x in V2 if x != (0,0)]
isometric = [y for y in nonzero if wt(y) == wt(c)]
extendable = [y for y in nonzero if y in monomial_images(c)]
assert sorted(isometric) == sorted([(1,0),(0,1)])
assert sorted(extendable) == sorted(isometric)
assert (1,1) not in extendable
print('VERIFY_OK')
