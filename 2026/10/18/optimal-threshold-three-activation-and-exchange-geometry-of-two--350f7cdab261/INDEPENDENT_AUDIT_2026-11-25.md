# Independent mathematical audit

## correctness

PASS

Independently reconstructed both adjacency graphs and checked the degree, all common-neighbor counts, and the distinct local graph types. On a six-regular graph an inactive set persists precisely if it contains a nonempty induced subgraph of minimum degree at least four. The final inactive set is the union of all such subgraphs disjoint from the seeds: no member of any such subgraph can be activated first, and the final inactive set itself is stable. Enumerating these subgraphs gave largest triple closures of 5 and 7 and exactly 864 and 720 percolating four-sets. Monotonicity excludes all smaller sets. A separate synchronous update using precomputed neighbor triples gave the stated rounds. Comparing every pair of optimum configurations and computing bitset distance layers from every configuration reproduced each move edge, connectivity, radius, diameter, eccentricity distribution and all diameter-witness distances. Enumerating and checking the specified actions reproduced all orbit rows. The independent run compared full labeled states, activation times, exchange edges and orbit invariants against certificate.json (SHA-256 224cee59db2384166af4bb653d47e137fa61bb317cdde0350d1650d75c3ea632). Replay: python3 /workspace/branches/check_record3.py <record-directory>/certificate.json. The result is exact for the stated graphs, threshold and explicit actions.

## originality

PASS

The rook minimum size, the activation/core duality and the move terminology are prior-covered and are not the distinct contribution. The evidence supports the narrower exact threshold-three census and configuration-geometry comparison; none of the inspected primary statements or nearest catalogue hit covers it.

## value

PASS

The natural nonisomorphic pair with identical strongly regular parameters supplies exact witnesses that optimum-family size, optimal activation time and jumping geometry are not fixed by those parameters, even with equal optimum cardinality. In particular every rook jumping state has eccentricity four, whereas 288 Shrikhande states have eccentricity five. The precise orbit and distance data distinguish feasible local moves from global access and quantify the separation; this is more than a recomputation of the known rook minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
