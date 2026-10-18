"""Exhaustive small-carrier check for finite monotone reflexive neighborhood products.

Only Python's standard library is used.  This tests the stated finite cases;
the unrestricted characterization and cardinality bounds require the proof.
"""
from itertools import product


def families(n):
    """Nonempty upward-closed neighborhood families at distinguished point 0,
    with every member containing 0."""
    containing = [s for s in range(1 << n) if s & 1]
    result = []
    for select in range(1, 1 << len(containing)):
        f = frozenset(s for i, s in enumerate(containing) if (select >> i) & 1)
        if all(t in f for s in f for t in containing if (s & t) == s):
            result.append(f)
    return result


def is_filter(f):
    return all((u & v) in f for u in f for v in f)


def product_box(rows, f, g):
    return any(all((v & rows[i]) == v for i in range(len(rows)) if (u >> i) & 1)
               for u in f for v in g)


def modal_values(p, n, m, f, g):
    rows = [sum(1 << j for j in range(m) if (p >> (i*m+j)) & 1)
            for i in range(n)]
    columns = [sum(1 << i for i in range(n) if (p >> (i*m+j)) & 1)
               for j in range(m)]
    qx = sum(1 << i for i in range(n) if rows[i] in g)
    qy = sum(1 << j for j in range(m) if columns[j] in f)
    return product_box(rows, f, g), qx in f, qy in g


def verify(n, m):
    ff, gg = families(n), families(m)
    first_failure_pairs, second_failure_pairs = 0, 0
    simultaneously_failing_pairs = 0
    examined = 0
    witness = None
    for f, g in product(ff, gg):
        theory_first = (1 in f) or is_filter(g)
        theory_second = (1 in g) or is_filter(f)
        first_ok, second_ok, joint_fail = True, True, False
        for p in range(1 << (n*m)):
            value_product, value_hv, value_vh = modal_values(p,n,m,f,g)
            examined += 1
            assert not value_product or (value_hv and value_vh)
            if value_hv and not value_product:
                first_ok = False
            if value_vh and not value_product:
                second_ok = False
            if value_hv and value_vh and not value_product:
                joint_fail = True
                if witness is None:
                    witness = (sorted(f), sorted(g), p)
        assert first_ok == theory_first, (n,m,'first',f,g)
        assert second_ok == theory_second, (n,m,'second',f,g)
        first_failure_pairs += not first_ok
        second_failure_pairs += not second_ok
        simultaneously_failing_pairs += joint_fail
    print(f'{n}x{m}: families={len(ff)}*{len(gg)}, '
          f'valuations={examined}, '
          f'first_fail={first_failure_pairs}, '
          f'second_fail={second_failure_pairs}, '
          f'both_same_valuation={simultaneously_failing_pairs}')
    return witness


if __name__ == '__main__':
    witnesses={}
    for n in range(1,4):
        for m in range(1,4):
            witnesses[n,m]=verify(n,m)
    f2 = frozenset({3})
    g3 = frozenset({3,5,7})
    p23 = (1<<0) | (1<<1) | (1<<3) | (1<<5)
    assert modal_values(p23,2,3,f2,g3)==(False, True, False)
    f3=g3
    p33=sum(1<<(i*3+j) for i,j in ((0,0),(0,1),(1,0),(1,2),(2,1)))
    assert modal_values(p33,3,3,f3,g3)==(False,True,True)
    print('EXACT_FINITE_T_PRODUCT_OK; 2x3 and 3x3 witnesses confirmed')
