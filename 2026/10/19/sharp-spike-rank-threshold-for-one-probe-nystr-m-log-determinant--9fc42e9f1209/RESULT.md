# Sharp spike-rank threshold for one-probe Nyström log-determinant variance

## Finding
For every positive integer pair \(r,s\), every integer \(1\leq\ell<r+s\), and every real \(t\geq1\), consider the positive-definite two-level matrix \(A_t=\operatorname{diag}(tI_r,I_s)\). A Gaussian Nyström approximation with \(\ell\) columns is used to precondition the regularized log-determinant, and one independent Gaussian vector estimates the remaining matrix-logarithm trace exactly (without Lanczos truncation).

The expected squared estimation error obeys
\[
\mathbb E(\widehat L_t-L_t)^2
=2(r-\ell)_+\log^2(1+t)+R_{r,s,\ell}(t),\qquad
0\leq R_{r,s,\ell}(t)\leq C_{r,s,\ell}<\infty.
\]
Here the finite constant depends on the integer dimensions but not on the spike contrast \(t\). Therefore the mean-square error is uniformly bounded over all \(t\geq1\) precisely when \(\ell\geq r\). For \(\ell<r\), the coefficient \(2(r-\ell)\) of the divergent \(\log^2(1+t)\) term is exact.

In particular, the zero-oversampling case \(\ell=r\) already has finite, contrast-uniform expected squared error, despite the absence of the positive oversampling required by a generic error bound for this algorithm.

## Assumptions and scope
Fix integers \(r,s\geq1\) and \(1\leq\ell<n=r+s\). Write \(A_t=\operatorname{diag}(tI_r,I_s)\), \(t\geq1\), and draw \(\Omega=\begin{pmatrix}U\\V\end{pmatrix}\in\mathbb R^{n\times\ell}\), with mutually independent standard-normal entries, \(U\in\mathbb R^{r\times\ell}\), \(V\in\mathbb R^{s\times\ell}\). Almost surely, \(\Omega^{\mathsf T}A_t\Omega\) is invertible. Define
\[
\widehat A_t=A_t\Omega(\Omega^{\mathsf T}A_t\Omega)^{-1}\Omega^{\mathsf T}A_t,
\quad P_t=I_n+\widehat A_t,
\quad M_t=P_t^{-1/2}(I_n+A_t)P_t^{-1/2}.
\]
Independently draw \(w\sim N(0,I_n)\). Set \(L_t=\log\det(I_n+A_t)\) and \(\widehat L_t=\log\det(P_t)+w^{\mathsf T}\log(M_t)w\), using the real principal symmetric matrix logarithm. This is the exact-quadratic-form version of the one-probe estimator; there is no stochastic Lanczos quadrature truncation error in the claim. All expectations include \(\Omega\) and \(w\).

## Proof
**Step 1: conditional mean and variance.** Since \(\det(I_n+A_t)=\det(P_t)\det(M_t)\), the conditional expectation of \(\widehat L_t\) given \(\Omega\) is \(L_t\). The standard quadratic-form identity for independent real Gaussian \(w\) gives
\[
\mathbb E_w[(\widehat L_t-L_t)^2\mid\Omega]
=2\|\log(M_t)\|_F^2.
\tag{1}
\]
Thus there is no extra bias-squared term to bound.

**Step 2: exact spike directions missed by the sketch.** Almost surely, \(\operatorname{rank}(U)=\min(r,\ell)\). Let \(E=\ker(U^{\mathsf T})\oplus\{0\}\subset\mathbb R^r\oplus\mathbb R^s\). Then \(\dim E=(r-\ell)_+\). For any \(e\in E\), \(\Omega^{\mathsf T}A_te=0\) and \(A_te=te\); hence \(\widehat A_te=0\), \(P_te=e\), and \(M_te=(1+t)e\). As these matrices are real symmetric, \(E\) and \(H=E^\perp\) simultaneously reduce each. In particular,
\[
\|\log M_t\|_F^2
=(r-\ell)_+\log^2(1+t)+\|\log(M_t|_H)\|_F^2.
\tag{2}
\]
If \(\ell<r\), \(H=\operatorname{range}(U)\oplus\mathbb R^s\); if \(\ell\geq r\), \(H=\mathbb R^n\). No eigenvalue is lost in this decomposition; the single-spike two-dimensional case is only a strict specialization, not the general rank boundary.

**Step 3: contrast-free bound on the retained block.** The positive-semidefinite Nyström residual \(B_t=A_t-\widehat A_t\) has the variational characterization
\[
y^{\mathsf T}B_ty=\min_{c\in\mathbb R^\ell}(y-\Omega c)^{\mathsf T}A_t(y-\Omega c).
\tag{3}
\]
Take any \(y=(a,b)\in H\). Then \(a\in\operatorname{range}(U)\). Choosing \(c=U^+a\), where \(U^+\) is the Moore--Penrose pseudoinverse, makes the upper block of \(y-\Omega c\) vanish. Thus
\[
0\leq y^{\mathsf T}B_ty\leq\|b-VU^+a\|_2^2
\leq(1+\|VU^+\|_2^2)\|y\|_2^2.
\tag{4}
\]
Since \(M_t=I_n+P_t^{-1/2}B_tP_t^{-1/2}\) and \(P_t\succeq I_n\), equation (4) and simultaneous reduction imply the spectral inclusion
\[
1\leq\lambda(M_t|_H)\leq 2+\|VU^+\|_2^2.
\tag{5}
\]
Therefore
\[
0\leq 2\|\log(M_t|_H)\|_F^2
\leq 2n\log^2(2+\|VU^+\|_2^2).
\tag{6}
\]
The right-hand side is independent of \(t\).

