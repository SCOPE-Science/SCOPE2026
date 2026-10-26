# Generic one-rank inflation in trace-matched Lanczos computational uncertainty

## Finding

For an exact, nonterminating Lanczos run on a real symmetric positive-definite matrix, the rank-one-boundary-plus-isotropic-bulk covariance approximation associated with the Schur-complement construction of Fifen, Karambal and Hennig has **one more positive eigenvalue** than the exact conditional computational-uncertainty covariance. Precisely, if \(1\le m\le d-2\) and two consecutive Lanczos residual coefficients \(\beta_m,\beta_{m+1}\) are nonzero, then

\[
\operatorname{rank}(\widehat R_m)=d-m+1,
\qquad \operatorname{rank}(R_m)=d-m.
\]

The Gaussian distributions with common mean and covariance \(\widehat R_m\) and \(R_m\), respectively, are mutually singular; either directed measure-theoretic Kullback--Leibler divergence is infinite. This persists when the matrix-norm approximation error tends to zero in a nonterminating family.

The smallest defined instance with an isotropic bulk has dimension three. For
\[
A=\begin{pmatrix}2&1&0\\1&2&1\\0&1&2\end{pmatrix},
\quad q_1=e_1,\quad m=1,
\]
the approximate residual covariance is
\[
\widehat R_1=\begin{pmatrix}
\frac14&-\frac12&\frac14\\
-\frac12&\frac{29}{25}&-\frac{19}{50}\\
\frac14&-\frac{19}{50}&\frac{59}{100}
\end{pmatrix},\qquad \det\widehat R_1=\frac1{100}>0,
\]
whereas \(R_1=A^{-1}-\frac12 e_1e_1^{\mathsf T}\) has rank two and kills the exactly observed direction \(Aq_1=(2,1,0)^{\mathsf T}\). That direction is assigned the strictly positive approximate variance
\[
(Aq_1)^{\mathsf T}\widehat R_1(Aq_1)=\frac4{25}.
\]

## Assumptions and scope

Let \(d\ge3\) and \(A\in\mathbb R^{d\times d}\) be symmetric positive definite. Run Lanczos in exact arithmetic from a unit initial vector. Let \(Q_m\), \(T_m=Q_m^{\mathsf T}AQ_m\), \(q_{m+1}\), and \(\beta_m>0\) satisfy \(AQ_m=Q_mT_m+\beta_mq_{m+1}e_m^{\mathsf T}\), with \(1\le m\le d-2\). Assume \(\beta_{m+1}>0\), i.e. the next Lanczos step does not terminate. Set \(r=d-m\ge2\). Choose an orthogonal complement basis \(Q_\perp\) whose first two columns are \(q_{m+1},q_{m+2}\); let \(e_1\) denote its first coordinate vector.

Define the positive-definite Schur complement and its inverse by
\[
S=Q_\perp^{\mathsf T}AQ_\perp-\gamma e_1e_1^{\mathsf T},\quad
\gamma=\beta_m^2 e_m^{\mathsf T}T_m^{-1}e_m,\quad B=S^{-1}.
\]
Set \(a=\beta_m Q_mT_m^{-1}e_m\), \(v=Q_\perp Be_1\), \(u=v/\|v\|_2\), and \(P_\perp=I-Q_mQ_m^{\mathsf T}\). Define
\[
p_j=e_1^{\mathsf T}B^je_1,\quad
\sigma=\frac{p_3}{p_2},\quad
\omega=\frac{\operatorname{tr}B-\sigma}{r-1}.
\]
The approximation studied is the **analytic exact-trace** version of the covariance construction, not its finite-probe Monte Carlo estimator:
\[
\widehat R_m=p_1aa^{\mathsf T}-av^{\mathsf T}-va^{\mathsf T}
+\sigma uu^{\mathsf T}+\omega(P_\perp-uu^{\mathsf T}).
\]
The target covariance is \(R_m=A^{-1}-Q_mT_m^{-1}Q_m^{\mathsf T}\). The distinction between \(\widehat R_m\), a computational-uncertainty covariance, and the full-rank inverse approximation \(\Sigma_m=Q_mT_m^{-1}Q_m^{\mathsf T}+\widehat R_m\) is essential: the singularity conclusion applies to \(R_m\) versus \(\widehat R_m\), **not** to the two full inverse covariances.

