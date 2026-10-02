# Independent audit — 2026-10-01

## Final claim

The claim in `RESULT.md` is accepted without changing `RESULT.md` or `SLOGAN.txt`.

## Correctness — PASS

For a simple smallest eigenvalue of the reduced block, Schur-complement elimination produces an analytic effective matrix in \(t=1/\rho\). Standard simple-eigenvalue perturbation gives the second coefficient \(v^T(J-GSG)v\) with the signs stated. Independently expanding a random symmetric example numerically converged to this coefficient. The two-level Hermite weights were re-derived symbolically: they cancel the \(t,t^2,t^3\) terms exactly and leave the fourth-order term, while the stated two-dimensional witness expands to \(1-\rho^{-1}+2\rho^{-2}-3\rho^{-3}+2\rho^{-4}+\cdots\) and its \(q=2\) estimator has leading error \(-\tfrac12\rho^{-4}\).

Sources checked: https://arxiv.org/abs/2609.18538; https://doi.org/10.1137/21M1397349.

Residual risks: The theorem is asymptotic and assumes a simple constrained target; multiple eigenvalues are not covered.

## Originality — PASS

Wang--Xia prove finite-versus-asymptotic recovery, the first-order coefficient, and the value-only two-level \(O(\rho^{-2})\) extrapolation. Their inspected full text does not give the explicit second coefficient or derivative-enhanced fourth-/higher-order Hermite formulas. Bach treats Richardson extrapolation for regularization parameters generically but not this constrained eigenvalue path or the Hellmann--Feynman derivative construction. The only exact archive duplicate located is dated 2026-09-19, after the audited record.

Sources checked: https://arxiv.org/abs/2609.18538; https://doi.org/10.1137/21M1397349; published archive record SCOPE-20260919-b0d1ece5e105.

Residual risks: Generic Hermite extrapolation is classical, so the originality is in the penalty-path expansion and its derivative-enabled specialization rather than the interpolation algebra itself.

## Scientific value — PASS

The result gives a nontrivial next asymptotic coefficient and converts derivative information already available from penalized eigenpairs into a fourth-order two-level estimator and \(2p\)-order \(p\)-level family. This directly addresses the penalty-size/accuracy tradeoff in the motivating constrained-eigenvalue method and is more than a renaming of generic Richardson extrapolation.

Sources checked: https://arxiv.org/abs/2609.18538; https://doi.org/10.1137/21M1397349.

Residual risks: No finite-precision stability theorem is supplied, so practical gains can be limited by eigenpair-solver error amplification.

## Disposition

Passed. Publication status may be updated to independently reviewed; no scientific claim text changes are required.
