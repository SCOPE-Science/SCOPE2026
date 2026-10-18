# Almost-sure finite-time fixation of the receptive network in asynchronous adaptive-confidence opinion dynamics

## Finding
For the asynchronous adaptive-confidence Deffuant–Weisbuch (DW) process on **every finite undirected graph**, the receptive (effective) graph becomes exactly constant after an almost-surely finite, sample-dependent number of interactions. This holds for every \(0<\mu\le 1/2\), \(0<\gamma\le 1\), and \(0\le\delta\le 1\), including the no-confidence-decrease endpoint \(\delta=1\). It needs no genericity assumption on opinion limits or avoidance of equalities at a confidence boundary. The same assertion holds for history-dependent edge sampling when every edge's conditional selection probability is uniformly bounded below by a positive constant.

If \(\delta<1\), the fixed receptive graph is exactly the graph of edges with limiting dyadic confidence \(1\); the confidence of every eventually unreceptive edge tends to \(0\). At \(\delta=1\), graph fixation still holds, but that confidence-limit characterization is not asserted.

## Assumptions and scope
Let \(G=(V,E)\) be any finite simple undirected graph, with opinion \(x_i(t)\in[0,1]\) for each vertex and dyadic confidence \(c_e(t)\in[0,1]\) for each edge. Initial values are arbitrary and deterministic or random, possibly correlated. Write the pre-selection history as \(\mathcal F_t\). At each integer time \(t\ge0\), choose one edge \(S_t\) such that for a constant \(q>0\),
\[
  \Pr(S_t=e\mid\mathcal F_t)\ge q
  \quad\text{almost surely for every }e\in E,\ t\ge0.
\]
The published independently uniform edge rule has \(q=1/|E|\). No edge need exist; in the edgeless case the assertion is immediate.

For \(e=\{i,j\}\), define receptivity at the **pre-selection** state by
\[
 R_e(t)=\mathbf1\{|x_i(t)-x_j(t)|<c_e(t)\}.
\]
For a selected receptive edge, with \(0<\mu\le 1/2\) and \(0<\gamma\le1\), perform
\[
 x_i(t+1)=(1-\mu)x_i(t)+\mu x_j(t),\quad
 x_j(t+1)=\mu x_i(t)+(1-\mu)x_j(t),
 \quad c_e(t+1)=c_e(t)+\gamma(1-c_e(t)).
\]
For a selected nonreceptive edge, leave all opinions unchanged and set \(c_e(t+1)=\delta c_e(t)\), with \(0\le\delta\le1\). Unselected confidence values and all other opinions remain unchanged. Define \(E_{\mathrm{eff}}(t)=\{e\in E:R_e(t)=1\}\). The claim is the existence of an almost-surely finite **integer** \(T\) such that \(E_{\mathrm{eff}}(t)=E_{\mathrm{eff}}(T)\) for all integers \(t\ge T\).

## Proof
**1. Deterministic convergence of every labeled opinion.** This requires no randomness. For each \(1\le k\le |V|\), let \(S_k(t)\) be the sum of the \(k\) smallest components of \(x(t)\), equivalently the minimum of all sums of \(k\) labeled components. A selected receptive update is a two-coordinate doubly stochastic averaging step. For any fixed \(k\)-subset \(A\), its updated sum is either unchanged or is a convex combination of the original sum on \(A\) and that on the \(k\)-subset obtained by swapping the unique updated endpoint of \(A\) with the other endpoint. Both original sums are at least \(S_k(t)\). Thus \(S_k(t+1)\ge S_k(t)\). All such partial sums are bounded and therefore converge. It follows that each ordered component (the difference of successive ordered partial sums) converges.

The quadratic energy \(Q(t)=\sum_{i\in V}x_i(t)^2\) is nonincreasing. On a selected receptive edge \(\{i,j\}\), direct expansion gives the **exact** identity
\[
 Q(t)-Q(t+1)=2\mu(1-\mu)(x_i(t)-x_j(t))^2;
\]
otherwise it is zero. Hence \(Q(t)\) converges, and the maximum absolute coordinate increment in a step tends to \(0\). Let \(a_1<\cdots<a_r\) be the distinct limiting ordered values. Every component \(x_i(t)\) lies arbitrarily close to \(\{a_1,\ldots,a_r\}\) once \(t\) is sufficiently large, because it equals one of the ordered components. If \(r>1\), take disjoint neighborhoods of radius less than a quarter of the least separation between distinct \(a_j\); for large \(t\), every step is too small for any component to move between two such neighborhoods. Therefore each labeled component remains associated with one \(a_j\), and its distance to that value tends to zero. The case \(r=1\) is immediate. Consequently, for each vertex \(i\), \(x_i(t)\to x_i^\infty\) along **every** realized edge sequence.

**2. No infinitely recurring receptivity without successful selection.** Fix an edge \(e\). Each event \(R_e(t)=1\) is measurable before \(S_t\) is selected. The lower sampling bound implies the following conditional-thinning statement: almost surely, if this edge is receptive at infinitely many times, then the edge is selected **while receptive** infinitely often. To prove it, after any deterministic time \(T\), expose successive receptive opportunities. Conditional on the history at the \(k\)-th such opportunity, the chance of not selecting \(e\) is at most \(1-q\). Thus the chance of having at least \(k\) such opportunities but no selected receptive meeting is at most \((1-q)^k\). Letting \(k\to\infty\), and taking the countable union over \(T\), excludes infinitely many receptive opportunities with only finitely many successful selections. This argument applies even when sampling probabilities depend on the past.

