# Minimum quasi-total Roman functions of connected chain graphs
## Finding
Let \(G=(X,Y,E)\) be a connected chain graph with
\[
s=|X|\ge2,
\qquad
t=|Y|\ge2.
\]
Define the universal classes
\[
U_X=\{x\in X:N(x)=Y\},
\qquad
U_Y=\{y\in Y:N(y)=X\},
\]
and put
\[
u=|U_X|,
\qquad
v=|U_Y|.
\]
Both classes are nonempty.

The minimum quasi-total Roman domination number
\[
\gamma_{qtR}(G)=4
\]
is prior work. The new result is a complete classification and count of every minimum function.

Every minimum quasi-total Roman dominating function belongs to exactly one of the following four families.

**Universal-pair family.** Choose
\[
x\in U_X,
\qquad
y\in U_Y,
\]
assign
\[
f(x)=f(y)=2,
\]
and assign \(0\) to every other vertex.

**Two-vertex \(X\)-side family.** This family exists only when \(s=2\). Choose
\[
x\in U_X
\]
for label \(2\), assign label \(1\) to the other vertex of \(X\), choose an arbitrary vertex of \(Y\) for a second label \(1\), and assign \(0\) elsewhere.

**Two-vertex \(Y\)-side family.** Symmetrically, this family exists only when \(t=2\).

**All-one four-vertex family.** This single function exists only when
\[
s=t=2,
\]
and assigns label \(1\) to all four vertices.

Consequently the exact number of minimum quasi-total Roman dominating functions is
\[
N_{qtR}^{\min}(G)
=
uv
+
\mathbf 1_{s=2}\,ut
+
\mathbf 1_{t=2}\,vs
+
\mathbf 1_{s=t=2}.
\tag{1}
\]

For the half graph \(H_n\) with \(n\ge3\), each universal class is a singleton and both bipartition classes have order at least \(3\). Hence \(H_n\) has a unique minimum quasi-total Roman dominating function: its two universal vertices receive label \(2\), and every other vertex receives label \(0\).

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. A quasi-total Roman dominating function is a map
\[
f:V(G)\to\{0,1,2\}
\]
such that every vertex labeled \(0\) has a neighbor labeled \(2\), and every vertex labeled \(2\) has a positive-labeled neighbor. Its weight is
\[
\omega(f)=\sum_{z\in V(G)}f(z).
\]

A chain graph is a bipartite graph whose neighborhoods on either side are linearly ordered by inclusion. Connectedness implies that the maximum-neighborhood class on each side is universal to the opposite side, so \(U_X\) and \(U_Y\) are nonempty.

The theorem covers the nonstar connected chain graphs, namely \(s,t\ge2\). The scalar minimum \(4\) is published prior work and is not used as the originality basis.

## Proof
The prior scalar theorem gives
\[
\gamma_{qtR}(G)=4.
\]
We therefore classify all feasible label multisets of total weight \(4\).

The positive labels can have only one of three multisets:
\[
\{2,2\},
\qquad
\{2,1,1\},
\qquad
\{1,1,1,1\}.
\]

Suppose first that the positive labels are \(\{2,2\}\). The two label-\(2\) vertices cannot lie in the same bipartition class: vertices within one class are nonadjacent, so the two label-\(2\) vertices would have no positive neighbor and the quasi-total condition would fail. Hence one label \(2\) lies in \(X\) and one in \(Y\), say at \(x\) and \(y\).

Every zero in \(Y\) must be adjacent to \(x\). Since all vertices of \(Y\setminus\{y\}\) are zero and \(x\) must also be adjacent to \(y\) in order to support its positive label, we obtain
\[
N(x)=Y,
\]
so \(x\in U_X\). Symmetrically \(y\in U_Y\). Conversely, every pair from \(U_X\times U_Y\) gives a valid function. This is the universal-pair family, with \(uv\) functions.

