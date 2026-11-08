# Review of a boundary-atom metric-star spline norm

## Correctness

**PASS.** The theorem's full parameter domain is an integer arm count \(m\ge2\) and a strictly positive atom mass \(w\). The arclength-plus-atom Hilbert-space inner product is positive definite on the \((m+1)\)-dimensional continuous piecewise-affine space. The proof computes the Gram inverse by a rank-one update, then computes the signed kernels at each vertex, including the atomic contribution. Positivity of explicit factored difference polynomials proves ordinary-leaf dominance; convexity and an actual strict sign conflict prove absence of interior maximizers. A positive-coefficient derivative certificate proves strict monotonicity, and the precise cubic equation proves the two-arm transition. The proof accounts for every equality case. Independent exact-rational Gram inversion and a symbolic identity checker ran successfully; finite tests are supplementary, not the basis of universal quantifiers.

## Originality

**PASS, with residual literature risk.** The closest previously available star model with a hub atom applies to a different supported measure and cannot imply a leaf-supported atom's exact norm or the movement of norming points from the perturbed leaf to the others. The ordinary atom-free case is an acknowledged limiting endpoint, not claimed as new. Oswald's 2006 full preprint concerns simplicial finite-element meshes, an interval upper bound, and a higher-dimensional instability construction; it does not provide a boundary-atom metric-star norm. Hangelbroek–Narcowich–Sun–Ward (2010), read through its projector and main-results sections, derives general bounds for kernel-generated approximation on manifolds, not the stated finite graph/Dirac model. Targeted published mathematical-record and primary-literature searches returned no equivalent or stronger theorem, but unindexed preprints and specialized graph finite-element notes remain possible. No negative search result alone is treated as a proof of originality.

## Mathematical value

**PASS.** Exact endpoint operator norms are natural stability invariants for least-squares finite-element projection. This theorem isolates how a single highly localized observation alters worst-case stability: arbitrarily small positive point mass increases the norm, yet the extremizers occur at the *unobserved* leaves, not at the observed location. The dimension-dependent crossing of norm \(2\) for precisely two arms, the monotonicity for every positive weight, the limiting constants and exact positivity-loss witnesses provide a complete, motivated classification rather than an arbitrary parameter sample.

## Limitations and closest sources

The result concerns real first-order continuous splines on unit-length metric-star arms with exactly one atomic mass at a leaf; it does not treat arbitrary edge lengths, interior knots, or multiple atoms. The main external comparisons are Peter Oswald, arXiv:math/0611573 (2006-11-19), and Hangelbroek et al., arXiv:1005.2424 (2010-05-13). An equivalent theorem in inaccessible specialist literature remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
