#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, deque

E=[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]
P=[]
for ei,(a,b) in enumerate(E):
    P.append((a,ei,b)); P.append((b,ei,a))

def valid_oriented(face):
    mv=set(); me=set(); out={}
    for j in face:
        v,e,w=P[j]
        if v in mv or e in me: return False
        mv.add(v); me.add(e); out[v]=w
    for s in out:
        seen=set(); x=s
        while x in out:
            if x in seen: return False
            seen.add(x); x=out[x]
    return True

def enum_faces_direct():
    layers={0:[()]}
    for k in range(1,7):
        layers[k]=[c for c in combinations(range(18),k) if valid_oriented(c)]
    return layers

def is_forest(edges):
    parent=list(range(6))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for ei in edges:
        a,b=E[ei]; ra,rb=find(a),find(b)
        if ra==rb:return False
        parent[ra]=rb
    return True

def forest_component_sizes(edges):
    adj=[[] for _ in range(6)]
    used=set()
    for ei in edges:
        a,b=E[ei]; adj[a].append(b);adj[b].append(a);used|={a,b}
    sizes=[];seen=set()
    for s in sorted(used):
        if s in seen:continue
        q=[s];seen.add(s);n=0
        while q:
            x=q.pop();n+=1
            for y in adj[x]:
                if y not in seen:seen.add(y);q.append(y)
        sizes.append(n)
    return sizes

def count_faces_forest_route():
    counts={0:1}
    for k in range(1,6):
        total=0
        for es in combinations(range(9),k):
            if is_forest(es):
                ways=1
                for s in forest_component_sizes(es): ways*=s
                total+=ways
        counts[k]=total
    counts[6]=0
    return counts

def rank_cols(cols):
    piv={};r=0
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;r+=1;break
    return r

def rank_rows(rows):
    # Same elimination on the transposed representation (rows instead of columns).
    return rank_cols([x for x in rows if x])

def boundary_data(layers,k):
    low=layers[k-1]; idx={f:i for i,f in enumerate(low)}
    cols=[]
    for f in layers[k]:
        x=0
        for i in range(k): x ^= 1<<idx[f[:i]+f[i+1:]]
        cols.append(x)
    rows=[0]*len(low)
    for j,x in enumerate(cols):
        y=x
        while y:
            b=(y & -y).bit_length()-1
            rows[b] |= 1<<j
            y &= y-1
    return cols,rows

def compose_zero(layers,k):
    if k<2:return True
    low=layers[k-2]; mid=layers[k-1]
    ilow={f:i for i,f in enumerate(low)}; imid={f:i for i,f in enumerate(mid)}
    # columns d_{k-1}
    dlow=[]
    for f in mid:
        x=0
        for i in range(k-1):x^=1<<ilow[f[:i]+f[i+1:]]
        dlow.append(x)
    for f in layers[k]:
        acc=0
        for i in range(k):acc ^= dlow[imid[f[:i]+f[i+1:]]]
        if acc:return False
    return True

layers=enum_faces_direct()
counts={k:len(v) for k,v in layers.items()}
expected={0:1,1:18,2:126,3:428,4:705,5:450,6:0}
assert counts==expected,(counts,expected)
assert count_faces_forest_route()==expected
ranks={}
for k in range(1,6):
    cols,rows=boundary_data(layers,k)
    a=rank_cols(cols); b=rank_rows(rows)
    assert a==b,(k,a,b)
    ranks[k]=a
    if k>=2: assert compose_zero(layers,k)
assert ranks=={1:1,2:17,3:109,4:319,5:386},ranks
betti={}
for k in range(1,6):
    betti[k-1]=len(layers[k])-ranks[k]-ranks.get(k+1,0)
assert betti=={0:0,1:0,2:0,3:0,4:64},betti
# graph parameters used in comparison with the published connectivity theorem
assert len(E)==9
assert max(sum(v in e for e in E) for v in range(6))==3
print('VERIFY_OK')
print('face_counts',expected)
print('boundary_ranks',ranks)
print('reduced_mod2_betti',betti)
