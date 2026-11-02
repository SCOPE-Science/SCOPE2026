# Independent mathematical audit

## correctness

PASS

Independently reconstructed the LCF [5,7,-7,7,-7,-5]^3 graph as an 18-vertex 27-edge simple cubic graph and all-pairs BFS distances (each shell 1,3,6,6,2; diameter 4). Inspected the actual pinned RESULT.md, verify_pappus_magnitude.py, VERIFICATION.md, AUDIT.json and verification_output.txt. Wrote and ran independent exhaustive Python code enumerating ALL proper tuples of 3,4,5 vertices with total shortest-path length exactly 4, grouped by all 324 ordered endpoints; boundary deletes only smooth interior points, using exact F2 XOR and independent pivot rank. All 324 blocks satisfy d3*d4=0. At endpoint distances 0,1,2,3,4, the sole observed tuples (dim C2,dim C3,dim C4,rank d3,rank d4,dim H3) were (6,18,15,6,12,0), (0,0,0,0,0,0), (7,18,9,7,9,2), (0,0,0,0,0,0), (12,18,6,11,6,1). Pair counts were 18,54,108,108,36; global dimensions C2=1296,C3=2916,C4=1458 and ranks 1260,1404, hence H3=252. The independent verifier is a complete finite enumeration, not a sample or merely the repository log. Proper chains allow nonconsecutive repeats; no assertion about integer torsion, arbitrary fields, higher bidegrees, or other graphs.

## originality

PASS

Qualified best-of-knowledge. The full finite statement is a specific endpoint-distance profile for the Pappus graph; no inspected published theorem, table, or wider-family result implies the values 2 at distance 2, 1 at distance 4, zero elsewhere, total 252. Asao–Hiraoka–Kanazawa vanishing requires girth >=7, whereas Pappus has girth 6. Closest published Resultary incidence theorem assumes a finite projective plane, which the Pappus 9_3 configuration is not. Zhu’s 2026 signature dataset contains standard families and all graphs only up to 7 vertices, excluding this 18-vertex named graph. Resultary matching hit is the assessed claim, not an independent antecedent. A general computational algorithm is not an already-known numeric table. Unindexed computations or a broader unlocated theorem remain priority risks, not grounds for an unsupported novelty guarantee.

## value

PASS

The Pappus graph is a named cubic symmetric distance-regular girth-six Levi graph of the classical Pappus configuration, not an arbitrary selected subgraph. Bidegree (3,4) is the first off-diagonal location not forced to vanish by the published girth>=7 theorem, making this a motivated boundary computation. The exact F2 endpoint-distance profile (two, one, or zero generators) adds geometrically localized information not implied by graph size/girth/degree, and provides a reproducible finite benchmark for comparisons among canonical girth-six incidence graphs. The independent work verifies all blocks, so the result is a substantive exact natural invariant even without an infinite-family generalization. Limited scope (F2, one graph, one bidegree) is stated; no unsupported downstream theorem or integral claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
