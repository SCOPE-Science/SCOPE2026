"""Independently replay face collapses, signed integral pivots, and affine traces.

This program does not trust precomputed topology or signed-chain ranks.
Run with Python 3.10+; no external packages.
"""
import collections
import itertools
import json
from pathlib import Path

P=19
c=json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf-8'))
R={x*x%P for x in range(1,P)}
assert sorted(R)==c['quadratic_residues']
N=[{(v+r)%P for r in R} for v in range(P)]
faces={0}
for target in N:
    v=sorted(target)
    for k in range(1,len(v)+1):
        for t in itertools.combinations(v,k):
            faces.add(sum(1<<z for z in t))
assert [sum(s.bit_count()==k for s in faces) for k in range(1,10)]==c['face_counts_by_cardinality']
assert set(range(19))==set(v for nei in N for v in nei)
assert sum(s.bit_count()==3 for s in faces)==969

cofaces={s:set() for s in faces if s}
for s in faces:
    if not s: continue
    for bit in range(P):
        if s & (1<<bit):
            low=s^(1<<bit)
            if low: cofaces[low].add(s)
live=faces-{0}
for low,high in c['collapse_pairs_bitmasks']:
    assert low in live and high in live
    assert high.bit_count()==low.bit_count()+1
    assert len(cofaces[low])==1 and high in cofaces[low]
    assert not cofaces[high]
    for s in (low,high):
        live.remove(s)
        for bit in range(P):
            if s & (1<<bit):
                sub=s^(1<<bit)
                if sub and sub in live:
                    cofaces[sub].remove(s)
assert len(c['collapse_pairs_bitmasks'])==3508
assert [sum(s.bit_count()==k for s in live) for k in range(1,5)]==c['collapsed_face_counts_by_cardinality']
assert max(s.bit_count() for s in live)==4

# Build signed C_3 -> C_2 boundary afresh, in ascending bit-mask basis.
tris=sorted(s for s in live if s.bit_count()==3)
tetra=sorted(s for s in live if s.bit_count()==4)
index={s:i for i,s in enumerate(tris)}
rows={i:{} for i in range(len(tris))}
cols={j:{} for j in range(len(tetra))}
for j,t in enumerate(tetra):
    verts=[v for v in range(P) if t&(1<<v)]
    for k,v in enumerate(verts):
        i=index[t^(1<<v)]; sign=(-1)**k
        rows[i][j]=sign;cols[j][i]=sign

def entry(i,j,val):
    if val:rows[i][j]=val;cols[j][i]=val
    else:rows[i].pop(j,None);cols[j].pop(i,None)
for i,j,sign in c['boundary3_pivots_row_column_sign']:
    assert i in rows and j in cols and rows[i][j]==sign and abs(sign)==1
    for jj,a in list(rows[i].items()):
        if jj!=j:
            for ii,b in list(cols[j].items()):
                if ii!=i:
                    entry(ii,jj,rows[ii].get(jj,0)-b*a*sign)
    for ii in list(cols[j]):entry(ii,j,0)
    for jj in list(rows[i]):entry(i,jj,0)
    rows.pop(i);cols.pop(j)
assert len(c['boundary3_pivots_row_column_sign'])==404
assert [len(rows),len(cols)]==c['remaining_boundary3_shape']
assert sum(len(x) for x in rows.values())==c['remaining_boundary3_nonzero_entries']==0
# The whole 2-skeleton was complete, hence pi_1=0 and rank(d2)=171-19+1=153.
assert len(tris)-153-404==1 and len(tetra)-404==78

# Complete affine character: H2 has rank 1, and the affine group has odd order.
# Thus the H2-character is trivial; signed simplex Lefschetz yields H3 traces.
chars=collections.Counter()
for a in sorted(R):
    for b in range(P):
        g=lambda v:(a*v+b)%P
        assert all({g(v) for v in N[u]}==N[g(u)] for u in range(P))
        lefschetz=0
        for s in faces:
            if s==0: continue
            verts=[v for v in range(P) if s&(1<<v)]
            moved=[g(v) for v in verts]
            if set(moved)!=set(verts):continue
            idx={v:i for i,v in enumerate(verts)}
            perm=[idx[v] for v in moved]
            inversions=sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
            lefschetz+=(-1)**(len(verts)-1+inversions)
        h3=2-lefschetz
        if a==1 and b==0:key='identity'
        elif a==1:key='translation'
        elif pow(a,3,P)==1:key='multiplier_order_3'
        else:
            assert pow(a,9,P)==1
            key='multiplier_order_9'
        chars[(key,h3)]+=1
assert dict(chars)=={('identity',78):1,('translation',2):18,
                     ('multiplier_order_3',-3):38,('multiplier_order_9',0):114},chars
assert sum(value*count for (label,value),count in chars.items())==0
print('PASS: 8246 nonempty faces, 3508 elementary collapses, 404 integral unit pivots; homotopy S2 wedge 78 S3; affine H3-character 78/2/-3/0; invariant H3=0')
