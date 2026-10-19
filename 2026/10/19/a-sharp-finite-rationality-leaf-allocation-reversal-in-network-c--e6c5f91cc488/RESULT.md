# A sharp finite-rationality leaf-allocation reversal in network coordination

## Finding

Consider a graph-based binary coordination game with homogeneous log-linear updates and stationary rationality \(\beta>0\). Attach a prescribed number \(L\) of new leaves to either of two designated vertices of any connected simple core graph. The stationary probability of unanimous coordination is maximized by exactly the integers nearest to an explicit pinned-partition center; in particular, an exact four-leaf example changes its optimal topology at a unique positive rationality threshold. The higher-rationality optimum has a strictly larger degree-square sum than the lower-rationality optimum.

**General two-anchor theorem.** Fix a connected finite simple core graph \(H\), distinct core vertices \(a,b\), an integer \(L\geq1\), \(\beta>0\), and \(0<\theta<1\). For each integer \(0\leq s\leq L\), attach \(s\) labeled new leaves to \(a\) and the remaining \(L-s\) to \(b\). Define
\[
 u=e^{\beta\theta},\quad v=e^{\beta(1-\theta)},\quad A=1+u,\quad B=1+v.
\]
For \(i,j\in\{0,1\}\), let \(C_{ij}>0\) be the sum of core Gibbs weights over strategy profiles with \(x_a=i\) and \(x_b=j\), using factor \(u\) on each \(00\) edge, factor \(v\) on each \(11\) edge, and factor \(1\) on each discordant edge. The exact whole-graph partition function is
\[
 Z_s=C_{00}A^L+C_{11}B^L+C_{01}A^sB^{L-s}+C_{10}B^sA^{L-s}.
\]
When \(\theta\ne1/2\), put
\[
 s_* =\frac L2+\frac{\log(C_{10}/C_{01})}{2\log(A/B)}.
\]
The maximizers of either unanimous-state probability, and therefore of their sum, are precisely those integers \(s\in\{0,\ldots,L\}\) minimizing \(|s-s_*|\). At most two maximizers occur, and two are tied exactly if the relevant center lies at a half-integer between two feasible integers. At \(\theta=1/2\), all \(L+1\) allocations have exactly the same stationary unanimity probability, for all \(\beta>0\) and every core \(H\).

**Sharp rationality-induced reversal.** Take the four-vertex *paw* core with triangle \(1,2,3\) and pendant edge \(0,3\), let \(a=3\) (degree three), \(b=0\) (degree one), \(L=4\) and \(\theta=1/3\). Write \(t=e^{\beta/3}>1\). Then the unique optimum is \(s=1\) for \(1<t<t_*\), the unique optimum is \(s=0\) for \(t>t_*\), and exactly \(s=0,1\) are tied at \(t=t_*\), where \(t_*\in(2,3)\) is the unique root above one of
\[
 Q(t)=2t^6-2t^4-9t^3-5t^2-3t+1.
\]
Numerically \(t_*=2.00523666090993\ldots\) and \(\beta_*=3\log t_*=2.08728626747836\ldots\). The \(s=1\) graph has degree-square sum \(44\), but the optimal \(s=0\) graph at larger rationality has degree-square sum \(46\). These are the only admissible designs being compared: no global optimality claim over arbitrary graphs is made.

## Assumptions and scope

Every vertex \(i\) chooses \(x_i\in\{0,1\}\) and receives
\[
 U_i(x)=x_i\left(\sum_{j\sim i}x_j-\theta\deg(i)\right).
\]
One uniformly selected vertex updates at each step via a logit choice conditional on its neighbors' current choices, using the same inverse-temperature/rationality \(\beta\). Since \(0<\beta<\infty\), the finite Markov chain is irreducible and aperiodic and admits a unique stationary measure proportional to \(e^{\beta\Phi(x)}\) for the exact potential
\[
 \Phi(x)=\sum_{\{i,j\}\in E}\left(x_ix_j-\theta(x_i+x_j)+\theta\right).
\]
This normalization gives edge Boltzmann factors \(u,v,1\) on \(00,11,01\) edges, respectively. The result concerns the stationary probability of the all-zero profile, the all-one profile, or their union, not transient learning times, mixing rates, or the expected payoff. All graphs are simple, undirected, and connected, and the leaf budget is fixed. The labels of leaves do not change partition functions.

## Proof

The edge potential has unilateral difference \(\Phi(1,x_{-i})-\Phi(0,x_{-i})=\sum_{j\sim i}x_j-\theta\deg(i)\), precisely the player's unilateral payoff difference. This proves the Gibbs representation from detailed balance for asynchronous logit updates.

Condition on the strategies at the core. Summing over a leaf adjoining a core vertex in state zero contributes \(1+u=A\): the leaf choices have edge factors \(u\) and \(1\). A leaf joining a core vertex in state one contributes \(1+v=B\). Multiplying independent leaf contributions and summing the four classes of core states yields the displayed \(Z_s\). For every \(s\), the graph has exactly \(|E(H)|+L\) edges, so the stationary all-zero probability is \(u^{|E(H)|+L}/Z_s\), and the stationary all-one probability is \(v^{|E(H)|+L}/Z_s\). Consequently, optimizing either unanimity event (or their union) is exactly minimizing \(Z_s\).

