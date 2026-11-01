# Review: Hamiltonian-cycle-deleted bipartite graphs

## Correctness (C) — PASS

The graph, two-independence face condition, and integer range \(n\ge4\) are explicit. The proof partitions faces by the chosen bipartite class \(B\) and performs a sequential-element matching. The fiber case analysis leaves one vertex, \(n(n-3)/2\) mixed three-cells, and \((n^2-3n-2)/2\) pure three-cells. The standard acyclicity proposition for sequential element matchings is given in Deshpande–Singh, Proposition 2.10; Forman's theorem then gives an integral wedge of \(n^2-3n-1\) three-spheres. Unlike an inference from homology, the absence of critical intermediate-dimensional cells supplies trivial attaching maps.

The executable `verify.py` independently evaluates the membership predicate on every subset through \(n=8\), verifies all matching arrows and acyclicity through \(n=12\), and computes mod-two homology through \(n=8\). These checks corroborate but do not replace the infinite proof. The exceptional \(n=3\) graph is a disjoint matching, hence a simplex at parameter two.

## Originality (O) — PASS on inspected evidence, with residual risk

Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs* (arXiv:1501.06754v1, first posted 2015-01-27), treats path/cycle/forest graph complexes; its cycle theorem covers the isolated \(n=4\) case, not the family. Deshpande–Singh, *Higher independence complexes of graphs and their homotopy types* (arXiv:2001.05448), gives the technique and a complete-multipartite classification; the latter does not apply to a graph with an alternating Hamiltonian cycle deleted.

The ordinary independence complex of the same deleted-cycle graph, a graph-metric Vietoris–Rips complex described using its deleted factor, the first higher-independence complex of a crown graph (one deleted matching), and the complete bipartite graph without deleted edges all have different face conditions and do not imply this theorem. Searches covering dissociation, \(P_3\)-devoid, induced-degree-one and Hamiltonian-cycle deletion terminology found no covering stronger result. Accessible indexed records and earlier recoverable claims were compared on their implications, not only title similarities. An equivalent unindexed publication remains possible.

## Mathematical value (V) — PASS

Deleting one alternating spanning cycle is a canonical, connected, regular-graph construction rather than an arbitrary choice of exceptional small graph. The first higher-independence complex of this dense bipartite family has an exact uniform, nontrivial integral homotopy type. It changes from the complete bipartite family's degree-one homology to degree-three homology, with an explicit quadratic sphere multiplicity. This identifies the structural impact of deleting a single spanning 2-factor and supplies a baseline for more general 2-factor deletions. The value comes from the uniform topology, not from a small numerical improvement or code alone.

## Scope and limitations

The result is nonequivariant and concerns exactly the first higher-independence parameter. Neither arbitrary unions of deleted cycles nor higher parameters are addressed. Finite verification does not prove the infinite statement. Definitive publication priority and independent mathematical validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
