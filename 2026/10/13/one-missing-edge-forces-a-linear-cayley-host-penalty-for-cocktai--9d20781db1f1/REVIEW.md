# Self-review

## Correctness — PASS
The complement of the edge-deleted cocktail-party graph is exactly one four-vertex path and \(r-2\) disjoint edges. The proof counts crossing edges in an arbitrary regular complementary host, using degree at least two, and forces at least \(r-1\) vertices outside the embedded graph. The cyclic complement construction realizes exactly this order, with separate boundary \(r=2\). The standalone checker validates explicit constructions through \(r=100\); the universal proof does not rely on enumeration.

## Originality — PASS with literature risk
The September 2026 induced-Cayley-host paper [1] gives the definition and earlier path and complete-bipartite benchmarks, but the accessible abstract does not state the one-edge-deleted cocktail-party theorem. The 2016 cocktail-party Cayley result [2] treats the undeleted graph, where the host order is simply its vertex count. A prior exact result for the single-book \(K_{1,1,n}\) under the same invariant does not determine this quite different edge-deletion family. published-finding corpus searches of the equivalent complement formulation and direct Cayley-host formulation returned no dominating statement. The 2026 full text was inaccessible, so residual coverage risk remains; absence from an abstract is not definitive proof of novelty.

## Value — PASS
This exact infinite-family extremal result shows that deleting just one edge from a vertex-transitive graph raises the least induced abelian Cayley-host order by a quantity growing linearly with the number of parts. The sharp lower bound even applies to all vertex-transitive hosts, while the construction is cyclic. This gives a mathematically motivated stability boundary for a recently studied graph invariant, rather than an isolated finite value.

## Scientific limits
Neither other edge-deletion patterns nor the uniqueness of minimizing hosts is resolved. Independent verification is outstanding.

Self-review: passed. Independent audit: not yet performed.

References: [1] arXiv:2609.01486 (first public 2026-09-01); [2] doi:10.1007/s10623-016-0209-4.
