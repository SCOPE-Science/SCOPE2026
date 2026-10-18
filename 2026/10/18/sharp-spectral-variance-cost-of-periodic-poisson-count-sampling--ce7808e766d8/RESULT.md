# Sharp spectral variance cost of periodic Poisson count sampling

## Finding
Let \(\lambda>0\), and let \(\eta:\mathbb R\to(0,\infty)\) be a continuous, one-periodic function with \(\int_0^1\eta(u)\,du=1\). On the entire real line, take a Poisson point process of deterministic intensity \(\lambda\eta(t)\,dt\), and write \(S(t)\) for the number of its points in \((t-1,t]\). In particular, \(S(t)\) has exactly the Poisson law with mean \(\lambda\) at **every** time, regardless of \(\eta\). Define the physical-time factorial-pair estimator, for each integer \(n\ge1\), by
\[
Q_n=\frac1n\int_0^n S(t)(S(t)-1)\,dt,
\qquad
\widehat\eta(k)=\int_0^1\eta(t)e^{-2\pi i k t}\,dt.
\]
Then the following central limit theorem and **exact asymptotic-variance identity** hold:
\[
\sqrt n\,(Q_n-\lambda^2)\ \Longrightarrow\ N(0,V_\eta),
\qquad
\lim_{n\to\infty}n\operatorname{Var}(Q_n)=V_\eta,
\]
\[
\boxed{V_\eta=4\lambda^3+\frac43\lambda^2
+\frac{2\lambda^2}{\pi^2}\sum_{k\in\mathbb Z\setminus\{0\}}
\frac{|\widehat\eta(k)|^2}{k^2}.}
\]
The entire admissible class has the sharp variance corridor
\[
4\lambda^3+\frac43\lambda^2\ \le V_\eta
\ <\ 4\lambda^3+2\lambda^2.
\]
The **unique minimizer** is the constant-rate sampler \(\eta\equiv1\); the upper bound is a strict, **unattained supremum** approached by smooth positive periodic intensities concentrating into narrow pulses. For the explicit harmonic modulation \(\eta(t)=1+a\cos(2\pi kt)\), \(0<|a|<1\), \(k\in\mathbb N\), its exact variance excess is \(\lambda^2a^2/(\pi^2k^2)\). In contrast, the physical-time average of the **linear** statistic \(S(t)\) always has asymptotic variance \(\lambda\), independently of \(\eta\).

## Assumptions and scope
All assertions concern the **integer-horizon physical-time estimator** above and the Poisson-process equilibrium construction on all of \(\mathbb R\). The rate profile is strictly positive, continuous, one-periodic, and normalized to total mass one per period; the result does not require any differentiability. All moments exist. The point process is independently scattered, but the overlapping counts \(S(t)\) are not independent. Its one-time target law is \(\operatorname{Poisson}(\lambda)\).

The model is the univariate Poisson-target, history-independent periodic-base-intensity case of the sliding-window point-process sampler: with target unnormalized weights \(f(j)=\lambda^j\), intensity \(\lambda\eta(t)\) implements the target exactly. Sampling efficiency here refers to physical-time integration of a specified observable, **not** to an event-count-normalized or nonlinear-clock-normalized performance metric.

## Proof
**1. Two-window Poisson covariance.** Fix times \(t\) and \(t+h\). For \(0\le h\le1\), the overlap of their windows is \((t+h-1,t]\), with Poisson mean
\[
\rho(t,h)=\lambda A_{1-h}(t),\qquad A_L(t)=\int_{t-L}^{t}\eta(u)\,du.
\]
The two nonoverlapping parts and the common part of the windows have independent Poisson counts. Therefore, for \(X=S(t)\) and \(Y=S(t+h)\), the bivariate factorial generating function is
\[
\mathbb E[(1+z)^X(1+w)^Y]
=\exp\{\lambda z+\lambda w+\rho(t,h)zw\}.
\]
Differentiating twice in each variable at the origin gives
\[
\operatorname{Cov}((X)_2,(Y)_2)=4\lambda^2\rho(t,h)+2\rho(t,h)^2,
\quad (x)_2=x(x-1).
\]
For \(|h|\ge1\), the windows are disjoint and this covariance is zero. Also \(\mathbb E(S(t))_2=\lambda^2\) at every time.

**2. Long-run variance and limit law.** Let \(B_j=\int_j^{j+1}((S(t))_2-\lambda^2)\,dt\), for integer \(j\). Each \(B_j\) depends only on point-process increments over \((j-1,j+1]\). Periodicity makes \((B_j)\) strictly stationary, and independent increments make it **one-dependent**: \(B_j\) and \(B_{j+r}\) are independent for \(|r|\ge2\). Its moments of all orders are finite. Consequently the one-dependent central limit theorem gives a centered Gaussian limit for \(n^{-1/2}\sum_{j=0}^{n-1}B_j\), with variance \(\operatorname{Var}(B_0)+2\operatorname{Cov}(B_0,B_1)\). Direct covariance integration, exploiting time-periodicity and symmetry of covariance, identifies that variance as
\[
V_\eta=2\int_0^1\int_0^1
[4\lambda^3 A_{1-h}(t)+2\lambda^2 A_{1-h}(t)^2] \,dh\,dt.
\]
This same integral equals \(\lim_{n\to\infty}n\operatorname{Var}(Q_n)\), by one-dependence (the finite-horizon variance is \(n\operatorname{Var}(B_0)+2(n-1)\operatorname{Cov}(B_0,B_1)\)).

