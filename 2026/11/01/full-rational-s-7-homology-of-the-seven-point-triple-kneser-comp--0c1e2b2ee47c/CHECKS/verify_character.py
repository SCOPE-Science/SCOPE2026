"""Exact character computation for Ind(KG(7,3)), using only Python's standard library.

No homology is computed here: a Lefschetz orbit formula plus the published
rational Betti ranks determines the two rational homology characters.
"""
from functools import lru_cache
from itertools import combinations
from collections import Counter
from math import factorial


def partitions(n, low=1):
    if not n:
        yield ()
    else:
        for a in range(low, n + 1):
            for tail in partitions(n-a, a):
                yield (a,) + tail


def orbit_graph(parts):
    n = sum(parts)
    assert n == 7
    p = list(range(n)); start = 0
    for length in parts:
        for j in range(length):
            p[start+j] = start+(j+1)%length
        start += length
    triples = [sum(1<<i for i in x) for x in combinations(range(7),3)]
    seen = set(); orbits = []
    for x in triples:
        if x in seen:
            continue
        orbit=[]; y=x
        while y not in seen:
            seen.add(y); orbit.append(y)
            y=sum(1<<p[i] for i in range(7) if (y>>i)&1)
        if all(a&b for a,b in combinations(orbit,2)):
            orbits.append(orbit)
    m=len(orbits); conflict=[0]*m
    for i in range(m):
        for j in range(i+1,m):
            if any(not(a&b) for a in orbits[i] for b in orbits[j]):
                conflict[i]|=1<<j; conflict[j]|=1<<i
    return conflict


def lefschetz(parts):
    conflict = orbit_graph(parts)
    @lru_cache(None)
    def independence_at_minus_one(mask):
        if mask == 0:
            return 1
        candidate = max((v for v in range(len(conflict)) if mask>>v&1),
                        key=lambda v: (conflict[v]&mask).bit_count())
        vbit = 1<<candidate
        return (independence_at_minus_one(mask^vbit)
                - independence_at_minus_one(mask &~(vbit|conflict[candidate])))
    return -independence_at_minus_one((1<<len(conflict))-1)


def subdiagrams(shape, remaining):
    for ascent in partitions(remaining):
        sub=tuple(reversed(ascent))
        if len(sub)<=len(shape) and all(sub[i]<=shape[i] for i in range(len(sub))):
            yield sub


@lru_cache(None)
def symmetric_character(shape, cycle_type):
    """Murnaghan–Nakayama formula with connected 2x2-free rim strips."""
    if not cycle_type:
        return int(not shape)
    r=cycle_type[-1]; answer=0
    for smaller in subdiagrams(shape,sum(shape)-r):
        ribbon={(i,j) for i,L in enumerate(shape)
                for j in range(smaller[i] if i<len(smaller) else 0,L)}
        if len(ribbon)!=r or not ribbon:
            continue
        if any((i,j+1) in ribbon and (i+1,j) in ribbon and (i+1,j+1) in ribbon
               for i,j in ribbon):
            continue
        seen={next(iter(ribbon))};stack=list(seen)
        while stack:
            i,j=stack.pop()
            for adjacent in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if adjacent in ribbon and adjacent not in seen:
                    seen.add(adjacent);stack.append(adjacent)
        if len(seen)==r:
            h=len({i for i,j in ribbon})
            answer+=(-1)**(h-1)*symmetric_character(smaller,cycle_type[:-1])
    return answer


def z_of_partition(parts):
    result=1
    for length, multiplicity in Counter(parts).items():
        result*=length**multiplicity*factorial(multiplicity)
    return result


def main():
    types=list(partitions(7))
    L={p:lefschetz(p) for p in types}
    expected = [22,6,-5,2,4,3,-3,2,0,4,2,-1,1,1,1]
    assert [L[p] for p in types]==expected
    coefficients={}
    for p in types:
        shape=tuple(reversed(p))
        numerator=sum(L[q]*symmetric_character(shape,q)*factorial(7)//z_of_partition(q)
                      for q in types)
        assert numerator%factorial(7)==0
        coefficients[shape]=numerator//factorial(7)
    nonzero={p:v for p,v in coefficients.items() if v}
    assert nonzero=={
        (7,):1,(4,3):1,(2,2,2,1):1,(1,)*7:-1,(2,1,1,1,1,1):-1}
    # The published homology dimensions are beta_6=29 and beta_9=7.
    # In the Grothendieck group H6-H9=L, the negative terms must occur
    # in H9; they consume its entire seven-dimensional rank.
    H9={(1,)*7:1,(2,1,1,1,1,1):1}
    H6={(7,):1,(4,3):1,(2,2,2,1):1}
    def hook_dimension(shape):
        hook_product=1
        for i,row in enumerate(shape):
            for j in range(row):
                hook_product*=row-j+sum(shape[k]>j for k in range(i+1,len(shape)))
        return factorial(7)//hook_product
    assert sum(m*hook_dimension(s) for s,m in H9.items())==7
    assert sum(m*hook_dimension(s) for s,m in H6.items())==29
    for cls in types:
        lhs=sum(m*symmetric_character(s,cls) for s,m in H6.items())
        lhs-=sum(m*symmetric_character(s,cls) for s,m in H9.items())
        assert lhs==L[cls]
        print(f'{str(cls):30s} {L[cls]:3d} {lhs:3d}')
    print('PASS: 15 Lefschetz traces; all 15 irreducible multiplicities; 29/7 ranks; classwise equality.')

if __name__=='__main__':
    main()
