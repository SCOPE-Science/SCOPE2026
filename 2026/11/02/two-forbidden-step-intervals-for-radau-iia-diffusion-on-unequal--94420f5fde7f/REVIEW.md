# Scientific review

## Correctness — PASS

All four Laplacian eigenspaces and their projectors are explicit. The complete rational matrix has five entry classes: each off-diagonal class factors into a strictly positive expression for every positive step. Each diagonal class has an exact rational numerator with a quartic polynomial. The global minimum of the scalar Radau function proves all diagonal entries positive for at most eleven vertices. For at least twelve vertices, an explicit, distinct timestep for each vertex class makes its diagonal negative, proved by a uniformly positive quadratic with negative discriminant. Descartes' rule and the sign at zero/infinity force precisely two simple positive roots for each diagonal quartic and exactly the stated union of forbidden intervals. Rational root brackets prove that three safe windows occur on \(K_{2,10}\), while two safe windows occur on \(K_{5,7}\). The independent full-matrix rational verifier passed 30,768 assertions; it is supporting evidence, not the infinite proof.

## Originality — PASS on checked evidence

The closest accessible prior claim treats **balanced** complete multipartite graphs and covers only the equal-part case of this two-part family, deliberately excluded here. It has just one diagonal class and one forbidden interval. In contrast, distinct part sizes split the nonconstant spectral values and diagonal classes, producing two independent quartics and even three safe windows, a phenomenon not implied by replacing a parameter in the balanced result. The author's available original numerical-analysis literature concerns energy monotonicity, SSP perturbations, or a different integrator; the checked searches did not reveal an equal or stronger unequal-bipartite classification. Possible unindexed work and incomplete historical coverage are residual risks, not grounds for assuming novelty is established by silence.

## Value — PASS

Entrywise positivity is required when a numerical diffusion step is to preserve nonnegative concentrations. This theorem gives a natural family-wide exact step-size admissibility criterion and reveals a non-monotone safety set with up to three separated windows, structurally different from a single CFL-like threshold. The first failure at twelve vertices is universal for all unequal bipartite side profiles. The mathematical contribution is the complete two-quartic sign classification and coexistence of distinct safety-window patterns, rather than the already-covered equal-part specialization or routine matrix evaluation.

## Closest literature and limits

Hairer–Lubich (2013, https://doi.org/10.1093/imanum/drt031) prove energy results and stability-functional-calculus foundations without entrywise inequalities for this graph. Higueras–Ketcheson–Kocsis (2015, https://arxiv.org/abs/1505.04024) treat monotonicity-preserving perturbed Runge–Kutta methods, rather than the exact unperturbed endpoint map. The theorem does not identify an elementary inequality in \(p,q\) deciding interval overlap; it instead supplies roots that exactly determine the domain for every unequal pair. General graphs, other discretizations, intermediate stages and independent validation remain outside scope.

Self-review: passed. Independent audit: not yet performed.
