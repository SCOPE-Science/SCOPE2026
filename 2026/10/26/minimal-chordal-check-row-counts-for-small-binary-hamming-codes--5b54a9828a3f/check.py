"""Exact chordal-primal parity-check threshold checks, Python 3 standard library."""
from itertools import combinations

def graph_rows(r, extra):
    nn = (1 << r) - 1
    adj = [0] * nn
    for row in tuple(1 << i for i in range(r)) + tuple(extra):
        if row == 0:
            continue
        support = [i for i in range(nn) if ((i + 1) & row).bit_count() & 1]
        mask = sum(1 << i for i in support)
        for i in support:
            adj[i] |= mask & ~(1 << i)
    return adj

def chordal_mcs(adj):
    """MCS theorem: an undirected graph is chordal iff the MCS reverse order is a PEO."""
    n = len(adj)
    chosen = 0
    selected = []
    degrees = [0] * n
    for _ in range(n):
        v = max((i for i in range(n) if not ((chosen >> i) & 1)),
                key=lambda i: (degrees[i], -i))
        selected.append(v)
        chosen |= 1 << v
        for w in range(n):
            if not ((chosen >> w) & 1) and ((adj[v] >> w) & 1):
                degrees[w] += 1
    seen = 0
    for v in selected:
        seen |= 1 << v
        prior = adj[v] & (seen & ~(1 << v))
        t = prior
        while t:
            bit = t & -t
            u = bit.bit_length() - 1
            if prior & ~(1 << u) & ~adj[u]:
                return False
            t -= bit
    return True

def one(r, extra):
    return chordal_mcs(graph_rows(r, extra))

def run():
    # Independence of coordinate basis rows: all nonzero columns, unique.
    # Restricted to a coordinate subspace of dimension s, larger graphs
    # contain the induced s-dimensional support-intersection graph.
    assert one(3, ())
    assert not one(4, ())
    assert one(4, (0b000011,))
    assert not one(5, ())
    count5 = 0
    for f in range(1,1<<5):
        assert not one(5, (f,))
        count5 += 1
    assert one(5, (0b00011, 0b01100))
    assert not one(6, ())
    count6a = 0
    for f in range(1,1<<6):
        assert not one(6, (f,))
        count6a += 1
    count6b = 0
    for f,g in combinations(range(1,1<<6),2):
        assert not one(6,(f,g))
        count6b += 1
    assert one(6,(0b000011,0b001100,0b110000))
    assert (count5,count6a,count6b)==(31,63,1953)
    print('VERIFY_OK')
    print('r3=3 rows; r4=5 rows; r5=7 rows; r6=9 rows')
    print('negative witnesses checked:',count5,count6a,count6b)
    print('universal lower: r>=4:+1, r>=5:+2, r>=6:+3')

if __name__ == '__main__':
    run()
