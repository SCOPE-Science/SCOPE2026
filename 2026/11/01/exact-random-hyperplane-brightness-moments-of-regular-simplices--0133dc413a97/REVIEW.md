# Self-review

## Correctness (PASS)
The theorem uses the published all-direction simplex projection formula with its exact Euclidean normalization. A Gaussian projection onto the zero-sum subspace gives coordinate variances and correlation \(-1/(m-1)\); the spherical first-coordinate beta integral yields the mean, while Gaussian covariance differentiation yields the bivariate absolute-product expectation and hence the exact second moment. Gamma-ratio and elementary Taylor expansions establish the sharp \(m^{-1}\) variance correction. The proof explicitly couples centered Gaussian absolute sums to independent Gaussian sums, incurring \(O_{\mathbb P}(m^{-1/2})\) after normalization; the earlier cube-width CLT then applies without claiming a new limit theorem for the cube. All assertions quantify over integer \(m\ge3\). The separate standalone verification code passed 210 deterministic assertions; finite tests supplement rather than replace proof.

## Originality (PASS with priority risk)
Primary full texts inspected: Pandis, arXiv:2601.18436, and Jakimiuk–Pandis, arXiv:2610.23489, prove projection identities, extrema and stability but not Haar-normal brightness moments. Kabluchko–Litvak–Zaporozhets, arXiv:1511.08479, treats random line-widths and includes an exact cube CLT; this establishes the *limit law* after the present transfer but neither the zero-sum finite moment formulas nor the finite-size correction. Affentranger–Schneider (1992) appears in accessible abstracts as a face-count paper; its full text was not read, so historical coverage cannot be ruled out conclusively. Relevant indexed-result and literature searches did not identify a dominating exact moment formula. The limit alone is not asserted as independent novelty.

## Value (PASS)
Haar-random hyperplane projection volume is a natural stochastic counterpart to the currently active deterministic extremal and stability theory of regular simplices. The exact finite-dimensional dispersion and its sharp first correction answer how much projection volume varies in typical orientations and supply an explicit high-dimensional benchmark beyond first-moment Cauchy formulas. The result requires no conjectural downstream theorem; this is a motivated exact invariant of a canonical body, with nonzero asymptotic fluctuations and a quantified finite-size effect.

## Limitations and verification status
No results on arbitrary simplices, arbitrary orientation distributions, or full projection-volume distributions are claimed. The existing cube-width CLT is used and credited. Exact historical priority is not independently certified, particularly concerning old spherical absolute-value moment identities and the inaccessible full Affentranger–Schneider paper.

Self-review: passed. Independent audit: not yet performed.
