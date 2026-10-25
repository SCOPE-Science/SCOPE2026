# Positive pair-connectivity covariance in weighted cactus arboreal gases

## Finding
Let \(G=(V,E)\) be any finite connected simple **cactus graph** (each edge lies on at most one simple cycle). Fix arbitrary positive edge fugacities \(\beta_e>0\). Sample a spanning forest \(F\subseteq E\) with probability proportional to \(\prod_{e\in F}\beta_e\). For any two unordered vertex pairs \(\{x,y\}\) and \(\{u,v\}\), with distinct endpoints within each pair, write \(A=\{x\leftrightarrow y\}\) and \(B=\{u\leftrightarrow v\}\) for their respective connectivity events in \(F\).

**Theorem.** For all such graphs, weights, and pairs, \(\operatorname{Cov}(\mathbf 1_A,\mathbf 1_B)\geq0\). More precisely, let \(\mathcal B(x,y)\) be the set of bridge-edge or simple-cycle blocks traversed by the unique block-tree route joining \(x\) to \(y\). Then
\[
\operatorname{Cov}(\mathbf 1_A,\mathbf 1_B)>0
\quad\Longleftrightarrow\quad
\mathcal B(x,y)\cap\mathcal B(u,v)\ne\varnothing.
\]
If the two block-route supports are disjoint, the two events are **independent**, not merely uncorrelated. The two terminal pairs may share vertices or coincide.

This gives an all-fugacity, heterogeneous-weight subfamily of the general positive connectivity-correlation problem, together with an exact strictness and independence criterion.

## Assumptions and scope
The host is finite, connected, simple, and cactus. Every edge activity \(\beta_e\) is finite and strictly positive. A spanning forest includes all vertices but may have many connected components. The edge-subset probability is \(\mathbb P(F)=Z^{-1}\prod_{e\in F}\beta_e\), over all acyclic edge subsets. The theorem is not asserted for graphs with overlapping simple cycles, correlated edge activities, zero or infinite edge weights, or random-cluster parameters other than the forest case.

The blocks of a cactus consist of its bridges and its simple cycles; they meet only at articulation vertices. The vertex--block incidence graph (original vertices joined to blocks containing them) is a tree. Its unique path between two distinct original vertices identifies the traversed blocks \(\mathcal B(x,y)\). At every traversed cycle, the entry and exit vertices differ.

## Proof
**1. Independent block measures.** Every simple cycle of a cactus is an edge-disjoint block, and no other simple cycle exists. A chosen edge set is acyclic exactly when it omits at least one edge from each cycle block. Since forest weights factor over edges, the restrictions to different blocks are independent. A bridge block retains its edge with probability \(p_e=\beta_e/(1+\beta_e)\in(0,1)\). Within a cycle block, the edge indicators are independent Bernoulli variables with probabilities \(p_e\), conditioned on not retaining every edge.

**2. Positive covariance of any two nontrivial connectivity events on one cycle.** Consider a cycle \(C\) and two distinct-vertex pairs on it. Each pair divides the cycle edges into two nonempty complementary arcs; the pair is connected in the retained forest precisely when **all missing edges** lie inside one of its two arcs. Overlay the two arc bipartitions, obtaining four disjoint cells \(C_{11},C_{12},C_{21},C_{22}\), some possibly empty. Define their *failure odds* by
\[
 a=\prod_{e\in C_{11}}p_e^{-1}-1,\quad
 b=\prod_{e\in C_{12}}p_e^{-1}-1,\quad
 c=\prod_{e\in C_{21}}p_e^{-1}-1,\quad
 d=\prod_{e\in C_{22}}p_e^{-1}-1.
\]
Thus \(a,b,c,d\geq0\), each strictly positive exactly when its cell is nonempty. Relative to the weight of retaining all edges, the weight of choosing a nonempty set of missing edges inside a cell equals its failure odds. Conditioning on at least one failure gives normalizing factor
\[
 Z_C=(1+a)(1+b)(1+c)(1+d)-1.
\]
The first pair's connectivity event requires failures to be confined to one row, and the second pair's event to one column. Their respective unnormalized weights are
\[
 U=a+b+ab+c+d+cd,\qquad V=a+c+ac+b+d+bd.
\]
Their intersection requires all failures to lie in a single cell, so its unnormalized weight is \(S=a+b+c+d\). Therefore
\[
 Z_C^2\operatorname{Cov}(\mathbf1_A,\mathbf1_B)=SZ_C-UV.
\]
Direct polynomial expansion yields the **nonnegative certificate**
\[
\begin{aligned}
 SZ_C-UV={}&ad\big[(a+d)(1+b)(1+c)+b+c+bc\big]\\
 &+bc\big[(b+c)(1+a)(1+d)+a+d+ad\big]+2abcd.
\end{aligned}
\]
Because both arc partitions are nontrivial, at least one diagonally opposite cell pair is simultaneously nonempty, i.e. \(ad>0\) or \(bc>0\): if the first row has any nonempty cell and its other row is also nonempty, and simultaneously each column is nonempty, the occupied-cell incidence bipartite graph necessarily contains a two-edge matching. Consequently the displayed certificate is strictly positive. Hence the two local cycle-connectivity indicators have strictly positive covariance for arbitrary positive edge weights.

