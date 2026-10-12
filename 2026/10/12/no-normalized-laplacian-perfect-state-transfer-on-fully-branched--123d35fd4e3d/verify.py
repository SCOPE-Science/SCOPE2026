"""Exact finite checks of the two independent obstructions in a depth-two tree."""
from fractions import Fraction
from itertools import product


def verify_profile(p):
    m = len(p)
    edges = []
    root = 0
    hubs = list(range(1, m + 1))
    leaves = []
    next_vertex = m + 1
    for i, count in enumerate(p):
        edges.append((root, hubs[i]))
        leaf_group = list(range(next_vertex, next_vertex + count))
        next_vertex += count
        for v in leaf_group:
            edges.append((hubs[i], v))
        leaves.append(leaf_group)
    n = next_vertex
    deg = [0] * n
    N = [[] for _ in range(n)]
    for u,v in edges:
        deg[u] += 1; deg[v] += 1
        N[u].append(v); N[v].append(u)
    assert deg[root] == m
    assert all(deg[hubs[i]] == p[i] + 1 for i in range(m))
    assert all(deg[v] == 1 for group in leaves for v in group)
    # S f = 0 exactly, with f=D^(1/2)z; A z=0 is an exact rational test.
    z = [Fraction(0)] * n
    z[root] = Fraction(1)
    for i,group in enumerate(leaves):
        for v in group:
            z[v] = Fraction(-1,p[i])
    for u in range(n):
        assert sum((z[v] for v in N[u]),Fraction(0)) == 0
    # Each sibling pair has a nonzero common vector in the H=1 eigenspace.
    sibling_pairs=0
    for group in leaves:
        for j in range(len(group)):
            for k in range(j+1,len(group)):
                u,v=group[j],group[k]
                assert z[u]+z[v] != 0
                sibling_pairs += 1
    # Root and a degree-compatible intermediate hub have distinct 2-step moments.
    for i,h in enumerate(hubs):
        if deg[root] == deg[h]:
            root2=sum((Fraction(1,m*deg[x]) for x in N[root]), Fraction(0))
            hub2=sum((Fraction(1,deg[h]*deg[x]) for x in N[h]), Fraction(0))
            assert root2 <= Fraction(1,2)
            assert hub2 >= Fraction(3,4)
            assert root2 != hub2
    return n,sibling_pairs

def main():
    profiles=vertices=pairs=0
    for m in range(2,6):
        for p in product((1,2,3),repeat=m):
            n,s=verify_profile(p)
            profiles += 1;vertices+=n;pairs+=s
    print('VERIFY_OK profiles=%s total_vertices=%s sibling_pairs=%s exact_rational_witnesses' % (profiles,vertices,pairs))

if __name__ == '__main__':
    main()
