# Even intervention budgets and exact heterogeneous-biclique timed targeting

## Finding

For non-progressive, synchronous binary threshold dynamics with interventions at arbitrary discrete times, consider any finite **bipartite** graph \(G=(A\sqcup B,E)\) without isolated vertices and with integer thresholds \(1\leq\tau(v)\leq d(v)\). Let \(\operatorname{MTT}(G,\tau)\) be the minimum total number of targeted vertex-time occurrences required to reach an all-positive, intervention-free configuration. Then

\[
\operatorname{MTT}(G,\tau)=2c(G,\tau),
\]

where \(c(G,\tau)\) is the minimum intervention cost for **one** alternating parity strand (part \(A\) at even times, part \(B\) at odd times) to reach a fully positive part. In particular, every such bipartite instance has an **even** optimum and admits a minimum-cost schedule obtained from two time-shifted copies of a single strand schedule.

For the complete bipartite graph \(K_{a,b}\), with arbitrary individual thresholds \(\tau_1,\dots,\tau_a\in\{1,\dots,b\}\) on \(A\) and \(\sigma_1,\dots,\sigma_b\in\{1,\dots,a\}\) on \(B\), the value and an optimal timed intervention schedule can be found in \(O(ab\log(a+b))\) time and \(O(ab)\) space by a single nonnegative shortest-path computation on \(a+b+2\) count states (or \(a+b+3\) vertices including the source). This applies without uniformity, majority, or monotonicity assumptions beyond positive feasible thresholds.

More precisely, set
\[
 f(v)=\#\{i\in A:\tau_i\leq v\},\quad 0\leq v\leq b,
 \qquad g(u)=\#\{j\in B:\sigma_j\leq u\},\quad 0\leq u\leq a.
\]
Build the weighted directed graph with source \(s\), states \(A_u\) for \(0\leq u\leq a\), and \(B_v\) for \(0\leq v\leq b\), and arcs
\[
 s\longrightarrow A_u\ (\text{weight }u),\qquad
 A_u\longrightarrow B_v\ (\text{weight }v-g(u))\quad(v\geq g(u)),
\]
\[
 B_v\longrightarrow A_u\ (\text{weight }u-f(v))\quad(u\geq f(v)).
\]
Then the exact answer is
\[
 \boxed{\operatorname{MTT}(K_{a,b},\tau,\sigma)
 =2\min\{\operatorname{dist}(s,A_a),\operatorname{dist}(s,B_b)\}.}
\]

In particular, if every vertex of \(A\) has the same threshold \(\alpha\) and every vertex of \(B\) has the same threshold \(\beta\), then
\[
 \boxed{\operatorname{MTT}(K_{a,b};\alpha,\beta)=2\min\{\alpha,\beta\}.}
\]

## Assumptions and scope

The graph is finite, simple, undirected and bipartite; each vertex has positive degree and a fixed integer threshold between one and its degree, inclusive. Time is synchronous and discrete. At time \(t\), let \(S_t\) be the manually targeted vertices, \(Q_t\) the naturally positive vertices, and \(X_t=Q_t\cup S_t\) the actual positive set. The rules are
\[
 Q_0=\varnothing,\qquad Q_{t+1}=\{v:\ |N(v)\cap X_t|\geq\tau(v)\}.
\]
The aim is to find finite \(T\) with \(S_T=\varnothing\) and \(Q_T=V\), minimizing \(\sum_{t=0}^{T}|S_t|\). Repeatedly targeting the same vertex on different dates incurs a separate cost each time. An intervention on an already naturally positive vertex is redundant and can be omitted. The formulas above concern **timed** targeting; they are not formulas for irreversible diffusion or for untimed target sets.

The strand beginning with \(A\) at time zero records successively the positive configurations on \(A\) at times \(0,2,4,\dots\), and on \(B\) at times \(1,3,5,\dots\), together with precisely the interventions at those vertex-times. Its opposite strand records \(B\) at even times and \(A\) at odd times. A strand is called saturated if, at any of its sampled times, the active set equals its entire current part.

## Proof

