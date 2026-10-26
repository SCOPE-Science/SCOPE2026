# Fixed long-run abundance with strictly accelerated fixation turnover in nonlinear public-goods games

## Finding
Consider the well-mixed, finite-population public-goods game defined below, with Fermi pairwise comparison at any **positive finite** selection intensity. Keeping the full-cooperation return fixed while increasing **any one** partially cooperative return strictly increases **both** opposite-direction single-mutant fixation probabilities. Nevertheless their ratio, and hence the stationary proportion of the two homogeneous states in the rare-mutation reduction, remains exactly unchanged. The relaxation rate of that reduction therefore strictly increases.

The result is global in the returns and intensity, not a weak-selection expansion. Moreover, for each fixed group size \(n\ge3\), there are strictly positive return schedules with exactly half of the stationary mass in each homogeneous state but an exponentially small relaxation rate as the population grows. The sharp logarithmic exponent is established below. These conclusions concern **switching between homogeneous states** in the rare-mutation reduction, not the mean absorption time within a polymorphic population at a fixed nonzero mutation rate.

## Assumptions and scope
Take integers \(N>n\ge3\), contribution cost \(c>0\), selection intensity \(\delta>0\), and nonnegative group multipliers \(r_1,\ldots,r_n\). A uniformly sampled group of \(n\) individuals with \(j\) cooperators gives each member benefit \(c j r_j/n\); each cooperator additionally pays \(c\). Individuals update by the Fermi pairwise comparison process with mean payoffs from sampling without replacement. In the absence of mutation, the counts \(0\) and \(N\) of cooperators are absorbing. Denote by \(\rho_C\) the probability that a single cooperator fixes among defectors, and by \(\rho_D\) the probability that a single defector fixes among cooperators.

Write \(\Delta_i=P_C(i)-P_D(i)\), for \(1\le i\le N-1\), and \(B_k=\sum_{i=1}^{k}\Delta_i\), with \(B_0=0\). The convention \(\binom ab=0\) when \(b<0\) or \(b>a\) applies throughout. Let \(\mu>0\) be a common, sufficiently small mutation-attempt factor in the *reduced* two-state chain, with transition probabilities \(\mu\rho_C\) and \(\mu\rho_D\). This reduction is a limiting description as the physical mutation rate tends to zero, and is not asserted to be exact for an arbitrary positive mutation rate.

## Proof
**1. Cumulative payoff kernel.** At cooperator count \(i\), conditional focal-group probabilities yield
\[
\Delta_i=-c+\frac{c}{n\binom{N-1}{n-1}}\sum_{j=1}^{n}j r_j
\left[\binom{i-1}{j-1}\binom{N-i}{n-j}-\binom{i}{j}\binom{N-i-1}{n-j-1}\right].
\]
For each fixed \(j\), the bracket equals \(F_i-F_{i-1}\), where \(F_i=\binom{i}{j}\binom{N-i-1}{n-j}\). This follows twice from Pascal's identity and remains valid at the boundary using the zero-binomial convention. Telescoping gives the **exact kernel**
\[
\boxed{B_k=-ck+\frac{c}{n\binom{N-1}{n-1}}\sum_{j=1}^{n}j r_j\binom{k}{j}\binom{N-k-1}{n-j}},\qquad 0\le k\le N-1.
\]
In particular, every derivative in a partially cooperative return is nonnegative,
\[
\frac{\partial B_k}{\partial r_j}=\frac{cj}{n\binom{N-1}{n-1}}\binom{k}{j}\binom{N-k-1}{n-j}\ge0\quad(1\le j<n),
\]
and it is strictly positive for at least \(k=j\). For \(k=N-1\), all mixed-return terms vanish and
\[
S:=B_{N-1}=c\left[\frac{N-n}{n}r_n-(N-1)\right].
\]

