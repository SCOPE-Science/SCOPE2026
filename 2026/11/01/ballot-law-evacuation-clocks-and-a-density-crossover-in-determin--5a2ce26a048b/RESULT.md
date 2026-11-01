# Ballot-law evacuation clocks and a density crossover in deterministic parallel traffic

## Finding
For every integer \(n\ge1\), consider binary configurations on a one-way \(n\)-site road. At each integer step, every occupied site simultaneously moves one cell right if the target cell was vacant at the start of the step; a particle at the last site exits; no particles enter at the left. Let \(T_n(x)\) be the first time the road is empty. Put \(S_0=0\), \(S_i=\sum_{j=1}^i(2x_j-1)\), and, for a nonzero configuration, put \(H(x)=\max_{i:x_i=1}S_{i-1}\). Then
\[
T_n(x)=\begin{cases}0,&x=0^n,\\n+H(x),&x\ne0^n.\end{cases}
\]
In particular the sharp maximal evacuation time is \(2n-1\), attained only by the all-occupied initial configuration.

Write \(q=1-p\), and sample the initial sites independently with occupancy probability \(p\in(0,1)\). For integers \(m,a\ge0\), define
\[
Q_p(m,a)=\sum_{r=0}^{\lfloor(m+a)/2\rfloor}
 \left[\binom mr-\binom m{r-a-1}\right]p^rq^{m-r},
\]
where any binomial coefficient with an out-of-range lower index is zero. The **entire finite-size evacuation-time distribution**, for every integer \(t\), is
\[
\Pr_p\{T_n\le t\}=\begin{cases}
0,&t<0,\\
q^{n-t}Q_p(t,1),&0\le t<n,\\
Q_p(n,t-n+1),&t\ge n.
\end{cases}
\]
For the uniform law \(p=1/2\), the exact number \(N_n(t)\) of initial configurations with evacuation time \(t\) is
\[
N_n(t)=\begin{cases}
1,&t=0,\\
\binom{t}{(t-1)/2},&1\le t\le n,\ t\text{ odd},\\
\binom{t}{t/2-1},&1\le t\le n,\ t\text{ even},\\
\binom n{\lfloor(2n-t-1)/2\rfloor},&n<t\le2n-1,\\
0,&\text{otherwise}.
\end{cases}
\]
Thus every early-time shell with \(t<n\) is independent of the road length \(n\).

There is also a sharp three-regime density crossover. As \(n\to\infty\), writing \(Z\) for a standard normal random variable:

- If \(p<1/2\), then \(T_n-n\) converges in distribution to an integer-valued random variable \(H_\infty\) with, for integers \(h\ge0\), \(\Pr\{H_\infty\le h\}=1-(p/q)^{h+2}\), and for integers \(r\ge1\), \(\Pr\{H_\infty\le-r\}=q^r[1-(p/q)^2]\).
- If \(p=1/2\), then \((T_n-n)/\sqrt n\Rightarrow |Z|\) (half-normal).
- If \(p>1/2\), then \((T_n-2pn)/(2\sqrt{npq})\Rightarrow Z\).

## Assumptions and scope
The discrete time step is a **fully parallel** update, with movements determined by the pre-update configuration (not left-to-right sequential updates). A particle at site \(n\) exits in one step, regardless of its left neighbor. A particle elsewhere moves right if and only if its immediate right neighbor is empty before the update. No particle enters. The empty configuration is absorbing, and \(T_n\) is measured in whole synchronous updates. The finite CDF is exact for all \(n\ge1\) and \(p\in(0,1)\); the three limiting laws hold for a fixed density \(p\) as \(n\to\infty\). Endpoints \(p=0\) and \(p=1\) are deterministic and can be recovered directly rather than from the nondegenerate limit laws.

## Proof
**Height descent.** Interpret each initial \(1\) as an up-step of the word-height walk \((S_i)\) and each \(0\) as a down-step. In any nonempty word, let \(H\) be the largest height at the *start* of any up-step. Under a parallel update an internal moving \(10\to01\) up-step shifts right by one and its starting height drops by exactly one: in the local pair the height path \((h,h+1,h)\) becomes \((h,h-1,h)\). An up-step that stays put must be blocked by an adjacent \(1\) to its right, whose initial start height is one larger. Therefore every surviving up-step has updated starting height at most \(H-1\). These local changes are disjoint, since every active internal \(10\) has distinct sites; the removed final up-step cannot increase any earlier height.

Conversely, if an up-step of initial start height \(H\) occurs internally, it is followed by a \(0\) (otherwise the following up-step would start at \(H+1\)); it consequently moves and survives at updated height \(H-1\). If every maximizer is at the final site and at least two particles exist, the penultimate site must also be occupied: otherwise, taking the final preceding occupied site shows that it has initial starting height at least \(H\) and is internal. The penultimate particle is blocked, survives, and starts at height \(H-1\). Hence, whenever an update from a nonempty configuration remains nonempty, \(H\) decreases by **exactly one**.

The only nonempty configuration whose next state is empty is \(0^{n-1}1\): a particle at an earlier site cannot disappear in one step. This terminal nonempty configuration has \(H=1-n\). Every nonempty word has \(H\ge1-n\), with equality only for that terminal singleton, because its first up-step must then be at position \(n\). Therefore descending \(H\) by one on each nonfinal update and taking one final exit step gives \(T_n=n+H(x)\). Since \(H\le n-1\), with equality only if every site is occupied, the maximal time is \(2n-1\).

