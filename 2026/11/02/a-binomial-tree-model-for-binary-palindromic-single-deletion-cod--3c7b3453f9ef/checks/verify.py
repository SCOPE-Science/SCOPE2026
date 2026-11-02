"""Independent finite checks for palindrome-restricted binary deletion codes.
Run: python3 checks/verify.py
Standard library only. Checks are finite corroboration, not an infinite proof.
"""
from itertools import combinations


def pal(half, even):
    return half + (half[::-1] if even else half[-2::-1])


def descendants(word):
    return {word[:j] + word[j + 1:] for j in range(len(word))}


def words(m):
    return [format(i, '0%db' % m) for i in range(1 << m)]


def predicted_edges(m):
    out = set()
    for half in words(m):
        for r in range(1, m + 1):
            tail = half[-r:]
            if all(tail[j] != tail[j + 1] for j in range(r - 1)):
                other = half[:-r] + ''.join('0' if c == '1' else '1' for c in tail)
                out.add(tuple(sorted((half, other))))
    return out


def actual_edges(m, even):
    vv = words(m)
    shadows = {u: descendants(pal(u, even)) for u in vv}
    return {(u, v) for u, v in combinations(vv, 2)
            if not shadows[u].isdisjoint(shadows[v])}


def dp_max_sets(vv, edges, anchor):
    adj = {v: [] for v in vv}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def visit(v, prev):
        data = [visit(w, v) for w in adj[v] if w != prev]
        # (maximal size, count) conditional on v omitted/included
        val0 = sum(max(t[0][0], t[1][0]) for t in data)
        count0 = 1
        for d0, d1 in data:
            if d0[0] > d1[0]: count0 *= d0[1]
            elif d0[0] < d1[0]: count0 *= d1[1]
            else: count0 *= (d0[1] + d1[1])
        val1 = 1 + sum(t[0][0] for t in data)
        count1 = 1
        for d0, d1 in data: count1 *= d0[1]
        return ((val0, count0), (val1, count1))

    d0, d1 = visit(anchor, None)
    top = max(d0[0], d1[0])
    return top, (d0[1] if d0[0] == top else 0) + (d1[1] if d1[0] == top else 0), (d1[1] if d1[0] == top else 0)


def count_formula(m):
    factor = 1
    for j in range(1, m):
        factor *= j ** (2 ** (m - 1 - j))
    return (m + 1) * factor, factor


def test():
    for m in range(1, 9):
        vv = words(m)
        calc = actual_edges(m, even=False)
        pred = predicted_edges(m)
        assert calc == pred, ('odd edge criterion', m, calc ^ pred)
        assert len(calc) == (1 << m) - 1
        # A connected graph with n-1 edges is a tree.
        adj = {v: [] for v in vv}
        for a, b in calc: adj[a].append(b); adj[b].append(a)
        seen, todo = set(), [vv[0]]
        while todo:
            v = todo.pop()
            if v not in seen:
                seen.add(v)
                todo.extend(adj[v])
        assert len(seen) == len(vv)
        alt = ''.join('01'[i % 2] for i in range(m))
        optimum, num, contain = dp_max_sets(vv, calc, alt)
        expected, expected_contain = count_formula(m)
        assert optimum == (1 << (m - 1)), (m, optimum)
        assert num == expected, (m, num, expected)
        assert contain == expected_contain, (m, contain, expected_contain)
        even_edges = actual_edges(m, even=True)
        assert not even_edges, ('even palindromes conflict', m, even_edges)
        print('m=%d odd_n=%d alpha=%d max_codes=%d even_n=%d even_alpha=%d' %
              (m, 2 * m - 1, optimum, num, 2 * m, len(vv)))
    # Brute-force all possible codebooks for small odd lengths; no tree DP here.
    for m in range(1, 5):
        vv = words(m)
        edges = actual_edges(m, even=False)
        best, number = 0, 0
        for bits in range(1 << len(vv)):
            chosen = {vv[j] for j in range(len(vv)) if bits >> j & 1}
            if all(not (u in chosen and v in chosen) for u, v in edges):
                size = len(chosen)
                if size > best: best, number = size, 1
                elif size == best: number += 1
        assert best == (1 << (m - 1)) and number == count_formula(m)[0]
    print('VERIFY_OK')

if __name__ == '__main__':
    test()
