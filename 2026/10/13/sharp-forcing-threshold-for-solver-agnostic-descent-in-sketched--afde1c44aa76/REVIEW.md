# Self-review

## Correctness

PASS. For a fixed nonzero \(g\), the worst legal residual is parallel to \(H^{-1}g\), giving the exact worst directional derivative
\[
-g^{\mathsf T}H^{-1}g+\eta\|g\|\|H^{-1}g\|.
\]
The resulting robust-descent constant is the minimum cosine between \(g\) and \(H^{-1}g\). A direct spectral proof gives
\[
\frac{2\sqrt{ab}}{a+b},
\]
and a two-eigenvalue construction attains equality. The construction can be realized by a linear least-squares model of the same form as the source.

The LSMR comparison is separately exact: the source Krylov step satisfies \(s^{\mathsf T}\rho=0\), so multiplying the regularized normal equation by \(s^{\mathsf T}\) yields strict descent for every nonzero step.

## Originality

PASS. The primary full text and the closest same-author inexact Gauss-Newton predecessor were inspected at the residual stopping tests and descent proofs. Both use Krylov orthogonality and do not state a condition-number-dependent solver-agnostic frontier. Classical forcing-term and LSMR sources were checked for stronger coverage. Targeted published-research and public web searches did not locate an equivalent source-specific theorem.

The main residual originality risk is that the same minimum-angle constant may appear in older matrix-analysis literature under another name; the application and sharp solver-portability consequence were not located.

## Value

PASS. The theorem is a practical structural boundary: it identifies exactly when the primary paper's residual tolerance can be transferred from LSMR to an arbitrary inner solver. The condition-number dependence can be severe, so the result is not a cosmetic sharpening. It explains the hidden value of Krylov orthogonality and supplies an exact replacement stopping rule when that structure is absent.

Self-review: passed. Independent audit: not yet performed.