**2. Exact fixation formulas and monotonicity.** The Fermi transition ratio at state \(i\) is \(T_i^-/T_i^+=e^{-\delta\Delta_i}\). The standard first-step recurrence for the absorbing birth–death chain then gives
\[
\rho_C=\left(\sum_{k=0}^{N-1}e^{-\delta B_k}\right)^{-1},\qquad
\rho_D=e^{-\delta S}\rho_C.
\]
The second identity follows also by applying the same recurrence to the reversed count of defectors. Consequently,
\[
\boxed{\frac{\rho_C}{\rho_C+\rho_D}=\frac{1}{1+e^{-\delta S}}.}
\]
This ratio identity is a consequence of classical two-type fixation theory combined with the already known terminal-payoff cancellation; it is used here, rather than represented as the independent novelty claim. For each \(j<n\), differentiating the first fixation formula and using the positive kernel from step 1 shows
\[
\frac{\partial\rho_C}{\partial r_j}=\frac{\delta cj\,\rho_C^2}{n\binom{N-1}{n-1}}
\sum_{k=1}^{N-2}e^{-\delta B_k}\binom{k}{j}\binom{N-k-1}{n-j}>0.
\]
Because \(S\) is independent of the mixed returns, also \(\partial\rho_D/\partial r_j=e^{-\delta S}\partial\rho_C/\partial r_j>0\). This proves strict simultaneous fixation-rate monotonicity for all finite \(\delta>0\), despite the fact that a given \(\Delta_i\) need not be monotone in \(r_j\).

**3. Sharp switching-rate range.** The homogeneous-state reduction has transition matrix
\[
\begin{pmatrix}1-\mu\rho_C&\mu\rho_C\\ \mu\rho_D&1-\mu\rho_D\end{pmatrix}
\]
when states are ordered (all defectors, all cooperators). Its nontrivial spectral gap is
\[
\lambda=\mu(\rho_C+\rho_D).
\]
At fixed \(r_n\), this is strictly increasing in each \(r_j\), \(j<n\). Among all nonnegative mixed returns its minimum is obtained at \(r_1=\cdots=r_{n-1}=0\); if strictly positive returns are required, the same value is the unattained infimum. For every \(1\le k\le N-2\), at least one coefficient of a mixed return in \(B_k\) is positive. Thus when **all** mixed returns tend to infinity, \(B_k\to\infty\) for these \(k\), but \(B_0=0\) and \(B_{N-1}=S\) stay fixed. Hence
\[
\lim\rho_C=\frac1{1+e^{-\delta S}},\qquad \lim\rho_D=\frac{e^{-\delta S}}{1+e^{-\delta S}},\qquad
\boxed{\sup\lambda=\mu}.
\]
The supremum is not attained at finite returns because the other exponential terms are strictly positive.

**4. Exponentially separated switching rates at identical stationary abundance.** Fix once and for all an interaction size \(n\ge3\), \(\delta,c>0\), and any constant \(\varepsilon\) with \(0<\varepsilon<n\). Let \(N\to\infty\) through integers \(N>n\) and choose
\[
r_1=\cdots=r_{n-1}=\varepsilon,\qquad r_n=\frac{n(N-1)}{N-n}.
\]
All returns are strictly positive and \(S=0\), so \(\rho_C=\rho_D\) and the two homogeneous states each have stationary probability \(1/2\). Set \(q_N=(N-n)/(n(N-1))\) and let \((z)_{\underline m}=z(z-1)\cdots(z-m+1)\). Vandermonde's identity reduces the exact kernel to
\[
B_k=-c(1-\varepsilon q_N)\left[k-\frac{(k)_{\underline n}}{(N-2)_{\underline{n-1}}}\right],\quad 0\le k<N.
\]
Uniformly for \(k/N\in[0,1]\), the bracket divided by \(N\) tends to \(x-x^n\). Its maximum is attained at \(x_*=n^{-1/(n-1)}\), with value \(\kappa_n=(1-1/n)n^{-1/(n-1)}>0\). Since the fixation denominator is a sum of \(N\) positive exponentials, it lies between its largest term and \(N\) times that term. Applying these bounds gives the **exact exponential rate**
\[
\boxed{\lim_{N\to\infty}\frac1N\log\frac{\mu}{\lambda_N}
=\delta c\left(1-\frac{\varepsilon}{n}\right)\left(1-\frac1n\right)n^{-1/(n-1)}.}
\]
For every fixed \(N\), by contrast, increasing all intermediate returns without changing \(r_n\) makes \(\lambda_N/\mu\to1\) by step 3, while the stationary split remains \(1/2\) throughout. This constructs an exponentially strong finite-population separation between stationary composition and the rate of rare-mutant substitutions.

