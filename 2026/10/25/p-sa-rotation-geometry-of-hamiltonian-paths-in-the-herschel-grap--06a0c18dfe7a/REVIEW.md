# Scientific review

## Correctness

PASS. The explicit eleven-vertex graph is verified by degree and edge counts. Two structurally independent enumerators, one extending Hamiltonian vertex sequences and the other testing every ten-edge subset, both find exactly 222 spanning undirected paths. Their independently built rotation/exchange graphs both have 444 edges, one component, radius 8, diameter 9, and eccentricity counts 198 and 24. The equivalence of endpoint Pósa rotations and one-edge exchanges follows from the impossibility of a Hamiltonian cycle in this odd bipartite graph. All numerical statements are finite, exhaustively certified claims.

## Originality

PASS, with residual risk. Kriesell–Pedersen (arXiv:1108.1036v1) identifies the classical Herschel graph as the dual of a graph in a colouring-number classification, not its Hamiltonian-path rotation graph. Krivelevich (arXiv:1507.00205), Section 2.3, introduces the general rotation operation without this exact census. Previously recorded Petersen Hamiltonian-path rotation geometry concerns a nonisomorphic 10-vertex graph and therefore does not imply these 222-state invariants. Targeted searches of mathematical records and related literature found no covering equivalent; unindexed finite tables remain a publication-priority risk.

## Value

PASS. The Herschel graph is the smallest non-Hamiltonian polyhedral graph, so asking whether its Hamiltonian paths form a single space under the canonical rotation-extension move is a motivated boundary question. Connectivity and the sharp nine-move transformation distance demonstrate full path-space flexibility despite the obstruction to Hamiltonian cycles. The result answers a natural complete finite question rather than selecting arbitrary vertices or parameters.

## Scope

The assertions concern this finite graph only. Reproduction requires only Python 3 and the embedded checkers. Publication priority remains conditional on broader literature coverage, and no independent scientific audit is claimed.

Self-review: passed. Independent audit: not yet performed.
