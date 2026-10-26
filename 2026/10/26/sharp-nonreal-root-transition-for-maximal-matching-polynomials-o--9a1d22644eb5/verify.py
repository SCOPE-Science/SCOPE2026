"""Exact verification of maximal-matching roots in triangle coronas.

Standalone Python 3; only Python's standard library is required.
"""
from functools import lru_cache
from collections import Counter
from math import comb


def core_coefficients(n, edges):
    """Counts by number of matched core edges via a separate subset DP."""
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    @lru_cache(None)
    def local_weight(vertices):
        if vertices == 0:
            return 1
        bit = vertices & -vertices
        v = bit.bit_length() - 1
        others = vertices ^ bit
        neighbors = others & adj[v]
        # Choosing one of two spokes contributes 2; choosing the
        # private edge forces every adjacent core vertex to use a spoke.
        return (2 * local_weight(others)
                + (1 << neighbors.bit_count()) * local_weight(others ^ neighbors))

    ans = [0] * (n // 2 + 1)

    def matchings(available, free, k):
        if not available:
            ans[k] += local_weight(free)
            return
        bit = available & -available
        v = bit.bit_length() - 1
        rest = available ^ bit
        matchings(rest, free | bit, k)
        choices = rest & adj[v]
        while choices:
            second = choices & -choices
            choices ^= second
            matchings(rest ^ second, free, k + 1)

    matchings((1 << n) - 1, 0, 0)
    return ans


def discriminant(a):
    degree = len(a) - 1
    while degree > 0 and a[degree] == 0:
        degree -= 1
    if degree < 2:
        return 1
    if degree == 2:
        p, q, r = a[:3]
        return q * q - 4 * p * r
    assert degree == 3
    p, q, r, s = a[:4]
    return (q*q*r*r - 4*p*r**3 - 4*q**3*s
            - 27*p*p*s*s + 18*p*q*r*s)


def corona_edges(n, edges):
    """Vertices 0,...,n-1 are core; 2n private vertices form n edges."""
    result = list(edges)
    for v in range(n):
        a = n + 2*v
        b = a + 1
        result.extend([(v, a), (v, b), (a, b)])
    return result


def direct_maximal_matching_counts(n, edges):
    """Enumerate matchings in the actual 3n-vertex graph, no core formula."""
    e = corona_edges(n, edges)
    N = 3 * n
    adj = [0] * N
    for u, v in e:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    out = Counter()

    def rec(avail, unsat, edges_used):
        if not avail:
            for v in range(N):
                if (unsat >> v) & 1 and adj[v] & unsat:
                    return
            out[edges_used] += 1
            return
        bit = avail & -avail
        v = bit.bit_length() - 1
        rest = avail ^ bit
        rec(rest, unsat | bit, edges_used)
        opts = rest & adj[v]
        while opts:
            second = opts & -opts
            opts ^= second
            rec(rest ^ second, unsat, edges_used + 1)

    rec((1 << N) - 1, 0, 0)
    return out


def spider_edges(r):
    # center=0, internal vertices 1..r, terminal vertices r+1..2r
    return [(0, i) for i in range(1, r+1)] + [(i, i+r) for i in range(1, r+1)]


def formula_spider(r):
    # 2(8+t)^r+(6+t)^r+3rt(8+t)^{r-1}
    return [2*comb(r, k)*8**(r-k) + comb(r,k)*6**(r-k)
            + (3*r*comb(r-1,k-1)*8**(r-k) if k>=1 else 0)
            for k in range(r+1)]


def test():
    # Exhaustively test all 2^15 labelled simple graphs on six vertices.
    # Smaller graphs are covered by adjoining isolated core vertices:
    # each isolated vertex multiplies the normalized polynomial by 3.
    n = 6
    possible = [(u,v) for u in range(n) for v in range(u+1,n)]
    degree_counts = Counter()
    delta_zero = 0
    min_delta = None
    checksum = 0
    for mask in range(1 << len(possible)):
        E = [e for j,e in enumerate(possible) if (mask >> j) & 1]
        a = core_coefficients(n, E)
        d = len(a)-1
        while d>0 and a[d]==0:
            d-=1
        degree_counts[d] += 1
        delta = discriminant(a)
        assert delta>=0, (mask, E, a, delta)
        if delta==0:delta_zero+=1
        if min_delta is None or delta<min_delta:min_delta=delta
        checksum = (checksum*1000003+sum((j+1)*a[j] for j in range(len(a)))) % (2**64)
    assert dict(degree_counts)=={0:1,1:191,2:7753,3:24823}
    assert delta_zero==160
    assert checksum==903070490435883371
    print('ALL_6_VERTEX_GRAPHS:',1<<len(possible),'degree_distribution:',sorted(degree_counts.items()),
          'zero_discriminants:',delta_zero,'minimum_discriminant:',min_delta, 'checksum:',checksum)

    # Direct enumeration of matchings in actual corona graphs, not the
    # symbolic core decomposition, including the 21-vertex witness.
    probes = [
        (1, []),
        (2, [(0,1)]),
        (3, [(0,1),(1,2)]),
        (4, [(0,1),(1,2),(2,3)]),
        (7, spider_edges(3)),
    ]
    for n,E in probes:
        derived=core_coefficients(n,E)
        direct=direct_maximal_matching_counts(n,E)
        expected={n+k:value for k,value in enumerate(derived) if value}
        assert dict(direct)==expected, (n,derived,direct)
        print('DIRECT_MAXIMAL_MATCHINGS_OK:',n,'edges',len(E),'coefficients',derived)

    # Every labelled graph with four core vertices is also checked directly.
    pairs = [(u,v) for u in range(4) for v in range(u+1,4)]
    for mask in range(1 << len(pairs)):
        E = [pair for i,pair in enumerate(pairs) if (mask>>i)&1]
        actual = direct_maximal_matching_counts(4, E)
        expected = {4+i:a for i,a in enumerate(core_coefficients(4,E)) if a}
        assert dict(actual)==expected, (mask,actual,expected)
    print('ALL_4_VERTEX_GRAPHS_DIRECT_OK:',1<<len(pairs))

    for r in range(1,9):
        actual=core_coefficients(2*r+1,spider_edges(r))
        expected=formula_spider(r)
        assert actual==expected, (r,actual,expected)
    assert formula_spider(3)==[1240,1068,210,12]
    assert discriminant(formula_spider(3))==-13023936
    print('SPIDER_FORMULA_OK: r=1..8; cubic_discriminant=-13023936')
    print('VERIFY_OK')

if __name__=='__main__':
    test()
