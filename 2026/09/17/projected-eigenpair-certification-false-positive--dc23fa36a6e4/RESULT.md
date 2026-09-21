# Zero-residual false positives in projected certification of constrained extremal eigenpairs

## Statement

Consider the maximum-eigenvalue side of the Penalty–Split–Merge (PSM) framework of Wang and Xia (2026). For a feasible subspace
\[
\mathcal S_X=\mathcal N(A)\cap\operatorname{span}(X)^\perp,
\]
the target is
\[
\lambda_X^c=\max_{u\in\mathcal S_X,\ \|u\|=1}u^THu
          =\inf_{\rho\ge0}\lambda_{\max}(M_\rho^{(X)}),
\]
where
\[
M_\rho^{(X)}=H-\rho(A^TA+XX^T).
\]
The published stopping rule accepts after the penalized eigen-residual, projected feasibility residual, projected KKT residual, and projected outer-change residual all fall below their tolerances.

Those four quantities do **not** certify that the returned stationary eigenpair has the requested extremal index. In fact, they can all vanish while the returned eigenvalue has arbitrarily large error.

### Theorem 1 — exact zero-residual false certificate

For every \(M\ge1\), set
\[
H_M=\operatorname{diag}(0,0,M),\qquad A=\begin{bmatrix}1&0&0\end{bmatrix},\qquad X=\varnothing.
\]
Then
\[
\mathcal N(A)=\operatorname{span}\{e_2,e_3\},\qquad \lambda^c=M,
\]
with target eigenvector \(e_3\). For every \(\rho>0\),
\[
M_\rho=\operatorname{diag}(-\rho,0,M),
\qquad \lambda_{\max}(M_\rho)=M,
\]
so the penalty representation is already exact at every positive penalty.

Take instead the feasible non-dominant eigenvector \(u=e_2\). Its penalized Rayleigh quotient is \(\theta^{\rm pen}=0\), and
\[
M_\rho u-\theta^{\rm pen}u=0.
\]
The projector is
\[
P=I-A^T(AA^T)^{-1}A=\operatorname{diag}(0,1,1),
\]
so \(\widehat u=e_2\), \(\widehat\theta=0\), and therefore
\[
r_M=r_{\rm feas}=r_{\rm KKT}=0.
\]
At any subsequent penalty level the same projected value is obtained, hence
\[
r_{\rm out}=0.
\]
Thus the complete PSM acceptance test is satisfied for every positive choice of tolerances, although
\[
\boxed{\lambda^c-\widehat\theta=M.}
\]
The absolute error is unbounded under scaling, and with \(M=1\) the example already has unit spectral error despite all four residuals being exactly zero.

This is an eigenvalue-index failure, not a penalty-tail failure: the desired dominant penalized eigenpair is \((M,e_3)\) for every \(\rho>0\).

## Compatibility with the stated inner iteration

Using the conservative bounds \(\underline\lambda_H=0\), \(\overline\lambda_H=M\), and \(\overline\nu_A=1\), the shifted/scaled PSM inner operator is
\[
\mathcal K_\rho
=\frac{M_\rho+\rho I}{M+\rho}
=\operatorname{diag}\!\left(0,\frac{\rho}{M+\rho},1\right).
\]
Hence \(e_2\) is a non-dominant eigenvector of \(\mathcal K_\rho\) with a strictly positive eigenvalue. The public Split–Merge implementation stops when its eigenvector residual vanishes; at any exact eigenvector this residual is zero. Its documentation also states that the starting vector should not be orthogonal to the dominant eigenvector. The Split–Merge convergence theorem likewise assumes nonzero dominant overlap, whereas PSM Algorithm 1 states only that the initial vector has unit norm.

Consequently, the initialization \(u^{(0)}=e_2\) is allowed by the displayed PSM algorithm but lies outside the inner convergence theorem's overlap hypothesis. With residual-based inner stopping, it is returned immediately as a converged inner eigenvector. Warm starting preserves the same vector at the next penalty level, after which the projected rule accepts the wrong constrained eigenpair.

The counterexample therefore identifies a hypothesis/interface gap: a local eigenpair residual is being used as if it also certified the requested spectral index.

## The obstruction is not only an exact-eigenvector phenomenon

Let
\[
u_\delta=\sqrt{1-\delta^2}\,e_2+\delta e_3,
\qquad 0<\delta<1.
\]
This vector is exactly feasible for every \(\rho\), and its Rayleigh quotient is
\[
\theta_\delta=M\delta^2.
\]
Since the penalty term vanishes on the feasible plane,
\[
\|M_\rho u_\delta-\theta_\delta u_\delta\|
=\|Hu_\delta-\theta_\delta u_\delta\|
=M\delta\sqrt{1-\delta^2}.
\]
Thus, for fixed \(M\), the penalized and projected KKT residuals tend to zero linearly with \(\delta\), whereas
\[
\lambda^c-\theta_\delta=M(1-\delta^2)\longrightarrow M.
\]
If the same feasible approximation is presented at two consecutive penalty levels, its projected Rayleigh quotient does not depend on \(\rho\), so \(r_{\rm out}=0\) as well.

Therefore there is no deterministic error bound of the form
\[
\lambda_X^c-\widehat\theta\le \Psi(r_M,r_{\rm feas},r_{\rm KKT},r_{\rm out})
\]
with \(\Psi\to0\) as its arguments tend to zero, unless additional information certifying the spectral index is supplied.

## A direct repair: an extremality bracket

