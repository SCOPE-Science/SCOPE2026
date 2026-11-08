# A finite quantum Fisher ceiling and phase-aliasing separation for globally reset Rabi spins

## Finding

**Theorem (one stationary snapshot).** Fix \(\Omega>0\), a reset rate \(\gamma>0\), and an integer \(N\ge1\). Consider \(N\) noninteracting qubits evolving under
\[
H=\hbar\Omega\sum_{j=1}^{N}\sigma_x^{(j)},
\]
with *simultaneous* complete resets to \(\lvert0\rangle^{\otimes N}\) at the events of a rate-\(\gamma\) Poisson clock. Observe the stationary state once, without observing the clock or its reset history. Let \(\mathcal F_Q^{(N)}(\gamma)\) denote the supremum, over all POVMs on these \(N\) qubits, of the classical Fisher information for estimating \(\gamma\) (\(\Omega\) is known).

Put \(x=\gamma/\Omega\). Then
\[
0<\mathcal F_Q^{(N)}(\gamma)\le \frac{1}{\Omega^2}\left[\frac{1}{x^2}-\frac{\pi^2}{4\sinh^2(\pi x/2)}\right]<\frac{1}{\gamma^2},
\]
and the first upper bound is sharp in the infinite-population limit:
\[
\boxed{\lim_{N\to\infty}\mathcal F_Q^{(N)}(\gamma)
=\frac{1}{\Omega^2}\left[\frac{1}{x^2}-\frac{\pi^2}{4\sinh^2(\pi x/2)}\right].}
\]
Indeed, nonentangling measurements alternating between \(\sigma_y\) and \(\sigma_z\) on successive qubits attain this limit; collective entangled measurements do not improve the limiting value. Thus the best information available from one stationary, globally reset ensemble remains bounded even as \(N\to\infty\).

For the more restricted experiment measuring \(\sigma_z\) on every qubit, write \(\mathcal F_z^{(N)}(\gamma)\) for the information in the resulting count, and \(a=\pi/2\). Define, for \(0<\theta<a\),
\[
g_x(\theta)=\frac{x\cosh(x(a-\theta))}{\sinh(ax)},\qquad
s_x(\theta)=\frac1x+(a-\theta)\tanh(x(a-\theta))-a\coth(ax).
\]
Then the exact population-limit information is
\[
\boxed{\lim_{N\to\infty}\mathcal F_z^{(N)}(\gamma)
=\frac1{\Omega^2}\int_0^a g_x(\theta)s_x(\theta)^2\,d\theta.}
\]
For every \(x>0\), this limit is strictly positive and strictly smaller than the unrestricted limit; the sequence of \(\sigma_z\)-count information values increases strictly in \(N\). As \(\gamma/\Omega\downarrow0\), the limits have different orders:
\[
\lim_{N\to\infty}\mathcal F_Q^{(N)}(\gamma)
=\frac{\pi^2}{12\Omega^2}+O(\gamma^2/\Omega^4),\qquad
\lim_{N\to\infty}\mathcal F_z^{(N)}(\gamma)
=\frac{\pi^4\gamma^2}{180\Omega^4}+O(\gamma^4/\Omega^6).
\]
Consequently the asymptotic information advantage of phase-sensitive measurements diverges quadratically in \(\Omega/\gamma\) in this regime.

For comparison only, if each spin instead has its *own independent* rate-\(\gamma\) reset clock, independent \(\sigma_z\) measurements have Fisher information
\[
\mathcal F_{z,\mathrm{ind}}^{(N)}(\gamma)=\frac{N}{\Omega^2}\frac{8x^2}{(x^2+4)^2(x^2+2)},
\]
which is linear in population size for every fixed \(\gamma>0\). This comparison isolates the common-clock mechanism behind the ceiling.

## Assumptions and scope

The observations are a *single simultaneous stationary snapshot*; repetitions with independently refreshed clock histories would provide additional information. The qubits are ideal, noninteracting, and initially prepared to \(\lvert0\rangle^{\otimes N}\) at each global reset. There is no dephasing, detuning, readout error, individual resetting, partial resetting, or feedback. The parameter to estimate is the positive reset rate \(\gamma\); the positive Hamiltonian coefficient \(\Omega\) is known. Fisher information is *local* at a fixed parameter value and concerns statistical models, not the performance of a finite-sample estimator.

A POVM may be arbitrary and joint; a fixed, parameter-independent local two-basis strategy suffices asymptotically. The result does not assert a finite-\(N\) quantum Fisher formula, nor equality with the ceiling at finite \(N\).

## Proof

