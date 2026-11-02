# Rigidity of the disconnected matching-independent law on five vertices

## Finding

**Theorem.** Let \(G\) be a random simple graph on the labeled vertex set \([5]\), disconnected almost surely. Suppose edge indicators corresponding to disjoint edges are independent, and every edge is present with probability at least \(p\). Then
\[
p\le p_\star=\frac{1}{\sqrt5}.
\]
Equality is possible, but the entire law at equality is unique. It assigns probability
\[
a=\frac{\sqrt5-2}{5}
\]
to **each** of the five graphs consisting of a complete four-vertex component and one isolated vertex, and probability
\[
b=\frac{3-\sqrt5}{10}
\]
to **each** of the ten graphs consisting of a triangle and a separate edge. All other graphs have probability zero. Moreover, this unique extremal law satisfies full subgraph independence: induced subgraphs on disjoint vertex sets are independent (not merely indicators of disjoint edges).

Consequently, among matching-independent laws on five vertices, edge marginals strictly greater than \(1/\sqrt5\) force positive probability of connectivity, and at the boundary there is exactly one disconnected law. The analogous sharp boundary and law hold for the stronger edge-subgraph-independent and subgraph-independent classes.

## Assumptions and scope

All graphs are simple, undirected, and have the fixed labeled vertex set \(V=[5]\). Edge indicators are \(X_e=\mathbf1_{\{e\in E(G)\}}\). Matching independence means the indicators in each collection of pairwise vertex-disjoint edges are mutually independent; on five vertices the largest matching has two edges. The graph is disconnected with probability one. Marginal lower bounds need not initially be equal and symmetry of the law is **not** assumed. Full subgraph independence means the random induced graphs \(G[U]\) and \(G[W]\) are independent for any vertex-disjoint \(U,W\).

## Proof

**1. An extremal witness.** For a deterministic graph \(H\), let
\[
Q(H)=\sum_{\{e,f\}:\,e\cap f=\varnothing}\mathbf1_{\{e,f\subseteq E(H)\}},
\]
where the sum is over unordered pairs of disjoint potential edges. There are \(15\) such pairs on \(V\). Every disconnected \(H\) is contained in the union of the complete graphs on its connected components. A disconnected partition of five vertices is refined by a partition of type \(4+1\) or \(3+2\); adding edges cannot decrease \(Q\). For a complete \(K_4\) and an isolate, \(Q=3\) (the three perfect matchings of the four-set). For \(K_3\cup K_2\), \(Q=3\) (each triangle edge together with the edge in the two-set). Hence \(Q(H)\le3\). Equality forces \(H\) to be exactly one of these fifteen graphs: in either two-component maximal type, deleting any present edge destroys at least one of the three disjoint-edge pairs, and every strictly finer partition has at most one such pair.

By matching independence and marginal lower bounds,
\[
3\ge\mathbb E Q(G)
=\sum_{\{e,f\}:\,e\cap f=\varnothing}\Pr(X_e=1)\Pr(X_f=1)
\ge15p^2.
\]
Therefore \(p\le1/\sqrt5\). At equality \(p=p_\star\), equality holds in every step: \(Q(G)=3\) almost surely and all ten marginal edge probabilities equal \(p_\star\), since every edge occurs in three of the fifteen summands, each marginal is at least \(p_\star>0\), and each summand must be exactly \(p_\star^2\).

**2. Equality implies a rigid, symmetric law.** Write \(a_z\) for the mass at the graph \(K_{V\setminus\{z\}}\cup K_{\{z\}}\), and \(b_{uv}\) for the mass at \(K_{\{u,v\}}\cup K_{V\setminus\{u,v\}}\). If \(uv,wx\) are disjoint and \(z\) is the fifth vertex, both edges occur together in exactly three supported graphs: the \(4+1\) graph isolated at \(z\), and the \(3+2\) graphs with two-components \(uv\) and \(wx\). Consequently
\[
a_z+b_{uv}+b_{wx}=\frac15.\tag{1}
\]
For four distinct indices \(u,v,w,x\), applying (1) to all three perfect matchings of the same four vertices yields the four-point identities
\[
b_{uv}+b_{wx}=b_{uw}+b_{vx}=b_{ux}+b_{vw}.\tag{2}
\]
They imply the additive form \(b_{uv}=t_u+t_v\) for five real numbers \(t_u\). Indeed, choose labels \(1,2,3\), set \(t_1=(b_{12}+b_{13}-b_{23})/2\) and cyclically define \(t_2,t_3\); for \(z=4,5\) set \(t_z=b_{1z}-t_1\). The relations (2) force the formula for every remaining pair, including \(45\).

