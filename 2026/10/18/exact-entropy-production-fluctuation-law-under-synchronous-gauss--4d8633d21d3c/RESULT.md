# Exact entropy-production fluctuation law under synchronous Gaussian resetting

## Finding

Let \(d\in\{1,2,\ldots\}\), with \(\kappa,D,r,\sigma^2>0\). Between resets, \(d\) coordinates evolve as independent overdamped harmonic diffusions:
\[
 dX_i(t)=-\kappa X_i(t)\,dt+\sqrt{2D}\,dB_i(t),\qquad i=1,\ldots,d.
\]
A **single common** Poisson clock of rate \(r\) resets the entire vector to a fresh \(N(0,\sigma^2 I_d)\) vector, independent of the clock, history, and thermal noises. Start the process in its stationary distribution. Its entropy production \(S_t\) is the logarithm of the ratio of the probability density of its full path to that of the time-reversed path, including both diffusive and reset jumps, as defined in Mori--Olsen--Krishnamurthy [1]. Define the dimensionless parameters
\[
q=r/\kappa>0,\qquad s=\kappa\sigma^2/D>0.
\]
Then the asymptotic mean \(m_d\) and variance \(v_d\) exist, and satisfy
\[
 \boxed{m_d=\lim_{t\to\infty}\frac{\mathbb E S_t}{t}=\frac{d\kappa q(s-1)^2}{s(q+2)}}
\]
and
\[
 \boxed{v_d=\lim_{t\to\infty}\frac{\operatorname{Var}(S_t)}{t}
 =m_d\left[2+\frac{4(s-1)^2}{s(q+4)}\left(1+\frac{2d}{(q+2)^2}\right)\right].}
\]
For \(s\ne1\), the long-time entropy-production Fano ratio \(v_d/m_d\) is strictly greater than \(2\), strictly decreases with \(q\), and tends to \(2\) as \(q\to\infty\) with the other dimensionless parameters fixed. If \(S_t^{(i)}\) denotes the usual path entropy associated with the individual coordinate's diffusion and its marked jumps on the same clock, then, for distinct \(i,j\),
\[
\boxed{\lim_{t\to\infty}\frac{\operatorname{Cov}(S_t^{(i)},S_t^{(j)})}{t}
=\frac{8\kappa q(s-1)^4}{s^2(q+2)^3(q+4)}>0.}
\]
In particular, **after first taking the long-time limit at each finite \(d\)**,
\[
\boxed{\lim_{d\to\infty}\frac{v_d}{m_d^2}
=\frac{8}{\kappa q(q+2)(q+4)}>0.}
\]
For the comparator in which each coordinate is reset from the same Gaussian law by its own independent rate-\(r\) clock, the mean is unchanged but \(v_d=d v_1\), so the analogous ratio tends to zero. When \(s=1\), the OU equilibrium and reset distribution coincide, detailed balance holds and \(S_t=0\) almost surely: the ratio \(v_d/m_d\) is *undefined*, not \(2\).

## Assumptions and scope

The particles are overdamped; the diffusion, harmonic strength and Gaussian reset variance are isotropic and known. Resetting is instantaneous, complete, Poissonian and synchronous, with fresh mutually independent Gaussian reset coordinates on every common event. The reset law has full support. The initial law is the unique stationary distribution: the mixture of the Gaussian OU transition laws from the latest reset, with independent exponential reset age. The entropy is the dimensionless path-probability log ratio, not a model of a finite-time actuator's energetic cost. Limits in \(t\) precede the limit in the number of coordinates. All claims hold for every positive parameter above, not merely for numerically sampled values.

## Proof

