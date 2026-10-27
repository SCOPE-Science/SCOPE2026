# Two reentrant covariance-isotropy rates for a harmonically trapped resetting active Brownian particle

## Finding
Consider a planar active Brownian particle whose position and heading are simultaneously reset to the origin and the positive horizontal direction at independent Poisson rate \(r>0\). The particle experiences isotropic harmonic confinement with relaxation rate \(k>0\), propulsion speed \(v>0\), rotational diffusivity \(d>0\), and any isotropic translational diffusivity \(D\geq0\). Define the stationary centered covariance anisotropy
\[
\Delta(r)=\operatorname{Var}(X)-\operatorname{Var}(Y).
\]
Then
\[
\boxed{\Delta(r)=\frac{v^2r\,P_{k,d}(r)}{(r+2k)(r+k+d)(r+4d)(r+d)^2(r+k)^2}},
\]
where
\[
P_{k,d}(r)=r^4+(k-d)r^3-(2d^2+6dk)r^2-4dk(d+k)r+2d^2k^2.
\]
For **every** \(k,d>0\), this quartic has **exactly two distinct simple positive roots** \(r_-<r_+\), obeying \(0<r_-<d<r_+\). Thus the centered stationary positional covariance is isotropic precisely at those two reset rates. The variance along the reset direction is larger for \(0<r<r_-\) and for \(r>r_+\), while the perpendicular variance is larger for \(r_-<r<r_+\). Both covariance eigenvalues remain positive, and the mean position is displaced along the reset direction, so covariance isotropy is **not** rotational invariance of the stationary law.

The two rates are **independent of propulsion speed and of isotropic translational thermal noise**. Their singular confinement limits, at fixed \(d>0\), are
\[
\begin{aligned}
 k/d\downarrow0:&\quad r_-=(\sqrt2-1)k+o(k),\qquad r_+=2d+o(d),\\
 k/d\uparrow\infty:&\quad r_-=\tfrac12d+o(d),\qquad r_+=2\sqrt{kd}\,[1+o(1)].
\end{aligned}
\]
The finite-confinement double transition therefore collapses to a single positive reset-rate crossing in the free-particle limit \(k=0\).

## Assumptions and scope
Let \(B_t=(B_t^1,B_t^2)\) and \(W_t\) be independent standard Brownian motions. Between Poisson resets, let
\[
\begin{aligned}
 dX_t&=(-kX_t+v\cos\Theta_t)\,dt+\sqrt{2D}\,dB_t^1,\\
 dY_t&=(-kY_t+v\sin\Theta_t)\,dt+\sqrt{2D}\,dB_t^2,\\
 d\Theta_t&=\sqrt{2d}\,dW_t\pmod{2\pi}.
\end{aligned}
\]
At each reset, \((X_t,Y_t,\Theta_t)\mapsto(0,0,0)\). Quantifiers are \(k,d,v,r>0\), \(D\geq0\), and stationary observation time. Poisson resets are independent of all Brownian drivers, and the same reset clock acts on position and heading. No angular torque or anisotropic translational noise is present. The process has a unique stationary regenerative law with finite positional moments of every fixed order, because the reset rate is positive and the between-reset dynamics are stable.

The horizontal axis is the reset-heading axis, and the vertical axis is its perpendicular. Invariance under \((Y,\Theta)\mapsto(-Y,-\Theta)\) gives \(\mathbb EY=\operatorname{Cov}(X,Y)=0\); hence the covariance eigenvalues are exactly \(\operatorname{Var}(X)\) and \(\operatorname{Var}(Y)\).