**3. Edgewise fixation.** Fix \(e=\{i,j\}\) and work on the probability-one event of Step 2 and the convergence from Step 1.

If \(x_i^\infty\ne x_j^\infty\), there can be only finitely many selected receptive meetings: each such meeting changes the opinion of \(i\) by exactly \(\mu|x_i(t)-x_j(t)|\), which is bounded below by a positive constant at all sufficiently late times, contradicting convergence of the labeled opinion. By Step 2, \(R_e(t)=1\) itself can occur only finitely often. Therefore \(e\) is eventually absent.

If \(x_i^\infty=x_j^\infty\), choose an integer \(T_e\) large enough that \(|x_i(t)-x_j(t)|<\gamma\) for every \(t\ge T_e\). If there is any selected receptive meeting at \(t\ge T_e\), its confidence update gives \(c_e(t+1)\ge\gamma\). Thereafter the opinion gap remains strictly below \(\gamma\). Hence this edge is receptive at the next step, any later selection of it is again receptive, and its confidence is nondecreasing and at least \(\gamma\). This proves it is receptive forever after the first such meeting. If no selected receptive meeting occurs after \(T_e\), Step 2 forces only finitely many receptive opportunities, so the edge is eventually absent. In either case \(R_e(t)\) is eventually constant.

There are finitely many edges; the maximum of their individual finite fixation times is finite almost surely. This proves fixation of the entire effective graph.

**4. Confidence limits when \(\delta<1\).** The uniform positive conditional selection probability also ensures that every edge is selected infinitely often almost surely. On a permanently receptive edge, each selection applies \(c\mapsto c+\gamma(1-c)\), so its confidence tends to \(1\). On a permanently unreceptive edge, each selection applies \(c\mapsto\delta c\), hence its confidence tends to \(0\) for \(\delta<1\). The converse identifications follow from these exhaustive alternatives. At \(\delta=1\) the second argument fails: e.g. an edge with distinct constant opinions and an unreceptive confidence can remain unreceptive without its confidence decreasing. No such equivalence is asserted at that endpoint.

## Verification
The argument is fully analytic. The exact quadratic-energy identity follows by expanding the two displayed opinion-update equations. The ordered-partial-sum step can be verified directly for the four cases where a subset contains neither, both, or exactly one endpoint of the selected edge; the single-endpoint case is explicitly a convex combination of two original subset sums. The conditional-thinning estimate is an iterated conditional-probability bound with factor \(1-q\). Finally, the permanent-receptivity step depends strictly on \(\gamma>0\) and the strict confidence inequality, both stated in the assumptions. No numerical experiment is used to infer finite-time fixation, and no unbounded stopping-time expectation or quantitative tail is claimed.

## Relationship to prior work
Li, Luo and Porter (first public preprint 14 March 2023; journal version 2025) introduce this dyadwise adaptive-confidence DW process. Their journal Theorem 3.8 establishes confidence convergence for \(\gamma>0\) and \(\delta<1\), and Theorem 3.11 establishes that sufficiently late effective edges only join equal-limit opinion groups. Their future-work discussion explicitly leaves eventual constancy of the **entire asynchronous effective graph** unproved. The present result establishes that stronger conclusion for all finite graphs and broadens it to \(\delta=1\) and uniformly persistent conditional edge selection. The published opinion-convergence theorem is used only as context: the proof above gives an independent argument for it.

Lorenz's stabilization theorem concerns convergence of products of reciprocal stochastic opinion-update matrices, not permanent stabilization of the time-dependent *receptivity* relation. Chen and collaborators' fixed heterogeneous-confidence DW variants likewise do not contain the adaptive confidence reinforcement mechanism. Later adaptive-interaction-probability models change sampling weights rather than updating the dyadic confidence thresholds as above. A general theorem implying this result from standard stochastic-approximation or conditional-selection principles remains a publication-priority risk.

## Limitations
The social graph is finite, compromise is symmetric with fixed \(\mu>0\), and successful meetings raise dyadic confidence by at least the fixed \(\gamma>0\). A uniform positive lower bound on each conditional edge-selection probability is essential to the given proof; a model permitting an edge to be sampled only finitely often may behave differently. No assertion is made about synchronous adaptive-confidence HK dynamics, infinite networks, repulsion, or state-dependent compromise parameters. Fixation has an almost-surely finite time but no deterministic upper bound or expected-time bound is provided. At \(\delta=1\), an unreceptive edge need not have confidence limit zero. Publication priority has not been established independently.

## References
1. Grace J. Li, Jiajie Luo, Mason A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, arXiv:2303.07563, initially posted 2023-03-14; SIAM Journal on Applied Dynamical Systems 24 (2025), DOI 10.1137/23M1558951. Journal author's full text: https://www.math.ucla.edu/~mason/papers/BCM-dynamic-April2025.pdf; preprint https://arxiv.org/abs/2303.07563.
2. Jan Lorenz, *A stabilization theorem for dynamics of continuous opinions*, arXiv:0708.2981, https://arxiv.org/abs/0708.2981.
3. Chen, Su, Mei and Bullo, work on heterogeneous-confidence Deffuant–Weisbuch dynamics, arXiv:1901.02092, https://arxiv.org/abs/1901.02092.
4. *A Bounded-Confidence Model with Adaptive Interaction Probabilities*, arXiv:2605.20418, https://arxiv.org/abs/2605.20418 (distinct adaptive selection model).