**1. Exact bipartite strand separation.** On a bipartite graph, the natural state on \(A\) at time \(t+1\) depends exclusively on the actual positive state on \(B\) at time \(t\), and conversely. Therefore the two alternating vertex-time strands are independent: each evolves from its own prescribed interventions, without consulting any state in the other strand. Let \(c_A\) and \(c_B\) be their respective minimum costs to saturate a part.

Both strands begin with empty natural states. Since thresholds are positive, an entirely empty active state produces an empty natural successor. Any feasible \(A\)-first strand can be shifted by one time unit to yield a feasible \(B\)-first strand of the same cost, leaving the newly introduced \(B\)-state at time zero empty. The reverse shift is equally valid. Hence \(c_A=c_B=:c\).

Any global successful schedule has \(Q_T=A\sqcup B\); in particular both strands are saturated at time \(T\), so each incurs at least \(c\) interventions. Thus \(\operatorname{MTT}(G,\tau)\geq 2c\). Conversely, choose a minimum-cost \(A\)-first saturating strand and its one-time-shifted copy as the other strand. A saturated side makes the opposite side fully naturally positive one step later, because every threshold is at most the corresponding degree. Two steps after saturation the first side is again fully naturally positive. Hence, after adding no further interventions and allowing enough zero-cost steps, both strands jointly provide \(S_T=\varnothing\) and \(Q_T=V\). Their total intervention cost is exactly \(2c\), proving the equality and parity conclusion. The same construction outputs an optimal full schedule from any optimal strand schedule.

**2. Count compression on a biclique.** In \(K_{a,b}\), every vertex of one part is adjacent to every vertex of the opposite part. If the active \(A\)-state has \(u\) vertices, the naturally positive next \(B\)-state consists **exactly** of the \(g(u)\) vertices whose thresholds are at most \(u\), regardless of which \(u\) vertices were active. By paying \(v-g(u)\) one can target any additional \(v-g(u)\) vertices and make the next active \(B\)-state have any prescribed cardinality \(v\) in \([g(u),b]\). It is never beneficial to pay for a vertex already naturally positive. The analogous transition from a \(B\)-state with \(v\) positives to an \(A\)-state with \(u\) positives costs \(u-f(v)\) for \(u\geq f(v)\).

Initially the natural \(A\)-state is empty; starting with \(u\) active vertices therefore costs exactly \(u\). These are precisely the source and transition arcs in the stated graph. Every finite strand schedule produces a directed source-to-state walk of identical intervention cost, and conversely every such walk can be realized as a strand schedule because the opponent neighborhood is complete. A strand saturates as soon as it reaches \(A_a\) or \(B_b\). Thus its optimum \(c\) is the minimum of the two shortest-path distances in the statement; multiplying by two gives the asserted exact timed-target value.

**3. Complexity and construction.** There are \(a+b+3\) vertices including the source and at most \((a+1)(b+1)\) arcs in each direction, plus \(a+1\) source arcs. The threshold cumulative counts \(f,g\) can be computed in \(O(a+b)\) time using threshold histograms, and all arc weights are nonnegative integers. Standard Dijkstra search and backtracking construct an optimal strand with \(O(ab\log(a+b))\) time and \(O(ab)\) space. For each transition one targets any number of vertices not yet naturally positive needed to match its next-state count. The parity argument then gives a full optimal schedule.

**4. Uniform-threshold corollary.** To saturate the \(B\)-part naturally, intervene on \(\beta\) vertices of \(A\) in one step, so \(c\leq\beta\). Alternatively, leave the first \(A\)-state empty and intervene on \(\alpha\) vertices of \(B\) at the next step to naturally saturate \(A\), giving \(c\leq\alpha\). For the reverse inequality, until at least \(\min\{\alpha,\beta\}\) vertices have been manually activated in total, no natural positive vertex can appear: the first nonempty natural update would require at least \(\alpha\) or \(\beta\) positive neighbors in the preceding state, all previously manually activated if that update is the first. Also, directly saturating one part manually costs at least \(\min\{a,b\}\geq\min\{\alpha,\beta\}\). Therefore \(c\geq\min\{\alpha,\beta\}\). Equality proves the displayed closed formula.

## Verification

The supplementary, standard-library Python program `verify.py` implements the weighted count-state Dijkstra algorithm and a separately written full-state Dijkstra algorithm that explores all intervention subsets of each binary state without parity or count compression. Running `python verify.py` produced:

