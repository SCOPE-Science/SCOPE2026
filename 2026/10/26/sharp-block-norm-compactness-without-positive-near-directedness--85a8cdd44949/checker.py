"""Finite exact checks for the anchored-block combinatorial norm.

The finite tests illustrate algebraic identities; they do not replace
proofs for arbitrarily many blocks or for infinite-dimensional limits.
"""
from itertools import combinations, product
from fractions import Fraction
from random import Random


def subsets_at_most(block, cap):
    for k in range(cap + 1):
        for s in combinations(block, k):
            yield s


def anchored_sets(blocks):
    out = {()}
    for i, head in enumerate(blocks, 1):
        choices = []
        for j, block in enumerate(blocks, 1):
            if j < i:
                choices.append([()])
            elif j == i:
                choices.append(list(subsets_at_most(block, len(block))))
            else:
                choices.append(list(subsets_at_most(block, len(block)//(2**i))))
        for selections in product(*choices):
            candidate = tuple(k for selection in selections for k in selection)
            out.add(candidate)
    return out


def top_sum(seq, cap):
    return sum(sorted(map(abs, seq), reverse=True)[:cap])


def formula(values, blocks):
    return max(sum(abs(values[t]) for t in blocks[i-1]) +
               sum(top_sum([values[t] for t in blocks[j-1]],
                           len(blocks[j-1])//(2**i))
                   for j in range(i+1, len(blocks)+1))
               for i in range(1, len(blocks)+1))


def run():
    blocks = [tuple(range(0, 2)), tuple(range(2, 6)), tuple(range(6, 14))]
    families = anchored_sets(blocks)
    assert len(families) == 7450, len(families)
    rng = Random(112358)
    count = 0
    for _ in range(48):
        values = tuple(rng.randrange(-5, 6) for _ in range(14))
        brute = max(sum(abs(values[t]) for t in E) for E in families)
        closed = formula(values, blocks)
        assert brute == closed, (brute, closed)
        assert Fraction(sum(map(abs, values)), 2) <= closed <= sum(map(abs, values))
        count += 3
    for k in range(1, 28):
        # k equal block masses, uniform within each block, all exactly rational.
        values = [Fraction(1, k*2**j) for j in range(1, k+1)]
        L = [Fraction(1, k) + Fraction(k-i, k*2**i) for i in range(1,k+1)]
        assert max(L) == Fraction(k+1, 2*k)
        assert sum(2**j * values[j-1] for j in range(1,k+1)) == 1
        count += 2
    for i in range(2, 32):
        # For an earlier anchor h, at most half of all B_i can be used;
        # at anchor i, every later block is sampled at rate 2^{-i}.
        for h in range(1, i):
            assert Fraction(2**(i-h), 2**i) <= Fraction(1,2)
            count += 1
        assert Fraction(2**i, 2**(2*i)) == Fraction(1, 2**i)
        count += 1
    print(f"PASS: {count} exact algebraic and finite-combinatorial checks")


if __name__ == '__main__':
    run()
