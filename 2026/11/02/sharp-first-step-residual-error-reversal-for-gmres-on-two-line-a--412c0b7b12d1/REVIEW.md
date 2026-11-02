# Review: Sharp first-step residual–error reversal for GMRES on two-line alternating projections

## Correctness

**PASS (self-review).** The exact projection matrices, the normal-equation minimizer \(\alpha=1/(1+z-z^2)\), and the two squared-norm ratios are calculated in `RESULT.md`. For every \(0<z<1\), the residual ratio is below one and the squared solution-error ratio exceeds one; the derivative of the latter's positive excess determines its unique sharp maximum. The rank-two Krylov determinant is \(-cs^3\neq0\), proving exact GMRES termination in two steps. The bundled `verify.py` passed 2,485 exact-rational checks and supplementary grid checks, but the continuum claim rests on the algebraic proof.

## Originality

**PASS (self-review), with bounded historical-priority uncertainty.** The full accessible text of Lerman–Zhang, *When Windowed Anderson Acceleration Converges Faster* (arXiv:2610.30073v1, first public 2026-10-21), was compared by statement and method. It studies affine Anderson convergence and links to GMRES but does not state these exact two-line residual-versus-distance reversal formulas. Bauschke et al. (2003) study a different extrapolation accelerator for alternating projections, so their convergence result is not an assertion about this first residual-minimizing GMRES step. Saad–Schultz's general residual-minimization theorem is credited, and nearby numerical acceleration findings concern other systems. Older full-text priority was not exhaustively eliminated, especially for principal-angle-specific GMRES analysis.

## Mathematical value

**PASS (self-review).** Residual norms are common algorithmic stopping or acceleration indicators; this all-angle theorem proves they can order two methods oppositely to their Euclidean solution error, quantifies the unique worst geometry exactly, and reconciles the short-horizon reversal with GMRES two-step termination. This is a structurally complete low-dimensional benchmark, rather than an arbitrary isolated arithmetic example. It makes no broad finite-precision or high-dimensional conclusion.

## Limitations and sources

The result is specific to two distinct nonorthogonal lines, the stated initial vector, the ordinary projection sweep and conventional Euclidean-residual GMRES for \(I-P_2P_1\). The relative error penalty is at most 3.74 percent; its scope is comparison and interpretation, not a claim of serious practical instability. Full source: https://arxiv.org/html/2610.30073v1 . Related abstract: https://doi.org/10.1090/S0002-9947-03-03136-2 . Classical algorithm: https://doi.org/10.1137/0907058 .

Self-review: passed. Independent audit: not yet performed.
