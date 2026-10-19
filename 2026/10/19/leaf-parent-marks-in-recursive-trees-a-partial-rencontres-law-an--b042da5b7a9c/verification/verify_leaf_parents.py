"""Exact checks for leaf-parent events in uniform random recursive trees.

This script enumerates all labelled recursive trees at orders 2,...,8;
checks universal leaf-parent cylinder probabilities, the restricted
permutation-fixed-point law, protected-root and protected-vertex probabilities,
and cross-parent leaf-child covariance.
"""
from itertools import product, permutations, combinations
from fractions import Fraction
from collections import Counter
from math import factorial, comb

checks = 0
for n in range(2,9):
    trees = list(product(*(range(1,i) for i in range(2,n+1))))
    den = factorial(n-1)
    assert len(trees) == den
    # For every tree record its set of leaf-parent marks (j,i).
    samples=[]
    for seq in trees:
        parent={i:seq[i-2] for i in range(2,n+1)}
        nonleaf=set(seq)
        marks=frozenset((parent[i],i) for i in range(2,n+1) if i not in nonleaf)
        samples.append(marks)
    taglist=[(j,i) for i in range(2,n+1) for j in range(1,i)]
    for size in range(1,min(3,len(taglist))+1):
        for tags in combinations(taglist,size):
            children={i for (j,i) in tags}
            eligible=(len(children)==size and all(j not in children for j,i in tags))
            count=sum(all(tag in marks for tag in tags) for marks in samples)
            predicted=Fraction(factorial(n-size-1),factorial(n-1)) if eligible else Fraction(0)
            assert Fraction(count,den)==predicted, (n,tags,count,den,predicted)
            checks+=1
    # Exact indicator-field distribution vs permutations on n-1 labels.
    for j in range(1,n+1):
        kids=list(range(j+1,n+1))
        distribution=Counter(tuple(int((j,i) in marks) for i in kids) for marks in samples)
        perm_dist=Counter(tuple(int(perm[i-2]==i-1) for i in kids) for perm in permutations(range(1,n)))
        assert distribution==perm_dist, (n,j,distribution,perm_dist)
        checks+=1
        p0=sum(1 for marks in samples if all((j,i) not in marks for i in kids))
        # Protected = no leaf child and positive total children.
        protected=sum(1 for seq,marks in zip(trees,samples)
                      if all((j,i) not in marks for i in kids)
                      and (j in seq))
        formula=sum(Fraction((-1)**r*comb(n-j,r),
                             factorial(n-1)//factorial(n-1-r)) for r in range(n-j+1))
        formula-=Fraction(j-1,n-1)
        assert Fraction(protected,den)==formula,(n,j,protected,formula)
        checks+=1
    for j in range(1,n):
        for k in range(j+1,n+1):
            # use direct Y counts, not indicators of Y>0
            total_j=sum(sum((j,i) in marks for i in range(j+1,n+1)) for marks in samples)
            total_k=sum(sum((k,i) in marks for i in range(k+1,n+1)) for marks in samples)
            total_prod=sum(sum((j,i) in marks for i in range(j+1,n+1))*sum((k,i) in marks for i in range(k+1,n+1)) for marks in samples)
            cov=Fraction(total_prod,den)-Fraction(total_j,den)*Fraction(total_k,den)
            predicted=Fraction(0) if n==2 else Fraction(-(n-k)*(n+j-2),(n-1)**2*(n-2))
            assert cov==predicted,(n,j,k,cov,predicted)
            checks+=1
    print('n=',n,'trees=',den,'checks_so_far=',checks)
print('TOTAL_EXACT_ASSERTIONS',checks)
