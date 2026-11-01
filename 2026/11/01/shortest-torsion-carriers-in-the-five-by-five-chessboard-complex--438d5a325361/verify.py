#!/usr/bin/env python3
"""Exact finite checks for the five-by-five chessboard octahedral carrier theorem.
Only Python 3 standard library and the neighboring COCHAIN.json file are needed.
"""
import itertools, json
from collections import Counter
from pathlib import Path

N=5
P=3
cells=tuple(range(N*N))
def faces(k):
    return sorted(tuple(sorted(N*r+c for r,c in zip(rows,cols)))
       for rows in itertools.combinations(range(N),k)
       for cols in itertools.permutations(range(N),k))
f1,f2,f3,f4=(faces(k) for k in range(1,5))
assert list(map(len,(f1,f2,f3,f4)))==[25,200,600,600]
inds={k:{f:i for i,f in enumerate(ff)} for k,ff in ((1,f1),(2,f2),(3,f3),(4,f4))}

# Sparse simplicial chains indexed by lexically ordered face tuples.
def add(d,t,a):
    b=d.get(t,0)+a
    if b: d[t]=b
    elif t in d: del d[t]
def bd(ch):
    out={}
    for f,a in ch.items():
        for i in range(len(f)):
            add(out,f[:i]+f[i+1:],(-1)**i*a)
    return out

def wedge_zero(i,j):return {i:1,j:-1}
def join_0_0_0(a,b,c):
    out={}
    for i,ai in a.items():
     for j,bj in b.items():
      for k,ck in c.items():
       seq=(i,j,k)
       inv=sum(seq[u]>seq[v] for u in range(3) for v in range(u+1,3))
       add(out,tuple(sorted(seq)),(-1)**inv*ai*bj*ck)
    return out

z=join_0_0_0(wedge_zero(0,1),wedge_zero(13,18),wedge_zero(22,24))
assert len(z)==8 and not bd(z)

obj=json.loads((Path(__file__).parent/'COCHAIN.json').read_text(encoding='utf-8'))
assert obj['coefficient_field']==3
wc={f3[i]:val for i,val in obj['nonzero_entries']}
assert len(wc)==184 and set(wc.values())<={1,2}
def pair(c):return sum(wc.get(t,0)*a for t,a in c.items())%3
assert all(sum((-1)**i*wc.get(f[:i]+f[i+1:],0) for i in range(4))%3==0 for f in f4)
assert pair(z)==2

def action(ch,row=None,col=None,transpose=False):
    if row is None:row=tuple(range(N))
    if col is None:col=tuple(range(N))
    out={}
    for face,a in ch.items():
        seq=tuple(row[x//5]*5+col[x%5] if not transpose
            else col[x%5]*5+row[x//5] for x in face)
        inv=sum(seq[u]>seq[v] for u in range(len(seq)) for v in range(u+1,len(seq)))
        add(out,tuple(sorted(seq)),(-1)**inv*a)
    return out
swap=(1,0,2,3,4)
values={
 'row_transposition':pair(action(z,row=swap)),
 'column_transposition':pair(action(z,col=swap)),
 'board_transpose':pair(action(z,transpose=True))}
assert values=={'row_transposition':1,'column_transposition':1,'board_transpose':1}

# Count all six-vertex induced octahedra and test every fundamental sphere.
by_type=Counter()
cohomology_values=Counter()
vertex_incidence=Counter()
pair_incidence=Counter()
for s in itertools.combinations(cells,6):
    incompatible=[(a,b) for a,b in itertools.combinations(s,2)
        if a//N==b//N or a%N==b%N]
    if len(incompatible)!=3 or len(set(itertools.chain.from_iterable(incompatible)))!=6:
        continue
    nh=sum(a//N==b//N for a,b in incompatible)
    assert nh in (1,2)
    by_type[nh]+=1
    oc=join_0_0_0(*[wedge_zero(a,b) for a,b in incompatible])
    assert len(oc)==8 and not bd(oc)
    p=pair(oc)
    assert p!=0
    cohomology_values[p]+=1
    vertex_incidence.update(s)
    pair_incidence.update(itertools.combinations(s,2))
assert by_type=={1:900,2:900}
assert len(vertex_incidence)==25 and set(vertex_incidence.values())=={432}
assert len(pair_incidence)==300
assert all(count==(54 if a//N==b//N or a%N==b%N else 108)
           for (a,b),count in pair_incidence.items())

# Exact row-reduction over the prime field for the two relevant differentials.
def gf3rank(columns):
    pivots={}
    for initial in columns:
        v={j:x%3 for j,x in initial.items() if x%3}
        while v:
            p=min(v)
            w=pivots.get(p)
            if w is None:
                if v[p]==2:v={i:(2*a)%3 for i,a in v.items()}
                pivots[p]=v
                break
            m=v[p]
            for i,a in w.items():
                nv=(v.get(i,0)-m*a)%3
                if nv:v[i]=nv
                else:v.pop(i,None)
    return len(pivots)

def columns(higher,lower):
    ix={f:i for i,f in enumerate(lower)}
    for face in higher:
        yield {ix[face[:i]+face[i+1:]]:(-1)**i for i in range(len(face))}
r2=gf3rank(columns(f3,f2))
r3=gf3rank(columns(f4,f3))
assert (r2,r3)==(176,423)
assert len(f3)-r2-r3==1

print('FACE_COUNTS',list(map(len,(f1,f2,f3,f4))))
print('RANKS_MOD_3',r2,r3,'DIM_H2_MOD_3',len(f3)-r2-r3)
print('EIGHT_FACE_CYCLE_BOUNDARY_ZERO',len(z),'DUAL_PAIRING',pair(z),'COCHAIN_SUPPORT',len(wc))
print('GENERATOR_ACTIONS',values)
print('OCTAHEDRAL_SUPPORTS',sum(by_type.values()),'TYPES',dict(sorted(by_type.items())))
print('ALL_1800_NONZERO_PAIRINGS',dict(sorted(cohomology_values.items())))
print('BLOCK_INCIDENCE',set(vertex_incidence.values()),'ATTACK',54,'COMPATIBLE',108)
print('VERIFY_OK')
