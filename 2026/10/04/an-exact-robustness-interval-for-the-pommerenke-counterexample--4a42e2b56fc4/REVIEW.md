# Review of An exact robustness interval for the Pommerenke counterexample

## Correctness

PASS. The source gives exact values of \(F'(z_0)\), \(G'(z_0)\), \(z_0F''(z_0)\), and \(z_0G''(z_0)\). Keeping the mixture parameter \(\lambda\) symbolic makes both
\[
D_\lambda=H_\lambda'(z_0)
\]
and
\[
N_\lambda=H_\lambda'(z_0)+z_0H_\lambda''(z_0)
\]
affine in \(\lambda\). Exact expansion of
\[
\operatorname{Re}(N_\lambda\overline{D_\lambda})
\]
and
\[
|D_\lambda|^2
\]
gives the stated two quadratics. The denominator is positive, and the numerator has exactly the two displayed roots, so the sign interval is rigorous.

The source's weighted Laurent-tail proof also extends directly from \(\lambda=3/5\) to every \(0<\lambda<1\), proving that all mixtures remain in \(\Sigma\). At the interval endpoints the curvature real part is zero, which still violates the strict exterior-convexity criterion.

## Originality

PASS. The full primary paper fixes \(\lambda=3/5\) throughout its concrete counterexample calculation and reports only the single curvature value there. Its conclusion explains the complex phase mechanism but does not state a parameter interval or solve for curvature crossings.

Published-finding searches used the exact source identifier together with robustness, mixture-weight interval, same-point obstruction, and the numerical endpoint values. No implication-equivalent result was located. General web searches likewise returned the original preprint and its summaries rather than a quantitative follow-up.

The residual risk is mainly temporal: because the source is very recent and its formulas are explicit, an unindexed note could independently observe the same parameter sweep.

## Value

PASS. The source resolves a decades-old problem by one explicit mixture. The new calculation shows that the phenomenon is not isolated or fragile: more than three quarters of the entire convex-combination parameter segment is certified nonconvex by one fixed point.

This exact robustness window is a natural quantitative invariant of the published pair. It separates the underlying phase mechanism from the arbitrary-looking choice \(\lambda=3/5\) and provides a concrete target for any future attempt to classify which mixtures of that pair are actually convex.

Same-model review: passed. Independent audit: not yet performed.
