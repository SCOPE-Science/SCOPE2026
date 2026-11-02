# Pair-codegree rigidity and hidden consensus-time differences in polyadic voting

## Finding

Consider a fixed finite hypergraph on \(n\geq3\) labeled participants, with nonempty finite hyperedge family \(\mathcal E\), hyperedges of size at least two, and a positive Poisson rate \(a_e\) for every \(e\in\mathcal E\). At each event on \(e\), choose one member of \(e\) uniformly and replace the binary opinion of **every** member of \(e\) by the chosen member's opinion. Events on monochromatic groups have no effect. This is the static-topology, proportional-propagation rule studied in the hypergraph adaptive-voter literature.

For a binary configuration \(s\in\{0,1\}^n\), write \(K(s)=\sum_i s_i\) and \(H(s)=K(s)(n-K(s))\), the number of unordered pairs with different opinions. Define the weighted pair-codegrees
\[
w_{ij}=\sum_{e\supseteq\{i,j\}}a_e\qquad(1\leq i<j\leq n).
\]

**Exact closure and converse.** There is a common constant \(\lambda\geq0\) for which every initial configuration satisfies
\[
\mathbb E_s[H(S(t))]=H(s)e^{-\lambda t}\quad\text{for all }t\geq0
\]
if and only if \(w_{ij}=\lambda\) for every unordered pair. The criterion is necessary as well as sufficient. If \(\lambda>0\), consensus occurs almost surely, the probability of all-1 consensus is \(K(s)/n\), and, writing \(T\) for the consensus time and \(H_0=H(s)>0\),
\[
\frac{H_0}{\lfloor n^2/4\rfloor}e^{-\lambda t}\leq\Pr_s(T>t)\leq\frac{H_0}{n-1}e^{-\lambda t},
\quad
\frac{H_0}{\lambda\lfloor n^2/4\rfloor}\leq\mathbb E_s T\leq\frac{H_0}{\lambda(n-1)}.
\]
In particular, the initial number of 1-opinions determines both the exact first and second moments of the number at all times:
\[
\mathbb E_s K(t)=K_0,\qquad \mathbb E_s K(t)^2=nK_0-K_0(n-K_0)e^{-\lambda t}.
\]

**Pairwise summaries are nevertheless insufficient for consensus time.** On seven vertices, let one process have one unit-rate edge for every pair (the complete graph \(K_7\)), and let the other have the seven unit-rate triples of the Fano plane:
\[
\{1,2,3\},\{1,4,5\},\{1,6,7\},\{2,4,6\},\{2,5,7\},\{3,4,7\},\{3,5,6\}.
\]
Both have \(w_{ij}=1\) for all 21 pairs and therefore identical time-dependent first and second moments of \(K(t)\) from every initial binary configuration. Yet from an initial state with exactly one opinion-1 participant,
\[
\mathbb E[T_{\mathrm{Fano}}]=\frac{16}{21},\qquad
\mathbb E[T_{K_7}]=\frac7{10},\qquad
\mathbb E[T_{\mathrm{Fano}}]-\mathbb E[T_{K_7}]=\frac{13}{210}>0.
\]
Every stated rate is per existing hyperedge per unit of continuous time, without normalizing by the number of hyperedges. These are finite, exact expectations, not asymptotic estimates.

## Assumptions and scope

The vertex set and hyperedge family are fixed; opinions are exactly binary; all updates are simultaneous across the selected group; the propagated opinion belongs to a uniformly chosen participant in that group. Hyperedge clocks are independent, continuous-time, and state-independent, with strictly positive rates. Multiple identical hyperedges, if present, may be combined by summing rates. There is no rewiring, majority selection, node-by-node updating, stubbornness, or exogenous noise. The characterization covers arbitrary hyperedge sizes and positive real rates for all finite \(n\geq3\). Its converse requires **one common exponential rate for every initial configuration**, not merely an exponential fit to a selected experiment.

## Proof

