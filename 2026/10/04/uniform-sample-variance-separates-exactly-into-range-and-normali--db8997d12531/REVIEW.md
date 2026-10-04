# Review

## Correctness

PASS. The ordered-uniform density is constant, and the minimum/range/interior-shape transformation has Jacobian \(r^{n-2}\). The transformed density factors exactly, proving independence of the normalized interior shape from the two endpoints. Since \(S^2/R^2\) is a function only of normalized shape, the claimed independence follows.

The mean normalized variance is reconstructed directly from a configuration with fixed endpoints \(0,1\) and \(n-2\) iid uniform interior observations. The range has the beta \((n-1,2)\) law, so the all-power covariance is an exact moment calculation. The sign is strictly positive for every \(q>0\).

## Originality

PASS, with a specific residual risk from classical spacing theory. Papadatos's full arXiv article was inspected at its range problem, historical review, and MSC statement; it optimizes expected range under moment information and does not treat sample variance conditional on range.

The full 2026 Cheng--Hu--Lin article was inspected at its range-versus-standard-deviation setup, its uniform-range beta moments, and its applications section. It explicitly notes that same-sample range and standard deviation are generally dependent, but does not state the normalized-variance independence, conditional regression, or covariance formulas here.

Targeted exact-formula, independence, normalized-spacing, and studentized-range searches did not locate the combined statement. The normalized-spacing factorization itself is classical in spirit, so originality is claimed only for the sample-variance consequence and closed covariance family.

## Value

PASS. Range and variance are two of the most basic same-sample dispersion summaries, and their dependence is central to studentized-range ideas and range-versus-standard-deviation comparisons. The result gives a complete and unusually simple dependence decomposition for the canonical bounded location-scale model.

The independence of \(S^2/R^2\) from the endpoints is stronger than a covariance calculation, while the exact regression and all-power covariance formulas make the structural fact directly usable.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK normalized_mean_checks=399 range_moment_checks=6783 covariance_identity_checks=7980 positivity_checks=7980 q1_checks=399`.