**Step 4: the required logarithmic inverse moment exists with zero oversampling.** Put \(k=\min(r,\ell)\). Choose a square \(k\times k\) Gaussian submatrix \(G\) of \(U\), taking \(k\) rows if \(r\geq\ell\) or \(k\) columns if \(r<\ell\). Then \(\sigma_{\min}(U)\geq\sigma_{\min}(G)\), so \(\|U^+\|_2\leq\|G^{-1}\|_2\) almost surely. The adjugate formula bounds \(\|G^{-1}\|_2\leq c_k\|G\|_F^{k-1}/|\det G|\). By Gaussian QR, \(|\det G|\) has the law of the product of independent chi variables with degrees \(k,k-1,\dots,1\), whose negative moments of orders less than one are finite. In particular, Hölder's inequality with exponents \(3\) and \(3/2\) gives
\[
\mathbb E\|G^{-1}\|_2^{1/2}
\leq c_k^{1/2}(\mathbb E\|G\|_F^{3(k-1)/2})^{1/3}
(\mathbb E|\det G|^{-3/4})^{2/3}<\infty.
\tag{7}
\]
The Gaussian matrices \(U\) and \(V\) are independent and \(V\) has moments of every positive order, hence \(\mathbb E\|VU^+\|_2^{1/2}<\infty\). The elementary growth bound \(\log^2(2+z^2)\leq c(1+z^{1/2})\), for \(z\geq0\), shows
\[
C_{r,s,\ell}:=2n\mathbb E\log^2(2+\|VU^+\|_2^2)<\infty.
\tag{8}
\]

**Step 5: combine.** Taking expectations in (1)--(2), and applying (6)--(8), gives the asserted exact diverging term and uniformly bounded nonnegative remainder. If \(\ell<r\), \(\log^2(1+t)\to\infty\) forces divergence; if \(\ell\geq r\), the term vanishes and the constant (8) is finite. This proves both directions of the sharp threshold.

## Verification
A standalone NumPy script, `verify.py`, checks the exact spike eigenspace, determinant identity, spectral bounds, and remainder inequalities on 1,008 independent numerical examples covering \(1\leq r\leq4\), \(1\leq s\leq3\), all \(1\leq\ell<r+s\), and \(t\in\{1,10,1000\}\). It outputs `VERIFY_OK numerical_matrix_cases=1008`. This finite check is independent of, and does not certify, the infinite-family argument. The finite logarithmic inverse moment in (7)--(8) is proved analytically rather than numerically.

## Relationship to prior work
Cortinovis and Toni, *Detecting When One Probe Vector Is Enough for Preconditioned Log-Determinant Approximation*, arXiv:2601.05778 (original public version, 9 January 2026), formulate precisely the Nyström preconditioner and independent one-Gaussian-vector trace estimator considered here. Their Section 2 gives ideal best-spectral-rank variance (which presupposes an ideal rather than Gaussian Nyström sketch), and their Section 3.1 (Theorem 3.2) establishes a generic bound with positive oversampling \(p\geq2\) and \(\ell\geq4\). Neither inspected result implies the sharp almost-sure spike-subspace decomposition plus contrast-uniform zero-oversampling second moment above. Their experiments do not establish an exact iff threshold for this two-level spectral family.

Frangella, Tropp, and Udell's *Randomized Nyström Preconditioning* (SIAM J. Matrix Anal. Appl., 2023) analyzes Nyström preconditioners and effective-dimension bounds for linear solves; its main object is not the independent-Gaussian one-probe log-determinant variance. The algebraic Nyström residual variational formula, Gaussian quadratic-form variance identity, QR chi-product law, and logarithmic integrability are standard ingredients, not claimed as original here. The claim is specifically their combination yielding the precise all-multiplicity zero-oversampling phase transition for the stated estimator and family; no novelty is attributed to a lone two-dimensional special case. A semantically equivalent older argument may exist; independent literature validation is outstanding.

## Limitations
The matrix has exactly two flat eigenvalue levels and fixed finite \(r,s,\ell\). The finite constant may depend on these dimensions and is not claimed universal in dimension. The probe is Gaussian and independent of the Gaussian sketch. All operations are in exact arithmetic; there is no bound on stochastic Lanczos truncation, finite-precision effects, wall-clock cost, or arbitrary spectral tails. The large-contrast lower bound does not assert failure of alternative trace estimators or adaptive procedures. No independent mathematical audit has been performed.

## References
1. A. Cortinovis and D. Toni, *Detecting When One Probe Vector Is Enough for Preconditioned Log-Determinant Approximation*, arXiv:2601.05778v1, publicly posted 2026-01-09; *Numerical Linear Algebra with Applications* (2026), DOI: 10.1002/nla.70106. https://arxiv.org/abs/2601.05778 ; https://onlinelibrary.wiley.com/doi/full/10.1002/nla.70106
2. Z. Frangella, J. A. Tropp, and M. Udell, *Randomized Nyström Preconditioning*, *SIAM Journal on Matrix Analysis and Applications* (2023), DOI: 10.1137/21M1466244; author manuscript https://tropp.caltech.edu/papers/FTU23-Randomized-Nystrom-SIMAX.pdf
