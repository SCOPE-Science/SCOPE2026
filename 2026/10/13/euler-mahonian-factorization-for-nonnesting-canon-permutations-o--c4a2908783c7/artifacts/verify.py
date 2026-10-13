"""Exact verification of descent/major-index refinement for pattern-free canon words.

This uses only Python standard library. All listed parameter cases are exhaustive.
"""
from collections import Counter
from itertools import permutations, combinations
from math import factorial


def lattice_words(n,k):
    counts=[0]*n
    w=[]
    def rec():
        if len(w)==n*k:
            yield tuple(w)
            return
        for i in range(n):
            if counts[i]<k and (i==0 or counts[i]<counts[i-1]):
                counts[i]+=1;w.append(i)
                yield from rec()
                w.pop();counts[i]-=1
    yield from rec()


def avoids_nesting_positions(w):
    """A nested pair requires two copies of one letter between two of another."""
    pos={x:[] for x in set(w)}
    for i,x in enumerate(w):pos[x].append(i)
    for a,b in combinations(sorted(pos),2):
        aa,bb=pos[a],pos[b]
        if sum(aa[0]<t<aa[-1] for t in bb)>=2:return False
        if sum(bb[0]<t<bb[-1] for t in aa)>=2:return False
    return True


def avoids_nesting_literal(w):
    for i,j,r,s in combinations(range(len(w)),4):
        a,b,c,d=w[i],w[j],w[r],w[s]
        if a==d and b==c and a!=b:
            return False
    return True


def swapped_family(sigma,k):
    n=len(sigma)
    base=[v for v in sigma for _ in range(k)]
    for mask in range(1<<(n-1)):
        w=base.copy()
        for i in range(n-1):
            if mask>>i & 1:
                at=(i+1)*k
                w[at-1],w[at]=w[at],w[at-1]
        yield tuple(w)


def stats(w):
    ds=[i for i in range(1,len(w)) if w[i-1]>w[i]]
    return len(ds),sum(ds)


def poly_mul(A,B):
    C=Counter()
    for (d1,m1),c1 in A.items():
        for (d2,m2),c2 in B.items():
            C[d1+d2,m1+m2]+=c1*c2
    return C


def predicted(n,k):
    A=Counter(stats(sigma) for sigma in permutations(range(n)))
    A=Counter({(d,k*m):cnt for (d,m),cnt in A.items()})
    for i in range(1,n):
        A=poly_mul(A,Counter({(0,0):1,(1,k*i):1}))
    return A

cases=[(n,k) for n in range(1,5) for k in (3,4)]
cases += [(5,3),(2,5),(3,5)]
canons_tested=0
literal_tested=0
admissible_tested=0
for n,k in cases:
    found=Counter()
    all_good=set()
    for rel in lattice_words(n,k):
        for sig in permutations(range(n)):
            w=tuple(sig[x] for x in rel)
            ok=avoids_nesting_positions(w)
            if n<=3 and k<=3:
                assert ok==avoids_nesting_literal(w), ("literal",n,k,w)
                literal_tested+=1
            canons_tested+=1
            if ok:
                found[stats(w)]+=1
                all_good.add(w)
                admissible_tested+=1
    structural={w for sig in permutations(range(n)) for w in swapped_family(sig,k)}
    assert all_good==structural, ("classification",n,k,len(all_good),len(structural))
    want=predicted(n,k)
    assert found==want, ("bivariate polynomial",n,k, found, want)
    assert sum(found.values())==factorial(n)*2**(n-1), ("known cardinality",n,k)
    print(f"n={n} k={k}: words={sum(found.values())}, "
          f"bivariate_terms={len(found)}, "
          f"major_range={min(q for d,q in found)}..{max(q for d,q in found)}")
print("ALL CHECKS PASSED; "
      f"cases={len(cases)}; canons_tested={canons_tested}; "
      f"literal_four_index_checks={literal_tested}; "
      f"admissible_words={admissible_tested}; "
      "all cases exhaustive")
