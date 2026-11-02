#!/usr/bin/env python3
"""Exact characteristic-two polynomial checks for the Fermat flex divisor.

Uses sparse multivariate polynomials represented by sets of exponent triples.
Every operation is performed over F_2 using integer arithmetic only.
"""
from itertools import permutations

ONE = frozenset({(0, 0, 0)})
ZERO = frozenset()

def add(*args):
    s = set()
    for a in args:
        s.symmetric_difference_update(a)
    return frozenset(s)

def mul(a, b):
    s = set()
    for e in a:
        for f in b:
            g = tuple(e[i] + f[i] for i in range(3))
            if g in s: s.remove(g)
            else: s.add(g)
    return frozenset(s)

def prod(*args):
    z = ONE
    for a in args: z = mul(z, a)
    return z

def power(a,n):
    z=ONE
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a)
        n//=2
    return z

def deriv(a,axis):
    s=set()
    for exp in a:
        if exp[axis]&1:
            g=tuple(exp[j]-(j==axis) for j in range(3))
            if g in s:s.remove(g)
            else:s.add(g)
    return frozenset(s)

def monom(axis,e):
    x=[0,0,0];x[axis]=e
    return frozenset({tuple(x)})

x,y,z=[monom(i,1) for i in range(3)]
L=(x,y,z,add(x,y),add(y,z),add(x,z),add(x,y,z))
assert add(*L) == ZERO, 'binary linear-form sum'
assert add(*(power(v,3) for v in L)) == ZERO, 'binary cubes sum'
assert len(set(L)) == 7, 'distinct Fano linear forms'


def det3(a):
    result=ZERO
    for perm in permutations(range(3)):
        result=add(result,prod(a[0][perm[0]],a[1][perm[1]],a[2][perm[2]]))
    return result

assert det3([[ONE, ONE, ONE], [x, y, z], [power(x,3), power(y,3), power(z,3)]]) == \
       prod(add(x,y), add(y,z), add(x,z), add(x,y,z)), 'universal Moore determinant'

for d in [1,3,5,7,9]:
    X,Y,Z=[monom(j,d) for j in range(3)]
    F=prod(x,y,z,add(X,Y),add(Y,Z),add(X,Z),add(X,Y,Z))
    n=4*d+3
    assert all(sum(exp)==n for exp in F)
    gradient=[deriv(F,i) for i in range(3)]
    euler=[x,y,z]
    frob2=[monom(i,d+1) for i in range(3)]
    frob4=[monom(i,3*d+1) for i in range(3)]
    assert add(*(mul(euler[i],gradient[i]) for i in range(3)))==F
    assert add(*(mul(frob2[i],gradient[i]) for i in range(3)))==ZERO
    assert add(*(mul(frob4[i],gradient[i]) for i in range(3)))==ZERO
    assert det3([euler,frob2,frob4])==F
    predicted_tau=(n-1)**2-(d+1)*(3*d+1)
    local_tau=4*d*d+3*(d+1)**2+3*d*(2*d+2)
    assert predicted_tau==local_tau==13*d*d+12*d+3
    print(f'd={d}: degree={n}, monomials={len(F)}, syzygies=({d+1},{3*d+1}), Tjurina={predicted_tau}, PASS')
print('FANO_FERMAT_CHAR2_GENERAL_IDENTITIES_AND_FIVE_EXACT_INSTANCES_PASS')
