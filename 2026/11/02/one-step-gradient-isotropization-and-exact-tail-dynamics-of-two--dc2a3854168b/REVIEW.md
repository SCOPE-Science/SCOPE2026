# Scientific review: two-row polar-gradient collapse

## Correctness — PASS

The theorem covers arbitrary real two-row gradients of full row rank, any number of columns at least two, and arbitrary non-scalar symmetric positive-definite left curvature at the inverse-trace fixed step. The proof identifies the trace-free symmetric first-step left factor, uses its exact two-by-two square-scalar identity, and shows that every subsequent nuclear-polar update equals twice the gradient; a second trace-free identity supplies the sharp exact factor. The rank-one and one-step-termination boundaries are proved separately. The bundled exact-rational verifier passed 648 full-row-rank configurations, including dense noncommuting factors, and 48 rank-one cases. Direct SVD simulations were supplementary; the universal proof does not rely on finite tests.

## Originality — PASS, with priority risk

Jawanpuria, Garai and Mishra (2026) establish the update, rank-aware stable fixed-step range, exact one-step objective identity, and some invariant directions. Those are prior results, not claimed as new. Their general-directional rate is left unspecified. Lau, Long and Su (2025) introduce the family and prove broader qualitative convergence estimates. The additional two-row, full-rank **finite gradient singular-value equalization plus complete linear-tail law** is not contained in the inspected statements or supplied as a simple quoted invariant-direction case. Available mathematical record comparisons returned no equivalent result. Unindexed older spectral-norm steepest-descent or matrix-polar literature may nonetheless cover equivalent formulations; no independent priority certification is claimed.

## Value — PASS

The result completely characterizes a natural low-row-dimension optimization model, including all dense noncommuting full-rank initializations, one-step termination, a sharp optimal-GD tail rate, and a discontinuous rank-one boundary. It answers a concrete structural question about why a nonlinear spectral optimizer can suddenly become ordinary optimally tuned gradient descent, and it identifies the precise role of gradient rank. The statement is limited to exact polar factors, two rows, fixed SPD quadratic curvature, and the inverse-trace step; no general dimensional, stochastic, or finite-precision conclusion follows.

Self-review: passed. Independent audit: not yet performed.
