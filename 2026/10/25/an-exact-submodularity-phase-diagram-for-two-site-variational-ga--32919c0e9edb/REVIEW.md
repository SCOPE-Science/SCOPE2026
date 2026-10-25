# Review of the two-site variational free-energy submodularity classification

## Correctness — PASS

The fully specified Titsias objective yields exact two-by-two Nyström matrices for each of four inducing sets. The difference of their inverse quadratic forms diagonalizes in the symmetric/antisymmetric basis. A derivative factorization proves strict positivity of the scalar baseline, and elementary positivity proves both response coefficients. This gives an *if and only if* two-site characterization. A Schur-complement argument proves set monotonicity independently, while the rational special case has rigorously negative logarithmic defect. A Python standard-library checker independently reconstructs 1,343 direct-matrix cases. Finite cases are corroboration, not the universal proof.

## Originality — PASS, with qualified historical-priority risk

The 2026 pivot-selection source proves positive variational gains, not the data-dependent submodularity criterion. The older Cao–Brubaker–Fleet–Hertzmann selection framework gives related variational objectives, but inspected sections do not show the exact two-site quadratic region. Titsias defines the underlying objective. Krause–Singh–Guestrin's Gaussian mutual-information submodularity is a different set function. Published-record searches and semantic research-record searches used aliases including inducing subset, Nyström VFE, diminishing returns and correlated responses; no stronger implication or equivalent was identified. Older specialized literature or hidden formulations remain a residual risk, so priority is not independently certified.

## Value — PASS

Diminishing returns is the hypothesis behind standard submodular greedy guarantees. The exact phase diagram determines when that hypothesis is valid or invalid for the smallest nontrivial variational inducing-set problem. The weak-correlation limit demonstrates a robust failure mechanism despite nearly independent kernels. This supplies a mathematically motivated boundary and explicit counterexample, not simply a generic logdet identity.

## Scope and risks

The theorem is limited to two equal-variance candidates, positive correlations and the standard homoscedastic sparse-GP variational objective. No general multivariate characterization or greedy approximation ratio is claimed. Priority needs independent historical review.

Self-review: passed. Independent audit: not yet performed.
