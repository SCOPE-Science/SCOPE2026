#!/usr/bin/env python3
"""Exact exhaustive tests for semantic fibers of strong modal chain frames."""
from collections import Counter, defaultdict
from itertools import product, combinations_with_replacement
from math import comb, factorial


def polynomial_product(factors):
    out = Counter({0: 1})
    for maximum in factors:
        new = Counter()
        for exp, coefficient in out.items():
            for t in range(maximum + 1):
                new[exp + t] += coefficient
        out = new
    return out


def records(a):
    result = []
    maximum = 0
    for p, height in enumerate(a):
        if height > maximum:
            result.append((p, height))
            maximum = height
    return tuple(result)


def ell_of(a):
    n = len(a)
    return tuple(next((z for z, height in enumerate(a) if height > x), n)
                 for x in range(n))


def operator_signature(a):
    n = len(a)
    return tuple(tuple(int(all(not (a[z] > x) or z >= threshold
                                   for z in range(n)))
                       for x in range(n))
                 for threshold in range(n + 1))


def fiber_factor_description(record, n):
    fixed = [0] * n
    free = []
    if record:
        for i, (p, h) in enumerate(record):
            fixed[p] = h
            end = record[i+1][0] if i+1 < len(record) else n
            for z in range(p+1, end):
                free.append((z, h))
    return tuple(fixed), tuple(free)


def verify(limit=7):
    assertions = 0
    total_examined = 0
    for n in range(1, limit+1):
        by_ell = defaultdict(list)
        sig_to_ell = {}
        for a in product(*(range(j+2) for j in range(n))):
            total_examined += 1
            ell = ell_of(a)
            rec = records(a)
            inferred = tuple(next((p for p,h in rec if h > x), n)
                             for x in range(n))
            assert ell == inferred
            assertions += 1
            # independently evaluate modal forcing on every upset
            signature = operator_signature(a)
            previous = sig_to_ell.setdefault(signature, ell)
            assert previous == ell
            assertions += 1
            assert all(ell[x] >= x and (x==0 or ell[x-1] <= ell[x])
                       for x in range(n))
            assertions += 1
            if n <= 4:
                R = {(x,z) for z,h in enumerate(a) for x in range(h)}
                for x in range(n):
                    for y in range(n):
                        for z in range(n):
                            assert not ((x,y) in R and (y,z) in R) or (x,z) in R
                assertions += 1
            by_ell[ell].append(a)

        all_ell = {tuple(f) for f in combinations_with_replacement(range(n+1), n)
                   if all(y >= i for i,y in enumerate(f))}
        assert set(by_ell) == all_ell
        assertions += 1
        catalan = comb(2*n+2, n+1)//(n+2)
        assert len(by_ell) == len(sig_to_ell) == catalan
        assertions += 1
        assert sum(len(v) for v in by_ell.values()) == factorial(n+1)
        assertions += 1
        assert sum(len(v)==1 for v in by_ell.values()) == 2**n
        assertions += 1
        total_poly = Counter()
        for ell, fiber in by_ell.items():
            rec = records(fiber[0])
            assert all(records(a) == rec for a in fiber)
            assertions += 1
            fixed, free = fiber_factor_description(rec,n)
            # All non-record columns are free and independently ranged.
            expected_count = 1
            for _, h in free:
                expected_count *= h+1
            assert expected_count == len(fiber)
            assertions += 1
            implied_set = {
                tuple(next((val for zz,val in assignment if zz==z), fixed[z])
                      for z in range(n))
                for possible in product(*(range(h+1) for z,h in free))
                for assignment in [tuple(zip((z for z,h in free),possible))]
            }
            assert implied_set == set(fiber)
            assertions += 1
            predicted_poly = polynomial_product([h for _,h in free])
            predicted_poly = Counter({e+sum(fixed): c for e,c in predicted_poly.items()})
            actual_poly = Counter(sum(a) for a in fiber)
            assert actual_poly == predicted_poly
            assertions += 1
            total_poly.update(actual_poly)
        expected_total_poly = polynomial_product([z+1 for z in range(n)])
        assert total_poly == expected_total_poly
        assertions += 1
        # Verify the source relation semigroup, the Catalan quotient,
        # and the multiplication orientation without relying on the proof.
        if n <= 4:
            all_cols = list(product(*(range(j+2) for j in range(n))))
            def pmax(a):
                out = [0]
                for v in a:
                    out.append(max(out[-1], v))
                return tuple(out)
            for a in all_cols:
                pa = pmax(a)
                for b in all_cols:
                    pb = pmax(b)
                    # Relational composition: x (R_a o R_b) z
                    # iff some y satisfies x R_a y and y R_b z.
                    product_matrix = {
                        (x, z) for x in range(n) for z in range(n)
                        if any(x < a[y] and y < b[z] for y in range(n))
                    }
                    c = tuple(max((a[y] for y in range(b[z])), default=0)
                              for z in range(n))
                    assert product_matrix == {(x, z) for z, h in enumerate(c)
                                              for x in range(h)}
                    assert pmax(c) == tuple(pa[pb[k]] for k in range(n+1))
                    assertions += 2
            # R_<= is only a left identity before passing to the quotient.
            if n >= 2:
                increasing = tuple(z+1 for z in range(n))
                sample = tuple([1] + [0]*(n-1))
                assert tuple(max((increasing[y] for y in range(sample[z])),default=0)
                             for z in range(n)) == sample
                assert tuple(max((sample[y] for y in range(increasing[z])),default=0)
                             for z in range(n)) != sample
                assertions += 2
        print('n=',n, 'frames=',factorial(n+1),'modalities=',catalan,
              'singleton_fibers=',2**n,'checks=',assertions)
    print('VERIFY_OK',assertions,'exact assertions;',total_examined,
          'accessibility matrices screened; all operators evaluated on every upset through n=',limit)

if __name__ == '__main__':
    verify()
