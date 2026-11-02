#!/usr/bin/env python3
"""Exact certificate checker for five-report distance-proportional two-facility location.

Python 3, standard library only. Polynomial identities certify the continuous theorem;
finite enumerations are independent corroboration, not its logical basis.
"""
from collections import defaultdict
from itertools import combinations, product
from fractions import Fraction

E = tuple(tuple(int(i == j) for i in range(4)) for j in range(4))
ZERO = (0, 0, 0, 0)

def plus(*terms):
    return tuple(sum(t[i] for t in terms) for i in range(4))

def minus(a, b):
    return tuple(a[i]-b[i] for i in range(4))

def leq(a, b):
    return all(a[i] <= b[i] for i in range(4))

def mul(a, b):
    out = defaultdict(int)
    for i in range(4):
        for j in range(4):
            out[tuple(sorted((i,j)))] += a[i]*b[j]
    return dict(out)

def coeffs_sum(terms):
    out = defaultdict(int)
    for factor, a, b in terms:
        for key, val in mul(a,b).items():
            out[key] += factor*val
    return dict(out)

def p_sub(a, b):
    keys = set(a) | set(b)
    return {k:a.get(k,0)-b.get(k,0) for k in keys}

def p_scale(a, scale):
    return {k:v*scale for k,v in a.items()}

def p_clean(a):
    return {k:v for k,v in a.items() if v}

def p_from_monomials(table):
    letters = 'abcd'
    return {tuple(sorted((letters.index(u), letters.index(v)))): coeff for (u,v), coeff in table.items()}

# For the ten genuinely incomparable service distances, choose one endpoint.
# Keys are zero-indexed (first facility, second facility, unselected client).
BRANCHES = {
    (0,2,1):('q','p'),
    (0,3,1):('q','p'),
    (0,3,2):('q','q'),
    (0,4,1):('q','p'),
    (0,4,2):('q','q'),
    (0,4,3):('q','q'),
    (1,3,2):('p','q'),
    (1,4,2):('p','q'),
    (1,4,3):('p','q'),
    (2,4,3):('p','p'),
}

def bound_polynomial(which):
    positions = [ZERO]
    for gap in E:
        positions.append(plus(positions[-1], gap))
    terms = []
    seen = set()
    for i, j in combinations(range(5),2):
        w = minus(positions[j], positions[i])
        for k in range(5):
            if k in (i,j):
                continue
            p = tuple(abs(x) for x in minus(positions[k], positions[i]))
            q = tuple(abs(x) for x in minus(positions[k], positions[j]))
            key = (i,j,k)
            if leq(p,q): choice = p
            elif leq(q,p): choice = q
            else:
                assert key in BRANCHES
                seen.add(key)
                choice = p if BRANCHES[key][which] == 'p' else q
            terms.append((1,w,choice))
    assert seen == set(BRANCHES), (seen, set(BRANCHES)-seen)
    return p_clean(coeffs_sum(terms))

Z = (4,6,6,4)
T1 = (0,1,2,1)
T2 = (1,0,1,1)
U1 = bound_polynomial(0)
U2 = bound_polynomial(1)
S1 = p_clean(p_sub(p_scale(mul(Z,T1),9),p_scale(U1,4)))
S2 = p_clean(p_sub(p_scale(mul(Z,T2),9),p_scale(U2,4)))
expected_U1 = p_from_monomials({'ab':9,'ac':12,'ad':9,'bb':6,'bc':18,'bd':14,'cc':6,'cd':13,'dd':3})
expected_U2 = p_from_monomials({'aa':3,'ab':9,'ac':12,'ad':9,'bc':12,'bd':12,'cc':5,'cd':13,'dd':4})
expected_S1 = p_from_monomials({'ac':24,'bb':30,'bc':90,'bd':34,'cc':84,'cd':74,'dd':24})
expected_S2 = p_from_monomials({'aa':24,'ab':18,'ac':42,'ad':36,'bc':6,'bd':6,'cc':34,'cd':38,'dd':20})
assert U1 == expected_U1
assert U2 == expected_U2
assert S1 == expected_S1
assert S2 == expected_S2
assert all(c >= 0 for c in S1.values()) and all(c >= 0 for c in S2.values())

def value(poly, g):
    return sum(v*g[i]*g[j] for (i,j),v in poly.items())

def cost_data(g):
    x = [0]
    for v in g: x.append(x[-1]+v)
    z = n = 0
    costs = []
    for i, j in combinations(range(5),2):
        d = x[j]-x[i]
        c = sum(min(abs(y-x[i]),abs(y-x[j])) for y in x)
        costs.append(c)
        z += d
        n += d*c
    opt = min(costs)
    return z,n,opt

profiles = 0
for g in product(range(13), repeat=4):
    z,n,opt = cost_data(g)
    assert z == sum(t*v for t,v in zip(Z,g))
    assert opt == min(g[1]+2*g[2]+g[3],g[0]+g[2]+g[3],g[0]+g[1]+g[3],g[0]+2*g[1]+g[2])
    assert n <= value(U1,g) and n <= value(U2,g)
    assert 4*n <= 9*z*opt
    if opt > 0:
        assert 4*n < 9*z*opt
    else:
        assert n == 0
    assert cost_data(g[::-1]) == (z,n,opt)
    profiles += 1

for t in range(2,160):
    z,n,opt = cost_data((t,1,0,1))
    assert (z,n,opt) == (4*t+10,18*t+22,2)
    assert Fraction(n,z*opt) < Fraction(9,4)
    assert Fraction(9,4) - Fraction(n,z*opt) == Fraction(23,2*(4*t+10))

print('VERIFY_OK symbolic_upper_bound_coefficients=2*10 continuous_nonnegative_slack_certificates=2 integer_gap_profiles=%d sharpness_instances=158' % profiles)
