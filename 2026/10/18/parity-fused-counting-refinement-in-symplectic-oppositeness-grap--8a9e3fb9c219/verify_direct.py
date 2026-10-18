"""Direct binary symplectic geometry and individualized color refinement.
Run: python verify_direct.py  (standard library only)
"""
from collections import defaultdict, Counter
from math import prod


def pairing(x, y, n):
    mask = (1 << n) - 1
    return (((x & mask) & (y >> n)).bit_count() +
            (((x >> n) & mask) & (y & mask)).bit_count()) % 2


def lagrangians(n):
    full = 1 << (2*n)
    level = {1}  # bit-vector for the zero subspace
    for rank in range(1, n+1):
        new = set()
        for sub in level:
            vecs = [v for v in range(full) if (sub >> v) & 1]
            for v in range(1, full):
                if (sub >> v) & 1 or any(pairing(v, u, n) for u in vecs):
                    continue
                ext = sub
                for u in vecs:
                    ext |= 1 << (v ^ u)
                new.add(ext)
        level = new
    expected = prod(2**j + 1 for j in range(1, n+1))
    assert len(level) == expected, (n, len(level), expected)
    return sorted(level)


def check(n):
    subs = lagrangians(n)
    N = len(subs)
    A = sum(1 << u for u in range(1 << n))
    assert A in subs
    s = [(S & A).bit_count().bit_length()-1 for S in subs]
    neigh = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if (subs[i] & subs[j]) == 1:
                neigh[i].append(j)
                neigh[j].append(i)
    assert set(map(len, neigh)) == {2**(n*(n+1)//2)}
    colors = [1 if S == A else 0 for S in subs]
    observed = {}
    for r in range(1, 6):
        sig = []
        for i in range(N):
            hist = tuple(sorted(Counter(colors[j] for j in neigh[i]).items()))
            sig.append((colors[i], hist))
        canonical = {x:k for k,x in enumerate(sorted(set(sig)))}
        colors = [canonical[x] for x in sig]
        bycolor = defaultdict(set)
        for c, rank in zip(colors, s):
            bycolor[c].add(rank)
        observed[r] = tuple(sorted(tuple(sorted(v)) for v in bycolor.values()))
        if r == 1:
            assert (len(bycolor) == 3), observed
        if r == 2:
            if n == 3:assert len(bycolor) == 3
            if n == 4:assert len(bycolor) == 4
        if r == 3:
            if n == 4:assert len(bycolor) == 5
    if n == 2:
        target = ((0,), (1,), (2,))
    elif n == 3:
        target = ((0,), (1, 2), (3,))
    else:
        target = tuple((t,) for t in range(5))
    assert observed[5] == target, (n, observed)
    print('n=%d  vertices=%d  degree=%d  rounds1-3=%s  stable=%s PASS' %
          (n, N, 2**(n*(n+1)//2),
           [len(observed[j]) for j in (1,2,3)], observed[5]))


if __name__ == '__main__':
    for n in (2, 3, 4):
        check(n)
    print('DIRECT_VERIFICATION_PASS')