## Verification
Run `python verify.py` from the extracted package directory. It uses only Python's standard library, independently forms both focal hypergeometric payoff sums, checks the exact cumulative kernel and its coefficients over finite parameter families, verifies reverse-mutant fixation through a separate reversed-chain sum, and checks strict switching-rate inequalities and the exponential asymptotic numerically. The program reports the total assertions. All general statements above are proven analytically; the finite checks do not establish the universal quantifiers or the asymptotic limit.

## Relationship to prior work
Wang, Liu, Chen and Szolnoki (2026) introduced general composition-dependent public-goods returns and proved the terminal-payoff cancellation at weak selection, including the exact summed-payoff identity used in step 1 at \(k=N-1\). Hauert and McAvoy (2024) derived general fixation formulas and studied a linearly varying return schedule; their weak-selection formulas show a joint effect of their endpoint return parameter on both fixation probabilities. Traulsen, Nowak and Pacheco (2006) established the general all-selection Fermi fixation framework, especially for pair games. Fudenberg and Imhof (2006) gave the rare-mutation homogeneous-state reduction.

The present contribution is the **partial-sum hypergeometric positivity law for every intermediate multiplier**, which implies exact, simultaneous *strict* fixation monotonicity at all finite positive intensities, the sharp attainable/supremal switching-rate range, and the explicit positive-return exponential separation at fixed long-run abundance for each \(n\ge3\). The terminal-cancellation formula and the general birth–death ratio are expressly prior ingredients. In the inspected sources, the strong joint monotonicity and exponential separation are not stated, and neither follows from the weak-selection endpoint statements alone without further analysis of partial sums.

## Limitations
The exact results depend on uniform sampling without replacement, expected-payoff Fermi comparison, two strategies, and the rare-mutation homogeneous-state reduction. They need not extend to nonlinear mappings other than Fermi, heterogeneous networks, three or more strategies, or finite mutation regimes in which transient polymorphic populations carry significant stationary mass. The reduced-chain spectral gap measures substitution mixing *in the limiting two-state description*; it is not a claim about fixation duration or the spectral gap of the full finite-mutation population chain. The large-population asymptotic first forms this reduction for each \(N\), and any physical joint limit must choose mutation rates sufficiently small for that approximation. The all-selection stationarity formula itself is implied by earlier generic fixation identities plus the 2026 terminal cancellation; originality is claimed for the monotonicity and exponential switching separation. Historical-priority risk persists for related results formulated in other payoff variables.

## References
1. Q. Wang, Y. Liu, X. Chen and A. Szolnoki, *Evolutionary dynamics in public goods games with general frequency-dependent returns* (2026), arXiv:2607.16809, https://arxiv.org/abs/2607.16809 (first submitted July 18, 2026). Section 2 and Appendix B.
2. C. Hauert and A. McAvoy, *Frequency-dependent returns in nonlinear public goods games*, Journal of the Royal Society Interface 21 (2024), 20240334, https://doi.org/10.1098/rsif.2024.0334, especially Sections 4.1–4.2.
3. A. Traulsen, M. A. Nowak and J. M. Pacheco, *Stochastic dynamics of invasion and fixation*, Physical Review E 74 (2006), 011909, https://arxiv.org/abs/q-bio/0609020, especially the Fermi transition and fixation formulas.
4. D. Fudenberg and L. A. Imhof, *Imitation processes with small mutations*, Journal of Economic Theory 131 (2006), 251–262, https://doi.org/10.1016/j.jet.2005.04.006.
