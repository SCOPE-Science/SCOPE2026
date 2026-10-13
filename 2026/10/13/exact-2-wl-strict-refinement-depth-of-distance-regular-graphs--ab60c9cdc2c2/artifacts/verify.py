from collections import deque, Counter, defaultdict
from itertools import combinations
from math import ceil, log2


def cycle(n):
    A=[set() for _ in range(n)]
    for i in range(n):
        j=(i+1)%n
        A[i].add(j); A[j].add(i)
    return A


def complete_bipartite(a,b):
    n=a+b; A=[set() for _ in range(n)]
    for i in range(a):
        for j in range(a,n):
            A[i].add(j); A[j].add(i)
    return A


def hypercube(d):
    n=1<<d; A=[set() for _ in range(n)]
    for x in range(n):
        for i in range(d):
            A[x].add(x^(1<<i))
    return A


def petersen():
    # vertices are 2-subsets of {0,1,2,3,4}; adjacency = disjointness
    vs=list(combinations(range(5),2)); n=len(vs)
    A=[set() for _ in range(n)]
    for i in range(n):
        si=set(vs[i])
        for j in range(i+1,n):
            if si.isdisjoint(vs[j]):
                A[i].add(j); A[j].add(i)
    return A


def johnson(n,k):
    vs=list(combinations(range(n),k)); N=len(vs)
    A=[set() for _ in range(N)]
    sets=[set(v) for v in vs]
    for i in range(N):
        for j in range(i+1,N):
            if len(sets[i]&sets[j])==k-1:
                A[i].add(j); A[j].add(i)
    return A


def distances(A):
    n=len(A); D=[[None]*n for _ in range(n)]
    for s in range(n):
        D[s][s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in A[u]:
                if D[s][v] is None:
                    D[s][v]=D[s][u]+1; q.append(v)
        assert all(x is not None for x in D[s])
    return D


def is_distance_regular(A,D):
    n=len(A); diam=max(max(r) for r in D)
    ref={}
    for x in range(n):
        for y in range(n):
            k=D[x][y]
            c=Counter((D[x][z],D[z][y]) for z in range(n))
            if k not in ref: ref[k]=c
            elif ref[k]!=c: return False
    return set(ref)==set(range(diam+1))


def canonicalize(signatures):
    vals={v for row in signatures for v in row}
    ids={v:i for i,v in enumerate(sorted(vals, key=repr))}
    return [[ids[v] for v in row] for row in signatures]


def two_wl(A):
    n=len(A)
    colors=[]
    for x in range(n):
        row=[]
        for y in range(n):
            row.append(0 if x==y else (1 if y in A[x] else 2))
        colors.append(row)
    strict=0
    while True:
        sig=[[None]*n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                pairs=Counter((colors[x][z],colors[z][y]) for z in range(n))
                sig[x][y]=(colors[x][y],tuple(sorted(pairs.items())))
        new=canonicalize(sig)
        # Compare partitions, not raw integer labels.
        old_rel=[[colors[x][y]==colors[u][v] for u in range(n) for v in range(n)] for x in range(n) for y in range(n)]
        new_rel=[[new[x][y]==new[u][v] for u in range(n) for v in range(n)] for x in range(n) for y in range(n)]
        if old_rel==new_rel:
            return strict, colors
        colors=new; strict+=1


def terminal_is_distance_partition(colors,D):
    n=len(colors)
    bydist=defaultdict(set)
    color_to_dist=defaultdict(set)
    for x in range(n):
        for y in range(n):
            bydist[D[x][y]].add(colors[x][y])
            color_to_dist[colors[x][y]].add(D[x][y])
    return all(len(s)==1 for s in bydist.values()) and all(len(s)==1 for s in color_to_dist.values())


def predicted(diam):
    return 0 if diam<=2 else ceil(log2(diam-1))


def check(name,A):
    D=distances(A); diam=max(max(r) for r in D)
    assert is_distance_regular(A,D), f'{name} not distance-regular'
    r,c=two_wl(A)
    assert r==predicted(diam), (name,diam,r,predicted(diam))
    assert terminal_is_distance_partition(c,D), f'{name}: terminal colors != distance partition'
    return name,len(A),diam,r


def main():
    out=[]
    for n in range(3,15): out.append(check(f'C{n}',cycle(n)))
    for a in range(2,6): out.append(check(f'K{a},{a}',complete_bipartite(a,a)))
    for d in range(1,6): out.append(check(f'Q{d}',hypercube(d)))
    out.append(check('Petersen',petersen()))
    for n in range(4,8): out.append(check(f'J({n},2)',johnson(n,2)))
    print('VERIFY_OK', f'graphs={len(out)}', f'max_vertices={max(x[1] for x in out)}',
          'families=cycles,balanced_complete_bipartite,hypercubes,Petersen,Johnson')

if __name__=='__main__': main()
