# Random stationary empirical density in a partially batch-reset Brownian gas

## Finding
Consider the noninteracting Brownian gas with *fixed-fraction batch resetting*. Although particles are asymptotically conditionally independent given the shared resetting clock, its stationary empirical density **does not self-average** when the reset fraction tends to an interior number. Its full random weak limit is an explicit countable mixture of Gaussian laws. Its empirical second spatial moment converges in mean square to a geometric exponential perpetuity, whose fluctuations persist at infinite particle number.

Fix \(D,r>0\) and a sequence of integers \(1\leq m_N\leq N\) with \(p_N=m_N/N\to\alpha\in(0,1)\). Write \(q=1-\alpha\). Let \(E_0,E_1,\ldots\) be independent \(\operatorname{Exp}(r)\) random variables and \(T_j=\sum_{i=0}^{j}E_i\). The random probability measure
\[
\nu=\sum_{j=0}^{\infty}\alpha q^j\,\mathcal N(0,2DT_j)
\]
is well defined almost surely. For the unique stationary distribution of the \(N\)-particle gas, let \(\mu_N=N^{-1}\sum_{i=1}^{N}\delta_{X_i}\). On a coupling with the common Poisson reset clock, \(\mu_N\) converges weakly in probability, conditional on that clock, to \(\nu\). More precisely, for every bounded continuous test function \(f\),
\[
\mathbb E[|\mu_N(f)-\nu(f)|^2\mid E_0,E_1,\ldots]\longrightarrow0
\]
for almost every clock realization; the convergence is also unconditional in \(L^2\). Consequently, the convergence is stable with respect to every bounded observable of that clock.

For the empirical cloud second moment \(M_N=\mu_N(x\mapsto x^2)\), the stronger \(L^2\) limit holds:
\[
M_N\longrightarrow M:=\int x^2\nu(dx)=2D\sum_{j=0}^{\infty}q^jE_j.
\]
The nondegenerate random limit has Laplace transform and cumulants
\[
\mathbb E e^{-tM}=\prod_{j=0}^{\infty}\bigl(1+2Dtq^j/r\bigr)^{-1},\quad t\geq0,
\qquad
\kappa_k(M)=\frac{(k-1)!(2D/r)^k}{1-q^k}\quad(k\geq1).
\]
In particular,
\[
\mathbb E M=\frac{2D}{r\alpha},\qquad
\operatorname{Var}(M)=\frac{4D^2}{r^2\alpha(2-\alpha)}>0.
\]
When the thermodynamic limit is taken first and \(\alpha\downarrow0\) second, the normalized energy \(W_\alpha=\alpha rM/(2D)\) satisfies
\[
\frac{W_\alpha-1}{\sqrt{\alpha}}\Longrightarrow\mathcal N(0,1/2).
\]
A known general small-deviation principle for geometrically weighted exponentials also takes the model-specific form
\[
\lim_{\varepsilon\downarrow0}\frac{\log\mathbb P(M\leq\varepsilon)}{[\log(1/\varepsilon)]^2}
=-\frac{1}{2|\log q|}.
\]
This last formula is included as a consequence for the gas, **not** claimed as a new abstract small-deviation theorem.

## Assumptions and scope
At each event of one rate-\(r\) Poisson clock, uniformly select exactly \(m_N\) distinct labels from \(\{1,\ldots,N\}\) independently of other events and set their positions to zero. All particles evolve between events as independent Brownian motions with generator \(D\partial_{xx}\); resetting subsets and driving Brownian motions are independent. The process is stationary, viewed at an independently fixed time. The diffusion coefficient and Poisson rate are held fixed as \(N\to\infty\). The reset proportion \(p_N\) has a fixed limit \(\alpha\in(0,1)\). The Gaussian notation \(\mathcal N(0,v)\) means the centered law of variance \(v\), including the degenerate law at \(v=0\). The second limit \(\alpha\downarrow0\) is sequential and does not claim a joint \(N,\alpha\) limit.

The stationary state exists uniquely for every \(N\): each labelled particle experiences resets at positive rate \(rp_N\), which erase its earlier trajectory; a finite collection of labels all have a reset in a sufficiently long backwards interval with probability tending to one. The independent marks and Brownian increments give the explicit coupling used below.

## Proof
**1. Common-clock representation and finite-label asymptotics.** Extend the common clock to all negative times; enumerate its backward inter-event intervals by \(E_0,E_1,\ldots\), where \(E_0\) is the stationary backward age. The most recent reset of a tagged particle is the \(j\)-th past event with probability \(p_N(1-p_N)^j\), independent of the clock lengths. Conditional on its most recent reset having age \(T_j\), the position is Gaussian with variance \(2DT_j\).

