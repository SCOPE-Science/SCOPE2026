# Scientific review

## Correctness — PASS

The exact gamma integral follows by partitioning into inverse images of the integer expanding map and applying the finite gamma product. Strict positivity follows from Chebyshev's covariance inequality for two strictly decreasing functions. Stirling's positive remainder, bounded uniformly for all shifts in the unit interval, yields the proved \(4^{-k}\) error for each time covariance. Summation with exact geometric first and second moments yields the finite-size variance law and its explicit \(8\,4^{-N}/9\) error. The verifier independently compares direct integrals with the gamma formula and reproduces small-time variances. The finite checks are not offered as proof for all times.

## Originality — PASS under examined evidence

Defaveri and Smith, arXiv:2610.21288v1, present the precise doubling-map logarithmic observable and compute its variance numerically (Table 2: \(3.705486\)); they derive an analytic variance only for the distinct logistic map (Appendix A.3). The Green–Kubo identity and numerical value do not imply the lagwise gamma representation, the \(k2^{-k}\) correlation asymptotic, the finite-time intercept, or its rigorous exponential correction. Schindler, arXiv:1810.03223, investigates a nonintegrable observable with trimming; only its abstract could be inspected in this comparison, so possible unnoticed related arguments remain a priority risk. Searches of related mathematical findings and primary literature found no covering exact statement; search absence is not proof of universal novelty.

## Mathematical value — PASS

The source explicitly reports the doubling-map variance only as a computed numerical coefficient even though it calculates the analogous logistic-map coefficient analytically. An exact natural Green–Kubo coefficient with an explicit truncation bound improves reproducibility, while the leading lag law and nonzero finite-size intercept quantify correlation and bias at all sample lengths. The \(N2^{-N}\) correction is a dynamical finite-time statement not contained in the known asymptotic variance, and its sharp coefficient is mathematically substantive. The results do not purport to settle unrelated condensation or large-deviation questions.

## Sources and residual limitations

Primary mathematical comparison: L. Defaveri and N. R. Smith, *Dynamical phase transition for a logarithm observable in chaotic systems*, arXiv:2610.21288v1, Sections II and Appendix A, https://arxiv.org/html/2610.21288v1 . Further relevant comparison: T. Schindler, *Trimmed sums for observables on the doubling map*, arXiv:1810.03223v1, https://arxiv.org/abs/1810.03223 (abstract inspected only). Semantic research-record searches also found unrelated pair-correlation and hybrid-oscillator covariance results, but no equivalent all-lag logarithmic-observable formula. Older priority under alternate special-function formulations cannot be ruled out. Numerical digits rely on high-precision quadrature in addition to the proven analytic series-tail control; no independently certified numerical integral bounds are claimed.

Self-review: passed. Independent audit: not yet performed.
