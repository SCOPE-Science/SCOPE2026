# Self-review

## Correctness
PASS. The density is an even logistic kernel multiplied by a known polynomial. Its first two raw moments are reproduced by parity, and the derivative signs give exact unique mean and variance turning points with polynomial positivity certificates on the entire real parameter domain. High-precision integration of the source density verifies the corrected table, including the opposite-sign mean for positive and negative skew parameter. The mismatch is incompatible with rounding.

## Originality
PASS for the source-specific moment-table and interpretation correction. The original publication already states correct analytic moments and plots their shapes; originality is not claimed for rederiving those formulas. It does *not* reconcile the following numerical table and misleading dispersion/mean claims with them. A related 2025 flexible alpha-skew logistic article has a different model. Focused table, DOI, equivalence, exact moment and turning-point searches did not locate a published reconciliation.

Residual risk: A later unindexed correction may exist, and the cause of the printed numerical error is unknown. The finding does not infer which implementation was used.

## Value
PASS. Dispersion and directional asymmetry are central advertised motivations for the model, and the numerical table is not simply rounded incorrectly: its values violate normalization-derived moment identities and the paper's own analytical variance bounds by orders of magnitude. The exact parameter phase identifies where variance really decreases and where it increases, materially correcting interpretations of model flexibility.

Self-review: passed. Independent audit: not yet performed.
