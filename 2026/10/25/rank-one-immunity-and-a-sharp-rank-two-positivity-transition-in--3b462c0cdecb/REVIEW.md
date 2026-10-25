# Scientific review

## Correctness
PASS. The asserted update is the exact specialization of the published projected exponential Euler equation. Its tangent projection and three-dimensional eigendecomposition give a necessary-and-sufficient rank-two spectral-selection criterion. Positive eigenvalue dominance proves universal rank-one semidefinite preservation. Embedding proves the minimal rank and dimension, while a direct comparison of spectral truncation residuals gives the repair-cost ratio. The attached verifier checks all nontrivial formulas and matrix reconstructions. Exact statements, not sampled runs, establish the universal claims.

## Originality
PASS under available published-literature and mathematical-record comparisons, with publication-priority uncertainty. The source publication [1] supplies the algorithm and convergence analysis; it does not formulate the rank-one immunity/rank-two transition for positive Lyapunov evolution. Kressner et al. [2] explicitly document indefinite low-rank Lyapunov approximations and positive-part correction in another Krylov algorithm; those qualitative facts and general spectral remedies are prior work. Schmidt et al. [3] use different low-rank covariance factorization machinery. No retrieved result provides the exact damped-step threshold, minimal-rank dichotomy, and repair-cost ratio for the projected exponential Euler map of [1]. Equivalent specialized calculations might exist outside inspected sources; absence from search results is not proof of priority.

## Value
PASS. Approximate Lyapunov covariances must be positive semidefinite for direct probabilistic use. The finding exposes a precise rank-dependent limitation of a motivated low-rank integrator even with a stable scalar drift, positive forcing and exact matrix functions. It gives the full parameter boundary and shows why a timestep restriction cannot be uniform as the smallest retained covariance eigenvalue vanishes. The unbounded loss of Frobenius optimality under positive-semidefinite repair quantifies a genuine design tradeoff, without asserting instability or inadequacy of other integrators.

## Scope and risks
The theorem concerns exact one-step operations and the stated scalar drift. Published work already explains general indefinite approximations, so priority attaches only to the narrow exact classification. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
