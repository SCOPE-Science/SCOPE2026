"""Exact finite tests for two-valued mixed-item EF1 restoration.

Run with Python 3.8 or later; uses no third-party packages.
Finite tests support, but do not replace, the all-size mathematical proof.
"""
from itertools import product
from functools import lru_cache

@lru_cache(maxsize=None)
def compositions(total, parts):
    if parts == 1:
        return ((total,),)
    return tuple((i,) + t for i in range(total + 1)
                 for t in compositions(total - i, parts - 1))


def values(state, a, b):
    return tuple(a * g - b * c for g, c in state)


def envy(state, a, b):
    """Signed EF1 shortfall, positive exactly for a genuine EF1 violation."""
    s = values(state, a, b)
    n = len(state)
    return tuple(tuple(0 if i == j else
             s[j] - s[i] - max(b if state[i][1] else 0,
                                  a if state[j][0] else 0)
             for j in range(n)) for i in range(n))


def solve(state, a, b):
    current = tuple(tuple(t) for t in state)
    n = len(current)
    initial = current
    initial_chore = current[0][1]
    initial_else_goods = sum(x[0] for x in current[1:])
    iterations = 0
    while True:
        E = envy(current, a, b)
        assert all(E[i][j] <= 0 for i in range(1, n) for j in range(n))
        if all(E[0][j] <= 0 for j in range(n)):
            break
        s = values(current, a, b)
        donor = max(range(1, n), key=lambda j: (s[j], -j))
        nxt = [list(z) for z in current]
        if nxt[0][1]:
            nxt[0][1] -= 1
            nxt[donor][1] += 1
        else:
            assert nxt[donor][0] > 0
            nxt[donor][0] -= 1
            nxt[0][0] += 1
        nxt = tuple(map(tuple, nxt))
        F = envy(nxt, a, b)
        assert all(F[i][j] <= 0 for i in range(1, n) for j in range(n)), (a,b,current,nxt)
        assert all(F[0][j] <= E[0][j] for j in range(1,n)), (a,b,current,nxt)
        assert values(nxt, a, b)[0] > s[0]
        current = nxt
        iterations += 1
        assert iterations <= initial_chore + initial_else_goods
    if a == b:
        s = values(initial, a, b)
        target = (sum(s) // (a*n))
        expected = target - s[0] // a
        assert iterations == expected, (initial, current, expected, iterations)
    return iterations


def main():
    cases = 0
    steps = 0
    two_direction = 0
    for a,b in ((1,1),(1,2),(2,1),(2,3),(3,2),(1,5),(5,1)):
        for n in (2,3,4):
            for m in range(2,9):
                for G in range(1,m):
                    C = m-G
                    for gs in compositions(G,n):
                        for cs in compositions(C,n):
                            state=tuple(zip(gs,cs))
                            E=envy(state,a,b)
                            if all(E[i][j]<=0 for i in range(1,n) for j in range(n)) and any(E[0][j]>0 for j in range(1,n)):
                                t=solve(state,a,b)
                                assert t>0
                                cases+=1
                                steps+=t
                                if state[0][1] and t>state[0][1]:
                                    two_direction+=1
    sample=((0,1),(3,0),(2,0))
    assert values(sample,2,1)==(-1,6,4)
    assert solve(sample,2,1)==2
    print('PASS: all finite states tested; near-EF1 cases',cases,
          'total verified transfers',steps,'both-direction candidates',two_direction)

if __name__=='__main__':
    main()
