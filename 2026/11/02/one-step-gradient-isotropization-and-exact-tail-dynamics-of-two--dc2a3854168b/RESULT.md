# One-step gradient isotropization and exact tail dynamics of two-row polar descent

## Finding

Let \(n\ge 2\), and let \(H\in\mathbb R^{2\times2}\) be symmetric positive definite with distinct eigenvalues \(0<a<b\). On the quadratic
\[
f(X)=\tfrac12\operatorname{tr}((X-X_\star)^\mathsf TH(X-X_\star)),\qquad X\in\mathbb R^{2\times n},
\]
consider the exact nuclear-scaled polar-gradient update
\[
X_{k+1}=X_k-\frac{\|G_k\|_*}{\operatorname{tr}H}\operatorname{polar}(G_k),\qquad G_k=H(X_k-X_\star),
\]
where \(\operatorname{polar}(G)=UV^\mathsf T\) for a thin singular-value decomposition \(G=U\Sigma V^\mathsf T\), and the update vanishes at \(G=0\).

**Theorem (full-row-rank stratum).** For every initial gradient \(G_0\) of row rank two, the *first* updated gradient either vanishes or has two exactly equal positive singular values. In either case, from iteration one onward, the nonlinear polar iteration is *exactly* the optimally tuned ordinary gradient descent iteration:
\[
G_{k+1}=CG_k,\quad C=I_2-\frac{2H}{\operatorname{tr}H},\qquad k\ge1.
\]
Define \(\rho=(b-a)/(a+b)\in(0,1)\). Since \(C^2=\rho^2 I_2\), the gradient and error satisfy \(G_{k+2}=\rho^2G_k\) and \(X_{k+2}-X_\star=\rho^2(X_k-X_\star)\) for every \(k\ge1\). If \(G_1\ne0\), then for all \(k\ge1\),
\[
\sigma_1(G_k)=\sigma_2(G_k)>0,\quad
f(X_k)=\rho^{2(k-1)}f(X_1),\quad
\lim_{k\to\infty}\|X_k-X_\star\|_{\mathrm F}^{1/k}=\rho.
\]
Exact one-step termination occurs if and only if \(X_0-X_\star=cQ\) for some \(c>0\) and a row-isometry \(Q\in\mathbb R^{2\times n}\) with \(QQ^\mathsf T=I_2\). In that case, \(G_1=0\).

**Rank-one boundary.** If \(G_0\) has rank one, every \(G_k\) retains rank one and the iteration instead obeys
\[
X_k-X_\star=\left(I_2-\frac{H}{\operatorname{tr}H}\right)^k(X_0-X_\star).
\]
Thus rank-one starts do not undergo gradient isotropization. For a start supported along the eigenspace of \(a\), the root factor is \(b/(a+b)\), strictly larger than the full-rank factor \(\rho\). Hence the exact asymptotic convergence factor is discontinuous at that rank-one start, although every trajectory converges.

## Assumptions and scope

All matrices and iterates are real; arithmetic and the polar factor are exact. The row dimension is two, the column dimension is any integer \(n\ge2\), and \(H\) is fixed symmetric positive definite with *distinct* positive eigenvalues. The nuclear norm \(\|G\|_*\) is the sum of positive singular values, and \(\operatorname{polar}(G)=UV^\mathsf T\) is the canonical partial-isometry polar factor, independent of the choice of singular-vector basis. The step length is fixed at \(1/\operatorname{tr}H\). Neither the matrix \(X_\star\) nor the initial point is assumed diagonal, commutative with \(H\), or aligned with its eigenspaces. The zero gradient remains zero.

## Proof

**Full-rank first step.** Put \(T=\operatorname{tr}H=a+b\), and let \(G_0=AO\) be the left polar decomposition, with \(A=(G_0G_0^\mathsf T)^{1/2}\succ0\) and \(O O^\mathsf T=I_2\). Since \(\|G_0\|_*=\operatorname{tr}A=:S\), the new gradient is
\[
G_1=H(X_1-X_\star)=G_0-\frac ST HO=BO,\qquad B=A-\frac ST H.
\]
The matrix \(B\) is symmetric and has trace zero. Every real symmetric two-by-two trace-zero matrix has the form \(\bigl(\begin{smallmatrix}u&v\\v&-u\end{smallmatrix}\bigr)\), so
\[
B^2=(u^2+v^2)I_2=:\beta^2 I_2,
\qquad G_1G_1^\mathsf T=BOO^\mathsf T B=\beta^2I_2.
\]
Thus \(G_1=0\) if \(\beta=0\), and otherwise both singular values of \(G_1\) equal \(\beta>0\). The first-step collapse holds for arbitrary \(n\), arbitrary noncommuting \(A,H\), and arbitrary row-isometry \(O\).

