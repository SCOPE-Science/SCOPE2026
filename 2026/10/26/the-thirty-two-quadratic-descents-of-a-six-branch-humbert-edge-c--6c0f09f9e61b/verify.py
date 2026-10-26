#!/usr/bin/env python3
"""Exact field arithmetic and twist-census checks for six-branch genus-17 curves.

Run: python3 verify.py. Only Python's standard library is needed.
This code checks finite inputs; the accompanying proof establishes the
geometric cover, character decomposition, and all-extension zeta identities.
"""
from itertools import combinations, product
from collections import Counter
from math import comb

P = 7
BRANCH = tuple(range(5))
SQUARES = {x*x % P for x in range(P)}

def chi7(x):
    x %= P
    return (1 if x in SQUARES else -1) if x else 0

# a+b*i in F49, where i^2=-1, which is nonsquare in F7.
class F49:
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a, self.b = a % 7, b % 7
    def __add__(self, other):
        return F49(self.a + other.a, self.b + other.b)
    def __sub__(self, other):
        return F49(self.a - other.a, self.b - other.b)
    def __mul__(self, other):
        return F49(self.a*other.a - self.b*other.b,
                   self.a*other.b + self.b*other.a)
    def __pow__(self, exponent):
        assert exponent >= 0
        result, base = F49(1), self
        while exponent:
            if exponent & 1:
                result = result*base
            base = base*base
            exponent //= 2
        return result
    def __eq__(self, other):
        return isinstance(other, F49) and (self.a, self.b) == (other.a, other.b)
    def __hash__(self):
        return hash((self.a, self.b))
    def __repr__(self):
        return f"({self.a},{self.b})"

FIELD49 = [F49(a,b) for a in range(7) for b in range(7)]
SQUARES49 = {v*v for v in FIELD49}
assert len(FIELD49) == len(set(FIELD49)) == 49
assert len(SQUARES49) == 25
assert all(v**49 == v for v in FIELD49)

def curve_points(subset, field):
    """Projective points on y^2=prod(t-i), normalized degree 3,4,5."""
    subset = tuple(subset)
    odd_degree = len(subset) & 1
    if field == 7:
        # infinity: 1 for odd degree; 2 for even monic degree.
        total = 1 if odd_degree else 2
        for t in range(7):
            value = 1
            for i in subset:
                value = value*(t-i) % 7
            total += 1 + chi7(value)
        return total
    if field == 49:
        total = 1 if odd_degree else 2
        for t in FIELD49:
            value = F49(1)
            for i in subset:
                value = value*(t-F49(i))
            total += 1 if value == F49(0) else 2 if value in SQUARES49 else 0
        return total
    raise ValueError(field)

SUBSETS = [s for k in (3,4) for s in combinations(BRANCH,k)]
assert len(SUBSETS) == 15
TRACES = {s: 8-curve_points(s,7) for s in SUBSETS}
assert Counter(TRACES.values()) == Counter({0: 9, -4: 4, 4: 2})
assert all(curve_points(s,49) == 50 - (TRACES[s]**2 - 14)
           for s in SUBSETS)
assert curve_points(BRANCH,7) == 8
assert curve_points(BRANCH,49) == 46
# The genus-two Weil numerator is 1-2*T^2+49*T^4.
# e2=((sum roots)^2-sum roots^2)/2=(0-(50-46))/2=-2.


def zeta_trace_count(bits):
    """F7 count from all quotient Frobenius traces."""
    assert len(bits) == 5
    tr = 0
    for s, base_trace in TRACES.items():
        tr += (-1)**sum(bits[i] for i in s) * base_trace
    # Genus-two first trace is zero for either twist.
    return 8 - tr


def direct_count(bits, field):
    """Count X itself via fiber sizes, independent of quotient trace sums."""
    q = field
    assert q in (7,49)
    if q == 7:
        chi = lambda x: chi7(x)
        vals = range(7)
        scalar = lambda e: 1 if e == 0 else 3
        zero = 0
        product_value = lambda d,t,i: d*(t-i)%7
    else:
        vals = FIELD49
        chi = lambda x: 0 if x == F49(0) else 1 if x in SQUARES49 else -1
        scalar = lambda e: F49(1 if e == 0 else 3)
        zero = F49(0)
        product_value = lambda d,t,i: d*(t-F49(i))
    d = [scalar(e) for e in bits]
    result = 0
    for t in vals:
        choices = [1 + chi(product_value(d[i],t,i)) for i in BRANCH]
        ways = 1
        for c in choices:
            ways *= c
        result += ways
    if field == 7:
        result += 16 if len(set(bits)) == 1 else 0
    else:
        # Every d_i/d_0 is a square in F49; there are 16 infinity points.
        result += 16
    return result

counts, representatives, zeros = Counter(), {}, []
for bits in product((0,1), repeat=5):
    bitstr = ''.join(map(str, bits))
    via_characters = zeta_trace_count(bits)
    via_fibers = direct_count(bits,7)
    assert via_characters == via_fibers, (bits, via_characters, via_fibers)
    assert via_characters in (0,16,32)
    counts[via_characters] += 1
    representatives.setdefault(via_characters, bitstr)
    if via_characters == 0:
        zeros.append(bitstr)
    # For all q=7^m even with m=2 all d_i are squares, so X/F49 same.
    assert direct_count(bits,49) == 160, bitstr
    m_plus = (40-via_characters)//8
    assert m_plus in (1,3,5)
    assert sum(((-1)**sum(bits[i] for i in s))*TRACES[s] for s in SUBSETS) == 4*(2*m_plus-8)

# A third, independent route enumerates the actual projective model in P^5,
# without choosing a base parameter t or quotient curves.
def points_projective_model(bits):
    d = [1 if e == 0 else 3 for e in bits]
    inverse_d0 = pow(d[0], -1, 7)
    total = 0
    for leading in range(6):
        for tail in product(range(7), repeat=5-leading):
            coords = (0,)*leading + (1,) + tail
            sqcoords = [c*c % 7 for c in coords]
            u0sq = sqcoords[0]
            zsq = sqcoords[5]
            if all((sqcoords[i]-(d[i]*inverse_d0)*u0sq+i*d[i]*zsq)%7 == 0
                   for i in range(1,5)):
                total += 1
    return total

for bits in product((0,1), repeat=5):
    assert points_projective_model(bits) == zeta_trace_count(bits), bits

assert counts == Counter({0:18,16:12,32:2}), counts
assert representatives == {16:'00000', 0:'00001', 32:'10100'}
assert sum(Counter(TRACES.values()).values()) == 15
assert comb(5,3)+comb(5,4) == 15
print('F7 curve genus = 17; 32 quadratic twist labels checked.')
print('Independent homogeneous P5 enumeration agrees for all 32 labels')
print('F7 elliptic quotient traces:', dict(sorted(Counter(TRACES.values()).items())))
print('F7/F49 genus-two quotient:', curve_points(BRANCH,7),curve_points(BRANCH,49))
print('F7 marked-twist point spectrum:', dict(sorted(counts.items())))
print('F49 rational points for every marked twist = 160')
print('zeta numerator: (1+7*T^2)^9 (1-4*T+7*T^2)^m (1+4*T+7*T^2)^(8-m)')
print('m=5 for 18, m=3 for 12, m=1 for 2 twist labels')
print('VERIFY_OK')