Fix \(k\) labelled particles and \(L\) most recent clock events. For each event the vector of the \(k\) selection indicators is multivariate hypergeometric. For each fixed bit pattern, its probability tends to that of independent \(\operatorname{Bernoulli}(\alpha)\) indicators because \(p_N\to\alpha\) and \(k\) is fixed. Independence across clock events yields convergence in total variation of all \(kL\) bits. The probability that at least one of the \(k\) labels had no reset among these \(L\) events is at most \(k(1-p_N)^L\). For any fixed \(\alpha>0\) it can be made uniformly small by taking \(L\) large. Thus the joint law of the \(k\) last-reset indices, conditional on the clock, tends to the product of \(k\) geometric distributions with masses \(\alpha q^j\).

Conditional on those ages, the independent Brownian drivers make the \(k\) positions independent centered Gaussians with the corresponding variances. Therefore the conditional stationary law of any fixed \(k\) distinct labels converges weakly to \(\nu^{\otimes k}\), for almost every common-clock history. This is a conditional propagation-of-chaos statement, **not** unconditional independence.

**2. Empirical-measure limit.** For bounded continuous \(f\), conditional exchangeability and the one-label convergence show \(\mathbb E[\mu_N(f)\mid\mathcal E]\to\nu(f)\). The conditional variance is
\[
\operatorname{Var}(\mu_N(f)\mid\mathcal E)=\frac1N\operatorname{Var}(f(X_1)\mid\mathcal E)
+\frac{N-1}{N}\operatorname{Cov}(f(X_1),f(X_2)\mid\mathcal E),
\]
and its right-hand side tends to zero by the two-label limit. Hence the asserted conditional mean-square convergence. Choosing a countable convergence-determining family of bounded continuous test functions proves weak convergence of the random measures: conditional tightness follows from \(\mathbb E[\mu_N(x^2)\mid\mathcal E]=2D\sum_{i\geq0}(1-p_N)^iE_i\), which is bounded in \(N\) for almost every clock, since eventually \(1-p_N\leq q_0<1\) and \(\sum_i q_0^iE_i<\infty\) almost surely. Multiplying the conditional convergence by any bounded clock-measurable random variable gives the stated stable convergence.

**3. Unbounded quadratic statistic.** A tagged particle is reset by an independently thinned Poisson clock of rate \(rp_N\), so its unconditional stationary age is \(\operatorname{Exp}(rp_N)\). Its Gaussian mixture has an eighth absolute moment bounded uniformly for sufficiently large \(N\), since \(p_N\to\alpha>0\). Consequently the pair products \(X_1^2X_2^2\) are uniformly integrable. The two-label limit with truncation then implies \(\mathbb E[X_1^2X_2^2]\to\mathbb E[M^2]\), where the limit is conditional product sampling from \(\nu\). Diagonal contributions to \(\mathbb E[M_N^2]\) are \(O(N^{-1})\), so \(\mathbb E[M_N^2]\to\mathbb E[M^2]\).

On the other hand, conditional on the clock,
\[
\mathbb E[M_N\mid\mathcal E]
=2D\sum_{j\geq0}p_N(1-p_N)^jT_j
=2D\sum_{i\geq0}(1-p_N)^iE_i.
\]
The last identity follows by nonnegative Fubini. The sum converges in \(L^2\) to \(M=2D\sum_{i\geq0}q^iE_i\), since the \(E_i\) have finite second moment and geometric bounds hold uniformly for large \(N\). Thus \(\mathbb E[M_NM]=\mathbb E[M\,\mathbb E(M_N\mid\mathcal E)]\to\mathbb E[M^2]\). Expanding \(\mathbb E|M_N-M|^2\) proves the \(L^2\) assertion.

**4. The exact fluctuation law.** The independent exponential gaps give
\(\mathbb E e^{-t(2Dq^j E_j)}=(1+2Dtq^j/r)^{-1}\). Multiplication and expansion of the logarithm at zero yield the product and cumulants. The sums converge because \(0<q<1\). The second cumulant is strictly positive, so the macroscopic cloud energy remains random. Averaging the Gaussian mixture over the clock recovers the established deterministic one-particle Laplace density \(\sqrt{r\alpha/D}\,e^{-|x|\sqrt{r\alpha/D}}/2\), which does not describe the fluctuations of the empirical density.

