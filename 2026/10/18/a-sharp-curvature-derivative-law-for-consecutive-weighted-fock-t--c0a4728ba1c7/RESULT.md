# A sharp curvature-derivative law for consecutive weighted-Fock Toeplitz eigenvalue functionals

## Finding
Let \(\gamma\in C^\infty(\mathbb R;(0,\infty))\) be constant sufficiently far to the left and satisfy \(1\le\gamma\le2\), \(|\gamma'|\le1/4\), and \(\sup|\gamma''|<\infty\). Define the radial weight \(\Phi(0)=0\), \(\Phi'(r)=r\gamma(\log r)\). In the weighted holomorphic Fock space \(\mathcal F^2_\Phi\), denote by \(\lambda_k(a)\) the \(k\)-th monomial eigenvalue of the Toeplitz operator of a bounded measurable radial symbol \(a\), and define its sharp adjacent-eigenvalue sensitivity
\[
\Delta_k=\sup_{\|a\|_{L^\infty}\le1\atop a\ \mathrm{radial}}|\lambda_{k+1}(a)-\lambda_k(a)|.
\]
The maximizer of the exact radial moment density occurs at the unique \(r_k>0\) satisfying \(k+\tfrac12=r_k^2\gamma(\log r_k)\). Then
\[
\boxed{\sqrt{k+1}\,\Delta_k=\frac{2}{\sqrt\pi}\sqrt{\frac{\gamma(\log r_k)}{2\gamma(\log r_k)+\gamma'(\log r_k)}}+O(k^{-1/2}).}
\]
For each finite \(k\), the supremum is attained by an explicit radial threshold symbol taking only the values \(\pm1\).

Suppose additionally that \(\gamma(s)=g(s)\) for all sufficiently large \(s\), where \(g\) is smooth positive \(L\)-periodic. Let \(D_g(s)=2s+\log g(s)\), with inverse \(\tau\), and define
\[
Q_g(u)=\frac{2}{\sqrt\pi}\sqrt{\frac{g(\tau(u))}{2g(\tau(u))+g'(\tau(u))}}.
\]
Then \(Q_g\) is \(2L\)-periodic and
\[
\boxed{\sqrt{k+1}\,\Delta_k=Q_g(\log(k+1))+O(k^{-1/2}).}
\]
Its exact cluster set is \([\min Q_g,\max Q_g]\). This interval is nondegenerate if and only if \(g\) is nonconstant. Equivalently, the sharp adjacent slope in the square-root metric has the complete cluster interval \([2\min Q_g,2\max Q_g]\):
\[
\frac{\Delta_k}{\sqrt{k+2}-\sqrt{k+1}}=2Q_g(\log(k+1))+O(k^{-1/2}).
\]
For the Gaussian curvature \(g\equiv1\), the universal leading constant is \(\sqrt{2/\pi}\) for \(\sqrt{k+1}\,\Delta_k\). Thus the sharp local bound remembers the *logarithmic derivative of curvature*, not merely the curvature's value.

## Assumptions and scope
The weighted Fock norm is \(\|F\|_\Phi^2=\int_{\mathbb C}|F(z)|^2e^{-2\Phi(|z|)}\,dA(z)\). The Toeplitz operator is \(T_a=P_\Phi M_a\) and the monomial eigenvalues for radial \(a\) are \(\lambda_k(a)=\langle T_ae_k,e_k\rangle\), where \(e_k\) are the normalized monomials. Uniform curvature follows from radial Hessian eigenvalues \(\gamma\ge1\) and \(\Phi''(r)=\gamma+\gamma'\ge3/4\). The hypotheses guarantee smoothness at the origin, finite monomial moments, bounded logarithmic curvature derivatives and the quantitative local Laplace expansion. No positivity, monotonicity, continuity or other regularity is required of the optimizing radial symbol \(a\). The supremum is over all bounded *radial* symbols with essential supremum at most one; it is not asserted to be the norm of a nonradial symbol map.

For a nonconstant admissible example take \(\gamma(s)=3/2+\eta(s)\sin(s)/8\), where \(\eta\) is a smooth cutoff vanishing for \(s\le0\), equal to one for \(s\ge4\), taking values in \([0,1]\) and with \(|\eta'|\le1\). Then \(L=2\pi\) and the sharp sensitivity coefficient is genuinely oscillatory.

## Proof
**1. Exact variational formula.** Radiality and angular orthogonality yield
\[
\lambda_k(a)=\int_0^\infty a(r)\,d\mu_k(r),\qquad d\mu_k(r)=\frac{r^{2k+1}e^{-2\Phi(r)}\,dr}{I_k},\quad I_k=\int_0^\infty r^{2k+1}e^{-2\Phi(r)}\,dr.
\]
Writing \(m_k=\mathbb E_{\mu_k}R^2=I_{k+1}/I_k\), one has \(d\mu_{k+1}/d\mu_k=r^2/m_k\). Therefore the total-variation duality formula gives *exactly*, for every \(k\ge0\),
\[
\boxed{\Delta_k=\mathbb E_{\mu_k}\left|\frac{R^2}{m_k}-1\right|.}
\]
Equality is attained by \(a_k(r)=\operatorname{sgn}(r^2-m_k)\). The exact threshold is \(r=\sqrt{m_k}\), and the sign at the threshold is immaterial. The same supremum over bounded *continuous* radial symbols is obtained by approximating this threshold in \(L^1(\mu_k+\mu_{k+1})\), though exact attainment is only asserted for the measurable class.

**2. Quantitative moving Gaussian saddle.** Put \(h_k(r)=(2k+1)\log r-2\Phi(r)\). Its unique mode \(r_k\) solves \(k+\tfrac12=r_k^2\gamma(\log r_k)\), and \(r_k\asymp\sqrt{k+1}\). One has
\[
h_k''(r)=-\frac{2k+1}{r^2}-2\bigl(\gamma(\log r)+\gamma'(\log r)\bigr)\le-3/2,
\]
so the normalized law of \(X_k=R-r_k\) is uniformly Gaussian-tailed. The centered quadratic coefficient at the mode is
\[
A_k=-\tfrac12h_k''(r_k)=2\gamma(\log r_k)+\gamma'(\log r_k)\in[7/4,17/4].
\]
The derivative bounds on \(\gamma\) imply \(|h_k'''(r)|\le C/r_k\) for \(|r-r_k|\le r_k/2\), while strong concavity controls its complement. Taylor expansion of the density at the mode, with normalizing integrals estimated by even Gaussian moments, gives the uniform quantitative estimates
\[
\mathbb E X_k=O(r_k^{-1}),\quad \mathbb E X_k^2=\frac1{2A_k}+O(r_k^{-1}),\quad \mathbb E|X_k|=\frac1{\sqrt{\pi A_k}}+O(r_k^{-1}),\quad \mathbb E|X_k|^3=O(1).
\]
For completeness, split \(|X_k|\le r_k^{1/8}\) from its complement. On the first part, \(h_k(r_k+x)-h_k(r_k)=-A_kx^2+O(|x|^3/r_k)\) uniformly, with an integrable dominating Gaussian; its error in integrals of polynomials of degree at most three is \(O(r_k^{-1})\). On the complement the global Gaussian tail gives an error smaller than any power of \(r_k^{-1}\). Oddness of \(x e^{-A_kx^2}\) supplies the improved mean estimate. These statements hold uniformly in the varying value of \(A_k\), so no convergence of curvature is assumed.

**3. Extraction of the sharp coefficient.** Since \(R=r_k+X_k\), the moment center satisfies
\[
m_k=r_k^2+2r_k\mathbb EX_k+\mathbb EX_k^2=r_k^2+O(1).
\]
Moreover \(R^2-m_k=2r_kX_k+X_k^2-(m_k-r_k^2)\). The inequality \(|\,|u+v|-|u|\,|\le|v|\) and the moment estimates imply
\[
\mathbb E|R^2-m_k|=2r_k\mathbb E|X_k|+O(1)=\frac{2r_k}{\sqrt{\pi A_k}}+O(1).
\]
Dividing by \(m_k=r_k^2+O(1)\) proves \(\Delta_k=2/(r_k\sqrt{\pi A_k})+O(r_k^{-2})\). The saddle relation \((k+1/2)/r_k^2=\gamma(\log r_k)\) gives the first boxed formula with absolute \(O(k^{-1/2})\) error after multiplication by \(\sqrt{k+1}\).

**4. Exact phase and cluster set.** In the periodic tail let \(s_k=\log r_k\), \(u_k=\log(k+1/2)\). The saddle equation becomes \(u_k=D_g(s_k)\). Since \(D_g'=2+g'/g\ge7/4\), this is an invertible change of phase, satisfying \(\tau(u+2L)=\tau(u)+L\). Hence the above coefficient equals \(Q_g(u_k)\), and replacing \(u_k\) by \(\log(k+1)\) changes it by \(O(k^{-1})\). Because \(\log(k+1)\) approaches every phase modulo \(2L\) along suitable integer subsequences, the cluster set is the range of \(Q_g\). If \(Q_g\) were constant, then \(g/(2g+g')\) would be constant, forcing \(g'/g\) to be constant; periodicity makes this constant zero. Conversely constant \(g\) gives constant \(Q_g\). Thus periodic variation is detected with no possibility of phase cancellation. Finally \((\sqrt{k+2}-\sqrt{k+1})^{-1}=2\sqrt{k+1}+O(k^{-1/2})\), proving the sharp square-root-metric slopes.

## Verification
The argument proves the exact total-variation optimization and the quantitative asymptotic via the local Gaussian expansion. The accompanying self-contained checker integrates the centered monomial moment densities for a nonconstant periodic curvature tail, calculates the exact \(L^1\) difference of successive moment laws and tests the predicted log-curvature-derivative coefficient at increasing degrees. The finite computations are diagnostics only and cannot replace the quantifier-uniform proof.

## Relationship to prior work
Bdarneh, *Toeplitz C*-algebras on radially weighted Fock spaces: commutativity and spectral representation* (arXiv:2609.20652v1, 2026), supplies the radial moment eigenvalue formula and investigates which eigenvalue sequences are uniformly continuous in the square-root index metric. The present result determines the **optimal operator norm of each individual adjacent-eigenvalue difference functional**, including the leading local Lipschitz coefficient, extremal radial symbols and complete curvature-dependent oscillatory phase. Integral representation alone does not establish this sharp asymptotic, and the source does not state the local total-variation coefficient.

Xu and Dong, *IDA symbols and Schatten--Lorentz theory for Toeplitz operators on weighted Fock spaces* (arXiv:2609.16970v1, 2026), considers singular-value Weyl coefficients for individual Toeplitz symbols and gives a nonquadratic radial obstruction. This result instead optimizes across **all** bounded radial symbols and controls the difference of two eigenvalue functionals. The metric normalization and the appearance of \(g'\) distinguish it from eigenvalue asymptotics for a fixed power-decay symbol.

A published logarithmic spectral filter study concerns oscillating symbols on Gaussian weight and a different averaging statistic.

## Limitations
The result concerns one complex variable, smooth radial uniformly convex weights with the specified bounded logarithmic derivatives, and adjacent monomial eigenvalues of bounded radial Toeplitz symbols. It does not give the global optimal modulus for arbitrary distant indices, nor a norm for nonradial Toeplitz symbols. Extremizing threshold symbols depend on the index \(k\); no *single* bounded symbol is claimed to attain every adjacent optimum. The displayed phase law requires eventual periodic curvature; the general local formula does not. The comparison with wider Laplace-asymptotic literature may leave residual publication-priority risk, and no independent audit has been performed.

## References
1. K. Bdarneh, *Toeplitz C*-algebras on radially weighted Fock spaces: commutativity and spectral representation*, arXiv:2609.20652v1, publicly posted 2026-09-17, https://arxiv.org/abs/2609.20652, especially Sections 6 and 9.
2. C. Xu and J. Dong, *IDA symbols and Schatten--Lorentz theory for Toeplitz operators on weighted Fock spaces*, arXiv:2609.16970v1, publicly posted 2026-09-15, https://arxiv.org/abs/2609.16970, especially Section 5.
3. *The logarithmic spectral filter for smooth radial Fock Toeplitz operators*, public mathematical finding, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-logarithmic-spectral-filter-for-smooth-radial-fock-toeplitz--0bc5b54dc8b5.
