# Scientific review

## Correctness — PASS

The claim is supported by an exact compound-Poisson cumulant factorization through the \(\operatorname{Beta}(1,2)\) kernel. The rare component of the normalized remainder is exactly \(q_BB^2G(Bt)/V_B\); at the specified logarithmically centered argument it tends to \(2e^s/v_0\). The global optimization is not inferred from numerical searches: it is bounded uniformly on both sides of the scale \(h_B/B\), proving \(c_B\sim B/h_B\). Independent algebra checks for the Taylor coefficients and finite diagnostic calculations are reproducible with the bundled script. Integer moment convergence follows from \(e^{-h_B}B^r\to0\) for each fixed \(r\). The analytical proof, not finite testing, certifies the universal assertions.

## Originality — PASS, with residual priority risk

Chen's arXiv:2610.00032v1 (Sections 2, 3, 6 and 7) establishes the exact variational characterization and illustrates fixed bounded two-point jump laws; neither a varying rare-spike regime nor the sharp logistic profile and discontinuity under all-moment convergence is explicitly derived. This finding uses Chen's identity as an acknowledged prior input and establishes a uniform asymptotic maximizing regime. Leskelä–Välimaa study sub-Poisson variance proxies, which optimize a different inequality; Arbel–Marchal–Nguyen study optimal sub-Gaussian proxy variance, also different. Search comparisons found no matching statement, though the asymptotic may be latent in a broader earlier concentration theorem. Priority is not guaranteed by negative searches, and the result has not been independently reviewed.

## Value — PASS

For right-tail Bernstein-type bounds, using the true variance does not protect the optimal linear scale against astronomically rare, increasingly large shocks. The theorem establishes a sharp escape rate and a nontrivial logistic boundary layer even when every fixed moment converges to a benign law. This provides a concrete and quantitatively sharp instability boundary for variance-fixed concentration analysis, beyond a routine finite-parameter substitution. It does not give an optimal joint variance-scale trade-off or a second-order maximizer expansion.

Self-review: passed. Independent audit: not yet performed.