If \(\theta=1/2\), then \(u=v\) and hence \(A=B\); the formula shows that \(Z_s\) is constant. Otherwise, since \(A\ne B\), direct algebra gives
\[
 Z_s=C_{00}A^L+C_{11}B^L+2\sqrt{C_{01}C_{10}}(AB)^{L/2}\cosh\!\left(\log(A/B)(s-s_*)\right).
\]
All coefficients are strictly positive. Since \(\cosh\) is strictly increasing in the absolute value of its argument on the nonnegative half-line, the admissible integer minimizers are exactly the nearest integers to \(s_*\), including endpoint clamping and the possible two-way half-integer tie. This also establishes uniqueness of the real minimum and rules out omitted interior candidates.

For the paw, write \(T_0=C_{01}\) and \(T_1=C_{10}\). Direct enumeration over the two non-pinned triangle vertices gives
\[
 T_0=t^3+t^2+2t,\qquad T_1=t^6+2t^2+t,
\]
\[
 C_{00}=tT_0,\qquad C_{11}=t^2T_1.
\]
The following exact factorizations hold for every real \(t\):
\[
 T_1(1+t)^2-T_0(1+t^2)^2
 =t(t-1)^2(t^2+t+1)(t^3+2t^2+2t-1),
\]
\[
 T_1(1+t)^4-T_0(1+t^2)^4
 =-t(t-1)(t^9+t^8+3t^7+t^6+11t^5+14t^4+21t^3+9t^2+4t-1).
\]
For \(t>1\), their signs are respectively positive and negative (each parenthetical polynomial displayed has positive value at one and positive coefficients except for its constant). As \(A=1+t<B=1+t^2\), these inequalities imply \(0<s_*<1\). Only \(s=0\) and \(s=1\) can therefore minimize \(Z_s\). Their difference factors exactly as
\[
 Z_0-Z_1=-t^2(t-1)^2Q(t),\quad
 Q(t)=2t^6-2t^4-9t^3-5t^2-3t+1.
\]
The coefficient sequence of \(Q\) has exactly two sign changes, so Descartes' rule gives at most two positive roots counted with multiplicity. Since \(Q(0)=1>0\), \(Q(1)=-16<0\), and \(Q(2)=-1<0<Q(3)\), there is one positive root in \((0,1)\) and one in \((2,3)\), hence no others. The signs on \((1,t_*)\) and \((t_*,\infty)\) follow. The \(s=1\) graph has degree sequence \((4,4,2,2,1,1,1,1)\); the \(s=0\) graph has \((5,3,2,2,1,1,1,1)\). Their degree-square sums are \(44\) and \(46\), respectively. This proves the entire sharp classification and reversal.

## Verification

The independently runnable standard-library script `check.py` enumerates every binary profile on each test graph with exact rational weights. It compares brute-force partition sums against the conditional-core formula for paw budgets \(L=1,\ldots,5\) and \(t\in\{3/2,2,3,4\}\), and checks a distinct five-core-vertex graph, all paw pinned coefficients, and the exact factorization \(Z_0-Z_1=-t^2(t-1)^2Q(t)\). Its 88 partition comparisons and further rational identities pass. The analytic factorizations, convexity, Descartes root count, and Gibbs detailed balance constitute the infinite-parameter proof; finite checks do not replace them.

## Relationship to prior work

Wang, Akyol, and Vasconcelos (2026) study network design for log-linear coordination and provide a degree-regularity sufficient condition for optimality at sufficiently low rationality and a general graph-theoretic lower bound at arbitrary rationality. Their theorem is not an exact optimization of this two-anchor leaf budget for every rationality, nor does it state this rationality-induced reversal. The present result is a sharp constrained-design comparison for stationary coordination. The method of minimizing a positive exponential sum by a hyperbolic-cosine center is elementary convexity; the contribution is its conditional-core representation with a verified, nontrivial topology switch. Standard spin-system partition-function comparison literature can provide wider techniques; full independence from every earlier graph-specific theorem has not been externally established.

## Limitations

No optimality is claimed among graph structures outside the fixed core and two-anchor leaf relocation family. The rationality threshold is derived for the specified paw core and \(\theta=1/3\), not for all payoff parameters. Unanimity probability is an equilibrium statistical quantity, not speed or probability of finite-time convergence, and physical dynamic interpretation requires the log-linear updating assumptions. Mathematical validity is supported by an analytic proof and self-review, but no independent scientific audit or exhaustive historical-priority search was performed.

## References

1. Z. Wang, E. Akyol, M. M. Vasconcelos, *Learning to Coordinate over Networks with Bounded Rationality* (2026), arXiv:2604.07751v1, first posted 2026-04-09; https://arxiv.org/abs/2604.07751 .
2. D. Galvin, *Bounding the partition function of spin-systems* (2006; arXiv posting 2012), general comparison techniques for finite-graph spin partition functions; https://arxiv.org/abs/1206.3200 .
