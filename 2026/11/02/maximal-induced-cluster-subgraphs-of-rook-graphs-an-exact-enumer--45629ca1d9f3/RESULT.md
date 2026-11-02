# Maximal induced cluster subgraphs of rook graphs: an exact enumerator and cardinality gaps

## Finding

For positive integers \(a,b\), let \(R_{a,b}=K_a\square K_b\), with one vertex for each cell of an \(a\)-by-\(b\) board and adjacency between distinct cells in the same row or column. A cluster graph is a disjoint union of cliques. Write \(\mathcal C_{a,b}(z)\) for the polynomial whose coefficient of \(z^s\) is the number of **inclusion-maximal vertex subsets** of \(R_{a,b}\) inducing cluster graphs and having size \(s\).

Let \(S_{\ge2}(n,k)\) count partitions of an \(n\)-element labeled set into \(k\) blocks, each of size at least two, and let \((q)_k=q!/(q-k)!\) for \(0\le k\le q\). With empty sums interpreted as zero, the following identity holds for all \(a,b\ge1\):

\[
\begin{aligned}
\mathcal C_{a,b}(z)={}&a!b!\,[x^a y^b]\exp\bigl(x(e^{zy}-1)+y(e^{zx}-1)-zxy\bigr)\\
&+z^a\sum_{k=1}^{\min(b-1,\lfloor a/2\rfloor)}(b)_k S_{\ge2}(a,k)\\
&+z^b\sum_{k=1}^{\min(a-1,\lfloor b/2\rfloor)}(a)_k S_{\ge2}(b,k).
\end{aligned}
\]

If \(2\le a\le b\), the exact support is
\[
\operatorname{supp}(\mathcal C_{a,b})=\{a\}\cup\{b,b+1,\ldots,a+b-2\}.
\]
If \(a=1\), the polynomial is simply \(z^b\). In particular, for every \(b\ge2\),
\[
\boxed{\mathcal C_{2,b}(z)=b z^2+2^b z^b.}
\]
Thus all sizes strictly between \(2\) and \(b\) are absent whenever \(b\ge4\). As a second exact consequence, for \(a,b\ge3\), the number of maximum-cardinality such sets is \(ab\), and their common size is \(a+b-2\). The complements of the counted sets are precisely inclusion-minimal cluster vertex-deletion sets.

## Assumptions and scope

All graphs are finite, simple, undirected and labeled by their given vertex sets. Both shores of the complete bipartite graph used below are nonempty. Inclusion-maximality refers to adding any one vertex to the induced cluster subgraph, not to maximum possible cardinality. The polynomial counts distinct labeled subsets, not isomorphism types.

A star includes a one-edge star. In a bipartite graph a star forest is an edge set whose non-isolated components are stars; original vertices incident to no selected edge are called *unused*. The variable \(z\) marks selected rook vertices, equivalently selected bipartite edges.

## Proof

**Line-graph reduction.** Identify the cell \((i,j)\) with the edge between row vertex \(i\) and column vertex \(j\) in \(K_{a,b}\). Then \(R_{a,b}\cong L(K_{a,b})\). For an edge set \(F\subseteq E(K_{a,b})\), the induced graph \(L(K_{a,b})[F]=L((V,F))\) is a cluster graph exactly when \((V,F)\) is a star forest. Indeed, a cluster graph is characterized by forbidding induced three-vertex paths. If a component of \((V,F)\) has three edges forming a path, its line graph contains an induced three-vertex path. Conversely, if a connected triangle-free graph is not a star, it contains a path of three edges; three consecutive edges on a shortest such path induce a three-vertex path in its line graph. Hence a connected, non-isolated component yielding a clique line graph is necessarily a star. Bipartiteness excludes the triangle alternative for clique line graphs.

**Maximality criterion.** Consider a star forest \(F\) on the two labeled shores \(A,B\). If an unused vertex exists in both \(A\) and \(B\), adding the edge joining them creates a new one-edge component, so \(F\) is not maximal. If every original vertex is used, then every missing bipartite edge joins distinct nontrivial star components; adding it produces a connected non-star component (it contains two original edges on different sides of the new edge, making a three-edge path). Therefore every full-support star forest is maximal.

Suppose that all vertices of \(A\) are used, while at least one vertex of \(B\) is unused. Any component centered in \(A\), or any one-edge component, can be enlarged by an edge from its \(A\)-vertex to an unused \(B\)-vertex while remaining a star forest. Thus maximality forces every selected component to be centered in \(B\) and to contain at least two leaves from \(A\). Conversely, these conditions imply maximality: a new edge to unused \(B\) attaches at a leaf of a star with at least two leaves, creating a non-star; an edge joining already-used vertices of distinct components also creates a non-star. The symmetric statement holds with the two shores exchanged. These three classes are disjoint: full support; full \(A\)-support but incomplete \(B\)-support; full \(B\)-support but incomplete \(A\)-support.

