# Sharp anisotropy bounds and a reentrant transverse regime for imperfect orientation resetting

## Finding
A planar active Brownian particle whose orientation is reset at independent Poisson times to an **arbitrary** distribution has an exact effective-diffusion tensor depending only on the first two angular Fourier moments of the reset law. Fix a prescribed mean reset direction \(\int e^{i\theta}\,\nu(d\theta)=a\), with \(0\le a\le1\) real, and write \(\Lambda=r/D_r\), \(p_1=\Lambda/(1+\Lambda)\), \(p_2=\Lambda/(4+\Lambda)\), \(k=r+D_r\). The longitudinal-minus-transverse diffusivity \(\Delta=D_x-D_y\) obeys the **sharp, complete interval**
\[
\frac{v^2}{k}\big[p_2(2a^2-1)-p_1^2a^2\big]\ \le\ \Delta\ \le\ \frac{v^2}{k}\big[p_2-p_1^2a^2\big].
\]
At \(a<1\), the lower equality holds **only** for equal-probability reset angles \(\theta=\pm\arccos a\); the upper equality holds **only** for angles \(0,\pi\) with probabilities \((1+a)/2,(1-a)/2\). Every intermediate value occurs. At \(a=1\), the two extremizers coincide at \(\theta=0\).

An exact rate-dependent **forced-transverse** regime follows. If \(\sqrt3/2<a<1\), then \(D_x<D_y\) for **every** resetting law with the prescribed mean direction exactly for
\[
\Lambda_-(a)<\Lambda<\Lambda_+(a),\qquad
\Lambda_\pm(a)=\frac{2a^2-1\pm a\sqrt{4a^2-3}}{1-a^2}.
\]
For rates outside the closed forbidden interval, an admissible reset law has \(D_x>D_y\). At the two boundary rates, the maximal difference is zero. For \(0\le a<\sqrt3/2\), there is no rate with universal strict transverse dominance. At \(a=\sqrt3/2\), the upper bound vanishes only at \(\Lambda=2\); at \(a=1\), it changes from positive to negative at \(\Lambda=1/2\). Thus moderate steering uncertainty permits **reentrant** longitudinal dominance as the resetting rate is increased.

## Assumptions and scope
Let \(D_r,r,v>0\), translational diffusivity \(D\ge0\), and independent standard Brownian motions \(B,W\). The angle on the circle follows \(d\theta_t=\sqrt{2D_r}\,dB_t\) between rate-\(r\) Poisson epochs. Each epoch replaces \(\theta\) by an independent fresh draw from \(\nu\), independent of all noises and previous draws. Position satisfies
\[
dX_t=v(\cos\theta_t,\sin\theta_t)\,dt+\sqrt{2D}\,dW_t.
\]
Initialize the angle at its unique stationary law. Set \(D_x=\lim_{t\to\infty}\mathrm{Var}(X_t^x)/(2t)\), and similarly for \(D_y\). The constrained class comprises **all** Borel probability laws on the circle with \(\int\cos\theta\,\nu(d\theta)=a\) and \(\int\sin\theta\,\nu(d\theta)=0\). The Cartesian axes are fixed by this polarization constraint; no symmetry of \(\nu\) is assumed.

## Proof
**1. Fourier balance.** For every integer \(n\ne0\), the stationary generator applied to \(e^{in\theta}\) gives
\[
0=-(D_rn^2+r)m_n+r\nu_n,\qquad
m_n=\frac r{r+D_rn^2}\nu_n,
\]
where \(m_n=\mathbb E[e^{in\theta_0}]\) and \(\nu_n=\int e^{in\theta}\nu(d\theta)\). Existence and uniqueness of the stationary angular law follow from its regeneration at positive-rate reset epochs.

**2. Exact diffusivity tensor.** For \(u(\theta)=(\cos\theta,\sin\theta)\), conditional first-harmonic relaxation gives
\[
\mathbb E[u(\theta_t)\mid\theta_0]
=e^{-kt}u(\theta_0)+(1-e^{-kt})\mathbb E[u(\theta_0)].
\]
Hence the lag covariance is \(\mathrm{Cov}(u(\theta_t),u(\theta_0))=e^{-kt}\mathrm{Cov}(u(\theta_0))\). Integrating this covariance in the stationary Green--Kubo identity gives
\[
\mathsf D_{\mathrm{eff}}=DI_2+\frac{v^2}{k}
\left[
\frac12\begin{pmatrix}1+p_2\Re\nu_2&p_2\Im\nu_2\\ p_2\Im\nu_2&1-p_2\Re\nu_2\end{pmatrix}
-p_1^2\begin{pmatrix}a^2&0\\0&0\end{pmatrix}
\right].
\]
The temporal covariance is integrable and establishes the stated limits for all Borel reset laws. Subtracting the two diagonal entries yields
\[
\Delta=\frac{v^2}{k}\big[p_2\Re\nu_2-p_1^2a^2\big].
\]

