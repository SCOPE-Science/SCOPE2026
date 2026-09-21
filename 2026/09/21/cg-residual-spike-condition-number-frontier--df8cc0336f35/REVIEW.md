# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The proof was checked adversarially at the coefficient, matrix-factorization, and extremal steps.

The key identity is the standard CG--Lanczos factorization \(T=LDL^T\), where the diagonal pivots are \(1/\alpha_k\) and the unit-lower-bidiagonal multipliers are \(\sqrt{\beta_k}=\|r_{k+1}\|_2/\|r_k\|_2\). After the first \(k\) pivots are eliminated, the trailing Schur complement has leading entries \(a=1/\alpha_k\) and \(c=\sqrt{\beta_k}/\alpha_k\), so \(|c|/a=\sqrt{\beta_k}\).

The spectral enclosure is preserved correctly: the Lanczos tridiagonal is an orthogonal compression of \(A\), hence its spectrum lies in \([\mu,L]\). The inverse of a trailing Schur complement is a principal block of the inverse tridiagonal; interlacing therefore keeps every trailing Schur complement in the same interval \([\mu,L]\). Its leading \(2\times2\) principal block consequently obeys \(\mu I\preceq B\preceq LI\).

For \(B=\begin{psmallmatrix}a&c\\c&d\end{psmallmatrix}\), the two PSD constraints imply
\(c^2\le(a-\mu)(d-\mu)\) and \(c^2\le(L-a)(L-d)\). Their best simultaneous value for fixed \(a\) occurs at \(d=L+\mu-a\), after which maximizing \((a-\mu)(L-a)/a^2\) gives \((L-\mu)^2/(4L\mu)\). The two-dimensional endpoint-spectrum example realizes equality, so the constant and the threshold are sharp.

A deterministic NumPy check reproduced the equality family, the threshold crossing, the inverse conditioning certificate, and tested every computed CG step in 2,400 rotated-SPD random cases. These checks support but do not replace the proof.

## Originality

**PASS, to the best of our knowledge.** The closest directly relevant prior result found is Bouyouli--Meurant--Smoch--Sadok (2009), whose Theorem 3.3 gives the all-step bound
\[
\|r_k\|_2/\|r_{k-1}\|_2\le(\kappa(A)-1)/2.
\]
The present result replaces this by the strictly sharper
\((\kappa-1)/(2\sqrt\kappa)\), and the two-dimensional equality family proves that no smaller condition-number-only constant is possible.

Meurant (2020) studies prescribed CG residual histories together with prescribed eigenvalues. Its two-dimensional discriminant implies, after translating notation, the same sharp **first-step** endpoint-spectrum feasibility frontier. Therefore neither the first-step constant nor the existence of residual oscillations is claimed as new. Searches targeted the exact formula, equivalent beta-coefficient statements, residual-increase/monotonicity wording, Lanczos/LDL formulations, condition-number-dependent Gaussian-elimination multipliers, and the threshold \(3+2\sqrt2\). No source was found that states the same sharp constant for every CG iteration in arbitrary dimension, the resulting exact universal residual-monotonicity threshold, or the fixed-SPD-preconditioner \(M^{-1}\)-residual version.

The 2024 Carson--Liesen--Strakoš survey was checked as a recent status reference; it discusses nonlinear and oscillatory CG behavior but did not surface this all-step sharp frontier. Hestenes--Stiefel establishes that unconstrained residual sequences may behave arbitrarily, which is consistent with the dependence on conditioning here.

Residual uncertainty remains. Meurant's 2006 monograph and older Gaussian-elimination/Cholesky multiplier literature are broad and were not exhaustively inspected theorem by theorem. Broyden's 1973 condition-number work on elimination factors is especially adjacent in technique, although the accessible abstract did not expose the present constant. This residual historical-equivalence risk is scientifically material and is not treated as evidence of absence.

## Value

**PASS.** The result sharpens an explicit published all-step residual-growth bound by a factor \(\sqrt\kappa\), turns it into an exact frontier, and identifies the precise condition-number threshold below which ordinary CG residual norms cannot spike. The inverse inequality converts any exact-arithmetic observed spike into a conditioning lower bound. The fixed-SPD-preconditioner extension gives the corresponding criterion in the natural preconditioned residual norm. These statements are directly relevant to interpreting residual-based diagnostics and to condition-number targets for preconditioning, while remaining clearly separated from finite-precision stopping criteria.

## Scientific limitations

- Exact arithmetic only; recursively updated and true residuals can separate in floating point.
- Real finite-dimensional SPD systems and standard CG only.
- The main constant uses the actual global spectral condition number; bounds based on spectral enclosures may be conservative.
- For PCG, the extension is for a fixed SPD preconditioner and the \(M^{-1}\)-norm of residuals, not ordinary Euclidean residuals in general.
- Global sharpness is realized at the first step; equality at arbitrary prescribed later steps is not claimed.
- The finding does not replace spectrum-distribution-dependent convergence analysis and is not an iteration-count bound.
- Older Lanczos/CG and elimination-factor literature was not exhaustively inspected theorem by theorem, leaving residual originality uncertainty.
