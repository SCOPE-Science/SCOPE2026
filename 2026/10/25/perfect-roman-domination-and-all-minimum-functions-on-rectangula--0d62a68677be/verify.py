#!/usr/bin/env python3
"""Independent finite checks for perfect Roman minimum classifications on rook graphs.

Uses the original neighbor condition on all ternary assignments in modest boards,
then uses all 2-label sets with a separate direct assignment test of their unique
minimal 1-label completion on larger boards.  Neither test proves the infinite claim.
"""
from itertools import product, combinations
from collections import Counter


def predicted(p, q):
    if (p, q) == (2, 2):
        return 3, 4
    count = q + (p if p == q else 0)
    if (p, q) == (2, 3):
        count += 6
    if (p, q) == (3, 3):
        count += 9
    return 2 * p, count


def neighbors(p,q):
    return [tuple(v for v in range(p*q) if v!=u and (v//q==u//q or v%q==u%q)) for u in range(p*q)]


def is_perfect_roman(labels, adj):
    return all(labels[v]!=0 or sum(labels[u]==2 for u in adj[v])==1 for v in range(len(labels)))


def brute_labels(p,q):
    adj=neighbors(p,q)
    b=10**9; count=0; total=0
    for labels in product((0,1,2), repeat=p*q):
        total += 1
        if not is_perfect_roman(labels,adj):
            continue
        w=sum(labels)
        if w<b:
            b=w; count=1
        elif w==b:
            count+=1
    exp=predicted(p,q)
    assert (b,count)==exp, (p,q,b,count,exp)
    return total


def brute_defender_sets(p,q):
    # Any optimum below or at 2p needs at most p twos; for C4 at most 1.
    adj=neighbors(p,q)
    N=p*q
    best=10**9; count=0; tested=0
    for t in range(0,p+1):
        for T in combinations(range(N),t):
            tested+=1
            two=set(T)
            labels=[2 if v in two else 0 if sum(u in two for u in adj[v])==1 else 1 for v in range(N)]
            assert is_perfect_roman(labels,adj)
            w=sum(labels)
            if w<best: best=w; count=1
            elif w==best:count+=1
    exp=predicted(p,q)
    assert (best,count)==exp,(p,q,best,count,exp)
    return tested


def check_inequalities():
    cases=0
    for p in range(4,51):
        for q in range(p, p+20):
            for r in range(1,p):
                for c in range(1,p):
                    for t in range(max(r,c),min(p-1,r*c)+1):
                        g=(p-r)*(q-c)+r*c+t
                        assert g>2*p,(p,q,r,c,t,g)
                        cases+=1
    return cases


def main():
    total=0
    for p,q in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4)]:
        t=brute_labels(p,q);total+=t
        print('DIRECT',p,q,'assignments',t,'minimum/count',predicted(p,q))
    total_sets=0
    for p,q in [(2,2),(2,3),(2,4),(2,8),(3,3),(3,4),(3,8),(4,4),(4,5),(5,5),(5,6)]:
        t=brute_defender_sets(p,q); total_sets+=t
        print('DEFENDERS',p,q,'sets',t,'minimum/count',predicted(p,q))
    cases=check_inequalities()
    print('DIRECT_TOTAL',total)
    print('DEFENDER_TOTAL',total_sets)
    print('INEQUALITY_CASES',cases)
    print('VERIFY_OK')

if __name__=='__main__':main()
