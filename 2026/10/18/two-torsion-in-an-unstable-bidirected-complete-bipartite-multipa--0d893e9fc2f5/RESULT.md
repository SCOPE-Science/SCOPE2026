# Two-torsion in an unstable bidirected complete-bipartite multipath complex

## Finding

Let \(G=\overleftrightarrow{K}_{2,4}\) denote the six-vertex digraph obtained by replacing every edge of the undirected complete bipartite graph \(K_{2,4}\) by both orientations. Let \(X(G)\) be its multipath simplicial complex: the vertices of \(X(G)\) are the sixteen arcs of \(G\), and its simplices are arc subsets inducing vertex-disjoint directed paths and isolated vertices.

Then

\[
\widetilde H_i(X(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{7}\oplus\mathbb Z/2\mathbb Z,&i=2,\\
0,&i\ne2.
\end{cases}
\]

Moreover, \(G\) is its own **unique dynamical module**, and that module is unstable in the definitions of Caputi, Collari, Di Trani, and Smith (2022). Consequently, this finite example contradicts their stated conjectural implication that torsion in the homology of a multipath complex of a dynamical module can occur only for stable modules.

## Assumptions and scope

Write the bipartition of \(G\) as \(L=\{0,1\}\) and \(R=\{2,3,4,5\}\). Its arcs are exactly \(u\to v\) and \(v\to u\) for every \(u\in L\) and \(v\in R\). No loops or multiple arcs with identical ordered endpoints occur; opposite orientations are separate arcs. Integral simplicial homology uses the increasing arc-index orientation defined in `CHECK.py`.

An arc subset is a multipath exactly when each graph vertex has in-degree and out-degree at most one in the selected arcs, and the selected directed graph contains no directed cycle (including directed two-cycles). Every arc touches one of the two left vertices, so each multipath contains at most four arcs. Therefore \(X(G)\) has dimension three, with exact face vector \((f_0,f_1,f_2,f_3)=(16,80,144,72)\).

The claim concerns this explicitly defined **bidirected** graph, not an alternating orientation of \(K_{2,4}\), an ordinary graph matching complex, a directed flag complex, or path homology.

## Proof

**Integral chain computation.** Enumerate each nonempty subset of at most four of the sixteen arcs and keep it precisely when its selected in-degrees and out-degrees are bounded by one and all selected directed cycles are absent. The complete enumeration contains respectively \(16,80,144,72\) simplices in dimensions zero through three. No higher simplex is possible by the preceding left-vertex degree bound.

Apply the deterministic acyclic matching described in `CHECK.py`. Scan arc indices in increasing order. At each index, scan the currently unpaired nonempty simplices by increasing cardinality and then incidence mask, and pair a simplex not containing the arc with its one-arc extension whenever both simplices remain. This constructs exactly \(147\) pairs. Orient every codimension-one face incidence downward except paired incidences, which are oriented upward; a complete topological sort visits all \(312\) simplices and thereby rules out every closed gradient path. The critical cells number \(1,1,12,4\) in dimensions \(0,1,2,3\).

Over \(\mathbb Z\), cancel the matched adjacent-dimensional cells using their unit incidence coefficients, updating the entire cellular boundary by integral elementary operations. The executable check finds a unit pivot at each of the \(147\) stages and verifies that the resulting boundary squares to zero. Its nonzero critical-cell differentials have sizes

\[
\partial_2:\mathbb Z^{12}\longrightarrow\mathbb Z,
\qquad
\partial_3:\mathbb Z^{4}\longrightarrow\mathbb Z^{12}.
\]

With critical cells ordered by increasing arc mask, the exact first matrix is
\[
\partial_2=(-1,1,0,0,0,0,0,1,0,1,-1,1).
\]
The exact second matrix is
\[
\partial_3=\begin{pmatrix}
1&0&0&-1\\
0&-1&1&0\\
0&1&0&-1\\
0&-1&0&1\\
1&0&-1&0\\
-1&0&1&0\\
-1&0&0&-1\\
1&0&0&1\\
0&-1&-1&0\\
0&1&1&0\\
0&0&2&0\\
0&0&0&-2
\end{pmatrix}.
\]

Direct multiplication gives \(\partial_2\partial_3=0\). Their nonzero Smith factors are \((1)\) and \((1,1,1,2)\), respectively. Because \(\partial_2\) is surjective, its kernel is a primitive rank-eleven sublattice of \(\mathbb Z^{12}\); the image of \(\partial_3\) lies in that kernel. The Smith factors of \(\partial_3\) therefore yield

\[
H_1=0,\qquad
H_2\cong\mathbb Z^{11}/\operatorname{im}\partial_3
\cong\mathbb Z^7\oplus\mathbb Z/2\mathbb Z,\qquad
H_3=0.
\]
The critical zero-cell and the surjectivity of \(\partial_2\) give \(H_0\cong\mathbb Z\). Integral unit cancellations preserve integral homology, so these are the groups of \(X(G)\).

**Unstable and unique dynamical module.** A vertex is called stable if it is a source or a sink, and a dynamical region is a connected full subgraph satisfying, among other conditions, that each boundary vertex is stable in the region (Definitions 4.1–4.2 of the cited 2022 work). All six vertices of \(G\) have positive in-degree and positive out-degree, so the full graph is unstable. Suppose a proper connected full subgraph \(R\) with at least one arc were a dynamical region. Every chosen arc belongs to a directed two-cycle in \(G\); condition (b) of Definition 4.2 forces its opposite arc also into \(R\). Thus each vertex of the connected nonempty-edge subgraph \(R\) is incident to an opposite-arc pair and has both positive in-degree and positive out-degree in \(R\), so no vertex of \(R\) is stable there. A proper edge subgraph \(R\) has a nonempty boundary (as \(G\) is connected), contradicting condition (a), which demands that each boundary vertex be stable in \(R\). Thus there is no proper dynamical region with an edge. The full graph is a dynamical region with empty boundary, so it is the unique minimal one: the unique dynamical module. Its second homology contains an element of order two, disproving the stated torsion-implies-stability implication.

## Verification

`CHECK.py` is a self-contained executable (Python 3 with SymPy) that enumerates the full finite complex, verifies the matching by directed-acyclicity, performs every unit cancellation with signed integer coefficients, and checks the two Smith normal forms and resulting homology. `FIELD_CHECK.py` independently rebuilds the complex with a distinct ordering of arcs and reports dimensions \((\dim H_1,\dim H_2,\dim H_3)=(0,8,1)\) in characteristic two and \((0,7,0)\) in characteristics three, five, seven, and eleven. The field check corroborates but does not replace the integral Smith calculation. `CHECK_OUTPUT.txt` records the actual successful executions.

To reproduce from one directory, run `python CHECK.py` and `python FIELD_CHECK.py`. The proof does not extrapolate from a sample of graphs: enumeration is exhaustive for the single six-vertex graph and the 16 specified arcs.

## Relationship to prior work

Caputi, Collari, Di Trani, and Smith (arXiv:2208.04656v1, 9 August 2022) defined the relevant dynamical regions and explicitly conjectured that torsion of a dynamical module's multipath complex forces stability. Their calculations cover oriented polygons, linear graphs, some grids, transitive tournaments, and alternating complete-bipartite Euler characteristics, but not this bidirected graph. Caputi, Collari, and Ramos (arXiv:2401.01248v1, 2 January 2024) proved bounded-torsion results under genus restrictions and a matching-complex comparison for digraphs **without directed cycles**. The latter comparison does not apply here, since every undirected edge of \(G\) produces a directed two-cycle. Their Example 4.5 concerns three-torsion in alternating orientations of \(K_{5,5}\), not this order-two torsion in an unstable bidirected module. The foundational path-poset paper of Caputi, Collari, and Di Trani develops other sample multipath complexes but does not contain the present computation.

## Limitations

This proves an explicit counterexample and the integral homology of a single digraph. It does not assert minimality among all unstable modules, classify all bidirected complete bipartite examples, or determine the complete homotopy type. Although finite-field agreement is independently checked, an independent mathematical audit of the integral certificate has not been performed. An unindexed equivalent computation may exist.

## References

1. L. Caputi, C. Collari, S. Di Trani, and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (first public 2022-08-09), in particular Definitions 2.1–2.2 and 4.1–4.2 and the torsion conjecture in the introduction. https://arxiv.org/abs/2208.04656
2. L. Caputi, C. Collari, and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248v1 (2024-01-02), in particular Section 4 and Example 4.5. https://arxiv.org/abs/2401.01248
3. L. Caputi, C. Collari, and S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, Journal of Algebraic Combinatorics (first published online 2022-11-10), DOI:10.1007/s10801-022-01180-9, in particular Sections 5 and 6. https://doi.org/10.1007/s10801-022-01180-9