## Proof

**1. Exact conditional rank and nullspace.** The block inverse formula for \(A\) shows
\[
R_m=A^{-1}-Q_mT_m^{-1}Q_m^{\mathsf T}\succeq0.
\]
The Gaussian-conditioning congruence \(R_m=(I-P)A^{-1}(I-P)^{\mathsf T}\), with \(P=Q_mT_m^{-1}Q_m^{\mathsf T}A\), proves \(\operatorname{rank}R_m=d-m\) and \(\ker R_m=A\operatorname{range}(Q_m)\). One can verify the rank directly by Schur complement: in the block basis \([Q_m,Q_\perp]\) the conditional covariance has an invertible \(r\times r\) Schur complement on the unresolved directions and exactly \(m\) null directions.

**2. Positivity and exact rank of the approximation.** Write \(p_2=\|v\|_2^2>0\). The unit vectors \(a/\|a\|_2\) and \(u\) are orthogonal. Relative to this two-dimensional plane, the first four terms of \(\widehat R_m\) have the matrix
\[
K=\begin{pmatrix}
 p_1\|a\|_2^2&-\|a\|_2\sqrt{p_2}\\
 -\|a\|_2\sqrt{p_2}&p_3/p_2
\end{pmatrix},
\quad
\det K=\|a\|_2^2\frac{p_1p_3-p_2^2}{p_2}.
\]
Cauchy--Schwarz applied to \(B^{1/2}e_1\) and \(B^{3/2}e_1\) gives \(p_2^2\le p_1p_3\), with equality precisely when \(Be_1\) is proportional to \(e_1\). But the second coordinate of \(Se_1\) equals the nonzero Lanczos coefficient \(\beta_{m+1}\): the rank-one Schur downdate affects only the first diagonal entry. Thus \(Se_1\) and hence \(Be_1\) cannot be proportional to \(e_1\). The inequality is strict, so \(K\succ0\).

The remaining \(r-1\) directions carry scalar variance \(\omega>0\), since \((r-1)\omega=\operatorname{tr}[(I-uu^{\mathsf T})Q_\perp BQ_\perp^{\mathsf T}]>0\) on a nonzero subspace. This bulk is orthogonal to the two-dimensional plane and to the other \(m-1\) resolved directions. Therefore the exact rank is \(2+(r-1)=r+1\), whereas the target rank is \(r\). In fact, \(\ker\widehat R_m=\{z\in\operatorname{range}(Q_m):a^{\mathsf T}z=0\}\), with dimension \(m-1\).

**3. Mutual singularity.** Both Gaussian laws are supported on affine subspaces of their covariance ranks. The exact law concentrates with probability one on its \(r\)-dimensional affine support, but the approximate Gaussian, with rank \(r+1\), assigns probability zero to any such affine subspace. They are mutually singular and each KL divergence is infinite, regardless of the shared mean.

**4. Minimal, exact-rational certificate.** The displayed three-dimensional matrix has leading principal minors \(2,3,4\), hence is positive definite. The first Lanczos coefficients are \(\beta_1=\beta_2=1\). Here \(T_1=(2)\), \(S=\begin{psmallmatrix}3/2&1\\1&2\end{psmallmatrix}\), and
\[
B=\begin{pmatrix}1&-1/2\\-1/2&3/4\end{pmatrix},\quad
(p_1,p_2,p_3)=(1,5/4,27/16),\quad
\sigma=27/20,\quad\omega=2/5.
\]
Inserting these into the definition gives the displayed \(\widehat R_1\) and its determinant \(1/100\). Exact inversion gives
\[
R_1=\begin{pmatrix}
1/4&-1/2&1/4\\-1/2&1&-1/2\\1/4&-1/2&3/4
\end{pmatrix},\quad R_1(2,1,0)^{\mathsf T}=0.
\]
The approximate quadratic form on that same observed vector is \(4/25\).

