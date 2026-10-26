"""Finite replay for the three-extension maximin distance on bidirected paths.

Run: python checker.py
The arbitrary-length result follows from the symbolic proof; this program
checks its finite base cases, insertion construction and finite instances.
"""
from itertools import combinations

BASE = {
    4: ('BC', 'A', 'C', 'AB'),
    5: ('BC', 'A', 'C', 'B', 'AC'),
    6: ('C', 'AB', 'C', 'B', 'A', 'BC'),
    7: ('C', 'AB', '', 'BC', 'A', 'B', 'AC'),
    8: ('BC', 'A', 'C', 'B', 'A', 'C', 'B', 'AC'),
    9: ('C', 'AB', 'C', 'B', 'A', 'BC', 'A', 'B', 'AC'),
}

def stable(column, letter):
    n = len(column)
    bits = [letter in c for c in column]
    return all(not (bits[i] and bits[i + 1]) for i in range(n - 1)) and all(
        bits[i] or (i > 0 and bits[i - 1]) or (i + 1 < n and bits[i + 1])
        for i in range(n)
    )

def distances(column):
    return tuple(sum((x in s) != (y in s) for s in column) for x, y in (
        ('A', 'B'), ('A', 'C'), ('B', 'C')))

def witness(n):
    if n in BASE:
        return BASE[n]
    if n < 7:
        raise ValueError('no infinite-family construction')
    r = 7 + (n - 7) % 3
    s = list(BASE[r])
    while len(s) < n:
        # The same location remains valid after every three-position insertion.
        after = s[5]
        if after == 'B':
            block = ('B', 'C', 'A')
        elif after in ('C', 'BC'):
            block = ('C', 'B', 'A')
        else:
            raise AssertionError(after)
        s[5:5] = block
    return tuple(s)

def independent_dominating_masks(n):
    a = []
    for x in range(1 << n):
        if x & (x << 1):
            continue
        if all(
            (x >> i & 1) or (i > 0 and (x >> (i-1) & 1))
            or (i + 1 < n and (x >> (i+1) & 1))
            for i in range(n)
        ):
            a.append(x)
    return a

def brute_optimum(n):
    a = independent_dominating_masks(n)
    if len(a) < 3:
        return None
    ds = {(i,j): (a[i] ^ a[j]).bit_count() for i in range(len(a)) for j in range(i+1, len(a))}
    best = 0
    for i,j,k in combinations(range(len(a)),3):
        best = max(best, min(ds[i,j],ds[i,k],ds[j,k]))
    return best

def expected(n):
    if n <= 3: return None
    if n == 6: return 3
    return 2*n//3

def main():
    assert [len(independent_dominating_masks(n)) for n in range(1,7)] == [1,2,2,3,4,5]
    count = 0
    for n in range(4,21):
        exact = brute_optimum(n)
        assert exact == expected(n), (n, exact, expected(n))
        count += 1
    for n in range(4,601):
        if n == 6: continue
        c = witness(n)
        assert len(c) == n
        assert all(stable(c,z) for z in 'ABC'), n
        assert min(distances(c)) == expected(n), (n, distances(c))
        count += 1
    assert len(independent_dominating_masks(6)) == 5
    assert brute_optimum(6) == 3
    print('ALL_CHECKS_OK', 'independent finite instances 4..20;',
          'explicit witnesses 4..600;', 'checked groups',count)

if __name__ == '__main__':
    main()
