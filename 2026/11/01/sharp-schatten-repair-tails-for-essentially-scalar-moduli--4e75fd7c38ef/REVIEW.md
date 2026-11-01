# Scientific review

## Correctness (C) — PASS
The precise hypotheses are an invertible operator with modulus a compact self-adjoint perturbation of a positive scalar identity and a finite rank budget on subcritical singular directions. Compactness of the shifted modulus after correction, the codimension-intersection min--max lower bound, the polar-aligned clipping extremizer, and the all-\(p\) Schatten infimum are proved in RESULT.md. The proof uses an infinite-dimensional min--max argument and does not extrapolate finite tests. The executable checker supplies 3,000 supplementary finite assertions.

## Originality (O) — PASS (best knowledge)
Su and Zhang, arXiv:2609.37621, establish the qualitative membership and compact-perturbation spectral criteria for \(eta_0(H)\). Bala and Golla, arXiv:2607.15222, characterize full Schatten deviations from scalar partial isometries. The inspected public record on polar-fiber density treats operator-norm approximation with no ideal restriction; the inspected public AN-distance record treats operator-norm distance. None of those inspected statements supplies the claimed universal pointwise singular-value lower bounds, sharp all-\(p\) correction costs, or one-sided Schatten repairability dichotomy. Statement-to-implication searches are detailed in AUDIT.json. Residual risk: an equivalent spectral-clipping/min--max theorem could exist under other terminology.

## Mathematical value (V) — PASS
The exact cost of restoring reducing-subspace norm attainment under a prescribed budget of subcritical spectral directions is a natural quantitative problem following the published perturbation stability and instability results. Simultaneous optimality for all singular values, not just one norm, and the inability of arbitrary noncommuting corrections to improve these costs give a complete, reusable structural invariant. One-sided Schatten repair can hold even when full scalar-unitary Schatten approximation fails, and finite-rank repair can remain impossible.

## Scientific scope and limitations
The result concerns invertible essentially-scalar-modulus operators and the modulus-defined class \(eta_0(H)\), not the whole class \(eta(H)\) or general essential spectra. Correctness is an analytical argument supplemented by finite numerical checks. Search incompleteness and independent mathematical assessment remain outstanding.

Self-review: passed. Independent audit: not yet performed.
