#!/usr/bin/env python3
"""Check four-pebble collinearity extension supports in small projective spaces.

For each assignment of three stationary pebbles, enumerate the complete
atomic patterns possible for the fourth pebble. All arithmetic is exact.
This is finite corroboration; the general theorem requires the proof.
"""
from itertools import product

def field(q):
    assert q in (2,3,4,5)
    if q != 4:
        return (lambda a,b:(a+b)%q), (lambda a,b:(a*b)%q), (lambda a:pow(a,q-2,q))
    def mul(a,b):
        c = 0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1: c ^= 1<<(i+j)
        if c & 4: c ^= 7   # t^2=t+1 over GF(2)
        return c
    def inv(a):
        assert a
        return mul(a,a)
    return lambda a,b:a^b, mul, inv

def space(q,dim):
    add,mul,inv=field(q)
    neg=lambda a: next(x for x in range(q) if add(a,x)==0)
    pts=set()
    for v in product(range(q),repeat=dim+1):
        if all(t==0 for t in v): continue
        first=next(x for x in v if x)
        pts.add(tuple(mul(t,inv(first)) for t in v))
    pts=sorted(pts)
    def rank(rows):
        a=[list(r) for r in rows]; h=0; w=dim+1
        for j in range(w):
            k=next((k for k in range(h,len(a)) if a[k][j]),None)
            if k is None: continue
            a[h],a[k]=a[k],a[h]
            z=inv(a[h][j]); a[h]=[mul(z,x) for x in a[h]]
            for i in range(len(a)):
                if i!=h and a[i][j]:
                    z=a[i][j]
                    a[i]=[add(x,neg(mul(z,y))) for x,y in zip(a[i],a[h])]
            h+=1
            if h==len(a): break
        return h
    n=len(pts)
    lines=[[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                lines[i][j]=(1<<n)-1
            elif lines[j][i] is not None:
                lines[i][j]=lines[j][i]
            else:
                lines[i][j]=sum(1<<k for k,p in enumerate(pts) if rank([pts[i],pts[j],p])<=2)
    return n, lines

def profiles(q,dim):
    n,L=space(q,dim)
    COL=lambda a,b,c: bool(L[a][b] & (1<<c))
    sup={}; class_sizes={}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                key=(a==b,a==c,b==c,COL(a,b,c))
                patterns=set()
                for z in range(n):
                    patterns.add((z==a,z==b,z==c,COL(a,b,z),COL(a,c,z),COL(b,c,z)))
                patterns=frozenset(patterns)
                if key in sup and sup[key]!=patterns:
                    raise AssertionError(('nonuniform support',q,dim,key,(a,b,c)))
                sup[key]=patterns
                class_sizes[key]=class_sizes.get(key,0)+1
    return n,sup,class_sizes

def main():
    records=[]
    tests=[(2,1),(3,1),(4,1),(5,1),(2,2),(2,3),(3,2),(3,3),(4,2),(5,2)]
    for q,d in tests:
        n,sup,sizes=profiles(q,d)
        key=('line' if d==1 else 'plane+', 'binary' if q==2 else 'nonbinary')
        records.append((q,d,n,key,sup,sizes))
        print(f'CHECK q={q} dimension={d} points={n} triple_types={len(sup)} assignments={n**3} PASS')
    templates={}
    for q,d,n,key,sup,_ in records:
        if key in templates: assert templates[key]==sup,(key,q,d)
        else: templates[key]=sup
    assert len(templates)==4
    sigs={k:tuple(sorted((str(a),str(sorted(p))) for a,p in v.items())) for k,v in templates.items()}
    assert len(set(sigs.values()))==4
    for k,v in sorted(templates.items()):
        print(f'TEMPLATE {k} triple_types={len(v)} supports={sum(len(p) for p in v.values())}')
    a=dict((k,s) for q,d,n,k,s,_ in records if (q,d) in ((2,2),(3,2)))
    assert sigs[('plane+','binary')]!=sigs[('plane+','nonbinary')]
    print('FO4_FOUR_CLASSES_EXACT_SMALL_INSTANCES PASS')
    print('GENERAL_INFINITE_CASE_REQUIRES_GEOMETRIC_EXTENSION_PROOF')

if __name__=='__main__': main()
