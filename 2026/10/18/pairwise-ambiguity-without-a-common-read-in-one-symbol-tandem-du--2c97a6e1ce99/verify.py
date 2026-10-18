#!/usr/bin/env python3
"""Exact finite replay for single-letter tandem-duplication clique types."""
from collections import defaultdict
from itertools import combinations, product
from math import comb


def predicted(n, q, size=3):
    up = down = 0
    for r in range(size, n + 1):
        up += q * (q - 1) ** (r - 1) * comb(r, size) * (comb(n - 2, r - 1) if n - 2 >= r - 1 else 0)
        down += q * (q - 1) ** (r - 1) * comb(r, size) * (comb(n - size, r - 1) if n - size >= r - 1 else 0)
    return up, down


def child_set(word):
    return {word[:i+1] + (word[i],) + word[i+1:] for i in range(len(word))}


def run_data(word):
    root = [word[0]]
    runs = [1]
    for x in word[1:]:
        if x == root[-1]:
            runs[-1] += 1
        else:
            root.append(x)
            runs.append(1)
    return tuple(root), tuple(r - 1 for r in runs)


def orientation(triple):
    entries = [run_data(x) for x in triple]
    assert len({root for root, vec in entries}) == 1
    vectors = [vec for root, vec in entries]
    low = tuple(min(v[i] for v in vectors) for i in range(len(vectors[0])))
    high = tuple(max(v[i] for v in vectors) for i in range(len(vectors[0])))
    if all(sum(a-b for a,b in zip(v,low)) == 1 for v in vectors):
        return 'up'
    if all(sum(a-b for a,b in zip(high,v)) == 1 for v in vectors):
        return 'down'
    raise AssertionError('unknown triangle type')


def run(q,n):
    words = list(product(range(q), repeat=n))
    children = [child_set(w) for w in words]
    parents = defaultdict(list)
    for i, ys in enumerate(children):
        for y in ys:parents[y].append(i)
    adjacency = [set() for w in words]
    for src in parents.values():
        for i,j in combinations(src,2):
            adjacency[i].add(j); adjacency[j].add(i)
    observed = [0,0]; count = 0
    for i in range(len(words)):
        for j in adjacency[i]:
            if j <= i:continue
            for k in adjacency[i].intersection(adjacency[j]):
                if k <= j:continue
                typ=orientation([words[t] for t in (i,j,k)])
                intersection=children[i]&children[j]&children[k]
                assert (typ=='down')==(len(intersection)==1),(q,n,words[i],words[j],words[k],typ,intersection)
                observed[typ=='down']+=1
                count+=1
    assert tuple(observed)==predicted(n,q),(q,n,observed,predicted(n,q))
    omega=max([1]+[len(x) for x in parents.values()])
    assert omega==(n+1)//2 or (n+1)//2==0
    if n >= 4 and ((q==2 and n<=8) or (q==3 and n<=6) or (q==4 and n<=5)):
        def cliques_after(prefix, candidates, size):
            if len(prefix)==size:
                typ=orientation([words[t] for t in prefix])
                common=set.intersection(*(children[t] for t in prefix))
                assert (typ=='down')==(len(common)==1)
                counts[typ=='down']+=1
                return
            for j,c in enumerate(candidates):
                cliques_after(prefix+[c], [d for d in candidates[j+1:] if d in adjacency[c]], size)
        for size in range(4,n):
            counts=[0,0]
            cliques_after([], list(range(len(words))), size)
            assert tuple(counts)==predicted(n,q,size), (q,n,size,counts,predicted(n,q,size))
    print('q',q,'n',n,'words',len(words),'edges',sum(map(len,adjacency))//2,'up',observed[0],'down',observed[1],'max_parents',omega)
    return count


if __name__=='__main__':
    total=0
    for q,hi in [(2,10),(3,7),(4,6)]:
        for n in range(1,hi+1):total+=run(q,n)
    print('TANDEM_TRIANGLE_HELLY_PASS triples',total)
