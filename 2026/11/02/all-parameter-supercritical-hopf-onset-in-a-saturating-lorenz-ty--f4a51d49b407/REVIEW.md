# Scientific review

## Correctness
PASS. The exact complex reduction, unique equilibrium, frequency and real-part crossing speed follow directly from the stated vector field. A center-manifold invariance equation gives the quadratic mean coefficient; removing nonresonant quadratic terms gives the real cubic coefficient, which factors into a strictly negative expression for every admissible parameter triple. The nondegenerate Hopf theorem then gives the unique locally attracting periodic orbit and its leading amplitude. The attached `verify_hopf.py` checks the generic symbolic identity and three independent real multilinear calculations; the parameter-universal conclusion rests on the analytic factorization and Hopf theorem, not on finitely many tests.

## Originality
PASS on inspected evidence, with residual priority risk. The source's 2026 full text defines the self-review, proves its linear Hopf threshold, and observes an apparently supercritical transition numerically for one parameter choice, but does not derive a third-order Lyapunov coefficient or an all-parameter sign theorem. The 1982 complex Lorenz equations differ in their nonlinear coupling, while general Hopf formulas give only a method. Similar published computations on other Lorenz/Sprott systems do not cover these equations. Searches for the source title, saturation law, exact amplitude, and related first-Lyapunov computations did not identify a theorem implying the present factorization; absence from search is not proof of novelty.

## Mathematical value
PASS. The criticality of the numerically identified onset was not analytically classified over the admissible physical parameters. An everywhere-negative cubic coefficient excludes a generalized-Hopf transition at both nonzero thresholds and gives an exact leading, physical-signal amplitude constant. This answers a structural question about this particular model and enables quantitative local onset comparison; the conclusion is neither merely a stability linearization nor an arbitrary parameter substitution.

## Closest literature and limits
Khodabandehlou–Maes, arXiv:2609.21415v1, Sections II and V, is the principal and closest source. Fowler–Gibbon–McGuinness (1982) treats a different complex Lorenz system. Generic normal-form methods appear in the Scholarpedia Hopf reference. A 2024 modified reduced Lorenz-model article could be examined only at abstract level because its full-text host returned a rate limit; this and possible unindexed older feedback-oscillator papers remain historical-priority risks. The theorem is local and does not assert global uniqueness of the attracting state.

Self-review: passed. Independent audit: not yet performed.
