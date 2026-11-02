# Four-state threshold for finite-rate optimal resetting beside an absorbing target

## Finding

Consider continuous-time nearest-neighbour motion on a finite weighted graph, absorbed at a target \(o\) and independently returned to its starting vertex \(x\) at Poisson rate \(r\). Although homogeneous lattice motion started next to the target favors arbitrarily fast resetting, the smallest undirected weighted graph exhibiting a **strict optimal finite positive resetting rate** has four vertices. Specifically, four vertices suffice; at most three vertices, even with directed asymmetric jump rates, never suffice if \(x\) has a direct positive-rate edge to \(o\).

Let \(M(r)=\mathbb E_x T_r\). On the four-vertex undirected weighted graph with vertices \(\{o,x,y,z\}\), jump rates (in both directions) \(q_{xo}=1\), \(q_{xy}=1\), \(q_{yo}=3\), and \(q_{xz}=1\), and no other edges, the exact mean is
\[
M(r)=\frac{r^2+7r+9}{r^2+8r+7},\qquad r\geq0.
\]
Its unique positive critical point is the strict global minimizer
\[
r_*=2+3\sqrt3,\qquad M(r_*)=\frac23+\frac{\sqrt3}{6}<1=\lim_{r\to\infty}M(r).
\]
By contrast, the at-most-three-vertex obstruction is exact for all nonnegative directed jump rates with direct target rate \(a=q_{xo}>0\). A complementary graph-independent sufficient criterion states that if \(q_{vo}\leq a\) for every non-target vertex \(v\), then
\[
\Pr_x(T_r>t)\ge e^{-at},\qquad M(r)\ge\frac1a\quad(r,t\ge0),
\]
and \(M(r)\to1/a\) as \(r\to\infty\). Thus arbitrarily rapid resetting is globally optimal whenever the restart vertex has the greatest direct target hazard.

## Assumptions and scope

The underlying state space is a finite graph. The particle waits an exponential holding time determined by the sum of outgoing positive jump rates \(q_{uv}\ge0\), then follows the corresponding directed edge. The distinguished target \(o\) is absorbing; the starting/reset vertex \(x\ne o\) has a direct edge rate \(a=q_{xo}>0\). At an independent Poisson event of rate \(r\), a living particle is instantaneously placed at \(x\); this does not alter the jump clocks or the absorbing target. An event while already at \(x\) has no physical effect. \(T_r\) is the first entrance time into \(o\), with \(r\ge0\). Any finite graph containing a direct positive-rate edge to \(o\) has finite \(M(r)\) for positive \(r\); in the four-vertex witness this also holds at \(r=0\). The hazard comparison applies to all such finite graphs, including asymmetric directed graphs. The state-count obstruction applies to graphs with at most three states *including the absorbing target*.

## Proof

**Hazard domination and the high-reset limit.** For the nonabsorbing auxiliary walk, let \(h(v)=q_{vo}\) for every non-target vertex. Conditional on its entire nonabsorbing/reset trajectory, absorption can be implemented by an independent inhomogeneous killing clock with instantaneous rate \(h(X_t)\). Consequently,
\[
\Pr_x(T_r>t)=\mathbb E_x\exp\left(-\int_0^t h(X_s)\,ds\right).
\]
If \(h(v)\le a\) everywhere, the integrand is at least \(e^{-at}\), proving survival and mean lower bounds. The unreset absorption-time Laplace transform \(f(s)=\mathbb E_x e^{-sT_0}\) satisfies \(f(s)=a/s+O(s^{-2})\) as \(s\to\infty\): this follows directly from the finite-state killed generator resolvent \(f(s)=1-s[(sI-K)^{-1}\mathbf1]_x\) and its Neumann expansion, since the first jump-to-target rate from \(x\) is \(a\). The renewal identity for independent exponential restarting is
\[
M(r)=\frac{1-f(r)}{r f(r)}\qquad(r>0),
\]
which implies \(M(r)\to1/a\). This limit also follows directly from the reset-modified backward equations, whose leading large-\(r\) balance at \(x\) leaves the direct target hazard \(a\).

**Two- and three-vertex obstruction.** For two vertices \(\{x,o\}\), \(T_r\) is exponential with rate \(a\) regardless of resets. For three vertices \(\{x,y,o\}\), write the only possible positive directed rates as \(q_{xo}=a>0\), \(q_{xy}=b\ge0\), \(q_{yo}=c\ge0\), and \(q_{yx}=d\ge0\). The reset backward equations, for \(r>0\), read
\[
(a+b)m_x-bm_y=1,\qquad -(r+d)m_x+(r+c+d)m_y=1.
\]
Solving gives
\[
M(r)=m_x=\frac{r+b+c+d}{ar+a(c+d)+bc},\qquad
M'(r)=\frac{b(c-a)}{[ar+a(c+d)+bc]^2}.
\]
The derivative has one fixed sign, or vanishes identically, throughout \((0,\infty)\). Thus an isolated strict interior minimizer is impossible, even for directed transitions. The single-edge degenerate cases follow from the same formula (or its trivial limit). Here \(M(0)\) may be infinite if an unreset trap is reachable; this does not affect the interior obstruction.

