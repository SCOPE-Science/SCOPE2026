"""Exact reproducible checks of maximum general-position sets in P_s strong K_(1,m).
No external dependencies. Uses independent BFS distances and positional counting."""
from collections import Counter, deque
from itertools import combinations, product
from math import comb


def strong_product(s,m):
    vertices=[(i,a) for i in range(s) for a in range(m+1)]
    adjacency=[[] for _ in vertices]
    for u,(i,a) in enumerate(vertices):
        for v,(j,b) in enumerate(vertices):
            if u!=v and abs(i-j)<=1 and (a==b or a==0 or b==0):
                adjacency[u].append(v)
    D=[]
    for src in range(len(vertices)):
        d=[-1]*len(vertices);d[src]=0;queue=deque([src])
        while queue:
            v=queue.popleft()
            for w in adjacency[v]:
                if d[w]<0:
                    d[w]=d[v]+1;queue.append(w)
        assert -1 not in d
        D.append(d)
    return vertices,D


def gp(subset,D):
    for u,v,w in combinations(subset,3):
        a,b,c=D[u][v],D[u][w],D[v][w]
        if a+b==c or a+c==b or b+c==a:
            return False
    return True


def proposed_structure(pts,m):
    counts=Counter(a for i,a in pts)
    if counts != {a:2 for a in range(1,m+1)}:
        return False
    support=sorted(set(i for i,a in pts))
    colors={i:{a for j,a in pts if i==j} for i in support}
    t=len(support)
    if t==2:
        return True
    if t==3:
        i,j,k=support
        if j==i+1 and k==j+1:return True
        if j==i+1 and k>j+1:return colors[i].isdisjoint(colors[j])
        if j>i+1 and k==j+1:return colors[j].isdisjoint(colors[k])
        return False
    if t==4:
        i,j,k,l=support
        return (j==i+1 and l==k+1 and
                colors[i].isdisjoint(colors[j]) and
                colors[k].isdisjoint(colors[l]))
    return False


def predicted_count(s,m):
    a=(2**m-2)
    b=(3**m-3)
    return (comb(s,2) + b*(s-2) + a*(s-2)*(s-3) +
            a*a*comb(s-2,2))


def pair_enumeration(s,m):
    # Independent counting through two distinct path layers for every leaf.
    pairs=list(combinations(range(s),2))
    count=0;types=Counter()
    for pair_choice in product(pairs,repeat=m):
        pts=[(i,a) for a,positions in enumerate(pair_choice,1) for i in positions]
        if proposed_structure(pts,m):
            count+=1
            types[len(set(i for i,a in pts))]+=1
    return count,types

full_cases=[(s,3) for s in range(2,9)]+[(s,4) for s in range(2,5)]+[(s,5) for s in range(2,4)]
full_checked=0
census={}
for s,m in full_cases:
    V,D=strong_product(s,m)
    c=0
    for S in combinations(range(len(V)),2*m):
        full_checked+=1
        actual=gp(S,D)
        classified=proposed_structure([V[u] for u in S],m)
        if actual!=classified:
            raise AssertionError(('GP/structure',s,m,S,actual,classified))
        if actual:c+=1
    expected=predicted_count(s,m)
    if c!=expected:
        raise AssertionError(('GP/count',s,m,c,expected))
    census[(s,m)]=c

pair_cases=[(s,3) for s in range(2,15)]+[(s,4) for s in range(2,8)]+[(s,5) for s in range(2,6)]
for s,m in pair_cases:
    count,types=pair_enumeration(s,m)
    a=2**m-2
    expected_by_support={
        2:comb(s,2),
        3:(3**m-3)*(s-2)+a*(s-2)*(s-3),
        4:a*a*comb(s-2,2),
    }
    if count!=predicted_count(s,m):
        raise AssertionError(('pairs/count',s,m,count,predicted_count(s,m)))
    if dict(types)!={k:v for k,v in expected_by_support.items() if v}:
        raise AssertionError(('pairs/support',s,m,types,expected_by_support))

print('ALL CHECKS PASSED; BFS/direct/structural exhaustive ' +
      ', '.join(f'(s={s},m={m},count={census[(s,m)]})' for s,m in full_cases) +
      f'; subsets_checked={full_checked}; positional_pairs_cases={len(pair_cases)};' +
      f' s14_m3_count={predicted_count(14,3)};' +
      f' s7_m4_count={predicted_count(7,4)};' +
      f' s5_m5_count={predicted_count(5,5)}')
