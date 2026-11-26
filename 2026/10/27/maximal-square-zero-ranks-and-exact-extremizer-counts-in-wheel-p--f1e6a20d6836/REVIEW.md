# Independent mathematical audit

## correctness

PASS

A partial injection is square-zero exactly when domain and image are disjoint. If the hub belongs to the domain and maps to v, at most two other images can be rim neighbors of v, giving rank at most three; inversion handles the image-hub case. The disjointness bound already gives floor(n/2) for even n. For odd n≥7 a larger rank uses the hub but would exceed three. For n=5 a hypothetical rank three has image {v−1,v,v+1}; the two other domain vertices v−2 and v+2 are adjacent, but v−1 and v+1 are not. Two disjoint alternating independent rim sets give the claimed attainable rank, and restriction gives all lower ranks. On the rim, adjacency determines the metric. Red domain and blue image therefore must have identical multisets of path-component orders. For a fixed red composition of k, blue orders contribute r!/∏ m_j!, isomorphisms contribute ∏ m_j!·∏ b_j^(m_j), and b_j is one for singletons and two otherwise. For even n a marked red start has n labels and represents a pair with its map r times, yielding n(r−1)! times the coefficient in B^r. For odd n deleting the unique unused vertex cuts a line, and equal run counts force unlike end colors, yielding 2n r! times that coefficient. With a hub, rank two counts directed rim edges avoiding the other domain vertex (2(n−2) choices); rank three counts the nonedges in the path remaining after deleting v and its neighbors, namely binom(n−3,2)−(n−4), and has two bijections for each. Multiplying by n and by two for inversion gives exactly the listed hub corrections; there are none at rank at least four.

## originality

PASS

The supported distinct claim is the uniform extremal enumeration in the inherited wheel metric, with disjointness built into the cyclic or linear run counts and explicit hub exceptions. The disjointness criterion, induced-subgraph model, earlier general-type enumerations, and the n=4 complete multipartite special case are not credited as distinct contributions.

## value

PASS

Square-zero elements expose a genuine difference from the ambient symmetric inverse monoid in odd wheels. The count at the largest attainable rank is a natural semigroup invariant: the parity distinction and hub exceptions give an exact count of the maps with the tightest possible disjointness constraint. The useful contribution is the exact uniform rim/hub enumeration, not the elementary rank upper bound alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