## Proof
Write \(Z=X+iY\). Stationary expectations of the generator and the reset rule give the first two angular Fourier coefficients
\[
\mathbb Ee^{i\Theta}=\frac r{r+d},\qquad \mathbb Ee^{2i\Theta}=\frac r{r+4d}.
\]
Since a reset makes \(Z=0\), the generator applied to \(Z\), \(Ze^{i\Theta}\), and \(Z^2\) yields the triangular identities
\[
\begin{aligned}
(r+k)\mathbb EZ&=v\mathbb Ee^{i\Theta},\\
(r+k+d)\mathbb E(Ze^{i\Theta})&=v\mathbb Ee^{2i\Theta},\\
(r+2k)\mathbb EZ^2&=2v\mathbb E(Ze^{i\Theta}).
\end{aligned}
\]
Here the isotropic translation noise contributes zero to the quadratic variation of \(Z^2\), because the two Cartesian Brownian quadratic variations cancel. Consequently
\[
\mathbb EZ=\frac{vr}{(r+k)(r+d)},\qquad
\mathbb EZ^2=\frac{2v^2r}{(r+2k)(r+k+d)(r+4d)}.
\]
Both expressions are real. For completeness, applying the generator to \(\overline Z e^{i\Theta}\) and \(|Z|^2\) gives
\[
\mathbb E(\overline Z e^{i\Theta})=\frac{v}{r+k+d},\qquad
\mathbb E|Z|^2=\frac{2v^2/(r+k+d)+4D}{r+2k}.
\]
Thus each individual covariance eigenvalue is explicitly specified by
\[
\operatorname{Var}(X)=\frac{\mathbb E|Z|^2+\mathbb EZ^2}{2}-(\mathbb EZ)^2,
\qquad
\operatorname{Var}(Y)=\frac{\mathbb E|Z|^2-\mathbb EZ^2}{2}.
\]
Subtracting cancels \(\mathbb E|Z|^2\), and therefore all translational-noise terms:
\[
\Delta(r)=\mathbb EZ^2-(\mathbb EZ)^2
=\frac{2v^2r}{(r+2k)(r+k+d)(r+4d)}-\frac{v^2r^2}{(r+k)^2(r+d)^2}.
\]
Clearing positive denominators gives the displayed quartic \(P_{k,d}\). Its polynomial coefficients in descending powers of \(r\) have signs
\[
+\,,\ \operatorname{sign}(k-d)\,,\ -\,,\ -\,,\ +,
\]
with the zero cubic coefficient omitted when \(k=d\). There are exactly two sign changes, so Descartes' rule of signs permits at most two positive roots, counted with multiplicity. Meanwhile
\[
P_{k,d}(0)=2d^2k^2>0,\quad
P_{k,d}(d)=-d^2(2d^2+9dk+2k^2)<0,\quad
\lim_{r\to\infty}P_{k,d}(r)=+\infty.
\]
Continuity produces a positive root on either side of \(d\). Because there can be no others, both roots are simple and these three sign intervals are exhaustive. In particular \(\operatorname{Var}(Y)>\operatorname{Var}(X)\) at \(r=d\) for every admissible confinement rate. Positivity of \(v^2r\) and of the denominator determines the claimed variance ordering.

For the root asymptotics set \(b=k/d\) and \(x=r/d\). Dividing the polynomial by \(d^4\) produces
\[
F_b(x)=x^4+(b-1)x^3-(2+6b)x^2-4b(1+b)x+2b^2.
\]
As \(b\downarrow0\), \(F_b(by)/b^2\to 2-4y-2y^2\) and \(F_0(x)=x^2(x-2)(x+1)\). The positive rescaled small-root limit is \(\sqrt2-1\), while the large root tends to \(2\). As \(b\uparrow\infty\), \(F_b(x)/b^2\to2-4x\) at fixed \(x\), and \(F_b(\sqrt b\,y)/b^{5/2}\to y^3-4y\) at fixed positive \(y\). The small root tends to \(1/2\), and the large root grows like \(2\sqrt b\). All the displayed candidate roots are simple in their limiting equations; continuity and the already-proved two-positive-roots theorem identify the required branches. This completes the proof.

