# Optimal diagonal conditioning of bivariate second-order Hermite chaos

## Finding

For a bivariate standard Gaussian pair with nondegenerate correlation \(\rho\), the homogeneous degree-two, density-derivative multivariate-Hermite Gram block admits a **covariance-independent optimal positive diagonal congruence scale**. Exactly,
\[
\min_{D\succ0\text{ diagonal}}\kappa_2(DG_\rho D)
=\left(\frac{1+|\rho|}{1-|\rho|}\right)^2,
\qquad
D\propto\operatorname{diag}(1,\sqrt2,1),
\]
and that minimizer is unique modulo a positive scalar. In comparison, Jacobi normalization of each basis polynomial to unit variance is strictly suboptimal for every nonzero correlation, with
\[
\lim_{|\rho|\uparrow1}
\frac{\kappa_2(J_\rho G_\rho J_\rho)}{\min_D\kappa_2(DG_\rho D)}=\frac98,
\qquad
J_\rho=\operatorname{diag}(G_{\rho,ii}^{-1/2}).
\]
The new object studied here is the exact best diagonal *conditioning* of an existing correlated-Hermite mass block, not its already-known entries.

## Assumptions and scope

Let \(-1<\rho<1\) and
\[
\xi=(\xi_1,\xi_2)^\mathsf T\sim\mathcal N(0,\Sigma_\rho),
\quad
\Sigma_\rho=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}.
\]
Put \(Q=\Sigma_\rho^{-1}\), \(a=Q_{11}=Q_{22}=(1-\rho^2)^{-1}\), \(b=Q_{12}=-\rho(1-\rho^2)^{-1}\), and \(Y=Q\xi\). Use the *unnormalized*, density-derivative multivariate Hermite polynomials
\[
H_{20}=Y_1^2-a,\qquad
H_{11}=Y_1Y_2-b,\qquad
H_{02}=Y_2^2-a.
\]
All expectations are under this Gaussian distribution. The matrix \(G_\rho\) is the real symmetric positive-definite \(3\times3\) matrix of their expected pairwise products in the displayed order. A positive diagonal congruence is \(D=\operatorname{diag}(d_1,d_2,d_3)\) with every \(d_i>0\). For positive-definite matrices, \(\kappa_2\) means largest divided by smallest eigenvalue. No arbitrary dense basis mixing, nonsymmetric row/column scaling, or higher-degree mass blocks are included.

## Proof

**1. Recover the mass block with its normalization.** Since \(\operatorname{Cov}(Y)=Q\), the centered Gaussian fourth-moment (Isserlis) identity gives
\[
G_\rho=
\begin{pmatrix}
2a^2&2ab&2b^2\\
2ab&a^2+b^2&2ab\\
2b^2&2ab&2a^2
\end{pmatrix}.
\]
For \(|\rho|<1\), these three quadratic chaos polynomials are linearly independent in Gaussian \(L^2\), so \(G_\rho\) is strictly positive-definite. This same matrix appears as the degree-two block of the previously published double-product matrix; it is not claimed to be a new moment identity.

**2. Exhibit a simple candidate and its complete spectrum.** Let \(D_*=\operatorname{diag}(1,\sqrt2,1)\) and \(B_\rho=D_*G_\rho D_*\). Three mutually orthonormal eigenvectors are
\[
v_+=\frac12(1,\sqrt2,1)^\mathsf T,\qquad
v_-=\frac12(1,-\sqrt2,1)^\mathsf T,\qquad
v_0=\frac1{\sqrt2}(1,0,-1)^\mathsf T.
\]
Direct multiplication gives corresponding eigenvalues
\[
\frac{2}{(1+\rho)^2},\qquad
\frac{2}{(1-\rho)^2},\qquad
\frac2{1-\rho^2}.
\]
The third lies between the first two. Therefore
\[
\kappa_2(B_\rho)=\left(\frac{1+|\rho|}{1-|\rho|}\right)^2.
\]

**3. Prove global optimality over every asymmetric diagonal scale.** Every eligible \(D\) has the form \(D=D_*T\) with a positive diagonal \(T\), so \(DG_\rho D=T B_\rho T\). Select the two extremal eigenvectors of \(B_\rho\) among \(v_+,v_-\) and denote them by \(v_{\min},v_{\max}\). Their componentwise squared magnitudes agree:
\[
|(v_{\min})_j|^2=|(v_{\max})_j|^2\in\{1/4,1/2,1/4\}.
\]
Consequently the common positive quantity
\[
q=\|T^{-1}v_{\min}\|_2^2
 =\|T^{-1}v_{\max}\|_2^2
\]
exists for **all** positive diagonal \(T\), not just reflection-symmetric ones. Apply Rayleigh--Ritz with trial vectors \(T^{-1}v_{\min}\) and \(T^{-1}v_{\max}\):
\[
\lambda_{\min}(TB_\rho T)\le\frac{\lambda_{\min}(B_\rho)}q,
\qquad
\lambda_{\max}(TB_\rho T)\ge\frac{\lambda_{\max}(B_\rho)}q.
\]
Dividing yields \(\kappa_2(TB_\rho T)\ge\kappa_2(B_\rho)\), attaining equality at \(T=I\).

