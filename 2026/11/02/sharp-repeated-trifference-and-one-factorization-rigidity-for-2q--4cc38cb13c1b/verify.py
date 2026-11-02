"""Standalone finite verification of ternary 2-trifferent length-five rigidity.
Finite checks supplement, but do not replace, the general theorem's proof.
"""
from itertools import combinations, permutations
from collections import Counter

V = tuple(range(6))
E = frozenset(combinations(V, 2))
def perfect_matchings(vertices):
    if not vertices:
        yield frozenset()
        return
    a, *rest = vertices
    for b in rest:
        remain = tuple(x for x in rest if x != b)
        for other in perfect_matchings(remain):
            yield frozenset({(a, b)} | set(other))
MS = list(perfect_matchings(V))
assert len(MS) == 15 and len(set(MS)) == 15
FACTORS = [s for s in combinations(range(15),5) if len(frozenset().union(*(MS[i] for i in s)))==15]
assert len(FACTORS)==6
assert len(set(FACTORS))==6
first=FACTORS[0]
for s in FACTORS:
    for tri in combinations(V,3):
        trifference=sum(not any(set(pair).issubset(tri) for pair in MS[j]) for j in s)
        assert trifference==2,(s,tri,trifference)

# Check unique orbit of the six 1-factorizations under point relabeling.
fac_set=set(FACTORS)
actions=[]
for perm in permutations(V):
    remap=[]
    for m in MS:
        image=frozenset(tuple(sorted((perm[u],perm[v]))) for u,v in m)
        remap.append(MS.index(image))
    actions.append(tuple(remap))
images={tuple(sorted(actions[p][j] for j in first)) for p in range(len(actions))}
assert images==fac_set

# Independent checks of the count and the label formulas.
ordered_row_matrices=len(FACTORS)*120*6**5
codebooks=ordered_row_matrices//720
assert ordered_row_matrices==5598720 and codebooks==7776
# Each row is a distinct word, so each unordered codebook has exactly 6! orderings.
print('NUMBER_OF_MATCHINGS',len(MS))
print('NUMBER_OF_FACTORIZATIONS',len(FACTORS))
print('NUMBER_OF_SYMMETRY_CLASSES',1)
print('LABELED_UNORDERED_CODEBOOKS',codebooks)
print('ORDERED_CODE_MATRICES',ordered_row_matrices)
print('TRIFFERENCE_ONE_FACTORIZATION_VERIFY_OK')

# Direct independent tests of the constructive infinite-parameter family.
# A cyclic round-robin one-factorization is checked without relying on
# the abstract proof. These finite tests do not prove the universal statement.
for q in range(3,9):
    odd = 2*q-1
    vertices = tuple(range(2*q))
    matchings = []
    for a in range(odd):
        pairs = [(odd,a)] + [tuple(sorted(((a+j)%odd,(a-j)%odd))) for j in range(1,q)]
        assert len(pairs) == q and len(set(v for pair in pairs for v in pair)) == 2*q
        matchings.append(tuple(frozenset(pair) for pair in pairs))
    edge_counts = Counter(tuple(sorted(pair)) for matching in matchings for pair in matching)
    assert len(edge_counts) == q*(2*q-1) and set(edge_counts.values()) == {1}
    # Actual q-ary code: each pair in one factor receives its own symbol.
    columns = []
    for matching in matchings:
        color = {}
        for c, pair in enumerate(matching):
            for v in pair:
                assert v not in color
                color[v] = c
        columns.append(color)
    code = [tuple(column[v] for column in columns) for v in vertices]
    assert len(set(code)) == 2*q
    for trip in combinations(vertices,3):
        separated = sum(len({column[v] for v in trip}) == 3 for column in columns)
        assert separated == 2*q-4, (q, trip, separated)
    print('ROUND_ROBIN_PARAMETER_VERIFIED',q,2*q,2*q-1,2*q-4)
print('GENERAL_FAMILY_FINITE_CHECKS_OK')
