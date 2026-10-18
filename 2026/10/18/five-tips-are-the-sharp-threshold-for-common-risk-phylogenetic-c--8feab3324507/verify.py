"""Exact independently reproducible verification of the five-tip conservation threshold.

Uses only Python's standard library.  All numbers are rational.
The universal argument for arbitrary edge lengths is given in RESULT.md;
finite checks below are not substituted for that argument.
"""
from fractions import Fraction as F
from itertools import combinations

# Each pair is (child, length), and each internal node is a tuple of child pairs.
# The rooted tree has root r, two children X and Y, and tips A,B,C,D,E.
# Shared root height is four.  Its crown split is (A,B) versus (C,(D,E)).
tree = (
    ((('A', F(1)), ('B', F(1))), F(3)),
    ((('C', F(2)), ((('D', F(1)), ('E', F(1))), F(1))), F(2)),
)

def leaves(node):
    if isinstance(node, str):
        return frozenset([node])
    return frozenset().union(*(leaves(ch) for ch, _ in node))

def edges(node):
    if isinstance(node, str):
        return []
    out = []
    for child, length in node:
        out.append((leaves(child), length))
        out.extend(edges(child))
    return out

names = sorted(leaves(tree))
edge_data = edges(tree)
assert names == list('ABCDE')
assert len(edge_data) == 8
assert all(w > 0 for _, w in edge_data)

# An edge contributes to rooted Faith PD iff a descendant is present.
def pd(survivors):
    return sum((w for desc, w in edge_data if desc & survivors), F(0))

def direct_hed(taxon, q):
    other = [x for x in names if x != taxon]
    answer = F(0)
    for r in range(5):
        for chosen in combinations(other, r):
            s = frozenset(chosen)
            mass = (1-q)**r * q**(4-r)
            answer += mass * (pd(s | {taxon})-pd(s))
    return answer

def edge_formula(taxon, q):
    return sum((w*q**(len(desc)-1) for desc, w in edge_data if taxon in desc), F(0))

# The two root-crown stems are a=3 (two-tip) and b=2 (three-tip),
# with the nested cherry at depth 3 and root-to-tip height H=4.
# Expected HED profiles: Psi_A=Psi_B=1+3q, Psi_C=2+2q^2,
# Psi_D=Psi_E=1+q+2q^2.
for q in (F(1, 100), F(1, 5), F(1, 2), F(4, 5), F(99, 100)):
    expected = {'A': 1+3*q, 'B':1+3*q, 'C':2+2*q*q,
                'D':1+q+2*q*q, 'E':1+q+2*q*q}
    assert {t:edge_formula(t,q) for t in names} == expected
    for t in names:
        assert edge_formula(t,q) == direct_hed(t,q)
    if q < F(1,2):
        assert expected['C'] > max(expected[t] for t in 'ABDE')
    elif q > F(1,2):
        assert expected['A'] == expected['B'] > max(expected[t] for t in 'CDE')
    else:
        assert expected['A'] == expected['B'] == expected['C'] > expected['D']

# Exact symbolic differences as polynomial coefficient tuples in q.
# Psi_C-Psi_A = (1-q)(1-2q); Psi_C-Psi_D=(1-q).
assert [x-y for x,y in zip((2,0,2),(1,3,0))] == [1,-3,2]
assert [x-y for x,y in zip((2,0,2),(1,1,2))] == [1,-1,0]
for q in (F(0), F(1,5), F(1,2), F(4,5), F(1)):
    assert (2+2*q*q)-(1+3*q) == (1-q)*(1-2*q)
    assert (2+2*q*q)-(1+q+2*q*q) == (1-q)

# Verify the 2+3 criterion in a second rational example and its boundary.
# For all 0<b<a<H and b<t<H, the three candidate expressions are
# two-tip H-a+a*q, 3-subtree singleton H-b+b*q^2, nested cherry H-t+(t-b)q+b*q^2.
for H,a,b,t in [(F(5),F(3),F(2),F(4)),
                 (F(5),F(2),F(2),F(4)),
                 (F(5),F(4),F(2),F(4,1)+F(1,2)),
                 (F(10),F(7),F(4),F(8))]:
    for q in (F(1,10), F(3,5), F(9,10)):
        pair = H-a+a*q
        singleton = H-b+b*q*q
        nested = H-t+(t-b)*q+b*q*q
        assert singleton-nested == (t-b)*(1-q)
        assert singleton-pair == (1-q)*(a-b*(1+q))
        assert H >= max(pair,singleton,nested)

print('VERIFY_OK taxa=5 rooted_edges=8 surviving_subsets=80 roots=1/2 exact_hed_formula=PASS exact_global_winners=PASS universal_factor_identities=PASS')
