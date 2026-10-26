"""Exact finite-graph witness for the two-cut rotation sampling theorem.
Run with Python 3, no dependencies.
The infinite dynamical argument is in RESULT.md; this verifies only its finite covering instances.
"""

def graph(k, r):
    assert k >= 1 and r >= 0
    d = k + 2 * r
    n = 1 << d
    mask = set(range(2 * r + 1)) | set(range(k, k + 2 * r + 1))
    arcs = []
    for state in range(n):
        for bit in (0, 1):
            w = [(state >> i) & 1 for i in range(d)] + [bit]
            if any(w[j] for j in mask):
                dest = (state >> 1) | (bit << (d - 1))
                arcs.append((state, dest, bit))
    return n, arcs


def certify_lower_bound(k, r, p, q):
    """No negative directed cycle with integer edge costs q*bit-p."""
    n, arcs = graph(k, r)
    dist = [0] * n
    for iteration in range(n):
        nxt = dist[:]
        for u, v, bit in arcs:
            nxt[v] = min(nxt[v], dist[u] + q * bit - p)
        if nxt == dist:
            return n, len(arcs), iteration + 1
        dist = nxt
    raise AssertionError('negative cycle: claimed lower bound fails')


def periodic_upper_bound(k, r, bits):
    q = len(bits)
    for start in range(q):
        assert any(bits[(start + offset) % q] for offset in
                   list(range(2*r+1)) + list(range(k, k+2*r+1)))
    return sum(bits), q


if __name__ == '__main__':
    # First nontrivial non-interval certificate: 2 observations per 11 time units.
    n, e, rounds = certify_lower_bound(5, 1, 2, 11)
    assert (n, e) == (128, 252)
    assert periodic_upper_bound(5, 1, [1,0,0,1,0,0,0,0,0,0,0]) == (2,11)
    # Consecutive observation windows, proving the expected exact densities.
    for k, r in [(1,0),(1,1),(2,1),(3,1),(3,2),(5,2)]:
        if k <= 2*r+1:
            q = 2*r+k+1
            certify_lower_bound(k,r,1,q)
            assert periodic_upper_bound(k,r,[1]+[0]*(q-1)) == (1,q)
    # Every R=0 and finite cut distance has an exact one-half obstruction.
    for k in range(1,10):
        certify_lower_bound(k,0,1,2)
        assert periodic_upper_bound(k,0,[1]*k + [0]*k) == (k,2*k)
    print('VERIFY_OK: exact finite graph dual bounds, periodic witnesses, and R=0 cases')
