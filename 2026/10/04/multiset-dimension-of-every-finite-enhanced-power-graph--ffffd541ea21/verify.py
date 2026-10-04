from itertools import combinations, permutations
from collections import deque


def closure(elements, mul, gens):
    H = {elements[0]}
    H.update(gens)
    changed = True
    while changed:
        changed = False
        for a in list(H):
            for b in list(H):
                c = mul(a, b)
                if c not in H:
                    H.add(c)
                    changed = True
    return H


def is_cyclic_subgroup(elements, mul, H):
    for g in H:
        if closure(elements, mul, [g]) == H:
            return True
    return False


def enhanced_graph(elements, mul):
    n = len(elements)
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            H = closure(elements, mul, [elements[i], elements[j]])
            if is_cyclic_subgroup(elements, mul, H):
                adj[i].add(j)
                adj[j].add(i)
    return adj


def distances(adj):
    n = len(adj)
    D = []
    for s in range(n):
        d = [-1] * n
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    q.append(v)
        assert all(x >= 0 for x in d)
        D.append(d)
    return D


def md_nonempty(adj):
    n = len(adj)
    D = distances(adj)
    for k in range(1, n + 1):
        for W in combinations(range(n), k):
            reps = [tuple(sorted(D[v][w] for w in W)) for v in range(n)]
            if len(set(reps)) == n:
                return k
    return None


def cyclic(n):
    E = tuple(range(n))
    return E, (lambda a, b: (a + b) % n)


def klein4():
    E = ((0,0),(1,0),(0,1),(1,1))
    return E, (lambda a,b: (a[0]^b[0], a[1]^b[1]))


def compose(p, q):
    return tuple(p[q[i]] for i in range(3))


def s3():
    E = tuple(permutations(range(3)))
    ident = (0,1,2)
    E = (ident,) + tuple(x for x in E if x != ident)
    return E, compose


def check(name, group, expected):
    E, mul = group
    adj = enhanced_graph(E, mul)
    assert all(0 in adj[i] for i in range(1, len(E)))
    got = md_nonempty(adj)
    assert got == expected, (name, got, expected)


check('C1', cyclic(1), 1)
check('C2', cyclic(2), 1)
check('C3', cyclic(3), None)
check('C4', cyclic(4), None)
check('V4', klein4(), None)
check('S3', s3(), None)
print('VERIFY_OK')
