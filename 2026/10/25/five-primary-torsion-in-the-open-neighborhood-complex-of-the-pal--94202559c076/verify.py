#!/usr/bin/env python3
"""Exact finite chain and discrete-Morse calculation for N(Paley(25))."""
import hashlib
import heapq
import json
from collections import Counter, deque
from functools import lru_cache
from pathlib import Path
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

VERTEX_ORDER = [24,10,13,6,11,1,17,5,23,14,22,16,20,19,8,21,0,18,2,4,15,12,3,9,7]
ROOT = Path(__file__).resolve().parent

def mul(x, y):
    return ((x[0]*y[0]+2*x[1]*y[1])%5, (x[0]*y[1]+x[1]*y[0])%5)

def oriented_facets(mask):
    bs=[]; m=mask
    while m:
        b=m&-m; bs.append(b);m-=b
    return [(mask^b,(-1)**i) for i,b in enumerate(bs)]

def rank2(columns):
    pivot={}
    for v in columns:
        while v:
            p=v.bit_length()-1
            if p not in pivot:
                pivot[p]=v;break
            v^=pivot[p]
    return len(pivot)

def rank_prime(columns,p):
    pivot={}
    for z in columns:
        v={r:c%p for r,c in z.items() if c%p}
        while v:
            j=max(v)
            if j not in pivot:
                a=pow(v[j],-1,p)
                pivot[j]={k:(c*a)%p for k,c in v.items()}
                break
            a=v[j]
            for k,c in pivot[j].items():
                d=(v.get(k,0)-a*c)%p
                if d:v[k]=d
                else:v.pop(k,None)
    return len(pivot)

def make_complex():
    field=[(a,b) for a in range(5) for b in range(5)]
    squares={mul(t,t) for t in field if t!=(0,0)}
    assert len(squares)==12 and (0,0) not in squares
    nb=[]
    for a,b in field:
        nbr=[j for j,(c,d) in enumerate(field) if ((c-a)%5,(d-b)%5) in squares]
        assert len(nbr)==12
        nb.append(nbr)
    for i in range(25):
        assert i not in nb[i]
        for j in range(25):
            assert (j in nb[i]) == (i in nb[j])
            if i!=j:
                assert len(set(nb[i])&set(nb[j])) == (5 if j in nb[i] else 6)
    masks={0}
    for ns in nb:
        for k in range(1,1<<12):
            masks.add(sum(1<<ns[i] for i in range(12) if (k>>i)&1))
    assert len(masks)==93351
    assert sorted(Counter(x.bit_count() for x in masks if x).items())==[(1,25),(2,300),(3,2200),(4,9475),(5,18750),(6,22950),(7,19800),(8,12375),(9,5500),(10,1650),(11,300),(12,25)]
    print('GRAPH 25 12 (25,12,5,6)')
    print('FACES',len(masks)-1)
    return masks

def free_collapses(faces):
    counts={f:0 for f in faces if f}
    for x in counts:
        for y,sgn in oriented_facets(x):
            if y:counts[y]+=1
    heap=[(x.bit_count(),x) for x in counts if counts[x]==1]
    heapq.heapify(heap)
    active=set(counts)
    pair_count=0
    while heap:
        _,x=heapq.heappop(heap)
        if x not in active or counts[x]!=1:continue
        matches=[x|(1<<i) for i in range(25) if not ((x>>i)&1) and x|(1<<i) in active]
        assert len(matches)==1
        y=matches[0]
        for q in (x,y):
            active.remove(q)
            for z,sgn in oriented_facets(q):
                if z in active:
                    counts[z]-=1
                    if counts[z]==1:heapq.heappush(heap,(z.bit_count(),z))
        pair_count+=1
    assert pair_count==43546
    assert len(active)==6258
    assert sorted(Counter(x.bit_count() for x in active).items())==[(1,25),(2,300),(3,1605),(4,2929),(5,1399)]
    print('FREE_COLLAPSE_PAIRS',pair_count)
    print('REMAINING_FACES',len(active))
    return active

