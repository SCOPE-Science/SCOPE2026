#!/usr/bin/env python3
"""Reproduce finite locally-transitive tournament score fibers and examples.
Pure Python 3.10+, no external dependencies. Vertex i beats j iff row[i] has bit j.
"""
from itertools import combinations, permutations
from collections import defaultdict, Counter

def transitive(rows, S):
    degrees = sorted(sum((rows[v] >> w) & 1 for w in S) for v in S)
    return degrees == list(range(len(S)))

def local(rows):
    n = len(rows)
    for v in range(n):
        plus = [u for u in range(n) if rows[v] >> u & 1]
        minus = [u for u in range(n) if u != v and rows[u] >> v & 1]
        if not transitive(rows, plus) or not transitive(rows, minus): return False
    return True

def score(rows): return tuple(sorted(r.bit_count() for r in rows))

def isomorphic(A,B):
    n=len(A)
    sa=[v.bit_count() for v in A]; sb=[v.bit_count() for v in B]
    for p in permutations(range(n)):
        if any(sa[i]!=sb[p[i]] for i in range(n)): continue
        if all(((A[i]>>j)&1)==((B[p[i]]>>p[j])&1) for i in range(n) for j in range(i+1,n)):
            return True
    return False

def tournaments(n):
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        rows=[0]*n
        for k,(i,j) in enumerate(pairs):
            if mask>>k & 1:rows[j]|=1<<i
            else:rows[i]|=1<<j
        yield rows

def five_regular(rows):
    return sum(all(sum((rows[v]>>w)&1 for w in S)==2 for v in S)
               for S in combinations(range(len(rows)),5))

def extensions(rows):
    n=len(rows); c=Counter()
    for mask in range(1<<n):
        extended=rows[:]+[0]
        for i in range(n):
            if mask>>i&1:extended[-1]|=1<<i
            else:extended[i]|=1<<n
        if local(extended):c[extended[-1].bit_count()]+=1
    return c

def clone(rows,v,h):
    # Replace vertex v by a transitive chain v_0 -> ... -> v_(h-1).
    groups=[[i] if i != v else list(range(v,v+h)) for i in range(len(rows))]
    # More directly assign positions with a non-overlapping new index block
    old=list(range(len(rows)))
    new=[]
    for i in old:
        for j in range(h if i==v else 1):new.append((i,j))
    result=[0]*len(new)
    for a,(i,t) in enumerate(new):
        for b,(j,u) in enumerate(new):
            if a==b:continue
            win=(t<u) if i==j else ((rows[i]>>j)&1)
            if win:result[a]|=1<<b
    return result

def main():
    for n in range(1,7):
        groups=defaultdict(list); labelled=0
        for rows in tournaments(n):
            if not local(rows):continue
            labelled+=1
            bucket=groups[score(rows)]
            if not any(isomorphic(rows,old) for old in bucket):bucket.append(rows)
        hist=sorted((s,len(b)) for s,b in groups.items())
        totals=sum(c for _,c in hist)
        assert (totals==[1,1,2,2,4,6][n-1])
        assert max((c for _,c in hist),default=1)==(2 if n==6 else 1)
        print(f'n={n} labelled={labelled} isomorphism_classes={totals} score_fibers={len(groups)} histogram={hist}')
    A=[14,28,56,48,33,3]
    B=[14,12,56,48,35,3]
    assert local(A) and local(B)
    assert score(A)==score(B)==(2,2,2,3,3,3)
    assert not isomorphic(A,B)
    assert five_regular(A)==2 and five_regular(B)==0
    assert extensions(A)==extensions(B)==Counter({2:3,3:6,4:3})
    print('base_witnesses score=(2,2,2,3,3,3), row_masks=',A,B,
          'regular_5_counts=(2,0), extension_histogram=(3,6,3)')
    # A_1 and B_0 both score 3, with predecessor score multiset (2,3)
    for rows,v in [(A,1),(B,0)]:
        assert rows[v].bit_count()==3
        assert tuple(sorted(rows[u].bit_count() for u in range(6) if rows[u]>>v&1))==(2,3)
    for h in range(1,13):
        AA=clone(A,1,h);BB=clone(B,0,h)
        assert local(AA) and local(BB)
        assert score(AA)==score(BB)
        assert five_regular(AA)==2*h
        assert five_regular(BB)==0
        if len(AA)<=10:
            assert extensions(AA)==extensions(BB)
            forecast=Counter()
            for s in score(AA): forecast[s]+=1;forecast[s+1]+=1
            assert extensions(AA)==forecast
        print(f'clone_size={h} order={len(AA)} score_equal=True regular_5_subtournaments=({five_regular(AA)},0)')
    print('ALL_CHECKS_PASS')
if __name__=='__main__':main()
