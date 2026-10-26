# Scientific review: Petersen two-token electrical resistance

## Correctness — PASS
The 45 configurations are exactly the 2-subsets of the ten Petersen vertices. A move changes one endpoint along one of fifteen Petersen edges while the other token stays fixed; the 120 moves are uniquely counted. The grounded Laplacian has size 44. The verifier calculates its inverse over exact rational numbers, verifies the identity product, and evaluates the electrical-resistance quadratic form for every one of 990 unordered pairs. Every one of the 120 permutations of the five underlying labels acts as an automorphism; these actions partition the pairs into exactly seventeen exhaustive orbits with pairwise distinct resistances. Since the full automorphism group preserves resistance and contains this subgroup, equality of resistance is equivalent to full-automorphism orbit equivalence. Shortest-path breadth-first search independently checks the nonmonotone distance comparison and Kirchhoff index is checked by an additional spectral identity. The code is a reproducible exhaustive finite certificate, not a proof for other graph families.

## Originality — PASS, with residual risks
The closest publications establish symmetric-square constructions and spectral constraints (Audenaert, Godsil, Royle and Rudolph, arXiv:math/0507251), token-graph combinatorics (Fabila-Monroy et al., arXiv:0910.4774), token Laplacian spectral inclusions (Dalfó et al., arXiv:2012.00808), automorphism reconstruction (Fabila-Monroy and Trujillo-Negrete, arXiv:2207.12336) and quotient/spectral analysis (Reyes, Dalfó and Fiol, arXiv:2310.16929). None of the inspected applicable results gives the grounded inverse, the seventeen resistance classes, or the exact resistance/orbit equivalence. A related two-particle Petersen configuration-homology study concerns homology rather than electrical resistance. Direct literature and research-record searches of aliases and stronger invariants did not identify a covering table. Search incompleteness and unpublished computations remain risks; novelty is not certified beyond the inspected evidence.

## Value — PASS
The finding classifies an intrinsic electrical metric on the canonical strongly regular Petersen graph's two-particle exclusion state space. Distinguishing all seventeen symmetry types by one scalar is a structural fact not obtained from known spectral summaries; the inversion of resistance relative to shortest-path distance illustrates a concrete distinction between electrical and geodesic geometry. It also supplies a complete exact-rational benchmark for graph exclusion processes and graph resistance calculations. Its scope is deliberately finite, and no downstream theorem is asserted.

## Limits
Reproduction requires running the provided Python 3 standard-library program. No independent external audit has been done; overlooked earlier tables are possible.

Self-review: passed. Independent audit: not yet performed.
