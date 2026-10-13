# Sharp convex-order envelope for one-pivot randomized Cholesky trace error

## Finding
Fix any integer \(n\ge2\) and any strictly positive spectrum \(\lambda_1,\ldots,\lambda_n\). Among all real symmetric positive-definite matrices with this spectrum, the distribution of the trace error after one diagonal-proportionally sampled Cholesky pivot is squeezed in **convex order** between a constant and a size-biased spectral variable. Both extreme distributions are attained, for every prescribed spectrum, by suitable real orthogonal changes of basis.

Write \(S=\sum_i\lambda_i\), \(M_q=\sum_i\lambda_i^q\), and \(m=S-M_2/S\). For **every** finite real convex function \(\varphi:[0,S]\to\mathbb R\),
\[
\varphi(m)\ \le\ \mathbb E\,\varphi(T_K)\ \le\ \frac1S\sum_{i=1}^n\lambda_i\varphi(S-\lambda_i).
\]
The expectation is only over the single random pivot. The upper bound is attained by the diagonal eigenvalue matrix. The lower bound is attained by a real orthogonal conjugate making \(T_K=m\) deterministically. In particular, the sharp range of the trace-error variance on the orthogonal orbit is
\[
0\le\operatorname{Var}(T_K)\le\frac{M_3}{S}-\left(\frac{M_2}{S}\right)^2.
\]
For strictly convex \(\varphi\), upper equality occurs precisely for a matrix diagonal in the pivot coordinates; lower equality occurs precisely when all possible pivot outcomes have the same trace error.

## Assumptions and scope
Let \(K\in\mathbb R^{n\times n}\) be positive definite and symmetric. The first randomly pivoted Cholesky update draws \(J\in\{1,\ldots,n\}\) with \(\Pr(J=j)=K_{jj}/S\) and gives the residual
\[
R_K=K-\frac{Ke_Je_J^{\mathsf T}K}{K_{JJ}},\qquad T_K=\operatorname{tr}(R_K)=S-\frac{(K^2)_{JJ}}{K_{JJ}}.
\]
All \(K_{jj}>0\), so no division by zero occurs. The residual is positive semidefinite, hence \(0\le T_K\le S\). Spectral comparison means holding the complete multiset of strictly positive eigenvalues fixed while varying \(K\) by **real orthogonal conjugation**. All assertions are exact-arithmetic, single-step statements.

## Proof
**Conditional-expectation representation.** Write \(K=U\operatorname{diag}(\lambda_1,\ldots,\lambda_n)U^{\mathsf T}\) with orthogonal \(U\). On a joint probability space define
\[
\Pr(J=j,I=i)=\frac{\lambda_iU_{ji}^2}{S}.
\]
This is nonnegative and sums to one. The \(J\)-marginal is \(K_{jj}/S\), and the \(I\)-marginal is \(\lambda_i/S\). Set \(X=S-\lambda_I\). Conditional on \(J=j\),
\[
\mathbb E[X\mid J=j]
=S-\frac{\sum_i\lambda_i^2U_{ji}^2}{\sum_i\lambda_iU_{ji}^2}
=S-\frac{(K^2)_{jj}}{K_{jj}}=T_K\bigm|_{J=j}.
\]
Thus \(T_K\) and \(\mathbb E[X\mid J]\) have the same law and \(\mathbb E T_K=\mathbb E X=m\). Conditional Jensen gives \(\mathbb E\varphi(T_K)\le\mathbb E\varphi(X)\), while ordinary Jensen gives \(\varphi(m)\le\mathbb E\varphi(T_K)\). These arguments apply to every finite convex \(\varphi\) on \([0,S]\).

**Simultaneous attainability of both bounds.** With \(K=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)\), pivot \(i\) occurs with probability \(\lambda_i/S\) and its trace error equals \(S-\lambda_i\), proving upper sharpness. To prove lower sharpness for any fixed spectrum, let
\[
H=\operatorname{diag}\left(\lambda_i^2-\frac{M_2}{S}\lambda_i\right)_{i=1}^n.
\]
This real symmetric matrix has zero trace. We prove by induction that every real symmetric traceless matrix \(H\) admits an orthonormal basis \(w_1,\ldots,w_n\) with \(w_j^{\mathsf T}Hw_j=0\) for each \(j\). This is immediate in dimension one. If \(H\ne0\), tracelessness provides a strictly positive and a strictly negative eigenvalue; a unit vector in the plane of their eigenvectors has zero quadratic form, by continuous interpolation. Its compression to the orthogonal complement remains symmetric and traceless, because both the total trace and this first quadratic form vanish. Apply induction to the compressed matrix. If \(H=0\), any orthonormal basis works. Let \(W\) contain this basis as columns and put \(K_0=W^{\mathsf T}\operatorname{diag}(\lambda_i)W\). Then
\[
(K_0^2)_{jj}-\frac{M_2}{S}(K_0)_{jj}=(W^{\mathsf T}HW)_{jj}=0
\]
for every \(j\). Since \((K_0)_{jj}>0\), each outcome has trace error \(T_{K_0}=m\). This proves lower sharpness simultaneously for all convex tests.

