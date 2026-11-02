# Scientific review: diameter--degree heterogeneity in permutation trees

## Correctness (C) — PASS

The original permutation-tree encoding gives the exact degree multiset and diameter; all statements use the same uniform model and explicit finite ranges. A uniform extra cut splits \((r+1,1)\) into \((a+1,c+1)\) and is a strict majorization step, establishing conditional ordering for every strictly convex degree cost. Stars-and-bars, the pair-in-one-run identity and a formal composition generating function prove the exact conditional expectation, covariance, and variance. The iid geometric renewal-reward theorem establishes the two-statistic CLT with variance limits 1/4 and 24 and cross-covariance -2. The included checker reconstructed inversion graphs and passed 14,234 exact assertions; these finite tests supplement but do not replace the proof.

## Originality (O) — PASS, qualified

Acan and Hitczenko, arXiv:1406.3958 (2014), own the exact run encoding, diameter marginal, and fixed-degree-count CLT. Their source was inspected in full where accessible; the existing encoding is not claimed as new. A complete published result on uniform-composition part-count/maximum dependence proves the same uniform extra-cut coupling and decreasing maximum, so those are also prior art. The full-degree-vector majorization strengthened by strict split comparisons and the exact Zagreb--diameter covariance, variance, and persistent \(-\sqrt{2/3}\) correlation were not in those inspected claims. Comparison with Bender and Canfield's general composition asymptotic framework and searched equivalent formulations found no dominant result. This is a best-knowledge comparison, not a certification of historical priority; older weighted-composition analyses remain a risk.

## Mathematical value (V) — PASS

Diameter measures global path length whereas the first Zagreb index measures concentration of local degrees. The all-convex degree-sequence coupling is a structural dependence law; the explicit conditional regression and strictly negative covariance quantify it, and the bivariate CLT shows the dependence persists at a sharp nonzero correlation scale. This goes beyond a scalar example or a fixed-degree count and supports statistical comparison of degree heterogeneity across conditioned random-tree samples.

## Scope and limitations

Only uniformly chosen permutation-graph trees are covered. The diameter-conditioned degree vectors are ordered in majorization, not coordinatewise by vertex labels. The convergence statement gives no finite-size normal approximation error. The proof uses earlier run encoding and an earlier uniform-cut coupling and claims neither as newly invented. A related result's strongest inspected claim concerns the maximum part; the quadratic-index dependence appears to be an unreported specific extension. Independent auditing has not been carried out.

Self-review: passed. Independent audit: not yet performed.
