# Exact one-cycle work asymmetry in a Gaussian memory-preserving information engine

## Finding

The proportional-shift information engine of Bahng, Lee, and Ghim [1] has an exactly solvable **single-cycle extracted-work distribution** when its colored active forcing is Ornstein–Uhlenbeck and measurement errors are independently Gaussian. This gives a complete distributional answer beyond the mean-work calculation of [1], with arbitrary positive cycle period and every feedback gain \(0<g<2\).

At the periodic Gaussian steady state, let \(V=\operatorname{Var}(y_-)\) be the prefeedback position variance, \(\sigma^2>0\) the measurement-error variance, and \(\kappa>0\) the trap stiffness. Put
\[
m=\frac{\kappa g}{2}\bigl[(2-g)V-g\sigma^2\bigr],\qquad d=\kappa^2g^2V\sigma^2,\qquad R=\sqrt{m^2+d}.
\]
For the work \(W=\kappa(y_-^2-y_+^2)/2\), the exact density for \(w\ne0\) is
\[
\boxed{\quad f_W(w)=\frac{\exp(mw/d)}{\pi\sqrt d}\,K_0\!\left(\frac{R|w|}{d}\right),\quad}
\]
where \(K_0\) is the modified Bessel function of the second kind. In particular,
\[
\boxed{\quad\frac{f_W(w)}{f_W(-w)}=\exp\!\left(\frac{2mw}{d}\right),\quad
\Pr(W>0)=\frac12+\frac1\pi\arctan\!\left(\frac{m}{\sqrt d}\right),\quad
\operatorname{Var}(W)=2m^2+d.\quad}
\]
Thus both signs of work occur with positive probability for every positive measurement-error variance; the work law is exactly even **if and only if** \((2-g)V=g\sigma^2\), the same boundary on which its mean vanishes. The displayed relation is a distributional *work-asymmetry identity*, not a Crooks/Jarzynski relation or a statement of entropy-production reversibility.

Moreover the variance \(V\) is available explicitly at finite cycle length. Write
\[
\tau_r=\gamma/\kappa,\quad \rho=e^{-\tau/\tau_r},\quad\nu=e^{-\tau/\tau_c},\quad q=1-g,\quad
C_\infty=\frac{A^2}{\gamma(1/\tau_r+1/\tau_c)},\quad
V_\infty=\frac{k_{\mathrm B}T+C_\infty}{\kappa},
\]
and set
\[
F=\begin{cases}\displaystyle\frac{\rho\nu-\rho^2}{1-\tau_r/\tau_c},&\tau_r\ne\tau_c,\\[3pt]
\displaystyle\frac{\tau}{\tau_r}\rho^2,&\tau_r=\tau_c.\end{cases}
\]
Then the exact periodic prefeedback cross-covariance and positional variance are
\[
\boxed{\quad C=\frac{C_\infty(1-\rho\nu)}{1-q\rho\nu},\qquad
V=\frac{\rho^2g^2\sigma^2+V_\infty(1-\rho^2)-\dfrac{2gC_\infty}{\kappa(1-q\rho\nu)}F}{1-q^2\rho^2}.\quad}
\]
These finite-period expressions make the asymmetry slope and exact probability of positive work functions of the physical bath and feedback parameters, without fitting a work histogram.

## Assumptions and scope

Fix \(\kappa,\gamma,\tau_c,\tau>0\), \(T>0\), an active-force amplitude \(A\ge0\), \(\sigma^2>0\), and gain \(0<g<2\). Between successive feedback times separated by \(\tau\), the relative position and active force obey the independent-noise, one-dimensional linear stochastic dynamics
\[
\gamma\,dy_t=-\kappa y_t\,dt+\eta_t\,dt+\sqrt{2\gamma k_{\mathrm B}T}\,dB_t,
\qquad
 d\eta_t=-\frac{\eta_t}{\tau_c}\,dt+\sqrt{\frac{2A^2}{\tau_c}}\,dB'_t.
\]
At each measurement, sample a fresh \(\epsilon\sim N(0,\sigma^2)\), independent of the entire premeasurement state and of all bath noises, and shift the trap center instantaneously with gain \(g\): \(y_+=(1-g)y_--g\epsilon\). The active force does not jump. Consider the unique zero-mean periodic stationary Gaussian state at measurement times. \(W\) counts **only** the instantaneous extracted work at one feedback event, not total heat, full-cycle entropy or an accumulated multi-cycle work sum.

