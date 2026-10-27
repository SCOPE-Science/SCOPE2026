# Self-review

## Correctness — PASS

The proof holds for every fixed finite dimension \(n\ge2\) and every nonsingular real symmetric indefinite matrix. The Gaussian direction is uniform on the sphere, and the rank-one approximation has unique nonzero eigenvalue \(\|Au\|_2^2/q(u)\). On the spherical null cone, \(\nabla_S q=2Au\neq0\), so coarea gives a continuously varying near-zero density and the surface coefficient. The reverse triangle bound transports the exact \(1/t\) coefficient to the residual. Integrating the tail gives the full positive-moment criterion. Weighted coarea applied to \(q\), rather than just a finite experiment, establishes the cutoff's logarithmic penalty. The closed-form two-dimensional example and the verifier supply independent algebraic sanity checks. It remains unproved here for singular indefinite matrices, higher rank, correlated probes, and finite-precision implementations.

## Originality — PASS (best-knowledge, subject to independent confirmation)

The motivating source already shows an unbounded indefinite Nyström error for a special sketch: that observation is **not** presented as original. The claim assessed here is the full Gaussian tail asymptotic for all invertible indefinite symmetric inputs, including the geometric coefficient, the if-and-only-if moment spectrum, and the exact leading hard-trimming penalty. Searches of relevant published records and archived claim summaries did not uncover a statement implying all three. Park–Nakatsukasa's source focuses on deterministic instability examples and stabilization; earlier generalized Nyström analysis uses independent two-sided sketches. Ratio-of-Gaussian-quadratic-forms literature is the main residual equivalence risk, and no claim of exhaustiveness is made for unindexed literature.

## Value — PASS

A high-probability Gaussian sketch can be almost surely defined yet have infinite mean spectral-norm error. This is a mathematically motivated assessment of numerical reliability, not an arbitrary special-case parameter. The sharp tail coefficient measures the risk of catastrophic cancellation for any fixed indefinite input; the matching logarithmic penalty quantifies the stability cost of a natural scalar-core rejection rule. The explicit signature family demonstrates the contrast between small prefactors and nonintegrability, while definite matrices form a precise structural boundary.

## Closest literature and residual risks

Park–Nakatsukasa (arXiv:2212.01127) is the closest source, because its rank-one generalized Nyström expression has the same denominator. It does not supply this complete Gaussian distributional characterization in the inspected source. Nakatsukasa (arXiv:2009.11392), Smith (1989), and later sketched indefinite linear-system works provide context; prior ratio-of-quadratic-form asymptotics might implicitly contain parts of this result. No independent novelty review has been performed.

Self-review: passed. Independent audit: not yet performed.
