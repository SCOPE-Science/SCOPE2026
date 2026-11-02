# Sharp universal mutation threshold for convergence in positive-payoff multiplayer evolutionary games

## Finding

Fix an integer \(d\ge 2\). For **every** symmetric two-strategy \(d\)-player evolutionary game with strictly positive payoffs, the standard two-strategy continuous-time replicator–mutator equation with symmetric mutation probability \(q\in[0,1/2]\) has exactly one equilibrium in the strategy-frequency simplex and every trajectory converges to it whenever
\[
q\ge q_d:=\frac{d-1}{2d}.
\]
This is the **sharp payoff-independent threshold**: for each \(0<q<q_d\), some game with all payoffs strictly positive has at least three distinct interior equilibria (and therefore cannot have global convergence to a single equilibrium). The unique equilibrium above the threshold is hyperbolically attracting. The theorem makes no claim about mutation-free \(q=0\) dynamics.

## Assumptions and scope

Let \(m=d-1\) and let \(a_k,b_k>0\) for every integer \(0\le k\le m\). For strategy-A frequency \(x\in[0,1]\), the expected fitnesses are the Bernstein polynomials
\[
f_A(x)=\sum_{k=0}^m\binom{m}{k}a_k x^k(1-x)^{m-k},\quad
f_B(x)=\sum_{k=0}^m\binom{m}{k}b_k x^k(1-x)^{m-k}.
\]
Fitnesses are computed under random mixing; strategies mutate reciprocally with probability \(q\), independently of the focal state, at reproduction. The exact equation is
\[
\dot x=F_q(x)=(1-q)xf_A(x)+q(1-x)f_B(x)-x\bigl(xf_A(x)+(1-x)f_B(x)\bigr).
\]
These are mutation–selection stationary states (not necessarily Nash equilibria). The absolute level of positive payoffs is meaningful for the equation; the theorem is not about additive mutation flows or games with negative fitness.

## Proof

**1. Confinement.** Algebra gives
\[
F_q(x)=x(1-q-x)f_A(x)-(1-x)(x-q)f_B(x).
\]
At \(q\in(0,1/2)\), positivity of both fitnesses implies \(F_q(x)>0\) for \(0\le x\le q\) and \(F_q(x)<0\) for \(1-q\le x\le1\). In particular all stationary states lie in \((q,1-q)\). Because \(F_q(0)>0\) and \(F_q(1)<0\), the simplex is positively invariant and at least one such state exists.

