"""Exact finite checks of the point-permutation character identity for two-ring motion groups.

The all-parameter theorem is proved algebraically; these checks test its cycle signs,
coefficient bookkeeping and finite cases, not a replacement for the proof.
"""
from itertools import permutations, combinations
from math import comb


def cycles_of(p):
    n = len(p)
    seen = set()
    ans = []
    for i in range(n):
        if i in seen:
            continue
        block = []
        j = i
        while j not in seen:
            seen.add(j)
            block.append(j)
            j = p[j]
        ans.append(block)
    return ans


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def closed_form(p):
    f, e = [1], [1]
    for c in cycles_of(p):
        ell = len(c)
        ff = [1] + [0] * ell
        ff[ell] = 2 if ell % 2 else -2
        f = mul(f, ff)
        if ell % 2 == 0:
            ee = [1] + [0] * ell
            ee[ell] = -2
            e = mul(e, ee)
    n = len(p)
    f += [0]
    e += [0] * (n + 2 - len(e))
    out2 = [f[d] + e[d] + (2 * f[d-1] if d else 0)
            for d in range(n+2)]
    assert all(x % 2 == 0 for x in out2)
    return tuple(x // 2 for x in out2)


def direct_enumeration(p):
    n = len(p)
    cycles = cycles_of(p)
    d0 = [0] * (n+2)
    d1 = [0] * (n+1)
    for selected in range(1 << len(cycles)):
        blocks = [c for i,c in enumerate(cycles) if (selected >> i) & 1]
        supp = set(v for c in blocks for v in c)
        q = len(supp)
        sign = (-1) ** (q - len(blocks))
        # On tensor basis (0/1) for each included point, count vectors fixed
        # under graded permutation, and under composition with color complement.
        fixed_perm = 0
        fixed_flip = 0
        positions = sorted(supp)
        for assignment in range(1 << q):
            color = {v: (assignment >> i) & 1 for i,v in enumerate(positions)}
            if all(color[v] == color[p[v]] for v in positions):
                fixed_perm += 1
            if all(color[v] == 1-color[p[v]] for v in positions):
                fixed_flip += 1
        assert (fixed_perm + fixed_flip) % 2 == 0
        d0[q] += sign * (fixed_perm + fixed_flip) // 2
        d1[q] += sign * fixed_perm
    # H_d receives coinvariants at q=d and base H1 at q=d-1.
    return tuple(d0[d] + (d1[d-1] if d else 0) for d in range(n+2))


def run():
    tested = 0
    for n in range(0, 7):
        for p in permutations(range(n)):
            direct = direct_enumeration(p)
            closed = closed_form(p)
            assert direct == closed, (n, p, direct, closed)
            if p == tuple(range(n)):
                expected = [1] + [2**(d-1)*comb(n+1,d) for d in range(1, n+2)]
                assert list(closed) == expected, (n,closed,expected)
            tested += 1
    print('VERIFY_OK', tested, 'permutations in 0<=k<=6')


if __name__ == '__main__':
    run()
