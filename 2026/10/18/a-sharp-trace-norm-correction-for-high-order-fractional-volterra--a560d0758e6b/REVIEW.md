# Self-review

## Correctness
**PASS.** Exact input/output rescaling identifies the reflected Hankel kernel. The key nonstandard lemma writes a twice-differentiable Hankel kernel as a superposition of reflected square-Volterra kernels and bounds each contribution in nuclear norm by \(t^2/2\). The weighted second-derivative Taylor remainder is \(O(\alpha^{-2})\), proving a nuclear, not merely Hilbert–Schmidt, approximation. A rank-three polynomial-exponential perturbation has one isolated positive eigenvalue and one negative first-order eigenvalue; their coefficients are checked by exact exponential moments. Ky Fan–Mirsky transfer handles the full singular sequence. The companion checker tests finite samples as independent corroboration, not as an infinite-dimensional proof.

## Originality
**PASS under examined sources, with historical priority risk.** Eveson's original full text (2003), especially its final page, explicitly asks for a sharper nuclear rank-one approximation rate than its \(\alpha^{-1/2+\delta}\) estimate and gives only the leading trace-norm constant. The present claim supplies the first correction, its coefficient, and a nuclear remainder estimate. The inspected 2010 polynomial-Volterra work treats fixed polynomial functions and does not imply the varying-order nuclear expansion. The 1998 Thorpe full text was inaccessible; its available abstract concerns leading operator and Hilbert–Schmidt behavior. An equivalent historical result cannot be ruled out by search alone.

## Value
**PASS.** The theorem quantitatively resolves the first-order scale suggested by Eveson's explicit question: the optimal rank-one *nuclear* error has coefficient \(1/8\), not just an upper bound of a weaker fractional power. The ingredient \(\|H_h\|_{\mathcal S_1}\le \tfrac12\int t^2|h''|\) prevents invisible nuclear tails that second-singular-value or Hilbert–Schmidt calculations do not control. This makes the statement an actual operator-ideal refinement rather than a restatement of the dominant spectral mode.

## Limits
No assertion about generalized Volterra kernels, an all-orders expansion, or independently established bibliographic priority. Numerical Nyström tests do not certify the limit and the actual proof is the analytic trace-class estimate.

Self-review: passed. Independent audit: not yet performed.