**Counting.** A full-support star forest is an unordered labeled set of star components. A star with one \(A\)-center and \(r\ge1\) \(B\)-leaves contributes \(xz^r y^r/r!\) to the two-sort exponential generating function, and symmetrically a star centered in \(B\) contributes \(yz^r x^r/r!\). One-edge stars occur in both forms and must be subtracted once, yielding the component series \(x(e^{zy}-1)+y(e^{zx}-1)-zxy\). The labeled exponential formula, without singleton-vertex components, proves the first term in the displayed polynomial.

For the second class, choose \(k\) distinct \(B\)-centers and partition all \(a\) vertices of \(A\) into \(k\) nonempty blocks of size at least two, assigning one block to each center. The number is \((b)_kS_{\ge2}(a,k)\), and incomplete \(B\)-support imposes \(k\le b-1\); the degree constraint imposes \(2k\le a\). Every such forest contains exactly \(a\) edges. The symmetric class contributes the third term. No configurations are double-counted.

**Support and extremal multiplicity.** Assume \(2\le a\le b\). In the full-support class, each component consumes at least one \(A\)-vertex, and at least two components are necessary because neither shore is a singleton. Hence the number \(k\) of components lies between \(2\) and \(a\), and the number of selected edges is \(a+b-k\). Every \(k\) in this interval occurs: choose one \(B\)-center with \(a-k+1\) \(A\)-leaves and \(k-1\) other \(A\)-centers, distributing the remaining \(b-1\) \(B\)-vertices among those centers with at least one each. The one-edge component convention permits \(k=a\). Thus the full-support sizes are exactly \(b,b+1,\ldots,a+b-2\). The two incomplete-support classes contribute only sizes \(a\) and \(b\), and size \(a\) occurs by taking one star with all \(a\) vertices as leaves and one of the \(b\) possible centers. This proves the support formula.

For \(a=2\), the full-support forests assign each of the \(b\) column vertices to one of the two row centers, using both centers; there are \(2^b-2\). The incomplete-\(A\)-support class consists of the two full-size stars centered in one row, while the incomplete-\(B\)-support class consists of the \(b\) two-edge stars centered in one column. This proves \(\mathcal C_{2,b}(z)=b z^2+2^b z^b\), with coincident degrees combined when \(b=2\). If \(a,b\ge3\), a full-support forest of maximum size has two nontrivial star components, necessarily one centered in each shore. Choosing the two centers freely determines the forest, giving exactly \(ab\) maximum sets. For \(a=1\) the rook graph is a clique, with its whole vertex set as its unique maximal induced cluster subgraph.

## Verification

The included standard-library script `verify_cluster_rook.py` directly constructs each rook graph and enumerates vertex subsets, independently testing clusterhood by pairwise adjacency of selected neighbors and testing inclusion-maximality by adding every omitted vertex. It compares the resulting full coefficient dictionary to a separately implemented recurrence for full-support star forests plus restricted set-partition counts. Direct tests include twelve dimensions from \(1\times1\) through \(4\times4\), including \(2\times7\), and an additional 221 support checks for dimensions \(1\le a\le13\), \(1\le b\le17\). Run `python3 verify_cluster_rook.py`; its recorded result is `VERIFY_OK direct_graphs=12 direct_subsets=120694 support_pairs=221`.

The unrestricted theorem is established by the bijection, maximality proof, and labeled exponential formula; finite testing alone would not prove it.

## Relationship to prior work

Y. Cao's *Enumerating Maximal Induced Subgraphs* (arXiv:2004.09885, first posted 2020-04-21; later ESA 2023) gives general algorithms for listing maximal induced subgraphs in hereditary classes, including cluster graphs. It does not state the present all-parameter rook-graph counting polynomial in its inspected relevant sections. H.-O. Le and V. B. Le's *Complexity of the Cluster Vertex Deletion Problem on H-Free Graphs* (MFCS 2022, DOI:10.4230/LIPIcs.MFCS.2022.68) studies the complexity of deleting vertices to obtain cluster graphs, not the present labeled size distribution. The equivalence between cluster graphs and induced-three-vertex-path-free graphs is standard and is not claimed new. The novelty proposed here is the full inclusion-maximal size enumerator, its three-part classification, and the exact size gaps for rook graphs.

## Limitations

This is an all-parameter mathematical derivation supported by finite direct tests, not an independent peer-reviewed validation. The searches and inspected primary texts did not reveal an identical theorem, but they cannot exclude unindexed or inaccessible earlier enumerations. The result concerns **vertex deletion** to a cluster graph, not the distinct operation of deleting edges to obtain a cluster graph. It counts labeled subsets and does not enumerate isomorphism classes.

## References

1. Y. Cao, *Enumerating Maximal Induced Subgraphs*, arXiv:2004.09885v1 (2020-04-21), https://arxiv.org/abs/2004.09885; later ESA 2023.
2. H.-O. Le and V. B. Le, *Complexity of the Cluster Vertex Deletion Problem on H-Free Graphs*, MFCS 2022, DOI:10.4230/LIPIcs.MFCS.2022.68, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2022.68.
