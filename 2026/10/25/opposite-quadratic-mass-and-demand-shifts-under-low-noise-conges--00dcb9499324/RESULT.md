# Opposite quadratic mass and demand shifts under low-noise congestion choice

## Finding
Consider two resources used by a nonatomic unit population with a uniformly distributed characteristic \(x\in[0,1]\). Let \(M_\sigma\) be the resource-1 population mass and \(E_\sigma\) its characteristic-weighted demand in a logit equilibrium with Gumbel cost-shock scale \(\sigma>0\). When the cost difference depends monotonically on these two aggregates, there is an exact local asymptotic law:

\[
M_\sigma=\theta-\frac{\pi^2 B}{6D}\sigma^2+O(\sigma^4),\qquad
E_\sigma=\frac{\theta^2}{2}+\frac{\pi^2 A}{6D}\sigma^2+O(\sigma^4),
\]
where \(A\), \(B\), \(D\), and \(\theta\) are defined below. If \(B>0\), **the number of agents at resource 1 goes down while their total weighted demand goes up** under a small positive noise level. Simultaneously, the expected assignment error is only first-order in noise:

\[
\int_0^1\bigl|q_\sigma(x)-\mathbf 1_{\{x<\theta\}}\bigr|\,dx
=2\sigma\log 2+O(\sigma^3).
\]
These three asymptotics form one coupled statement about equilibrium behavior, not independent approximations.

## Assumptions and scope
The population is \([0,1]\) with uniform probability measure. Each agent selects one of two resources. The baseline costs are \(c_1(x)=x\) and \(c_2(x)=t\); a common additive constant can make all total costs nonnegative without changing behavior. For a measurable choice probability \(q:[0,1]\to[0,1]\), define

\[
M(q)=\int_0^1q(x)\,dx,\qquad E(q)=\int_0^1xq(x)\,dx.
\]
The congestion terms are \(h_1(M,E)\) and \(h_2(1-M,1/2-E)\). Each \(h_i\) is continuous on the compact feasible aggregate region, \(C^3\) on an open neighborhood of that region, finite, and nondecreasing in each own aggregate coordinate. Define

\[
\Delta(M,E)=h_1(M,E)-h_2(1-M,\tfrac12-E).
\]
In particular \(\partial_M\Delta\ge0\) and \(\partial_E\Delta\ge0\). Assume the deterministic equilibrium is interior: some \(\theta\in(0,1)\) obeys

\[
t=\theta+\Delta(\theta,\theta^2/2).
\]
The function on the right is strictly increasing in \(\theta\), so the solution is unique. In the expressions below, all derivatives of \(\Delta\) are evaluated at \((\theta,\theta^2/2)\), and

\[
A=1+\partial_M\Delta,\qquad B=\partial_E\Delta,\qquad D=A+\theta B>0.
\]
The logit convention is that the difference of two independent standard Gumbel utility shocks is logistic; a cost gap \(c_1-c_2\) induces resource-1 probability \((1+\exp((c_1-c_2)/\sigma))^{-1}\). The equilibrium \(q_\sigma\) is the self-consistent choice probability, not a single noisy realization.

## Proof
**1. Scalar reduction and uniqueness.** Set \(y=t-\Delta(M,E)\) and

\[
p_\sigma(x;y)=\frac{1}{1+\exp((x-y)/\sigma)},\qquad
m_\sigma(y)=\int_0^1p_\sigma(x;y)\,dx,\qquad
e_\sigma(y)=\int_0^1xp_\sigma(x;y)\,dx.
\]
Each moment is nondecreasing in \(y\). Hence \(G_\sigma(y)=y+\Delta(m_\sigma(y),e_\sigma(y))\) is strictly increasing and continuous, with \(G_\sigma(y)\to\pm\infty\) as \(y\to\pm\infty\), since \(\Delta\) is bounded on the feasible region. It has exactly one root \(G_\sigma(y_\sigma)=t\). Thus \(q_\sigma(x)=p_\sigma(x;y_\sigma)\) is the unique logit equilibrium for every \(\sigma>0\). The deterministic equilibrium has \(q_0=\mathbf1_{x<\theta}\), mass \(\theta\) and weighted demand \(\theta^2/2\). Local uniform convergence of the two moments to \((y,y^2/2)\) on \(0<y<1\), together with monotonicity, gives \(y_\sigma\to\theta\).

