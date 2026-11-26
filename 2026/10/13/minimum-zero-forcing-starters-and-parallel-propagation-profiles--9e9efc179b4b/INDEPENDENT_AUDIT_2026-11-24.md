# Independent mathematical audit

## correctness

PASS

A size-delta starter can first force only from a minimum-degree vertex v and must be N[v] minus the single target. In the noncomplete path power only the two endpoints have degree k; their starter families are disjoint because each includes its own endpoint and omits the opposite endpoint. Exactly the missing neighbor is forced initially, then precisely one vertex per round: any forcing vertex that sees a later white vertex must also see the first white vertex. In a noncomplete cycle power the closed neighborhoods are cyclic intervals of length L=2k+1. At order 2k+2, the two whites are forceable exactly if nonantipodal, in one round by their antipodes. At n>=L+2 distinct L-intervals can share L−1 vertices only when their centers are consecutive (a two-piece overlap has size 2L−n<=L−2); hence exactly the contiguous starters have two representations and the other starters have a unique first force. For a contiguous black interval of length h>=2k, the two distances through black vertices from any forcing vertex to the white endpoints sum to h+1>2k, so only one boundary can be reached through black vertices from that vertex. Exactly the two white boundary vertices (one if coincident) can be forced, using vertices k steps back into the black interval. This gives both ceiling exponents and the claimed parity. Complete graphs give the stated complements-of-one-vertex case. The independent bit-mask enumeration gave the cycle profiles 24y, 45y^2 and 10y^2+40y^3 at (n,k)=(8,3),(9,3),(10,3), and checked both short path boundaries and an ordinary cycle.

## originality

PASS

Credit the prior scalar values, the near-complete size census from the universal zero-forcing polynomial, and ordinary-cycle propagation. Distinct indexed results reproduce much of the starter census and are treated as overlapping content, not dismissed by date or treated as establishing priority. The supported distinct claim is the full synchronous-time refinement in the higher powers: in particular the parity-sensitive split of the exhaustive long-cycle minimum-starter family and its exact multiplicities by time. Neither a scalar nor an unweighted census determines that refinement.

## value

PASS

Powers of paths and cycles are standard forcing test families with the same cardinality among all minimum starters. The full time profile quantifies how geometry rather than seed size changes performance: when the white gap length is even, puncturing the black interval costs an extra round, while it costs none for odd length. The counts and exact boundary regimes make that distinction usable without enumerating seeds; scalar values, complete cases or ungraded starter counts alone would not motivate another result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