For \(\rho\ne0\), equality forces both trial vectors to be extremal eigenvectors of \(TB_\rho T\). If \(TB_\rho T(T^{-1}v)=\lambda T^{-1}v\), while \(B_\rho v=\lambda_*v\), then \(T^2v=(\lambda_*/\lambda)v\). Every coordinate of each of \(v_+,v_-\) is nonzero, so positive diagonal \(T^2\) must be scalar. At \(\rho=0\), \(B_0=2I\), and \(TB_0T=2T^2\) has condition number one only if \(T\) is scalar. Hence \(D_*\) is the **unique** optimal diagonal up to scalar at every eligible \(\rho\).

**4. Quantify the failure of usual unit-variance normalization.** Put \(r=|\rho|\) and \(u=-\sqrt2\rho/\sqrt{1+\rho^2}\). Explicitly,
\[
J_\rho G_\rho J_\rho=
\begin{pmatrix}1&u&r^2\\u&1&u\\r^2&u&1\end{pmatrix}.
\]
Its odd eigenvalue is \(1-r^2\), and its even eigenvalues are
\[
\lambda_\pm=\frac{2+r^2\pm\sqrt{r^4+8u^2}}2,
\qquad
\lambda_+\lambda_- = \frac{(1-r^2)^2}{1+r^2}.
\]
As \(r\uparrow1\), \(\lambda_+\to3\), \(\lambda_-\sim(1-r^2)^2/6\), and \(1-r^2\) is asymptotically between them. Thus
\[
\kappa_2(J_\rho G_\rho J_\rho)\sim\frac{18}{(1-r^2)^2},
\quad
\min_D\kappa_2(DG_\rho D)\sim\frac{16}{(1-r^2)^2},
\]
which proves the asserted \(9/8\) ratio. At \(r>0\), Jacobi's middle-to-outer diagonal ratio is \(\sqrt{2/(1+r^2)}\), not \(\sqrt2\); the uniqueness result proves its strict inferiority without relying on asymptotics.

## Verification

The accompanying standalone `VERIFY.py` reconstructs the matrix algebra using exact SymPy symbolic identities. It checks all three eigenpairs, the determinant, the unit-diagonal matrix and its even eigenvalue product, and the \(9/8\) limit. It then compares \(3,200\) reproducibly seeded positive diagonal scalings at eight correlations against the closed-form global optimum, alongside the proposed scale. These finite tests are supplemental; the infinite-dimensional quantifier over all positive diagonal entries is proved by the Rayleigh argument in Step 3, not by sampling.

Run `python VERIFY.py` with SymPy and NumPy installed. The proof does not rely on this code and uses no external certificate.

## Relationship to prior work

Rahman (2017) developed the weakly orthogonal correlated multivariate Hermite framework. Lyman and Iaccarino (2021) gave exact **double-product** formulas. Lyman (2026), Section 5, writes the complete degree-two Gram block inside her \(X^{(2)}\) matrix; that previously known block is our starting data. Those papers address moment generation, coefficient systems and triple products, rather than the global optimum of its diagonal spectral conditioning. Qu, Gao, Hinder, Ye and Zhou (2022) analyze **general** optimal diagonal preconditioning via quasiconvex/SDP formulations. Their broad algorithms apply to general inputs but do not state this covariance-independent unique minimizer, the closed spectral condition curve, or the exact Jacobi penalty for this particular Gram family. This result supplies a concrete analytic solution to a specialized instance rather than a new general-purpose optimization algorithm.

## Limitations

The mass block studied has only three modes corresponding to homogeneous degree two and two standardized correlated Gaussian coordinates. The effect of spatial operators, coefficient-dependent triple products, truncation and discretization error is not addressed. Positive *diagonal congruence* is a narrower admissible class than arbitrary invertible basis changes; full whitening can make the mass block the identity. Although the exact optimization has been checked against the above literature, implicit equivalent observations in older symmetric-square or numerical scaling treatments may exist. No high-dimensional generalization is asserted.

## References

1. S. Rahman, *Wiener–Hermite polynomial expansion for multivariate Gaussian probability measures* (2017), https://arxiv.org/abs/1704.07912.
2. L. Lyman and G. Iaccarino, *Second Order Moments of Multivariate Hermite Polynomials in Correlated Random Variables* (ICCS 2021), https://www.iccs-meeting.org/archive/iccs2021/papers/127470672.pdf, DOI:10.1007/978-3-030-77980-1_53.
3. L. Lyman, *Triple Products of Correlated Multivariate Hermite Polynomials* (first public 2026-10-21), https://arxiv.org/abs/2610.30204v1, especially Sections 3 and 5.
4. Z. Qu, W. Gao, O. Hinder, Y. Ye and Z. Zhou, *Optimal Diagonal Preconditioning* (2022), https://arxiv.org/abs/2209.00809v2, particularly Sections 1–3 and the general SDP formulation.