**2. Exact logistic moment expansion.** Let \(W\) be a centered standard logistic random variable with distribution function \((1+e^{-w})^{-1}\). Its variance is \(\mathbb E W^2=\pi^2/3\); this follows, for instance, by expanding its symmetric density on the positive half-line into the absolutely integrable exponential series and summing \(4\sum_{k\ge1}(-1)^{k-1}/k^2=\pi^2/3\). By Fubini, writing \([z]_0^1=\min\{1,\max\{0,z\}\}\),

\[
m_\sigma(y)=\mathbb E [y+\sigma W]_0^1,\qquad
e_\sigma(y)=\frac12\mathbb E ([y+\sigma W]_0^1)^2.
\]
On a fixed compact subinterval of \((0,1)\), logistic tails are exponentially small uniformly; since \(\mathbb E W=0\),

\[
m_\sigma(y)=y+O(e^{-c/\sigma}),\quad
e_\sigma(y)=\frac{y^2}{2}+\frac{\pi^2}{6}\sigma^2+O(e^{-c/\sigma})
\]
for some \(c>0\). Polynomial factors in discarded logistic tail expectations can be absorbed by decreasing \(c\).

**3. Feedback through congestion.** Write \(u_\sigma=y_\sigma-\theta\). Substituting the two expansions into \(G_\sigma(y_\sigma)=t\) and applying Taylor's theorem at the deterministic aggregates gives

\[
0=(A+\theta B)u_\sigma+\frac{\pi^2}{6}B\sigma^2
+O(u_\sigma^2+|u_\sigma|\sigma^2+\sigma^4).
\]
Since \(D>0\), the implicit-function estimate first yields \(u_\sigma=O(\sigma^2)\), then

\[
u_\sigma=-\frac{\pi^2 B}{6D}\sigma^2+O(\sigma^4).
\]
Consequently \(M_\sigma=m_\sigma(y_\sigma)=\theta+u_\sigma+O(e^{-c/\sigma})\), and

\[
E_\sigma=e_\sigma(y_\sigma)=\frac{\theta^2}{2}+\theta u_\sigma+\frac{\pi^2}{6}\sigma^2+O(\sigma^4),
\]
which gives both stated coefficients. Positivity of \(A\) and nonnegativity of \(B\) fix the directions.

**4. Sharp assignment norm.** Integrating the logistic probabilities on either side of \(\theta\), and extending the tails beyond \([0,1]\) at exponentially small cost, gives

\[
\int_0^1|q_\sigma(x)-q_0(x)|\,dx
=2\sigma\log\left(2\cosh\frac{y_\sigma-\theta}{2\sigma}\right)+O(e^{-c/\sigma}).
\]
Since \(y_\sigma-\theta=O(\sigma^2)\), expansion of \(\log\cosh\) yields \(2\sigma\log2+O(\sigma^3)\). The positive leading constant proves that the linear norm rate cannot be improved for this class.

**5. Genuine two-moment, non-potential witness.** Take \(h_1(M,E)=2ME\), \(h_2=0\), and \(t=5/8\). The deterministic threshold is \(\theta=1/2\), while \(A=5/4\), \(B=1\), \(D=7/4\). Therefore