**(1) Exact epoch score.** A complete inter-reset interval has duration \(\tau\sim\operatorname{Exp}(r)\). Its initial post-reset vector is \(X\sim N(0,\sigma^2 I_d)\), and its pre-next-reset vector is
\[
Y=e^{-\kappa\tau}X+\sqrt{\frac D\kappa(1-e^{-2\kappa\tau})}\,Z,
\]
where \(Z\sim N(0,I_d)\) is independent of \(X,\tau\). During the interval, the harmonic potential \(V(x)=\kappa\|x\|^2/2\) dissipates medium entropy \(-[V(Y)-V(X)]/D\). At the subsequent reset, the jump contribution is \(\log[p_R(X)/p_R(Y)]\), with \(p_R\) the centered Gaussian reset density. The complete-epoch score is therefore
\[
W=\left(\frac1{2\sigma^2}-\frac\kappa{2D}\right)(\|Y\|^2-\|X\|^2)
=\sum_{i=1}^d W_i.
\]
This is exactly the reset-plus-medium term in the stationary path-ratio decomposition [1]. The process' system-entropy and incomplete-epoch terms are boundary terms whose second moments stay bounded uniformly in observation time, at every fixed finite \(d\): the stationary density is a mixture of centered Gaussians with covariance between \(\min\{\sigma^2,D/\kappa\}I_d\) and \(\max\{\sigma^2,D/\kappa\}I_d\), so its negative logarithm grows at most quadratically, and the exponential-age OU excursions have finite moments of all fixed orders. Thus those terms do not change the limits of the mean or variance *per unit time*; more precisely their covariance with the centered complete-cycle reward is at most order \(\sqrt t\) by Cauchy--Schwarz.

**(2) Conditional moments.** Write \(u=e^{-2\kappa\tau}\), \(c=(1-s)/(2\sigma^2)\), and \(a=(s-1)^2/(2s)\). For any coordinate, the above Gaussian law gives
\[
\begin{aligned}
\mathbb E[W_i\mid\tau]&=a(1-u),\\
\operatorname{Var}(W_i\mid\tau)&=2c^2\left[\left(\frac D\kappa\right)^2(1+(s-1)u)^2+\sigma^4-2\sigma^4u\right].
\end{aligned}
\]
Indeed, the pre-reset variance is \((D/\kappa)(1+(s-1)u)\), the post-reset variance is \(\sigma^2\), and their squared-covariance contribution is \(\sigma^4u\) by the bivariate Gaussian fourth-moment formula. Distinct coordinates are independent *conditional on the common duration*, although their unconditional rewards are correlated.

**(3) Renewal mean and variance.** Let \(m_1=r\,\mathbb E W_i\). Standard square-integrable regenerative-reward theory, or second-order expansion of the renewal moment-generating equation, yields
\[
 m_d=rd\,\mathbb EW_i,
\qquad v_d=r\,\mathbb E\bigl[(W-m_d\tau)^2\bigr].
\]
This includes the random number of reset intervals and the reward-duration covariance; replacing it by \(r\operatorname{Var}(W)\) would be incorrect. Since \(\mathbb E e^{-2j\kappa\tau}=q/(q+2j)\), for \(j=1,2\), \(\mathbb E\tau=1/r\), and \(\mathbb E\tau^2=2/r^2\), elementary integration gives
\[
 m_1=\frac{\kappa q(s-1)^2}{s(q+2)},
\]
\[
 A:=r\,\mathbb E[\operatorname{Var}(W_i\mid\tau)]
 =\frac{2\kappa q(s-1)^2(qs+2s^2+2)}{s^2(q+2)(q+4)},
\]
and
\[
 C:=r\,\mathbb E\left[\left(\mathbb E[W_i\mid\tau]-m_1\tau\right)^2\right]
 =\frac{8\kappa q(s-1)^4}{s^2(q+2)^3(q+4)}.
\]
Conditional independence gives exactly \(v_d=dA+d^2C\). Dividing by \(m_d=dm_1\), and simplifying the resulting rational function, gives the displayed Fano formula. The covariance rate of two distinct coordinatewise scores is \(C\), because the only shared randomness in their centered complete-cycle rewards is the duration \(\tau\). The joint full-path system-entropy boundary term need not split into coordinate marginals, but is negligible for these rates.

