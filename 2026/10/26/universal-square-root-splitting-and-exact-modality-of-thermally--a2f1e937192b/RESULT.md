# Universal square-root splitting and exact modality of thermally smoothed trapped run-and-tumble laws

## Finding
For the one-dimensional harmonically confined symmetric run-and-tumble model with thermal diffusion, the entire stationary modal phase diagram consists of exactly one peak for sufficiently rapid tumbling or sufficiently strong thermal noise, and exactly two symmetric peaks at lower thermal noise when tumbling is persistent. There are no additional stationary peaks. The two emergent maxima obey a **universal square-root calibration** independent of the persistence parameter:

\[
z_*(\theta)=\sqrt{\frac32}\sqrt{\theta_c(k)-\theta}+O_k((\theta_c(k)-\theta)^{3/2})\qquad(\theta\uparrow\theta_c(k)).
\]

Equivalently, in physical coordinates the two maxima lie at \(\pm x_*(D)\), where

\[
x_*(D)=\sqrt{\frac{3}{\mu}}\sqrt{D_c-D}+O_{\mu,\gamma,v_0}((D_c-D)^{3/2}),\qquad D_c=\frac{v_0^2\theta_c(k)}{2\mu}.
\]

In particular, the leading physical displacement coefficient \(\sqrt{3/\mu}\) depends on the trap relaxation rate but neither on the tumbling rate nor on the propulsion speed. The critical thermal-to-active ratio \(\theta_c(k)\) decreases strictly with \(k\in(0,1)\).

## Assumptions and scope
Let \(\mu,v_0,D,\gamma>0\). In stationarity, let

\[
dX_t=(-\mu X_t+v_0\eta_t)\,dt+\sqrt{2D}\,dW_t,
\]

where the independent symmetric telegraph orientation \(\eta_t\in\{-1,+1\}\) switches sign at rate \(\gamma/2\). Define \(k=\gamma/(2\mu)>0\), the dimensionless position \(z=\mu x/v_0\) and thermal strength \(\theta=2\mu D/v_0^2>0\). This switching convention is equivalent to independent orientation resampling at total event rate \(\gamma\). The stationary density, apart from a positive normalizing constant, is the Gaussian convolution

\[
f_{k,\theta}(z)=C_{k,\theta}\int_{-1}^{1}(1-u^2)^{k-1}\exp\!\left(-\frac{(z-u)^2}{\theta}\right)du.
\]

The athermal beta law and its Gaussian convolution are established in the cited literature and are not claimed as new. All statements below concern global maxima of this \(C^\infty\) positive even density over the entire real line. The case \(D=0\), nonharmonic trapping and higher spatial dimensions are excluded.

Set \(t=1/\theta\) and, for every integer \(n\geq0\),

\[
I_n(k,t)=\int_0^1 y^{n-1/2}(1-y)^{k-1}e^{-ty}\,dy,
\quad F_k(t)=2t\frac{I_1(k,t)}{I_0(k,t)}-1.
\]

For \(0<k<1\), let \(t_c(k)\) be the unique positive zero of \(F_k\), and set \(\theta_c(k)=1/t_c(k)\).

