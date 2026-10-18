# Independent mathematical audit

## correctness

PASS

Actual graph distances are 1/3 between opposite sides, 2 for distinct same-side and 0 at a selected landmark. Multiset signatures are thus determined by landmark membership, the side cardinalities p,q, and cumulative suffix R_i/prefix S_j. Injectivity on selected and unselected vertices yields p<=q+1, n-p<=q+1, q<=p+1, n-q<=p+1, implying size>=n-1. Odd equality forces same count on cross sides with matching remaining multiplicities. For even equality the cumulative-count blocks must all be two-point alternating pairs, forcing two complementary bases. For odd optimal size the unique singleton count block and no-repeat conditions force exactly one switch (indexed c,d with 0<=d<c<=m); the side automorphism doubles the m(m+1)/2 choices. Independent BFS distance/multiset subset enumeration confirmed n=2..6 and base counts 2,6,2,12,2; package verifier covers n2..9, but is not a substitute for all-n proof.

## originality

PASS

The exact statement and its implications were compared against the defining primary source, nearest general theorems, differently named invariants and Resultary published records. No dominating prior result was found among genuinely examined material; any inaccessible or unindexed potential coverage is retained as a residual risk, not treated as evidence of novelty.

## value

PASS

The half graph is the canonical twin-free chain/Ferrers graph; determining all minimum unordered-distance landmark sets and exact parity-sensitive base multiplicities is a natural complete extremizer classification, unavailable from scalar ordinary/edge/strong metric dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
