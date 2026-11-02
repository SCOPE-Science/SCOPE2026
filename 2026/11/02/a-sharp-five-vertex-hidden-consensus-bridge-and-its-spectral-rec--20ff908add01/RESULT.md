# A sharp five-vertex hidden-consensus bridge and its spectral receptivity threshold

## Finding

For synchronous adaptive dyadic confidence dynamics, a five-agent path has a **sharp spectral threshold** between a permanently invisible bridge and eventual first receptivity. In the permanently invisible regime, all opinions nonetheless converge to the same number. More precisely, fix the path \(1-2-3-4-5\), initial opinions
\[
(x_1(0),x_2(0),x_3(0),x_4(0),x_5(0))=(3/10,0,1/5,2/5,3/5),
\]
common initial dyadic confidence \(c_0=1/4\), \(0<\gamma\le1\), and \(0<\delta<1\). Define
\[
\lambda=\frac{3+\sqrt{33}}{12},\qquad A=\frac3{20}+\frac{\sqrt{33}}{44}.
\]
The edge \(\{1,2\}\) is unreceptive for every integer \(t\ge0\) **if and only if** \(\delta\le\lambda\). In that regime
\[
\lim_{t\to\infty}x_i(t)=3/10\quad(i=1,\ldots,5),\qquad
c_{12}(t)=\tfrac14\delta^t\to0,
\]
yet the effective graph remains an isolated vertex and the path \(2-3-4-5\). For \(\delta>\lambda\), define \(T(\delta)\) as the first time the bridge is receptive. It is finite and obeys the exact near-boundary law
\[
\lim_{\delta\downarrow\lambda}T(\delta)\log(\delta/\lambda)
=\log(4A)=\log\!\left(\frac35+\frac{\sqrt{33}}{11}\right)>0.
\]
The five-vertex construction is minimum-sized in the natural class of connected **tree** hosts whose initial effective graph consists of two connected components separated by exactly one inactive bridge, with all intra-component edges continuously receptive and a common limiting opinion.

## Assumptions and scope