**Linear tail.** Whenever a nonzero two-row gradient \(G\) satisfies \(GG^\mathsf T=\beta^2 I_2\), its polar factor is exactly \(G/\beta\) and its nuclear norm is exactly \(2\beta\). Consequently \(\|G\|_*\operatorname{polar}(G)=2G\), and the next gradient is \((I_2-2H/T)G=CG\). Now \(C\) is real symmetric with trace zero, eigenvalues \(\rho\) and \(-\rho\), and \(C^2=\rho^2I_2\). Hence \((CG)(CG)^\mathsf T=\rho^2 GG^\mathsf T\). Because \(\rho>0\), rank two and equal singular values persist unless \(G_1=0\). Induction yields \(G_{k+1}=CG_k\) for all \(k\ge1\), and \(G_{k+2}=\rho^2G_k\). Since \(H\) is invertible, the same two-step identity holds for the errors. For \(k\ge1\), \(G_kG_k^\mathsf T=\beta^2\rho^{2(k-1)}I_2\), giving
\[
f(X_k)=\frac12\operatorname{tr}(G_k^\mathsf TH^{-1}G_k)
=\frac{\beta^2}{2}\operatorname{tr}(H^{-1})\rho^{2(k-1)}.
\]
For \(G_1\ne0\), this proves the exact nonzero root factor \(\rho\) and the claimed objective identity.

**Termination set.** \(G_1=0\) is equivalent to \(B=0\), or \(A=(S/T)H\). Then \(X_0-X_\star=H^{-1}G_0=(S/T)O\), a positive multiple of a row-isometry. Conversely, for \(X_0-X_\star=cO\) with \(OO^\mathsf T=I_2\), we have \(G_0=cHO\), so its left polar factor is \(O\), and its nuclear norm is \(cT\); the prescribed step reaches \(X_\star\) exactly.

**Rank-one boundary.** A rank-one gradient has one nonzero singular value \(s\), hence \(\|G\|_*\operatorname{polar}(G)=s\operatorname{polar}(G)=G\). The update is ordinary gradient descent with step \(1/T\). Its error multiplier \(I_2-H/T\) has the strictly positive eigenvalues \(b/T\) and \(a/T\), so is invertible: the rank remains one for every nonzero rank-one start. Along an eigenvector of \(a\), the factor is exactly \(b/T\), whereas \(b/T-\rho=a/T>0\). Full-rank initial matrices can approach that rank-one matrix arbitrarily closely, proving the rate discontinuity.

## Verification

The standalone `VERIFY.py` contains only Python standard-library exact rational arithmetic. It tests 648 positive-definite curvature/polar-factor combinations with arbitrary rational rotations, including dense noncommuting positive-definite matrices and two- or three-column row-isometries; it checks the trace-zero identity, square-scalar identity, first-step singular-value identity, and six exact tail steps. It also checks 48 rank-one boundary examples. It is run as `python3 VERIFY.py` from the directory containing this file. Separate direct floating-point SVD checks of 300 random dense full-rank examples confirmed first-step equal singular values and the second-step linearization. The infinite-dimensional quantifier over \(n\) and the all-iterate statements follow from the proof, not from sampling.

## Relationship to prior work

Jawanpuria, Garai and Mishra (2026) define this nuclear-scaled polar update and establish global linear convergence on positive-definite matrix quadratics for steps below a trace-curvature threshold. Their Appendix C gives the exact one-step energy identity, its stronger rank-aware threshold, sharpness examples on invariant directions, and explicitly leaves general directional rates in closed form unresolved. The present assertion is different: a finite *one-step* collapse of every full-row-rank two-row gradient onto the equal-singular-value manifold, followed by an exact reduction of the **entire nonlinear tail** to optimally tuned ordinary gradient descent, without any diagonal or invariant-direction assumption. This yields the full-rank/one-rank rate split. Lau, Long and Su (2025) introduce the nuclear-scaled polar family and general condition-number convergence estimates, without this two-row finite identification law. The elementary trace-zero square identity is used as a proof ingredient, not claimed as a new matrix inequality.

## Limitations

The exact collapse uses a two-dimensional real row space and the distinguished step \(1/\operatorname{tr}H\). It need not hold for three or more rows, for a different stepsize, or for approximate polar factors. The objective is a fixed symmetric-positive-definite quadratic with one-sided left curvature; no stochastic, momentum, weight-decay, nonlinear-objective, or finite-precision guarantee is implied. No claim of historical priority is made beyond the accessible comparisons; an older formulation in steepest-descent spectral-norm geometry might exist. The initial full-row-rank assumption is essential and the rank-one behavior is explicitly different.

## References

- P. Jawanpuria, B. Garai and B. Mishra, *Constant Step Sizes for Muon-Type Spectral Optimizers on Strongly Convex Quadratics*, arXiv:2610.27747v1 (first public 2026-10-20), https://arxiv.org/html/2610.27747v1, especially Section 4 and Appendix C.
- T. T.-K. Lau, Q. Long and W. Su, *PolarGrad: A Class of Matrix-Gradient Optimizers from a Unifying Preconditioning Perspective*, arXiv:2505.21799 (first public 2025-05-27), https://arxiv.org/html/2505.21799v2, especially Section 4 and the accompanying proofs.