Let \(S=\sum_{v\in V}t_v\). Equation (1) gives
\[
a_z=\frac15-S+t_z.
\]
An edge \(uv\) is present in all three \(4+1\) graphs whose isolates lie outside \(\{u,v\}\); among \(3+2\) graphs it is present when the two-component is \(uv\), or is a two-subset of its complementary three-set. Thus its marginal is
\[
\Pr(X_{uv}=1)
=\sum_{z\notin\{u,v\}}a_z+b_{uv}
+\sum_{\{w,x\}\subseteq V\setminus\{u,v\}}b_{wx}
=\frac35-2(t_u+t_v).
\]
Every marginal equals \(p_\star\), so \(t_u+t_v=(3/5-p_\star)/2\) for every pair. Comparing pairs sharing one vertex forces every \(t_v\) equal. It follows that
\[
b_{uv}=\frac{3-\sqrt5}{10}=b,\qquad
 a_z=\frac{\sqrt5-2}{5}=a.
\]
This proves uniqueness without any exchangeability assumption.

**3. Attainment and stronger independence.** The constants \(a,b\) are strictly positive and obey \(5a+10b=1\). For each edge \(e\), precisely three supported \(4+1\) graphs and four supported \(3+2\) graphs contain it. Thus \(\Pr(X_e=1)=3a+4b=1/\sqrt5\). For disjoint \(e,f\), exactly one supported \(4+1\) and two supported \(3+2\) graphs contain both, so
\[
\Pr(X_e=X_f=1)=a+2b=\frac15
=\Pr(X_e=1)\Pr(X_f=1).
\]
Matching independence follows.

For full subgraph independence, it suffices to consider two nontrivial disjoint vertex sets, of sizes \(2+2\) or \(2+3\); smaller induced graphs are deterministic. The \(2+2\) case follows from matching independence. Fix a triple \(W\) and complementary edge \(e\). Under our supported law, the induced graph on \(W\) is either its triangle or exactly one of its three individual edges. By permutation invariance within \(W\), the latter outcomes have equal conditional probabilities for each state of \(X_e\), so it suffices to check the triangle event. Precisely one \(3+2\) and two \(4+1\) graphs induce the triangle on \(W\); among them only the \(3+2\) graph contains \(e\). Hence
\[
\Pr(G[W]=K_3)=b+2a,
\quad\Pr(G[W]=K_3,\ X_e=1)=b
=p_\star(b+2a).
\]
This establishes independence of \(G[W]\) and \(X_e\), and therefore of all induced graphs on disjoint vertex sets. The threshold statements follow.

## Verification

The standalone standard-library program `verify.py` exactly enumerates all \(2^{10}=1024\) labeled graphs on five vertices; checks that the bound \(Q\le3\) is sharp only for the prescribed fifteen disconnected graphs; evaluates the proposed probability law in \(\mathbb Q(\sqrt5)\); checks every edge marginal, every disjoint-edge pair and every pair of induced subgraph configurations on disjoint vertex sets; and verifies that the boundary linear constraints have full column rank \(15\). Run `python3 verify.py` from the extracted package. It returns `VERIFY_OK`. This finite exhaustive check supports, but does not replace, the analytic universal proof above.

## Relationship to prior work

The threshold \(p_\star=1/\sqrt5\) in the stronger **subgraph-independent** model is a specialization of the established finite complete-graph connectivity theorem of Day, Falgas-Ravry and Hancock [1]. Lengler and coauthors [2] introduced the hierarchy of matching-, edge-subgraph-, and subgraph-independent models and established general threshold bounds and a subgraph-independent disconnected construction. In particular their lower construction already supplies **existence** at \(p_\star\). No novelty is claimed for that existence or for the stronger model's numerical threshold. The contribution here is the **matching-independent upper bound at five vertices and the classification of every equality case, including automatic stronger independence**. These are implication-level distinctions, not merely changed terminology; no directly covering statement was located in the primary texts inspected.

## Limitations

The theorem concerns exactly five labeled vertices, disconnected laws and the boundary equality. It does not classify random graph laws with positive connectivity probability, or establish thresholds for larger orders. Historical priority remains open to broader examination, and there is no independent mathematical audit. The exact verification is finite and does not independently certify every algebraic lemma for larger vertex sets; no such generalization is claimed.

## References

[1] A. N. Day, V. Falgas-Ravry and R. Hancock, *Long paths and connectivity in 1-independent random graphs*, arXiv:1909.13771 (first public 2019-09-30), https://arxiv.org/html/1909.13771v2 .

[2] J. Lengler, A. Martinsson, K. Petrova, P. Schnider, R. Steiner, S. Weber and E. Welzl, *On connectivity in random graph models with limited dependencies*, arXiv:2305.02974 (first public 2023-05-04), https://arxiv.org/abs/2305.02974 ; full published text https://doi.org/10.1002/rsa.21220 .
