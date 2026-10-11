# Scientific review

## Correctness — PASS

The dual-complex construction follows directly from the definition of ordinary three-cut facets. Every connected triple is a two-edge path and each such path has a unique nonedge between its endpoints; two distinct middle vertices for one endpoint pair would form a forbidden four-cycle. Therefore each triangle collapses over its own free edge. This gives the exact integral first cohomology of the dual and, by integral Alexander duality, the entire homology of the original complex. The complete lower skeleton and \(n\ge7\) allow the Hurewicz–Whitehead argument proving the wedge homotopy type. Signed path chains inject into the complete-graph cycle space, and the ambient orientation character in equivariant Alexander duality establishes the claimed group-character formula. The standalone direct-face verifier completes 374 signed-Lefschetz comparisons and six complete mod-two rank checks.

## Originality — PASS, with stated residual risk

The closest original source, Bayer et al., *Topology of Cut Complexes of Graphs* (arXiv:2304.13675), Theorem 6.1 and Proposition 6.2, already determines the codimension-one skeleton and an Euler-characteristic expression under the girth hypothesis; these ingredients and the isolated cycle/tree calculations are **not** presented as new. The later *Topology of Cut Complexes II* (arXiv:2407.08158) treats selected graph families and group representations. The hexagonal-grid result (arXiv:2512.21755) gives a specialized shellable subfamily. None of these inspected texts determines the complete automorphism character uniformly for all graphs without triangles or four-cycles, and the first source's general skeleton theorem alone does not imply vanishing of its permitted lower-degree homology. Residual risk: an equivalent general theorem in unlocated literature, possibly formulated through an Alexander dual of a partial two-dimensional clique complex, would cover part or all of the finding; absence from searches is not definitive novelty proof.

## Value — PASS

The conclusion is a natural all-graph topological classification rather than a finite case or routine restatement of an Euler characteristic. The private opposite-edge collapse mechanism solves the previously undetermined lower homology uniformly, while the short exact sequence of signed path chains provides the full rational group representation of each graph's automorphism group. The formula treats disconnected graphs and high-symmetry examples with the same proof, including the Petersen graph as a consistency case, and yields a reusable template for equivariant cut-complex calculations. The exact nontrivial representation information is not implied by total Betti numbers alone.

## Boundaries

The homotopy equivalence is not claimed to respect graph symmetries. Graphs with triangles or four-cycles, and graphs on fewer than seven vertices, are outside the statement. The finite program is a verifier of examples, not a proof for infinitely many graphs. No shellability statement follows merely from the sphere-wedge result. Published equivalences not located remain possible.

Same-model review: passed. Independent audit: not yet performed.
