"""Independent exact-integer Apéry verification of four-term repunit semigroups.

Requires Python 3 standard library only. Finite checks supplement, not replace,
the symbolic theorem.
"""
import heapq


def apery_dijkstra(gens):
    a = gens[0]
    inf = 10**100
    d = [inf] * a
    d[0] = 0
    queue = [(0, 0)]
    while queue:
        val, r = heapq.heappop(queue)
        if val != d[r]:
            continue
        for g in gens[1:]:
            r2, v2 = (r + g) % a, val + g
            if v2 < d[r2]:
                d[r2] = v2
                heapq.heappush(queue, (v2, r2))
    return d


def count_greedy(t, b):
    q = b + 1
    h = b * b + b + 1
    z, rem = divmod(t, h)
    y, x = divmod(rem, q)
    return z + y + x


def check_one(a, b, r):
    q = b + 1
    h = b * b + b + 1
    assert a >= h and a % h == r
    reps = [1, q, h]
    c = (b - 1) * a + 1
    gens = [a] + [a + c * t for t in reps]
    d = apery_dijkstra(gens)
    assert all(d[(c * t) % a] == a * count_greedy(t, b) + c * t
               for t in range(a))
    actual = sorted({w-a for w in d
                     if all(w-a+g >= d[(w-a+g) % a] for g in gens[1:])})
    Q, rem = divmod(a, h)
    assert rem == r
    if r == 0:
        tips = [(Q-1) * h + h-2, (Q-1) * h + h-1]
    elif r == 1:
        tips = [(Q-1) * h + h-2, (Q-1) * h + h-1, Q * h]
    elif r == q:
        tips = [(Q-1) * h + h-2, Q * h + b]
    else:
        raise ValueError('unrequested residue case')
    expected = sorted(a * count_greedy(t, b) + c * t - a for t in tips)
    assert actual == expected, (a,b,r,actual,expected)
    if r == 0:
        assert actual == [actual[-1]-1, actual[-1]]
    if r == 1:
        assert actual == [actual[-1]-2, actual[-1]-1, actual[-1]]
    if r == q:
        assert actual == [actual[-1]-(b*b*a+b+2), actual[-1]]
    return len(actual)


def main():
    generic = 0
    for b in range(2, 13):
        h = b*b+b+1
        for Q in range(1, 11):
            for r in (0, 1, b+1):
                if h*Q+r > 13000:
                    continue
                check_one(h*Q+r, b, r)
                generic += 1
    repunit = 0
    for b in range(2, 14):
        for n in range(5, 12):
            a = sum(b**i for i in range(n))
            if a > 40000:
                break
            r = {0: 0, 1: 1, 2: b+1}[n % 3]
            check_one(a, b, r)
            repunit += 1
    print('PASS: %d generic residue cases, %d consecutive-repunit cases; all exact Apéry and pseudo-Frobenius comparisons matched.' % (generic, repunit))


if __name__ == '__main__':
    main()
