# Oscillatory memory hidden by the stationary law of a cyclically reset Brownian particle

## Finding
Let \(a,D,r,\nu>0\). Define the planar triangle vertices \(v_j=a(\cos(2\pi j/3),\sin(2\pi j/3))\), \(j\in\{0,1,2\}\). A continuous-time Markov chain \(Y_t\) makes only the jumps \(j\to j+1\pmod3\), each at rate \(\nu\). Independently, a planar Brownian particle evolves with generator \(D\Delta\). At independent rate-\(r\) Poisson times its position is reset instantly to \(v_{Y_t}\), without changing \(Y_t\).

The process admits a unique invariant law. Under that law, with \(\kappa=\sqrt{r/D}\), the marginal planar position density away from the three reset sites is
\[
p_*(x)=\frac{r}{6\pi D}\sum_{j=0}^2 K_0(\kappa\lVert x-v_j\rVert),
\]
where \(K_0\) is the modified Bessel function. Thus **the stationary position law contains no information about \(\nu\)**, although its time correlations do.

Set \(\alpha=3\nu/2\), \(\beta=\sqrt3\nu/2\), and \(\lambda=\alpha-i\beta\). The stationary (mean-zero) dot-product autocovariance \(C(t)=\mathbb E[X_0\cdot X_t]\), for every \(t\ge0\), is
\[
\boxed{C(t)=\left(a^2+\frac{4D}{r}\right)e^{-rt}
+a^2r^2\operatorname{Re}\!\left(
\frac{e^{-\lambda t}-e^{-rt}}{r^2-\lambda^2}
\right).}
\]
In particular the covariance is negative on intervals extending to arbitrarily large lags **if and only if**
\[
\boxed{r>\frac{3\nu}{2}\quad\text{or}\quad
\left(r=\frac{3\nu}{2}\ \text{and}\ 0<D<D_c\right),
\qquad
D_c=\frac{3\nu a^2(3\sqrt{13}-10)}{104}>0.}
\]
If \(0<r<3\nu/2\), then \(C(t)>0\) for all sufficiently large \(t\). If \(r=3\nu/2\) and \(D>D_c\), it is strictly positive for every \(t\ge0\). At \(r=3\nu/2\), \(D=D_c\), it is everywhere nonnegative and vanishes at infinitely many positive lags (without becoming negative).

## Assumptions and scope
Rates \(r,\nu\), diffusivity \(D\), and radius \(a\) are strictly positive and do not vary with time. Between resets, \(dX_t=\sqrt{2D}\,dB_t\) with standard two-dimensional Brownian motion \(B_t\). The vertex chain and the reset clock are independent of the Brownian noise and each other. A reset changes \(X_t\) only; it does **not** restart or resample \(Y_t\). The scalar \(C(t)\) is the dot-product covariance of two planar position vectors, not the covariance of their norms. No conclusion is asserted for noncyclic switching or non-Poissonian reset clocks.

## Proof
**1. Existence, uniqueness, and the one-time law.** Construct stationary independent two-sided versions of the rate-\(r\) reset clock, the three-state chain \(Y\), and Brownian increments. Let \(T\) be the last reset before time zero, and \(A=-T\). The backward reset age \(A\) has density \(re^{-rA}\) on \((0,\infty)\), independently of \(Y\). Write
\[
X_0=v_{Y_{-A}}+\sqrt{2D}(B_0-B_{-A}).
\]
Since \(Y\) is stationary uniform, \(v_{Y_{-A}}\) is uniformly distributed over the three vertices, independently of \(A\). This yields the mixture of the three free Brownian resolvent kernels. The standard identity
\[
\int_0^\infty\frac{r e^{-ru}}{4\pi Du}
\exp\!\left(-\frac{\lVert x\rVert^2}{4Du}\right)du
=\frac{r}{2\pi D}K_0(\sqrt{r/D}\lVert x\rVert)
\]
proves the asserted formula. In particular \(\mathbb E[X_0]=0\) and \(\mathbb E\lVert X_0\rVert^2=a^2+4D/r\). Uniqueness follows because the irreducible finite chain loses its initial-state memory and the first subsequent reset removes dependence on the initial particle position; together with Brownian coupling this gives convergence to the constructed stationary law.

**2. Exact covariance.** On the plane the cyclic three-state chain has vertex autocorrelation
\[
\mathbb E[v_{Y_0}\cdot v_{Y_s}]
=a^2e^{-\alpha s}\cos(\beta s),\qquad
\alpha=3\nu/2,\quad\beta=\sqrt3\nu/2.
\]
Indeed the complex vertex function \(j\mapsto a e^{2\pi i j/3}\) is an eigenfunction of the directed-cycle generator with eigenvalue \(-\alpha+i\beta\). For \(s\ge0\), the independent backward exponential age gives
\[
\mathbb E[X_0\cdot v_{Y_s}]
=a^2\operatorname{Re}\left(\frac{r e^{-\lambda s}}{r+\lambda}\right),
\qquad\lambda=\alpha-i\beta.
\]
If no reset occurs during \((0,t)\), an event of probability \(e^{-rt}\), the covariance contribution is \(e^{-rt}(a^2+4D/r)\). Otherwise, if the last reset occurs at \(s\in(0,t)\), its unconditional density is \(r e^{-r(t-s)}ds\); after that reset the independent Brownian increment contributes zero to the cross-moment. Therefore
\[
C(t)=e^{-rt}\left(a^2+\frac{4D}{r}\right)
+a^2r^2\operatorname{Re}\left(
\frac1{r+\lambda}\int_0^t
 e^{-r(t-s)}e^{-\lambda s}\,ds\right).
\]
Integrating the exponential and using \((r+\lambda)(r-\lambda)=r^2-\lambda^2\) yields the displayed formula. The denominator never vanishes because \(\operatorname{Im}\lambda\ne0\).

