"""Finite comparison of repeated commutator fibers in two ways."""
from collections import Counter
from itertools import product

EDGES = ((0,0), (0,1), (0,1), (1,2), (2,0))
N, M = 3, len(EDGES)


def mul(x, y):
    return tuple(x[v]*y[v] for v in range(N)) + tuple(
        (x[u]*y[N+j]) ^ (x[N+j]*y[v]) for j,(u,v) in enumerate(EDGES))


def convolution(left, right):
    out = Counter()
    for (x,a),(y,b) in product(left.items(),right.items()):
        out[tuple(u^v for u,v in zip(x,y))] += a*b
    return out


def coloring(t):
    out = Counter()
    for c in product(range(2**(2*t)),repeat=N):
        distinct = [c[u] != c[v] for u,v in EDGES]
        lifts = 2**(2*t*M-sum(distinct))
        for target in product(*(range(2) if d else (0,) for d in distinct)):
            out[target] += lifts
    return out


if __name__ == '__main__':
    one = Counter()
    for x,y in product(product(range(2),repeat=N+M),repeat=2):
        a,b = mul(x,y),mul(y,x)
        assert a[:N] == b[:N]
        one[tuple(u^v for u,v in zip(a[N:],b[N:]))] += 1
    f = one
    for t in (2,3):
        f = convolution(f,one)
        assert f == coloring(t)
        assert sum(f.values()) == 2**(2*t*(N+M))
        print('pairs',t,'nonempty fibers',len(f),'tuples',sum(f.values()))
    print('MULTIPLE_COMMUTATOR_FIBERS_OK')
