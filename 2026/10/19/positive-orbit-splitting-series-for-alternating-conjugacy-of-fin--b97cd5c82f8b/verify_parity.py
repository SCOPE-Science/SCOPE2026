"""Independent arithmetic and direct checks for alternating-label conjugacy of finite maps.

Uses only Python's standard library. Run: python3 verify_parity.py
This checker tests finite cases; the general assertions require the accompanying proof.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial


def partitions(n, largest=None):
    if n == 0:
        yield ()
        return
    for k in range(min(n, largest if largest is not None else n), 0, -1):
        for p in partitions(n - k, k):
            yield (k,) + p


def burnside_counts(bound):
    result = [(1, 1)]  # size zero; treated separately for alternating groups
    for n in range(1, bound + 1):
        ordinary = Fraction(0)
        signed = Fraction(0)
        for lam in partitions(n):
            multiplicities = Counter(lam)
            stabilizer = 1
            fixed = 1
            for d, m in multiplicities.items():
                stabilizer *= d**m * factorial(m)
                choices = sum(e * multiplicities[e] for e in multiplicities if d % e == 0)
                fixed *= choices**m
            term = Fraction(fixed, stabilizer)
            ordinary += term
            signed += (-1)**(n - len(lam)) * term
        assert ordinary.denominator == signed.denominator == 1
        result.append((int(ordinary), int(signed)))
    return result


def rooted_tree_types(bound):
    """Represent a rooted tree by the tuple of its ordered-canonical child codes."""
    all_trees = [()]
    size = {(): 1}
    by_size = defaultdict(list)
    by_size[1].append(())
    for n in range(2, bound + 1):
        choices = [tree for tree in all_trees if size[tree] < n]
        def build(start, remaining, members):
            if remaining == 0:
                t = tuple(members)
                size[t] = n
                by_size[n].append(t)
                return
            for j in range(start, len(choices)):
                t = choices[j]
                if size[t] <= remaining:
                    build(j, remaining - size[t], members + [t])
        build(0, n - 1, [])
        all_trees.extend(by_size[n])
    eligible = {}
    for tree in all_trees:
        mult = Counter(tree)
        eligible[tree] = all(eligible[child] and (size[child] % 2 == 0 or count == 1)
                             for child, count in mult.items())
    ordinary = [0] * (bound + 1)
    even_stable = ordinary[:]
    for n in range(1, bound + 1):
        ordinary[n] = len(by_size[n])
        even_stable[n] = sum(eligible[t] for t in by_size[n])
    return ordinary, even_stable, all_trees, size, eligible


def phi(n):
    return sum(1 for i in range(1, n + 1) if gcd(i, n) == 1)


def gcd(a, b):
    while b: a, b = b, a % b
    return a


def mobius(n):
    primes = 0
    d = 2
    while d*d <= n:
        if n % d == 0:
            primes += 1
            n //= d
            if n % d == 0:
                return 0
            while n % d == 0:
                n //= d
        d += 1
    return (-1)**(primes + (n > 1))


def multiply(a, b, N):
    result = [Fraction(0)] * (N + 1)
    for i, x in enumerate(a):
        if not x: continue
        for j, y in enumerate(b[:N + 1 - i]):
            if y: result[i + j] += x * y
    return result


def power(a, k, N):
    ans = [Fraction(1)] + [Fraction(0)] * N
    while k:
        if k & 1:
            ans = multiply(ans, a, N)
        k //= 2
        if k: a = multiply(a, a, N)
    return ans


def substitute(a, d, N):
    out = [Fraction(0)] * (N + 1)
    for i in range(N // d + 1):out[d * i] = a[i]
    return out


def cyclic_necklace_polynomials(rooted, N):
    """All and aperiodic weighted necklaces from Pólya and Möbius sums."""
    all_c = [Fraction(0)] * (N + 1)
    primitive = all_c[:]
    r = list(map(Fraction, rooted))
    for ell in range(1, N + 1):
        for d in range(1, ell + 1):
            if ell % d: continue
            term = power(substitute(r, d, N), ell // d, N)
            for i, v in enumerate(term):
                all_c[i] += Fraction(phi(d), ell) * v
                primitive[i] += Fraction(mobius(d), ell) * v
    return all_c, primitive


def product_from_components(counts, N, restrict_odd_repeats):
    ans = [Fraction(1)] + [Fraction(0)] * N
    for s in range(1, N + 1):
        number = int(counts[s])
        factor = [Fraction(0)] * (N + 1)
        for copies in range(N // s + 1):
            v = (comb(number, copies) if restrict_odd_repeats and (s % 2)
                 else comb(number + copies - 1, copies) if number > 0 else int(copies == 0))
            factor[s * copies] = v
        ans = multiply(ans, factor, N)
    return [int(x) if x.denominator == 1 else x for x in ans]


def positive_series(N):
    all_r, good_r, *_ = rooted_tree_types(N)
    C, _ = cyclic_necklace_polynomials(all_r, N)
    CR, PR = cyclic_necklace_polynomials(good_r, N)
    E = CR[:]
    for factor in range(2, N + 1, 2):
        for odd in range(1, N // factor + 1, 2):
            E[odd * factor] -= PR[odd]
    assert all(x.denominator == 1 and x >= 0 for x in C + E)
    return (product_from_components(C, N, False),
            product_from_components(E, N, True),
            [int(t) for t in E], good_r)


def canonical_cycle(seq):
    return min(seq[i:] + seq[:i] for i in range(len(seq)))


def direct_structure(N):
    _, _, trees, size, good = rooted_tree_types(N)
    ids = {t:i for i,t in enumerate(trees)}
    data = {ids[t]:(size[t], good[t]) for t in trees}
    comps = {}
    for ell in range(1, N + 1):
        def rec(rem, members):
            if len(members) == ell:
                if rem != 0:return
                cyc = canonical_cycle(tuple(members))
                if cyc in comps:return
                n = sum(data[x][0] for x in cyc)
                p = next(p for p in range(1, ell + 1)
                         if ell % p == 0 and all(cyc[j] == cyc[j%p] for j in range(ell)))
                k = ell // p
                w = sum(data[x][0] for x in cyc[:p])
                eligible = all(data[x][1] for x in cyc) and (k % 2 == 1 or w % 2 == 0)
                comps[cyc] = (n, eligible)
                return
            for i, (s,_) in data.items():
                if s <= rem:rec(rem - s, members + [i])
        for total in range(ell, N + 1):rec(total, [])
    all_count = [0]*(N+1)
    good_count = [0]*(N+1)
    for n, eligible in comps.values():
        all_count[n] += 1
        if eligible:good_count[n] += 1
    return (product_from_components(all_count, N, False),
            product_from_components(good_count, N, True))


def permutation_sign(p):
    return (-1)**sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))


def direct_labeled(N):
    for n in range(2, N + 1):
        perms = list(permutations(range(n)))
        odd = [p for p in perms if permutation_sign(p) == -1]
        even = [p for p in perms if permutation_sign(p) == 1]
        def action(f, p):
            out = [0]*n
            for i in range(n):out[p[i]]=p[f[i]]
            return tuple(out)
        seen = set()
        o = splits = alt = 0
        for f in product(range(n), repeat=n):
            if f in seen:continue
            sym_orbit = {action(f,p) for p in perms}
            seen |= sym_orbit
            o += 1
            if not any(action(f,p)==f for p in odd):splits += 1
            alt += 1 if len({action(f,p) for p in even}) == len(sym_orbit) else 2
        yield n, o, splits, alt


def main():
    N = 9
    reference = burnside_counts(15)
    ordinary, extra, connected, good_tree = positive_series(N)
    independently_ordinary, independently_extra = direct_structure(N)
    for n in range(2, N + 1):
        assert (ordinary[n], extra[n]) == reference[n] == (independently_ordinary[n], independently_extra[n]), n
    for n,o,g,a in direct_labeled(5):
        assert (o,g,a) == (*reference[n], sum(reference[n])), n
    print('TREE_COUNTS', good_tree[1:])
    print('ELIGIBLE_CONNECTED_COUNTS', connected[1:])
    print('SYMMETRIC_COUNTS', ordinary[1:])
    print('SPLIT_CLASS_COUNTS', extra[1:])
    print('ALTERNATING_COUNTS', [1]+[ordinary[n]+extra[n] for n in range(2,N+1)])
    print('BRUTE_LABELED_VERIFIED_N=2..5')
    print('SIGNED_BURNSIDE_VERIFIED_N=2..15; POSITIVE_RECURSION_VERIFIED_N=2..9')
    print('CHECKER_OK')

if __name__ == '__main__':main()
