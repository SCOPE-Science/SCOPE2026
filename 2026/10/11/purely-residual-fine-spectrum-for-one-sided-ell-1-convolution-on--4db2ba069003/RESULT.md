# Purely residual fine spectrum for one-sided \(\ell_1\) convolution on \(\ell_\infty\)
## Finding
Let \(a=(a_n)_{n\ge0}\in\ell_1(\mathbb N_0)\), and define the one-sided convolution operator \(T_a\) on complex \(\ell_\infty(\mathbb N_0)\) by
\[
(T_a x)_n=\sum_{k=0}^n a_kx_{n-k}.
\]
Write
\[
\Phi_a(z)=\sum_{n\ge0}a_nz^n,\qquad |z|\le1.
\]
Then
\[
\|T_a\|=\|a\|_1.
\]
If \(a\) is non-scalar, meaning that \(a_m\ne0\) for at least one \(m\ge1\), then
\[
\sigma(T_a)=\sigma_r(T_a)=\Phi_a(\overline{\mathbb D}),
\qquad
\sigma_p(T_a)=\sigma_c(T_a)=\varnothing.
\]
Thus every spectral value is residual. If \(a=(a_0,0,\ldots)\), then \(T_a=a_0I\), so the sole spectral value \(a_0\) is an eigenvalue and the residual and continuous spectra are empty.

## Assumptions and scope
The scalar field is \(\mathbb C\). The index set is \(\mathbb N_0=\{0,1,2,\ldots\}\), and \(\ell_\infty(\mathbb N_0)\) carries the supremum norm. The kernel is any absolutely summable one-sided sequence \(a\in\ell_1(\mathbb N_0)\); finite support is not assumed. The residual spectrum means those \(\lambda\) for which \(T_a-\lambda I\) is injective but has non-dense range, and the continuous spectrum means injective operators with dense non-surjective range.

## Proof
Let \(R\) be the right shift,
\[
R(x_0,x_1,\ldots)=(0,x_0,x_1,\ldots).
\]
Because \(\|R^k\|=1\) and \(a\in\ell_1\), the operator series
\[
T_a=\sum_{k\ge0}a_kR^k
\]
converges in operator norm, giving \(\|T_a\|\le\|a\|_1\). For the reverse inequality, fix \(N\). Choose a vector \(x^{(N)}\) with \(\|x^{(N)}\|_\infty=1\) and, for \(0\le k\le N\), choose \(x^{(N)}_{N-k}\) so that \(a_kx^{(N)}_{N-k}=|a_k|\) whenever \(a_k\ne0\). Then
\[
\|(T_ax^{(N)})_N\|=\sum_{k=0}^N|a_k|.
\]
Letting \(N\to\infty\) gives \(\|T_a\|=\|a\|_1\).

Assume now that \(a\) is non-scalar, and let
\[
m=\min\{k\ge1:a_k\ne0\}.
\]
Suppose \(T_ax=\lambda x\) for a nonzero \(x\). Let \(j\) be the first index with \(x_j\ne0\). The \(j\)-th coordinate gives \(\lambda=a_0\). At coordinate \(j+m\), every term involving \(a_k\) with \(1\le k<m\) vanishes by the definition of \(m\), and every term involving an index of \(x\) below \(j\) vanishes by the definition of \(j\). Hence the eigenvalue equation reduces to
\[
a_mx_j=0,
\]
a contradiction. Therefore \(\sigma_p(T_a)=\varnothing\).

