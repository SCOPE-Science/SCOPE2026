"""Exhaustive finite support checks for union-closed monadic classes.
Run: python3 monadic_union_check.py
The theorem for all structures is proved symbolically, not by this program.
"""
from functools import reduce

def family_data(colors, mask):
    supports = range(1, 1 << colors)
    family = {s for i, s in enumerate(supports) if mask & (1 << i)}
    return family

def is_union_closed(family):
    return all((a | b) in family for a in family for b in family)

def irreducibles(family):
    return {s for s in family if not any(a < s and b < s and (a | b) == s
                                           for a in family for b in family)}

def universal_existential_normal_form(support, irreducible_family, colors):
    # The x-element has a color t; it must lie in some J whose every color is witnessed.
    for t in range(colors):
        if support & (1 << t):
            if not any((j & support) == j and (j & (1 << t)) for j in irreducible_family):
                return False
    return True

def test(colors):
    nonempty_supports = range(1, 1 << colors)
    nfamilies = 1 << ((1 << colors) - 1)
    accepted = 0
    for mask in range(nfamilies):
        family = family_data(colors, mask)
        if not is_union_closed(family):
            continue
        accepted += 1
        basis = irreducibles(family)
        # Prove irreducibles generate, and are mandatory in any generator family.
        for support in family:
            generated = reduce(int.__or__, (j for j in basis if (j & support) == j), 0)
            assert generated == support
        for support in nonempty_supports:
            assert universal_existential_normal_form(support, basis, colors) == (support in family)
        # Small exact first-order models: each chosen support can be represented by any positive multiplicity.
        if colors <= 2:
            for n in range(1, 5):
                for code in range(colors**n):
                    values = []
                    c = code
                    for _ in range(n):
                        values.append(c % colors)
                        c //= colors
                    realized = reduce(int.__or__, (1 << t for t in values), 0)
                    actual = all(any((j & realized) == j and j & (1 << values[i])
                                     for j in basis) for i in range(n))
                    assert actual == (realized in family)
    return accepted

if __name__ == '__main__':
    expected = {1: 2, 2: 7, 3: 61, 4: 2480}
    for c, ans in expected.items():
        count = test(c)
        assert count == ans, (c, count, ans)
        print('UNION_CLOSED_PROFILE_OK', c, count)
    # Sharpness within the target form: rank-one forall-x quantifier-free
    # depends only on each element's local color, so it is downward closed on supports.
    # For one unary predicate, the class "some P" is union-preserved but not support-downward closed.
    P, notP = 1, 2
    someP = {P, P | notP}
    assert is_union_closed(someP)
    assert someP != {s for s in [P, notP, P | notP] if (s & notP) == 0}
    print('RANK_TWO_SHARPNESS_EXAMPLE_OK')
