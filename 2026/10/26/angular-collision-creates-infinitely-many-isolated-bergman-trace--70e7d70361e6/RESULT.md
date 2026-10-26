# Angular collision creates infinitely many isolated Bergman trace eigenvalues

## Finding
For each real \(\alpha>-1\), set \(\lambda=\alpha+2\) and let \(A^2_\alpha(\mathbb D)\) be the analytic Hilbert space with norm
\[
\|f\|_\alpha^2=\frac{\alpha+1}{\pi}\int_{\mathbb D}|f(z)|^2(1-|z|^2)^\alpha\,dA(z).
\]
For \(0\le\theta<\pi\), define the bounded, positive self-adjoint operator \(T_{\alpha,\theta}\) by its quadratic form
\[
\langle T_{\alpha,\theta}f,f\rangle
=\int_{-1}^{1}(1-x^2)^{\alpha+1}
\bigl(|f(x)|^2+|f(e^{i\theta}x)|^2\bigr)\,dx.
\]
Set
\[
C_\alpha=\frac{2^{\alpha+1}\Gamma((\alpha+2)/2)^2}{\Gamma(\alpha+2)},
\qquad D_\alpha=2B(1/2,\alpha+2).
\]
Then \(C_\alpha<D_\alpha<2C_\alpha\). For **every** \(0<\theta<\pi\), the Fredholm essential spectrum is exactly
\[
\sigma_{\mathrm{ess}}(T_{\alpha,\theta})=[0,C_\alpha],
\]
and the operator has an **isolated eigenvalue of finite multiplicity** greater than or equal to \(D_\alpha>C_\alpha\). More strongly, for every \(\mu\) strictly between \(C_\alpha\) and \(2C_\alpha\), the number \(N_{\alpha,\theta}(\mu)\) of eigenvalues strictly above \(\mu\), counting multiplicity, is finite for each fixed nonzero \(\theta\), but satisfies
\[
\lim_{\theta\downarrow0}N_{\alpha,\theta}(\mu)=+\infty.
\]
At the collision angle \(\theta=0\), the essential spectrum is \([0,2C_\alpha]\). Moreover,
\[
\lim_{\theta\downarrow0}\|T_{\alpha,\theta}\|=2C_\alpha,
\qquad \|T_{\alpha,\theta}\|_{\mathrm{ess}}=C_\alpha
\quad(0<\theta<\pi).
\]
Thus the essential spectral edge jumps at angular coincidence while the operator norm converges, and an unbounded finite family of isolated eigenvalues fills the emergent interval from below.

## Assumptions and scope
The area measure \(dA\) is ordinary planar Lebesgue measure and the weighted Bergman measure above is probability-normalized. The chord measure is ordinary \(dx\), not normalized length and not the endpoint weight \((1-|x|)^{\alpha+1}\). Both trace paths are full diameters: distinct exactly when \(0<\theta<\pi\). All limits fix \(\alpha>-1\), and the eigenvalue-count limit fixes \(C_\alpha<\mu<2C_\alpha\). The essential spectrum uses the Fredholm definition; every eigenvalue counted above \(\mu>C_\alpha\) is isolated with finite multiplicity. No uniform rate in \(\theta\) or formula for individual eigenvalues is asserted.