**Four-vertex witness and unique optimum.** Order transient states as \((x,y,z)\) and take unit, unit, triple, unit edge rates as specified above. Under resetting the exact backward equations are
\[
3m_x-m_y-m_z=1,\qquad
-(r+1)m_x+(r+4)m_y=1,\qquad
-(r+1)m_x+(r+1)m_z=1.
\]
Eliminating \(m_y,m_z\) gives the displayed rational function for \(M(r)=m_x\). Its derivative is
\[
M'(r)=\frac{r^2-4r-23}{(r^2+8r+7)^2}.
\]
The denominator is strictly positive on \([0,\infty)\). The numerator has exactly one positive zero \(2+3\sqrt3\), with the derivative strictly negative before and positive after it. Substitution yields \(M(r_*)=2/3+\sqrt3/6\), while \(M(0)=9/7\) and \(M(\infty)=1\). Therefore this is a strict global minimum, not just a local minimum. Combining this construction with the at-most-three-vertex obstruction proves that **four is the sharp minimal state count** within the stated finite weighted graph class.

**Structural explanation.** The source \(x\) can jump directly to target at rate one, but its competing excursions reach the high-absorption vertex \(y\) (target hazard three) or the dead-end \(z\) (target hazard zero). Restarting helps recover from \(z\) but suppresses productive occupation of \(y\). This competition creates the strictly finite optimum. The hazard-maximality criterion fails precisely because \(q_{yo}=3>q_{xo}=1\). The derivative signs near zero and infinity are strict, so a small perturbation of the four positive edge weights retains at least one finite optimal resetting rate; thus the phenomenon is not a zero-width parameter accident.

## Verification

The independent standard-library Python program `verify.py` solves the backward equations using exact rational Gaussian elimination, enumerates three-vertex directed-rate families, checks the rational four-vertex formula at 101 rates, independently tests the renewal/resolvent identity, checks its derivative polynomial, and samples all eligible weighted four-vertex graphs with edge weights in \(\{0,1,2\}\) against the hazard lower bound. It executes as `python3 verify.py` and reports `PASS: 1559 independent rational and root checks`. Floating-point tests are used only for the radical value of the root and its minimum; all rational identities are tested exactly. The universal conclusions follow from the analytic argument above, not from these finite enumerations.

## Relationship to prior work

Hartmann and Majumdar, *Diffusion with stochastic resetting on a lattice* (first made public May 26, 2025, arXiv:2505.19903v1), prove that homogeneous hypercubic lattice walks started adjacent to a target have a monotonically decreasing mean search time as the reset rate increases. Their general renewal identity and simple finite-state explanatory model are known ingredients, not claimed here. The present statement concerns arbitrary weighted finite graphs and separates a robust high-reset optimality condition from the sharp four-state counterexample.

Riascos, Boyer, Herringer and Mateos (arXiv:1910.13568) give general network resetting and first-passage formulas for discrete-time walks; Chen, Li and Huang (arXiv:2111.01330) give general fundamental-matrix methods for discrete-time absorbing chains. Such methods can be specialized to compute a fixed example. The assessed contribution is the **sharp state-count obstruction together with a concrete minimal undirected witness and the all-graph hazard criterion**, not the existence of a renewal or resolvent formula. No independence or comprehensive literature priority is claimed.

## Limitations

The construction uses freely weighted edge rates. It does not claim that equal-rate or regular graphs can have this finite optimum from a nearest neighbour; the motivating homogeneous-lattice result remains intact. The general hazard criterion is sufficient but not necessary; it guarantees global optimality of the infinite-rate limit but not monotonicity in reset rate. The three-state classification assumes a direct positive target jump from the reset state. The analysis concerns means and survival bounds, not arbitrary first-passage quantiles. Non-Poisson resetting and non-Markovian transport are not covered. Originality is assessed against inspected sources and available records, and still requires independent literature validation.

## References

1. A. K. Hartmann and S. N. Majumdar, *Diffusion with stochastic resetting on a lattice*, arXiv:2505.19903v1 (publicly submitted May 26, 2025); *Physical Review E* 112, 034102 (2025), DOI:10.1103/1xkk-7q63. https://arxiv.org/abs/2505.19903
2. A. P. Riascos, D. Boyer, P. Herringer and J. L. Mateos, *Random walks on networks with stochastic resetting*, arXiv:1910.13568, *Physical Review E* 101, 062147 (2020). https://arxiv.org/abs/1910.13568
3. H. Chen, G. Li and F. Huang, *First passage in discrete-time absorbing Markov chains under stochastic resetting*, arXiv:2111.01330, *Journal of Physics A* 55, 384005 (2022). https://arxiv.org/abs/2111.01330
