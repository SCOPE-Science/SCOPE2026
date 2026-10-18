# Scientific review

## Correctness: PASS

The proof is complete for every real full-rank two-column input and every positive integer sketch-row count: rank-one residual identities, an exact diagonalization of a Gaussian quadratic-form difference, an independent chi-square ratio, the symmetric-beta comparison for sketch counts at least two, the balanced-column sharpness family, and the Cauchy one-row counterexample. All hypotheses, normalizations and extremal limits are explicit. The standalone checker passed 21,092 consistency checks; finite tests do not substitute for the analytical argument.

## Originality: PASS, with stated bibliographic risk

The closest motivating 2025 manuscript uses an oblivious-subspace-embedding hypothesis and high-probability strong rank-revealing bounds; the present unconditional two-column law compares Gaussian maximum-sketch-norm pivoting to norm-squared sampling and establishes the sharp sketch-row threshold. Exact risk comparison is not a direct corollary of the inspected general high-probability results. Published prior records about adaptive randomized pivoting, complete-pivot ACA and Gaussian sketching concern different pivot rules or different error outcomes. Duersch--Gu 2017 is a plausible overlapping source that was not available in full; novelty remains a best-knowledge judgment, not a uniqueness certificate.

## Value: PASS

The minimal sketch dimension that suppresses arbitrarily large *mean-square* pivoting losses is a natural question for Gaussian-sketched QR and column subset selection. A sharp constant and its exact finite-dimensional law quantify the trade-off even under unbounded condition numbers. The result is limited to one pivot on two columns and does not claim broad algorithmic acceleration.

Self-review: passed. Independent audit: not yet performed.