## Proof
**1. Exact one-diameter model.** Let \(R_{\alpha,0}:A^2_\alpha(\mathbb D)\to L^2(-1,1;dx)\) send \(f\) to \((1-x^2)^{(\alpha+1)/2}f(x)\), initially on analytic polynomials. The Bergman kernel for our normalization is \(K_\alpha(z,w)=(1-z\overline w)^{-\lambda}\). Consequently, \(R_{\alpha,0}R_{\alpha,0}^*\) has integral kernel
\[
(1-x^2)^{(\lambda-1)/2}(1-y^2)^{(\lambda-1)/2}(1-xy)^{-\lambda}.
\]
Under the unitary coordinate change \(x=\tanh u\), \(h(x)\mapsto\operatorname{sech}u\,h(\tanh u)\), this kernel becomes precisely \(\operatorname{sech}^{\lambda}(u-v)\). The Fourier transform therefore diagonalizes the one-diameter operator, with multiplier
\[
m_\alpha(\xi)=\frac{2^{\lambda-1}}{\Gamma(\lambda)}
\left|\Gamma\left(\frac\lambda2+\frac{i\xi}2\right)\right|^2.
\]
It is strictly positive, continuous, tends to zero at infinity, and its maximum is \(m_\alpha(0)=C_\alpha\), since its convolution kernel is strictly positive. Thus the one-diameter operator \(Q_\alpha=R_{\alpha,0}^*R_{\alpha,0}\) is bounded, positive, with spectrum and Fredholm essential spectrum both \([0,C_\alpha]\). Indeed \(R_{\alpha,0}\) is injective by analyticity; its range is dense because polynomials are dense in \(L^2(-1,1)\) after the strictly positive interior weight; polar decomposition identifies \(R_{\alpha,0}^*R_{\alpha,0}\) with \(R_{\alpha,0}R_{\alpha,0}^*\). The multiplier has no point masses, so its positive-top spectral subspaces \(\mathbf1_{(c,C_\alpha]}(Q_\alpha)A^2_\alpha\) are infinite-dimensional for every \(c<C_\alpha\).

**2. Two distinct diameters are orthogonal modulo compacts.** Define \(R_{\alpha,\theta}f(x)=(1-x^2)^{(\alpha+1)/2}f(e^{i\theta}x)\) and \(Q_{\alpha,\theta}=R_{\alpha,\theta}^*R_{\alpha,\theta}\). This is a unitary rotation of \(Q_\alpha\). For \(0<\theta<\pi\), the cross operator \(R_{\alpha,0}R_{\alpha,\theta}^*\) is Hilbert–Schmidt, because its integral kernel is
\[
\frac{(1-x^2)^{(\alpha+1)/2}(1-y^2)^{(\alpha+1)/2}}
{(1-xy e^{-i\theta})^{\lambda}},
\]
and \(\inf_{x,y\in[-1,1]}|1-xy e^{-i\theta}|>0\), while the squared endpoint weights are integrable. Therefore \(Q_\alpha Q_{\alpha,\theta}=R_{\alpha,0}^*(R_{\alpha,0}R_{\alpha,\theta}^*)R_{\alpha,\theta}\) is compact. In the Calkin algebra these are commuting positive elements with zero product; the spectrum of their sum is the union of their spectra (including zero). Each has essential spectrum \([0,C_\alpha]\); hence the essential spectrum of \(T_{\alpha,\theta}=Q_\alpha+Q_{\alpha,\theta}\) equals \([0,C_\alpha]\).

**3. A uniform isolated eigenvalue.** The constant function has Bergman norm one. Its Rayleigh quotient for the sum is \(D_\alpha=2B(1/2,\alpha+2)\), independent of \(\theta\). To show \(D_\alpha>C_\alpha\), write \(\lambda=\alpha+2>1\) and \(I_\lambda=\int_{\mathbb R}\operatorname{sech}^{\lambda}u\,du\). The first step gives \(C_\alpha=I_\lambda\), whereas \(D_\alpha=2I_{2\lambda}\) after \(x=\tanh u\). For all nonzero real \(u\), \(\cosh(2u)=2\cosh^2u-1>\cosh^2u\), so \(\operatorname{sech}^{2\lambda}u>\operatorname{sech}^{\lambda}(2u)\). Integration gives \(D_\alpha=2I_{2\lambda}>I_\lambda=C_\alpha\). Conversely \(I_{2\lambda}<I_\lambda\), so \(D_\alpha<2C_\alpha\). The variational principle and the strict essential-spectrum bound force the spectral top to be a finite-multiplicity isolated eigenvalue at least \(D_\alpha\).

