# Scientific review

**Correctness — PASS.** The global bound follows from the piecewise-affine normal-fan decomposition of the Euclidean nearest-point map. The exact-rational checker exhausts all 8 three-point and 4,096 four-point subsets of triangle normals, computes the associated orthogonal projection row sums, and proves that none exceeds the stated factor. The displayed strictly positive finite input pair and its strictly positive KKT multipliers attain the four-point upper bound; the three-point facet case is attained analogously. The code was executed successfully on the present seven-file package's standalone checker source.

**Originality — PASS within examined evidence.** The 2004 and 2008 primary metric-nearness texts concern formulation, convergence and computation of minimizers, whereas this result gives the exact Lipschitz modulus between *two fitted outputs* under edgewise perturbation. Deza–Goldengorin–Pasechnik's four-point cone geometry identifies the cone but not the new projection-stability constant. Searches of published mathematical records for four-point metric-nearness perturbation constants found no implication or equivalent result. Historical priority remains provisional; an older exact small-cone projection computation is a residual risk.

**Value — PASS.** Edgewise measurement uncertainty is a natural input model in distance repair. Exact amplification distinguishes the first multi-triangle interaction from a single triangle, and the finite positive witness demonstrates realizable worst-case instability. The finite four-point cutoff is intrinsic: it is the first problem beyond a single triangle, not an arbitrary parameter choice. No higher-dimensional extrapolation is asserted.

The exact checker certifies a finite exhaustive calculation, not historical novelty or any unproved general case. A separate independent mathematical or bibliographic review has not been performed.

Self-review: passed. Independent audit: not yet performed.
