# Scientific review

## Correctness — PASS
The state Laplacian is the Kronecker sum of complete-graph Laplacians. Its four eigenspaces are explicitly reconstructed with dimensions and exact eigenvalues. The zero-row/zero-column interaction space is unobservable precisely when the unselected bipartite graph contains a cycle, by alternating circulation and forest leaf elimination. At resonance the two centered main-effect spaces merge, and vanishing on selected cells becomes a component-wise constant parameter system with exactly two sum constraints. Its two-by-component matrix is full column rank precisely under the stated component-count condition. The PBH implication and explicit optimal designs cover every \(p,q\ge2\) and \(a,b>0\). The exact program completed 11,378 assertions, supporting but not replacing the proof. Risk: implementation checks finite configurations only; infinite statement rests on the displayed algebraic and graph proof.

## Originality — PASS, with residual risk
The relevant prior results on PBH, Cartesian eigenstructure, maximum eigenspace multiplicity, and bipartite incidence cycle spaces are not claimed as novel. Notarstefano–Parlangeli (arXiv:1203.0129) focus on path grids; Yuan et al. (arXiv:1310.5806) establish a general multiplicity rule; Anđelić–Brunetti–Stanić (DOI 10.1007/s00373-020-02212-6) explicitly analyze *one binary input* for graph products; Dai (DOI 10.1049/cth2.12385) treats separate self-similar graph families. None of the inspected primary texts states this exact if-and-only-if test for all independent terminal actuator sets, especially the component-ratio condition precisely at \(ap=bq\). Searches for rook graphs, Hamming squares, two-way ANOVA designs and bipartite sampling failed to locate equivalent full coverage. Risk: unindexed literature under a different design-theoretic formulation may cover it; Yuan's count baseline means the bare cardinality result alone is not a new principle.

## Value — PASS
The result reduces a high-dimensional PBH test for any candidate sensor/actuator placement to a forest check and at most a two-component imbalance comparison. It identifies why a spectrally optimal-size rectangular placement fails on the resonance surface and provides a same-size replacement except on width-two networks, where one more actuator is necessary. At nonresonance all optimal placements are enumerated exactly by spanning trees. This is a natural complete classification and an operational design rule, not an arbitrary finite example.

## Scientific limitations
Only direction-constant positive weights, products of two complete graphs and independently controlled node coordinates are covered. There is no theorem for arbitrary edge weights, input energy, robustness, or higher-factor Cartesian products. Full-text absence is not asserted for unavailable unindexed material; no independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