**3. Sharp sign classification.** If \(r>\alpha\), the complex exponential \(e^{-\lambda t}\) decays more slowly than \(e^{-rt}\). Its coefficient \(a^2r^2/(r^2-\lambda^2)\) is nonzero, so \(C(t)\) has asymptotically a nonzero sinusoid times \(e^{-\alpha t}\). It therefore takes both signs on unbounded sets of positive lags.

If \(0<r<\alpha\), factor out \(e^{-rt}\). The limiting coefficient is
\[
A=a^2+\frac{4D}{r}-a^2r^2\operatorname{Re}\left(\frac1{r^2-\lambda^2}\right)
=\frac{4D}{r}+a^2\frac{\tfrac32\nu^2(6\nu^2-r^2)}
{(r^2-\tfrac32\nu^2)^2+\tfrac{27}{4}\nu^4}>0,
\]
because \(r^2<9\nu^2/4<6\nu^2\). Thus \(C(t)>0\) eventually.

At the boundary \(r=\alpha=3\nu/2\), the exact formula reduces to
\[
e^{rt}C(t)=\frac{10a^2}{13}+\frac{4D}{r}
+\frac{3a^2}{\sqrt{13}}\cos(\beta t+\phi),
\]
where \(\phi\) is a fixed real phase determined by the complex denominator; only the nonzero amplitude is needed for the sign classification. The constant offset is smaller than the oscillation amplitude precisely when
\[
D<\frac r4a^2\left(\frac3{\sqrt{13}}-\frac{10}{13}\right)
=\frac{3\nu a^2(3\sqrt{13}-10)}{104}.
\]
The strict, equal, and reverse inequalities give respectively infinitely many negative intervals, nonnegative oscillations touching zero infinitely often, and strict positivity for all lags. This proves the claim.

## Verification
The accompanying `verify.py` computes \(C(t)\) by three independently coded routes: the closed expression, direct Simpson integration of the Poisson last-reset-time formula, and fourth-order integration of the finite-state Markov-generator moment equations. It also checks the exact critical envelope, strict slow-mode positivity on representative parameters, and late sign reversals. Running `python verify.py` with Python 3 returned `PASS 601 independent and boundary checks; max numerical error 2.2147333966771043e-10`. These finite tests support—but do not replace—the analytic statements for all positive parameters and unbounded times.

## Relationship to prior work
Evans and Majumdar's 2011 resetting model establishes the renewal stationary law for a fixed reset point. Their subsequent work treats independent random reset positions; its stationary one-point mixture principle encompasses the marginal-density portion here, which is **not claimed as novel**. The distinction here is a correlated sequence of reset targets produced by an autonomous **directed cyclic Markov chain not reset by the particle's clock**. Its two-time covariance and the sharp transition to arbitrarily-late anticorrelation are the proposed addition. Rose, Touchette, Lesanovsky, and Garrahan analyze resetting to a single fixed full-system configuration; their uniform mode shift does not apply verbatim to the environment whose Markov state is preserved. Julián-Salgado, Dagdug, and Boyer treat two reset sites with fixed selection probabilities and first-passage optimization, rather than cyclically correlated sites and time covariance. The related switching-diffusion resetting model of Bressloff resets the internal diffusion state, unlike the protocol studied here.

## Limitations
The historical-priority assessment is based on inspected primary sources and search results, not exhaustive proof of absence from the literature. Some switching-diffusion specialist full text was not available for detailed comparison. The one-time law is a direct corollary of published renewal resetting theory and is contextual, not the novelty claim. The main novelty candidate is the exact correlation and its phase boundary. This theorem concerns a stylized nonreversible three-state target and does not assert universality of the threshold under other environments or resetting protocols.

## References
1. M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, arXiv:1102.2704 (first public 2011-02-14), https://arxiv.org/abs/1102.2704.
2. M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting*, arXiv:1107.4225 (2011), https://arxiv.org/abs/1107.4225.
3. D. C. Rose, H. Touchette, I. Lesanovsky, and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, arXiv:1806.01298 (2018), https://arxiv.org/abs/1806.01298.
4. P. Julián-Salgado, L. Dagdug, and D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897 (2023), https://arxiv.org/abs/2311.11897.
5. P. C. Bressloff, *Switching diffusions and stochastic resetting*, J. Phys. A 53 (2020), 275003, DOI: 10.1088/1751-8121/ab97e0.