**2. Odds comparison.** On \((q,1-q)\) write \(R(x)=f_A(x)/f_B(x)\) and
\[
G_q(x)=\frac{(1-x)(x-q)}{x(1-q-x)}.
\]
The equilibrium equation is exactly \(R(x)=G_q(x)\). For any positive Bernstein polynomial \(f_A\), define \(p_k^A(x)=\binom mk a_k x^k(1-x)^{m-k}/f_A(x)\) and \(\mu_A(x)=\sum k p_k^A(x)\). These probabilities are strictly positive for \(x\in(0,1)\); hence \(0<\mu_A(x)<m\). Define \(\mu_B\) analogously. Termwise differentiation gives
\[
\frac{d}{dx}\log R(x)=\frac{\mu_A(x)-\mu_B(x)}{x(1-x)}<\frac{m}{x(1-x)}.
\]
On the other hand exact differentiation yields
\[
x(1-x)\frac{d}{dx}\log G_q(x)
=q\left(\frac{1-x}{x-q}+\frac{x}{1-q-x}\right)
\ge\frac{2q}{1-2q}.
\]
To check the inequality without invoking convexity, put \(z=x-1/2\), \(c=1/2-q\), so that \(|z|<c\). The difference between the preceding middle expression and \(2q/(1-2q)\) is exactly
\[
\frac{4q(1-q)z^2}{(1-2q)(c^2-z^2)}\ge0.
\]
The threshold inequality \(q\ge m/[2(m+1)]\) is equivalent to \(2q/(1-2q)\ge m\). Thus \((\log G_q-\log R)'\) is **strictly positive everywhere** on \((q,1-q)\) even at the threshold. Since \(G_q(x)\to0\) as \(x\downarrow q\) and \(G_q(x)\to+\infty\) as \(x\uparrow1-q\), while \(R\) is positive and finite, there is exactly one intersection \(x_*\).

**3. Dynamics and local stability.** The factorization \(F_q=x(1-q-x)f_B(R-G_q)\) shows that \(F_q(x)>0\) below \(x_*\) and \(F_q(x)<0\) above \(x_*\); combine this with step 1 outside \((q,1-q)\). Uniqueness of solutions to this polynomial scalar ODE and monotonicity show every initial condition \(x(0)\in[0,1]\) converges to \(x_*\). At the root, the positive factor and strict log-slope inequality give \(F_q'(x_*)<0\). If \(q=1/2\), direct factorization instead gives \(F_{1/2}(x)=(1/2-x)[xf_A(x)+(1-x)f_B(x)]\), proving global attraction and negative derivative at \(x_*=1/2\).

**4. Sharpness for every lower positive mutation.** Fix \(0<q<m/[2(m+1)]\). Choose a positive parameter \(\varepsilon\in(0,1)\) and the symmetric, endpoint-favoring payoffs \(a_m=b_0=1\), \(a_k=\varepsilon\) for \(k<m\), and \(b_k=\varepsilon\) for \(k>0\). Then
\[
f_A(x)=\varepsilon+(1-\varepsilon)x^m,\quad
f_B(x)=\varepsilon+(1-\varepsilon)(1-x)^m.
\]
The point \(1/2\) is always stationary, and as \(\varepsilon\downarrow0\) its logarithmic fitness-ratio slope tends to \(4m\), whereas the mutation odds logarithmic slope there equals \(8q/(1-2q)<4m\). For all sufficiently small **strictly positive** \(\varepsilon\), the central equilibrium therefore has \(F'_q(1/2)>0\). Together with \(F_q(0)=qf_B(0)>0\) and \(F_q(1)=-qf_A(1)<0\), the intermediate value theorem gives at least one additional stationary state in each interval \((0,1/2)\) and \((1/2,1)\). Thus no smaller payoff-uniform global-uniqueness threshold is possible.

For an explicit rational instance, \(d=3\), \(q=1/4\), \(\varepsilon=1/100\) gives
\[
F_q(x)=-\frac{(2x-1)(99x^2-99x+20)}{80},
\]
so the three distinct interior equilibria are \(\tfrac12\) and \(\tfrac12\pm\sqrt{209}/66\).

## Verification

A standalone symbolic checker is in `scripts/check_threshold.py`, with requirements in `requirements.txt`. It verifies the drift and logarithmic-derivative identities exactly, and uses exact rational Sturm root counts for 144 strictly positive payoff examples at/above the proposed threshold (group sizes \(2\) through \(7\)). It also checks six strictly positive counterexample families below threshold and the explicit cubic witness. The analytic arguments above—not the finite test cases—establish the claims for all degrees and all positive payoffs.

## Relationship to prior work

Duong and Han, *On Equilibrium Properties of the Replicator–Mutator Equation in Deterministic and Random Games* (arXiv:1904.09805, first public 2019-04-22), §2.3, equations (12)–(18), study exactly this general \(d\)-player fitness and mutation model. They provide a transformed polynomial and Descartes/Sturm-derived root counting tools, and discuss Bernstein coefficients, but do not give a sharp payoff-independent mutation level ensuring one globally attracting equilibrium for **all** positive payoff vectors. Their general root-count algorithm applies to any fixed payoff choice; it does not alone imply the universal threshold or establish its optimality.

Chen, Deng, Duong and Han, *On the Number of Equilibria of the Replicator-Mutator Dynamics for Noisy Social Dilemmas* (arXiv:2303.16558, first public 2023-03-29), analyze pairwise social-dilemma payoff distributions, including nonpositive payoff entries, rather than uniform positive-payoff games of arbitrary degree. Duong and Han's related 2021 work (arXiv:2107.06025) likewise studies statistical counts in normalized pairwise games. None of these inspected results supplies both a universal \(d\)-dependent bound and sharp positive-payoff witnesses. The required positivity assumption is substantive: it supplies strict Bernstein-coefficient inequalities and prevents pathologies caused by sign-changing fitness.

## Limitations

The result concerns **two strategies**, one well-mixed infinite population, symmetric multiplicative mutation \(0\le q\le1/2\), continuous-time dynamics, and strictly positive payoff entries. It does not characterize asymmetric mutation, three or more strategies, payoff matrices with negative/zero fitness, mutation-free \(q=0\), or discrete-time replicator maps. The proof yields qualitative global attraction and local exponential relaxation but does not provide a payoff-uniform convergence rate. Equivalent universal bounds in difficult-to-index earlier literature cannot be completely excluded.

## References

1. M. H. Duong and T. A. Han, *On Equilibrium Properties of the Replicator–Mutator Equation in Deterministic and Random Games*, first public 2019-04-22, arXiv:1904.09805, https://arxiv.org/abs/1904.09805.
2. L. Chen, C. Deng, M. H. Duong, and T. A. Han, *On the Number of Equilibria of the Replicator-Mutator Dynamics for Noisy Social Dilemmas*, first public 2023-03-29, arXiv:2303.16558, https://arxiv.org/abs/2303.16558.
3. M. H. Duong and T. A. Han, *Statistics of the Number of Equilibria in Random Social Dilemma Evolutionary Games with Mutation*, arXiv:2107.06025, https://arxiv.org/abs/2107.06025.
