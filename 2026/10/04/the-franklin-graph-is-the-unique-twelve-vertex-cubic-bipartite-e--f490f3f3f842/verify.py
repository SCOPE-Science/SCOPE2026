#!/usr/bin/env python3
from itertools import combinations, permutations

M=6
ROWMASKS=[sum(1<<j for j in c) for c in combinations(range(M),3)]

def transpose(rows):
    return tuple(sum(((rows[i]>>j)&1)<<i for i in range(M)) for j in range(M))

def normalize_cols(rows):
    # column permutation acts by permuting the 6 column bitstrings; sorting them is canonical for fixed row order
    cols=[]
    for j in range(M):
        bits=0
        for i,r in enumerate(rows): bits |= ((r>>j)&1)<<i
        cols.append(bits)
    cols=sorted(cols)
    out=[]
    for i in range(M):
        mask=0
        for j,c in enumerate(cols): mask |= ((c>>i)&1)<<j
        out.append(mask)
    return tuple(out)

def canonical_side(rows):
    best=None
    for p in permutations(range(M)):
        cand=normalize_cols(tuple(rows[i] for i in p))
        if best is None or cand<best: best=cand
    return best

def canonical(rows):
    a=canonical_side(tuple(rows))
    b=canonical_side(transpose(tuple(rows)))
    return min(a,b)

def connected(rows):
    adj=[set() for _ in range(2*M)]
    for i,r in enumerate(rows):
        for j in range(M):
            if r>>j&1:
                adj[i].add(M+j); adj[M+j].add(i)
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v in adj[u]-seen:
            seen.add(v); stack.append(v)
    return len(seen)==2*M

def edges(rows):
    return [(i,M+j) for i,r in enumerate(rows) for j in range(M) if r>>j&1]

def dominates(rows, matching):
    adj=[set() for _ in range(2*M)]
    for u,v in edges(rows): adj[u].add(v); adj[v].add(u)
    D={x for e in matching for x in e}
    return all(v in D or bool(adj[v]&D) for v in range(2*M))

def min_dom_matching(rows):
    es=edges(rows)
    for k in (1,2,3,4,5,6):
        for esub in combinations(es,k):
            flat=[v for e in esub for v in e]
            if len(set(flat))<2*k: continue
            if dominates(rows,esub): return k,esub
    raise AssertionError

def lcf_franklin_rows():
    # [5,-5]^6: Hamilton cycle plus one chord per vertex, duplicate-safe
    adj=[set() for _ in range(12)]
    for i in range(12):
        j=(i+1)%12; adj[i].add(j); adj[j].add(i)
    offs=[5,-5]*6
    for i,o in enumerate(offs):
        j=(i+o)%12; adj[i].add(j); adj[j].add(i)
    # 2-color and convert to 6x6 incidence rows
    color={0:0}; st=[0]
    while st:
        u=st.pop()
        for v in adj[u]:
            if v not in color: color[v]=1-color[u]; st.append(v)
            elif color[v]==color[u]: raise AssertionError('LCF not bipartite')
    A=sorted([v for v,c in color.items() if c==0]); B=sorted([v for v,c in color.items() if c==1])
    bi={v:i for i,v in enumerate(B)}
    rows=[]
    for u in A:
        rows.append(sum(1<<bi[v] for v in adj[u]))
    return tuple(rows)

classes={}
raw=0
rows=[]
def rec(i,start,cols):
    global raw
    if i==M:
        if cols!=[3]*M:return
        raw+=1
        rs=tuple(rows)
        if not connected(rs):return
        can=canonical(rs)
        classes.setdefault(can,0); classes[can]+=1
        return
    rem=M-i-1
    for t in range(start,len(ROWMASKS)):
        r=ROWMASKS[t]; nc=cols[:]; ok=True
        for j in range(M):
            if r>>j&1:
                nc[j]+=1
                if nc[j]>3: ok=False; break
        if not ok: continue
        if any(c+rem<3 for c in nc): continue
        rows.append(r); rec(i+1,t,nc); rows.pop()
rec(0,0,[0]*M)

assert len(classes)==5, len(classes)
frank=canonical(lcf_franklin_rows())
assert frank in classes
records=[]
for can in sorted(classes):
    k,w=min_dom_matching(can)
    records.append((can,2*k,w,can==frank,classes[can]))

# exact cubic-bipartite lower bound for size 2: endpoints of one edge dominate at most 6 vertices, so gamma_pr !=2 at n=12.
assert all(g in (4,6) for _,g,_,_,_ in records)
assert [g for _,g,_,_,_ in records].count(6)==1
assert next(r for r in records if r[3])[1]==6

print('ALL CHECKS PASSED')
print('sorted_row_multisets_examined=',raw)
print('connected_isomorphism_classes=',len(records))
for idx,(can,g,w,isf,mult) in enumerate(records,1):
    print('class',idx,'rows='+','.join(f'{r:06b}' for r in can),'gamma_pr='+str(g),'franklin='+str(isf).lower(),'semilabeled_multiplicity='+str(mult),'witness='+str(w))
