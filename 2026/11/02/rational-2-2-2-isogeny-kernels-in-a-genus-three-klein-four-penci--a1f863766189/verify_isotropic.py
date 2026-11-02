#!/usr/bin/env python3
"""Standalone exact checks for isotropic kernel counts on a genus-three family.

Uses only the Python standard library.  Finite tests corroborate, but do not replace,
the proof for arbitrary odd finite fields in RESULT.md.
"""
from collections import Counter
from itertools import combinations

FULL = (1 << 8) - 1


def canonical(m):
    return min(m, m ^ FULL)


def sumv(a, b):
    return canonical(a ^ b)


def weil(a, b):
    return (a & b).bit_count() & 1


V = tuple(m for m in range(256) if m.bit_count() % 2 == 0 and m < (m ^ FULL))
assert len(V) == 64


def permute(m, permutation):
    out = 0
    for i in range(8):
        if (m >> i) & 1:
            out |= 1 << permutation[i]
    return canonical(out)


def lagrangians():
    out = set()
    for a, b, c in combinations(V[1:], 3):
        if weil(a, b) or weil(a, c) or weil(b, c):
            continue
        basis = {0, a, b, c, sumv(a, b), sumv(a, c), sumv(b, c),
                 sumv(sumv(a, b), c)}
        if len(basis) == 8:
            out.add(frozenset(basis))
    return out


def matchings(xs):
    if not xs:
        yield ()
        return
    first, *others = xs
    for j, other in enumerate(others):
        for rest in matchings(others[:j] + others[j+1:]):
            yield ((first, other),) + rest


def matching_lagrangians():
    out = set()
    for pairs in matchings(list(range(8))):
        a, b, c, d = (canonical((1 << x) | (1 << y)) for x, y in pairs)
        out.add(frozenset((0, a, b, c, d, sumv(a, b), sumv(a, c), sumv(a, d))))
    return out


def kernel_census():
    all_lags = lagrangians()
    matching = matching_lagrangians()
    assert len(all_lags) == 135
    assert len(matching) == 105 and matching <= all_lags
    classes = {
        "1^8": tuple(range(8)),
        "1^4 2^2": (0, 1, 2, 3, 5, 4, 7, 6),
        "2^4": (1, 0, 3, 2, 5, 4, 7, 6),
    }
    expected = {
        "1^8": (64, 135, 105, 30),
        "1^4 2^2": (16, 15, 9, 6),
        "2^4": (16, 39, 25, 14),
    }
    for name, p in classes.items():
        fixed_v = sum(permute(x, p) == x for x in V)
        fixed_l = {L for L in all_lags if frozenset(permute(x, p) for x in L) == L}
        fixed_match = len(fixed_l & matching)
        result = (fixed_v, len(fixed_l), fixed_match, len(fixed_l) - fixed_match)
        assert result == expected[name], (name, result, expected[name])
        print("FROBENIUS", name, "J2/LAGRANGIAN/MATCHING/AFFINE", result)
    # Affine-structure group calculation is an independent non-enumerative check.
    agl = 8 * 7 * 6 * 4
    assert agl == 1344
    assert (2**2 * 2 * 24) * 42 // agl == 6
    assert (2**4 * 24) * 49 // agl == 14


class Field:
    def __init__(self, p, modulus=None):
        self.p = p
        self.mod = modulus or (0, 1)
        self.n = len(self.mod) - 1
        assert self.mod[-1] == 1
        self.q = p ** self.n

    def digits(self, a):
        return [(a // self.p ** j) % self.p for j in range(self.n)]

    def elem(self, ds):
        return sum((v % self.p) * self.p**i for i, v in enumerate(ds))

    def add(self, a, b):
        return self.elem([x+y for x,y in zip(self.digits(a), self.digits(b))])

    def neg(self, a):
        return self.elem([-x for x in self.digits(a)])

    def mul(self, a, b):
        a, b = self.digits(a), self.digits(b)
        z = [0] * (self.n * 2 - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                z[i+j] += x*y
        for k in range(len(z)-1, self.n-1, -1):
            v = z[k] % self.p
            for j in range(self.n):
                z[k-self.n+j] -= v * self.mod[j]
        return self.elem(z[:self.n])

    def pow(self, a, k):
        b = 1
        while k:
            if k&1: b = self.mul(b,a)
            a = self.mul(a,a)
            k //= 2
        return b

    def check_field(self):
        assert self.q >= 3
        for a in range(1,self.q):
            assert self.pow(a,self.q-1) == 1, (self.q,a)

    def polynomial_mul_mod(self, a, b, mod):
        z=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                z[i+j]=self.add(z[i+j],self.mul(x,y))
        for k in range(len(z)-1,len(mod)-2,-1):
            v=z[k]
            for j in range(len(mod)-1):
                z[k-len(mod)+1+j]=self.add(z[k-len(mod)+1+j],self.neg(self.mul(v,mod[j])))
        return z[:len(mod)-1]

    def xpower_mod(self, k, mod):
        x=[0,1,0,0]
        ans=[1,0,0,0]
        while k:
            if k&1: ans=self.polynomial_mul_mod(ans,x,mod)
            x=self.polynomial_mul_mod(x,x,mod)
            k//=2
        return ans


def finite_fields():
    for p in (3,5,7,11,13,17,19,23,29,31):
        yield Field(p)
    # Explicit irreducible moduli: t^2+1 over F3 or F7,
    # t^2+2 over F5, t^3+2t+1 over F3.
    yield Field(3,(1,0,1))
    yield Field(5,(2,0,1))
    yield Field(7,(1,0,1))
    yield Field(3,(1,2,0,1))


def parameter_census():
    total_pairs = 0
    for f in finite_fields():
        f.check_field()
        q=f.q
        two=f.add(1,1)
        minus_two=f.neg(two)
        allowed=[a for a in range(q) if a not in (two,minus_two)]
        assert len(allowed)==q-2
        split={}
        for a in allowed:
            roots=[]
            for x in range(q):
                xx=f.mul(x,x)
                val=f.add(f.add(f.mul(xx,xx),f.mul(a,xx)),1)
                if not val: roots.append(x)
            assert len(roots) in (0,4), (q,a,roots)
            split[a]=(len(roots)==4)
            # The field F_(q^2) contains every quartic root (separability assumed).
            poly=[1,0,a,0,1]
            assert f.xpower_mod(q*q,poly) == [0,1,0,0], (q,a)
        S=sum(split.values())
        E=(q-1-(4 if q%4==1 else 2))//4
        assert S==E, (q,S,E)
        U=q-2-S
        freq=Counter()
        for a in allowed:
            for b in allowed:
                if a!=b:
                    k=int(split[a])+int(split[b])
                    freq[k]+=1
        assert freq[2] == S*(S-1)
        assert freq[1] == 2*S*U
        assert freq[0] == U*(U-1)
        assert sum(freq.values()) == (q-2)*(q-3)
        total_pairs+=sum(freq.values())
        print("FIELD",q,"SPLIT",S,"NONSPLIT",U,"COUNTS",dict(sorted(freq.items())))
    print("TOTAL_VERIFIED_ORDERED_PAIRS", total_pairs)


if __name__ == '__main__':
    kernel_census()
    parameter_census()
    print('GENUS3_LAGRANGIAN_FROBENIUS_ALL_CHECKS_PASS')
