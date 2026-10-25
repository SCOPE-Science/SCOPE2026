"""Finite exact checks for a sharpness law in many-valued modal logic.

Run: python3 checker.py. Standard library only.
All tests are finite; the asymptotic arguments are proved in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import exp


def residuum(a, b, top):
    return top if a <= b else b


def predicted(n, weights):
    weights = tuple(Fraction(w) for w in weights)
    assert n >= 1 and sum(weights) == 1 and all(w >= 0 for w in weights)
    tails = [sum(weights[i:]) for i in range(len(weights))] + [Fraction(0)]
    min_mass = [tails[i]**n - tails[i + 1]**n for i in range(len(weights))]
    ties = sum(z*z for z in min_mass)
    order = (1 + sum(w*w for w in weights))/2
    return (1 - ties)/2 + order**n


def enumerate_equal(n, weights):
    weights = tuple(Fraction(w) for w in weights)
    k = len(weights)
    total = Fraction(0)
    conditional = Fraction(0)
    witness = Fraction(0)
    for pairs in product(range(k*k), repeat=n):
        aa = [v//k for v in pairs]
        bb = [v%k for v in pairs]
        mass = Fraction(1)
        for a,b in zip(aa,bb):
            mass *= weights[a]*weights[b]
        if mass == 0:
            continue
        lhs = min(residuum(a,b,k-1) for a,b in zip(aa,bb))
        rhs = residuum(min(aa),min(bb),k-1)
        assert lhs <= rhs
        criterion = (min(aa)>min(bb)) or all(a<=b for a,b in zip(aa,bb))
        assert (lhs == rhs) == criterion
        if lhs == rhs:
            total += mass
        if min(aa)>min(bb):
            conditional += mass
        if all(a<=b for a,b in zip(aa,bb)):
            witness += mass
    assert total == conditional + witness
    return total


def uniform_exact(n,k):
    return predicted(n,[Fraction(1,k)]*k)


def main():
    cases = 0
    for k in range(1,6):
        for n in range(1,5):
            if (k*k)**n > 700_000:
                continue
            result = enumerate_equal(n,[Fraction(1,k)]*k)
            assert result == uniform_exact(n,k)
            cases += 1
    for weights in ((Fraction(1,5),Fraction(2,5),Fraction(2,5)),
                    (Fraction(1,2),Fraction(1,3),Fraction(1,6)),
                    (Fraction(1,4),Fraction(3,4))):
        for n in (1,2,3):
            assert enumerate_equal(n,weights) == predicted(n,weights)
            cases += 1
    assert uniform_exact(2,2) == Fraction(3,4)
    assert uniform_exact(2,3) == Fraction(59,81)
    assert uniform_exact(3,3) == Fraction(125,243)
    assert uniform_exact(2,4) == Fraction(93,128)
    # Numeric smoke tests for the two nontrivial scaling examples.
    for ratio in (1,2):
        n = 400
        k = ratio*n
        target = 1/(1+exp(n/k))
        actual = float(uniform_exact(n,k))
        assert abs(actual-target) < 0.001
    print('exact weighted/uniform cases:',cases)
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    main()
