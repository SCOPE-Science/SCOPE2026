"""Self-contained finite checks for monogenic power-semigroup host bounds.
No external dependencies. Run with: python monogenic_host_checker.py
"""
from itertools import product


def subset_powers(mul, subset):
    n = len(mul)
    seen = {}
    power = frozenset(subset)
    first = 1
    while power not in seen:
        seen[power] = first
        power = frozenset(mul[x][y] for x in power for y in subset)
        first += 1
    return seen[power], first - seen[power]


def group_table(dims):
    vertices = list(product(*(range(d) for d in dims)))
    rank = {v: i for i, v in enumerate(vertices)}
    return [[rank[tuple((a+b) % d for a,b,d in zip(x,y,dims))]
             for y in vertices] for x in vertices]


def check_all_subsets(dims):
    t = group_table(dims)
    n = len(t)
    observed = set()
    equalities = []
    for mask in range(1,1<<n):
        A = [i for i in range(n) if mask >> i & 1]
        m, r = subset_powers(t,A)
        lower = r if m==1 else (m+1)*r
        assert lower <= n, (dims,A,m,r,lower)
        observed.add((m,r))
        if lower == n and m>=2:
            # Equality criterion: after subtracting a generator,
            # the difference set must have exactly two points.
            g=A[0]
            inv = next(x for x in range(n) if t[g][x] == 0)
            D={t[a][inv] for a in A}
            assert len(D)==2, (dims,A,m,r,D)
            equalities.append((m,r,tuple(A)))
    return len(observed), len(equalities)


def check_constructive():
    for m in range(1,12):
        for r in range(1,12):
            N = r if m==1 else (m+1)*r
            t = [[(i+j)%N for j in range(N)] for i in range(N)]
            A = [1%N] if m==1 else [1, (1+r)%N]
            got = subset_powers(t,A)
            assert got==(m,r), (m,r,N,A,got)
    return 121


def main():
    count=0
    for dims in [(n,) for n in range(1,13)]+[(2,2),(2,3),(2,4),(3,3),(2,2,2)]:
        ntypes, nequal=check_all_subsets(dims)
        count+=1
        print('GROUP',dims,'types',ntypes,'minimum-order non-group examples',nequal)
    print('CONSTRUCTIONS_VERIFIED', check_constructive())
    print('VERIFY_OK',count,'groups')

if __name__=='__main__':
    main()
