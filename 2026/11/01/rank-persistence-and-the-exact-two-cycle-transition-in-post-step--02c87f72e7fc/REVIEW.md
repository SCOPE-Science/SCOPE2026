# Review of the exact polar spectral-decay classification

## Correctness
PASS. The signed SVD basis persists because the correction is a polar factor of a scalar multiple of the current matrix. For each nonzero spectral coefficient, exact iteration reduces to \(r\mapsto|sr-\tau|\), which is a strict contraction with positive fixed radius. The unique chains of positive preimages of zero are computed exactly, proving completeness of the exceptional set. Eventual sign behavior distinguishes a matrix two-cycle from a fixed point, and soft thresholding follows a different recursion. The embedded verifier returned `CHECKS_OK 156222` for its supplementary finite checks. Risk: practical approximate polar and floating-point thresholding are outside the proof.

## Originality
PASS with priority qualification. The motivating October 2026 work supplies the un-clipped post-step polar update and remarks on subthreshold crossing, but its inspected Section 4 and Appendix A do not give the complete long-time rank classification, isolated gradient resonance, and exact zero-preimage formula. Classical subgradient cycling, genuine proximal SVT, and known polar-gradient or SVT rank-staircase analyses are not independent novelty claims here. The distinctions are iteration identity, clipping versus nonclipping, rank-loss exception set, and matrix asymptotic limit. Risk: stronger older results on constant-step signed spectral shrinkage could subsume this specialization.

## Value
PASS. Persistent full rank and limiting equal singular values are directly relevant to interpreting a numerical regularizer intended to concentrate matrix spectra. The exact resonance set quantifies how rarely rank can drop in exact arithmetic, and the step-size transition separates a two-cycle, complete termination, and a spurious positive-rank fixed point. This provides a concrete benchmark for selecting true proximal clipping or assessing finite-horizon versus asymptotic claims. The value is in the algorithm-specific matrix classification, not the elementary scalar contraction alone.

The scope is centered isotropic quadratic loss, constant gradient step, and exact minimum-norm polar factor. No claim is made about adaptive optimizers, noisy gradients, or approximate Newton--Schulz implementations. The 2026 originating paper, earlier soft-thresholding literature, published related numerical findings, and sign-method cycling examples are the closest comparisons.

Self-review: passed. Independent audit: not yet performed.