**Generator and quadratic drift.** Condition on a hyperedge \(e\) of size \(r\) containing \(m\) opinion-1 vertices. The change \(\Delta K\) is \(r-m\) with probability \(m/r\), or \(-m\) with probability \((r-m)/r\). Therefore \(\mathbb E[\Delta K\mid e,s]=0\) and
\[
\mathbb E[(\Delta K)^2\mid e,s]=\frac{m}{r}(r-m)^2+\frac{r-m}{r}m^2=m(r-m).
\]
Since \(H=nK-K^2\), its generator is
\[
\mathcal LH(s)=-\sum_{e\in\mathcal E}a_e m_e(r_e-m_e)
=-\sum_{i<j}w_{ij}\,\mathbf 1\{s_i\ne s_j\}.
\tag{1}
\]
The second identity counts, inside each hyperedge, exactly the \(m_e(r_e-m_e)\) cross-opinion vertex pairs. It is valid for arbitrary weights and overlapping groups.

**Sufficiency.** If all \(w_{ij}=\lambda\), (1) yields \(\mathcal LH=-\lambda H\). Dynkin's formula for this finite Markov chain and uniqueness of the scalar initial-value problem imply the asserted exact exponential law. The conditional mean increment of \(K\) vanishes at each event, so \(K(t)\) is a bounded martingale and its first moment is constant. The quadratic identity then gives the second-moment formula.

For \(\lambda>0\), any nonconsensus configuration has \(n-1\le H\le\lfloor n^2/4\rfloor\), while consensus states have \(H=0\). As consensus is absorbing, those inequalities applied to \(\mathbb E H(t)\) yield both bounds on \(\Pr(T>t)\), imply almost-sure absorption, and after integration yield the stated expected-time bounds. Bounded martingale convergence identifies the all-1 consensus probability as \(K_0/n\).

**Necessity.** Suppose the same exponential law holds for every deterministic initial configuration. Differentiating at \(t=0\) in (1), define \(d_{ij}=w_{ij}-\lambda\). Every cut \(S\subseteq\{1,\dots,n\}\) must satisfy
\[
\sum_{i\in S,j\notin S}d_{ij}=0.
\]
The singleton cuts give \(\sum_{j\ne i}d_{ij}=0\) for every \(i\). For the two-element cut \(S=\{i,j\}\), the left-hand side is the sum of those two zero row sums minus \(2d_{ij}\). Consequently \(d_{ij}=0\) for every pair. No graph-connectivity or symmetry premise was used for the converse.

**The exact seven-vertex separation.** Each pair of Fano vertices belongs to exactly one listed triple; each pair in \(K_7\) is itself exactly one edge. Both therefore have weighted pair-codegree 1. To calculate mean absorption times, identify configurations with their global binary complements. On the Fano plane, classify a configuration by the minority size 1, 2, or 3; a minority triple is either one of the seven listed Fano lines (class \(L\)) or not (class \(U\)). Direct group-incidence counting shows that these four classes form an exact Markov lumping. The negative transient generator, ordered as \(1,2,L,U\), is
\[
-Q_F=\begin{pmatrix}
3&0&-1&0\\
-8/3&5&-2/3&-4/3\\
0&-6&6&0\\
-1&-3&0&4
\end{pmatrix}.
\]
For instance, with one dissenter, the three incident Fano triples each eliminate that dissenter at rate \(2/3\) or create a full minority Fano line at rate \(1/3\), giving total transition rates 2 to consensus and 1 to class \(L\). A two-dissenter state has one triple containing both dissenters, four containing exactly one, and two containing neither, giving the displayed second row. For a minority line the six mixed triples each move the system to the size-2 class; for a nonline minority triple, direct counting gives rates 1 to the size-1 class, 3 to size 2, and 2 within the nonline class. Thus the expected-time vector solves \((-Q_F)u=\mathbf1\), with exact solution
\[
u_F=\begin{pmatrix}16/21\\47/42\\9/7\\215/168\end{pmatrix}.
\]
For the complete graph, complement classes are simply minority sizes 1, 2, and 3. Since each opposite-opinion pair rings at rate 1 and chooses its winning opinion fairly, the corresponding matrix and solution are
\[
-Q_K=\begin{pmatrix}6&-3&0\\-5&10&-5\\0&-6&6\end{pmatrix},\qquad
u_K=\begin{pmatrix}7/10\\16/15\\37/30\end{pmatrix}.
\]
The first coordinates give the two advertised one-dissenter expectations. The partition into four Fano and three complete-graph transient classes, all off-class rates, and both rational solutions are also checked against all 126 nonabsorbing labeled states by the accompanying program.

