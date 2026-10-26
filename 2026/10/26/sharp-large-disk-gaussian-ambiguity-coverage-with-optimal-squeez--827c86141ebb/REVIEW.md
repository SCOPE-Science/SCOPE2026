# Scientific review: Gaussian ambiguity squared-coverage minimax law

## Correctness

PASS. Gaussian integration with unit-norm normalization gives the stated squared ambiguity exponential, and radial monotonicity reduces the disk problem to its boundary. The largest circular gap provides a uniform exponential upper bound. At the equispaced construction, a two-term boundary-layer argument supplies the matching sharp prefactor, with all other Gaussian terms exponentially smaller. Combining the two estimates yields global optimizer rigidity and the explicit microscopic perturbation limit. The proof treats fixed \(m\ge3\) and separately resolves \(m\le2\); it never uses finite sampling as a substitute for an infinite or continuum argument. The stand-alone finite checker passed 86 assertions from its delivered path.

## Originality

PASS with qualification. Alaifari and Yang (arXiv:2410.05486, Section 2.1, Remark 2.1) already derive the rotated Gaussian ellipse geometry, and their denominator directly implies the optimal *exponential rate* for threshold-union coverage after elementary minimization. That rate by itself is **not new**. The assessed claim is the global optimization of the **squared ambiguity sum**, including the sharp pre-exponential factor, optimizer rigidity at separate angular and squeeze scales, and the full perturbation penalty. The cited source treats threshold ellipses and positive unsquared sums, not these exact squared least-squares multiplier assertions. Hardin–Kendall–Saff (arXiv:1208.5261) prove circle-polarization equispacing under convex geodesic potentials; this Gaussian potential has negative second derivative at the origin and is outside that hypothesis. Targeted literature searches did not locate a theorem dominating the assessed claim. Historical priority is provisional, with a residual risk from unindexed Gaussian polarization results.

## Value

PASS. The squared sum is the precise information multiplier for equal-variance linear inversion of jointly measured ambiguity channels. The result answers how many squeezed Gaussian windows are needed to beat isotropic large-disk decay, what the optimal per-channel amplification constant is, and how angular misalignment and squeeze errors degrade that constant on two different asymptotic scales. It therefore supplies a directly motivated spectral-conditioning design law and a sharp robustness profile; it does not claim a complete nonlinear phase-retrieval theorem.

## Limits and comparisons

The original paper's ellipse-intersection expression controls the same exponent in a different coverage objective, and its mathematical implication is expressly excluded from the novelty claim. Other optimization objectives, channel-dependent squeezing, unequal precisions, finite-radius exact optimizer uniqueness for \(m\ge3\), and growing numbers of channels remain unproved. Bibliographic absence does not prove uniqueness of discovery. The numerics only corroborate explicitly proved expressions.

Self-review: passed. Independent audit: not yet performed.
