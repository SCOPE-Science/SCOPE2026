# Quartic finite-size switching window at the majority-reset quantum transition

## Finding

For the symmetric majority-based conditional resetting of noninteracting Rabi spins, the probability of changing the fully polarized reset label at the next Poisson reset has a sharp, three-regime asymptotic classification. The critical point is a **quartic**, rather than Gaussian, saddle; the switching probability decays as \(N^{-1/4}\), with an explicit Gamma-function coefficient and a nontrivial critical-window scaling function. Strictly below the transition the switching probability has the sharp entropy exponent and an \(N^{-1}\) prefactor, while above the transition it approaches an explicit positive limit.

Let \(N\) tend to infinity through **odd** positive integers and put
\[
 a=\frac{\Omega^2}{\Omega^2+\Delta^2},\qquad
 \omega=\sqrt{\Omega^2+\Delta^2},\qquad
 \beta=\frac{\gamma}{\omega},\qquad
 S_\beta=\frac{e^{-\beta\pi/2}}{1-e^{-\beta\pi}}.
\]
Let \(Q_N\) denote the exact probability that the all-up/all-down label changes at the next reset, averaged over its exponentially distributed waiting time. For fixed \(\beta>0\), the conclusions are:

**Subcritical \(0<a<1/2\).** Define \(I(a)=-\tfrac12\log[4a(1-a)]>0\). Then
\[
 Q_N\sim
 \frac{2\beta\sqrt a(1-a)}{(1-2a)^{3/2}}
 S_\beta\,\frac{e^{-N I(a)}}{N}.
\]

**Critical \(a=1/2\).** Then
\[
 Q_N\sim
 \beta S_\beta\frac{2^{1/4}\Gamma(3/4)}{\sqrt\pi}\,N^{-1/4}.
\]

**Supercritical \(1/2<a<1\).** With
\(\theta_a=\arcsin[(2a)^{-1/2}]\in(0,\pi/2)\),
\[
 Q_N\longrightarrow
 \frac{e^{-\beta\theta_a}-e^{-\beta(\pi-\theta_a)}}
 {1-e^{-\beta\pi}}>0.
\]

The critical window also has a complete nonconstant profile. Fix physical \(\Delta>0\) and \(\gamma>0\), and choose a sequence of positive driving strengths \(\Omega_N\) such that
\[
 a_N=\frac{\Omega_N^2}{\Omega_N^2+\Delta^2}
 =\frac12+\frac{\xi}{\sqrt N}
\]
for a fixed real \(\xi\) and all sufficiently large odd \(N\). Define \(\beta_c=\gamma/(\sqrt2\,\Delta)\). Then
\[
 \boxed{\lim_{N\to\infty}N^{1/4}Q_N
 =\beta_c S_{\beta_c}\,\mathcal F(\xi),\qquad
 \mathcal F(\xi)=\int_{-\infty}^{\infty}
 \Phi(2\xi-u^2)\,du,}
\]
where \(\Phi\) is the standard-normal distribution function. This integral is finite and strictly positive for every fixed real \(\xi\), and
\[
 \mathcal F(0)=\frac{2^{1/4}\Gamma(3/4)}{\sqrt\pi}.
\]
These results concern the **event-indexed reset label** and its switch probability; they do not assert an exponential law for switching in physical time.

## Assumptions and scope

Consider the Hamiltonian
\[
 H=\Omega\sum_{i=1}^{N}\sigma_i^x+
 \Delta\sum_{i=1}^{N}\sigma_i^z,
\]
with \(\Omega,\Delta,\gamma>0\), \(N\) odd, and instantaneous independent Poisson reset opportunities at rate \(\gamma\). Between resets all \(N\) spins evolve independently under this Hamiltonian. At each opportunity all spins are measured in the \(z\)-basis; if the measured number of up spins exceeds \(N/2\), the next state is all-up, otherwise all-down. For odd \(N\) no ties occur. The initial state is any one of the two reset configurations. The memory of earlier events is erased by each successful reinitialization.

The probability for a single up spin to be measured down at time \(t\) after reset equals \(p(t)=a\sin^2(\omega t)\). Conditional on \(t\), the count of flipped spins is \(\operatorname{Bin}(N,p(t))\). Thus, writing \(m=(N+1)/2\) and
\[
 B_N(p)=\Pr\{\operatorname{Bin}(N,p)\ge m\}
 =\sum_{k=m}^N\binom Nk p^k(1-p)^{N-k},
\]
the exact one-opportunity switching probability is
\[
 Q_N=\gamma\int_0^\infty e^{-\gamma t}B_N(p(t))\,dt
 =\frac{\beta}{1-e^{-\beta\pi}}
 \int_0^\pi e^{-\beta\theta}B_N(a\sin^2\theta)\,d\theta.
 \tag{1}
\]
By spin-flip symmetry the two directions have the same transition probability, so the embedded two-state Markov transition matrix is
\[
 \begin{pmatrix}1-Q_N&Q_N\\Q_N&1-Q_N\end{pmatrix}.
\]
Its nonconstant eigenvalue is \(1-2Q_N\); its event-counted mean label contrast after \(j\) opportunities is \((1-2Q_N)^j\). The classification does not rely on independence between elapsed waiting time and the direction of a flip; these are correlated at each event.

