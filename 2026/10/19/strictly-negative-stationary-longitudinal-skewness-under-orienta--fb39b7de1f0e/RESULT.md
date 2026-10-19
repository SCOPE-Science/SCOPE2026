# Strictly negative stationary longitudinal skewness under orientation-only resetting in a harmonic trap

## Finding
For a two-dimensional active Brownian particle confined by a harmonic trap, whose **orientation alone** is reset at Poisson times to the positive horizontal direction, the longitudinal stationary third central moment is strictly negative at every positive resetting rate, angular diffusion, propulsion speed, and trap strength. In the time units where angular diffusivity equals one, this third central moment is
\[
\operatorname{cum}_3(X)=-\frac{4rv^3(37\beta r+13\beta+52r^2+191r+67)}{\beta(r+1)^3(r+4)(r+9)(\beta+r+1)(\beta+r+4)(2\beta+r+1)}<0.
\]
The expression is **independent of the translational Brownian diffusivity**, including its possible zero value. It remains strictly negative at the resetting-rate ratio \(r=1/2\), for which the centered second-order free-displacement covariance is isotropic for deterministic orientation resetting: disappearance of covariance anisotropy does not eliminate this one-point third-order asymmetry in a trap.

## Assumptions and scope
Let \(\theta\) take values on the circle and evolve as angular Brownian motion of generator \(\partial_\theta^2\), interrupted at independent rate \(r>0\) by jumps \(\theta\mapsto0\). Let \(\beta,v>0\) and \(D\ge0\). The horizontal position evolves continuously as
\[
 dX_t=(-\beta X_t+v\cos\theta_t)\,dt+\sqrt{2D}\,dW_t,
\]
with independent translational Brownian motion \(W\); **the position does not reset**. The vertical position has the analogous \(v\sin\theta\) forcing but does not enter the claim. The stationary process exists uniquely in distribution: the angular process has a unique regenerative invariant law; exponential filtering of the bounded propulsion, together with an independent stationary Ornstein–Uhlenbeck process for the thermal term, constructs the position component with moments of every order. The formula concerns \(\mathbb E[(X-\mathbb EX)^3]\) in this stationary law, not a finite-time displacement cumulant or a mean conditioned on resetting.

Physical units with angular diffusion coefficient \(D_{\mathrm{rot}}>0\) are recovered by rescaling time by \(D_{\mathrm{rot}}\) and putting \(r=\lambda/D_{\mathrm{rot}}\), \(\beta=\kappa/D_{\mathrm{rot}}\), \(v=v_{\mathrm{phys}}/D_{\mathrm{rot}}\), and \(D=D_{\mathrm{phys}}/D_{\mathrm{rot}}\). The claim covers every positive \(\lambda,\kappa,v_{\mathrm{phys}},D_{\mathrm{rot}}\) and nonnegative \(D_{\mathrm{phys}}\).

## Proof
For smooth polynomial-trigonometric test functions the stationary generator is
\[
 \mathcal L f=(-\beta x+v\cos\theta)\partial_x f+D\partial_x^2f+\partial_\theta^2f+r[f(x,0)-f(x,\theta)].
\]
Apply stationarity to \(\cos(n\theta)\), obtaining the exact angular harmonics \(a_n:=\mathbb E\cos(n\theta)=r/(r+n^2)\) for positive integers \(n\). Set \(m=\mathbb EX\), \(u=\mathbb E[X\cos\theta]\), \(q=\mathbb EX^2\), \(k=\mathbb E[X\cos2\theta]\), \(h=\mathbb E[X^2\cos\theta]\), and \(z=\mathbb EX^3\). Applying the same generator successively to \(x\), \(x\cos\theta\), \(x^2\), \(x\cos2\theta\), \(x^2\cos\theta\), and \(x^3\) gives the closed triangular system
\[
\begin{aligned}
\beta m&=va_1,\\
(\beta+r+1)u&=v(1+a_2)/2+rm,\\
\beta q&=vu+D,\\
(\beta+r+4)k&=v(a_1+a_3)/2+rm,\\
(2\beta+r+1)h&=v(m+k)+2Da_1+rq,\\
\beta z&=vh+2Dm.
\end{aligned}
\]
All denominators are positive. In particular, the term \(rq\) in the fifth equation arises because resetting \(\theta\) sends \(x^2\cos\theta\) to \(x^2\), while leaving \(x\) untouched. The Gaussian diffusion term \(2Da_1\) is essential for cancellation below.