**3. Sharp optimization and uniqueness.** Since \(\cos2\theta=2\cos^2\theta-1\), Jensen's inequality and the pointwise bound \(\cos^2\theta\le1\) imply
\[
2a^2-1\le\Re\nu_2\le1.
\]
Equality on the left forces \(\cos\theta=a\) almost surely; for \(a<1\), the zero-sine constraint uniquely fixes equal masses at \(\pm\arccos a\). Equality on the right forces \(\cos\theta\in\{-1,1\}\) almost surely, and the first-moment constraint uniquely fixes masses at \(0,\pi\). Both laws are admissible. Mixing them preserves the first moment and fills the entire closed interval of differences. At \(a=1\) the first-moment constraint itself forces the point mass at zero.

**4. Universal sign classification.** The upper bound has the sign of
\[
F(\Lambda)-a^2,\qquad
F(\Lambda)=\frac{(1+\Lambda)^2}{\Lambda(4+\Lambda)}.
\]
Direct differentiation shows
\[
F'(\Lambda)=\frac{2(\Lambda-2)(\Lambda+1)}{\Lambda^2(\Lambda+4)^2}.
\]
Thus \(F\) decreases from infinity to \(F(2)=3/4\) and then increases to \(1\) from below. Solving \(F(\Lambda)=a^2\) gives precisely the two displayed roots for \(\sqrt3/2<a<1\), both positive and straddling \(2\). Consequently the maximum is negative strictly between these roots, and positive outside the closed interval. The single critical and deterministic-reset endpoint cases follow directly from this monotonicity. These comparisons are global because the upper bound is attained in the admissible class.

## Verification
The accompanying standalone script `verify_diffusion.py` checks stationary Fourier generator identities for random atomic laws, both extremal measures across 56 parameter pairs, intermediate convex mixtures, the reentrant sign intervals, and reduction at \(\nu=\delta_0\) to the two already published fixed-orientation formulas. It reports **PASS 412 independent numerical/algebraic tests**. These checks corroborate, but do not replace, the exact analytic proof; the proof uses no finite-enumeration assumption.

## Relationship to prior work
Baouche, Franosch, Meiners and Kurzthaler (arXiv:2405.06769v1, first available 2024-05-10) derive the fixed-orientation Poisson-reset diffusivities and specifically identify generalizing the reset-angle distribution as a physically relevant direction. Setting \(\nu=\delta_0\) above recovers their distinct longitudinal and transverse formulas. The present theorem instead optimizes the diffusivity **over all Borel reset-angle laws at fixed polarization** and proves unique optimal laws and the universal reentrant forbidden-rate window. Chaki, Olsen and Löwen (arXiv:2406.17550v1) study anisotropic **passive-particle** resetting, which is a different source of anisotropy. Olsen and Löwen (arXiv:2405.14326v1) consider strategic **relative reorientations** in chiral active motion, not the same fixed-laboratory-frame angular reset ensemble. Standard stationary Fourier-generator and Green--Kubo identities are mathematical ingredients, not claimed new in isolation.

## Limitations
The constrained mean-first-harmonic law is an exact model of steering fidelity, not a complete metric on angular calibration error. The theorem compares coordinatewise diffusion coefficients; for nonsymmetric laws, off-diagonal diffusion need not vanish and these coefficients need not be principal eigenvalues. No assertion is made about finite-sample measurement errors, time-dependent reset distributions, interactions, chirality, entropy production, or uniqueness of the result in the full literature. Prior results in broader moment-constrained stochastic control or harmonic response might subsume aspects of this calculation; independent priority assessment remains necessary.

## References
1. I. Baouche, T. Franosch, H. Meiners, C. Kurzthaler, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769v1 (first publicly submitted 2024-05-10), https://arxiv.org/html/2405.06769v1.
2. K. Olsen and H. Löwen, *Optimal diffusion of chiral active particles with strategic reorientations*, arXiv:2405.14326v1 (2024), https://arxiv.org/html/2405.14326v1.
3. A. Chaki, K. Olsen, H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550v1 (2024), https://arxiv.org/html/2406.17550v1.
4. S. Santra, U. Basu, S. Sabhapandit, *Active Brownian motion in two-dimensions under stochastic resetting*, arXiv:2008.03294 (2020), https://arxiv.org/abs/2008.03294.
