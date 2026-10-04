# Review

## Correctness
PASS. The claim reduces the bMGP covariance pair \((\Sigma_0,\Sigma_0+\Sigma_\star)\) to its generalized eigenvalues. Whitening gives the exact limiting quadratic form \(Q=\sum_i(1+\lambda_i)^{-1}Z_i^2\). Monotonicity yields the unique level-specific ellipsoid scalar, Rayleigh-quotient extremality yields the all-contrast threshold, strict pathwise spectral bounds yield their anisotropic separation, and chi-square upper-tail comparison yields their high-confidence coalescence. The proof distinguishes asymptotic statements from the illustrative finite numerical check.

## Originality
PASS. Tanaka (2026) already shows that scalar generalized-posterior calibration is level-specific and that all-level Gaussian calibration requires proportional posterior and sampling covariance; those statements are therefore not claimed as new. The motivating bMGP paper establishes conservative covariance addition but does not state the surviving result checked here: for anisotropic bMGP mismatch, the exact scalar for a chosen joint ellipsoid is strictly below the sharp scalar threshold required to prevent undercoverage for every linear contrast, with the two thresholds converging at extreme confidence. Matrix-valued sandwich/location-scale calibration is broader but addresses a different transformation class.

## Value
PASS. Conservative bMGP calibration can produce substantially wider regions than necessary. The result identifies exactly how much scalar contraction is possible for a chosen joint credible ellipsoid without rerunning predictive simulations or rotating draw directions, and it proves the unavoidable price of that contraction for at least one linear contrast. The spectrum gives an interpretable anisotropy diagnostic, and the extreme-confidence limit explains when the distinction disappears.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations
The closest sources are Wang--Fong--Frazier's bMGP covariance theorem, Tanaka's scalar generalized-posterior coverage calibration theory, Huggins--Miller's bagged-posterior covariance analysis, and matrix-valued sandwich/location-scale posterior adjustments. The present result is asymptotic and scalar-constrained. It does not claim generic level-specific scalar calibration, proportional-covariance characterizations across all levels, or matrix-valued covariance calibration. Plug-in covariance estimation and finite-sample coverage are not established here.
