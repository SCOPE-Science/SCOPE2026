"""Independent finite checker for idempotent-unary analogy classification.

Uses the original term-justification maximality rule, not the four-class
characterization, to evaluate each ordered quadruple.
Run: python verify.py
"""
from itertools import product


def check_map(f):
    n = len(f)
    assert all(f[f[i]] == f[i] for i in range(n))
    # Idempotence makes the truth of a rule f^k(z)->f^l(z) depend only
    # on whether k and l are 0 or positive.
    powers = [[i for i in range(n)], list(f), list(f)]
    arrows = [(a, b) for a in range(n) for b in range(n)]
    # Directly evaluate existence of a witness to each rule.
    just = {}
    for a, b in arrows:
        mask = 0
        for k, l in product(range(2), repeat=2):
            if any(powers[k][u] == a and powers[l][u] == b
                   for u in range(n)):
                mask |= 1 << (k * 2 + l)
        just[a, b] = mask
    # For n>1 no syntactic justification is trivial (justifies every
    # ordered arrow); n=1 is handled separately.
    if n == 1:
        return 1, True
    assert not [bit for bit in range(4)
                if all(just[a, b] & (1 << bit) for a, b in arrows)]

    def directed(a, b, c, d):
        left, right = just[a, b], just[c, d]
        if left == right == 0:
            return True
        inter = left & right
        if inter == 0:
            return False
        # No candidate strictly dominates the intersection.
        return all((inter | (left & just[c, e])) != (left & just[c, e])
                   or (left & just[c, e]) == inter for e in range(n))

    def predicted_class(a, b):
        if a == b: return 0
        if f[a] == b: return 1
        if f[b] == a: return 2
        return 3

    actual = 0
    for a, b, c, d in product(range(n), repeat=4):
        holds = (directed(a,b,c,d) and directed(b,a,d,c)
                 and directed(c,d,a,b) and directed(d,c,b,a))
        expected = predicted_class(a,b) == predicted_class(c,d)
        assert holds == expected, (f, (a,b,c,d), holds, expected)
        actual += holds
    q = sum(f[i] != i for i in range(n))
    formula = n*n + 2*q*q + (n*(n-1) - 2*q)**2
    assert actual == formula, (f, actual, formula)
    return actual, True


def partition(n):
    # canonical forest representatives, each block size includes its root
    def gen(low, rem):
        if rem == 0:
            yield ()
        else:
            for p in range(low, rem+1):
                for tail in gen(p, rem-p):
                    yield (p,)+tail
    for blocks in gen(1, n):
        f = []
        offset = 0
        for size in blocks:
            f.extend([offset]*size)
            offset += size
        yield tuple(f)


def main():
    maps = quadruples = 0
    for n in range(1,7):
        current = 0
        for f in product(range(n), repeat=n):
            if not all(f[f[i]] == f[i] for i in range(n)):
                continue
            check_map(f)
            current += 1
            maps += 1
            quadruples += n**4
        print('labelled', n, current)
    canonical = 0
    for n in range(7,10):
        for f in partition(n):
            check_map(f)
            canonical += 1
            quadruples += n**4
    print(f'VERIFY_OK labelled_maps={maps} canonical_large={canonical} ordered_quadruples={quadruples}')

if __name__ == '__main__':
    main()
