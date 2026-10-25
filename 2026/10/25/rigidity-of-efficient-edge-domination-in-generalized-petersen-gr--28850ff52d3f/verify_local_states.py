#!/usr/bin/env python3
"""Independent vertex-state test for dominating induced matchings in GP(n,2).

Searches cyclic outer black/white words (not the edge exact-cover state space).
Every matched vertex must have one matched neighbor; every unmatched vertex
must have no unmatched neighbor. This condition is checked at all 2n vertices.
"""


def adjacency(n):
    adj = [set() for _ in range(2*n)]
    for i in range(n):
        for a,b in ((i,(i+1)%n), (i,n+i), (n+i,n+(i+2)%n)):
            adj[a].add(b);adj[b].add(a)
    return adj


def possible_words(n):
    # Generate all cyclic binary words avoiding adjacent whites (00)
    # and any run of three consecutive blacks (111).
    for mask in range(1 << n):
        a = [bool(mask >> i & 1) for i in range(n)]
        if any((not a[i] and not a[(i+1)%n]) or
               (a[i] and a[(i+1)%n] and a[(i+2)%n]) for i in range(n)):
            continue
        yield a


def direct_states(n):
    adj = adjacency(n)
    accepted = set()
    for outer in possible_words(n):
        # Inner black if an outer vertex is white or its two outer
        # neighbors are white (therefore the selected spoke is its partner).
        inner = [not outer[i] or
                 (not outer[(i-1)%n] and not outer[(i+1)%n]) for i in range(n)]
        b = outer + inner
        # For a black vertex: exactly one black neighbor.
        # For a white vertex: all neighbors are black.
        if all(sum(b[w] for w in adj[v]) == (1 if b[v] else 3)
               for v in range(2*n)):
            # Determine selected matching as edges with both black endpoints.
            mm=frozenset(tuple(sorted((v,w))) for v in range(2*n)
                          for w in adj[v] if v<w and b[v] and b[w])
            accepted.add(mm)
    return accepted


def main():
    for n in range(5,21):
        found = direct_states(n)
        expected = 5 if n%5==0 else 0
        assert len(found) == expected, (n, len(found), expected)
        for matching in found:
            assert len(matching) == 3*n//5
        print('n=%d: %d valid vertex-state configurations' % (n,len(found)))
    print('VERTEX_STATES_OK')

if __name__ == '__main__':
    main()