**Walk barriers and the finite CDF.** If \(H(x)\le h\) with \(h\ge0\), every up-step begins below or at \(h\), equivalently the complete walk has running maximum at most \(h+1\). For \(h=-r<0\), this condition forces the first \(r\) symbols to be \(0\); relative to height \(-r\), the remaining \(n-r\) steps must have running maximum at most \(1\). These descriptions also contain the all-zero word when computing the CDF. The standard reflection principle counts length-\(m\) walks with exactly \(r\) up-steps that do not cross level \(a\) as \(\binom mr-\binom m{r-a-1}\); multiplying by their Bernoulli weights and summing proves \(Q_p(m,a)\) and the stated piecewise formula. If \(t<n\), the forced initial \(n-t\) zeros contribute \(q^{n-t}\); if \(t\ge n\), the barrier is \(t-n+1\). For \(t<0\) the CDF is zero.

**Unweighted time shells.** For \(p=q=1/2\), the integer count of walks of length \(m\) with running maximum at most \(a\) is the sum \(\sum_{r\le\lfloor(m+a)/2\rfloor}[\binom mr-\binom m{r-a-1}]\). With \(a=1\) this telescopes to the sum of the two central adjacent binomial coefficients. Consecutive differences yield \(N_n(t)=\binom{t}{(t-1)/2}\) for odd \(t\) and \(N_n(t)=\binom{t}{t/2-1}\) for even \(t\), as long as \(1\le t\le n\). For \(t>n\), the difference of two successive walk-barrier counts is a single binomial coefficient indexed by \(\lfloor(2n-t-1)/2\rfloor\), proving the remaining cases. In the boundary case \(t=n\), the adjacent-binomial calculation gives the same formula. The shells sum to \(2^n\), as required by their partition of all configurations.

**Density crossover.** Couple all lengths to the same iid Bernoulli(p) sequence. For \(p<q\), the random walk drifts to minus infinity, so its supremum of up-step starting heights \(H_n\) converges almost surely to finite \(H_\infty\). For \(h\ge0\), the gambler's-ruin probability of reaching level \(h+2\) is \((p/q)^{h+2}\), giving its upper CDF. For \(h=-r\), the first \(r\) sites must be zero, followed by a walk that never reaches level \(2\), giving the stated lower CDF. For \(p=q\), the walk maximum \(M_n=\max_{0\le j\le n}S_j\) satisfies \(M_n/\sqrt n\Rightarrow |Z|\) by the invariance principle and reflection. On the event \(M_n>0\), \(H_n=M_n-1\); the complementary event has vanishing probability, proving the half-normal law. For \(p>q\), \(M_n-S_n\) is tight, by time reversal and the finite supremum of an iid negative-drift walk; also \(\Pr(M_n>0)\to1\), so \(H_n=S_n+O_{\Pr}(1)\). The central limit theorem for \(S_n=2\sum x_i-n\) yields the stated Gaussian limit. None of the asymptotic reasoning is used in the finite distribution formulas.

## Verification
The standalone `check_python.py` implements the simultaneous update directly using tuples, independently computes the height statistic, and checks every initial state for \(1\le n\le15\) (65,534 configurations in total). It verifies the full shell census and, using integer weights with occupancy-to-vacancy odds \(1:2\), \(2:1\), and \(1:1\), the exact CDF for every attainable integer time. The separate `check_cpp.cpp` uses a distinct bitwise direct update implementation and exhaustively checks the pathwise identity and all shell counts through \(n=20\) (2,097,150 configurations). Their reproduced outputs appear in `check_python.out` and `check_cpp.out`. These checks support but are not substituted for the all-length proofs above.

## Relationship to prior work
Deterministic right-moving exclusion is the classical traffic cellular automaton Rule 184; no novelty is claimed for the local rule, the Bernoulli walk reflection principle, or the underlying central limit theorem. Tilstra and Ernst's 1997 work studies stationary and boundary-driven profiles and correlation functions for synchronous exclusion, and discusses particle travel times under continuing inflow, rather than the distribution of the final emptying time from arbitrary independent initial data with no inflow. Cividini, Hilhorst and Appert-Rolland (2013) treat stochastic open-boundary injection/removal and moving domain walls, not the exact initial-condition-resolved deterministic evacuation law here. Dorignac, Geniet and Pitard (2023) study stochastic **continuous-time** exclusion and step-initial evacuation times; their process and its clearance-time law differ. The particular contribution assessed here is the finite closed-form weighted clearance-time distribution for arbitrary Bernoulli occupancy, the uniform early-time shell counts, and the sharp three-regime density crossover. Related known stationary and transient traffic results make overlap with an unlocated equivalent formulation a remaining possibility.

## Limitations
The theorem concerns a single deterministic, synchronous, right-moving species on a finite path with zero inflow and immediate right-boundary exit. It does not cover random hopping, stochastic extraction rates, periodic boundaries, nonzero inflow, multiple particle species, general correlated initial distributions or varying density scales \(p=p(n)\). The limiting laws assume fixed \(p\); the finite count identities are exact independently of those limits. A comprehensive guarantee of priority cannot be obtained solely from indexed searches, and related traffic/TASEP work may encode the same stopping-time law in alternative terms. Independent mathematical audit has not been performed.

## References
- L. G. Tilstra and M. H. Ernst, *Analytic profiles and correlation functions in synchronous asymmetric exclusion processes*, arXiv:cond-mat/9712237, first arXiv posting 1997-12-19, https://arxiv.org/abs/cond-mat/9712237.
- J. Cividini, H. J. Hilhorst and C. Appert-Rolland, *Exact domain wall theory for deterministic TASEP with parallel update*, arXiv:1310.2090 (2013), https://arxiv.org/abs/1310.2090.
- J. Dorignac, F. Geniet and E. Pitard, *TASEP Exit Times*, arXiv:2310.08477 (2023), https://arxiv.org/abs/2310.08477.