**5. Arbitrarily small matrix error, persistent support mismatch.** For \(0<\epsilon<\sqrt3\), take
\[
A_\epsilon=\begin{pmatrix}2&1&0\\1&2&\epsilon\\0&\epsilon&2\end{pmatrix}.
\]
Its leading principal minors are \(2,3,2(3-\epsilon^2)>0\); \(\beta_1=1\) and \(\beta_2=\epsilon\). Exact substitution yields
\[
(A_\epsilon e_1)^{\mathsf T}\widehat R_1(A_\epsilon e_1)
=\frac{4\epsilon^2}{(4+\epsilon^2)^2}>0,
\qquad
\det\widehat R_1=\frac{\epsilon^2}{2(3-\epsilon^2)(4+\epsilon^2)^2}>0.
\]
The analytic matrix entries of \(\widehat R_1\) and \(R_1\) extend continuously to \(\epsilon=0\), where the coupling direction becomes a Schur-complement eigenvector and the two covariances coincide. Consequently \(\|\widehat R_1-R_1\|_2\to0\) as \(\epsilon\downarrow0\), although mutual singularity and infinite KL persist for every strictly positive \(\epsilon\).

## Verification

`CHECK.py` uses only the Python standard library to reconstruct the three-dimensional certificate with exact rational arithmetic, calculate the exact Schur moments, construct both covariances, check the determinant, exact observation nullspace, and spurious variance. It also checks the general two-dimensional coupling determinant for several exact-rational positive-definite tridiagonal matrices. Run `python CHECK.py` in the directory containing this result. The proof above, not these finite checks, establishes the universal assertions.

## Relationship to prior work

Fifen, Karambal and Hennig (2026), Section 4, equations (21)--(30), explicitly define the Schur coupling, trace-matched isotropic bulk and Gaussian sampler analyzed here. Their Proposition 14 bounds covariance-matrix approximation error, while Proposition 16 gives the rank and nullspace of the **exact** conditional covariance. The result here instead determines the exact rank of the **approximated** conditional covariance and the resulting singularity of the two Gaussian measures. The source's full-rank inverse-covariance KL experiments concern a different pair of measures and are not contradicted.

Cockayne, Oates, Ipsen and Girolami (2019), and Bartels, Cockayne, Ipsen and Hennig (2019), explain exact Gaussian linear conditioning and posterior contraction; these facts motivate retaining the exactly determined observation subspace, but their inspected results do not analyze this later rank-one-plus-isotropic Lanczos formula. The rank inequality is specific to the complement boundary construction and uses its consecutive Lanczos coefficients, not merely the general fact that Gaussian conditioning has a nullspace.

## Limitations

All claims use exact arithmetic and the analytic trace-matched complement coefficient, not numerical trace estimation, finite-precision Lanczos, or any unexamined software implementation. The result applies when \(\beta_m\beta_{m+1}>0\) and \(d-m\ge2\); it does not assert rank inflation after exact Lanczos breakdown or in a one-dimensional complement. It concerns the computational-uncertainty posterior rather than the full inverse-covariance approximation. Infinite KL is a measure-theoretic consequence of different support ranks; it does not imply that bounded test-function expectations or matrix norms must be far apart.

## References

1. H. Fifen, I. Karambal and P. Hennig, *Stochastic Lanczos Quadrature for Computational Uncertainty in Linear Algebra*, arXiv:2609.10080v1 (first publicly posted 2026-09-09), https://arxiv.org/html/2609.10080v1 ; especially Section 4, Proposition 14, Proposition 16.
2. J. Cockayne, C. J. Oates, I. C. F. Ipsen and M. Girolami, *A Bayesian Conjugate Gradient Method*, Bayesian Analysis 14 (2019), arXiv:1801.05242, https://arxiv.org/abs/1801.05242 .
3. S. Bartels, J. Cockayne, I. C. F. Ipsen and P. Hennig, *Probabilistic Linear Solvers: A Unifying View*, Statistics and Computing 29 (2019), https://doi.org/10.1007/s11222-019-09897-7 .