## Proof

**1. Reduction and exact binomial representation.** Because the single-spin evolution is a product and the two reset configurations are related by exchanging up and down, both label-flip probabilities equal the binomial majority tail \(B_N\) above. The waiting time is exponential with parameter \(\gamma\). Changing variables \(\theta=\omega t\) and summing successive periods of \(\sin^2\theta\) gives (1), including its geometric factor \(1/(1-e^{-\beta\pi})\).

**2. Fixed subcritical majority-tail asymptotic.** For any fixed \(0<p<1/2\), Stirling's formula at the first admissible binomial count \(m=(N+1)/2\) yields
\[
 \binom Nm p^m(1-p)^{N-m}
 \sim\sqrt{\frac2{\pi N}}\sqrt{\frac p{1-p}}
 [4p(1-p)]^{N/2}.
\]
The ratios of consecutive masses tend to \(p/(1-p)<1\). They are decreasing in their count index, so a geometric-series bound and fixed-offset convergence justify summing the tail:
\[
 B_N(p)\sim\sqrt{\frac2{\pi N}}
 \frac{\sqrt{p(1-p)}}{1-2p}
 \exp[-NI(p)],\qquad
 I(p)=-\tfrac12\log[4p(1-p)].\tag{2}
\]
The approximation is uniform on compact subintervals of \((0,1/2)\). For \(a<1/2\), the phase-dependent quantity \(p(\theta)=a\sin^2\theta\) has the unique maximum \(a\) in \([0,\pi]\), at \(\theta_0=\pi/2\). The exponent \(I(p(\theta))\) has its unique minimum at this same point, with local expansion
\[
 p(\theta_0+s)=a-a s^2+O(s^4),\qquad
 I(p(\theta_0+s))=I(a)
 +\frac{1-2a}{2(1-a)}s^2+O(s^4).
\]
Insert (2) into (1) near the maximum; on every fixed complement away from \(\theta_0\), the binomial Chernoff upper bound \(B_N(p)\le e^{-NI(p)}\) is exponentially smaller. A standard Gaussian Laplace integral at the unique minimum gives
\[
 \begin{aligned}
 Q_N&\sim\frac{\beta e^{-\beta\pi/2}}{1-e^{-\beta\pi}}
 \sqrt{\frac2{\pi N}}
 \frac{\sqrt{a(1-a)}}{1-2a}e^{-NI(a)}
 \sqrt{\frac{2\pi(1-a)}{N(1-2a)}}\\
 &=\frac{2\beta\sqrt a(1-a)}{(1-2a)^{3/2}}
 S_\beta\frac{e^{-NI(a)}}{N}.
 \end{aligned}
\]
The formula uses the **exact Bernoulli relative-entropy exponent**; replacing it with a Gaussian tail approximation away from the transition changes the rate.

**3. Critical quartic saddle.** At \(a=1/2\), put \(\theta=\pi/2+uN^{-1/4}\). Then
\[
 p(\theta)=\frac12-\frac{u^2}{2\sqrt N}+O(u^4/N),
 \qquad 2\sqrt N\,(p(\theta)-1/2)\to-u^2.
\]
The de Moivre–Laplace central limit theorem for a binomial majority count gives
\[
 B_N\bigl(p(\pi/2+uN^{-1/4})\bigr)
 \longrightarrow\Phi(-u^2)
\]
for each fixed \(u\). A bound uniformly integrable in \(u\) follows from \(B_N(p)\le\exp[-NI(p)]\) for \(p\le1/2\) and the inequality \(I(\tfrac12\sin^2\theta)\ge c\,\lvert\theta-\pi/2\rvert^4\) near \(\pi/2\), supplemented by exponentially small contributions outside a fixed neighborhood. Dominated convergence after the \(N^{-1/4}\) change of variables gives
\[
 N^{1/4}Q_N\to\beta S_\beta
 \int_{-\infty}^{\infty}\Phi(-u^2)\,du.
\]
Using Fubini's theorem on the nonnegative integrand and the standard-normal density \(\varphi\),
\[
 \int_{-\infty}^{\infty}\Phi(-u^2)\,du
 =2\int_0^\infty\sqrt t\,\varphi(t)\,dt
 =\frac{2^{1/4}\Gamma(3/4)}{\sqrt\pi}.
\]
The exponent \(1/4\) is caused by quadratic tangency of \(p(\theta)\) to the binomial majority threshold and the \(N^{-1/2}\) binomial central-limit scale.

