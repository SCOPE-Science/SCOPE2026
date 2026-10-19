# Scientific review

## Correctness — PASS
The exact projector law uses an independent Gaussian inverse-Wishart quadratic form with residual \(n-\ell\) degrees of freedom, proved by a column-rotation Schur complement. For fixed width the Gram matrix converges to an identity-plus-rank-one matrix; its top mode dominates the initial coordinate coefficient at every positive power, uniformly in the power index. Bounded singular-value conditioning transmits that fact to the original rangefinder and proves the joint chi-square limit. The continuous no-ties joint law gives the sharp improvement probability, and a rank-one Loewner sandwich gives spectral-error and expectation claims. The included checker passed direct projector, iterate, and spectral-error checks. Simulations do not substitute for the convergence proof.

## Originality — PASS, with residual risk
The closest method is Chang and Yang's 2026 sketch-power algorithm, which defines exactly the powered operator and establishes general error bounds; the inspected full text does not establish the present fixed-width spike joint law or uniform-in-positive-iteration saturation. Chenakkod and Dereziński (2026) use sketched-power iteration with initialization inside the auxiliary sketch range rather than the independent initial sketch used here; their norm inequalities do not imply this chance-of-regression formula. Classic Wishart and beta results already imply the exact projector ceiling, which is credited and not separately presented as novel. The prior one-spike ellipsoid section-radius calculation has a related beta transform but a different object and no power recurrence. Unindexed or terminologically different prior literature could overlap.

## Value — PASS
For a critically scaled spike, more independent sketch-power iterations cost computation but offer no further asymptotic leading-vector capture after the first. The exact event probability \(1-1/\sqrt2\) that a two-column auxiliary sketch reduces capture relative to the raw independent initialization distinguishes expectation from per-instance performance and helps determine whether to spend resources on additional powers or sketch width. This natural finite-width threshold is a motivated algorithmic accuracy/risk result, not a routine numerical recomputation.

## Scope and outstanding limits
The claim assumes real standard Gaussians, a single scaled spike, fixed auxiliary width and exact arithmetic; it neither gives finite-dimensional monotonic improvement nor covers the two-sided oblique approximation estimator. Independent scientific audit remains unperformed. Literature coverage cannot prove global uniqueness.

Self-review: passed. Independent audit: not yet performed.
