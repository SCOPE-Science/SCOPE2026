# Paths are the unique expected-range maximizers

## Definitions

Let \(G\) be a finite connected simple graph and fix a root \(o\in V(G)\).
For a connected bipartite graph, let \(\mathcal H(G,o)\) be the set of integer-valued
functions \(f\) with \(f(o)=0\) and
\[
 |f(u)-f(v)|=1\qquad(uv\in E(G)).
\]
Write
\[
 \widehat h(G)=\mathbb E_{f\in\mathcal H(G,o)}
 \left(\max_V f-\min_V f\right).
\]
For every connected graph, let \(\mathcal L(G,o)\) be the corresponding set with
\(|f(u)-f(v)|\le 1\), and define
\[
 h(G)=\mathbb E_{f\in\mathcal L(G,o)}
 \left(\max_V f-\min_V f\right).
\]
Both expectations are independent of the chosen root.

Yinfeng Zhu recently proved the Benjamini--Häggström--Mossel expectation inequality
\(\widehat h(G)\le \widehat h(P_n)\) for every connected bipartite \(n\)-vertex
simple graph, and derived the Loebl--Nešetřil--Reed inequality
\(h(G)\le h(P_n)\) for every connected \(n\)-vertex simple graph.  The latter was
shown there to be strict when \(G\) contains a cycle.

## Main theorem

**Theorem 1 (unique maximizers).**

1. For every finite connected bipartite simple graph \(G\) on \(n\) vertices,
   \[
   \boxed{\widehat h(G)=\widehat h(P_n)\quad\Longleftrightarrow\quad G\cong P_n.}
   \]
2. For every finite connected simple graph \(G\) on \(n\) vertices,
   \[
   \boxed{h(G)=h(P_n)\quad\Longleftrightarrow\quad G\cong P_n.}
   \]

Thus the path is not merely a maximizer in either expectation problem: it is the
unique maximizer up to isomorphism.

## Equality mechanism in the BHM proof

Let \(G=(B,W;E)\) be connected and bipartite.  Following Zhu, form the auxiliary
graph \(S_B\) on \(B\), joining two vertices when they have a common neighbour in
\(W\).  For a uniform standard height function, restriction to \(B\), after the
usual rescaling, gives a weighted lazy height function on \(S_B\).  If \(K_B\) is
the number of components of its full zero-edge subgraph and \(b_j=\widehat h(P_{j+1})\),
Zhu's single-class comparison is
\[
 \mathbb E b_{K_B-1}\le
 \mathbb E b_{Y_{|B|-1,1/2}},
\]
where \(Y_{d,1/2}\sim\operatorname{Bin}(d,1/2)\).

The proof of that comparison yields the following exact equality criterion.

**Lemma 2 (single-class equality criterion).**  Equality holds in the preceding
single-class comparison if and only if

- \(S_B\) is a tree (allowing the one-vertex tree), and
- every edge of \(S_B\) has exactly one common neighbour in \(W\).

### Proof

If \(S_B\) contains a cycle, Zhu's Proposition 4.4 gives strict inequality.
Suppose therefore that \(S_B\) is a tree.  In this case every \(w\in W\) has at
most two neighbours in \(B\), since three neighbours would create a triangle in
\(S_B\).  For an edge \(e=uv\) of \(S_B\), let \(t_e\) be the number of vertices
of \(W\) whose neighbourhood is exactly \(\{u,v\}\).  The edge increment in the
weighted lazy model is nonzero with probability
\[
 p_e=\frac{2}{2^{t_e}+2}\le\frac12,
\]
and these edge increments are independent.  Hence \(K_B-1\) is a sum of
independent Bernoulli variables with parameters \(p_e\), coupled coordinatewise
below independent fair Bernoulli variables.

The sequence \(b_j\) is strictly increasing.  Therefore the expectation is equal
to the fair-binomial expectation exactly when every \(p_e=1/2\), equivalently
\(t_e=1\) on every edge.  Because \(S_B\) is a tree, every common neighbour of
the endpoints of an auxiliary edge has degree exactly two into \(B\), so \(t_e\)
is exactly their codegree in \(W\).  This proves the criterion. \(\square\)

The same criterion holds after interchanging \(B\) and \(W\).

## Proof of Theorem 1, standard model

Zhu's proof decomposes the standard expected range into the two bipartition
classes and then applies the two single-class comparisons.  Consequently, if
either single-class comparison is strict, then
\(\widehat h(G)<\widehat h(P_n)\).

Assume both comparisons are equalities.  By Lemma 2, both auxiliary graphs
\(S_B,S_W\) are trees.  Since the neighbourhood of any vertex in one
bipartition class forms a clique in the opposite auxiliary graph, neither class
can contain a vertex of degree at least three in \(G\).  Hence \(\Delta(G)\le2\).
A connected graph of maximum degree at most two is a path or a cycle.

Because \(G\) is bipartite, a cycle would be \(C_{2m}\).  If \(m\ge3\), each
same-class auxiliary graph is a cycle \(C_m\), contradicting the tree condition.
For \(C_4\), each auxiliary graph is \(K_2\), but its unique edge has two common
neighbours in the opposite class, contradicting the codegree-one condition in
Lemma 2.  Therefore \(G\) must be a path.

