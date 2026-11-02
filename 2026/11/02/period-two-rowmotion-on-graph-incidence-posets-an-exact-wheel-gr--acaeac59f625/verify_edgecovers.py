"""Independent edge-colouring and transfer-matrix verification."""
from itertools import combinations


def wheel_edges(r):
    # Vertex 0 is the hub; vertices 1,...,r lie on the rim.
    return r + 1, [(0, i) for i in range(1, r + 1)] + [
        (i, i + 1) for i in range(1, r)] + [(r, 1)]


def valid_edge_bicolorings(n, edgelist):
    incident = [[] for _ in range(n)]
    for j, (u, v) in enumerate(edgelist):
        incident[u].append(j)
        incident[v].append(j)
    good = 0
    for bits in range(1 << len(edgelist)):
        if all(any((bits >> j) & 1 for j in js)
               and any(not ((bits >> j) & 1) for j in js)
               for js in incident):
            good += 1
    return good


def lucas_independent_sets_cycle(n):
    return sum(1 for bits in range(1 << n) if all(not ((bits >> i) & 1 and
                                       (bits >> ((i + 1) % n)) & 1) for i in range(n)))


def check_wheels():
    for r in range(3, 11):
        n, E = wheel_edges(r)
        good = valid_edge_bicolorings(n, E)
        lucas = lucas_independent_sets_cycle(r)
        assert good == 3**r + (-1)**r - 2*lucas
        assert good % 2 == 0
        print(f'r={r} edge_bicolorings={good} period2_orbits={good//2} Lucas={lucas}')
    print('WHEEL_EDGECOVER_TRANSFER_PASS')


def connected(n, E):
    if not n:
        return False
    seen = {0}
    while True:
        nxt = seen | {v for u,v in E if u in seen} | {u for u,v in E if v in seen}
        if len(nxt) == len(seen):
            break
        seen = nxt
    return len(seen) == n


def bipartite(n,E):
    return any(all(((mask>>u)&1) != ((mask>>v)&1) for u,v in E) for mask in range(1<<n))


def row(state, n, E):
    S,T=state
    allowed = sum(1 << j for j,(u,v) in enumerate(E) if (S>>u)&1 and (S>>v)&1)
    U=allowed^T
    result=((1<<n)-1)^S
    for j,(u,v) in enumerate(E):
        if U>>j&1:
            result|=(1<<u)|(1<<v)
    return result,U


def check_general():
    for n in range(2,5):
        possible=list(combinations(range(n),2))
        tested=0
        for mask in range(1<<len(possible)):
            E=[e for i,e in enumerate(possible) if mask>>i&1]
            if not E or not connected(n,E):
                continue
            expected=(int(bipartite(n,E)) + valid_edge_bicolorings(n,E)//2)
            points=0
            for S in range(1<<n):
                allowed=sum(1<<j for j,(u,v) in enumerate(E) if (S>>u)&1 and (S>>v)&1)
                T=allowed
                while True:
                    q=(S,T); q1=row(q,n,E)
                    if q1!=q and row(q1,n,E)==q:
                        points+=1
                    if not T:break
                    T=(T-1)&allowed
            assert points%2==0 and points//2==expected,(n,E,points,expected)
            tested+=1
        print(f'connected_labeled_graphs_n={n} tested={tested}')
    print('ALL_CONNECTED_GRAPHS_N_LE_4_PASS')


if __name__=='__main__':
    check_wheels()
    check_general()
