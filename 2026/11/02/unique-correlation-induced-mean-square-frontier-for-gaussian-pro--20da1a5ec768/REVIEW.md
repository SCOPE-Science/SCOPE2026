# Scientific review

## Correctness

PASS. The exact method specializes from the published affine-forward-map discretization. The conditional Gaussian-noise expansion gives a stationary path-product moment formula. A positive compact Mehler-kernel operator converts this formula to an exact spectral-radius criterion with nonzero overlap of the top positive eigenfunction. The normalized Hermite decomposition proves a strictly increasing spectral radius, using the nonintegrability of the inverse multiplier on its zero sphere to rule out equality. Strong OU-semigroup convergence proves divergence of the spectral radius near unit correlation; the independence endpoint and rational witness are computed exactly. `verify.py` independently checks \(95\) finite exact-rational identities; infinite-horizon claims rest on the analytical steps, not these tests.

## Originality

PASS on available evidence, subject to a substantive historical-priority risk. The 2026 source treats a compact-state multiscale sampler and leaves noncompact Gaussian settings outside its proved scope. The 2021 original method describes numerical stiffness without this correlation monotonicity law. The 2024 SGD paper studies independently sampled batches, so it cannot directly imply the OU-persistent path-product threshold. The 1993 correlated-Gaussian LMS paper reports exact expectation recursions and mean-square step-size bounds and may contain a related specialization; its full text was not accessible during this comparison. The accessible abstract is insufficient to establish or exclude exact coverage, and a specialist comparison remains warranted. Classic Markov multiplicative functional spectral arguments are acknowledged.

## Mathematical value

PASS. A unique transition in noise temporal correlation, for every finite number of probes, is an exact design boundary for step sizes and OU time scales in a recently analyzed derivative-free sampling method. It explains why stable fresh-probe second moments do not guarantee stable finite-correlation second moments, even in the simplest Gaussian target. The theorem is not an assertion about general ergodicity or correctness of the numerical approximation under other assumptions.

Self-review: passed. Independent audit: not yet performed.
