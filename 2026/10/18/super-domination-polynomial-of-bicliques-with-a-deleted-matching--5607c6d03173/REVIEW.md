# Scientific review: super-domination of matching-deleted bicliques

## Correctness — PASS

The definition fixes open-neighborhood witnesses and counts labeled vertex subsets. The proof first bounds the omitted vertices to two in each bipartition; it then gives a necessary-and-sufficient witness test for all nine occupancy patterns. The only small-boundary failures arise when a side of order three leaves a single selected witness, exactly producing the two correction terms. Summing the disjoint cases gives every polynomial coefficient, and the leading nonzero coefficient gives both the minimum and its multiplicity. The standalone exhaustive verifier agreed for 130 profiles and 407040 subsets, including the six-vertex exception. This computation corroborates but does not replace the all-parameter proof.

## Originality — PASS, with residual source-access risk

The closest full texts inspected were Ghanbari, Jäger and Lehtilä, *Super Domination: Graph Classes, Products and Enumeration* (arXiv:2209.01795), and Akbari, Ghanbari and Henning, *End Super Dominating Sets in Graphs* (arXiv:2209.02980). Their results for complete bipartite graphs, cycles, graph operations and general bounds do not give a complete polynomial for complete bipartite graphs with an arbitrary matching deleted. A published classification for complete multipartite graphs gives the no-deletion case but does not cover the missing-edge family. The 2024 chapter by Kaidash (DOI 10.1007/978-3-031-73365-9_6) develops super-domination polynomials and could contain an equivalent special case, but only its abstract was accessible. No priority claim is made beyond the inspected evidence; an unindexed or inaccessible equivalent result remains possible.

## Value — PASS

The formula describes *every* super dominating set by cardinality, not only an optimum, throughout a natural three-parameter graph family. It explains why one deleted edge changes no minimum, two allow one extra omission, and four allow two extra omissions, and isolates the six-vertex crown boundary. Exact optimal-set multiplicities distinguish deletion profiles with the same optimum size; the complete polynomial is insensitive to one deleted edge yet distinguishes every larger matching size. This represents a concrete stability phenomenon for a standard graph parameter, motivated by prior complete-bipartite enumeration and graph-modification studies.

## Limits

The theorem assumes both sides have at least three vertices. The counts are by labeled subsets and do not enumerate automorphism orbits. Full bibliographic priority validation and independent scientific checking are outstanding. The inaccessible 2024 polynomial chapter is a specific originality risk, not evidence of coverage.

Self-review: passed. Independent audit: not yet performed.