**3. Global covariance and equality.** By the unique vertex--block route, a terminal-pair connectivity indicator is the product, over blocks, of the local connection indicator across that route; blocks not traversed contribute the constant one. For a traversed bridge, this is the edge-retention indicator; for a traversed cycle, it is the event in Step 2 between its entry and exit vertices. The two global events can thus be written \(\mathbf1_A=\prod_B A_B\) and \(\mathbf1_B=\prod_B B_B\), using independent blocks and local indicators (possibly one). Consequently
\[
\mathbb P(A\cap B)=\prod_B\mathbb E[A_BB_B],
\qquad \mathbb P(A)\mathbb P(B)=\prod_B\mathbb E[A_B]\mathbb E[B_B].
\]
Every local expectation is strictly positive. For a block traversed by both routes, the local covariance is strictly positive: at a bridge it equals \(p_e(1-p_e)>0\), and at a cycle it is positive by Step 2. For blocks traversed by at most one route, the two factors agree. Multiplying the inequalities proves nonnegative global covariance, strictness exactly when a block is shared, and independence when supports are disjoint. \(\square\)

## Verification
The standalone `verify.py` uses exact rational arithmetic. It checks the four-cell polynomial identity for all nonnegative integer \(a,b,c,d\leq3\), and independently exhausts all acyclic edge subsets for weighted cycles of lengths three through seven, two triangles meeting at a vertex, two triangles joined by a bridge, and a triangle bridged to a four-cycle. It compares the signs of all distinct pairs of connectivity events with the intersection of their unique block-route supports, for **1,095 exact assertions**. Run \`python verify.py\` with Python 3 standard library only. These finite tests corroborate, but do not replace, the symbolic and block-factorization proof for arbitrary finite cacti.

## Relationship to prior work
Huang, *On Negative Correlation of Arboreal Gas on Some Graphs* (arXiv:2311.00965v1, November 2, 2023) introduces the same weighted spanning-forest measure and analyzes negative **edge** correlations on selected graphs, rather than this all-weights joint **vertex-pair connectivity** theorem. Çiçeksiz and Ravichandran, *Negative Correlation for Forests and the \(q<1\) Random-Cluster Model* (arXiv:2610.00549v1, September 30, 2026), Section 6, formulate the general positive two-pair connectivity-covariance inequality (Conjecture 6.2) and establish asymptotic high-fugacity results (Proposition 6.1). The cactus theorem above verifies an explicit, structurally defined subfamily for **all** heterogeneous positive edge activities and settles its equality cases. Neither the general conjecture nor a general arbitrary-graph connectivity theorem is claimed here.

## Limitations
This theorem covers cactus graphs only. Nothing is proved here for arbitrary graphs, overlapping cycles, or nonforest random-cluster models. The proof is an exact all-finite-sizes argument, and no asymptotic graph limit is asserted. The priority comparison is limited to the specified relevant accessible literature and database searches; a more remote equivalent theorem could exist. No independent external audit has been performed.

## References
1. Xiangyu Huang, *On Negative Correlation of Arboreal Gas on Some Graphs*, arXiv:2311.00965v1 (2023-11-02). https://arxiv.org/abs/2311.00965.
2. R. Altar Çiçeksiz and Mohan Ravichandran, *Negative Correlation for Forests and the \(q<1\) Random-Cluster Model*, arXiv:2610.00549v1 (2026-09-30), Section 6, Conjecture 6.2 and Proposition 6.1. https://arxiv.org/abs/2610.00549.
3. Gourab Ray and Ben Xiao, *Forests on wired regular trees*, ALEA 19 (2022), 1035–1043. https://alea.impa.br/articles/v19/19-42.pdf.
