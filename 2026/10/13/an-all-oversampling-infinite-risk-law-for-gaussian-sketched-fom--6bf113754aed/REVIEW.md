# Review

## Correctness

PASS. The scalar Galerkin and least-squares coefficients are exact. Orthogonal decomposition reduces each Gaussian sketch ratio to a standard Student law; the FOM reciprocal has a strictly positive density at its pole and therefore a \(1/t\) absolute tail for every finite sketch size. The energy-error decomposition proves that its unconditional squared energy loss has infinite expectation. The GMRES coefficient has a finite second moment exactly when \(\ell>2\), and its exact expected residual follows by quadratic expansion. The standalone checker verifies independent algebraic reductions; infinite risk is proved analytically, not inferred from finite sampling.

## Originality

PASS. The defining Güttel–Schweitzer sketched FOM/GMRES paper, the Timsit–Grigori–Balabanov randomized projection analysis, and the later Palitta–Schweitzer–Simoncini full-text analysis contain relevant conditional convergence and stability results but not the one-step reciprocal-Student coefficient law or the all-oversampling moment contrast. Focused semantic comparisons with related published findings did not identify an implication-equivalent result. Standard Student ratio facts themselves are prior.

Residual priority risk: an unindexed note, possibly from earlier randomized Gram–Schmidt work, might contain the same probability calculation. This does not invalidate the independently derived theorem, but limits any universal priority claim.

## Value

PASS. The discrepancy between high-probability sketch guarantees and unconditional mean-risk certification matters for randomized linear solvers: increasing finite oversampling suppresses the catastrophic event probability but never gives a finite FOM mean squared energy. The finite-risk one-step GMRES contrast identifies an intrinsic choice of projection, not a generic sketching failure.

Self-review: passed. Independent audit: not yet performed.
