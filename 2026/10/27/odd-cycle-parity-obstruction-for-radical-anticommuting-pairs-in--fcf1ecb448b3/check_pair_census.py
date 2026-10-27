#!/usr/bin/env python3
"""Independent finite-field tests for two radical-pair counts on kQ/J^3.
No external dependencies. Coefficients are encoded as integers; GF(4) uses x^2+x+1.
"""
from itertools import product


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def neg(a, q):
    return a if q == 4 else (-a) % q


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    ans = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & 1 and (b >> j) & 1:
                ans ^= 1 << (i + j)
    if ans & 8:
        ans ^= 0b1110  # x^3=x^2+x in GF(4)
    if ans & 4:
        ans ^= 0b111  # x^2=x+1 in GF(4)
    return ans


def transition_graph(arrows):
    n = len(arrows)
    pairs = [(i,j) for i,(s,t) in enumerate(arrows)
             for j,(u,v) in enumerate(arrows) if t == u]
    adj = [set() for _ in range(n)]
    for i,j in pairs:
        adj[i].add(j)
        adj[j].add(i)
    return pairs, adj


def factors(arrows, q):
    pairs, adj = transition_graph(arrows)
    total_plus = total_minus = 0
    n = len(arrows)
    for mask in range(1 << n):
        unseen = set(i for i in range(n) if (mask >> i) & 1)
        factor_plus = 1
        count = bin(mask).count('1')
        while unseen:
            root = unseen.pop()
            col = {root: 0}
            todo = [root]
            bip = True
            while todo:
                i = todo.pop()
                for j in adj[i]:
                    if j not in col and (mask >> j) & 1:
                        col[j] = 1 - col[i]
                        unseen.discard(j)
                        todo.append(j)
                    elif (mask >> j) & 1 and col.get(j, 1-col[i]) == col[i]:
                        bip = False
            factor_plus *= q + 1 if q % 2 == 0 or bip else 2
        # Independently compute number of connected components for commuting pairs.
        leftover = set(i for i in range(n) if (mask >> i) & 1)
        cc = 0
        while leftover:
            cc += 1
            walk = [leftover.pop()]
            while walk:
                i = walk.pop()
                for j in adj[i] & leftover:
                    leftover.remove(j)
                    walk.append(j)
        factor_minus = (q + 1) ** cc
        total_plus += (q-1)**count * factor_plus
        total_minus += (q-1)**count * factor_minus
    scale = q**(2*len(pairs))
    return total_plus*scale, total_minus*scale


def brute(arrows, q):
    pairs, _ = transition_graph(arrows)
    plus = minus = 0
    n = len(arrows)
    for v in product(range(q*q), repeat=n):
        ab = [x % q for x in v]
        bb = [x // q for x in v]
        jplus = jminus = True
        for i,j in pairs:
            z = mul(ab[i],bb[j],q)
            w = mul(bb[i],ab[j],q)
            if add(z,w,q):
                jplus = False
            if add(z,neg(w,q),q):
                jminus = False
            if not jplus and not jminus:
                break
        plus += jplus
        minus += jminus
    scale = q**(2*len(pairs))
    return plus*scale, minus*scale


def run():
    cases = [
        ('one_loop',[(0,0)],[2,3,4,5]),
        ('two_loops',[(0,0),(0,0)],[2,3,4]),
        ('two_parallel',[(0,1),(0,1)],[2,3,4]),
        ('linear_path',[(0,1),(1,2)],[2,3,4,5]),
        ('two_cycle',[(0,1),(1,0)],[2,3,4]),
        ('oriented_triangle',[(0,1),(1,2),(2,0)],[2,3,4,5]),
        ('acyclic_odd_transition',[(0,1),(1,2),(2,4),(1,3),(3,5),(5,4),(4,6)],[2]),
    ]
    checked = 0
    for name, arrows, sizes in cases:
        for q in sizes:
            expected = factors(arrows,q)
            direct = brute(arrows,q)
            assert direct == expected, (name,q,direct,expected)
            checked += 1
            print('PASS',name,q,'anticommuting',direct[0],'commuting',direct[1])
    a=[(0,1),(1,2),(2,0)]
    for q in [3,5]:
        anti,comm=factors(a,q)
        assert comm-anti==q**6*(q-1)**4
    a=[(0,1),(1,2),(2,4),(1,3),(3,5),(5,4),(4,6)]
    for q in [3,5]:
        anti,comm=factors(a,q)
        assert comm-anti==q**14*(q-1)**8
    print('QUIVER_ANTICOMMUTING_PARITY_OK',checked,'direct exhaustive cases; two algebraic odd-cycle checks')

if __name__=='__main__':
    run()
