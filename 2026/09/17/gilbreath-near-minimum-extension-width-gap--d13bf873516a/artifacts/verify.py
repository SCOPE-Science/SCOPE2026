from functools import lru_cache
from collections import Counter

def preimage(e, T):
    out = set()
    for t in T:
        out.add(e + t)
        if t <= e:
            out.add(e - t)
    return tuple(sorted(out))

@lru_cache(maxsize=None)
def distances(e):
    T = (1,)
    for x in reversed(e):
        T = preimage(x, T)
    return T

def width(e):
    D = distances(e)
    return 2 * len(D) - (1 if 0 in D else 0)

def child(e, d):
    r = d
    ans = [r]
    for x in e:
        r = abs(r - x)
        ans.append(r)
    assert ans[-1] == 1
    return tuple(ans)

def shape_ok(e, w):
    middle = e[1:-1]
    if w == 5:
        return e[0] == 2 and all(x == 0 for x in middle)
    if w == 7:
        return e[0] == 2 and middle.count(2) == 1 and all(x in (0, 2) for x in middle)
    if w == 9:
        case1 = e[0] == 4 and middle.count(2) == 1 and all(x in (0, 2) for x in middle)
        case2 = e[0] == 2 and middle.count(2) == 2 and all(x in (0, 2) for x in middle)
        return case1 or case2
    return False

def generate(max_n=10):
    states = [(3, (1,))]  # last term and right anti-diagonal for (2,3)
    rows = {}
    for n in range(3, max_n + 1):
        nxt = []
        for last, e in states:
            for d in distances(e):
                if d > 0:
                    nxt.append((last + d, child(e, d)))
        states = nxt
        rows[n] = states
    return rows

rows = generate(10)
for n, states in rows.items():
    low = Counter()
    for _, e in states:
        A = sum(e)
        w = width(e)
        assert w >= min(A + 2, 10)
        assert (w <= 9) == (A <= 7)
        if w <= 9:
            assert w == A + 2
            assert shape_ok(e, w)
            low[w] += 1
    print(n, len(states), dict(sorted(low.items())))
