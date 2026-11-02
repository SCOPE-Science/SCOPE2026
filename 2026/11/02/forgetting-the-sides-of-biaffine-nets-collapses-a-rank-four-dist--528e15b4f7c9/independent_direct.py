"""Independent unoptimized vertex-tuple recursion for four-round types.

Enumerates ALL ordered pairs and subsequent vertices without orbit
representatives. Intended as a cross-check on small prime-field graphs.
"""
from itertools import product


def incidence(q):
    vertices = [('P', x, y) for x in range(q) for y in range(q)]
    vertices += [('L', m, b) for m in range(q) for b in range(q)]
    edges = []
    for a in vertices:
        row = []
        for b in vertices:
            if a[0] == 'P' and b[0] == 'L':
                row.append(a[2] == (b[1]*a[1]+b[2]) % q)
            elif a[0] == 'L' and b[0] == 'P':
                row.append(b[2] == (a[1]*b[1]+a[2]) % q)
            else:
                row.append(False)
        edges.append(row)
    return vertices, edges


def signature(q, colored):
    vertices, edges = incidence(q)
    n = len(vertices)
    def atomic(t):
        pairs = tuple((t[i] == t[j], edges[t[i]][t[j]])
                      for i in range(len(t)) for j in range(i+1, len(t)))
        return (tuple(vertices[x][0] for x in t), pairs) if colored else pairs
    def triple(t):
        possibilities = set()
        for w in range(n):
            if w in t:
                continue
            mark = tuple(edges[w][x] for x in t)
            possibilities.add((vertices[w][0], mark) if colored else mark)
        return atomic(t), frozenset(possibilities)
    def pair(t):
        return atomic(t), frozenset(triple(t+(w,)) for w in range(n))
    def singleton(t):
        return atomic(t), frozenset(pair(t+(w,)) for w in range(n))
    return frozenset(singleton((v,)) for v in range(n))


def main():
    pure = {q: signature(q, False) for q in (2, 3, 5)}
    named = {q: signature(q, True) for q in (2, 3, 5)}
    assert pure[2] != pure[3] == pure[5] 
    assert named[2] != named[3] and named[3] != named[5] 
    assert named[2] != named[5]
    print('INDEPENDENT_DIRECT_ENUMERATION_OK orders=2,3,5')


if __name__ == '__main__':
    main()
