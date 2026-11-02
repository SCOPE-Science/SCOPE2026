#!/usr/bin/env python3
"""Direct one-point extension profiles of finite partial geometries.
Run with Python 3.9+. No third-party packages required.
"""
from collections import defaultdict
import hashlib, json

def geom(points,lines,name):
    P=list(points); L=[frozenset(x) for x in lines]
    assert len(L)==len(set(L))
    adj=[set() for _ in P]
    bypoint={p:i for i,p in enumerate(P)}
    for B in L:
        assert B<=set(P)
        for x in B:
            for y in B:
                if x!=y:adj[bypoint[x]].add(bypoint[y])
    t=(len(P[0]) if False else None)
    degs={sum(p in B for B in L) for p in P}
    sizes={len(B) for B in L}
    assert len(degs)==len(sizes)==1 and min(degs)>=3 and min(sizes)>=3,(name,degs,sizes)
    s=next(iter(sizes))-1;t=next(iter(degs))-1
    intersect={(i,j): bool(L[i]&L[j]) for i in range(len(L)) for j in range(len(L)) if i!=j}
    for i in range(len(P)):
        for j in range(i+1,len(P)):
            assert sum(P[i] in B and P[j] in B for B in L)<=1
    alphas=set()
    for p in P:
        for B in L:
            if p not in B:
                alphas.add(sum(q in B for q in (P[k] for k in adj[bypoint[p]])))
    assert len(alphas)==1 and next(iter(alphas))>0,(name,alphas)
    a=next(iter(alphas))
    assert 1<=a<=min(s+1,t+1)
    return dict(name=name,P=P,L=L,s=s,t=t,a=a,adj=adj,intersect=intersect)

def dual(g):
    return geom(range(len(g['L'])), [frozenset(i for i,B in enumerate(g['L']) if p in B) for p in g['P']], 'dual_'+g['name'])

def fano():
    return geom(range(1,8),{frozenset([x,y,x^y]) for x in range(1,8) for y in range(x+1,8)}, 'fano')

def sts15():
    return geom(range(1,16),{frozenset([x,y,x^y]) for x in range(1,16) for y in range(x+1,16)}, 'sts15')

def affine3():
    P=list(range(9));pt=lambda x,y:3*x+y
    L=[{pt(x,y) for x in range(3) for y in range(3) if x==b} for b in range(3)]
    L += [{pt(x,y) for x in range(3) for y in range(3) if (y-m*x-b)%3==0} for m in range(3) for b in range(3)]
    return geom(P,L,'affine3')

def net3():
    P=list(range(9));pt=lambda x,y:3*x+y
    L=[{pt(x,y) for x in range(3) for y in range(3) if x==b} for b in range(3)]
    L += [{pt(x,y) for x in range(3) for y in range(3) if (y-m*x-b)%3==0} for m in range(2) for b in range(3)]
    return geom(P,L,'net3')

def td34():
    P=[(g,v) for g in range(3) for v in range(4)]
    L=[{(0,i),(1,j),(2,(i+j)%4)} for i in range(4) for j in range(4)]
    return geom(P,L,'td34')

def gq22():
    symp=lambda x,y: (((x>>0)&1)*((y>>2)&1)+((x>>1)&1)*((y>>3)&1)+((x>>2)&1)*((y>>0)&1)+((x>>3)&1)*((y>>1)&1))%2
    L={frozenset([x,y,x^y]) for x in range(1,16) for y in range(x+1,16) if symp(x,y)==0}
    return geom(range(1,16),L,'w32')

def profile(g):
    P=g['P'];L=g['L']; np=len(P);nl=len(L);B=[{i for i,p in enumerate(P) if p in line} for line in L]
    lineof=[{j for j,line in enumerate(B) if i in line} for i in range(np)]
    def relation(x,y):
        typx='P' if x<np else 'L';typy='P' if y<np else 'L'
        if x==y:return typx+'E'
        if typx==typy=='P':return 'PC' if lineof[x]&lineof[y] else 'PN'
        if typx==typy=='L':return 'LM' if B[x-np]&B[y-np] else 'LN'
        if typx=='P':return 'PI' if x in B[y-np] else 'PO'
        return 'LI' if y in B[x-np] else 'LO'
    types=defaultdict(set); individual=defaultdict(set)
    for x in range(np+nl):
        for y in range(np+nl):
            T=relation(x,y)
            S=frozenset((relation(x,z),relation(y,z)) for z in range(np+nl))
            types[T].add(S)
            individual[T].add((x,y))
    assert all(len(x)==1 for x in types.values()),(g['name'], {k:len(v) for k,v in types.items()})
    compact={k:sorted(list(next(iter(v)))) for k,v in types.items()}
    return compact, {k:len(v) for k,v in individual.items()}

def main():
    orig=[gq22(),net3(),td34(),affine3(),sts15(),fano()]
    allg=orig+[dual(x) for x in (td34(),affine3(),sts15())]
    assert len(allg)==9
    buckets=defaultdict(list)
    for g in allg:
        s,t,a=g['s'],g['t'],g['a']
        category=lambda r: '2' if a==r+1 else ('1' if a==r else '0')
        key=category(s)+category(t)
        p,stats=profile(g)
        buckets[key].append((g['name'],p))
        print(f"{g['name']:14s} | s={s:2d},t={t:2d},alpha={a:2d} | point={len(g['P']):2d},line={len(g['L']):2d} | class={key} | pair_classes={len(p)} | aggregate_extension_types={sum(map(len,p.values()))}")
    assert len(buckets)==9, buckets.keys()
    for key,arr in sorted(buckets.items()):
        assert all(p==arr[0][1] for _,p in arr)
    print('NINE_SUPPORT_CLASSES',sorted(buckets))
    print('ALL_NINE_NONIDENTICAL',len({json.dumps(arr[0][1],sort_keys=True) for arr in buckets.values()})==9)
    print('PASS')
if __name__=='__main__':main()
