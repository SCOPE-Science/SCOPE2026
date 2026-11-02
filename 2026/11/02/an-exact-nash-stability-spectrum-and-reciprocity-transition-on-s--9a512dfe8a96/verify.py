"""Finite checks for Nash partitions of signed directed star hedonic games.

Run: python verify.py. Only ordinary Python standard library required.
"""
from itertools import product
from functools import lru_cache
from math import comb


def partitions(items):
    """All unlabeled set partitions of a labeled tuple."""
    if not items:
        yield ()
        return
    first, *rest = items
    for pi in partitions(tuple(rest)):
        yield ((first,),) + pi
        for j in range(len(pi)):
            yield pi[:j] + (pi[j] + (first,),) + pi[j+1:]


def direct_stable(pi, valuations):
    n = len(valuations)
    for v in range(n):
        current = next(block for block in pi if v in block)
        current_u = sum(valuations[v][u] for u in current if u != v)
        if current_u < 0:  # singleton deviation
            return False
        for other in pi:
            if other is current:
                continue
            if sum(valuations[v][u] for u in other) > current_u:
                return False
    return True


def structural_stable(pi, pairs):
    # pairs = (a,b): utility of leaf i for hub, hub for leaf i
    center = next(block for block in pi if 0 in block)
    required = {j + 1 for j,(a,b) in enumerate(pairs) if a == 1}
    if set(center) != {0} | required:
        return False
    U = sum(b for a,b in pairs if a == 1)
    return U >= 0 and all(sum(pairs[v-1][1] for v in block) <= U
                          for block in pi if 0 not in block)


def formula_count(pairs):
    plus = sum(a == -1 and b == 1 for a,b in pairs)
    minus = sum(a == -1 and b == -1 for a,b in pairs)
    U = sum(b for a,b in pairs if a == 1)
    if U < 0:
        return 0
    # exponential-formula coefficient implemented via labeled block recursion
    @lru_cache(None)
    def rec(r, s):
        if r == s == 0:
            return 1
        if r:
            return sum(comb(r-1, i-1)*comb(s,j)*rec(r-i,s-j)
                       for i in range(1,r+1) for j in range(s+1)
                       if i-j <= U)
        return sum(comb(s-1,j-1)*rec(0,s-j) for j in range(1,s+1) if -j <= U)
    return rec(plus,minus)


def exact_existence(pairs):
    U = sum(b for a,b in pairs if a == 1)
    R = sum(b for a,b in pairs if a == -1)
    return U > 0 or (U == 0 and R <= 0)


def trial(n):
    cases = 0
    tested_partitions = 0
    for pairs in product(product((-1,1), repeat=2), repeat=n):
        val = [[0]*(n+1) for _ in range(n+1)]
        for leaf,(a,b) in enumerate(pairs,1):
            val[leaf][0] = a
            val[0][leaf] = b
        direct_count = 0
        struct_count = 0
        for pi in partitions(tuple(range(n+1))):
            direct = direct_stable(pi, val)
            struct = structural_stable(pi, pairs)
            assert direct == struct, (n,pairs,pi,direct,struct)
            tested_partitions += 1
            direct_count += direct
            struct_count += struct
        assert direct_count == formula_count(pairs),(n,pairs,direct_count,formula_count(pairs))
        assert bool(direct_count) == exact_existence(pairs)
        cases += 1
    return cases,tested_partitions


def verify():
    totalc = totalp = 0
    for n in range(0,6):
        c,p = trial(n)
        totalc += c;totalp += p
        valid = 0
        for pairs in product(product((-1,1), repeat=2), repeat=n):
            valid += exact_existence(pairs)
        target = (4**n)//2 if n%2 else (4**n + comb(n,n//2)**2)//2
        assert valid == target,(n,valid,target)
        print('n=',n,'profiles=',c,'partition_checks=',p,'stable_profiles=',valid)
    print('ALL_CHECKS_PASSED',totalc,totalp)

if __name__ == '__main__':
    verify()

# Additional exact-rational probability cross-checks at five reciprocity levels.
def verify_reciprocity():
    from fractions import Fraction
    from math import comb
    table = {}
    for n in range(1, 7):
        for num in range(5):
            rho = Fraction(num, 4)
            numerator = 0
            for pairs in product(product((-1, 1), repeat=2), repeat=n):
                if exact_existence(pairs):
                    match = sum(a == b for a, b in pairs)
                    numerator += Fraction(1, 2**n) * rho**match * (1-rho)**(n-match)
            probability = numerator
            if num == 0:
                assert probability == 0, (n, probability)
            if num == 4:
                assert probability == 1, (n, probability)
            if num == 2:
                expected = Fraction(1,2) if n % 2 else (Fraction(1,2) + Fraction(comb(n,n//2)**2,2*4**n))
                assert probability == expected, (n, probability, expected)
            table[(n,num)] = probability
    print('RECIPROCITY_CHECKS_PASSED', len(table), 'values; n=4:', [str(table[4,j]) for j in range(5)])

verify_reciprocity()
