#!/usr/bin/env python3
"""Exact integer certificates for distance-neighbour tomography on Hamming graphs.
Usage: python3 verify.py  (reads kernel_basis.json in same directory).
Requires Python standard library only.
"""
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
import json

Q=4; P=1000003

def partitions(r):
    out=[]
    def rec(p):
        if len(p)==r:
            out.append(tuple(p)); return
        for b in range(max(p)+2 if p else 1):
            rec(p+[b])
    rec([]); return out

def types(r):
    return [(p,s) for p in partitions(r) if (k:=max(p)+1)<=Q
            for s in range(k+(k<Q))]

def displacement_counts(pi,status):
    counts=Counter()
    for new in range(Q):
        if new==status: continue
        delta=tuple(int(new!=pi[j])-int(status!=pi[j]) for j in range(len(pi)))
        counts[delta]+=1
    return counts

def make_matrix(r):
    ts=types(r)
    ps=[pi for pi in partitions(r) if max(pi)+1<=Q]
    ds=list(product((-1,0,1),repeat=r))
    cs=[displacement_counts(pi,status) for pi,status in ts]
    rows=[[cc.get(d,0) for cc in cs] for d in ds]
    rows.extend([[int(pi==pj) for pi,_ in ts] for pj in ps])
    rows.extend([[int(status!=pi[j]) for pi,status in ts] for j in range(r)])
    return ts,rows

def rank_mod(matrix,p=P):
    a=[[v%p for v in row] for row in matrix]
    if not a:return 0
    h=len(a);w=len(a[0]); row=0
    for col in range(w):
        pivot=next((i for i in range(row,h) if a[i][col]),None)
        if pivot is None:continue
        a[row],a[pivot]=a[pivot],a[row]
        inv=pow(a[row][col],-1,p)
        a[row]=[(v*inv)%p for v in a[row]]
        pivotrow=a[row]
        for i in range(row+1,h):
            coeff=a[i][col]
            if coeff:
                a[i][col]=0
                for j in range(col+1,w):
                    a[i][j]=(a[i][j]-coeff*pivotrow[j])%p
        row+=1
        if row==h:break
    return row

def distance(u,v):return sum(a!=b for a,b in zip(u,v))

def distances_to(u,anchors):return tuple(distance(u,a) for a in anchors)

def neighbor_displacements(u,anchors):
    base=distances_to(u,anchors); out=Counter()
    for j in range(len(u)):
        for a in range(Q):
            if a!=u[j]:
                v=u[:j]+(a,)+u[j+1:]
                ds=distances_to(v,anchors)
                out[tuple(ds[i]-base[i] for i in range(len(base)))]+=1
    return out

def main():
    ranks=[]
    for r in range(1,6):
        ts,M=make_matrix(r)
        rk=rank_mod(M)
        ranks.append((r,len(ts),rk,len(M)))
    assert [(r,cols,rk) for r,cols,rk,_ in ranks]==[(1,2,2),(2,5,5),(3,15,15),(4,51,51),(5,187,182)]
    ts,M=make_matrix(5)
    index={t:i for i,t in enumerate(ts)}
    kernel=json.loads((Path(__file__).parent/'kernel_basis.json').read_text())
    assert kernel['q']==4 and kernel['r']==5 and len(kernel['basis'])==5
    vecs=[]
    for sparse in kernel['basis']:
        v=[0]*len(ts)
        for pi,s,c in sparse:
            assert c in (-1,1)
            idx=index[(tuple(pi),s)];assert v[idx]==0
            v[idx]=c
        assert any(v)
        assert all(sum(row[i]*v[i] for i in range(len(ts)))==0 for row in M)
        vecs.append(v)
    assert rank_mod(vecs)==5
    # A 12-coordinate collision is obtained from the first kernel vector.
    signed=defaultdict(dict)
    for pi,s,c in kernel['basis'][0]:
        assert c not in signed[tuple(pi)]
        signed[tuple(pi)][c]=s
    assert len(signed)==12 and all(set(z)=={-1,1} for z in signed.values())
    coords=sorted(signed)
    anchors=tuple(tuple(pi[j] for pi in coords) for j in range(5))
    x=tuple(signed[pi][1] for pi in coords)
    y=tuple(signed[pi][-1] for pi in coords)
    assert len(set(anchors))==5 and x!=y
    assert distances_to(x,anchors)==distances_to(y,anchors)
    assert neighbor_displacements(x,anchors)==neighbor_displacements(y,anchors)
    # Different coordinate-type profiles: no anchor-pointwise automorphism sends x to y.
    px=Counter((pi,x[i]) for i,pi in enumerate(coords))
    py=Counter((pi,y[i]) for i,pi in enumerate(coords))
    assert px!=py
    print('RANKS',ranks)
    print('FIVE_KERNEL_VECTORS_VERIFIED',len(vecs),'INDEPENDENT',rank_mod(vecs))
    print('WITNESS_DIMENSION',len(coords),'DISTANCES',distances_to(x,anchors))
    print('WITNESS_NEIGHBOR_COUNTS',sum(neighbor_displacements(x,anchors).values()),
          'DISTINCT_DISPLACEMENTS',len(neighbor_displacements(x,anchors)))
    print('WITNESS_MARKERS',anchors)
    print('WITNESS_X',x)
    print('WITNESS_Y',y)
    print('ALL_TESTS_PASS')
if __name__=='__main__':main()