Conversely, Zhu's path decomposition is exact: both auxiliary graphs are paths,
every auxiliary edge has one common neighbour, and the comparison gives equality.
This proves part 1, including the trivial one-vertex case. \(\square\)

## A standard-to-lazy gap transfer

The equality statement for the lazy model follows from a quantitative relation
that may be useful separately.

For connected bipartite \(G\), set
\[
 p_G=\frac{|\mathcal H(G,o)|}{|\mathcal L(G,o)|}.
\]
This is precisely the probability that a uniform lazy height function has no
zero edge.

**Theorem 3 (gap transfer).**  For every connected bipartite \(n\)-vertex simple
graph,
\[
\boxed{
 h(P_n)-h(G)
 \;\ge\;
 p_G\bigl(\widehat h(P_n)-\widehat h(G)\bigr).
}
\]
In particular, for every \(n\)-vertex tree \(T\),
\[
 h(P_n)-h(T)
 \ge
 \left(\frac23\right)^{n-1}
 \bigl(\widehat h(P_n)-\widehat h(T)\bigr).
\]

### Proof

For a uniform lazy height function \(f\), let \(A_f\) be its full set of zero
edges and let \(K\) be the number of components of \((V(G),A_f)\).  Contracting
the zero-edge components gives a connected bipartite graph \(G/A_f\) on \(K\)
vertices, and Zhu's zero-edge contraction identity gives
\[
 h(G)=\mathbb E\,\widehat h(G/A_f).
\]
Applying the BHM inequality to every quotient,
\[
 \mathbb E b_{K-1}-h(G)
 =\mathbb E\bigl[b_{K-1}-\widehat h(G/A_f)\bigr]\ge0.
\]
On the event \(A_f=\varnothing\), which has probability \(p_G\), we have
\(K=n\) and \(G/A_f=G\).  Keeping only this nonnegative contribution gives
\[
 \mathbb E b_{K-1}-h(G)
 \ge p_G\bigl(\widehat h(P_n)-\widehat h(G)\bigr).
\]
Zhu's contraction comparison also gives
\(\mathbb E b_{K-1}\le h(P_n)\), proving the displayed inequality.
For a tree, lazy edge increments are independent and uniform in
\(\{-1,0,1\}\), so \(p_T=(2/3)^{n-1}\). \(\square\)

## Proof of Theorem 1, lazy model

If \(G\) is bipartite and is not a path, part 1 makes the standard-model gap
strict, while \(p_G>0\).  Theorem 3 therefore gives \(h(G)<h(P_n)\).
If \(G\) is nonbipartite, it contains a cycle, and the strictness assertion in
Zhu's LNR corollary already gives \(h(G)<h(P_n)\).  A path itself clearly attains
\(h(P_n)\).  This proves part 2. \(\square\)

## Relation to prior work

The direct source is Yinfeng Zhu, *Paths maximize the expected range of
graph-indexed random walks*, arXiv:2609.19728 (17 September 2026).  The paper
proves the non-strict BHM inequality for all connected bipartite graphs and the
non-strict LNR inequality for all connected graphs, with strictness in the lazy
model when the graph contains a cycle.  It does not state the BHM equality
classification, and its Remark 5.6 explicitly notes that its contraction
comparison does not by itself assert equality for every tree in the LNR
inequality.

Earlier work of Wu, Xu, and Zhu, *Average Range of Lipschitz Functions on Trees*
(Moscow Journal of Combinatorics and Number Theory 6(1), 2016, 96--116), proves
the two expectation inequalities for trees.  Bok and Nešetřil later extended
the inequalities to unicyclic graphs.  Searches for equality cases, unique
maximizers, and equivalent formulations did not locate a result classifying all
connected bipartite BHM equality cases, all connected LNR equality cases, or the
gap-transfer inequality above.

## Limitations and originality scope

Originality is asserted only **to the best of our knowledge**.  The complete
2016 Wu--Xu--Zhu manuscript was not inspected in full; accessible indexed and
secondary theorem statements record the non-strict tree inequalities, so a
body-only tree equality remark remains a residual risk.  Such a remark would
not by itself cover the all-connected-bipartite equality classification or the
general standard-to-lazy gap transfer proved here.  The 2026 source is very
recent, so unindexed parallel work is an additional residual risk.

This result concerns equality in the expectation inequalities only.  It does
not resolve the stronger stochastic-domination form of the BHM conjecture.

## Sources

- Y. Zhu, *Paths maximize the expected range of graph-indexed random walks*, arXiv:2609.19728: https://arxiv.org/abs/2609.19728
- Y. Wu, Z. Xu, Y. Zhu, *Average Range of Lipschitz Functions on Trees*, Moscow Journal of Combinatorics and Number Theory 6(1) (2016), 96--116: https://mjcnt.phystech.edu/en/article.php?id=108
- J. Bok, J. Nešetřil, *Graph-indexed random walks on pseudotrees*, Electronic Notes in Discrete Mathematics 68 (2018), 263--268: https://doi.org/10.1016/j.endm.2018.06.045
