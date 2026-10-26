"""Independent constructive check for the two exceptional graph families.
Use: python3 check_types.py
"""
from itertools import combinations
n=7
pairs=list(combinations(range(n),2))
index={e:j for j,e in enumerate(pairs)}
def bits(edges):
    return sum(1<<index[tuple(sorted(e))] for e in edges)
A,B=set(),set()
for v in range(n):
    rest=[u for u in range(n) if u!=v]
    clique=list(combinations(rest,2))
    for u in rest:
        A.add(bits(clique+[(v,u)]))
    for u,w in combinations(rest,2):
        B.add(bits([e for e in clique if e!=(u,w)]+[(v,u),(v,w)]))
assert len(A)==42 and len(B)==105 and not(A&B)
# A depth-four shattered tree with precisely sixteen hypotheses
# must make an exact 8-versus-8 split at its root.
q=[bits([e for e in pairs if all((s>>u)&1 for u in e)]) for s in range(1<<n)]
for mask in A|B:
    assert mask.bit_count()==16
    assert all((mask&t).bit_count()!=8 for t in q)
# Compare the exhaustive verifier's computed exception list.
from pathlib import Path
out=Path('verification_output.txt').read_text(encoding='utf-8')
actual={int(line.split()[1],16) for line in out.splitlines() if line.startswith('FAIL ')}
assert actual==A|B,(len(actual),len(A|B))
print('TWO_TYPES_CONFIRMED',len(A),len(B),len(actual))
