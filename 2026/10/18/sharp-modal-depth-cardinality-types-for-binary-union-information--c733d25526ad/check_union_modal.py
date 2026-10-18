#!/usr/bin/env python3
"""Finite verification of the marked-powerset binary-union modal-depth claim.

Python 3, standard library only.  Checks direct subset-level semantics against
an independent cardinality abstraction; finite checks do not prove the theorem.
"""
from functools import lru_cache
from itertools import product
from random import Random

Z = ('zero',)
A = ('atom',)
N = lambda f: ('not', f)
D = lambda f, g: ('and', f, g)
O = lambda f, g: ('or', f, g)
J = lambda f, g: ('join', f, g)

@lru_cache(None)
def formulas(d):
    """Returns characteristic formulas for cardinalities 0..2**d."""
    if d == 0:
        return (Z, A)
    old = formulas(d - 1)
    t = 2 ** (d - 1)
    out = list(old)
    for k in range(t + 1, 2 * t + 1):
        f = J(old[t], old[k - t])
        for j in range(t, k):
            f = D(f, N(out[j]))
        out.append(f)
    return tuple(out)

@lru_cache(None)
def abstract_truth(formula, n):
    tag = formula[0]
    if tag == 'zero': return n == 0
    if tag == 'atom': return n == 1
    if tag == 'not': return not abstract_truth(formula[1], n)
    if tag == 'and': return abstract_truth(formula[1], n) and abstract_truth(formula[2], n)
    if tag == 'or': return abstract_truth(formula[1], n) or abstract_truth(formula[2], n)
    assert tag == 'join'
    for i in range(n + 1):
        if not abstract_truth(formula[1], i): continue
        for j in range(n + 1):
            if max(i, j) <= n <= i + j and abstract_truth(formula[2], j):
                return True
    return False

class Direct:
    def __init__(self, n):
        self.n = n
        self.cache = {}
        self.witnesses = [tuple((i, j) for i in range(1 << n) for j in range(1 << n)
                                if (i | j) == x and (i & ~x) == 0 and (j & ~x) == 0)
                          for x in range(1 << n)]

    def truth(self, f, x):
        key = (f, x)
        if key in self.cache: return self.cache[key]
        tag = f[0]
        if tag == 'zero': ans = (x == 0)
        elif tag == 'atom': ans = (x.bit_count() == 1)
        elif tag == 'not': ans = not self.truth(f[1], x)
        elif tag == 'and': ans = self.truth(f[1], x) and self.truth(f[2], x)
        elif tag == 'or': ans = self.truth(f[1], x) or self.truth(f[2], x)
        else:
            assert tag == 'join'
            ans = any(self.truth(f[1], y) and self.truth(f[2], z)
                      for y, z in self.witnesses[x])
        self.cache[key] = ans
        return ans


def random_formulas(depth, count, seed=44025):
    rng = Random(seed)
    def draw(d):
        if d == 0 or rng.random() < .18:
            return rng.choice((Z, A))
        op = rng.choice(('not', 'and', 'or', 'join'))
        if op == 'not': return N(draw(d)) if rng.random() < .2 else N(draw(d-1))
        left, right = draw(d-1), draw(d-1)
        return {'and': D, 'or': O, 'join': J}[op](left, right)
    return tuple(draw(depth) for _ in range(count))


def profile_counts(max_n=70, max_d=5):
    types = [0 if n == 0 else (1 if n == 1 else 2) for n in range(max_n+1)]
    counts=[]
    for d in range(max_d+1):
        distinct = len(set(types))
        expected = min(max_n + 1, 2**d + 2)
        assert distinct == expected, (d, distinct, expected)
        for n in range(max_n + 1):
            for m in range(max_n + 1):
                should = min(n, 2**d + 1) == min(m, 2**d + 1)
                assert (types[n] == types[m]) == should, (d,n,m)
        counts.append(distinct)
        if d == max_d: break
        signatures=[]
        for n in range(max_n + 1):
            pairs = frozenset((types[i], types[j]) for i in range(n+1)
                              for j in range(n+1) if i+j>=n)
            signatures.append((types[n],pairs))
        unique={s:i for i,s in enumerate(dict.fromkeys(signatures))}
        types=[unique[s] for s in signatures]
    return counts


def main():
    counts = profile_counts()
    truth_checks=0
    characteristic_checks=0
    f_rand = random_formulas(3, 70)
    for n in range(0, 9):
        direct=Direct(n)
        for f in f_rand:
            for x in range(1 << n):
                assert direct.truth(f,x) == abstract_truth(f,x.bit_count()), (n,x,f)
                truth_checks += 1
        for d in range(4):
            for k,f in enumerate(formulas(d)):
                for x in range(1 << n):
                    assert direct.truth(f,x) == (x.bit_count() == k), (n,d,k,x)
                    characteristic_checks += 1
    print('BINARY_UNION_DEPTH_VERIFY_OK',
          'profiles='+','.join(map(str,counts)),
          'subset_semantics='+str(truth_checks),
          'characteristic_checks='+str(characteristic_checks))

if __name__ == '__main__':
    main()