```
PASS: independent full-state bicliques 168
PASS: independent all small bipartite graph instances 3860
PASS: uniform-threshold exact formula instances 3025
```

The biclique comparisons cover every pair of threshold **multisets** on \(K_{a,b}\) for \(1\leq a,b\leq3\); permutations cannot change the result on a biclique. The arbitrary-bipartite test covers all graphs of order \(2\) through \(5\) and every allowable positive threshold choice, with the trivial zero threshold on isolated vertices when present; those isolated-vertex tests extend beyond the theorem's stated domain. The uniform-threshold test covers both part sizes up to ten. These finite checks are consistency tests, not the proof of the infinite results.

A heterogeneous four-by-four witness shows why the temporal schedule matters. For thresholds on \(A\) equal to \((1,1,1,2)\) and thresholds on \(B\) equal to \((1,2,2,2)\), target **one** vertex of \(B\) at time one and again at time two (the same vertex may be targeted twice). The active cardinalities \((|A_t|,|B_t|)\) at times zero through four are, successively,
\[
 (0,0),\quad(0,1),\quad(3,1),\quad(3,4),\quad(4,4).
\]
The last state is entirely natural, with no intervention. Thus the total cost is two, and the parity lower bound shows it is optimal. The positive counts increase through multiple alternating updates rather than just one instantaneous exposure.

## Relationship to prior work

Soltani, Zehmakan and Hushmandi introduced the timed-target formulation above, established general hardness and bounds, and gave an exact linear-time tree algorithm. Their 2023 preprint's Example 1 treats the star \(K_{1,n-1}\), and the tightness example in Appendix B treats a family \(K_{2,2\ell}\) under strict-majority thresholds. Their Appendix B.3 uses an even/odd partition of intervention times to compare a graph with its bipartite double cover; the parity separation **technique** here is closely related, and no novelty is claimed merely for separating even and odd times. The present contribution is the precise equal-cost stranded optimization and, crucially, the fully heterogeneous count-state shortest-path formula, algorithm, and schedule reconstruction for every biclique—not implied by the published tree algorithm, strict-majority bounds, or these uniform-threshold special examples.

Prior work on progressive target-set selection in dense graph classes is inapplicable to the present non-progressive timed update, while static non-monotone target-set algorithms solve a different intervention model. Research-record searches found related irreversible conversion and complete-bipartite domination results, but none of the results inspected established this timed heterogeneous shortest-path reduction. That search outcome is not an exhaustive proof of first discovery.

## Limitations

The universal parity statement requires bipartiteness and strictly positive feasible thresholds. The biclique shortest-path algorithm requires complete adjacency across the two parts and unit cost for each vertex-time intervention; it is not claimed for general bipartite graphs. The result addresses exact deterministic synchronous adoption, not stochastic contagion, adversarial response, weighted intervention prices, or asynchronous updating. The linear-time tree algorithm, source examples on stars, and parity double-cover argument predate this result; they are acknowledged rather than recast as novel. Priority against all specialized older literature is not guaranteed. Formal or independent external validation has not been performed.

## References

1. H. Soltani, A. N. Zehmakan, and A. B. Hushmandi, *Minimum Target Sets in Non-Progressive Threshold Models: When Timing Matters*, arXiv:2307.09111v1, first publicly posted 18 July 2023. https://arxiv.org/abs/2307.09111 ; https://arxiv.org/pdf/2307.09111 . Relevant material: Definition 1; Example 1; Theorems 2–3 and 8; Appendix B.3; Section 4.
2. C. Baste, S. Ehard, and D. Rautenbach, *Non-monotone target sets for threshold values restricted to 0, 1, and the vertex degree*, *Discrete Mathematics & Theoretical Computer Science*, 2022. https://dmtcs.episciences.org/en/articles/6844 . This studies untimed targets with restricted thresholds.
3. P. Dvořák, D. Knop, and T. Toufar, *Target Set Selection in Dense Graph Classes*, arXiv:1610.07530. https://arxiv.org/abs/1610.07530 . This treats progressive/irreversible target selection rather than timed non-progressive intervention.
