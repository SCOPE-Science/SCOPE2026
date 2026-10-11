"""Exact rational finite spot checks for the cut-polytope John ellipsoid theorem.

Execute with Python >=3.9; only standard-library dependencies. Finite tests do
not replace the general switching and facet-redundancy proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations


def graph(n, edges):
    out = tuple(sorted({tuple(sorted(e)) for e in edges}))
    assert all(a != b and 0 <= a < n and 0 <= b < n for a, b in out)
    return n, out


def triangles(g):
    n, edges = g
    es = set(edges)
    return tuple(tuple(sorted((es1, es2, es3)))
                 for a, b, c in combinations(range(n), 3)
                 if all(tuple(sorted(x)) in es for x in ((a,b),(a,c),(b,c)))
                 for es1, es2, es3 in [(tuple(sorted((a,b))), tuple(sorted((a,c))), tuple(sorted((b,c))))])


def chordless_cycles(g):
    n, edges = g
    es = set(edges)
    adj = {v: set() for v in range(n)}
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    found = set()
    for start in range(n):
        def rec(path):
            u = path[-1]
            if len(path) >= 3 and start in adj[u]:
                ordered = path
                cycle_es = frozenset(tuple(sorted((ordered[i], ordered[(i+1)%len(ordered)]))) for i in range(len(ordered)))
                if len(cycle_es) == len(ordered):
                    induced = {e for e in es if e[0] in ordered and e[1] in ordered}
                    if induced == set(cycle_es):
                        found.add(cycle_es)
            if len(path) == n:
                return
            for v in adj[u]:
                if v <= start or v in path:
                    continue
                rec(path+[v])
        rec([start])
    return tuple(sorted(found, key=lambda x:(len(x),tuple(sorted(x)))))


def wheel(k):
    return graph(k+1, [(0,i) for i in range(1,k+1)] + [(i,i+1) for i in range(1,k)] + [(k,1)])


def book(p):
    return graph(p+2, [(0,1)] + [(0,i) for i in range(2,p+2)] + [(1,i) for i in range(2,p+2)])


def cactus_example():
    return graph(9, [(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,2),(5,6),(6,7),(7,8)])


def check(g, s, lambda_t):
    n, edges = g
    tri = triangles(g)
    index = {e:i for i,e in enumerate(edges)}
    assert set(s)==set(edges) and all(x>0 for x in s.values())
    assert set(lambda_t)==set(tri)
    for e in edges:
        assert s[e] <= F(1,4)
    for T in tri:
        assert sum((s[e] for e in T),F(0))<=F(1,4)
    # Exact stationarity and complementary slackness, sufficient by strict concavity.
    for T in tri:
        lam=lambda_t[T]; assert lam>=0
        if lam:
            assert sum((s[e] for e in T),F(0))==F(1,4)
    for e in edges:
        mu=F(1,s[e])-sum((lambda_t[T] for T in tri if e in T),F(0))
        assert mu>=0
        if s[e]<F(1,4):
            assert mu==0
    # Barahona--Mahjoub cycle and nontriangle-edge facets: exact containment
    # and contact classifications for each odd signed-cycle inequality.
    tri_edges=set(e for T in tri for e in T)
    cycles=chordless_cycles(g)
    facets=0; contacts=0
    for e in edges:
        if e not in tri_edges:
            assert s[e]==F(1,4)
            facets+=2; contacts+=2
    for C in cycles:
        k=len(C)
        left=sum((s[e] for e in C),F(0))
        right=F((k-2)*(k-2),4)
        assert left<=right
        expected=(k==3 and left==F(1,4)) or (k==4 and all(s[e]==F(1,4) for e in C))
        assert (left==right)==expected
        facets+=1 << (k-1)
        if expected: contacts+=1 << (k-1)
    # Independently verify every signed facet inequality on every cut for
    # these finite graphs, in integer arithmetic. Test all odd subsets F.
    signed = []
    for C in cycles:
        cc = tuple(index[e] for e in C)
        for signs in range(1 << len(cc)):
            if signs.bit_count()%2==1:
                signed.append((cc, signs, signs.bit_count()-1))
    for mask in range(1<<n):
        cut = tuple((mask>>a&1)^(mask>>b&1) for a,b in edges)
        for cc,signs,rhs in signed:
            val=sum((cut[j] if (signs>>i)&1 else -cut[j]) for i,j in enumerate(cc))
            assert val<=rhs
    # This finite enumeration corroborates Barahona--Mahjoub; it is not a
    # substitute for their general facet theorem or the analytic proof.
    return len(cycles),facets,contacts,(1<<n)


def run():
    count=0; facets=0; vertices=0
    for k in range(4,11):
        g=wheel(k)
        es=g[1]
        s={e:(F(1,16) if 0 in e else F(1,8)) for e in es}
        ls={T:F(8) for T in triangles(g)}
        out=check(g,s,ls)
        assert out[2]==4*k
        count+=1;facets+=out[1];vertices+=out[3]
    for p in range(1,11):
        g=book(p)
        es=g[1]
        s={e:(F(1,4*(2*p+1)) if e==(0,1) else F(p,4*(2*p+1))) for e in es}
        ls={T:F(4*(2*p+1),p) for T in triangles(g)}
        out=check(g,s,ls)
        assert out[2]==4*p
        count+=1;facets+=out[1];vertices+=out[3]
    for g in [graph(4,[(0,1),(1,2),(2,3)]),
              graph(4,[(0,1),(1,2),(2,3),(3,0)]),
              graph(5,[(i,(i+1)%5) for i in range(5)]),
              graph(4,list(combinations(range(4),2))),
              cactus_example()]:
        tri=triangles(g)
        s={e:(F(1,12) if any(e in T for T in tri) else F(1,4)) for e in g[1]}
        # K4 has four triangles per edge in two triangles; uniformly 1/12
        # is not feasible optimum. Supply exact K4 optimum s=1/12 under
        # each 3-edge constraint, with equal lambda=6 at each triangle.
        if len(g[1])==6 and len(tri)==4:
            ls={T:F(6) for T in tri}
        else:
            ls={T:F(12) for T in tri}
        out=check(g,s,ls)
        count+=1;facets+=out[1];vertices+=out[3]
    print('EXACT_VERIFY_PASS instances=%d cycle_facet_inequalities=%d tested_cuts=%d' %(count,facets,vertices))

if __name__=='__main__':
    run()