**5. Weak-fraction Gaussian crossover.** Put \(U_j=rE_j\), independent unit exponentials. Then \(W_\alpha=\sum_{j\geq0}\alpha q^jU_j\), \(\mathbb EW_\alpha=1\), and \(\operatorname{Var}(W_\alpha)=\alpha/(2-\alpha)\). In the triangular array for \((W_\alpha-1)/\sqrt\alpha\), the largest coefficient is \(\sqrt\alpha\to0\), and the total variance tends to \(1/2\). Exponential tails establish Lindeberg's condition by dominated exponential moments, so the triangular-array central limit theorem gives the stated Gaussian limit.

**6. Optional small-ball corollary.** Set \(a=|\log q|\). An elementary comparison of the logarithm of the product with \(\sum_{j\geq0}(\log t-aj)_+\) shows \(-\log\mathbb E e^{-tM}=(\log t)^2/(2a)+O(\log t)\) for large \(t\). Markov's bound for \(e^{-tM}\) with \(t=1/\varepsilon\) yields the requisite upper probability estimate. For a lower bound, let \(n=(\log(1/\varepsilon))/a+O_\alpha(1)\), with the additive constant chosen so that the expected weighted-exponential tail after index \(n\) is at most \(\varepsilon/4\). Require each of the first \(n\) terms to be at most \(\varepsilon/(2n)\), and use Markov's inequality to make the independent remaining tail at most \(\varepsilon/2\) with probability at least \(1/2\). Multiplication of the first \(n\) exponential small-value probabilities gives logarithm \(-[\log(1/\varepsilon)]^2/(2a)+O(\log(1/\varepsilon)\log\log(1/\varepsilon))\). This proves the displayed coefficient, consistently with established geometric small-deviation theory.

## Verification
The standalone `verify.py` uses only the Python standard library and checks 80 deterministic and seeded-simulation comparison groups. In particular, it checks the exact finite-\(N\) pair covariance against the formula in the motivating paper, its thermodynamic value against \(\operatorname{Var}(M)\), the geometric cumulants, the renewal identity for the product Laplace transform, exponential asymptotic scaling, and weak-fraction cumulants. Numerical checks are supporting evidence only; the infinite-particle, Gaussian and small-ball limits are proved above.

## Relationship to prior work
De Mauro, Majumdar and Schehr (arXiv:2601.20077, 2026) introduced this batch-reset Brownian model, its exact marginal hierarchy, stationary one- and two-particle distributions, connected density-density covariance, and spectral form factor. Those components are prior work. The distinction here is the **complete random thermodynamic empirical-measure limit conditional on the common clock**, and the resulting explicit non-self-averaging cloud energy and sequential Gaussian crossover. Pair information alone does not specify the whole limiting random measure.

Bressloff (arXiv:2401.03501, 2024) studied local independent versus fully synchronized Poisson resetting through global density equations and established persistent common-shot-noise effects for the fully synchronized case. De Mauro and coauthors (arXiv:2509.06658, 2025) studied conditionally independent structure for fully simultaneous resetting with general renewal clocks. Neither model treats uniformly resampled interior fixed-fraction reset subsets at each clock event. The geometric exponential sum and its generic small-ball asymptotic belong to established weighted-series theory; compare Aurzada (arXiv:0711.2576, 2007/2008). No abstract geometric-series novelty is claimed.

## Limitations
The theorem fixes an interior reset fraction \(0<\alpha<1\) before taking \(N\to\infty\). The second Gaussian limit is sequential. It does not establish a joint limit with \(\alpha_N\to0\), any temporal measure-valued process limit, interactions, state-dependent resetting, or a quantitative finite-\(N\) convergence rate. The mathematical priorities of general common-environment propagation-of-chaos theorems and geometric perpetuity theory remain relevant; the claimed new result is this model's precise limit, not those general methodologies. Independent assessment has not been performed.

## References
1. G. de Mauro, S. N. Majumdar and G. Schehr, *Tuning the strength of emergent correlations in a Brownian gas via batch resetting*, arXiv:2601.20077v1 (first public 2026-01-27); complete revision v3 and supplemental sections S8–S9 consulted, https://arxiv.org/html/2601.20077v3 .
2. P. C. Bressloff, *Global density equations for interacting particle systems with stochastic resetting: from overdamped Brownian motion to phase synchronization*, arXiv:2401.03501, https://arxiv.org/abs/2401.03501 .
3. G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658, https://arxiv.org/abs/2509.06658 .
4. F. Aurzada, *A short note on small deviations of sequences of i.i.d. random variables with exponentially decreasing weights*, arXiv:0711.2576, https://arxiv.org/abs/0711.2576 .