**4. Supercritical limit.** For \(a>1/2\), the binomial law of large numbers gives \(B_N(a\sin^2\theta)\to1\) wherever \(a\sin^2\theta>1/2\), and \(0\) wherever it is smaller. The exceptional equality points have zero measure. The strict inequality holds exactly on \((\theta_a,\pi-\theta_a)\); bounded convergence in (1) evaluates the weighted interval and gives the stated positive limit.

**5. Critical window.** Fix \(\xi\in\mathbb R\) and take \(a_N=1/2+\xi/\sqrt N\). Since \(\Delta,\gamma\) are fixed, \(\beta_N=\gamma\sqrt{1-a_N}/\Delta\to\beta_c\). For fixed \(u\),
\[
 2\sqrt N\left[a_N\sin^2\left(\frac\pi2+uN^{-1/4}\right)-\frac12\right]
 \longrightarrow2\xi-u^2.
\]
The triangular-array binomial CLT therefore gives pointwise convergence of the majority tail to \(\Phi(2\xi-u^2)\). On the tails \(\lvert u\rvert>R\) with \(R^2>2\max(\xi,0)+1\), the success probability is below \(1/2\), and Chernoff's bound gives \(B_N\le C e^{-c u^4}\) for \(R<\lvert u\rvert<\epsilon N^{1/4}\), with fixed positive \(c,C\) after choosing a sufficiently small neighborhood. The remaining macroscopic phase range is exponentially negligible. The central bounded region requires only \(B_N\le1\). This yields uniformly integrable rescaled integrands and hence the asserted full scaling profile by dominated convergence. The case \(\xi=0\) recovers step 3.

The five steps establish every regime and the event-indexed spectral consequence under the stated quantifiers.

## Verification

The standalone `verify.py` evaluates the exact finite-\(N\) formula (1) with regularized incomplete beta functions and independent numerical quadrature, comparing its limits with the derived analytic coefficients. It separately integrates \(\Phi(-u^2)\) and checks its Gamma expression, tests subcritical, critical and supercritical convergence for odd \(N\) up to \(1601\), and tests three fixed critical-window coordinates. It produced `23 assertions passed`. The executable numerics support the proof but are not substitutes for its all-parameter arguments.

## Relationship to prior work

Magoni, Carollo, Perfetto and Lesanovsky (arXiv:2202.12655, first public 2022-02-25) introduce and analyze this exact noninteracting-spin model with conditional majority resetting. Their main paper identifies the thermodynamic transition at \(\Omega=\Delta\), and their fully examined supplement provides the finite-\(N\) binomial majority sum (S4), the Poisson renewal integral (S3), the equality of the two directional flip probabilities (S8), and a qualitative statement about exponentially long finite-size dynamics below threshold. Their generic Gaussian-tail estimate (S10) is not a uniform asymptotic at critical tangency. These ingredients are explicitly **prior art** and are not newly claimed.

The narrowly assessed contribution here is the *evaluated, sharp, odd-\(N\) event-flip asymptotic classification*: the entropy-corrected \(N^{-1}\) subcritical prefactor, the quartic-saddle \(N^{-1/4}\) law with exact coefficient, and the entire parameter-window profile. These are deductions from the published exact majority formula, not new physical protocols or new finite-\(N\) transition kernels. The related quantum-reset renewal framework of Perfetto, Carollo, Magoni and Lesanovsky (arXiv:2106.13761) is also acknowledged. The close relation to the precursor formulas warrants independent priority checking; published broader results may in principle yield these asymptotics through specialization.

## Limitations

The theorem applies to odd-size ensembles, identical independent spins, the stated two-state majority-reset protocol, and exponential independent reset opportunities. It is an infinite-size asymptotic at fixed physical parameters or within the specifically defined \(N^{-1/2}\) drive window. It does not determine the physical-time mixing spectrum, experimental time budgets, effects of individual-spin decoherence, finite-\(N\) uniform error constants, correlated measurements, even-\(N\) tie rules, or other reset protocols. The mathematical result has only self-review, not independent audit or external priority certification.

## References

1. M. Magoni, F. Carollo, G. Perfetto, and I. Lesanovsky, “Emergent quantum correlations and collective behavior in non-interacting quantum systems subject to stochastic resetting,” arXiv:2202.12655v1 (first public 2022-02-25), especially Protocol II and Supplemental Sections I–II, equations (S3)–(S11). https://arxiv.org/abs/2202.12655
2. G. Perfetto, F. Carollo, M. Magoni, and I. Lesanovsky, “Designing nonequilibrium states of quantum matter through stochastic resetting,” arXiv:2106.13761 (2021). https://arxiv.org/abs/2106.13761
3. F. Carollo, I. Lesanovsky, and J. P. Garrahan, “Universal and nonuniversal probability laws in Markovian open quantum dynamics subject to generalized reset processes,” arXiv:2310.06981 (2023). https://arxiv.org/abs/2310.06981
