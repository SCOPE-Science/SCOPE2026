"""Independent finite sanity checks of four branches, not an infinite proof."""
import itertools
import json
from collections import Counter, defaultdict


class Field:
    def __init__(self, coefficients):
        self.m = len(coefficients) - 1
        self.q = 3 ** self.m
        self.coefficients = coefficients
        self.digits = [[a // 3 ** i % 3 for i in range(self.m)] for a in range(self.q)]
        self.adds = [[self.encode([(x+y) % 3 for x, y in zip(a, b)])
                      for b in self.digits] for a in self.digits]
        self.negs = [self.encode([-x % 3 for x in a]) for a in self.digits]
        self.products = [[self.multiply(a, b) for b in self.digits] for a in self.digits]
        self.squares = {self.mul(a, a) for a in range(1, self.q)}
        assert len(self.squares) == (self.q - 1) // 2
        assert all(self.pow(a, self.q - 1) == 1 for a in range(1, self.q))

    def encode(self, digits):
        return sum(x * 3 ** i for i, x in enumerate(digits))

    def multiply(self, a, b):
        t = [0] * (2 * self.m - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                t[i+j] = (t[i+j] + x*y) % 3
        for d in range(len(t)-1, self.m-1, -1):
            c = t[d]
            for i, x in enumerate(self.coefficients[:-1]):
                t[d-self.m+i] = (t[d-self.m+i] - c*x) % 3
        return self.encode(t[:self.m])

    def add(self, *args):
        result = 0
        for a in args:
            result = self.adds[result][a]
        return result

    def neg(self, a):
        return self.negs[a]

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, *args):
        result = 1
        for a in args:
            result = self.products[result][a]
        return result

    def pow(self, a, n):
        result = 1
        while n:
            if n & 1:
                result = self.mul(result, a)
            a = self.mul(a, a)
            n //= 2
        return result

    def chi(self, a):
        return 0 if not a else 1 if a in self.squares else -1


def check(coefficients):
    f = Field(coefficients)
    q = f.q
    Ds = [a for a in range(1, q) if f.chi(a) == -1]
    if f.m % 2:
        Ds = [1]  # theta^2=-1, hence N(x+theta y)=x^2+y^2.
    elif q > 9:
        Ds = Ds[:1]
    rows = []
    for D in Ds:
        def plus(s, t):
            return f.add(s[0], t[0]), f.add(s[1], t[1])
        def minus(s, t):
            return f.sub(s[0], t[0]), f.sub(s[1], t[1])
        def norm(s):
            return f.add(f.mul(s[0], s[0]), f.mul(D, s[1], s[1]))
        T = {(x, y) for x in range(q) for y in range(q) if norm((x, y)) == 1}
        assert len(T) == q + 1
        pairs = defaultdict(list)
        for a, b in itertools.combinations(sorted(T), 2):
            s = plus(a, b)
            if s != (0, 0) and s not in T:
                pairs[s].append((a, b))
        assert all(len(v) == 1 for v in pairs.values())
        deep = {(x, y) for x in range(q) for y in range(q)} - T - set(pairs) - {(0, 0)}
        triples = Counter()
        for a, b, c in itertools.combinations(sorted(T), 3):
            s = plus(plus(a, b), c)
            if s in deep:
                triples[s] += 1
        marked = {s: [a for a in T if minus(s, a) in pairs] for s in deep}
        assert all(len(marked[s]) == 3 * triples[s] and triples[s] > 0 for s in deep)
        by_norm = defaultdict(set)
        for s in deep:
            by_norm[norm(s)].add(triples[s])
        assert all(len(v) == 1 for v in by_norm.values())
        tested = Counter()
        branches = ('cyclic1', 'cyclic2') if f.m % 2 == 0 else ('constacyclic1', 'constacyclic2')
        for branch in branches:
            for alpha in range(1, q):
                S = (0, alpha) if branch == 'cyclic2' else (alpha, f.neg(alpha)) if branch == 'constacyclic2' else (alpha, 0)
                if S not in deep:
                    continue
                exceptional, good = set(), set()
                for u in range(q):
                    aa, a3, a4, uu = f.mul(alpha, alpha), f.pow(alpha, 3), f.pow(alpha, 4), f.mul(u, u)
                    if branch in ('cyclic1', 'constacyclic1'):
                        g = f.sub(1, uu)
                        A = f.sub(f.mul(2, alpha, u), f.add(aa, 1))
                        B = f.add(f.mul(2, alpha, uu), f.neg(u), a3, alpha)
                        C = f.add(f.mul(f.neg(f.add(aa, 1)), uu), f.mul(f.add(a3, alpha), u), f.neg(a4), aa)
                        desired = -1 if branch == 'cyclic1' else 1
                    elif branch == 'cyclic2':
                        d2 = f.mul(D, D)
                        g = f.sub(1, f.mul(D, uu))
                        A = f.sub(f.mul(2, alpha, d2, u), f.add(f.mul(aa, d2), D))
                        B = f.add(f.mul(2, alpha, d2, uu), f.neg(f.mul(D, u)), f.mul(a3, d2), f.mul(alpha, D))
                        C = f.add(f.mul(f.neg(f.add(f.mul(aa, d2), D)), uu), f.mul(f.add(f.mul(a3, d2), f.mul(alpha, D)), u), f.neg(f.mul(a4, d2)), f.mul(aa, D))
                        desired = 1
                    else:
                        g = f.sub(2, uu)
                        A = f.add(f.mul(alpha, u), f.mul(2, aa), 1)
                        B = f.add(f.mul(alpha, uu), u, f.mul(2, a3), alpha)
                        C = f.add(f.mul(f.add(f.mul(2, aa), 1), uu), f.mul(f.add(f.mul(2, a3), alpha), u), f.mul(2, a4), f.mul(2, aa))
                        desired = 1
                    delta = f.sub(f.mul(B, B), f.mul(A, C))
                    if u == 0 or A == 0 or delta == 0:
                        exceptional.add(u)
                    elif f.chi(g) == desired and f.chi(delta) == 1:
                        good.add(u)
                assert len(exceptional) <= 6
                def parameter(beta):
                    if branch == 'cyclic2':
                        return beta[1]
                    if branch == 'constacyclic2':
                        return f.mul(2, f.sub(beta[1], beta[0]))
                    return beta[0]
                lifts = Counter(parameter(beta) for beta in T)
                valid = Counter(parameter(beta) for beta in marked[S])
                assert all(lifts[u] == valid[u] == 2 for u in good)
                assert {u for u in valid if u not in exceptional} == good
                assert sum(valid[u] for u in exceptional) <= 12
                Acount = len(good)
                assert 2*Acount <= len(marked[S]) <= 2*Acount + 12
                # Squared inequalities avoid floating-point boundary decisions.
                assert max(0, q-28-4*Acount)**2 <= 9*q
                assert max(0, 4*Acount-q-4)**2 <= 9*q
                assert max(0, abs(6*triples[S]-q)-28)**2 <= 9*q
                tested[branch] += 1
        row = dict(q=q, D=D, deep_syndromes=len(deep), multiplicities=sorted(set(triples.values())), branches=dict(tested))
        rows.append(row)
        print(json.dumps(row, sort_keys=True), flush=True)
    return rows


for polynomial in ((2, 1, 1), (1, 2, 0, 1), (2, 0, 0, 2, 1)):
    check(polynomial)
print('VERIFY_BRANCHES_OK')
