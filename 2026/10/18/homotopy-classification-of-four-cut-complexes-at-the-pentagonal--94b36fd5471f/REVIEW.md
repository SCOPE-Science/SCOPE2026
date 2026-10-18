# Mathematical review: pentagonal girth boundary for four-cut complexes

## Correctness
The claim is uniform for every finite simple graph of order at least nine and girth at least five, including disconnected graphs. The key classification of faces of the Alexander dual identifies connected four-sets, exactly five-cycle higher faces, and no faces on six or more vertices. All tetrahedra admit specified free-face collapses after each pentagon four-simplex is removed. This gives an integral wedge of two-spheres for the dual. Integral combinatorial Alexander duality, the complete two-skeleton of the original complex, Hurewicz, and Whitehead prove the final wedge in degree \(n-5\). The program separately checks combinatorics, finite-field ranks, and actual free-face reductions on several finite examples; finite experiments are not substituted for a proof.

## Originality
The original cut-complex paper (arXiv:2304.13675) gives the girth-at-least-six skeleton sufficient for the older four-cut method and classifies special families. Crucially, its sequel (arXiv:2407.08158, Proposition 2.18) *already determines the pentagonal correction to the Euler characteristic*. The new content is not that Euler formula; it is the complete integral homotopy type for all girth-five four-cut complexes. The closest publicly recorded general wedge theorem requires girth at least six (`ec8bbe3d352b`), and the recorded four-cycle correction theorem concerns three-cuts (`8ca830284420`). A Petersen four-cut homotopy calculation is a known special case. No covering arbitrary-girth-five four-cut homotopy theorem was identified, but unindexed equivalent work remains a genuine risk.

## Mathematical value
At the first girth threshold omitted by the existing four-cut wedge theorem, induced pentagons produce higher faces of the Alexander dual and defeat the earlier private-face argument. The new collapse handles all these higher faces simultaneously, even with overlapping pentagons, and proves that no lower-degree homology or torsion survives. This upgrades a known Euler formula to a homotopy theorem for an infinite class of graphs, including the dodecahedral graph with sphere rank 841. This is structural rather than a routine one-parameter numerical increment.

## Scope and residual risks
No assertions for fewer than nine vertices, triangles or squares, shellability, total cut complexes, natural equivariant equivalences, or publication priority. The proof is elementary but not independently audited. Similar unpublished or unindexed formulations could cover it.

Self-review: passed. Independent audit: not yet performed.