**3. Fourier evaluation.** For each \(L\in[0,1]\), \(\int_0^1A_L(t)\,dt=L\). Thus the linear-overlap term contributes exactly \(4\lambda^3\). Plancherel on the unit circle gives
\[
\int_0^1 A_L(t)^2\,dt=L^2+
\sum_{k\ne0}|\widehat\eta(k)|^2\frac{\sin^2(\pi kL)}{\pi^2k^2}.
\]
Tonelli applies to the nonnegative sum. Since \(\int_0^1L^2\,dL=1/3\) and \(\int_0^1\sin^2(\pi kL)\,dL=1/2\) for nonzero integer \(k\), substitution proves the stated exact expression for \(V_\eta\).

**4. Sharp extrema.** Each Fourier penalty is nonnegative; it vanishes precisely when all nonzero Fourier coefficients vanish, which by completeness of the trigonometric system and continuity means \(\eta\equiv1\). Since \(\eta>0\) and \(0<L<1\), every arc integral satisfies \(0<A_L(t)<1\), so \(\int_0^1 A_L(t)^2dt<\int_0^1A_L(t)dt=L\). Integrating yields \(\int_0^1\int_0^1 A_L(t)^2\,dt\,dL<1/2\), proving the strict upper bound. For sharpness choose a sequence of smooth positive normalized periodic functions converging weakly to a unit atom at one phase (a narrow smooth nonnegative bump with vanishing positive constant floor). For each nonzero integer \(k\), the corresponding Fourier coefficient tends to one in modulus and is bounded in modulus by one. Dominated convergence and \(\sum_{k\ne0}k^{-2}=\pi^2/3\) give convergence to \(4\lambda^3+2\lambda^2\), with no upper maximizer. The sinusoidal formula follows because only \(\widehat\eta(\pm k)=a/2\) are nonzero away from the constant mode.

**5. Linear-statistic contrast.** With \(X=S(t)\), \(Y=S(t+h)\), the covariance is just \(\rho(t,h)\). Repeating step 2 for centered linear averages, the variance coefficient is \(2\lambda\int_0^1(1-h)\,dh=\lambda\). The same one-dependent argument proves a Gaussian limit for the linear average. No statement about optimality for other nonlinear observables or higher-dimensional interacting targets is made.

## Verification
The standalone `verify.py` recomputes the Fourier identity for sinusoidal profiles, checks the strict variance bounds on a broad parameter grid, and cross-checks the quadratic-window-overlap expression through independent two-dimensional deterministic quadrature. Its numerical checks are diagnostics; every infinite assertion above follows from the five analytical steps. To reproduce, run `python verify.py` with Python 3 and NumPy installed. No stochastic simulation or hidden data are required.

## Relationship to prior work
Stewart and Sahani, *Sampling on Discrete Spaces with Temporal Point Processes* (arXiv:2603.09089, first public March 10, 2026), construct the periodic-intensity Poisson target in their Example 1 and explicitly identify the influence of oscillatory modulation on asymptotic variance as an unresolved efficiency question in their Discussion. They anticipate that a common periodic time change may have little effect; they do not give the **physical-time nonlinear-observable spectral penalty**, its exact sharp corridor, or its unique optimizing intensity. The distinction is important: one-point Poisson marginals and linear-observable efficiency are unchanged while the quadratic factorial moment becomes less efficient.

Reitzner and Schulte, *Central limit theorems for U-statistics of Poisson point processes* (arXiv:1104.1039, first public April 6, 2011), provide general chaos expansions, moment and variance methods, and limit theorems for Poisson U-statistics. Those generic tools encompass the factorial-moment covariance calculation; the model-specific new assertion here is the exact **periodic modulation Fourier penalty and sharp extremal design**, with its physical-time versus target-marginal contrast. The proof deliberately uses elementary bivariate Poisson generating functions and one-dependence rather than claiming a new generic Poisson CLT. The literature comparison does not certify absolute historical priority.

## Limitations
This is a sharp result for one Poisson target, a deterministic full-period window, and continuous positive periodic intensity modulation. It does not cover interacting multivariate point-process samplers, arbitrary target laws, alternative time-normalizations, mixing-time optimization, or nonlinear observables beyond the explicitly analyzed pair-count. The supremum requires a **limiting sequence**, not an admissible continuous optimizer. Independent external audit and exhaustive priority verification have not been performed.

## References
1. C. A. Stewart and M. Sahani, *Sampling on Discrete Spaces with Temporal Point Processes*, arXiv:2603.09089v1 (first public March 10, 2026), especially Example 1 and Discussion; https://arxiv.org/abs/2603.09089 .
2. M. Reitzner and M. Schulte, *Central limit theorems for U-statistics of Poisson point processes*, arXiv:1104.1039 (first public April 6, 2011), especially Sections 3--4; https://arxiv.org/abs/1104.1039 .
