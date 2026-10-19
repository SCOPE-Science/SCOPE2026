#!/usr/bin/env python3
"""Reproduce finite checks for an explicit pair-merging law in cyclic automata.

No packages beyond the Python standard library are required.
"""
from collections import deque


def map_pair(pair, letter, n):
    i, j = pair
    if letter == 'a':
        images = ((i + 1) % n, (j + 1) % n)
    elif letter == 'b':
        images = (0 if i == n - 1 else i, 0 if j == n - 1 else j)
    else:
        raise ValueError(letter)
    return tuple(sorted(set(images)))


def explicit_ranks(n):
    rank = {}
    h = n // 2
    for k in range(1, h + 1):
        if 2*k == n:
            for i in range(k):
                rank[(i,i+k)] = (k-1)*n + (k-i)
        else:
            for i in range(n):
                pair = tuple(sorted((i,(i+k) % n)))
                assert pair not in rank
                rank[pair] = k*n - i
    assert len(rank) == n*(n-1)//2
    assert set(rank.values()) == set(range(1, n*(n-1)//2+1))
    return rank


def breadth_first_distances(n):
    # Independent pair-state transition graph, reverse BFS from all singletons.
    vertices = [(i,j) for i in range(n) for j in range(i+1,n)]
    reverse = {p: [] for p in vertices}
    dist = {p: None for p in vertices}
    first = deque()
    for p in vertices:
        for x in 'ab':
            image = map_pair(p,x,n)
            if len(image)==1:
                if dist[p] is None:
                    dist[p]=1
                    first.append(p)
            else:
                reverse[image].append(p)
    while first:
        q = first.popleft()
        for p in reverse[q]:
            if dist[p] is None:
                dist[p] = dist[q] + 1
                first.append(p)
    return dist


def shortest_path_counts(n, dist):
    by_rank = {d:p for p,d in dist.items()}
    # Once distance is obtained by BFS, shortest paths must lower it by one.
    counts = {}
    letters = {}
    for d in sorted(by_rank):
        p=by_rank[d]
        choices=[]
        count=0
        for x in 'ab':
            v=map_pair(p,x,n)
            if len(v)==1 and d==1:
                choices.append(x)
                count+=1
            elif len(v)==2 and dist[v]==d-1:
                choices.append(x)
                count+=counts[v]
        counts[p]=count
        letters[p]=choices
    return counts,letters


def check(n):
    formula = explicit_ranks(n)
    bfs=breadth_first_distances(n)
    assert bfs==formula, ('distance failure', n)
    counts, choices=shortest_path_counts(n,bfs)
    assert all(v==1 for v in counts.values()), ('nonunique shortest',n)
    assert all(len(v)==1 for v in choices.values()), ('two choices',n)
    for p,d in formula.items():
        for x in 'ab':
            q=map_pair(p,x,n)
            dq=0 if len(q)==1 else formula[q]
            assert dq>=d-1, ('potential failure', n,p,x,d,dq)
        chosen=choices[p][0]
        q=map_pair(p,chosen,n)
        assert (0 if len(q)==1 else formula[q])==d-1
    highest=max(formula,key=formula.get)
    letters=[]
    p=highest
    while len(p)==2:
        x=choices[p][0]
        letters.append(x)
        p=map_pair(p,x,n)
    word=''.join(letters)
    h=n//2
    predicted=('a'*(h-1)+'b'+('a'*(n-1)+'b')*(h-1) if n%2==0
               else ('a'*(n-1)+'b')*h)
    assert word==predicted, ('master failure', n, word,predicted)
    return len(formula),len(word)


if __name__=='__main__':
    for n in range(2,81):
        pairs, master = check(n)
        assert pairs==master==n*(n-1)//2
        if n in (2,3,4,5,8,13,20,40,80):
            print(f'n={n} pair_count={pairs} distances=1..{pairs} unique_shortest=YES master_length={master}')
    print('VERIFY_OK: all pair states, independent reverse BFS and path counts, n=2..80')