The penalty duality itself gives a simple way to state a valid global certificate. For any normalized feasible \(\widehat u\in\mathcal S_X\), let
\[
\widehat\theta=\widehat u^TH\widehat u.
\]
For every \(\rho\ge0\),
\[
\widehat\theta\le\lambda_X^c\le\lambda_{\max}(M_\rho^{(X)}).
\]
Hence, if an independent validated computation supplies any upper bound
\[
U_\rho\ge\lambda_{\max}(M_\rho^{(X)}),
\]
then
\[
\boxed{0\le\lambda_X^c-\widehat\theta\le U_\rho-\widehat\theta.}
\]
An acceptance rule requiring
\[
\frac{U_\rho-\widehat\theta}
{\max\{1,|U_\rho|,|\widehat\theta|\}}
\le\varepsilon_{\rm ext}
\]
therefore certifies the desired **global extremal value**, rather than merely stationarity of some eigenpair. The existing feasibility and KKT tests remain useful diagnostics, but they cannot replace this index-sensitive bound.

A crude always-valid choice is the supplied bound \(U_\rho=\overline\lambda_H\), because \(M_\rho^{(X)}\preceq H\). In practice this may be too loose; a tighter matrix-free upper enclosure for the dominant penalized eigenvalue is preferable. Classical work on Lanczos misconvergence explicitly distinguishes small Ritz residuals from certification of extreme eigenvalues and develops probabilistic extreme-eigenvalue bounds under random starts. Such a probabilistic bound could be used here if its probabilistic status is reported explicitly; a deterministic certificate requires a deterministic enclosure.

## Correctness checks

For the diagonal family, every displayed identity follows by direct multiplication. The included verification script checks the shifted/scaled penalized spectrum, the exact zero residuals, and the robust \(u_\delta\) residual formula numerically.

The logical separation is important:

- an eigenpair residual certifies backward accuracy for **some** eigenpair;
- projected feasibility certifies membership in the constrained subspace;
- the projected KKT residual certifies first-order stationarity on that subspace;
- outer stability certifies that the reported stationary value is not changing across penalty levels;
- none of these identifies the stationary point as the maximum eigenpair.

## Scope and limitations

- The result does not dispute the projected-Hessian penalty duality, finite-attainment theorem, or asymptotic penalty expansion in Wang and Xia (2026).
- The exact PSM trajectory uses an initialization orthogonal to the desired dominant eigenvector. Such an initialization has probability zero under an absolutely continuous random start, but PSM Algorithm 1 does not state a random-start or nonzero-overlap requirement.
- The nearby-vector calculation shows that the residual tests themselves remain non-index-certifying at arbitrarily small positive residuals. It does not assert that the safeguarded inner iteration reaches those nearby vectors with appreciable probability from a random initialization.
- A random-start convergence statement is not the same as an a posteriori extremality certificate. If certification rather than high-probability convergence is desired, an extremal eigenvalue enclosure or equivalent index-sensitive condition is necessary.
- The finding concerns the maximum-eigenvalue PSM path; the minimum-eigenvalue version has the analogous issue after sign reversal.

## Literature context and originality boundary

Wang and Xia (2026) introduce PSM and define inner convergence through a penalized eigen-residual, followed by projected feasibility, KKT, and outer-change tests. Their Algorithm 1 permits an arbitrary unit initial vector. The cited Split–Merge theory assumes nonzero overlap with the dominant eigenvector, and the public Split–Merge implementation documents the same requirement.

The general numerical-linear-algebra principle is not new. Parlett studied Lanczos “misconvergence,” and van Dorsselaer, Hochstenbach, and van der Vorst explicitly note that an extreme Ritz value need not approximate the corresponding extreme eigenvalue even when its residual is small. The contribution here is narrower: the exact zero-residual PSM counterexample, the identification of the missing spectral-index condition in its projected acceptance rule, the robust small-residual family, and the penalty-duality bracket that repairs the certification semantics.

No public erratum, comment, or source was located that states this PSM-specific counterexample or repair. Originality is therefore claimed only to the best of our knowledge.

## Reproducibility

`artifacts/verify_false_certificate.py` verifies the explicit family and the robust residual formula. It was executed with Python 3.13.5 and NumPy 2.3.5. `artifacts/verified_output.txt` records the verified numerical output for \(M=7\), \(\rho=0.3\), and \(\delta=10^{-8}\).

## References

1. M. Wang and Y. Xia, *The Projected Hessian Quantification Theorem: An Exact Duality for Constrained Eigenvalues*, arXiv:2609.18538, 2026. https://arxiv.org/abs/2609.18538
2. X. Liu and Y. Xia, *Split-Merge: A Difference-based Approach for Dominant Eigenvalue Problem*, arXiv:2501.15131v2, 2025. https://arxiv.org/abs/2501.15131
3. X. Liu and Y. Xia, public MATLAB implementation of Split–Merge. https://github.com/xzliu-opt/SplitMerge
4. J. L. M. van Dorsselaer, M. E. Hochstenbach, and H. A. van der Vorst, *Computing Probabilistic Bounds for Extreme Eigenvalues of Symmetric Matrices with the Lanczos Method*, SIAM J. Matrix Anal. Appl. 22 (2001), 837–852. https://doi.org/10.1137/S0895479800366859
5. B. N. Parlett, *Misconvergence in the Lanczos Algorithm*, in *Reliable Numerical Computation*, Oxford University Press, 1990, pp. 7–24. https://doi.org/10.1093/oso/9780198535645.003.0002