**Equality criteria.** For a strictly convex test, equality in the lower Jensen bound holds exactly when \(T_K\) is constant, which is equivalent to \(\operatorname{diag}(K^2-(M_2/S)K)=0\). For equality in conditional Jensen, every row's positive conditional weights must be supported entirely on eigenvalues that agree. The distinct-eigenvalue spectral projectors then have diagonal entries in \(\{0,1\}\); a symmetric orthogonal projector with zero off-diagonal Frobenius mass when its diagonal is zero or one must be a diagonal coordinate projector. Therefore \(K\) is diagonal. Conversely diagonal \(K\) attains equality. This includes repeated-eigenvalue and scalar-matrix cases.

**Sharp variance and intermediate values.** Taking \(\varphi(z)=(z-m)^2\), the lower distribution has variance zero and the upper distribution has variance
\[
\frac1S\sum_i\lambda_i(S-\lambda_i-m)^2
=\frac{M_3}{S}-\left(\frac{M_2}{S}\right)^2.
\]
For any specific input matrix the exact variance is
\[
\operatorname{Var}(T_K)=\frac1S\sum_{j=1}^n\frac{((K^2)_{jj})^2}{K_{jj}}-\left(\frac{M_2}{S}\right)^2.
\]
The bounds are attained as shown. Every intermediate value is also attained by a continuous path of real orthogonal conjugates: a column sign flip commutes with the eigenvalue diagonal, so the two extremizing orthogonal conjugations can be represented with determinants of the same sign; they are joined by a path in an appropriate connected component of \(O(n)\), and the displayed variance is continuous.

**Illustration.** For spectrum \((9,1)\), diagonal \(K\) gives trace error \(1\) with probability \(9/10\) and \(9\) with probability \(1/10\), so its mean is \(9/5\) and variance is \(144/25\). For the rotated \(K=\begin{pmatrix}5&4\\4&5\end{pmatrix}\), both pivots give trace error \(9/5\) exactly. The matrices have identical eigenvalues and identical expected trace loss, but maximally different one-step variability.

## Verification
The standalone `verify.py` uses exact rational arithmetic to verify the joint spectral coupling and four polynomial convex tests for 28 positive-definite Householder-conjugate cases. It also verifies the two-dimensional equality example exactly. It tests 490 further real positive-definite matrices, six convex test functions, the variance envelope, and a constructive numerical zero-diagonal basis in dimensions two through eight. Reproduce with Python 3, NumPy, and SciPy by running `python verify.py`; its expected completion marker is `VERIFY_OK`. Finite checks corroborate the proof but do not replace the all-dimension analytical argument.

## Relationship to prior work
Epperly's 2026 analysis of randomly pivoted Cholesky (arXiv:2608.20633v1, §§1.1–1.3 and §4) gives the diagonal-weighted pivot rule, strong multistep mean/high-probability trace bounds, and a Jensen inequality for **traces of convex spectral functions of the residual matrix**. The theorem here concerns **convex functions of the scalar trace error** and determines sharp laws over a prescribed spectral orbit; these nonlinear expressions are not interchangeable. Chen, Epperly, Tropp, and Webber (arXiv:2207.06503, §5.1) derive the one-step expected residual matrix and develop multistep bounds, but their mean identity alone does not determine the trace-loss distribution. Steinerberger (arXiv:2404.11487, §§1–2) studies pivot probabilities and exact mean spectral identities. The existence of an orthogonal basis with zero quadratic diagonal is a classical traceless-matrix consequence of the Schur–Horn/zero-diagonal principle and is proved directly above; neither the zero-diagonal principle nor conditional Jensen is claimed new. Related column subset and pivoting studies address different losses and selection criteria.

## Limitations
The result is restricted to real symmetric **positive-definite** matrices, independent of a particular application-specific kernel coordinate system, and a single diagonal-proportionally sampled pivot. Its lower extremizer is an existence construction, not an efficient kernel-matrix preprocessing algorithm. Convex order does not by itself order arbitrary tail probabilities. No statement is made about multistep pivot adaptation, deterministic pivoting, finite-precision behavior, or semidefinite matrices with zero diagonal entries. An equivalent scalar convex-order observation could exist under size-biased spectral sampling or Rao–Blackwell terminology; exhaustive literature uniqueness is not asserted.

## References
1. E. N. W. Epperly, *A new analysis of the randomly pivoted Cholesky algorithm*, arXiv:2608.20633v1 (first posted 2026-08-21), §§1 and 4.
2. Y. Chen, E. N. W. Epperly, J. A. Tropp, and R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, arXiv:2207.06503 (first posted 2022), §5.1.
3. S. Steinerberger, *Randomly Pivoted Partial Cholesky: Random How?*, arXiv:2404.11487 (2024), §§1–2.
4. E. N. W. Epperly, J. A. Tropp, and R. J. Webber, *Embrace Rejection: Kernel Matrix Approximation by Accelerated Randomly Pivoted Cholesky*, arXiv:2410.03969 (2024 preprint; later versions).
