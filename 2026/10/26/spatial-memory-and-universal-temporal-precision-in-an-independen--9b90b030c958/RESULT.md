# Spatial memory and universal temporal precision in an independently reset Brownian gas

## Finding
For a stationary gas of independent Brownian particles that each reset to their own fixed spatial anchor, the long-time variance of the **time-averaged number of particles crossing a fixed boundary** splits exactly into an anchor-geometry contribution and a universal temporal-noise correction. This universality holds for *every* stationary point-process distribution of the anchors of fixed positive intensity, subject to a stated second-moment condition; the correction does not depend on pair correlations of the anchors.

Put \(\alpha=\sqrt{r/D}\). If \(\mathcal A\) is the random locally finite set of positive anchor distances, of intensity \(\rho>0\), write
\[
 m(\mathcal A)=\frac12\sum_{x\in\mathcal A}e^{-\alpha x},\qquad
 \overline Q_T=\frac1T\int_0^TQ_t\,dt.
\]
Here \(Q_t\) counts the particles with positive physical position at time \(t\). Provided \(\operatorname{Var}(m(\mathcal A))<\infty\), as \(T\to\infty\),
\[
 \boxed{\operatorname{Var}(\overline Q_T)=\operatorname{Var}(m(\mathcal A))+
 \frac{7\rho}{16r\alpha\,T}+O(T^{-2}).}
\]
The remainder constant may depend on the model parameters but *not* on additional anchor correlations.

Two exact spatial ensembles illustrate the distinction. For Poisson anchors of intensity \(\rho\),
\[
 \operatorname{Var}(m)=\frac{\rho}{8\alpha}.
\]
For a uniformly phase-shifted lattice \(\mathcal A=\{(n+U)/\rho:n=0,1,2,\ldots\}\), with \(U\) uniform on \([0,1)\), set \(\beta=\alpha/\rho\). Then
\[
 \boxed{\operatorname{Var}(m)=\frac{\coth(\beta/2)}{8\beta}-\frac1{4\beta^2},\quad
 0<\operatorname{Var}(m)<\frac1{8\beta}.}
\]
The lattice-to-Poisson ratio is \(\coth(\beta/2)-2/\beta\), strictly between zero and one. It tends to zero as \(\beta\downarrow0\), even though *both* spatial ensembles have the same first time-decaying term \(7/(16r\beta T)\). Remarkably, the lattice plateau tends to \(1/48\) in the dense-anchor limit while the Poisson plateau diverges like \(1/(8\beta)\).

## Assumptions and scope
Let \(D,r,\rho>0\). Take a stationary locally finite simple point process on the real line of intensity \(\rho\), and retain its atoms strictly to the left of the origin; write their positive distances as \(\mathcal A\). Independently for each anchor \(-x\), define a Brownian displacement \(Y^{(x)}\) with generator \(D\partial_y^2\) and independent Poisson resetting to displacement zero at rate \(r\). At observation time zero, initialize each displacement independently from its unique stationary density \(\pi(y)=\alpha e^{-\alpha |y|}/2\), conditional on the anchors. The anchor configuration remains fixed throughout the observation. This is **individual** resetting, not simultaneous resetting of all particles.

Define \(Q_t=\sum_{x\in\mathcal A}\mathbf1_{\{Y_t^{(x)}>x\}}\), counting the particles on the positive half-line. Campbell's theorem gives \(\mathbb E Q_t=\rho/(2\alpha)<\infty\), so the count is almost surely finite at each fixed time and its time integral is defined by monotone approximation. Assume additionally that \(m(\mathcal A)\) has finite second moment. Both examples satisfy this assumption. The stationary step profile is defined by fixed anchors plus stationary displacements; it is not a statement about irreversible first-passage counts.

## Proof
**1. Static decomposition.** For an anchored particle at distance \(x>0\), stationarity gives
\[
 p_x=\Pr(Y>x)=\tfrac12e^{-\alpha x}.
\]
Conditional on \(\mathcal A\), all displacement processes are independent and stationary; their conditional mean count is \(m(\mathcal A)=\sum_xp_x\). Consequently the law of total variance is the exact identity
\[
 \operatorname{Var}(\overline Q_T)=\operatorname{Var}(m(\mathcal A))+
 \mathbb E_{\mathcal A}\bigl[\operatorname{Var}(\overline Q_T\mid\mathcal A)\bigr].
\]

**2. Stationary single-anchor temporal covariance.** Put \(f_x(y)=\mathbf1_{\{y>x\}}\), and let \(P_s^{\rm free}\) be the Brownian semigroup with variance \(2Ds\). The reset semigroup has the representation
\[
 P_s f_x(y)=e^{-rs}P_s^{\rm free}f_x(y)
 +r\int_0^s e^{-ru}P_u^{\rm free}f_x(0)\,du.
\]
The second term is independent of \(y\). Therefore for stationary \(Y_0\sim\pi\),
\[
 c_x(s)=\operatorname{Cov}(f_x(Y_0),f_x(Y_s))
 =e^{-rs}\operatorname{Cov}_{\pi}
 \bigl(f_x(Y_0),P_s^{\rm free}f_x(Y_0)\bigr).
\]
Because both functions inside this last covariance are increasing functions of the same real random variable, the covariance is nonnegative; moreover \(0\le c_x(s)\le e^{-rs}p_x\). This bound proves absolute integrability and allows all subsequent Tonelli/Fubini operations.

