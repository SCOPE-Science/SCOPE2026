#!/usr/bin/env python3
"""Exact, finite cross-checks for two-row nestedness/modularity formulas.

The mathematical result for arbitrary n is proved separately by column types,
community-label reduction, and a quadratic optimization. Enumeration below
only checks finite instances and does not claim to prove the infinite theorem.
"""
from fractions import Fraction
from itertools import product
from math import comb


def predicates(cols):
    n = len(cols)
    a = cols.count(1)
    b = cols.count(2)
    c = cols.count(3)
    assert a+b+c == n and 1 <= c < n
    return n,a,b,c


def predicted_nodf(cols):
    n,a,b,c=predicates(cols)
    out = Fraction(c*(a+b), comb(n,2)+1)
    if a!=b:
        out+= Fraction(c, (c+min(a,b))*(comb(n,2)+1))
    return out


def predicted_modularity(cols):
    n,a,b,c=predicates(cols)
    e=n+c
    x=max(a,b)
    return Fraction(2*x*(n-x), e*e)


def direct_nodf(cols):
    n = len(cols)
    k0 = sum(bool(t&1) for t in cols)
    k1 = sum(bool(t&2) for t in cols)
    numerator = Fraction(0)
    if k0 != k1:
        overlap = sum(t==3 for t in cols)
        numerator += Fraction(overlap, min(k0,k1))
    for i in range(n):
        for j in range(i+1, n):
            di=cols[i].bit_count()
            dj=cols[j].bit_count()
            if di != dj:
                numerator += Fraction((cols[i]&cols[j]).bit_count(), min(di,dj))
    return numerator / (comb(n,2)+1)


def restricted_growth_partitions(number_of_vertices):
    """All set partitions with canonical labels; exhaustive and duplication-free."""
    def rec(labels, largest):
        if len(labels)==number_of_vertices:
            yield tuple(labels)
            return
        for j in range(largest+2):
            yield from rec(labels+[j], max(largest,j))
    yield from rec([0],0)


def brute_modularity_all_partitions(cols, partitions):
    n=len(cols)
    e=sum(t.bit_count() for t in cols)
    k=(sum(bool(t&1) for t in cols), sum(bool(t&2) for t in cols))
    dj=[t.bit_count() for t in cols]
    best_num=0
    for labels in partitions:
        score_num=0
        for i in (0,1):
            for j,t in enumerate(cols):
                if labels[i]==labels[j+2]:
                    score_num += e * (1 if t&(1<<i) else 0) - k[i]*dj[j]
        if score_num>best_num:
            best_num=score_num
    return Fraction(best_num, e*e)


def brute_modularity_2_labels(cols):
    n=len(cols)
    e=sum(t.bit_count() for t in cols)
    k=(sum(bool(t&1) for t in cols), sum(bool(t&2) for t in cols))
    best=0
    for choices in product((0,1),repeat=n):
        score=0
        for j,t in enumerate(cols):
            i=choices[j]
            score += e * (1 if t&(1<<i) else 0) - k[i]*t.bit_count()
        best=max(best,score)
    return Fraction(best, e*e)


def formula_frontier(n,c):
    s=n-c
    return set(range(min(s,(n+1)//2),s+1))


def actual_frontier(n,c):
    s=n-c
    candidates={}
    for x in range((s+1)//2,s+1):
        a=x;b=s-x
        cols=(1,)*a+(2,)*b+(3,)*c
        candidates[x]=(direct_nodf(cols), predicted_modularity(cols))
    ans=set()
    for x,pair in candidates.items():
        dominated=False
        for y,(nscore,qscore) in candidates.items():
            if y==x:continue
            if nscore>=pair[0] and qscore>=pair[1] and (nscore>pair[0] or qscore>pair[1]):
                dominated=True
                break
        if not dominated:ans.add(x)
    return ans


def run():
    matrices=0
    partitions_checked=0
    label_assignments_checked=0
    for n in range(2,9):
        all_parts=tuple(restricted_growth_partitions(n+2)) if n<=5 else None
        for c in range(1,n):
            s=n-c
            for cols in product((1,2,3),repeat=n):
                if cols.count(3)!=c: continue
                assert predicted_nodf(cols)==direct_nodf(cols),('nodf',cols)
                assert predicted_modularity(cols)==brute_modularity_2_labels(cols),('modularity_two_label',cols)
                if all_parts is not None:
                    assert predicted_modularity(cols)==brute_modularity_all_partitions(cols,all_parts),('modularity_all_partitions',cols)
                    partitions_checked+=len(all_parts)
                matrices+=1
                label_assignments_checked+=2**n
            assert formula_frontier(n,c)==actual_frontier(n,c),(n,c)
            joint= ((n-c) in actual_frontier(n,c) and
                    predicted_modularity((1,)*(n-c)+(3,)*c) ==
                    max(predicted_modularity((1,)*x+(2,)*(s-x)+(3,)*c)
                        for x in range((s+1)//2,s+1)))
            assert joint == (c>=s-1),(n,c,joint)
    # A concrete low-connectance three-point Pareto frontier.
    assert actual_frontier(6,1)=={3,4,5}
    scores={x:(predicted_nodf((1,)*x+(2,)*(5-x)+(3,)),
               predicted_modularity((1,)*x+(2,)*(5-x)+(3,)))
            for x in (3,4,5)}
    assert scores=={3:(Fraction(1,3),Fraction(18,49)),
                    4:(Fraction(11,32),Fraction(16,49)),
                    5:(Fraction(3,8),Fraction(10,49))},scores
    # The common-maximizer threshold includes its equality boundary.
    assert actual_frontier(7,3)=={4}
    print('VERIFY_OK')
    print('matrices',matrices)
    print('all_set_partitions_checked',partitions_checked)
    print('two_label_assignments_checked',label_assignments_checked)
    print('network_dimensions',[(n,n-1) for n in range(2,9)])
    print('low_connectance_frontier',scores)

if __name__ == '__main__':
    run()