**4. Angular collision and eigenvalue proliferation.** Let \(U_\theta f(z)=f(e^{i\theta}z)\), a strongly continuous unitary family. Then \(Q_{\alpha,\theta}\) is a unitary conjugate of \(Q_\alpha\) and \(T_{\alpha,\theta}\to2Q_\alpha\) strongly as \(\theta\downarrow0\). The uniform upper bound \(\|T_{\alpha,\theta}\|\le2C_\alpha\) and the lower semicontinuity of the norm under strong convergence yield \(\|T_{\alpha,\theta}\|\to2C_\alpha\). For fixed \(\mu\in(C_\alpha,2C_\alpha)\), choose \(c\) with \(\mu/2<c<C_\alpha\). The spectral subspace of \(Q_\alpha\) above \(c\) has infinite dimension. For any integer \(N\), select an \(N\)-dimensional subspace \(E_N\) inside it; then \(\langle2Q_\alpha f,f\rangle\ge2c\|f\|^2>\mu\|f\|^2\) on \(E_N\). Strong convergence is uniform on the unit sphere of \(E_N\), so the same strict inequality holds for \(T_{\alpha,\theta}\) whenever \(\theta>0\) is sufficiently small. The min–max principle then gives at least \(N\) eigenvalues above \(\mu\), since its essential spectral edge remains \(C_\alpha\). As \(N\) was arbitrary, \(N_{\alpha,\theta}(\mu)\to\infty\). At \(\theta=0\), the operator is exactly \(2Q_\alpha\), with essential spectrum \([0,2C_\alpha]\).

## Verification
The Fourier-transform identity follows by setting \(t=e^{2u}\) in the integral of \(\operatorname{sech}^\lambda(u)e^{-i\xi u}\), which becomes an Euler beta integral. The cross-kernel Hilbert–Schmidt bound uses the squared weight \((1-x^2)^{\alpha+1}\), integrable exactly within the given \(\alpha>-1\) regime. The inequalities \(C_\alpha<D_\alpha<2C_\alpha\) have a pointwise integration proof, not numerical-only evidence. For numerical diagnostics, \(\alpha=0\) gives \(C_0=2\) and \(D_0=8/3\), and \(\alpha=1\) gives \(C_1=\pi/2\), \(D_1=32/15\). The accompanying program checks the coefficient formula and several beta/gamma identities; the infinite-dimensional statement follows from the proof, not the diagnostics.

## Relationship to prior work
Dawson, Ólafsson and Quiroga-Barranco (2018), Section 4.3, develop the hyperbolic restriction principle and the \(\cosh\)-kernel Fourier transform; their dimension-one single-orbit case contains the one-diameter spectral model in Step 1. It is **prior input**, not a claimed discovery. Halder and Kumar (2026) study Gabriel/Frazer inequalities, including pairs of diameter traces, but their results are inequality statements, not the angle-dependent essential-spectrum jump, isolated spectral branch and unbounded eigenvalue proliferation proved here. Kasuga (2025) surveys a related endpoint-weighted one-ray inequality with weight \((1-x)^{\alpha+1}\), a distinct weight/geometry. General Weyl and min–max principles are standard and are used only to turn the compact cross-interaction into the specific geometric spectral collision theorem.

## Limitations
The result determines the essential spectrum and a uniform isolated-eigenvalue lower bound, but not every discrete eigenvalue, its multiplicity, or the exact norm at nonzero angle. It supplies no rate for growth of the eigenvalue count as the angle collapses. The cross-compactness proof excludes coinciding diameter directions, which are handled separately by exact doubling. Earlier specialized spectral literature not located by the present searches may contain an equivalent two-diameter result; independent audit remains unperformed.

## References
1. Dawson, Ólafsson and Quiroga-Barranco, *The restriction principle and commuting families of Toeplitz operators on the unit ball*, arXiv:1805.00141 (2018), especially §4.3.
2. Halder and Kumar, *Gabriel's and Frazer's problems for weighted Bergman spaces and their applications*, arXiv:2607.13543 (first posted 2026-07-15).
3. Halder and Kumar, *Fejér–Riesz inequalities for harmonic Bergman spaces*, arXiv:2607.11795 (first posted 2026-07-13).
4. Kasuga, *Fejér–Riesz type inequalities for weighted Bergman spaces*, Far East Journal of Mathematical Sciences 142 (2025), 237–242, doi:10.17654/0972087125014.
