"""Enumerate the adjacent-position-swap graph induced on derangements."""
from collections import Counter, deque
from itertools import permutations


def signature(word):
    positions = {value: i for i, value in enumerate(word, 1)}
    return tuple(i for i in range(2, len(word)) if positions[i] < i)


def neighbors(word):
    n = len(word)
    for j in range(n - 1):
        a, b = word[j], word[j + 1]
        if a == j + 2 or b == j + 1:
            continue
        new = list(word)
        new[j], new[j + 1] = new[j + 1], new[j]
        yield tuple(new)


def profile(n):
    remaining = {p for p in permutations(range(1, n + 1)) if all(p[i] != i + 1 for i in range(n))}
    nvertices = len(remaining)
    classes = []
    seen_signatures = set()
    edges = 0
    isolates = []
    while remaining:
        root = remaining.pop()
        q = deque([root]); size = 0; halfedges = 0
        sig = signature(root)
        assert sig not in seen_signatures
        while q:
            w = q.popleft();size += 1
            assert signature(w) == sig
            adj = list(neighbors(w));halfedges += len(adj)
            for v in adj:
                if v in remaining:
                    remaining.remove(v)
                    q.append(v)
        if size == 1:isolates.append(root)
        classes.append(size)
        seen_signatures.add(sig)
        edges += halfedges // 2
    assert len(classes) == 2 ** (n - 2), (n, len(classes))
    assert len(seen_signatures) == 2 ** (n - 2)
    assert sorted(isolates) == sorted([tuple(range(2,n+1))+(1,), (n,)+tuple(range(1,n))]) if n>=3 else len(isolates)==1
    return nvertices,edges,len(classes),Counter(classes),len(isolates)


def shortest_path(n, src, dst):
    q=deque([src]);parents={src:None}
    while q:
        w=q.popleft()
        if w==dst:break
        for v in neighbors(w):
            if v not in parents:
                parents[v]=w;q.append(v)
    if dst not in parents:return None
    path=[];w=dst
    while w is not None:path.append(w);w=parents[w]
    return path[::-1]

if __name__=='__main__':
    for n in range(2,10):
        a,b,c,d,e=profile(n)
        print('n',n,'derangements',a,'edges',b,'components',c,'isolated',e,'sizes',sorted(d.items()))
    a=(3,1,2,5,6,4)
    b=(3,6,2,5,1,4)
    path=shortest_path(6,a,b)
    assert path and len(path)-1==7
    ref={v:i for i,v in enumerate(b)}
    inversion_distance=sum(ref[a[i]]>ref[a[j]] for i in range(6) for j in range(i+1,6))
    assert inversion_distance==5
    print('n6_witness_kendall',inversion_distance,'restricted',len(path)-1)
    print('n6_path',path)
    print('VERIFY_OK')
