#!/usr/bin/env python3
"""Exact, standard-library verification for a fixed-content prefix-normal-word series."""
from math import comb
from itertools import combinations

A = [1, 3, 9, 17, 35, 48, 76, 85, 108, 103, 108, 85, 76, 48,
     35, 17, 9, 3, 1]


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] += ai * bj
    return out


def add(a, b):
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


def neg(a):
    return [-x for x in a]


def trim(a):
    a = a[:]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


class Rat:
    def __init__(self, num, den=None):
        self.n = trim([num] if isinstance(num, int) else num)
        self.d = trim([1] if den is None else den)

    @staticmethod
    def cv(v):
        return v if isinstance(v, Rat) else Rat(v)

    def __add__(self, other):
        b = Rat.cv(other)
        return Rat(add(mul(self.n, b.d), mul(self.d, b.n)),
                   mul(self.d, b.d))

    __radd__ = __add__

    def __neg__(self):
        return Rat(neg(self.n), self.d)

    def __sub__(self, other):
        return self + -Rat.cv(other)

    def __rsub__(self, other):
        return Rat.cv(other) - self

    def __mul__(self, other):
        b = Rat.cv(other)
        return Rat(mul(self.n, b.n), mul(self.d, b.d))

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = Rat.cv(other)
        return Rat(mul(self.n, b.d), mul(self.d, b.n))

    def __rtruediv__(self, other):
        return Rat.cv(other) / self

    def __pow__(self, p):
        assert isinstance(p, int) and p >= 0
        x = Rat(1)
        for _ in range(p):
            x = x * self
        return x

    def equals(self, other):
        b = Rat.cv(other)
        return trim(mul(self.n, b.d)) == trim(mul(b.n, self.d))


z = Rat([0, 1])
phi = lambda x, q: x * (2 - x - q) / (1 - x)**2


def U(r, q):
    return ((phi(z**r * q, q) - z**2 * phi(z**(r+2) * q, q)) /
            ((1-z**2)*(1-q)**2) +
            (z**r * phi(z**2 * q, q) - phi(z**(r+2) * q, q)) /
            ((1-z**r)*(1-q)**2))

H_ge = (1 / ((1-z)*(1-z**2)) *
        (1/(1-z) * (1/(1-z)**2 - z**2/(1-z**3)**2) -
         1/(1-z**2) * (z/(1-z**2)**2 - z**3/(1-z**4)**2)))
H_lt = (U(3, z) - z*U(2, z**2))/(1-z)
H_expected = Rat(A) / ((1-z**3)*(1-z**4)**2*(1-z**6)**2)
assert (H_ge + H_lt).equals(H_expected), 'Formal rational identity failed'
print('Formal all-degree rational-function identity: PASS')
assert A == A[::-1] and sum(A) == 867

NMAX = 30
D = [0]*(NMAX+1)
D[0] = 1
for gap, exponent in ((1,1),(3,1),(4,2),(6,3)):
    for _ in range(exponent):
        for n in range(gap,NMAX+1):
            D[n] += D[n-gap]
F = [sum(A[j]*D[n-7-j] for j in range(len(A)) if n-7-j>=0)
     for n in range(NMAX+1)]

def direct_normal(positions, n):
    positions = set(positions)
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + (i in positions)
    for start in range(n):
        for end in range(start+1,n+1):
            if prefix[end]-prefix[start] > prefix[end-start]:
                return False
    return True


def all_gap_conditions(positions):
    gaps = [positions[i+1]-positions[i] for i in range(6)]
    return (positions[0]==0 and
            all(sum(gaps[i:i+r])>=sum(gaps[:r])
                for r in range(1,7) for i in range(7-r)))

tested = 0
for n in range(7,19):
    cnt = 0
    for positions in combinations(range(n),7):
        d = direct_normal(positions,n)
        assert d == all_gap_conditions(positions)
        cnt += d
        tested += 1
    assert cnt == F[n], (n,cnt,F[n])
print(f'Direct factor/gap equivalence and counts through n=18: PASS ({tested} words)')

for n in range(7,30):
    cnt = 0
    for a in range(1,(n-1)//6+1):
        remaining = n-1-6*a
        for b in range(remaining+1):
            for c in range(remaining-b+1):
                for d in range(remaining-b-c+1):
                    if c+d < b: continue
                    for e in range(remaining-b-c-d+1):
                        if d+e < b: continue
                        for f in range(remaining-b-c-d-e+1):
                            if e+f < b or d+e+f < b+c: continue
                            cnt += 1
    assert cnt == F[n], (n,cnt,F[n])
print('Independent five-variable cone enumeration n=7..29: PASS')
print('Coefficients n=7..21:', F[7:22])
print('Numerator coefficients:', A)
print('Numerator sum:', sum(A))
print('All checks: PASS; independent mathematical audit not performed')
