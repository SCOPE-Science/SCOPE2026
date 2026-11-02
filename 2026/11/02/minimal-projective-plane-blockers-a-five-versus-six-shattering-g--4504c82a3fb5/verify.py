#!/usr/bin/env python3
"""Standalone exhaustive verifier for minimal line-blocker shattering in PG(2,3).
Run: python3 verify.py [certificate.json]. Uses only Python standard library.
"""
from collections import Counter
from itertools import combinations,product
import json,sys

path=sys.argv[1] if len(sys.argv)>1 else 'certificate.json'
with open(path,encoding='utf-8') as f:cert=json.load(f)
assert cert['schema_version']==1 and cert['q']==3
points=tuple(tuple(p) for p in cert['points'])
assert len(points)==13 and len(set(points))==13
for p in points:
    assert all(x in range(3) for x in p) and next(x for x in p if x)==1
# Independent recomputation of each projective line from its normal vector.
expected_lines={sum(1<<i for i,(x,y,z) in enumerate(points) if (a*x+b*y+c*z)%3==0)
                for a,b,c in points}
lines=tuple(sorted(cert['line_masks']))
assert len(lines)==13 and set(lines)==expected_lines
assert all(L.bit_count()==4 for L in lines)
assert all((a&b).bit_count()==1 for a,b in combinations(lines,2))
assert all(sum((L>>i)&1 for L in lines)==4 for i in range(13))
assert all(sum((L>>i)&1 and (L>>j)&1 for L in lines)==1
           for i,j in combinations(range(13),2))

# A set is minimal line-hitting iff it hits all 13 lines and each selected
# point has a tangent: a line meeting the set at exactly that point.
def is_minimal(M):
    return all(M&L for L in lines) and all(any((M&L)==(1<<p) for L in lines)
                                                   for p in range(13) if M>>p&1)
H=tuple(M for M in range(1<<13) if is_minimal(M))
assert H==tuple(cert['minimal_blocker_masks'])
assert len(H)==247 and Counter(M.bit_count() for M in H)=={4:13,6:234}
assert set(M for M in H if M.bit_count()==4)==set(lines)
# Non-concurrent line triples define 234 distinct projective triangles.
triangles=set()
for A,B,C in combinations(lines,3):
    if A&B&C:continue
    T=(A|B|C)&~((A&B)|(B&C)|(A&C))
    assert T.bit_count()==6
    triangles.add(T)
assert len(triangles)==234
assert triangles=={M for M in H if M.bit_count()==6}
print('PG3_BLOCKING_CLASSIFICATION_PASS minimal=247 lines=13 triangles=234')

# Full trace calculation across ALL supports, not a sample.
expected={3:{8:286},4:{15:13,16:702},5:{29:117,31:468,32:702},
          6:{56:468,57:78,60:936,61:234}}
for k in (3,4,5,6):
    counts=Counter()
    for S in combinations(range(13),k):
        trace={sum(((M>>p)&1)<<j for j,p in enumerate(S)) for M in H}
        counts[len(trace)]+=1
    assert counts==expected[k]
    assert {int(key):value for key,value in cert['expected_spectrum'][str(k)].items()}==expected[k]
    print('PG3_COMPLETE_TRACE_SPECTRUM_PASS',k,dict(sorted(counts.items())))

# Geometric classification: exactly 702 five-subsets are triangle-minus-point,
# each has exactly two extensions to a complete projective triangle.
extensions=Counter(T^(1<<i) for T in triangles for i in range(13) if (T>>i)&1)
assert len(extensions)==702 and all(m==2 for m in extensions.values())
for S in combinations(range(13),5):
    support=sum(1<<i for i in S)
    full=len({sum(((M>>p)&1)<<j for j,p in enumerate(S)) for M in H})==32
    assert full==(support in extensions)
print('PG3_FIVE_QUERY_GEOMETRIC_CLASSIFICATION_PASS shattered=702 each_extensions=2')

# Replay EVERY branch and leaf of the complete depth-six tree. No rank oracle
# is assumed: every terminal hypothesis is actually checked along its path.
leaves=[]; internal=[]
def replay(node,d,conditions):
    if d==0:
        assert set(node)=={'witness'}
        M=node['witness'];assert M in H
        assert all(((M>>i)&1)==ans for i,ans in conditions)
        leaves.append(M)
        return
    assert set(node)=={'query','zero','one'}
    i=node['query'];assert 0<=i<13 and i not in dict(conditions)
    internal.append(i)
    replay(node['zero'],d-1,conditions+[(i,0)])
    replay(node['one'],d-1,conditions+[(i,1)])
assert cert['tree_depth']==6
replay(cert['adaptive_tree'],6,[])
assert len(internal)==63 and len(leaves)==64 and len(set(leaves))==64
# All minimal blockers contain <=6 points; the all-positive path of any
# shattered depth-seven decision tree would require seven distinct points.
assert max(M.bit_count() for M in H)==6
print('PG3_LITTLESTONE_DEPTH6_TREE_PASS internal=63 leaves=64 unique=64')
print('PG3_LITTLESTONE_DEPTH7_UPPER_PASS max_positive_support=6')

# For PG(2,2), every minimal blocker is one of its seven lines;
# no depth-three tree exists, tested by independent exact binary recurrence.
p2=[]
for raw in product(range(2),repeat=3):
    if any(raw):p2.append(raw)
p2=sorted(p2)
L2=tuple(sorted({sum(1<<i for i,p in enumerate(p2)
                    if sum(a*b for a,b in zip(n,p))%2==0)
                 for n in p2}))
H2=[M for M in range(1<<7) if all(M&L for L in L2) and all(
    any((M&L)==(1<<i) for L in L2) for i in range(7) if M>>i&1)]
assert len(H2)==7 and set(H2)==set(L2)
qbits=[sum(1<<j for j,M in enumerate(H2) if M>>p&1) for p in range(7)]
from functools import lru_cache
@lru_cache(None)
def rank(version):
    best=0
    for p in qbits:
        a=version&p;b=version&~p
        if a and b:best=max(best,1+min(rank(a),rank(b)))
    return best
assert rank((1<<7)-1)==2
print('FANO_PLANE_CONTROL_PASS minimal=7 VC=2 Ldim=2')
print('ALL_PROJECTIVE_BLOCKER_SHATTERING_CHECKS_PASS')
