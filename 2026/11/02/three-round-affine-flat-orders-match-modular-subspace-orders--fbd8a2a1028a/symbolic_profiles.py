#!/usr/bin/env python3
"""Exact symbolic three-round spectra for ranked affine/projective flat posets.

Finite arithmetic based on the geometric pair-extension lemma in RESULT.md.
It is a cross-check, not an automated proof of the lemma or its unbounded case.
"""
import json

# Relation order: 0 = equal, 1 = first strictly below second,
# 2 = first strictly above second, 3 = incomparable.
def available_relations(R, r, s):
    ans = []
    if r == s:
        ans.append(0)
    if r < s:
        ans.append(1)
    if r > s:
        ans.append(2)
    if 0 < r < R and 0 < s < R:
        ans.append(3)
    return ans


def extension_mask(R, r, s, c, binary_affine_line=False):
    """Bit 4*a+b iff some third z has rel(x,z)=a, rel(y,z)=b."""
    assert c in available_relations(R, r, s)
    ans = set()
    reverse = {0: 0, 1: 2, 2: 1, 3: 3}
    # The third element z equals either x or y.
    ans.add((0, c))
    ans.add((reverse[c], 0))
    # z is strictly below/above both.
    if r > 0 and s > 0:
        ans.add((1, 1))
    if r < R and s < R:
        ans.add((2, 2))
    # z lies strictly between a comparable pair.
    if c == 1 and s-r >= 2:
        ans.add((2, 1))
    if c == 2 and r-s >= 2:
        ans.add((1, 2))
    # z is lower than one, incomparable to the other.
    if r >= 2 and c in (2, 3) and s > 0:
        ans.add((1, 3))
    if s >= 2 and c in (1, 3) and r > 0:
        ans.add((3, 1))
    # z is higher than one, incomparable to the other.
    if R-r >= 2 and c in (1, 3) and s < R:
        ans.add((2, 3))
    if R-s >= 2 and c in (2, 3) and r < R:
        ans.add((3, 2))
    # z is incomparable to both; only the two-point affine line fails.
    if 0 < r < R and 0 < s < R:
        if not (binary_affine_line and R == 2 and c == 3):
            ans.add((3, 3))
    return sum(1 << (4*reverse[a]+reverse[b]) for a,b in ans)


def pointed_spectrum(R, r, binary_affine_line=False):
    return frozenset(
        (c, extension_mask(R, r, s, c, binary_affine_line))
        for s in range(R+1)
        for c in available_relations(R, r, s)
    )


def structure_spectrum(R, binary_affine_line=False):
    return frozenset(pointed_spectrum(R, r, binary_affine_line)
                     for r in range(R+1))


def canonical_table():
    catalog = {}
    for R in range(3, 10):
        for r in range(R+1):
            key = (min(r,3),min(R-r,3))
            value = pointed_spectrum(R,r)
            assert key not in catalog or catalog[key] == value, (R,r,key)
            catalog[key] = value
    assert len(catalog) == 10, len(catalog)
    # Every truncated-rank state has a different pointed two-round type.
    assert len(set(catalog.values())) == len(catalog)
    return catalog


def run():
    catalog = canonical_table()
    for R in range(3,61):
        for r in range(R+1):
            key = (min(r,3),min(R-r,3))
            assert pointed_spectrum(R,r) == catalog[key],(R,r)
    assert structure_spectrum(2,True) != structure_spectrum(2,False)
    assert len({structure_spectrum(2,True),structure_spectrum(2,False),
                *[structure_spectrum(R) for R in range(3,15)]}) == 6
    stable = structure_spectrum(6)
    assert all(structure_spectrum(R) == stable for R in range(6,61))
    assert all(structure_spectrum(R) != stable for R in range(2,6))
    print('PASS: 10 distinct truncated (rank,corank) pointed spectra')
    print('PASS: six theories (two rank-two cases; ranks 3, 4, 5, >=6)')
    print('PASS: stabilization at lattice rank six for R=6..60')
    print('PASS: every R=2..5 type is distinct from the stable type')
    print('PROFILE_SIZE_TABLE='+json.dumps({str(R):[len(pointed_spectrum(R,r))
           for r in range(R+1)] for R in range(3,9)},sort_keys=True))
    # Machine-readable certificates for the finite symbolic case split.
    out = {'two_point_affine_line':[sorted(list(s)) for s in [pointed_spectrum(2,r,True) for r in range(3)]],
           'affine_line_at_least_three_points':[sorted(list(s)) for s in [pointed_spectrum(2,r,False) for r in range(3)]],
           'truncated_rank_states':[
             {'rank_cut':k[0],'corank_cut':k[1],
              'pair_extension_types':[{'pair_relation':c,'third_pattern_mask_hex':f'{v:04x}'}
                    for (c,v) in sorted(t)]}
             for k,t in sorted(catalog.items())]}
    with open('symbolic_certificate.json','w',encoding='utf-8') as f:
        json.dump(out,f,sort_keys=True,indent=2,ensure_ascii=False)
        f.write('\n')
    print('CERTIFICATE_WRITTEN symbolic_certificate.json')

if __name__ == '__main__':
    run()
