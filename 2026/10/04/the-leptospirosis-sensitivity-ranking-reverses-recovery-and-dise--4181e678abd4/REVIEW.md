# Same-model review

## Correctness

PASS. The disease-free infected subsystem is reconstructed directly from the five printed model equations. Its next-generation matrix has characteristic polynomial
\[
z^2-az-c,
\]
which gives the stated spectral radius. The direct-plus-vector type threshold
\[
\mathcal T=a+c
\]
crosses \(1\) at exactly the same parameter boundary. Differentiating the exact formulas proves that \(\lambda_h\) has zero sensitivity and that \(\delta_h\) and \(\gamma_h\) have negative sensitivity under both conventions. Exact rational arithmetic reproduces the type-threshold table, and high-precision eigenvalue and finite-difference checks replay the spectral calculation.

## Originality

PASS. Next-generation and normalized-sensitivity methods are prior art. The earlier leptospirosis model already uses a direct-plus-vector threshold, so that construction is not claimed as new. The surviving contribution is the source-specific correction of the 2022 sensitivity paragraph and the exact ranking at its own parameter set. Searches by DOI, title, loss-of-immunity/recovery aliases, sensitivity terminology, and erratum terminology found no published correction.

## Value

PASS. The source says its sensitivity analysis is intended to identify parameters useful for reducing infection spread and informing controls. The corrected analysis changes that interpretation substantially: recovery and human disease removal decrease the invasion threshold, loss of immunity does not affect invasion at all, and the vector-mediated elasticities are tiny relative to direct human transmission for the source parameter set.

## Closest literature and limitations

The 2012 same-family leptospirosis paper provides the closest prior threshold formula and establishes the direct-plus-vector convention as prior. A 2013 host-vector paper develops related global threshold dynamics. A separate 2022 human-rodent leptospirosis model gives conventional signed sensitivity indices but does not cover the source-specific correction.

The report distinguishes the standard next-generation spectral radius from the threshold-equivalent human-generation quantity because their numerical elasticities are not identical away from the invasion boundary. The sign correction is common to both.

Same-model review: passed. Independent audit: not yet performed.