For each \(z\in\overline{\mathbb D}\), construct a nonzero functional \(F_z\in\ell_\infty^*\) satisfying
\[
F_zR=zF_z.
\]
If \(|z|<1\), take
\[
F_z(x)=\sum_{n\ge0}z^nx_n.
\]
If \(|z|=1\), choose a complex shift-invariant Banach limit \(L\) and define
\[
F_z(x)=L((z^nx_n)_{n\ge0}).
\]
Then \(F_z\ne0\) and the desired intertwining identity holds. Operator-norm convergence of the series for \(T_a\) therefore gives
\[
F_zT_a=\Phi_a(z)F_z.
\]
Consequently the range of \(T_a-\Phi_a(z)I\) lies in the proper closed hyperplane \(\ker F_z\). Since the operator is injective, \(\Phi_a(z)\) lies in the residual spectrum. Thus
\[
\Phi_a(\overline{\mathbb D})\subseteq\sigma_r(T_a).
\]

It remains to exclude all other spectral values. Let \(A=\ell_1(\mathbb N_0)\) with convolution and unit \(e_0\). Every character \(\chi\) of \(A\) is determined by \(w=\chi(e_1)\). Since \(\|e_1\|_1=1\), one has \(|w|\le1\), and by continuity and the power relation \(e_n=e_1^{*n}\),
\[
\chi(a)=\sum_{n\ge0}a_nw^n=\Phi_a(w).
\]
Conversely each \(w\in\overline{\mathbb D}\) defines a character by this formula. Hence the Gelfand spectrum of \(a\) in \(A\) is exactly \(\Phi_a(\overline{\mathbb D})\). If \(\mu\notin\Phi_a(\overline{\mathbb D})\), then \(a-\mu e_0\) is invertible in \(A\). If \(b\in A\) is its convolution inverse, then \(T_b\) is a bounded two-sided inverse of \(T_a-\mu I\). Therefore
\[
\sigma(T_a)\subseteq\Phi_a(\overline{\mathbb D}).
\]
Combining the two inclusions gives the asserted spectral and fine-spectral identities.

## Verification
The proof independently checks the two points on which the infinite-support extension depends. First, the boundary \(|z|=1\) is handled by shift-invariant Banach-limit eigenfunctionals of the adjoint, so no density conclusion is inferred merely from approximate eigenvectors. Second, the reverse spectral inclusion is proved in the full convolution Banach algebra \(\ell_1(\mathbb N_0)\), not by truncating the kernel. The norm identity is also exact for infinite support, obtained from finite-coordinate phase matching followed by monotone convergence of the absolute partial sums.

## Relationship to prior work
Saha and Patra develop fine spectral tools for convolution-type operators on non-separable sequence spaces and prove, for \(\ell_\infty\), that every finite-band lower triangular Toeplitz operator \(p(R)\) has spectrum and residual spectrum equal to \(p(\overline{\mathbb D})\), with empty point and continuous spectra. The present result removes the finite-band restriction and treats every one-sided absolutely summable kernel. Earlier fine-spectrum work of Birbonshi and Srivastava and of Altun concerns finite-band triangular matrices or Toeplitz operators. General convolution results on weighted Hahn spaces concern a different ambient space and do not imply the \(\ell_\infty\) fine-spectrum classification here.

## Limitations
The theorem is one-sided and scalar-valued. It does not classify two-sided Laurent convolution, matrix-valued kernels, or kernels outside \(\ell_1\). The boundary residual-spectrum argument uses existence of shift-invariant Banach limits, hence the usual choice principle behind that construction. No claim is made about pseudospectra or quantitative resolvent growth near \(\Phi_a(\overline{\mathbb D})\).

## References
1. S. Saha and A. Patra, *Spectral Properties of Convolution Operators on Non-Separable Sequence Spaces*, arXiv:2610.02919v1, 2026.
2. R. Birbonshi and P. D. Srivastava, *On some study of the Fine Spectra of n-th band triangular matrices*, arXiv:1606.05993, 2016; Complex Analysis and Operator Theory 11 (2017), 739–753.
3. M. Altun, *On the fine spectra of triangular Toeplitz operators*, Applied Mathematics and Computation 217 (2011), 8044–8051.
4. S. Saha and A. Patra, *Convolution Operators on Weighted Hahn Spaces*, arXiv:2606.22912, 2026.
