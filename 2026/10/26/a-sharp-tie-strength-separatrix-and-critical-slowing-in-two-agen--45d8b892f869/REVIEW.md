# Mathematical review: A sharp tie-strength separatrix and critical slowing in two-agent adaptive opinion dynamics

## Correctness
**PASS.** Starting from the original normalization, the two-variable vector field is derived without changing units or tie normalization. Direct differentiation proves the conserved quantity. The opinion gap decreases, and its ordering relative to the unique maximum of the analytic potential forces the exhaustive consensus, polarized, and critical cases. A second-order Taylor expansion at the critical gap and the flow equation establish both sharp asymptotic coefficients. The admissible opinion range gives the sharp global decay-parameter threshold. Numerical checks (128 assertions, `verify.py`) independently corroborate selected differential identities and trajectories but are not used as infinite-time proofs.

## Originality
**PASS under best-knowledge search, with residual priority risks.** Nugent, Gomes, and Wolfram, arXiv:2305.09483v1, introduced the precise dynamic weights model and the logistic and exponential response choices; the qualitative possibility of weight-driven clustering is prior. Inspected sections on the model, proved properties and discussion do not give this sharp two-agent first integral, exact initial-weight separatrix, or critical rates. Kan, Feng, and Porter, *Journal of Complex Networks* 11 (2023) cnac055, study discrete network rewiring rather than the same flow. Semantic mathematical-record and primary-literature searches under model, separatrix, special-function, and critical-slowing equivalents found no directly subsuming statement. Possible broader ODE-equivalence results and only partially inspected historical work remain a real priority risk; nonappearance in search results is not considered a novelty proof.

## Value
**PASS.** The phenomenon is mathematically and socially motivated: an always-positive receptiveness is insufficient for consensus when the relationship is dynamically weakened. A sharp threshold in the initial relationship strength and explicit slow critical scaling separate three qualitatively different long-term outcomes of the minimal social tie. The result gives a reusable benchmark for testing adaptive-opinion numerical models, not a cosmetic finite instance or unsupported general-network claim.

## Limitations and relationships
The statement is specific to two reciprocal agents, self-degree normalization, unit-rate logistic edge evolution, and exponential receptiveness. It does not establish behavior for directed/multinode graphs, stochastic rewiring, or other interaction rules. The proof is self-contained but the literature assessment is not independent or exhaustive; the scientific scope and residual risks are detailed in AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