Now suppose the positive labels are \(\{2,1,1\}\), with the label \(2\) at some \(x\in X\). No other vertex of \(X\) is adjacent to \(x\). Therefore every vertex of
\[
X\setminus\{x\}
\]
must be positive; otherwise such a zero would have no adjacent label \(2\). At least one of the two label-\(1\) vertices must also lie in \(Y\) in order to give \(x\) a positive neighbor. Hence exactly one label \(1\) remains available for \(X\setminus\{x\}\), forcing
\[
s=2.
\]
The other vertex of \(X\) has label \(1\), while the remaining label \(1\) can be placed at some \(y\in Y\). Every other vertex of \(Y\) is zero and must see \(x\); the positive vertex \(y\) must also be adjacent to \(x\) to support the label \(2\). Thus
\[
x\in U_X.
\]
Conversely, every such choice is valid. This gives \(ut\) functions when \(s=2\). The case where the unique label \(2\) lies in \(Y\) is symmetric and gives \(vs\) functions when \(t=2\).

Finally suppose all four positive labels are \(1\). With no label \(2\), no vertex may be labeled \(0\). Therefore the graph has exactly four vertices, so
\[
s=t=2,
\]
and the all-one function is the unique function of this type.

The four families are disjoint and exhaustive, proving (1).

For the half graph \(H_n\), the nested neighborhoods are strict. Hence \(u=v=1\). When \(n\ge3\), neither small-side family nor the all-one family is available, so (1) gives exactly one minimum function.

## Verification
The included verifier generates every connected canonical chain-graph type of total order \(4\) through \(8\) with both bipartition classes of order at least \(2\). For each graph it enumerates every ternary labeling, tests the two quasi-total Roman conditions directly, determines all minimum functions, and compares them with the four-family theorem and formula (1).

The verifier checks \(114\) canonical chain-graph types and \(484{,}218\) ternary labelings. It also explicitly checks the three-by-three half graph boundary used in the prior-work comparison.

## Relationship to prior work
Quasi-total Roman domination was introduced in 2019. A 2021/2022 algorithmic paper subsequently determines the scalar minimum for connected chain graphs. For bipartition classes of sizes at least \(2\), its Theorem 7 states
\[
\gamma_{qtR}(G)=4,
\]
and Theorem 8 gives a linear-time optimization algorithm. Those scalar and algorithmic results are prior work.

The present result determines **every** minimum labeling and its exact multiplicity. In particular, the optimizer count depends only on the two side sizes and the cardinalities of the two universal twin classes, despite the potentially richer nested-neighborhood structure in between.

The published proof of the scalar chain theorem orders the neighborhoods as
\[
N(x_1)\subseteq\cdots\subseteq N(x_s),
\qquad
N(y_1)\supseteq\cdots\supseteq N(y_t),
\]
and displays a weight-four function placing label \(2\) at \(x_s\) and \(y_t\). Under that stated ordering, \(x_s\) is universal but \(y_t\) need not be. The three-by-three half graph gives an immediate counterexample to that displayed labeling: the pair \(x_3,y_3\) is not a quasi-total Roman dominating function, whereas the universal pair \(x_3,y_1\) is. The scalar theorem remains correct; the universal-pair family above supplies the valid general construction and the complete optimizer classification.

Targeted searches using chain graph, Ferrers graph, half graph, quasi-total Roman domination, minimum-function, and enumerative terminology did not locate this optimizer classification or count.

## Limitations
The theorem classifies minimum functions only, not the full quasi-total Roman weight enumerator of arbitrary chain graphs.

Stars and \(K_2\) are excluded because their published scalar minima are \(3\) and \(2\), respectively, and their minimum-function structures are different.

The finite exhaustive verification is corroborative only. The arbitrary-chain result follows from the weight-four case analysis.

A differently phrased or non-indexed optimizer enumeration may exist despite the targeted searches.

## References
1. S. Cabrera-García, A. Cabrera-Martínez, I. G. Yero, “Quasi-total Roman domination in graphs,” arXiv:1903.09789v1, 23 March 2019; Results in Mathematics 74 (2019), Article 173, DOI 10.1007/s00025-019-1097-5.
2. V. Mangal, P. Venkata Subba Reddy, “Algorithmic aspects of quasi-total Roman domination in graphs,” Communications in Combinatorics and Optimization 7 (2022), 93–104, DOI 10.22049/CCO.2021.27126.1200; published online 30 April 2021.
3. A. Cabrera Martínez, J. C. Hernández-Gómez, J. M. Sigarreta, “On the Quasi-Total Roman Domination Number of Graphs,” Mathematics 9 (2021), 2823, DOI 10.3390/math9212823.
