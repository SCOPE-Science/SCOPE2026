# Geometry and observation cadence in first passage with stable diffusivity bursts

## Finding

For Brownian motion in an absorbing planar wedge, let the diffusivity be redrawn independently at fixed physical-time intervals from a **positive stable distribution**. Its survival tail has an explicit geometry-dependent exponent and amplitude. With \(p=\pi/(2\theta)\), stable index \(0<\alpha<1\), and wedge opening \(0<\theta<2\pi\), the continuous-boundary survival law is
\[
\Pr(T_c>t)\sim K\,t^{-p/\alpha},
\qquad
K=\frac4\pi\frac{\Gamma(1+p/\alpha)}{\Gamma(1+2p)}
\left(\frac{r^2}{4D}\right)^p
\sin\!\left(\frac{\pi\phi}{\theta}\right)
\sigma^{-p/\alpha}\tau^{p/\alpha-p}.
\]
Consequently \(\mathbb E[T_c^q]<\infty\) **exactly when** \(0<q<p/\alpha\). In particular the mean changes from infinite to finite precisely at \(\alpha=p\) when \(p<1\); if \(p\ge1\), it is finite for every allowed \(\alpha\). At the boundary \(q=p/\alpha\), the truncated \(q\)-moment diverges logarithmically.

For stable index \(\alpha=1/2\), the full, finite-time survival distributions in the half-plane and quadrant simplify to arctangent formulas (below). At positive refresh times their right-hand temporal slope is singular of square-root type. Moreover, **the same freely evolving process has infinite mean first detection time if the boundary is inspected only at the refresh times**, even in regimes where continuous monitoring gives a finite mean. Thus geometry and sensing cadence can reverse the qualitative conclusion drawn from an unqualified mean-first-passage observable.

## Assumptions and scope

Fix \(D,\sigma,\tau,r>0\), \(0<\alpha<1\), \(0<\theta<2\pi\), and a starting angle \(0<\phi<\theta\). Let \(W_\theta=\{(\rho\cos\psi,\rho\sin\psi):\rho>0,\ 0<\psi<\theta\}\), with both rays absorbing. Let \(\Lambda_0,\Lambda_1,\ldots\) be independent, almost surely positive and finite random variables satisfying
\[
\mathbb E[e^{-s\Lambda_j}]=\exp(-\sigma s^\alpha),\qquad s\ge0.
\]
They are independent of the standard planar Brownian motion \(B\). Define the continuous physical-space process with initial state \(z=(r\cos\phi,r\sin\phi)\) by
\[
X_t=z+\int_0^t \sqrt{2D\Lambda_{\lfloor u/\tau\rfloor}}\,dB_u,
\qquad T_c=\inf\{t\ge0:X_t\notin W_\theta\}.
\]
Each rate is fixed on the half-open interval \([j\tau,(j+1)\tau)\), and the process is not spatially reset when the rate changes. Continuous monitoring means absorption upon the *first pathwise crossing*. The process used for stroboscopic sensing remains freely evolving, without absorption, between observation times; the sensor records the first nonpositive position at a refresh epoch. Diffusion normalization is \(D\Delta\), rather than \(\tfrac12D\Delta\).

Write \(t=n\tau+u\) for integer \(n\ge0\) and \(0\le u<\tau\). Define
\[
a(t)=[\sigma(n\tau^\alpha+u^\alpha)]^{1/\alpha}.
\]
For every \(t>0\), if \(Z_\alpha\) is the standard positive stable variable with \(\mathbb E[e^{-sZ_\alpha}]=e^{-s^\alpha}\), the operational time is distributed as \(a(t)Z_\alpha\). The statement is at a fixed starting point strictly inside the wedge, not uniformly in \(r\) or in a moving boundary.

## Proof

**1. Exact random clock.** Set \(A_t=\int_0^t\Lambda_{\lfloor u/\tau\rfloor}\,du=\tau\sum_{j=0}^{n-1}\Lambda_j+u\Lambda_n\). Independence gives, for all \(s\ge0\),
\[
\mathbb E[e^{-sA_t}]=\exp\{-\sigma(n\tau^\alpha+u^\alpha)s^\alpha\}.
\]
Conditional on the clock path, \(X\) is Brownian motion with generator \(D\Delta\) evaluated at the continuous, strictly increasing time \(A_t\). Consequently, with \(S_B(v)\) the passive Brownian wedge survival probability from \((r,\phi)\),
\[
\Pr(T_c>t)=\mathbb E[S_B(A_t)]=\mathbb E[S_B(a(t)Z_\alpha)].
\]
This equality uses first *continuous* exit, so replacing it by a survival probability at the endpoint alone would be incorrect.

