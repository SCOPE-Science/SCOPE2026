#!/usr/bin/env python3
"""Independent exhaustive tests of proposed rook-graph open-neighborhood sequences.
Uses only Python's standard library; graph neighborhoods are constructed from adjacency.
"""
from functools import lru_cache
from math import factorial


def predict(m, n):
    return m + n - 2 + int(abs(m-n) == 1)


def exception_count(a):
    odd_prod = 1
    for j in range(1, a):
        odd_prod *= 2*j + 1
    return factorial(a+1)*factorial(a)**2*odd_prod


def examine(m, n, classify=False):
    vertices = [(a,b) for a in range(m) for b in range(n)]
    vcount = len(vertices)
    nbr = []
    for u in vertices:
        nbr.append(sum(1 << j for j,v in enumerate(vertices)
                       if u != v and (u[0] == v[0] or u[1] == v[1])))
    full = (1 << vcount) - 1

    @lru_cache(maxsize=None)
    def solve(dominated, chosen):
        best = 0
        ways = 1
        for i, ni in enumerate(nbr):
            if chosen & (1 << i) or not (ni & (full ^ dominated)):
                continue
            length, count = solve(dominated | ni, chosen | (1 << i))
            if length + 1 > best:
                best, ways = length+1, count
            elif length + 1 == best:
                ways += count
        if best == 0:
            assert dominated == full
        return best, ways

    best, count = solve(0,0)
    assert best == predict(m,n), (m,n,best,predict(m,n))
    if abs(m-n) == 1:
        assert count == exception_count(min(m,n)), (m,n,count,exception_count(min(m,n)))

    if classify:
        assert n == m+1
        a = m
        seen = [0]
        def examine_path(path):
            pref = [vertices[j] for j in path[:a]]
            assert len(set(x for x,y in pref)) == a
            assert len(set(y for x,y in pref)) == a
            surplus = set(range(n)) - {y for x,y in pref}
            assert len(surplus) == 1
            special = vertices[path[a]]
            assert special[1] in surplus
            assert special[0] in {x for x,y in pref}
            used_rows = {special[0]}
            used_cols = {special[1]}
            for x,y in pref:
                if x == special[0]:
                    used_cols.add(y)
            for j in path[a+1:]:
                x,y = vertices[j]
                choices = [(i,k) for i,k in pref if i not in used_rows]
                matches = [(i,k) for i,k in choices if (x==i and y in used_cols)
                           or (y==k and x in used_rows)]
                assert len(matches) == 1, (path,x,y,matches)
                used_rows.add(matches[0][0]); used_cols.add(matches[0][1])
            assert len(used_rows)==a and len(used_cols)==n
            seen[0] += 1

        def walk(dominated, chosen, path):
            remaining,_ = solve(dominated, chosen)
            if remaining==0:
                examine_path(path)
                return
            for i,ni in enumerate(nbr):
                if chosen & (1<<i) or not (ni & (full ^ dominated)):
                    continue
                if 1+solve(dominated|ni,chosen|(1<<i))[0]==remaining:
                    walk(dominated|ni,chosen|(1<<i),path+[i])
        walk(0,0,[])
        assert seen[0]==count
        print(f'CLASSIFICATION_OK m={m} n={n} sequences={seen[0]}',flush=True)
    print(f'OK m={m} n={n} maximum={best} count={count} states={solve.cache_info().currsize}',flush=True)


def main():
    instances = [(2,n) for n in range(2,8)] + [(3,n) for n in range(3,7)] + [(4,4),(4,5)]
    for m,n in instances:
        examine(m,n,classify=(n==m+1 and m<=3))
    print('VERIFY_OK',flush=True)

if __name__=='__main__':
    main()
