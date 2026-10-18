"""Reproducible exact integral certificate for the Paley-37 flag complex.

Run: python3 verify_paley37.py paley37_integral_certificate.json
Only Python's standard library is needed.
"""
import collections
import itertools
import json
import math
import pathlib
import sys

p=37
quadratic={x*x%p for x in range(1,p)}
assert len(quadratic)==18 and 2 not in quadratic
neighbors=[{y for y in range(p) if (y-x)%p in quadratic} for x in range(p)]
faces=[[(i,) for i in range(p)]]
while True:
    nxt=[]
    for f in faces[-1]:
        for v in sorted(set.intersection(*(neighbors[x] for x in f))):
            if v>f[-1]:nxt.append((*f,v))
    if not nxt:break
    faces.append(nxt)
assert [len(z) for z in faces]==[37,333,888,555]
certpath=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(__file__).with_name('paley37_integral_certificate.json')
certificate=json.loads(certpath.read_text('utf8'))
assert certificate['prime']==p
assert certificate['residues']==sorted(quadratic)
assert certificate['f_vector']==[len(z) for z in faces]

def boundary(d):
    idx={f:i for i,f in enumerate(faces[d-1])}
    return {c:{idx[f[:i]+f[i+1:]]:(-1)**i for i in range(d+1)} for c,f in enumerate(faces[d])}

def verify_certificate(d):
    cols=boundary(d)
    rows={r:{} for r in range(len(faces[d-1]))}
    for c, column in cols.items():
        for r,v in column.items():rows[r][c]=v
    section=certificate[f'boundary_{d}']
    for r,c,s in section['unit_pivots']:
        assert rows[r][c]==s and abs(s)==1
        column=list(cols[c].items())
        row=list(rows[r].items())
        for cc,v in row:
            if cc==c:continue
            for rr,w in column:
                if rr==r:continue
                new=cols[cc].get(rr,0)-v*s*w
                if new:
                    cols[cc][rr]=new
                    rows[rr][cc]=new
                else:
                    cols[cc].pop(rr,None)
                    rows[rr].pop(cc,None)
            cols[cc].pop(r)
        for rr,_ in column:
            if rr!=r:rows[rr].pop(c)
        del rows[r]
        del cols[c]
    residual=[[c,r,v] for c,col in sorted(cols.items()) for r,v in sorted(col.items())]
    assert residual==section['residual_entries']
    assert len(rows)==section['remaining_rows']
    assert len(cols)==section['remaining_columns']
    assert all(abs(v)!=1 for _,_,v in residual)
    assert all(all(rows[r][c]==v for r,v in cols[c].items()) for c in cols)
    return len(section['unit_pivots']),residual,len(rows),len(cols)

b2=boundary(2)
b3=boundary(3)
for c,column in b3.items():
    composition=collections.Counter()
    for r,v in column.items():
        for rr,w in b2[r].items():composition[rr]+=v*w
    assert all(v==0 for v in composition.values())
rank2,res2,rows2,cols2=verify_certificate(2)
rank3units,res3,rows3,cols3=verify_certificate(3)
assert rank2==297 and res2==[] and (rows2,cols2)==(36,591)
assert rank3units==554 and (rows3,cols3)==(334,1)
assert len(res3)==74 and math.gcd(*(v for _,_,v in res3))==26
assert collections.Counter(v for _,_,v in res3)=={26:37,-26:37}
print('faces',*[len(f) for f in faces]);print('chain_identity d2*d3=0 confirmed on',len(b3),'columns')
print('integer_boundary2',rank2,'unit elementary factors; residual zero')
print('integer_boundary3',rank3units,'unit elementary factors plus Smith invariant',26)
print('integral_homology H0=Z H1=0 H2=Z^36 + Z/26 H3=0')

def modular_rank(columns, prime):
    basis={}
    for _, column in sorted(columns.items()):
        v={r:x%prime for r,x in column.items() if x%prime}
        while v:
            r=min(v)
            if r not in basis:
                inverse=pow(v[r],-1,prime)
                basis[r]={rr:(xx*inverse)%prime for rr,xx in v.items()}
                break
            coefficient=v[r]
            for rr,xx in basis[r].items():
                new=(v.get(rr,0)-coefficient*xx)%prime
                if new:v[rr]=new
                else:v.pop(rr,None)
    return len(basis)
for prime, expected3 in ((2,554),(3,555),(13,554)):
    assert modular_rank(b2,prime)==297
    assert modular_rank(b3,prime)==expected3
print('independent_modular_ranks',[(p,297,modular_rank(b3,p)) for p in [2,3,13]])

def trace_level(level,perm):
    v=0
    for face in level:
        mapped=[perm[i] for i in face]
        if sorted(mapped)==list(face):
            inv=sum(mapped[i]>mapped[j] for i in range(len(face)) for j in range(i+1,len(face)))
            v+=-1 if inv%2 else 1
    return v
chars=collections.Counter()
for a in sorted(quadratic):
    for b in range(p):
        perm=[(a*x+b)%p for x in range(p)]
        tr=sum((-1)**j*trace_level(fs,perm) for j,fs in enumerate(faces))-1
        expected=36 if a==1 and b==0 else -1 if a==1 else 0
        assert tr==expected,(a,b,tr,expected)
        chars[tr]+=1
assert chars=={36:1,-1:36,0:629}
assert all((2*(y-x))%p not in quadratic for x in range(p) for y in neighbors[x]);print('complement_isomorphism x->2x confirmed')
print('affine_character',dict(sorted(chars.items())),'666 group elements checked')
print('VERIFICATION SUCCESS')
