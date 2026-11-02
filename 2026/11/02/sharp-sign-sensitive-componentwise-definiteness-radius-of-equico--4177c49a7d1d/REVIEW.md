# Scientific review: equicorrelated Gram interval radius

## Correctness — PASS

For any admissible symmetric entrywise error, the quadratic form is bounded below by an explicitly defined sign-vertex quadratic form. With negative correlation a single coherent vertex dominates; with positive correlation the sign vertices split into two constant blocks, whose orthogonal-complement eigenvalues and a two-by-two determinant prove the radius. Balanced partitions minimize that determinant threshold, and explicit kernel vectors certify the sharp boundary. The zero-correlation case is diagonal. The proof includes all parameters and both strict and equality cases. The adjacent `verify.py` independently passed 1,512 exact-rational vertex calculations across 36 settings, but finite computation is only corroboration.

## Originality — PASS, with priority limitations

The motivating work by Balabanov, Melnichenko and Mahoney (arXiv:2610.16101v1) analyzes randomized Q-less Cholesky QR and componentwise error shaping, not the exact equicorrelation symmetric-entry robustness radius. Rohn's 1994 interval-positive-definiteness characterization and Roustant–Deville's 2017 compound-symmetry block-reduction theorem provide genuinely relevant antecedents and already cover the *general method* of reducing sign vertices to small blocks. The additional claim is the explicit optimization across all sign patterns, the signed-correlation dichotomy, the attained rational/square-root threshold and the exact parity dependence. Demmel's componentwise distance framework and Rump's structured perturbation results were compared at the claim/parameter level, not treated as absent based on title mismatches. A prior equivalent special-function formula is possible. Full-text access to Rohn (1994) and Rump (2003) remained incomplete, so historical priority is not independently established.

## Value — PASS

The complete sharp radius is a natural conditioning invariant of a structured positive-definite Gram family under a standard relative-entry uncertainty model. It identifies a worst perturbation, provides an explicit no-failure interval, and shows exactly where a condition-number-only estimate loses sharpness due to dimension parity. It can serve as a transparent benchmark for relative-error budgets in Gram-based numerical methods, without asserting that real floating-point errors are independent or attain the worst case. This is an exact self-contained matrix-conditioning fact, not a claimed general solver-convergence theorem.

## Remaining scientific boundaries

No extension is established for arbitrary Gram matrices, nonsymmetric uncertainties, actual machine-error correlations, or numerical factorization of a boundary matrix. The general interval-matrix and block-correlation reductions are credited prior results. Some plausible older full texts could not be retrieved for complete priority inspection.

Self-review: passed. Independent audit: not yet performed.
