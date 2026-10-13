# Edge general position number of crown graphs
## Finding
For every integer \(n\ge3\), let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},
\qquad
B=\{b_1,\ldots,b_n\},
\]
where
\[
M=\{a_i b_i:1\le i\le n\}
\]
is the deleted perfect matching. Then
\[
\operatorname{gp}_{\mathrm e}(\operatorname{Cr}_n)
=
\left\lfloor\frac{n^2}{2}\right\rfloor.
\]

More precisely, identify each crown edge \(a_i b_j\), \(i\ne j\), with the arc
\[
i\to j
\]
of a loopless digraph on \(\{1,\ldots,n\}\). An edge set is in edge general position if and only if the associated digraph contains no transitive directed triangle.

A sharp construction is obtained by partitioning the index set as evenly as possible,
\[
[n]=P\mathbin{\dot\cup}Q,
\]
and selecting every crown edge whose two indices lie in different classes, in both directions. This gives
\[
2|P||Q|
=
2\left\lfloor\frac n2\right\rfloor
 \left\lceil\frac n2\right\rceil
=
\left\lfloor\frac{n^2}{2}\right\rfloor
\]
selected edges.

## Assumptions and scope
All graphs are finite, simple, connected, and undirected. An edge set \(X\subseteq E(G)\) is in edge general position when no geodesic of \(G\) contains three edges from \(X\). The edge general position number \(\operatorname{gp}_{\mathrm e}(G)\) is the maximum cardinality of such a set.

The crown graph \(\operatorname{Cr}_n\) has diameter \(3\) for \(n\ge3\). Its only geodesics with three edges join the uniquely nonadjacent matched vertices \(a_i\) and \(b_i\).

## Proof
Write
\[
e_{ij}=a_i b_j
\qquad (i\ne j).
\]
Because \(\operatorname{Cr}_n\) has diameter \(3\), an edge set fails to be in edge general position exactly when it contains all three edges of a length-\(3\) geodesic.

Every length-\(3\) geodesic has the form
\[
a_i-b_j-a_k-b_i
\]
for pairwise distinct \(i,j,k\). Its three edges are
\[
e_{ij},\qquad e_{kj},\qquad e_{ki}.
\tag{1}
\]
Associate \(e_{uv}\) with the arc \(u\to v\). Then the three arcs in (1) are
\[
i\to j,\qquad k\to j,\qquad k\to i,
\]
which form a transitive directed triangle with ordering
\[
k\to i\to j
\]
and shortcut \(k\to j\). Conversely every transitive directed triangle gives a geodesic of the form (1). Hence an edge set \(X\) is in edge general position exactly when its associated loopless digraph \(D_X\) is transitive-triangle-free.

We now bound the number \(m\) of arcs of any transitive-triangle-free loopless digraph \(D\) on \(n\) vertices. For every arc
\[
u\to v,
\]
the out-neighborhoods of \(u\) and \(v\) are disjoint: a common out-neighbor \(w\) would create
\[
u\to v,\qquad v\to w,\qquad u\to w.
\]
Thus
\[
d^+(u)+d^+(v)\le n.
\tag{2}
\]
Similarly, the in-neighborhoods of \(u\) and \(v\) are disjoint, so
\[
d^-(u)+d^-(v)\le n.
\tag{3}
\]

Summing (2) over all arcs gives
\[
\sum_x d^+(x)^2+\sum_x d^+(x)d^-(x)\le mn.
\tag{4}
\]
Summing (3) gives
\[
\sum_x d^-(x)^2+\sum_x d^+(x)d^-(x)\le mn.
\tag{5}
\]
Adding (4) and (5),
\[
\sum_x\bigl(d^+(x)+d^-(x)\bigr)^2\le2mn.
\tag{6}
\]
Since
\[
\sum_x\bigl(d^+(x)+d^-(x)\bigr)=2m,
\]
Cauchy--Schwarz and (6) imply
\[
\frac{4m^2}{n}
\le
\sum_x\bigl(d^+(x)+d^-(x)\bigr)^2
\le
2mn.
\]
For \(m>0\), this yields
\[
m\le\frac{n^2}{2},
\]
hence
\[
m\le\left\lfloor\frac{n^2}{2}\right\rfloor.
\]

For the matching construction, choose a balanced partition
\[
[n]=P\mathbin{\dot\cup}Q
\]
and take both arcs between every cross-pair. The underlying undirected graph of this digraph is complete bipartite, hence triangle-free, so the digraph contains no transitive directed triangle. It has
\[
2|P||Q|
=
\left\lfloor\frac{n^2}{2}\right\rfloor
\]
arcs. Translating back to crown edges proves the theorem.

## Verification
The included verifier independently builds the forbidden geodesic triples using the crown adjacency pattern. It exhaustively checks every edge subset for
\[
n=3,4,5
\]
and determines the true maximum directly.

It also constructs the balanced bidirected-cut witness for every
\[
3\le n\le20
\]
and checks directly that no transitive directed triangle occurs.

The exhaustive maxima are \(4,8,12\), respectively, agreeing with
\[
\left\lfloor\frac{n^2}{2}\right\rfloor.
\]

## Relationship to prior work
Edge general position was introduced in 2021. The foundational paper determines the parameter for hypercubes, trees, and two-dimensional grids and explicitly points to bipartite graphs as a direction for further study. It contains no crown-graph or complete-bipartite occurrence in the inspected searchable text.

The cases \(n=3\) and \(n=4\) are not new special cases: \(\operatorname{Cr}_3\cong C_6\), whose edge general position number is \(4\), and \(\operatorname{Cr}_4\cong Q_3\), whose value is \(8\). The theorem extends these isolated instances to every crown graph.

A 2024 paper characterizes several extremal edge-general-position regimes and develops block-graph results; its searchable full text contains no crown or complete-bipartite treatment. A 2025 paper studies diameter-\(3\) graphs with edge general position number equal to size minus \(2\) and characterizes graphs with value \(4\); its available full text likewise contains no crown or complete-bipartite occurrence.

Targeted literature searches under the standard crown name, \(K_{n,n}\) minus a perfect matching, deleted-matching terminology, and the transitive-triangle reformulation did not locate the stated all-\(n\) formula.

## Limitations
The theorem determines the maximum cardinality but does not classify all maximum edge general position sets.

The proof uses the exact crown structure; it does not claim the same formula for arbitrary regular bipartite graphs or for \(K_{n,n}\) with a nonperfect matching deleted.

The exhaustive computation through \(n=5\) is corroborative only. The all-\(n\) result follows from the transitive-triangle equivalence and the degree-sum upper bound.

A differently phrased or non-indexed crown result may exist despite the targeted searches.

## References
1. P. Manuel, R. Prabha, S. Klavžar, “Edge general position problem,” arXiv:2105.04292v1, 10 May 2021; Bulletin of the Malaysian Mathematical Sciences Society 45 (2022), 2997–3009, DOI 10.1007/s40840-022-01319-8.
2. J. Tian, S. Klavžar, E. Tan, “Extremal Edge General Position Sets in Some Graphs,” arXiv:2302.01587v1, 3 February 2023; Graphs and Combinatorics 40 (2024), Article 40, DOI 10.1007/s00373-024-02770-z.
3. Y. Cao, S. Ji, L. Wang, “The Edge General Position Number of Some Graphs,” Bulletin of the Malaysian Mathematical Sciences Society 48 (2025), DOI 10.1007/s40840-025-01873-x.