## Verification
The standalone script `verification.py` performs symbolic expansion, the negative-sign identity at \(r=d\), and the four singular-root scaling limits. It numerically finds both positive roots for seven independent pairs \((k,d)\), checks the covariance signs on all three intervals and invariance of the variance difference under changing \(D\), and independently computes stationary mean and coordinate variances from the *last-reset age integral*. That quadrature integrates the distinct Brownian-angle kernels
\[
\mathbb E[e^{i(\Theta_s-\Theta_t)}]=e^{-d|s-t|},\quad
\mathbb E[e^{i(\Theta_s+\Theta_t)}]=e^{-d(\max(s,t)+3\min(s,t))}
\]
against the harmonic motion kernel and the exponential stationary reset-age distribution. Six independent parameter comparisons had maximum absolute discrepancy below \(7\times10^{-5}\) with the exact generator formulas at the specified quadrature resolution.

For \(k=d=v=1\), the two crossings are \(r_-=0.20726989465919865\ldots\) and \(r_+=3.209153942946819\ldots\). At \(r=1\), the strict transverse-over-longitudinal difference is exactly \(\Delta(1)=-13/720\), regardless of \(D\). Numerical checks corroborate finite formulas, while root multiplicity and infinite-domain all-parameter statements follow from the analytic proof, not the finite tests.

## Relationship to prior work
Shee (arXiv:2409.06920, first publicly available 2024-09-11) established the same simultaneous position-and-heading reset model in a harmonic trap and supplied its mean displacement, total mean-square displacement, longitudinal second moment and longitudinal centered variance (in particular Eqs. (9), (14), (60), (63)). **Those underlying moments and the model itself are prior results.** They imply the raw scalar covariance entries after algebraic reconstruction. The contribution here is the global, exact **two-positive-root, three-sign-regime theorem** for centered anisotropy, including thermal invariance and the two singular confinement scaling laws; the inspected source does not state or classify these reentrant covariance-isotropy transitions.

Kumar, Sadekar and Basu (arXiv:2008.03294, 2020) established complete resetting for free active Brownian motion and explicitly derived the two coordinate variances in Appendix B. In the free limit \(k=0\), the polynomial becomes \(r^2(r-2d)(r+d)\), consistent with just one finite positive crossing; that free result cannot supply the second crossing generated by nonzero harmonic confinement. Baouche et al. (arXiv:2405.06769, 2024) treat orientation-only resetting without simultaneous spatial reset, and Ghosh and Mandal (arXiv:2501.05149, first submitted 2025) study intrinsically anisotropic active motion without this harmonic trapping problem. None of these distinct setups establishes the global two-root theorem for the present model. A derivation could nevertheless be obtainable from older general moment or covariance formulas; publication priority has not been independently established.

## Limitations
The statement is about **centered second moments**, not isotropy of the complete distribution or its higher cumulants. The stationary mean is nonzero for every finite positive \(r\), so even at each equality of variances the stationary law is directionally biased. The double-crossing assertion requires \(k,d,v>0\) and a common position-and-heading reset clock; the free case \(k=0\), a nonpropelling particle \(v=0\), anisotropic thermal diffusion, independent reset clocks, or angular torque need not obey it. The formula gives no finite-sample method for inferring the crossings under measurement error and no time-dependent covariance-classification theorem.

## References
1. A. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920 (first version 2024-09-11), https://arxiv.org/abs/2409.06920.
2. V. Kumar, O. Sadekar and U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294 (2020), https://arxiv.org/abs/2008.03294.
3. Y. Baouche, T. Franosch, M. Meiners and C. Kurzthaler, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769 (2024), https://arxiv.org/abs/2405.06769.
4. A. Ghosh and S. Mandal, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149 (first version 2025-01-09), https://arxiv.org/abs/2501.05149.
5. American Mathematical Society, MSC2020 class 82C31, *Stochastic methods applied to time-dependent statistical mechanics*, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=82C31.
