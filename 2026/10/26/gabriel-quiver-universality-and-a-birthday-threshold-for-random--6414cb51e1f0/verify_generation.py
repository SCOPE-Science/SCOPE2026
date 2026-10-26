#!/usr/bin/env python3
"""Independent finite-field checks of generation probabilities for bound path algebras."""
from collections import Counter
from itertools import product
from fractions import Fraction


def rank_prime(vectors, p, dimension):
    pivots = {}
    for vector in vectors:
        row = [v % p for v in vector]
        for lead in sorted(pivots):
            if row[lead]:
                a = row[lead]
                row = [(z-a*w) % p for z,w in zip(row,pivots[lead])]
        for k,v in enumerate(row):
            if v:
                inv = pow(v,-1,p)
                pivots[k] = [(inv*z)%p for z in row]
                break
    return tuple(pivots[k] for k in sorted(pivots))


def basis_paths(vertices, edges, max_length):
    out = [(i,()) for i in range(vertices)]
    level=out[:]
    for _ in range(1,max_length):
        next_level=[]
        for src,seq in level:
            end=src
            for e in seq:end=edges[e][1]
            for idx,(a,b) in enumerate(edges):
                if a==end:next_level.append((src,seq+(idx,)))
        out.extend(next_level)
        level=next_level
    return out


def algebra(vertices, edges, max_length):
    paths=basis_paths(vertices, edges, max_length)
    index={path:i for i,path in enumerate(paths)}
    d=len(paths)
    mul=[[None]*d for _ in range(d)]
    for i,(s,word) in enumerate(paths):
        end=s
        for e in word:end=edges[e][1]
        for j,(t,w) in enumerate(paths):
            if end==t and len(word)+len(w)<max_length:
                mul[i][j]=index[(s,word+w)]
    one=tuple(1 if not word else 0 for _,word in paths)
    return d,mul,one


def times(a,b,p,mul):
    d=len(a)
    o=[0]*d
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                k=mul[i][j]
                if y and k is not None:
                    o[k]=(o[k]+x*y)%p
    return tuple(o)


def generates(xs,p,mul,one):
    d=len(one)
    span=rank_prime([one]+list(xs),p,d)
    while True:
        products=[times(a,b,p,mul) for a in span for b in span]
        larger=rank_prime(list(span)+products,p,d)
        if len(larger)==len(span):
            return len(span)==d
        span=larger


def formula(p,vertices,edges,r):
    groups=Counter(edges)
    diagonal=Fraction(1)
    for i in range(vertices):diagonal*=Fraction(p**r-i,p**r)
    ans=diagonal
    for (i,j),m in groups.items():
        usable=r-(1 if i!=j else 0)
        if m>usable:return Fraction(0)
        for h in range(m):ans*=1-Fraction(p**h,p**usable)
    return ans


def check(p,vertices,edges,length,r):
    d,mul,one=algebra(vertices,edges,length)
    assert p**(d*r)<=20000
    elems=list(product(range(p),repeat=d))
    count=sum(generates(xs,p,mul,one) for xs in product(elems,repeat=r))
    ratio=Fraction(count,p**(d*r))
    theoretical=formula(p,vertices,edges,r)
    print('p=%d vertices=%d edges=%s Loewy-length=%d samples=%d exact=%s formula=%s' %
           (p,vertices,str(edges),length,p**(d*r),ratio,theoretical))
    assert ratio==theoretical


def main():
    checks=[
       (2,1,[],2,0),
       (2,1,[(0,0)],2,1),
       (2,1,[(0,0)],3,1),
       (2,1,[(0,0),(0,0)],2,2),
       (2,2,[(0,1)],2,2),
       (2,2,[(0,1)],2,3),
       (2,2,[(0,1),(0,1)],2,2),
       (2,2,[(0,1),(0,1)],2,3),
       (2,2,[(0,0),(0,1)],2,2),
       (2,3,[(0,1),(1,2)],2,2),
       (2,3,[(0,1),(1,2)],3,2),
       (2,3,[(0,1),(0,2)],3,2),
       (3,2,[(0,1)],2,2)
    ]
    for x in checks:check(*x)
    print('All %d exact independently enumerated cases passed.'%len(checks))

if __name__=='__main__':main()
