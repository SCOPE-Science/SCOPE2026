# Review: exact membrane current fluctuations

## Correctness: PASS

The flux conditions in the primary model determine the tilted cell boundary operator (5). Its scalar eigenvalue determinant is (1); a positive compact semigroup identifies the principal root. A monotone real branch, analytic perturbation, and implicit derivatives establish the full current SCGF and the drift/diffusivity. Exact symbolic identities, the one-way reflecting/Robin renewal calculation, and finite-lattice spectral approximations passed the package's checks. The renewal limit independently gives \(22/81\), whereas the primary paper's printed equation (26) gives \(43/162\).

## Originality: PASS

Section III.A and appendix D of Kay--Giuggioli (arXiv:2406.07142) establish the model and long-time transport but do not explicitly report the tilted characteristic equation or full crossing-current large deviations. Reflecting-current large deviations (arXiv:2102.04846), symmetric semipermeable spectral transfer (arXiv:1807.06336), and a single-membrane renewal construction (arXiv:2209.09176) are closest methodological antecedents, not identified as covering the jointly asymmetric exact formula. Semantic searches and previous accessible claims supplied no covering counterpart. It is possible that an equivalent formulation exists in older transfer-operator literature or an unindexed correction; notably, the 1992 Powles et al. full text was not directly checked. The comparison targets the **printed** 2024 equation and does not assert that a later erratum is absent.

## Mathematical value: PASS

A full current fluctuation generating function, not only first two moments, is a natural missing observable for biased diffusion in membrane arrays. Its exact rate symmetry links transport to statistical-mechanical fluctuation relations. The independently certified variance discrepancy affects a central physical coefficient in the motivating model, making this a motivated structural correction rather than a routine parameter specialization.

## Scope and limitations

Identical, equally spaced, one-dimensional membranes with constant parameters and positive permeabilities only. The all-current rate function is implicit. Finite-grid numerical calculations are auxiliary. No random-barrier or non-Poisson extension is proved. Full bibliographic uniqueness is unproved.

Self-review: passed. Independent audit: not yet performed.