**2. Passive wedge asymptotic and coefficient.** Separation of variables for the Dirichlet heat kernel on the wedge yields angular modes \(\sin(k\pi\psi/\theta)\) and radial modified Bessel factors \(I_{k\pi/\theta}\). Integrating the first mode against area and using \(I_\nu(x)\sim (x/2)^\nu/\Gamma(1+\nu)\) at small argument gives
\[
S_B(v)\sim C_{\theta,z,D}v^{-p},\qquad
C_{\theta,z,D}=\frac4\pi\frac{\Gamma(1+p)}{\Gamma(1+2p)}
\left(\frac{r^2}{4D}\right)^p\sin\left(\frac{\pi\phi}{\theta}\right),
\quad p=\frac\pi{2\theta}.
\]
Indeed the first radial integral equals \(\tfrac12(4Dv)^{1+p}\Gamma(1+p)\) after extracting the Bessel leading factor. Every higher angular mode has strictly larger decay exponent. The heat-kernel expansion and positivity also imply a finite constant \(C_0\) such that \(0\le S_B(v)\le C_0v^{-p}\) for all \(v>0\) (enlarge the constant on compact times, where \(S_B\le1\)). The coefficient checks in the right-angle quadrant and half-plane are \(xy/(\pi D)\) and \(y/\sqrt{\pi D}\), respectively.

**3. Stable negative moments and the sharp tail.** The Mellin integral of the Laplace transform gives, for every \(p>0\),
\[
\mathbb E[Z_\alpha^{-p}]
=\frac1{\Gamma(p)}\int_0^\infty s^{p-1}e^{-s^\alpha}\,ds
=\frac{\Gamma(1+p/\alpha)}{\Gamma(1+p)}.
\]
Dominated convergence applies to \(a(t)^pS_B(a(t)Z_\alpha)\), dominated by \(C_0Z_\alpha^{-p}\), and gives \(a(t)^p\Pr(T_c>t)\to C_{\theta,z,D}\mathbb E[Z_\alpha^{-p}]\). Since \(a(t)\sim\sigma^{1/\alpha}\tau^{1-1/\alpha}t^{1/\alpha}\), this is exactly the positive constant \(K\) stated above. Finally \(\mathbb E[T_c^q]=q\int_0^\infty t^{q-1}\Pr(T_c>t)\,dt\), proving both moment directions, including divergence at equality. At equality the *truncated \(q\)-moment* \(\mathbb E[(T_c\wedge t)^q]\sim qK\log t\); all logarithms of dimensional time may equivalently use \(\log(t/\tau)\), changing only bounded terms. Almost-sure finite absorption follows from \(A_t\to\infty\) and ordinary wedge exit.

**4. Exact \(\alpha=1/2\) laws.** At this index put
\[
h(t)=\sigma[n\sqrt\tau+\sqrt u],\qquad A_t\stackrel d=h(t)^2Z_{1/2}.
\]
The reciprocal \(U=(4Z_{1/2})^{-1}\) has the Gamma distribution of shape \(1/2\) and unit rate. Conditional passive survival equals \(\operatorname{erf}(y/(2\sqrt{DA_t}))\) in a half-plane and the product of analogous error functions in a right-angle quadrant. Thus, for \(t>0\),
\[
\boxed{\displaystyle S_{\rm half}(t)=\frac2\pi\arctan\left(\frac{y}{\sqrt D\,h(t)}\right)}
\]
and, for Cartesian \(x,y>0\),
\[
\boxed{\displaystyle S_{\rm quad}(t)=\frac2\pi\arctan\left(\frac{xy}{\sqrt{Dh(t)^2[Dh(t)^2+x^2+y^2]}}\right).}
\]
At \(t=0\) both are \(1\) by continuity. To prove both identities without simulation, note that \(\sqrt{2U}\) has the law of the absolute value of a standard normal variable. Hence averaging one or two error functions computes the Cauchy-ratio probability \(\Pr(|N_1/G|\le b)\) or its two-dimensional counterpart \(\Pr(|N_1/G|\le b,|N_2/G|\le c)\) for independent standard normals. The bivariate Cauchy density \((2\pi)^{-1}(1+v^2+w^2)^{-3/2}\) integrates over the rectangle to \((2/\pi)\arctan(bc/\sqrt{1+b^2+c^2})\).

At a refresh instant \(t_0=n\tau\), integer \(n\ge1\), let \(b=y/(\sigma\sqrt D)\) and \(N=n\sqrt\tau\). Expanding the half-plane arctangent gives the **right cusp**
\[
S_{\rm half}(t_0+u)-S_{\rm half}(t_0)
=-\frac{2b}{\pi(N^2+b^2)}\sqrt u+O(u),\quad u\downarrow0.
\]
The derivative from the left is finite. At large times,
\[
S_{\rm half}(t)=\frac{2y\sqrt\tau}{\pi\sigma\sqrt D}\,t^{-1}+O(t^{-2}),\quad
S_{\rm quad}(t)=\frac{2xy\tau}{\pi D\sigma^2}\,t^{-2}+O(t^{-3}),
\]
so the half-plane truncated mean is \(\frac{2y\sqrt\tau}{\pi\sigma\sqrt D}\log(t/\tau)+O(1)\) while the quadrant mean is finite.

