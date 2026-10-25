# Scientific review

## Correctness — PASS

The top down-Laplacian is derived from oriented facets as \(L_n=nI-ss^{\mathsf T}\). In even order its two sign-class vertex simplices lie in orthogonal zero-sum subspaces, and the polar-product calculation gives the inradius while the vertex barycenter certifies the minimum enclosing sphere. In odd order, the exact barycentric coordinate gradients certify the unique incenter; the majority-sign vertex barycenter certifies the enclosing ball and a strict squared-radius deficit for all other vertices. The derivation covers all integers \(n\ge3\), uses the intrinsic metric, and does not rely on finite enumeration. An independent boundary-incidence/Qhull/linear-program calculation verified the analytic formulas for \(3\le n\le10\). Risk: any implementation relying on a changed orientation without a corresponding signed orthogonal coordinate transformation would be a different Euclidean realization, so the canonical metric convention is essential.

## Originality — PASS, with residual bibliographic risk

The closest full-text primary work is Juhnke-Kubitzke–Köhne, arXiv:2301.11602, which gives the exact matrix and the parity-dependent combinatorial types, but not these sharp Euclidean metric radii and contact sets. The published unimodular equivalences are not isometries, so their lattice-volume and \(h^*\) formulas do not imply the metric results. Braun–Meyer, arXiv:1706.07085, is about graph Laplacians, whose row-sum-zero operator differs from the top simplicial down-Laplacian. Indexed results on tree or vertex-transitive graph Laplacian simplices have distinct hypotheses and objects. An unindexed direct Euclidean analysis of this particular boundary-simplex family remains a possible overlap, and text access to some indexed findings was limited to their summaries.

## Mathematical value — PASS

This gives a complete intrinsic inball and minimum-sphere classification for the canonical geometric family singled out in arXiv:2301.11602, including exact unique centers and contact patterns. In odd order, only the majority sign-class vertices support the enclosing ball; in even order, all vertices do. The geometric aspect ratio grows like \(n^{3/2}\) along odd orders but like \(n/\sqrt2\) along even orders, despite a longest-to-shortest edge ratio tending to one. This is a concrete high-dimensional caution against inferring Euclidean fatness from nearly equal edge lengths or parity-insensitive lattice data.

## Scope and independent status

The finite checker is supporting evidence, not an all-dimension proof. The classification concerns the original Euclidean column realization; it does not extend to arbitrary unimodular images. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