\[
M_\sigma=\frac12-\frac{2\pi^2}{21}\sigma^2+O(\sigma^4),\qquad
E_\sigma=\frac18+\frac{5\pi^2}{42}\sigma^2+O(\sigma^4).
\]
This congestion dependence is not a potential functional on the continuum of assignments: the variation of the resource-1 congestion cost induced by changing the choice of type \(z\) is \(2(E+Mz)\), which is not symmetric in the affected and perturbing agent types. In particular, non-potentiality cannot be removed by replacing the demand moment with the mass alone.

## Verification
Run `python3 verify.py` from the same directory. The standalone standard-library checker numerically solves the scalar equilibrium by bisection and computes its integrals using composite Simpson quadrature with \(8192\) intervals. It checks sign conditions and asymptotic coefficients over \(27\) parameter triples and two small noise levels, plus the explicit non-potential witness at three noise levels. The checker reports **174 passed assertions**. These bounded numerical checks are corroboration, not proof for all \(\sigma\), all cost maps or all agent populations; the proof above supplies those quantifiers within its stated assumptions.

## Relationship to prior work
Dupont, Petit and Séguret (2026, arXiv:2610.18035), especially Theorems 2.1–2.2, Proposition 3.4, Section 4.3.1 and the conclusion, establish existence, uniqueness, a qualitative vanishing-noise limit and numerical convergence for much broader nonatomic congestion games. Their conclusion identifies quantitative zero-noise convergence rates as a future direction; the inspected primary text contains no corresponding coupled mass-versus-weighted-demand expansion or sharp assignment \(L^1\) constant. The present theorem is limited to two resources, a uniform scalar characteristic, one strict interior threshold and smooth monotone two-moment costs, but computes these previously unquantified effects exactly.

Koster, Verhoef, Shepherd and Watling (2014), Sections 2–5 and Appendices A–B, examine two-link probabilistic assignment with discrete traveler groups and congestion tolls, including deterministic-choice limits; their inspected calculations concern welfare and optimal pricing, not a continuous characteristic threshold with the coupled small-noise coefficients or the opposite movement of mass and weighted demand proved here.

Bagchi and Boyles (2026, arXiv:2605.21843), Sections 4–7 and Appendix A, analyze Jacobians and **algorithmic iteration convergence** for a fixed stochastic user equilibrium, not the variation of that equilibrium as Gumbel noise vanishes. The logistic second-moment coefficient is an elementary instance of the classical Sommerfeld expansion; this component alone is not asserted to be original. The new coupled coefficients require solving the endogenous aggregate feedback and yield the opposing drift phenomenon. Broader logit, traffic assignment and thermodynamic literature could contain an equivalent specialization, a remaining priority risk.

## Limitations
This is a local small-noise theorem for an interior single-threshold equilibrium. It does not extend without further proof to multiple resources, nonsmooth cost maps, nonuniform or discrete characteristic laws, nonmonotone congestion, boundary thresholds, or arbitrary noise distributions. The \(O(\sigma^4)\) errors are not asserted to be uniform across families where \(\theta\) tends to an endpoint or derivatives become unbounded. A numerical checker cannot independently audit the theoretical proof or establish publication priority.

## References
1. Alix Dupont, Quentin Petit and Adrien Séguret, *Non-Potential Congestion Games with a Continuum of Players* (2026), arXiv:2610.18035v1, https://arxiv.org/abs/2610.18035, first posted 2026-10-13 UTC.
2. Debojjal Bagchi and Stephen D. Boyles, *Spectral analysis of the logit mapping and implications for stochastic user equilibrium algorithms* (2026), arXiv:2605.21843v2, https://arxiv.org/abs/2605.21843.
3. Paul Koster, Erik T. Verhoef, Simon Shepherd and David Watling, *Probabilistic Choice and Congestion Pricing with Heterogeneous Travellers and Price-Sensitive Demand* (2014), Tinbergen Institute Discussion Paper 14-078/VIII, https://papers.tinbergen.nl/14078.pdf.
4. Classical Sommerfeld expansion for smoothed Fermi–Dirac step functions; only the elementary order-two logistic moment identity is used, and its derivation is given in the proof above.