**(4) Strict signs and scaling.** When \(s\ne1\), \(m_1>0\) and \(C>0\), proving strict positive cross-coordinate covariance and the strict Fano bound. The explicit excess in the Fano ratio is a positive multiple of \((q+4)^{-1}[1+2d/(q+2)^2]\), strictly decreasing in \(q\). Furthermore,
\[
\frac{v_d}{m_d^2}=\frac{A}{dm_1^2}+\frac{C}{m_1^2}
\longrightarrow\frac{8}{\kappa q(q+2)(q+4)}.
\]
Independent coordinate-reset clocks remove all cross-coordinate covariance and give \(v_d=d(A+C)\), implying \(v_d/m_d^2\to0\). For \(s=1\), the reset kernel is symmetric with respect to the common OU equilibrium \(N(0,(D/\kappa)I_d)\); both diffusion and reset jumps separately obey detailed balance, so every stationary path has zero time-reversal entropy.

## Verification

Run `python verify.py` with the NumPy and SciPy versions listed in `requirements.txt` (Python \(\ge3.10\)). The standalone checker uses two mathematically independent routes: analytic Gaussian conditional moments integrated afresh by numerical quadrature, and the displayed closed rational formulas. It tests \(100\) parameter-and-dimension combinations and verifies the decomposition, cross covariance and Fano ratios; it also runs two long-horizon regenerative Monte Carlo comparisons and checks the singular free-Brownian limit. It completed **530 assertions** without failure. Numerical checks are finite tests and do not constitute the proof of the all-parameter claims; the proof is the Gaussian moment calculation and renewal derivation above.

## Relationship to prior work

Mori, Olsen and Krishnamurthy [1] establish the trajectory-level decomposition into diffusion, reset and boundary contributions for resetting to a distribution, and evaluate mean entropy production for general confining potentials; they study the full entropy distribution explicitly for **unconfined** Brownian motion. Their free Brownian Gaussian example has mean rate \(1\) and variance rate \(6\) in its chosen units, which are reproduced as a consistency limit of the present one-coordinate formula. The new evaluated harmonic-confinement entropy-variance law and its synchronous-reset covariance are not the formulas reported there.

Bressloff [2] establishes that a global Poisson reset clock can preserve particle correlations even in a large-system limit; common-clock correlations themselves are **not** claimed as new here. The present claim identifies the distinct observable of the pathwise entropy production and evaluates its exact covariance and anomalous dimension scaling in this Gaussian harmonic model. Meylahn, Sabhapandit and Touchette [3] supply a general renewal large-deviation formalism for resetting observables, rather than this evaluated entropy Fano/covariance law. Pal, Reuveni and Rahav [4] study uncertainty relations for unidirectional-transition systems, not the exact positive-support Gaussian reset entropy score considered here. Such general frameworks could potentially yield the present specialized formula through further calculation; this is a genuine priority risk, not evidence of independent validation.

## Limitations

This is an exact asymptotic variance-rate statement and not a finite-time distribution formula or a uniform-in-\(d\) central limit theorem. The order of limits is long time first, then number of coordinates. A common reset clock creates statistical dependence despite independent thermal noises; the result does not apply to simultaneous resetting with correlated Gaussian marks, heterogeneous rates, nonlinear potentials, or partial resets. The ideal instantaneous-reset path entropy need not include the physical cost of implementing the reset apparatus. At \(s=1\) the Fano ratio is undefined. Priority relative to every possible specialization of general renewal and thermodynamic theory has not been independently certified.

## References

[1] F. Mori, K. S. Olsen and S. Krishnamurthy, *Entropy production of resetting processes*, arXiv:2211.15372 (first public 2022-11-28); https://arxiv.org/abs/2211.15372 .

[2] P. C. Bressloff, *Global density equations for interacting particle systems with stochastic resetting: from overdamped Brownian motion to phase synchronization*, arXiv:2401.03501 (first public 2024-01-07); https://arxiv.org/abs/2401.03501 .

[3] J. M. Meylahn, S. Sabhapandit and H. Touchette, *Large deviations for Markov processes with resetting*, Phys. Rev. E 92, 062148 (2015); https://doi.org/10.1103/PhysRevE.92.062148 .

[4] A. Pal, S. Reuveni and S. Rahav, *Thermodynamic uncertainty relation for systems with unidirectional transitions*, Phys. Rev. Research 3, 013273 (2021); https://doi.org/10.1103/PhysRevResearch.3.013273 .