**1. Fold the stationary reset age into its physical phase.** At stationarity, the age \(T\) since the last reset is exponential with density \(\gamma e^{-\gamma t}\). Conditional on \(T=t\), the state is \(\lvert\psi_t\rangle^{\otimes N}\), where
\[
\lvert\psi_t\rangle=\cos(\Omega t)\lvert0\rangle-i\sin(\Omega t)\lvert1\rangle.
\]
Since this *density matrix* is periodic in \(t\) with period \(\pi/\Omega\), define the observable phase \(\phi=\Omega T\pmod\pi\in[0,\pi)\). Its exact density is the folded exponential
\[
h_x(\phi)=\frac{x e^{-x\phi}}{1-e^{-\pi x}},\qquad 0\le\phi<\pi.
\]
The stationary \(N\)-qubit state is \(\rho_N(x)=\int_0^\pi h_x(\phi)(\lvert\psi_\phi\rangle\langle\psi_\phi\rvert)^{\otimes N}d\phi\), with \(\lvert\psi_\phi\rangle=\cos\phi\lvert0\rangle-i\sin\phi\lvert1\rangle\). This is a classical mixture of product states, with all dependence on the unknown rate in the mixing measure.

**2. Universal information ceiling.** Differentiate the logarithm of the phase density with respect to \(x\):
\[
S_x(\phi)=\partial_x\log h_x(\phi)
=\frac1x-\phi-\frac\pi{e^{\pi x}-1}.
\]
Its mean is zero. For any POVM, conditional outcome probabilities \(q(o\mid\phi)\) are independent of \(x\), and the observed score is \(\mathbb E_x[S_x(\phi)\mid o]\), by differentiation under the bounded-interval integral. Conditional Jensen then bounds *every* measurement's Fisher information for \(x\) by \(\mathbb E_x S_x^2=\operatorname{Var}_x(\phi)\). A truncated-exponential moment calculation, or two logarithmic derivatives of its normalizer, yields
\[
\operatorname{Var}_x(\phi)=\frac1{x^2}-\frac{\pi^2 e^{\pi x}}{(e^{\pi x}-1)^2}
=\frac1{x^2}-\frac{\pi^2}{4\sinh^2(\pi x/2)}.
\]
Conversion from \(x\) to \(\gamma\) introduces \(1/\Omega^2\). The variance is strictly positive and strictly smaller than \(1/x^2\), because the positive truncation correction is nonzero.

**3. Sharpness by a nonentangling strategy.** Measure \(\sigma_z\) on odd-labeled qubits and \(\sigma_y\) on even-labeled qubits, independently. Given \(\phi\), conditional means are \(\cos(2\phi)\) and \(-\sin(2\phi)\), respectively. As \(N\to\infty\), the two empirical means converge almost surely to these values. They uniquely determine \(\phi\pmod\pi\), including the wrap-around identification. Let \(\mathcal G_N\) be the sigma-field of the first \(N\) outcomes, with these fixed measurement choices. The observed score for \(x\) is \(M_N=\mathbb E_x[S_x(\phi)\mid\mathcal G_N]\). Since \(S_x\) is bounded and the infinite outcomes determine \(\phi\), the bounded \(L^2\) martingale convergence theorem gives \(M_N\to S_x(\phi)\) in \(L^2\). Thus the Fisher information of this concrete product measurement tends to \(\operatorname{Var}_x(\phi)/\Omega^2\); together with step 2 this proves the quantum optimum limit. This argument needs no assumption that a finite data set determines \(\phi\) exactly.

**4. A sharp measurement-basis gap.** With only \(\sigma_z\) observations, each conditional down-spin outcome has probability \(p=\sin^2\phi\). Hence infinitely many such observations determine only \(\theta=\arcsin\sqrt p\in[0,\pi/2]\), which identifies \(\phi\) with \(\pi-\phi\). Summing the two phase branches gives precisely \(g_x(\theta)=h_x(\theta)+h_x(\pi-\theta)\) above. Its score is \(s_x(\theta)=\partial_x\log g_x(\theta)\). The same bounded conditional-score and martingale argument proves the integral limit.

The phase score \(S_x(\phi)\) is strictly decreasing in \(\phi\). Conditional on an interior \(\theta\), both branches \(\phi=\theta\) and \(\phi=\pi-\theta\) have strictly positive conditional probabilities, and their phase scores differ. The law of total variance therefore gives a *strict* decrease of information after the reflection identification, for every fixed \(x>0\). The resulting \(s_x(\theta)\) is nonconstant and strictly decreasing in \(\theta\) (because \(u\tanh(xu)\) is strictly increasing in \(u>0\)), ensuring positive limiting information.

