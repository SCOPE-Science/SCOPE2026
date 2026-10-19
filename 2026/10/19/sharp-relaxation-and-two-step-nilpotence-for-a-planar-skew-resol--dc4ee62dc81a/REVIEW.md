# Scientific review

## Correctness — PASS

The stated map and domain are exact: \(q,c,\tau,\rho>0\), fixed 2-dimensional real iteration, universal convergence over all starts. Matrix inversion gives the displacement trace \(t\), determinant \(d\) and discriminant \(\Delta\). Positive real roots and conjugate roots yield exhaustive Schur boundaries. Equioscillation or strict convexity gives unique relaxation optima. Requiring zero eigenvalues determines the unique discriminant-zero step \(\tau_*\) and relaxation \(\rho_*\). Cayley--Hamilton supplies the square-zero identity while an off-diagonal entry proves the matrix itself nonzero. The standalone exact-rational and randomized reproduction checks pass. Numerical sampling is not used to infer any global or infinite assertion.

## Originality — PASS, with bounded residual risk

The September 30, 2026 motivation establishes an abstract forward--backward representation and nonexpansiveness/relaxation sufficiency, not this 2-by-2 skew-resolvent's exact Schur phase diagram, universal two-step termination threshold or unique tuning. The classic monotone-plus-skew paper instead analyzes a forward--backward--forward map. Nearby published descriptions of PDHG and ADMM finite termination concern different recurrences and cannot directly imply the statement. Actual semantic and alias searches were made; accessible previous claims were checked. Novelty is assessed as best knowledge, not as certification of absence from all publications. Related published records whose full bodies were not accessible remain residual risks.

## Value — PASS

The criterion \(q<2c\) is a sharp structural feasibility boundary for exact finite-step convergence of a natural two-parameter primal--dual fixed-point iteration, not an arbitrary isolated example. The complete piecewise rate and Schur formulas distinguish stability, rate optimality and nilpotence and explain why valid model-specific tuning can exceed generic relaxation values. Potential use is a calibrated numerical benchmark for splitting and parameter-selection claims; the result does not assert practical robustness or large-scale gains.

## Closest work and scope

Zhang--Liu--Zhang (arXiv:2609.38808v1), Briceño-Arias--Combettes (arXiv:1011.5517v1), and published records on scalar PDHG fixed-product tuning and warm-start over-relaxed ADMM are the closest comparisons. The exact result is restricted to the displayed constant skew-resolvent matrix, not anchored acceleration or ADMM.

Self-review: passed. Independent audit: not yet performed.
