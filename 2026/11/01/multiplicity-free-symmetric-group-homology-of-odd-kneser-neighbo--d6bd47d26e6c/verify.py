#!/usr/bin/env python3
"""Reproduce finite checks for odd Kneser neighborhood symmetry theorem.
Only mathematics and reproducibility; not an infinite-case certificate.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict, deque
from math import comb, factorial
from fractions import Fraction

def partitions(n, min_part=1):
    if n==0:
        yield ()
    else:
        for t in range(min_part,n+1):
            for x in partitions(n-t,t):
                yield (t,)+x

def z(mu):
    out=1
    for a,count in Counter(mu).items():
        out*=a**count*factorial(count)
    return out

def h(degree):
    if degree<0:return {}
    return {():Fraction(1)} if degree==0 else {p:Fraction(1,z(p)) for p in partitions(degree)}

def poly_product(a,b):
    o=defaultdict(Fraction)
    for p,ap in a.items():
        for q,bq in b.items():o[tuple(sorted(p+q))]+=ap*bq
    return dict(o)

def sign(perm):
    return (-1)**sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))

def schur_character(shape,cycle):
    l=len(shape);acc=Fraction(0)
    for perm in permutations(range(l)):
        p={():Fraction(1)}
        for i,j in enumerate(perm):p=poly_product(p,h(shape[i]-i+j))
        acc+=sign(perm)*p.get(tuple(sorted(cycle)),0)
    return acc*z(cycle)

def perm_cycles(p):
    seen=set(); lengths=[]
    for start in range(len(p)):
        if start in seen:continue
        u=start;t=0
        while u not in seen:
            seen.add(u);t+=1;u=p[u]
        lengths.append(t)
    return tuple(sorted(lengths))

def fixsets(subsets,p):
    return sum(tuple(sorted(p[x] for x in a))==a for a in subsets)

def test(k):
    n=2*k+1
    lower=list(combinations(range(n),k))
    upper=list(combinations(range(n),k+1))
    inc=[(a,b) for a in lower for b in upper if set(a)<set(b)]
    assert len(lower)==len(upper)==comb(n,k)
    assert len(inc)==(k+1)*comb(n,k)
    graph={('L',a):set() for a in lower}
    graph.update({('U',b):set() for b in upper})
    for a,b in inc:
        graph['L',a].add(('U',b));graph['U',b].add(('L',a))
    seen={('L',lower[0])}; queue=deque(seen)
    while queue:
        for v in graph[queue.popleft()]:
            if v not in seen:seen.add(v);queue.append(v)
    assert len(seen)==len(lower)+len(upper)
    rank=len(inc)-len(graph)+1
    assert rank==(k-1)*comb(n,k)+1
    facets=[set(combinations(b,k)) for b in upper]
    assert all(len(f & g)<=1 for i,f in enumerate(facets) for g in facets[i+1:])
    dims=[]
    for i in range(1,k+2):
        faces=set()
        for f in facets:
            faces.update(combinations(sorted(f),i))
        dims.append(len(faces))
    assert sum((-1)**i*size for i,size in enumerate(dims))==1-rank
    shapes=[(2*k-i,i,1) for i in range(1,k+1)]
    def hookdim(sh):
        hprod=1
        for row,sz in enumerate(sh):
            for col in range(sz):hprod*=sz-col+sum(v>col for v in sh[row+1:])
        return factorial(n)//hprod
    dimensions=[hookdim(s) for s in shapes]
    assert sum(dimensions)==rank
    if k<=3:
        reps={}
        checks=0
        for p in permutations(range(n)):
            cy=perm_cycles(p)
            trace=fixsets(inc,p) if False else sum(tuple(sorted(p[x] for x in a))==a and tuple(sorted(p[x] for x in b))==b for a,b in inc)
            trace-=2*fixsets(lower,p)
            trace+=1
            if cy not in reps:
                specht=sum(schur_character(sh,cy) for sh in shapes)
                assert specht.denominator==1
                reps[cy]=int(specht)
            assert trace==reps[cy],(k,cy,trace,reps[cy])
            checks+=1
        print('k=',k,'n=',n,'fvector=',tuple(dims),'H1rank=',rank,'shapes=',shapes,'dims=',dimensions,'permutations_tested=',checks,'cycle_types=',len(reps))
    else:
        print('k=',k,'n=',n,'fvector=',tuple(dims),'H1rank=',rank,'shapes=',shapes,'dims=',dimensions,'permutations_tested=0')

if __name__=='__main__':
    for k in (2,3,4):test(k)
    # Continuous, equivariant retraction on a simplex: tests on the center and branches.
    for m in range(3,7):
        bary=[Fraction(1,m)]*m
        for j in range(m):
            for s in [Fraction(0),Fraction(1,7),Fraction(3,5),Fraction(1)]:
                t=[(1-s)*u+(s if i==j else 0) for i,u in enumerate(bary)]
                a=sorted(t,reverse=True)
                gap=a[0]-a[1]
                if not gap:r=bary
                else:
                    imax=t.index(a[0]);r=[(1-gap)*u+(gap if i==imax else 0) for i,u in enumerate(bary)]
                assert t==r
    print('VERIFY_OK')
