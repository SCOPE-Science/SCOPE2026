"""Finite weak-order modal-generator theorem: independent finite checks.

Standard-library Python 3.10+; run: python3 verify.py
"""
from itertools import product
from math import prod
from random import Random


def falling(q, n):
    v = 1
    for j in range(n):
        v *= q-j
    return max(0, v)


def predicted(sizes, colors):
    i = 0
    level_colors = []
    for n in sizes:
        subset = tuple(colors[i:i+n]); i += n
        level_colors.append(subset)
        if len(set(subset)) != n:
            return False
    return all(
        (sizes[i+1] != 1 or level_colors[i+1][0] not in level_colors[i])
        for i in range(len(sizes)-1)
    )


def census(sizes, q):
    t = falling(q, sizes[-1])
    for i in range(len(sizes)-1):
        t *= falling(q - (sizes[i+1] == 1), sizes[i])
    return t


def accessibility(sizes):
    levels = tuple(i for i,n in enumerate(sizes) for _ in range(n))
    return tuple(tuple(v for v in range(len(levels))
        if v == u or levels[v] > levels[u]) for u in range(len(levels)))


def modal_refinement(rel, colors):
    # Distinct operation: fixed-point partition by color and successor-class supports.
    n = len(colors)
    labels = tuple(colors)
    partitions = []
    while True:
        uniq = {x:i for i,x in enumerate(sorted(set(labels)))}
        labels = tuple(uniq[x] for x in labels)
        partitions.append(labels)
        sig = [(colors[u],frozenset(labels[v] for v in rel[u])) for u in range(n)]
        uniq = {x:i for i,x in enumerate(sorted(set(sig),key=repr))}
        refined = tuple(uniq[x] for x in sig)
        if all((labels[u] == labels[v]) == (refined[u] == refined[v])
               for u in range(n) for v in range(n)):
            return len(set(labels)) == n, len(partitions)-1, partitions
        labels = refined


def independent_boolean_closure(rel, colors, q):
    # Directly close actual subsets of W under complement, union and modal preimage.
    n=len(colors); universe=(1<<n)-1
    masks={0,universe}
    for a in range(q):
        masks.add(sum((1<<u) for u,v in enumerate(colors) if v==a))
    while True:
        old=len(masks)
        snap=tuple(masks)
        for x in snap:
            masks.add(universe^x)
            masks.add(sum(1<<u for u,succ in enumerate(rel) if any((x>>v)&1 for v in succ)))
        snap=tuple(masks)
        for x in snap:
            for y in snap:
                masks.add(x|y)
        if len(masks)==old:
            return len(masks)==1<<n

checks=0; counts=0; closures=0; maxdepth=0
for h in range(1,6):
    for sizes in product(range(1,4),repeat=h):
        n=sum(sizes)
        if n>8: continue
        rel=accessibility(sizes)
        for q in (1,2,3,4):
            if q**n > 22000: continue
            observed=0
            for colors in product(range(q),repeat=n):
                p=predicted(sizes,colors)
                m, depth, _=modal_refinement(rel,colors)
                assert p==m,(sizes,q,colors,p,m)
                if m:
                    observed+=1
                    assert depth <= h-1,(sizes,q,colors,depth)
                    maxdepth=max(depth,maxdepth)
                checks+=1
                if n<=5 and checks%31==0:
                    assert independent_boolean_closure(rel,colors,q)==m,(sizes,colors)
                    closures+=1
            assert observed==census(sizes,q),(sizes,q,observed,census(sizes,q))
            counts+=1

rng=Random(112358)
randoms=0
for _ in range(5000):
    h=rng.randint(1,12)
    sizes=tuple(rng.randint(1,5) for _ in range(h))
    q=rng.randint(1,6)
    colors=tuple(rng.randrange(q) for _ in range(sum(sizes)))
    rel=accessibility(sizes)
    p=predicted(sizes,colors)
    m,depth,_=modal_refinement(rel,colors)
    assert p==m,(sizes,q,colors,p,m)
    if m:assert depth<=h-1
    randoms+=1

sharp=0
for h in range(2,16):
    sizes=(2,)*h
    colors=tuple(j for _ in sizes for j in (0,1))
    m,depth,_=modal_refinement(accessibility(sizes),colors)
    assert m and depth==h-1,(h,m,depth)
    sharp+=1

examples={
 'two_by_two':census((2,2),2),
 'two_one_one_q3':census((2,1,1),3),
 'two_one_one_q2':census((2,1,1),2),
}
assert examples=={'two_by_two':4,'two_one_one_q3':12,'two_one_one_q2':0}
print('VERIFY_OK exhaustive_labelings',checks,'parameter_censuses',counts,
      'direct_boolean_closures',closures,'random_cases',randoms,
      'sharp_depth_heights',sharp,'max_exhaustive_depth',maxdepth,'examples',examples)