def morse_match(active):
    remaining=set(active)
    pairs=[]
    for v in VERTEX_ORDER:
        bit=1<<v
        for x in sorted(remaining):
            if x&bit or x|bit not in remaining:continue
            y=x|bit
            remaining.remove(x);remaining.remove(y)
            pairs.append((x,y))
    assert len(pairs)==2967
    crit=Counter(x.bit_count() for x in remaining)
    assert crit=={1:1,4:262,5:61}
    matched=set(pairs)
    indeg={x:0 for x in active}
    edges={x:[] for x in active}
    covers=0
    for x in active:
        for y,sgn in oriented_facets(x):
            if y not in active:continue
            covers+=1
            if (y,x) in matched: a,b=y,x
            else:a,b=x,y
            indeg[b]+=1
            edges[a].append(b)
    ready=deque(x for x,d in indeg.items() if d==0)
    seen=0
    while ready:
        x=ready.popleft();seen+=1
        for y in edges[x]:
            indeg[y]-=1
            if indeg[y]==0:ready.append(y)
    assert seen==len(active)
    print('MORSE_MATCH_PAIRS',len(pairs))
    print('MORSE_COVER_INCIDENCES',covers)
    print('MORSE_CRITICAL_VECTOR',sorted(crit.items()))
    print('MATCHING_DAG_CHECK',seen)
    return remaining,pairs

def morse_boundary(critical,pairs):
    upper={x:y for x,y in pairs if x.bit_count()==4}
    down={y for x,y in pairs if y.bit_count()==4}
    c3=sorted(x for x in critical if x.bit_count()==4)
    c4=sorted(x for x in critical if x.bit_count()==5)
    @lru_cache(None)
    def proj(face):
        if face in critical:return {face:1}
        if face in down:return {}
        assert face in upper
        q=upper[face]
        incidence=dict(oriented_facets(q))
        p=incidence[face]
        out={}
        for g,sgn in oriented_facets(q):
            if g==face:continue
            for h,c in proj(g).items():
                out[h]=out.get(h,0)-p*sgn*c
        return {k:v for k,v in out.items() if v}
    row={f:i for i,f in enumerate(c3)}
    cols=[]
    for q in c4:
        out={}
        for g,sgn in oriented_facets(q):
            for h,c in proj(g).items():
                out[h]=out.get(h,0)+sgn*c
        cols.append({row[h]:v for h,v in out.items() if v})
    matrix=zeros(len(c3),len(c4))
    for j,col in enumerate(cols):
        for i,v in col.items():matrix[i,j]=v
    assert max(abs(v) for col in cols for v in col.values())==2
    diag=smith_normal_form(matrix,domain=ZZ)
    factors=[abs(int(diag[i,i])) for i in range(min(diag.shape)) if diag[i,i]!=0]
    assert Counter(factors)=={1:56,5:1}
    assert len(factors)==57
    assert rank_prime(cols,5)==56
    assert rank_prime(cols,2)==57
    canonical={'critical_3_masks':c3,'critical_4_masks':c4,
               'columns':[[[i,col[i]] for i in sorted(col)] for col in cols]}
    raw=(json.dumps(canonical,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode('utf8')
    target=ROOT/'morse_matrix.json'
    if not target.exists():
        target.write_bytes(raw)
    assert target.read_bytes()==raw
    print('MORSE_MATRIX_SHA256',hashlib.sha256(raw).hexdigest())
    print('MORSE_MATRIX',matrix.shape,'NONZERO',sum(len(c) for c in cols))
    print('SMITH_INVARIANTS',dict(Counter(factors)))
    return matrix

def direct_ranks(active):
    for deg in [2,3,4,5]:
        hi=sorted(x for x in active if x.bit_count()==deg)
        lo=sorted(x for x in active if x.bit_count()==deg-1)
        ids={f:i for i,f in enumerate(lo)}
        boundary_cols=[{ids[t]:c for t,c in oriented_facets(x)} for x in hi]
        bitcols=[sum(1<<i for i in col) for col in boundary_cols]
        r2=rank2(bitcols)
        r5=rank_prime(boundary_cols,5)
        assert ((r2,r5)==({2:(24,24),3:(276,276),4:(1329,1329),5:(1395,1394)}[deg]))
        print('DIRECT_BOUNDARY_RANKS',deg-1,'MOD2',r2,'MOD5',r5)

if __name__=='__main__':
    faces=make_complex()
    active=free_collapses(faces)
    critical,pairs=morse_match(active)
    morse_boundary(critical,pairs)
    direct_ranks(active)
    print('INTEGRAL_HOMOLOGY_H3_Z205_PLUS_Z5_H4_Z4')
    print('VERIFY_OK_PALEY25_NEIGHBORHOOD_FIVE_TORSION')