## Proof

**1. Existence of the Gaussian steady state.** Let \(Z_t=(y_t,\eta_t)^\top\). Relaxation for time \(\tau\) is an affine Gaussian update with deterministic linear part \(e^{\tau H}\), where
\[
H=\begin{pmatrix}-1/\tau_r&1/\gamma\\0&-1/\tau_c\end{pmatrix}.
\]
A feedback event multiplies the prior state by \(\operatorname{diag}(q,1)\) and adds independent Gaussian noise in the position. The one-period transition matrix has eigenvalues \(q\rho\) and \(\nu\), both strictly inside the unit disk. Iterating yields the unique centered stationary Gaussian law. Its prefeedback position variance \(V>0\) because \(T>0\).

**2. Explicit stationary covariance.** For the uncoupled relaxation of the active process, the fixed cross-covariance is \(C_\infty\) as defined above. From the linear drift and OU autocorrelation, for postfeedback covariance \(C_+=qC\),
\[
C=C_\infty+(C_+-C_\infty)\rho\nu.
\]
Solving gives \(C=C_\infty(1-\rho\nu)/(1-q\rho\nu)\) and \(C_\infty-C_+=gC_\infty/(1-q\rho\nu)\). The positional variance after feedback is \(V_+=q^2V+g^2\sigma^2\). The exact OU covariance propagation is
\[
V=\rho^2V_++V_\infty(1-\rho^2)-\frac{2}{\kappa}(C_\infty-C_+)F.
\]
Substitution and division by \(1-q^2\rho^2>0\) gives the asserted formula. The continuous value of \(F\) at \(\tau_r=\tau_c\) follows by a one-variable limit. All denominators in the resulting expression are nonzero for the stated positive parameters.

**3. Indefinite Gaussian quadratic form.** At a feedback time, \(y_-\sim N(0,V)\) and the current measurement error \(\epsilon\sim N(0,\sigma^2)\) are independent. Expanding the instantaneous work gives
\[
W=\frac{\kappa}{2}\left[g(2-g)y_-^2+2g(1-g)y_-\epsilon-g^2\epsilon^2\right].
\]
Writing \((y_-,\epsilon)=(\sqrt V U,\sigma Z)\) for independent standard Gaussians, \(W=(U,Z)B(U,Z)^\top\) with
\[
B=\frac{\kappa}{2}\begin{pmatrix}
g(2-g)V&g(1-g)\sqrt{V\sigma^2}\\g(1-g)\sqrt{V\sigma^2}&-g^2\sigma^2
\end{pmatrix}.
\]
Directly, \(\operatorname{tr}B=m\) and \(\det B=-d/4\), the latter because \((2-g)g+(1-g)^2=1\). Since \(d>0\), its eigenvalues \(\lambda_\pm=(m\pm R)/2\) have opposite signs, and orthogonal Gaussian invariance gives \(W\overset{d}{=}\lambda_+U_1^2+\lambda_-U_2^2\) with independent standard normal \(U_1,U_2\). Therefore for
\(-1/(R-m)<t<1/(R+m)\),
\[
\mathbb E[e^{tW}]
=(1-2t\lambda_+)^{-1/2}(1-2t\lambda_-)^{-1/2}
=\boxed{(1-2mt-dt^2)^{-1/2}}.
\]
The first two derivatives of its logarithm give mean \(m\) and variance \(2m^2+d\).

**4. Density, sign probability, and asymmetry.** Each positive variable \(\lambda_+U_1^2\) and \(|\lambda_-|U_2^2\) has a Gamma distribution with shape \(1/2\); convolving their difference gives the displayed Bessel-\(K_0\) density. In particular, the factor involving \(K_0\) is even in \(w\), which proves the exact ratio. Moreover \(W>0\) is the event
\(|U_1/U_2|>\sqrt{|\lambda_-|/\lambda_+}\). Since \(U_1/U_2\) is standard Cauchy, its probability simplifies to \(1/2+\arctan(m/\sqrt d)/\pi\). This lies strictly between zero and one; it equals one half precisely when \(m=0\), equivalent to the displayed work-symmetry boundary. The density has an integrable logarithmic singularity at the origin, so its ratio is stated only at \(w\ne0\).