**5. Sparse observation removes the finite-mean advantage.** On the freely evolving half-plane coordinate (without killing on between-sample crossings), set \(T_s=\tau\min\{j\ge1:Y_{j\tau}\le0\}\) with \(Y_0=y>0\). Block increments are independent, identically distributed and continuously symmetric; their characteristic function is exactly
\[
\mathbb E[e^{i\xi(Y_{(j+1)\tau}-Y_{j\tau})}]
=\exp[-\sigma(D\tau\xi^2)^\alpha].
\]
Let \(V_k=Y_{k\tau}-y\). The classical Sparre Andersen identity for iid symmetric continuous increments gives \(\Pr(V_1>0,\ldots,V_n>0)=\binom{2n}{n}4^{-n}\). This event implies \(Y_{k\tau}>0\) for all \(k\le n\), hence
\[
\Pr(T_s>n\tau)\ge\binom{2n}{n}4^{-n}\sim(\pi n)^{-1/2}.
\]
Therefore \(\mathbb E T_s=\infty\) for every \(0<\alpha<1\), whereas the continuously monitored mean is finite for \(0<\alpha<1/2\). This is a **lower bound** for positive \(y\), not an asserted exact equality for its survival law. The continuous and sampled experiments use identical motion but different detection protocols.

## Verification

The included `verify.py` independently integrates one- and two-error-function mixtures against a Gamma density and compares them to the two exact arctangent formulas; checks the passive half-plane and quadrant wedge prefactors; checks tail normalizations at multiple parameter sets; and verifies the positive Sparre Andersen lower bound against its asymptotic. Run `python verify.py` with Python 3.10+ and SciPy. The bounded numerical tests are diagnostic only. The unbounded moment claims follow from the analytical heat-kernel, stable Mellin and renewal arguments.

## Relationship to prior work

Levit and Reuveni (2026) established a first-passage mean transition for a **one-dimensional lattice walk with resampled Mittag–Leffler jump rates**. The half-line exponent \(1/(2\alpha)\) is anticipated by that result, and no priority is claimed for that exponent or for the qualitative fact of rate-induced regularization. The present process is continuous Brownian motion with positive-stable *diffusion coefficients*; the assessed claim is the **arbitrary-wedge angular threshold and sharp gamma amplitude, the exact critical-index arctangent half-plane/quadrant laws with time cusps, and the continuous-versus-sampled sensing contrast**.

Chupeau, Bénichou and Majumdar (2015) treat passive Brownian wedge exit without random diffusivity. Uchida, Miyoshi and Washizu (2025) analyze Brownian diffusion with stochastic diffusion coefficients, proving infinite means for an ergodic finite-mean class, which does not include the present iid positive-stable draws with infinite first moment. Najeeb, Pal and Prasad (2025) treat spatial stochastic resetting in a wedge, a different physical clock. Sparre Andersen's persistence identity is an explicit prior ingredient, not a new result. Grebenkov (2019) already establishes the general integrated-diffusivity transform framework for first passage and may imply the mixture representation; that framework is likewise **not** claimed as new. The particular stable-rate wedge amplitude, arctangent special-index results, and sampling contrast are the assessed combination. These comparisons do not prove worldwide uniqueness.

## Limitations

The law is for exact independent positive-stable refreshes, an idealized distribution with infinite mean. Correlated rates, finite cutoffs, anisotropic diffusivity, a moving or partially absorbing boundary, and switching based on the particle trajectory are not covered. The sensing statement concerns discrete inspection of an **unkilled** path; it is not a statement about the first exit of a process physically absorbed at the boundary. The arctangent formulas are restricted to index \(1/2\), and a half-plane or right-angle quadrant. Arbitrary-wedge formulas are asymptotic, not exact at finite time. Full technical inspection of some potentially relevant older primary papers, particularly Grebenkov (2019), could not be completed. A broad theorem could already imply parts of the time-change claim, leaving a publication-priority risk. No independent scientific audit has been performed.

## References

1. B. Levit and S. Reuveni, *First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean*, arXiv:2609.26925v1 (first public 2026-09-22), https://arxiv.org/abs/2609.26925.
2. M. Chupeau, O. Bénichou and S. N. Majumdar, *Survival probability of a Brownian motion in a planar wedge of arbitrary angle*, arXiv:1501.02274 (2015), https://arxiv.org/abs/1501.02274.
3. G. Uchida, H. Miyoshi and H. Washizu, *First passage time properties of diffusion with a broad class of stochastic diffusion coefficients*, arXiv:2502.20705 (first public 2025-02-28), https://arxiv.org/abs/2502.20705.
4. F. Najeeb, A. Pal and V. V. Prasad, *Diffusion in a wedge geometry: First-Passage Statistics under Stochastic Resetting*, arXiv:2505.04208 (2025), https://arxiv.org/abs/2505.04208.
5. D. S. Grebenkov, *A unifying approach to first-passage time distributions in diffusing diffusivity and switching diffusion models*, arXiv:1812.07249, J. Phys. A 52 (2019) 174001, https://arxiv.org/abs/1812.07249.
6. E. Sparre Andersen, *On the fluctuations of sums of random variables*, Math. Scand. 1 (1953), 263–285; Math. Scand. 2 (1954), 195–223 (persistence identity).
