# Independent mathematical audit

## correctness

PASS

For binary row-and-column parity checks, the erased-coordinate kernel is exactly the binary cycle space of the erasure bipartite graph with dimension e-v+c. Connected bipartite rank-1, rank-2 and rank-3 components need >=4, >=6, >=8 edges. At eight edges total rank >=3 requires a single connected six-vertex rank-3 graph; with 8 edges and bipartition sizes summing to six, the only possibilities are K_{2,4}, K_{4,2} or K_{3,3} minus one edge. Every edge lies on a cycle, so support(C(E))=E and exactly one three-space occupies each minimum support. Choosing row/column sets yields binom(m,2)binom(n,4)+binom(m,4)binom(n,2)+9binom(m,3)binom(n,3), with zero-binomial convention. No fewer-than-eight erasures can have rank three. Independent all-eight-edge bipartite graph enumeration returned predicted rank-three counts 1 at (2,4), 9 at (3,3), 39 at (3,4), 156 at (4,4). Uniform theorem rests on graph proof, not these finite tests.

## originality

PASS

Ribeiro Alves and Cardell (2026, arXiv:2608.26457 Theorem 7) already prove the generalized Hamming weight d3=8, which is expressly not claimed new. Cardell–Climent 2016 count all uncorrectable eight-erasure patterns, without verified separate rank-three classification in accessible text; Cardell–Climent–López Martín 2019 Theorem 3 counts strict failure graphs by degree margins using Kostka numbers. Neither accessible inspected statement directly gives the cycle-rank-three multiplicity and complete three-shape/minimum-three-subcode bijection; the margin enumerator may imply counts after new graph analysis. Strong plausible implicit coverage remains in inaccessible 2016 and uninspected 2019 full details; best-of-knowledge qualified PASS, not an exhaustive priority certification.

## value

PASS

An eight-erasure failure can have different ambiguity dimensions and hence 2,4 or 8 possible completions. The first eight-completion threshold and exact multiplicities of every extremal support across arbitrary rectangular SPC products distinguish this natural decoding-severity invariant from raw error counts; complete support geometries also classify every third-weight minimizing subcode. Structural classification rather than merely restating d3=8.

The dated certificate retains the supplied scientific assessment, sources and limitations.