The host is a fixed simple undirected graph. Every opinion lies in \([0,1]\), and all edge confidences initially equal \(c_0\). At integer time \(t\), edge \(\{i,j\}\) is receptive precisely if \(|x_i(t)-x_j(t)|<c_{ij}(t)\). Every agent simultaneously averages its own opinion with those of its receptive neighbors:
\[
x_i(t+1)=\frac{x_i(t)+\sum_{j:\,\{i,j\}\text{ receptive at }t}x_j(t)}{1+\#\{j:\,\{i,j\}\text{ receptive at }t\}}.
\]
The edge confidence is updated **using the same time-\(t\) receptivity test**:
\[
c_{ij}(t+1)=\begin{cases}
c_{ij}(t)+\gamma(1-c_{ij}(t)),&\text{receptive},\\
\delta c_{ij}(t),&\text{not receptive}.
\end{cases}
\]
The strict threshold convention matters at equality. The minimum-size statement assumes a tree, exactly one initially inactive edge, its continued inactivity, and continued receptivity of every other edge; it does not claim the minimum size under arbitrary switching histories or for all host graphs.

## Proof

**1. The four-node active component is invariant.** Initially only \(\{1,2\}\) is unreceptive: its gap is \(3/10>1/4\), whereas each other gap is \(1/5<1/4\). As long as this bridge remains inactive, symmetry of the connected four-agent path gives
\[
x_1(t)=3/10,\quad (x_2(t),x_3(t),x_4(t),x_5(t))
=(3/10-a_t,3/10-b_t,3/10+b_t,3/10+a_t),
\]
where \(a_0=3/10\), \(b_0=1/10\), and
\[
a_{t+1}=(a_t+b_t)/2,\qquad b_{t+1}=a_t/3.
\]
The rectangle \(0\le b_t\le1/10\), \(b_t\le a_t\le3/10\) is invariant: \(a_{t+1}\le a_t\le3/10\), \(b_{t+1}=a_t/3\le1/10\), and \(a_{t+1}\ge b_{t+1}\). Internal gaps are \(a_t-b_t,2b_t,a_t-b_t\). At \(t=0\), all are \(1/5\). For \(t\ge1\),
\[
a_t-b_t=a_{t-1}/6+b_{t-1}/2\le1/10,
\qquad 2b_t=2a_{t-1}/3\le1/5.
\]
Thus each internal gap stays strictly below \(c_0\), while the associated confidence never decreases. The assumed active four-path is self-consistent for every step until any bridge activation.

**2. Exact spectral race.** Eliminating \(b_t\) gives
\[
a_{t+2}=\tfrac12 a_{t+1}+\tfrac16a_t,
\qquad a_0=3/10,\quad a_1=1/5.
\]
Its roots are \(\lambda=(3+\sqrt{33})/12\) and \(\nu=(3-\sqrt{33})/12\), satisfying \(0<\lambda<1\) and \(-1<\nu<0\). Hence
\[
a_t=A\lambda^t+B\nu^t,\qquad A=3/20+\sqrt{33}/44>1/4,
\quad B=3/20-\sqrt{33}/44>0.
\]
In particular, \(a_t\to0\). Since \(\lambda^2=\lambda/2+1/6\), comparing the positive-coefficient recurrence with the initial strict inequalities \(a_0>\lambda^0/4\), \(a_1>\lambda/4\) yields
\[
\tfrac14\lambda^t<a_t\le\tfrac3{10}\lambda^t\quad(t\ge0).
\]
The upper inequality follows similarly from \(a_0=3/10\) and \(a_1<(3/10)\lambda\). If the bridge has been unreceptive through time \(t-1\), its time-\(t\) confidence is \(\delta^t/4\), while its gap is exactly \(a_t\). If \(\delta\le\lambda\), the strict lower bound keeps it unreceptive at time \(t\), closing an induction. Thus the four-path averages toward \(3/10\), node 1 stays at \(3/10\), and the confidence of their bridge vanishes.

Conversely, if \(\delta>\lambda\) and the bridge never became receptive, the upper bound would give \(a_t\le(3/10)\lambda^t<(1/4)\delta^t\) for sufficiently large \(t\), contradicting the threshold test. Hence its first receptive time \(T(\delta)\) is finite. Before that first event, the explicit formula yields the exact test
\[
T(\delta)=\min\left\{t\ge1:\ \delta^t>4(A\lambda^t+B\nu^t)\right\}.
\]
At \(\delta=\lambda\), the bridge never becomes receptive, so \(T(\delta)\to\infty\) as \(\delta\downarrow\lambda\). Because \(\nu/\lambda\) has absolute value below one, \(4a_t/\lambda^t\to4A>1\). Comparing the first-crossing inequality to \(\exp(t\log(\delta/\lambda))\), uniformly for sufficiently large \(t\), proves \(T(\delta)\log(\delta/\lambda)\to\log(4A)\). This is an asymptotic at the first appearance only; no assertion is made about later reconfiguration for \(\delta>\lambda\).

**3. Sharp small-tree obstruction.** Consider a connected tree with at most four vertices and only one initially unreceptive edge. Removing that edge leaves two tree components, each with at most three vertices. If all other edges stay receptive, each component performs fixed self-inclusive averaging, whose consensus weights are proportional to \(1+\deg(v)\). For a two-vertex component, its bridge endpoint lies strictly less than \(c_0/2\) from its component consensus. For a three-vertex component (a path), the stationary weights are \((2,3,2)/7\). If the bridge endpoint is central, its distance from consensus is less than \(4c_0/7\); if an endpoint, it is less than \((5c_0+2c_0)/7=c_0\), by the two initially receptive internal-edge inequalities. A singleton is exactly at its component consensus. For an at-most-four-vertex split the only possibilities are \((1,1)\), \((1,2)\), \((1,3)\), and \((2,2)\). If the component consensuses coincide, the initial bridge gap is respectively less than \(c_0\), contradicting the stipulated initial nonreceptivity. Five vertices are therefore necessary in this regime, and the displayed example attains five.

## Verification

The included `verify.py` independently implements the full five-node simultaneous averaging and dyadic-confidence updates over exact rational numbers. It checks initial receptivity, 60 and 20 time-step trajectories for rational decay values, the predicted first-reception times \(T(3/4)=5\), \(T(4/5)=2\), and \(T(9/10)=1\), the rational recurrence, the weighted average, and high-precision numerical consistency of the spectral formula. These finite tests are supplementary; the indefinite-time and minimum-size assertions follow from the proof above.

Run `python3 verify.py` using Python 3.9 or later; no nonstandard packages are required.

## Relationship to prior work

Li, Luo and Porter (arXiv:2303.07563) define this synchronous adaptive-confidence model and prove convergence of each confidence to zero or one and eventual constancy of its effective graph; their simulations show same-limit edges that lose receptivity. The present claim gives a fully analytic, size-sharp **disconnected effective graph with common limiting opinions**, a specific exact algebraic threshold for a cut edge, and a critical first-reception delay law. Their general theorems do not imply the explicit threshold or the small-tree obstruction. A related finite-time edge-repair classification for complete graphs concerns an effective graph that stays connected after one edge is removed; its complete-graph contraction rate does not cover this path/bridge theorem. Kan, Feng and Porter (arXiv:2112.05856) instead study asynchronous pairwise compromise and adaptive graph rewiring rather than fixed-host synchronous dyadic confidence decay.

## Limitations

The global-consensus/nonreceptive-bridge coexistence uses a precisely matched initial singleton opinion (a codimension-one condition), not generic initial data. The size-sharp assertion is limited to the specified fixed-two-component tree regime. For decay parameters above the spectral threshold, only **first** receptivity is classified. The result does not claim almost-sure behavior for random schedules or general finite networks. Independent audit has not been performed; unindexed equivalent studies remain a literature-priority risk.

## References

1. G. J. Li, J. Luo, and M. A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, arXiv:2303.07563, first submitted 2023-03-14, version 3 (2024). https://arxiv.org/abs/2303.07563 .
2. U. Kan, M. Feng, and M. A. Porter, *An Adaptive Bounded-Confidence Model of Opinion Dynamics on Networks*, arXiv:2112.05856, first submitted 2021-12-10. https://arxiv.org/abs/2112.05856 .
3. C. Bernardo, C. Altafini, A. Proskurnikov, and F. Vasca, *Bounded confidence opinion dynamics: A survey*, Automatica 159 (2024), 111302, https://doi.org/10.1016/j.automatica.2023.111302 .
