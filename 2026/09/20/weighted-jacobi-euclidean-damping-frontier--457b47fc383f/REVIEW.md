# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The central equivalence follows from an exact matrix inequality:
\((I-\omega B)^T(I-\omega B)\preceq I\) is equivalent, for \(\omega>0\), to
\(B+B^T-\omega B^TB\succeq0\), and congruence by \(B^{-T}\) and \(B^{-1}\) yields
\(B^{-T}+B^{-1}-\omega I\succeq0\). With \(B=D^{-1}A\), this gives the exact fixed-matrix ceiling \(\lambda_{\min}(A^{-1}D+DA^{-1})\).

For 2×2 SPD matrices, direct inversion gives
\((2ad-|c|(a+d))/(ad-c^2)\). Fixing eigenvalues to \(1,\kappa\) reduces the robust problem to minimizing the convex quadratic
\(2+[2z^2-(\kappa+1)z]/\kappa\) over
\(0\le z\le(\kappa-1)/2\). The constrained vertex changes location at \(\kappa=3\), producing the stated piecewise envelope. Its zero and unit crossings are respectively \(7+4\sqrt3\) and \(3+2\sqrt2\). Deterministic numerical checks reproduce the identities and threshold cases and verify that, above the no-damping threshold, spectral convergence can coexist with Euclidean one-step amplification for every positive damping.

Potential failure modes were checked: the inequalities are non-strict at the standard-Jacobi boundary; the no-positive-damping boundary is strict in \(\kappa\) for the universal existence statement because the worst matrix already has zero safety ceiling at \(7+4\sqrt3\); scaling \(A\) does not change \(D^{-1}A\); and every admissible off-diagonal magnitude used in the minimization is realized by a rotation of \(\operatorname{diag}(1,\kappa)\).

## Originality

**PASS, to the best of our knowledge.** Classical sources on Jacobi and weighted Jacobi were checked for the standard iteration and spectral convergence framework. Saad's Chapter 4 provides the basic iterative-method context. Varga and Young are broad historical references. Arioli–Romani (1985) gives condition-number bounds for the **spectral radius** of Jacobi under diagonal-dominance assumptions; its accessible theorem summary does not state a Euclidean one-step norm frontier. Hadjidimos–Neumann (1998) treats Euclidean-norm minimization for SOR/MSOR, not the weighted-Jacobi condition-number envelope proved here.

Searches using “weighted Jacobi”, “damped Jacobi”, “Euclidean norm”, “2-norm”, “nonexpansive”, the exact radical constants, and the matrix expressions \(A^{-1}D+DA^{-1}\) and \(B^{-1}+B^{-T}\) did not locate the fixed-matrix criterion or the two-dimensional robust formulas claimed here. The SCOPE archive was also searched for weighted-Jacobi/Euclidean-contractivity overlap and no matching result was found.

### Residual prior-coverage risk

The complete theorem-level text of Young's 1971 monograph and all relevant chapters of Varga's *Matrix Iterative Analysis* were not inspected end to end. Arioli–Romani's publisher page exposes the theorem summary and references but not the complete article text in the material inspected. These broad classical sources are the most plausible locations for an equivalent elementary 2×2 calculation, so historical prior coverage cannot be excluded completely. Hadjidimos–Neumann was inspected at abstract/reference level; it is related by its focus on Euclidean norms of relaxation operators, but the accessible statement concerns SOR/MSOR rather than weighted Jacobi.

## Value

**PASS.** The result separates two notions often conflated for diagonally preconditioned stationary iterations: spectral convergence and Euclidean stepwise safety. It gives an exact, directly computable matrix certificate in arbitrary dimension, then resolves the robust condition-number question completely in dimension two. The two thresholds quantify how much damping can repair Euclidean transient amplification and identify a sharp regime where damping cannot repair it at all. This is useful both as a diagnostic for nonnormal stationary iterations and as a small-dimensional benchmark for stronger norm or preconditioner analyses.

## Limitations

- Exact arithmetic, real SPD matrices, and simultaneous weighted Jacobi only.
- The sharp condition-number envelope is two-dimensional; no higher-dimensional condition-number-only frontier is claimed.
- Euclidean one-step error norm is the metric; energy norms, residual norms, componentwise monotonicity, and floating-point behavior are different questions.
- No claim is made about optimal asymptotic damping, smoothing factors, multigrid performance, or wall-clock performance.
- Historical prior-coverage risk remains because several broad monographs were not inspected in full theorem-level detail.