At finite \(N\), the count \(K_N\) is sufficient for the \(\sigma_z\)-only observations. The exact probabilities and score integrals are
\[
P_{N,k}(x)=\binom Nk\int_0^a g_x(\theta)\sin^{2k}\theta\cos^{2(N-k)}\theta\,d\theta,
\quad
P'_{N,k}(x)=\binom Nk\int_0^a g_x(\theta)s_x(\theta)\sin^{2k}\theta\cos^{2(N-k)}\theta\,d\theta.
\]
Consequently \(\mathcal F_z^{(N)}(\gamma)=\Omega^{-2}\sum_{k=0}^N (P'_{N,k})^2/P_{N,k}\). The information is strictly increasing in \(N\): conditional on any finite \(\sigma_z\) record, the posterior phase has positive density on \((0,a)\), the score \(s_x(\theta)\) decreases strictly as the Bernoulli probability \(\sin^2\theta\) increases, and their conditional covariance is strictly negative. Hence one further Bernoulli observation changes the conditional score with positive probability and strictly increases its squared \(L^2\) norm. The limit follows from the same martingale argument, now with the sample proportion identifying \(\theta\).

**5. Weak- and fast-reset limits.** Set \(a=\pi/2\). The folded-phase variance has the standard uniform-phase expansion \(\operatorname{Var}_x(\phi)=\pi^2/12+O(x^2)\). Uniformly for \(0\le\theta\le a\),
\[
g_x(\theta)=a^{-1}+O(x^2),\qquad
s_x(\theta)=x\bigl((a-\theta)^2-a^2/3\bigr)+O(x^3).
\]
A direct uniform-integral computation gives
\[
\lim_{x\downarrow0}\frac1{x^2}\int_0^a g_x s_x^2d\theta
=\frac1a\int_0^a(u^2-a^2/3)^2du
=\frac{4a^4}{45}=\frac{\pi^4}{180}.
\]
Both displayed weak-reset asymptotics now follow. For completeness, as \(x\to\infty\) both limiting information values are asymptotic to \(1/(\Omega^2 x^2)=1/\gamma^2\); for the \(\sigma_z\) case this follows by setting \(\theta=z/x\), using convergence of its rescaled density to \(e^{-z}\) and the rescaled score to \(1-z\), and bounding the exponentially small complement.

**6. Independent reset clock comparison.** With independent clocks each spin has marginal down probability \(p_x=\mathbb E\sin^2(\Omega T)=2/(x^2+4)\). Its Bernoulli Fisher information for \(x\) equals \((p_x')^2/[p_x(1-p_x)]=8x^2/[(x^2+4)^2(x^2+2)]\). Independent observations add their information, proving the stated contrast.

## Verification

The accompanying `verify.py` implements independently integrated folded-age densities, phase and count likelihoods, analytic-versus-numeric score comparisons, monotonicity, the small- and large-\(x\) limits, and the independent-clock identity. Run `python verify.py` with Python 3, NumPy, and SciPy. These finite checks are diagnostics only; they are not substitutes for the conditional-score and martingale arguments above.

## Relationship to prior work

Magoni, Carollo, Perfetto and Lesanovsky establish the globally resetting, noninteracting spin model and its stationary renewal mixture, classical correlations and local quantum uncertainty. Their results do not give this reset-*rate* quantum Fisher ceiling, its saturating two-basis measurement, or the weak-rate measurement-basis separation. Smiga, Radaelli, Binder and Landi derive information formulas for *temporal* stochastic data and empirical distributions, not a single spatially exchangeable quantum snapshot generated by one hidden Poisson age. Radaelli, Landi, Modi and Binder analyze correlated stochastic-data Fisher information and finite Markov order; that general framework does not imply the specific folded-clock information constants or the spatial quantum measurement-optimal limit. The conditional-score and monotone-information principles themselves are classical; their use is not claimed as a new general inequality.

## Limitations

No finite-population closed-form quantum Fisher formula, noisy-device guarantee, finite-sample estimator performance, or convergence speed is proved. The strict fixed-basis deficit concerns the specified \(\sigma_z\) measurement, not all single-basis strategies. All limits take population size to infinity at fixed positive \(\gamma,\Omega\), *before* the indicated rate asymptotics; interchanging limits is not justified. Other Hamiltonians, reset states, phase diffusion, and repeated snapshots may yield different information behavior. Broader unindexed results in exchangeable quantum statistical models remain a priority/novelty risk; independent expert validation has not occurred.

## References

1. M. Magoni, F. Carollo, G. Perfetto and I. Lesanovsky, *Emergent quantum correlations and collective behavior in non-interacting quantum systems subject to stochastic resetting*, arXiv:2202.12655, first public version February 25, 2022, https://arxiv.org/abs/2202.12655 . Main text and supplementary derivation of stationary reset mixtures, particularly Eq. (2) and Eq. (S14).
2. J. A. Smiga, M. Radaelli, F. C. Binder and G. T. Landi, *Stochastic metrology and the empirical distribution*, arXiv:2305.16480, first public version May 25, 2023, https://arxiv.org/abs/2305.16480 . Temporal sample-data Fisher-information comparison.
3. M. Radaelli, G. T. Landi, K. Modi and F. C. Binder, *Fisher information of correlated stochastic processes*, arXiv:2206.00463, first public version June 1, 2022, https://arxiv.org/abs/2206.00463 . Correlated-process Fisher-information context.
