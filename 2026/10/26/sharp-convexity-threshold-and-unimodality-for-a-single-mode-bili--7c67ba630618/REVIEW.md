# Review

## Correctness

**PASS.** The reduced state follows directly from the eigenfunction equation. Differentiation gives \(j''(c)=\lambda-q(\kappa+c)\); the derivative of \(q\) locates its unique maximum, yielding the exact convexity threshold. The logarithmic derivative of \(R(c)\) is strictly negative on the only interval where it is positive, proving that \(j'\) changes sign at most once and only from negative to positive. Endpoint cases are covered by monotonicity.

## Originality

**PASS, with residual risk.** published-finding corpus searches for equivalent formulations and for the exact scalar threshold returned nearby but mathematically different optimization/control findings. The inspected primary papers provide the general bilinear fractional-control model and local second-order conditions, but not this exact global threshold plus all-regularization unimodality classification. Search absence is not treated as proof of novelty.

## Value

**PASS.** Bilinear-control reduced objectives are generally nonconvex, and second-order sufficient conditions are local. This exact eigenmode benchmark separates loss of convexity from multiplicity of minima and supplies a sharp regularization threshold for solver tests and parameter calibration. Its scope is deliberately limited to a natural single-mode reduction.

## Closest literature and limitations

The closest sources are Wang–Wang–Zhou (arXiv:2310.05059v1) on adaptive finite-element approximation and Bersetche–Fuica–Otárola–Quero (arXiv:2301.13058) on analysis and discretization of bilinear fractional control. Both treat general first- and second-order conditions; neither inspected statement provides the exact scalar threshold claimed here. The full spatially varying problem remains outside scope.

Self-review: passed. Independent audit: not yet performed.