For an additional fixed-input diagnostic, hold \(V\) and \(\sigma^2\) fixed while varying the *single-step* gain. Then \(m/\sqrt d=[(2-g)V-g\sigma^2]/(2\sqrt{V\sigma^2})\) strictly decreases in \(g\). Thus maximizing the **chance** of any positive extracted work for a fixed input ensemble is not equivalent to maximizing the mean extracted work. This comparison does not optimize the periodic engine, where \(V\) itself depends on \(g\).

## Verification

The accompanying `verify.py` implements an independent two-dimensional OU covariance calculation using continuous and discrete Lyapunov equations, compares it with the closed prefeedback formulas, checks Gaussian quadratic eigenvalues and the moment generating function, numerically integrates the proposed Bessel-\(K_0\) density, independently integrates its positive tail, and tests the asymmetry ratio and zero-mean symmetry case. Running `python verify.py` with NumPy and SciPy yielded **114 passing deterministic comparisons** across seven parameter sets, including equal and unequal OU/relaxation time scales, nonzero active forcing, and feedback gains on both sides of one. These finite checks are corroboration; the proof is analytic.

## Relationship to prior work

Bahng, Lee, and Ghim [1] derive the feedback update, finite-time covariance propagation and average extracted work. They explicitly identify higher work moments and fluctuation relations as future directions. The distributional law, its explicit Bessel form, signed-work ratio, exact success probability and closed finite-period OU covariance above are the claims here; their baseline stochastic model and mean-work identities are **not** claimed to be new.

Paneru et al. [2] experimentally study the **full-shift, passive thermal** noisy information engine, including measured work histograms, first two work moments and the symmetry of the distribution at the noise-driven crossover. That case is contained as a specialization, with \(g=1\) and \(A=0\), and is explicitly not claimed as new. Paneru et al. [3] study thermodynamic uncertainty relations for such engines, rather than the full memory-preserving active-bath law with an explicit Bessel density. General diagonalization of Gaussian quadratic forms and variance-gamma/Bessel distributions is a classical mathematical technique; novelty is not asserted for that technique itself.

## Limitations

Only one instantaneous feedback event is studied in the periodic Gaussian OU steady state. Work values at successive cycles are correlated through bath memory; neither their sum nor a long-time work-fluctuation symmetry follows from the result. The density and ratio require positive independent Gaussian measurement noise and Gaussian active forcing; non-Gaussian colored forcing or correlated/non-Gaussian measurement errors generally invalidate the shape. No thermodynamic Crooks relation, Jarzynski equality or entropy-production fluctuation theorem is established. Finite feedback duration, nonlinear traps, nonstationary initial states and velocity degrees of freedom are outside scope. Prior experimental work [2] already treats the full-shift passive special case, and implicit coverage by general quadratic-Gaussian work-statistics formulas remains an originality risk.

## References

[1] S. Bahng, J. S. Lee, and C.-M. Ghim, *Memory-aware feedback enhances power in active information engines*, arXiv:2508.16866v1 (first posted 2025-08-23); subsequently Phys. Rev. E **112**, 054134 (2025). https://arxiv.org/abs/2508.16866; full HTML https://arxiv.org/html/2508.16866.

[2] G. Paneru, S. Dutta, T. Sagawa, T. Tlusty, and H. K. Pak, *Efficiency fluctuations and noise induced refrigerator-to-heater transition in information engines*, Nat. Commun. **11**, 1012 (2020), arXiv:1911.09833. https://doi.org/10.1038/s41467-020-14823-x.

[3] G. Paneru, S. Dutta, T. Tlusty, and H. K. Pak, *Reaching and violating thermodynamic uncertainty bounds in information engines*, Phys. Rev. E **102**, 032126 (2020), arXiv:1911.09835. https://arxiv.org/abs/1911.09835.
