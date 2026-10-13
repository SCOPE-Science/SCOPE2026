# Review

## Correctness
PASS. Under the stated symmetric no-zero law, signs are independent Rademacher variables independent of magnitudes. Conditioning on the magnitudes makes any sign-blind ordering deterministic. Expanding the centered sum of squares shows that a run-change indicator correlates with exactly one quadratic sign product, producing \(-A_{\pi_j}A_{\pi_{j+1}}\) in the squared-sum term and hence the displayed positive covariance after the sample-mean subtraction. The conditional mean of the run count is constant, so no omitted covariance-of-conditional-means term remains. Exact arithmetic in `verify.py` reproduces the identity and its specializations.

## Originality
PASS. The closest full source, arXiv:1401.2377v1, defines McWilliams' absolute-value ordering and sign-run statistic and develops its invariance, null distribution, multivariate extension, and power properties. A full-text inspection found no sample-variance or covariance result. Claim-specific searches for McWilliams runs together with sample variance, absolute-rank runs with variance, and sign-run covariance returned no equivalent statement. The original McWilliams article was not available in full text through the lawful sources checked, so its body is retained as a residual risk rather than treated as negative evidence. The existing marginal distribution-free theory does not dominate the new claim: it fixes the law of the run count but does not determine the ordering-dependent mixed moment with centered variance.

## Value
PASS. Runs after center-outward ordering are a canonical nonparametric symmetry statistic, and sample variance is a canonical centered scale statistic. The theorem identifies a sharp structural boundary: the runs statistic is independent of all magnitude-only scale summaries, yet centering at the random sample mean creates a strictly positive dependence whose exact size is an adjacent-magnitude functional. This explains how a distribution-free sign statistic can acquire distribution-dependent second-order coupling with a standard estimator, and it yields closed finite formulas for common parent laws.

## Closest literature and limitations
Dyckerhoff, Ley, and Paindaveine (arXiv:1401.2377v1) give a complete accessible description of the McWilliams statistic and its null theory. McWilliams (1990) is the originating source but its body was not accessible in the checked lawful channels. Corzo and Babativa's modified symmetry-runs paper supplies directly relevant nonparametric-testing context and is classified primarily under \(62G10\). The theorem here assumes a known symmetry center and does not cover sign-dependent orderings or asymmetric laws.

Self-review: passed. Independent audit: not yet performed.