## Verification

Run `python3 verify.py` with the Python standard library. The checker recomputes all 21 pair-codegrees on the Fano hypergraph and \(K_7\), checks the generator identity on all \(2^7=128\) binary states for both, checks uniformity of the claimed quotient transition rates across every one of the 126 nonabsorbing states, solves the two finite linear systems exactly with rational Gaussian elimination, and checks the displayed times and \(13/210\) gap. A separate four-vertex weighted example checks the general unequal-codegree generator formula on all 16 states. The general theorem is proved algebraically and does not rely on extrapolation from those finite computations.

## Relationship to prior work

Golovin, Mölter, and Kuehn (2023) define the proportional hyperedge-propagation update and show conservation of the initial mean magnetization in their adaptive-voter framework. The present work restricts to **fixed hyperedges** and derives the exact quadratic drift, characterizes when it closes into a universal exponential by an if-and-only-if weighted pair-codegree condition, and proves the Fano-versus-complete-graph distinction in exact absorption times. First-moment conservation alone does not imply these statements.

Papanikolaou et al. (2022) study a different group-influence/majority mechanism with magnetization drift. Kim et al. (2024) treat a node-update group-driven voter model and asymptotic exit times, not simultaneous group unanimity on a fixed Steiner design. Llabrés et al. (2026) prove exact pairwise reducibility for **single-node updates** and explicitly distinguish simultaneous hyperedge updates as outside that microscopic reduction. Their pairwise mapping therefore does not imply equality of the full seven-vertex processes; the differing exact hitting times here are consistent with that distinction. Existing voter-model martingale and pair-approximation results give important background, but the claims compared here require the precise simultaneous-update generator and two explicit transient chains.

## Limitations

This result is restricted to binary, neutral, simultaneous proportional updates on a **static** hypergraph with fixed clock rates. It does not assert that two equal-codegree hypergraphs have identical laws or consensus-time distributions; indeed, the Fano example proves the opposite. The expected-time bounds are general bounds, not exact expected times for arbitrary designs. Different time normalizations, rewiring, majority propagation, or single-node updates require a fresh calculation. A broader unpublished or unindexed equivalent statement remains possible.

## References

1. A. Golovin, J. Mölter, and C. Kuehn, *Polyadic Opinion Formation: The Adaptive Voter Model on a Hypergraph*, arXiv:2308.03640 (first posted 2023-08-07), https://arxiv.org/abs/2308.03640.
2. N. Papanikolaou, G. Vaccario, E. Hormann, R. Lambiotte, and F. Schweitzer, *Consensus from group interactions: An adaptive voter model on hypergraphs*, arXiv:2201.06421 (first posted 2022-01-17), https://arxiv.org/abs/2201.06421.
3. J. Kim, D.-S. Lee, B. Min, M. A. Porter, M. San Miguel, and K.-I. Goh, *Competition between group interactions and nonlinearity in voter dynamics on hypergraphs*, arXiv:2407.11261 (first posted 2024-07-15), https://arxiv.org/abs/2407.11261.
4. J. Llabrés, R. Toral, M. San Miguel, and F. Vázquez, *Reducibility of higher-order to pairwise interactions: Social impact models on hypergraphs*, arXiv:2601.05169 (first posted 2026-01-08), https://arxiv.org/abs/2601.05169.
