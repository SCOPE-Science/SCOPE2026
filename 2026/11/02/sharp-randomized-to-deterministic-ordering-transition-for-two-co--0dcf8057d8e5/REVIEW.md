# Scientific review

## Correctness — PASS

The component-gradient compositions give the exact scalar affine recursion at epoch boundaries. Its strict contraction ensures a unique stationary law, with exact stationary mean and variance. Differentiation produces a strictly convex quadratic in the order probability; checking both possible endpoint constraints yields the unique sharp curvature-dependent threshold. The asymptotic comparison follows from Taylor expansion. The complete algebraic proof is in `RESULT.md`; the standalone exact checker verifies symbolic stationary identities, phase thresholds, examples, and 108 finite-horizon moment comparisons for six rational settings. Finite checks are corroborative only.

## Originality — PASS, qualified

Rajput, Lee and Papailiopoulos (arXiv:2102.09718, §§4–6 and relevant appendices) prove general benefits of nonrandom and reversed permutations, but do not give a stationary-risk minimizer over all iid two-order probability laws for unequal-curvature scalar quadratics. Mohtashami, Stich and Jaggi (arXiv:2202.01838, §§3–4) use a gradient-prefix discrepancy; its squared value is identical for both permutations in this two-component family, so their statistic does not imply the exact optimal distribution. Domingo-Enrich (arXiv:2206.00632, §§3, 5 and Appendix C) studies uniform reshuffling using a common-Hessian approximation, not the exact heterogeneous-Hessian dynamics and biased order minimization here. Record searches for biased, curvature-weighted and nonuniform random reshuffling did not identify a stronger result that implies this phase boundary. This is evidence of a specific unresolved gap, not proof of worldwide novelty; relevant specialized ordering work remains a risk.

## Value — PASS

This is the complete optimal distribution within a natural, implementable fixed-budget, independent-epoch randomized reshuffling class. The sharp transition between true randomization and deterministic selection identifies qualitatively different optimal policies. More strongly, for nonidentical curvatures the exact optimal law removes the \(O(h^2)\) leading stationary risk of uniform shuffling, obtaining \(O(h^3)\) without extra gradient evaluations, with a ratio diverging like \(1/h\). The equal squared-prefix discrepancy of the two permutations shows why an existing coarse ordering diagnostic misses the effect. The contribution is intentionally narrow and does not assert global superiority over time-varying or adaptive ordering schedules.

## Closest literature and residual risks

The references and source comparisons are enumerated in `RESULT.md` and `AUDIT.json`. General random-order advantage, common-Hessian variance approximations and order-dependent convergence bounds predate this finding. Remaining risks are specialist analyses of biased permutation distributions and alternative order-schedule families outside the independent fixed-probability class.

Self-review: passed. Independent audit: not yet performed.