Solving successively and substituting into \(\mathbb E[(X-m)^3]=z-3mq+2m^3\) gives, by rational-function expansion and collection, the displayed formula. To make this algebra reproducible without a symbolic black box, the six explicit rational recursions and the final factored expression are evaluated with exact fractions in the accompanying standalone program. Because the numerator \(37\beta r+13\beta+52r^2+191r+67\) and every denominator factor are strictly positive, the cumulant is strictly negative for every admissible \(r,\beta,v\). The terms containing \(D\) cancel identically, as also follows from the independent centered Gaussian Ornstein–Uhlenbeck summand in stationary \(X\): cumulants of order three add, and a Gaussian contributes zero.

## Verification
Run \(\texttt{python3 verify_skewness.py}\) alongside this file. The standalone standard-library program checked 300 combinations of exact positive rational \(\beta,r,v\) and nonnegative rational \(D\). Each test verifies all six generator identities, the closed-form third cumulant, strict negativity, and equality between arbitrary thermal \(D\) and \(D=0\). An independent symbolic rational simplification of these six generator recursions produces the same factored numerator and denominator. These tests are reproducibility aids: the universal inequalities follow from the exact stationary generator identities and factor positivity, not from finite enumeration.

## Relationship to prior work
Shee (arXiv:2409.06920v1, September 11, 2024) analyzed harmonic active Brownian motion when **both position and orientation reset together**; its conclusion specifically points to orientation-only resetting in a harmonic trap as a further protocol. Baouche, Franosch, Meiners, and Kurzthaler (arXiv:2405.06769v1, May 10, 2024) obtained free-space orientation-only-reset displacement statistics, including negative intermediate-time longitudinal skewness that disappears at long times; this earlier free skewness is not claimed as new. Kumar, Sadekar, and Basu (arXiv:2008.03294, August 7, 2020) analyzed free-space orientation-only resetting among other protocols. Chaudhuri and Dhar (arXiv:2005.14234, May 28, 2020) obtained exact harmonic active-particle moments without orientational resets. The present result concerns the stationary **position** of the jointly constrained model where the trap remains active and only orientation resets; free-displacement or full-reset formulas cannot be substituted directly for its invariant third central moment.

## Limitations
No claim is made that negative finite-time skewness was previously unknown; the new object is stationary harmonic confinement without position resetting. This formula concerns the third central moment and does not classify the full position density, higher cumulants, multitime irreversibility, or stability of parameter estimation. Independence from thermal diffusivity concerns the unstandardized third central moment, not standardized skewness (which depends on variance). The result uses deterministic directional angular resets, isotropic translational Brownian noise, Poisson resets, and harmonic confinement; changing these assumptions may alter the sign. General moment-recursion machinery is established, so the priority of the specific factored formula and all-parameter sign should still receive independent literature assessment.

## References
- A. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920v1 (first public 2024-09-11), https://arxiv.org/html/2409.06920v1.
- Y. Baouche, T. Franosch, M. Meiners, C. Kurzthaler, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769v1 (first public 2024-05-10), https://arxiv.org/html/2405.06769v1.
- V. Kumar, O. Sadekar, U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294 (first public 2020-08-07), https://arxiv.org/abs/2008.03294.
- D. Chaudhuri, A. Dhar, *Active Brownian particle in harmonic trap: exact computation of moments, and re-entrant transition*, arXiv:2005.14234 (first public 2020-05-28), https://arxiv.org/abs/2005.14234.