**Complete modal classification.** If \(k\geq1\), or if \(0<k<1\) and \(\theta\geq\theta_c(k)\), then \(z=0\) is the unique global maximum and \(f'_{k,\theta}(z)<0\) for all \(z>0\). If \(0<k<1\) and \(0<\theta<\theta_c(k)\), then \(z=0\) is a strict local minimum, and there is exactly one positive maximum \(z_*(\theta)\in(0,1)\), and its negative reflection, with no further critical points. At the transition, \(z=0\) is a flat strict global maximum with negative quartic derivative.

## Proof
**Stationary convolution.** With \(D=0\), the stationary telegraph transport equations and their zero-net-current relation imply \(p_+(x)-p_-(x)=(\mu x/v_0)(p_+(x)+p_-(x))\). Their difference equation then yields \(p_+(x)+p_-(x)\propto(1-\mu^2x^2/v_0^2)^{k-1}\) on the support \(|\mu x/v_0|<1\). Independently, the Brownian forcing contributes a stationary Ornstein–Uhlenbeck Gaussian with variance \(D/\mu\); summing the independent active and thermal components proves the displayed convolution.

**Exact moment identity.** Integration by parts of \(y^{n+1/2}(1-y)^ke^{-ty}\), whose boundary contributions vanish for \(k>0\), gives for all \(n\geq0\):

\[
2t(I_{n+1}-I_{n+2})=(2n+1)I_n-(2n+2k+1)I_{n+1}.
\tag{1}
\]

Differentiating the convolution at the origin gives \(f''(0)/f(0)=2tF_k(t)\). For \(k\geq1\), the athermal density is log-concave on its support, hence its convolution with the strictly log-concave Gaussian is symmetric and unimodal; the strict derivative sign also follows from the power-series argument below. For \(0<k<1\), as \(t\downarrow0\), \(F_k(t)\to-1\), while Watson expansion as \(t\to\infty\) yields \(F_k(t)=(1-k)t^{-1}+O_k(t^{-2})>0\) for large \(t\).

At a zero \(t=t_c\), \(I_1/I_0=1/(2t_c)\), and (1) with \(n=0\) gives \(I_2/I_0=(2k+1)/(4t_c^2)\). The \(I_n/I_0\) are moments of a positive tilted law on \((0,1)\). Since \(\partial_t(I_1/I_0)=-\operatorname{Var}_t(Y)\), at every zero

\[
\operatorname{Var}_{t_c}(Y)=\frac{k}{2t_c^2},\qquad
F'_k(t_c)=\frac{1-k}{t_c}>0.
\tag{2}
\]

Thus every zero crosses strictly from negative to positive. The endpoint signs force existence and *uniqueness* of the zero. Moreover, \(\partial_kF_k(t)=2t\operatorname{Cov}_t(Y,\log(1-Y))<0\) by strict opposite monotonicity of the two functions. Implicit differentiation of (2) gives \(t'_c(k)>0\), hence \(\theta'_c(k)<0\) for \(0<k<1\).

**The global mode count, not only local curvature.** Write

\[
b_n=2t\frac{I_{n+1}}{I_n}-(2n+1).
\]

Equation (1) is equivalent to the exact recursion

\[
b_n=\frac{I_{n+1}}{I_n}\bigl(b_{n+1}+2(1-k)\bigr).
\tag{3}
\]

Because \(I_{n+1}<I_n\), one has \(b_n<0\) whenever \(2n+1>2t\). For \(0<k<1\), (3) shows that if \(b_n\leq0\) then \(b_{n+1}<0\); thus the signs of the sequence are initially positive and then strictly negative, or all negative (with possible \(b_0=0\)). For \(k\geq1\), (3) and eventual negativity imply by backward induction that every \(b_n<0\).

Expanding the sinh and cosh factors in the differentiated Gaussian convolution gives, for \(z>0\),

\[
\frac{f'_{k,\theta}(z)}{z}=2tC_{k,\theta}e^{-tz^2}
\sum_{n=0}^{\infty}\frac{(2t)^{2n}}{(2n+1)!}
\bigl[2tI_{n+1}-(2n+1)I_n\bigr]z^{2n}.
\tag{4}
\]

Here \(C_{k,\theta}\) is the same positive normalizer as in the density definition; the factor from evenness is included in the displayed coefficient. The absolute convergence on compact sets follows from \(0\leq Y\leq1\). By (3), the nonzero coefficients of the series in (4) have at most one sign change, from positive to negative. If the first coefficient is nonpositive, all coefficients are negative except possibly the zeroth, so \(f'(z)<0\) for all \(z>0\). If the first is positive, divide the power series by the highest nonnegative-index power before its negative tail; the resulting function is strictly decreasing on \((0,\infty)\). Therefore it has at most one positive root. One root must occur because \(f'(z)>0\) for small \(z>0\), while for every \(z\geq1\), direct differentiation under the convolution gives \(f'(z)<0\). This proves the full global classification.

**Critical quartic coefficient and universal peak splitting.** At \(t=t_c\), the two moment relations above imply

\[
\frac{f^{(4)}(0)}{f(0)}=16t_c^4\frac{I_2}{I_0}-48t_c^3\frac{I_1}{I_0}+12t_c^2=-8(1-k)t_c^2<0.
\tag{5}
\]

Equations (2) and (5) give the uniform local analytic expansion

\[
\frac{f'(z)}{zf(0)}=2(1-k)(t-t_c)-\frac43(1-k)t_c^2z^2
+O_k((t-t_c)^2+|t-t_c|z^2+z^4).
\tag{6}
\]

The analytic implicit-function theorem applied in \(z^2\) yields

\[
z_*^2=\frac{3}{2t_c^2}(t-t_c)+O_k((t-t_c)^2)
=\frac32(\theta_c-\theta)+O_k((\theta_c-\theta)^2).
\]

Taking the positive root proves the dimensionless result. Finally \(x=v_0z/\mu\) and \(\theta_c-\theta=2\mu(D_c-D)/v_0^2\) give the physical coefficient \(\sqrt{3/\mu}\), independent of \(k\) and \(v_0\). Every error estimate holds for fixed \(0<k<1\), not uniformly as \(k\) approaches its endpoints.

## Verification
The complete standalone file `verification.py` evaluates the defining tilted beta moments with Jacobi Gaussian quadrature, tests the integration-by-parts identities, verifies the critical second and fourth derivatives, checks global derivative signs, compares the critical peak-separation coefficient, and checks strict critical-thermal-strength monotonicity. Its deterministic run passed 266 individual assertions over the specified parameter grid. Finite numerical tests are diagnostic only; the all-parameter claims rest on equations (1)–(6). Run with Python 3, NumPy, and SciPy using `python verification.py`.

## Relationship to prior work
Guéneau, Majumdar and Schehr (2026) derive the exact stationary trapped-particle distribution and its thermal Gaussian convolution, and discuss the thermal shape transition including a center-curvature criterion. Sabhapandit and Majumdar (2024) derive a related convolution for a telegraphically displaced trap, including an implicit shape-transition criterion. These distributions and transition equations are prior results. Sevilla and Meléndez Mora (2026) independently discuss the thermal Gaussian convolution and qualitative crossover. The present theorem concerns the **global uniqueness of the positive-side mode**, the **strict monotonicity of the transition point**, and especially the **persistence-independent square-root coefficient** from exact critical fourth-order curvature. It does not claim that the Gaussian convolution or curvature-zero equation itself is new.

## Limitations
The critical threshold is defined by a one-dimensional moment equation and is not generally an elementary constant. The peak asymptotic is local in \(D_c-D\), at fixed \(0<k<1\); it does not treat weak-confinement, vanishing-diffusion and persistence-endpoint limits simultaneously. No claim is made for higher dimensions, time-dependent densities, inertia, nonlinear potentials, or colored thermal noise. General Gaussian smoothing theory might provide another route to aspects of the mode-count statement; independent priority assessment has not been undertaken.

## References
1. M. Guéneau, S. N. Majumdar, G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436v1 (first posted 2026-02-09), https://arxiv.org/abs/2602.08436.
2. S. Sabhapandit, S. N. Majumdar, *Noninteracting particles in a harmonic trap with a stochastically driven center*, arXiv:2404.02480v1 (2024), https://arxiv.org/abs/2404.02480.
3. F. J. Sevilla, J. A. Meléndez Mora, *Nonequilibrium statistics of harmonically trapped run-and-tumble particles: An exact convolution approach*, arXiv:2608.21781v1 (2026), https://arxiv.org/abs/2608.21781.
