# Scientific review

## Correctness — PASS

Every disjoint pair of missing base edges has all its common neighbors in the complement when the complement is convex. Fixing an included base edge \(uv\), this forces the missing-neighbor sets at \(u\) and \(v\) either to have an empty side (yielding a full star) or to be the same singleton. Ordinary general position rules out additions to a full star for \(n\geq4\), rules out the singleton case for \(n\geq5\), and forces an exact triangle in that case for \(n=4\). Complements of the remaining stars and exceptional triangles are geodesically convex. The proof checks all boundaries \(n\geq3\), distinguishes selected from missing endpoints, and does not extrapolate an infinite claim from finite tests. The independent-programming-path BFS verifier reproduces the predicted families exhaustively through \(n=6\), with additional sampled orders.

## Originality — PASS, subject to residual literature risk

Tian–Klavžar, arXiv:2402.17338v1, defines the dual variant and proves the generic convex-complement criterion but does not enumerate triangular-graph dual sets. Di Stefano et al., arXiv:2306.09965v1, Theorem 5.2, describes a distinct *lower ordinary* general-position invariant of exactly the same line graph; the ordinary maximal-configuration characterization does not imply the convex-complement restriction. The earlier line-graph ordinary-general-position literature likewise concerns the larger feasible family. Published complete-multipartite results can encompass the exceptional \(n=4\) instance; no novelty is claimed for this finite boundary. The genuine contribution is the arbitrary-order \(n\geq5\) classification and exact polynomial. Targeted aliases and implication searches found no covering source, but unindexed equivalent work remains possible and absence of retrieval is not a uniqueness certificate.

## Value — PASS

The result completely resolves a nonhereditary geometric set property for the classical strongly regular triangular graphs, rather than giving only its maximum size. Every nonempty feasible set must be a global star of size \(n-1\), so there are exactly \(n\) solutions and no feasible nonempty set at any of the \(n-2\) smaller sizes. The exact enumerator and unbounded cardinality gap identify a substantial structural obstruction supplied by complementary geodesic convexity and permit direct comparison with known ordinary and lower general-position parameters.

## Limitations and provenance

The literature overlap comparison is not a comprehensive world-wide priority certification. The self-review verifies the mathematical argument and new packaged verifier; independent scientific assessment remains pending. The 2024 source predates the applicable middle-period cutoff, and its first public arXiv date, not a later publication date, is used for scope.

Self-review: passed. Independent audit: not yet performed.
