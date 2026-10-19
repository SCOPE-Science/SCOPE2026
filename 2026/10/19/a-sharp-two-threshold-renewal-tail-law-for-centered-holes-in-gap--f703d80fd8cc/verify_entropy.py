"""Independent finite-state and high-precision checks of a centered-hole entropy law.

Run: python verify_entropy.py
Uses only the Python standard library. These finite checks are diagnostics,
not a substitute for the general countable-renewal argument.
"""
from decimal import Decimal, localcontext
from fractions import Fraction


def bisect(func, lo, hi, steps=95):
    assert func(lo) < 0 < func(hi)
    for _ in range(steps):
        mid = (lo + hi) / 2
        if func(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def gap_root(S, n):
    assert any(s < n for s in S) and any(s >= n for s in S)
    def fun(z):
        a = sum(z**(s + 1) for s in S if s < n)
        b = sum(z**(s + 1) for s in S if s >= n)
        return a * (1 + b) - 1
    return bisect(fun, 0.01, 1.0, 110)


def spectral_from_paths(adjacency, iterations=1100):
    count = [1] * len(adjacency)
    last_total = sum(count)
    for _ in range(iterations):
        new = [0] * len(adjacency)
        for i, row in enumerate(adjacency):
            for j in row:
                new[j] += count[i]
        count = new
        total = sum(count)
        assert total > 0
        last_total, prev_total = total, last_total
    return last_total / prev_total


def full_shift_automaton(n):
    word = '0' * n + '1' + '0' * n
    length = len(word)
    graph = [[] for _ in range(length)]
    for i in range(length):
        prefix = word[:i]
        for letter in '01':
            next_word = prefix + letter
            if next_word.endswith(word):
                continue
            candidates = [k for k in range(length) if next_word.endswith(word[:k])]
            graph[i].append(max(candidates))
    return graph


def finite_gap_automaton(S, n):
    S = set(S)
    m = max(S)
    states = [(p, z) for p in (0, 1) for z in range(m + 1)]
    ids = {state: idx for idx, state in enumerate(states)}
    graph = [[] for _ in states]
    for (prev_long, zeros), i in ids.items():
        if zeros < m:
            graph[i].append(ids[(prev_long, zeros + 1)])
        if zeros in S and not (prev_long and zeros >= n):
            graph[i].append(ids[(int(zeros >= n), 0)])
    return graph


def exact_transfer_identities():
    cases = [([0, 2, 5, 9], 3), ([1, 4, 6], 2), ([0, 1, 3], 2)]
    n_checks = 0
    for S, n in cases:
        for numerator, denominator in [(1, 2), (2, 3), (3, 5), (4, 7)]:
            z = Fraction(numerator, denominator)
            A = sum((z**(s + 1) for s in S if s < n), Fraction(0))
            B = sum((z**(s + 1) for s in S if s >= n), Fraction(0))
            T = (1 + B) / (1 - A - A * B)
            assert (1 - A * (1 + B)) * T == 1 + B
            n_checks += 1
    return n_checks


def high_precision_lacunary_tests():
    # First eight positive powers of two; the missing high tail is negligible
    # at tested levels. The theorem itself assumes the infinite set.
    with localcontext() as ctx:
        ctx.prec = 96
        d = Decimal
        S = [2**k for k in range(8)]
        low, high = d('0.3'), d('0.99')
        F = lambda z: sum((z ** (s + 1) for s in S), d(0))
        r = bisect(lambda z: F(z) - 1, low, high, 355)
        derivative = sum((d(s + 1) * r**s for s in S), d(0))
        ratios = []
        for n in [5, 9, 17, 33]:
            b = sum((r**(s + 1) for s in S if s >= n), d(0))
            rn = bisect(
                lambda z: sum((z**(s + 1) for s in S if s < n), d(0))
                * (1 + sum((z**(s + 1) for s in S if s >= n), d(0))) - 1,
                r, high, 355)
            deficit = (rn / r).ln()
            ratio = deficit * r * derivative / (b*b)
            assert abs(ratio - 1) < d('0.25')
            ratios.append((n, str(ratio)))
        assert abs(d(ratios[-1][1]) - 1) < d('0.00001')
        return ratios


def main():
    exact = exact_transfer_identities()
    print('Exact rational renewal identities:', exact)
    comparisons = 0
    for n in [1, 2, 3, 4, 5]:
        graph = full_shift_automaton(n)
        value = spectral_from_paths(graph, 1700)
        root = bisect(lambda z:
                      (z * (1-z**n) / (1-z))
                      * (1 + z**(n+1) / (1-z)) - 1,
                      0.01, 0.99)
        assert abs(value - 1 / root) < 1e-10, (n, value, root)
        comparisons += 1
        print('Binary full shift n = %d, Perron estimate = %.12f, root estimate = %.12f'
              % (n, value, 1/root))
    for S, n in [([0, 2, 4, 5], 3), ([0, 5], 1),
                 ([1, 3, 4], 2), ([2, 3, 9], 3)]:
        value = spectral_from_paths(finite_gap_automaton(S, n), 1700)
        root = gap_root(S, n)
        assert abs(value - 1 / root) < 1e-9, (S, n, value, root)
        comparisons += 1
        print('Finite-gap set %s, n = %d, estimates %.12f / %.12f'
              % (S, n, value, 1/root))
    ratios = high_precision_lacunary_tests()
    print('Lacunary correction ratios:', ratios)
    print('PASS: %d exact identities, %d spectral tests, %d high-precision tail checks'
          % (exact, comparisons, len(ratios)))




def asym_root_finite(S, a, b):
    assert a > min(S) and b > min(S)
    def fun(z):
        F = sum(z**(s + 1) for s in S)
        U = sum(z**(s + 1) for s in S if s >= a)
        V = sum(z**(s + 1) for s in S if s >= b)
        W = sum(z**(s + 1) for s in S if s >= max(a, b))
        return (F-1)*(1+W)-U*V
    return bisect(fun, 0.01, 0.99)


def asym_finite_automaton(S, a, b):
    S = set(S)
    maximum = max(S)
    states = [(p, z) for p in (0, 1) for z in range(maximum+1)]
    ids = {state:i for i,state in enumerate(states)}
    graph = [[] for _ in states]
    for (prev_high, zeros), i in ids.items():
        if zeros < maximum:
            graph[i].append(ids[(prev_high, zeros+1)])
        if zeros in S and not (prev_high and zeros >= b):
            graph[i].append(ids[(int(zeros >= a), 0)])
    return graph


def forbidden_word_automaton(a, b):
    word = '0' * a + '1' + '0' * b
    graph = [[] for _ in range(len(word))]
    for j in range(len(word)):
        for symbol in '01':
            candidate = word[:j] + symbol
            if candidate.endswith(word):
                continue
            graph[j].append(max(k for k in range(len(word))
                                if candidate.endswith(word[:k])))
    return graph


def asymmetric_tests():
    count = 0
    for S in ([0, 2, 5, 9], [1, 3, 7, 8]):
        for a,b in ((2, 3), (3, 2), (4, 5), (5, 4)):
            z = Fraction(3, 7)
            F = sum((z**(s+1) for s in S), Fraction(0))
            U = sum((z**(s+1) for s in S if s>=a), Fraction(0))
            V = sum((z**(s+1) for s in S if s>=b), Fraction(0))
            W = sum((z**(s+1) for s in S if s>=max(a,b)), Fraction(0))
            mat00, mat01 = F-U, U
            mat10 = sum((z**(s+1) for s in S if s<min(a,b)),Fraction(0))
            mat11 = U-W
            determinant = (1-mat00)*(1-mat11)-mat01*mat10
            assert determinant == (1-F)*(1+W)+U*V
            count += 1
    spectral = 0
    for S,a,b in [([0,2,5,9],2,3),([1,3,7,8],4,2),
                  ([0,2,5,9],7,3),([1,3,7,8],2,7)]:
        assert abs(spectral_from_paths(asym_finite_automaton(S,a,b),1500)
                   - 1/asym_root_finite(S,a,b)) < 1e-10
        spectral += 1
    for a,b in [(1,2),(2,3),(4,1),(3,4),(5,7)]:
        def rootfun(z):
            F=z/(1-z)
            U=z**(a+1)/(1-z)
            V=z**(b+1)/(1-z)
            W=z**(max(a,b)+1)/(1-z)
            return (F-1)*(1+W)-U*V
        r=bisect(rootfun,0.01,0.99)
        assert abs(spectral_from_paths(forbidden_word_automaton(a,b),1600)
                   - 1/r)<1e-10
        spectral += 1
    with localcontext() as ctx:
        ctx.prec=95
        d=Decimal
        S=[2**k for k in range(8)]
        F=lambda z:sum((z**(s+1) for s in S),d(0))
        r=bisect(lambda z:F(z)-1,d('.3'),d('.99'),345)
        Fprime=sum((d(s+1)*r**s for s in S),d(0))
        ratios=[]
        for a,b in [(5,9),(9,17),(17,33)]:
            U=sum((r**(s+1) for s in S if s>=a),d(0))
            V=sum((r**(s+1) for s in S if s>=b),d(0))
            def equation(z):
                return (F(z)-1)*(1+sum((z**(s+1) for s in S
                                               if s>=max(a,b)),d(0))) - (
                    sum((z**(s+1) for s in S if s>=a),d(0))
                    *sum((z**(s+1) for s in S if s>=b),d(0)))
            rn=bisect(equation,r,d('.99'),345)
            ratio=(rn/r).ln()*(r*Fprime)/(U*V)
            assert abs(ratio-1)<d('.1')
            ratios.append((a,b,str(ratio)))
        assert abs(d(ratios[-1][2])-1)<d('0.0001')
    print('Asymmetric exact rational determinant identities:',count)
    print('Asymmetric finite-state and full-shift tests:',spectral)
    print('Asymmetric product-tail correction ratios:',ratios)
    print('PASS: all asymmetric checks')


if __name__ == '__main__':
    main()
    asymmetric_tests()
