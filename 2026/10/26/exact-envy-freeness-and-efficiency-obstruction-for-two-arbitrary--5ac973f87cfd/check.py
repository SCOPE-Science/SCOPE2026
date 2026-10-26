#!/usr/bin/env python3
"""Standalone exhaustive verifier for two-person Boolean allocations.

For each m<=3 enumerate every pair of Boolean set functions on 2^[m].
Compute envy and Pareto status directly, without using the pairwise proof.
"""
from collections import Counter


def classification(m, vf, vg):
    q = 1 << m
    mask = q-1
    utilities = [(vf >> s & 1, vg >> (mask ^ s) & 1) for s in range(q)]
    efficient = [not any(a >= x and b >= y and (a > x or b > y)
                         for a,b in utilities) for x,y in utilities]
    fair = [(vf >> s & 1) >= (vf >> (mask ^ s) & 1)
            and (vg >> (mask ^ s) & 1) >= (vg >> s & 1)
            for s in range(q)]
    return any(fair), any(e and f for e,f in zip(efficient, fair))


def predicted_obstruction(m, vf, vg):
    if vf != vg or vf == 0:
        return False
    full = (1 << m)-1
    return not any((vf >> s & 1) and (vf >> (full ^ s) & 1)
                   for s in range(1 << m))


def verify(m):
    q=1 << m
    M=1 << q
    obs = Counter()
    conditional = Counter()
    for vf in range(M):
        for vg in range(M):
            ef, efpo = classification(m, vf, vg)
            no = predicted_obstruction(m, vf, vg)
            assert (not efpo) == no, (m,vf,vg)
            z = (1-(vf&1))+(1-(vg&1))
            obs[('noEF',)] += not ef
            obs[('noEFPO',)] += not efpo
            obs[('EFonly',)] += ef and not efpo
            conditional[(z, 'total')] += 1
            conditional[(z, 'noEFPO')] += not efpo
    L = 2**(m-1)
    expected = {
        ('noEF',): 2**L,
        ('noEFPO',): 3**L-1,
        ('EFonly',): 3**L-1-2**L,
    }
    assert obs == expected, (m, obs, expected)
    C = 4*16**(L-1)  # profiles for one specified pair of empty-bundle values
    expected_cond = {
        (0, 'noEFPO'): 3**(L-1),
        (1, 'noEFPO'): 0,
        (2, 'noEFPO'): 2*3**(L-1)-1
    }
    # For fixed first (empty/full) pair, L-1 further pairs contribute 16^(L-1).
    # z=0: one admissible first-pair pattern, then 3^(L-1) patterns.
    # z=2: two admissible first-pair patterns, excluding allzero.
    # z=1 encompasses two fixed-empty-bit configurations, zero failures.
    for z in (0,1,2):
        expected_total = 2*C if z==1 else C
        assert conditional[(z,'total')]==expected_total, (m,z, conditional)
        assert conditional[(z,'noEFPO')]==expected_cond[(z,'noEFPO')], (m,z,conditional,expected_cond)
    print(f'm={m} valuations={M*M} EF_absent={obs[("noEF",)]} EF_PO_absent={obs[("noEFPO",)]} '
          f'EF_but_not_PO={obs[("EFonly",)]} conditional_noEFPO=' +
          str(tuple(conditional[(z,"noEFPO")] for z in (0,1,2))))


if __name__ == '__main__':
    for m in (1,2,3):
        verify(m)
    print('PASS: direct exhaustive feasibility, Pareto and formula checks')