**3. Exact Green--Kubo kernel.** The Brownian resolvent \(r\int_0^\infty e^{-rs}P_s^{\rm free}\,ds\) is convolution with a symmetric Laplace random variable \(Z\) having density \(\alpha e^{-\alpha|z|}/2\). Hence
\[
 \int_0^\infty c_x(s)\,ds
 =\frac1r\left[\Pr(Y>x,Y+Z>x)-p_x\Pr(Y+Z>x)\right],
\]
where \(Y,Z\) are independent centered Laplace variables of rate \(\alpha\). Elementary integration gives, for all \(x\ge0\),
\[
 \Pr(Y>x,Y+Z>x)=\frac38e^{-\alpha x},\qquad
 \Pr(Y+Z>x)=\frac14(\alpha x+2)e^{-\alpha x}.
\]
Thus
\[
 K_x:=\int_0^\infty c_x(s)\,ds
 =\frac{3e^{-\alpha x}-(\alpha x+2)e^{-2\alpha x}}{8r}.
\]
This integrand is nonnegative: it is the integral of a nonnegative covariance. Its exact spatial integral is
\[
 \int_0^\infty K_x\,dx
 =\frac1{8r\alpha}\left(3-\frac14-1\right)
 =\frac7{32r\alpha}.
\]

**4. Universality and rate.** Conditional independence implies the conditional count covariance is \(\sum_{x\in\mathcal A}c_x(s)\). The Campbell intensity formula, independent of all higher anchor correlations, gives
\[
 \mathbb E_{\mathcal A}\sum_{x\in\mathcal A}K_x
 =\rho\int_0^\infty K_x\,dx=\frac{7\rho}{32r\alpha}.
\]
For each stationary count process, the integrated time-average covariance identity gives
\[
 \mathbb E_{\mathcal A}\operatorname{Var}(\overline Q_T\mid\mathcal A)
 =\frac2{T^2}\int_0^T(T-s)\,
 \mathbb E_{\mathcal A}\sum_{x\in\mathcal A}c_x(s)\,ds.
\]
The bound \(c_x(s)\le p_xe^{-rs}\) also controls the error from replacing the finite-lag integral by the infinite integral: the weighted first lag moment is bounded by \(\rho/(2\alpha r^2)\), and the tail is exponentially small. The expansion follows with \(O(T^{-2})\) remainder and the stated coefficient.

**5. Exact spatial plateaus.** For Poisson anchors, the Poisson stochastic-integral variance is \(\rho\int_0^\infty p_x^2dx=\rho/(8\alpha)\). For shifted-lattice anchors, conditional on the uniform phase \(U\),
\[
 m(U)=\frac{e^{-\beta U}}{2(1-e^{-\beta})},\quad
 \mathbb E_U m=\frac1{2\beta},\quad
 \mathbb E_U m^2=\frac{\coth(\beta/2)}{8\beta}.
\]
Subtracting the square of the mean gives the formula. The strict upper comparison follows from \(\coth(\beta/2)<1+2/\beta\) for positive \(\beta\), equivalently \(2/(e^\beta-1)<2/\beta\). The small-\(\beta\) expansion \(\coth(\beta/2)=2/\beta+\beta/6+O(\beta^3)\) gives the finite \(1/48\) limit. This completes the proof.

## Verification
The standalone Python standard-library checker `check_hyperuniform.py` checks the exact rational Green--Kubo prefactor, independently integrates the single-anchor kernel for three parameter choices, quadratures the lattice phase variance for seven spacings, validates the strict plateau comparison, tests the Laplace-convolution probabilities by independently seeded Monte Carlo, and checks the dense-spacing limit. It prints 25 passing assertions and exact rational coefficients. Its finite numerical checks are supplemental; the infinite-particle claim is established by the preceding analytic proof.

## Relationship to prior work
Di Bello, Hartmann, Majumdar, Mori, Rosso and Schehr [1] study independent Brownian or run-and-tumble particles reset to their individual anchors, with uniformly random/Poisson-limit step-profile initial positions. They calculate **single-observation-time** current distributions, annealed and quenched, and flag spatially correlated initial conditions as a research direction. Those one-time current laws are not presented here as new.

Banerjee, Jack and Cates [2] develop a general spatial-initial-condition variance decomposition and hyperuniform examples for **unreset diffusion**. In fact, the static/initial-geometry decomposition in the present argument follows their general principle and is not independently claimed as novel. The distinct result is its combination with a separately evaluated **stationary-resetting temporal Green--Kubo coefficient**, universal across spatially correlated anchor ensembles, and the resulting exact two-ensemble long-time *time-average* comparison. Formulae for the Poisson-only setting or single-time spatial plateaus alone are not claimed to be new.

## Limitations
The \(T\to\infty\) expansion concerns variance over both the fixed random anchors and the independent particle trajectories, with displacements already stationary at time zero. The positive static plateau is retained in this annealed variance; conditional (fixed-anchor) time-average variance instead decays as \(1/T\). The theorem does not prove an analogous coefficient for interacting gases, simultaneous group resetting, non-Poisson resetting clocks, or nonlinear observables. More general renewal and covariance-decomposition theories may admit an equivalent specialization; a comprehensive independent literature-priority assessment has not been performed. The dense-anchor limit is taken after the time-average asymptotic, without claiming a uniform interchange of limits.

## References
1. C. Di Bello, A. K. Hartmann, S. N. Majumdar, F. Mori, A. Rosso, and G. Schehr, "Current fluctuations in stochastically resetting particle systems", arXiv:2302.06696 (first version February 13, 2023), https://arxiv.org/abs/2302.06696 .
2. T. Banerjee, R. L. Jack, and M. E. Cates, "Role of initial conditions in 1D diffusive systems: compressibility, hyperuniformity and long-term memory", arXiv:2206.08739 (first version June 17, 2022), https://arxiv.org/html/2206.08739v2 .
