# Four-cut homotopy of graphs without cycles of length at most five

## Finding
Let \(G=(V,E)\) be any finite simple graph on \(n\ge 6\) vertices, with no cycles of lengths \(3\), \(4\), or \(5\); disconnected graphs and forests are permitted. Write \(d(v)\) for the degree of \(v\), and put
\[
 c_4(G)=\sum_{v\in V}\binom{d(v)}3+
 \sum_{\{u,v\}\in E}(d(u)-1)(d(v)-1),
 \qquad B(G)=\binom{n-1}3-c_4(G).
\]
Let \(\Delta_4(G)\) denote the **ordinary four-cut complex**, whose facets are precisely the complements in \(V\) of four-vertex sets inducing a disconnected subgraph. Then \(B(G)\) is a nonnegative integer and
\[
 \widetilde H_j(\Delta_4(G);\mathbb Z)\cong
 \begin{cases}\mathbb Z^{B(G)},& j=n-5,\\0,&j\ne n-5.\end{cases}
\]
Moreover, for every \(n\ge8\),
\[
 \boxed{\Delta_4(G)\simeq\bigvee^{B(G)}S^{n-5}.}
\]
The same wedge conclusion also holds when \(n=6\); for \(n=7\), only the integral-homology conclusion is asserted. A wedge of zero spheres means a point.

An equivalent, more geometric statement valid for every \(n\ge6\) is that the combinatorial Alexander dual \(K=\Delta_4(G)^\vee\) satisfies
\[
 K\simeq\bigvee^{B(G)}S^2.
\]
Thus all cubic graphs of girth at least six with \(n\) vertices have the same four-cut homotopy type (for \(n\ge8\)), with multiplicity \(\binom{n-1}3-7n\). For example, the Heawood graph gives \(188\) nine-spheres (previously calculated separately), while the Möbius–Kantor graph gives \(343\) eleven-spheres.

## Assumptions and scope
All graphs are finite, undirected and simple. The absence of cycles of lengths \(3\), \(4\), and \(5\) is interpreted as girth at least six, with forests regarded as having infinite girth. No connectedness or regularity hypothesis is needed. The ordinary cut complex is not the total cut complex. Homology is reduced integral simplicial homology. The formula is for all \(n\ge6\), and the homotopy assertion for \(n\ge8\) or \(n=6\). No assertion on the homotopy type for \(n=7\) is made.

## Proof
**1. Identify the Alexander dual.** A subset \(\sigma\subseteq V\) belongs to \(\Delta_4(G)\) if and only if \(V\setminus\sigma\) contains a disconnected induced four-vertex set. By the definition of combinatorial Alexander duality,
\[
 K=\{F\subseteq V:\text{every four-element subset of }F\text{ induces a connected subgraph}\}.
\]
Hence all subsets of size at most three belong to \(K\), and a four-element subset belongs precisely when it induces a connected subgraph.

**2. Show that there are no higher faces.** Suppose a five-element set \(F\) has every four-element induced subgraph connected. Then deletion of any vertex leaves a connected graph, which forces the induced graph on \(F\) to have minimum degree at least two: deleting a neighbor of a degree-one vertex would isolate that vertex, and degree-zero vertices likewise contradict deletion-connectedness. Any finite graph of minimum degree at least two on five vertices has a cycle of length at most five. This contradicts the girth hypothesis. Every larger set contains a five-element set, so \(K\) is three-dimensional with complete two-skeleton. Its three-simplices correspond exactly to connected induced four-vertex sets.

**3. Exhibit a different free triangle for every three-simplex.** The induced graph on any connected four-element set is a tree, because it has no cycle of length at most four. It is either a claw or a four-vertex path.

If it is a claw with center \(b\) and leaves \(a,c,d\), choose the triangle \(\{a,c,d\}\). Any connected four-element set containing those three pairwise nonadjacent vertices must add a common neighbor of all three. A second common neighbor distinct from \(b\) would create a four-cycle, so the selected triangle belongs to precisely one three-simplex of \(K\).

If it is a path \(a-b-c-d\), choose \(\{a,c,d\}\). In its induced graph, \(a\) is isolated and \(c,d\) are adjacent. A fourth vertex making the set connected must be adjacent to \(a\) and to at least one of \(c,d\). Apart from \(b\), such a vertex would create a four-cycle using the route \(a-b-c\), or a five-cycle using \(a-b-c-d\), respectively. Thus this selected triangle also belongs to only that three-simplex.

All selected triangles are consequently distinct, and each pair consisting of a connected-four-set tetrahedron and its chosen triangle is an elementary simplicial collapse. Performing all these collapses gives a two-dimensional complex \(L\) with every vertex and edge present and exactly \(\binom n3-c_4(G)\) triangles.

**4. Determine the dual homotopy type.** Because \(K\) has the complete two-skeleton of the simplex on \(n\) vertices, it is simply connected (adding three-cells cannot change the fundamental group). Its collapse \(L\) is likewise simply connected. Therefore \(\widetilde H_1(L;\mathbb Z)=0\), and its reduced Euler characteristic gives
\[
 \operatorname{rank}\widetilde H_2(L;\mathbb Z)
 =\binom n3-c_4(G)-\binom n2+n-1
 =\binom{n-1}3-c_4(G)=B(G).
\]
As \(L\) is two-dimensional, this second homology is free abelian. By the Hurewicz theorem, representatives of its basis give a map from a wedge of \(B(G)\) two-spheres inducing an integral homology isomorphism. Both spaces are simply connected CW complexes, so the homological Whitehead theorem makes this a homotopy equivalence. This proves the dual wedge statement, including \(B(G)=0\).

**5. Calculate the connected-four count.** Each connected induced four-vertex tree is uniquely either a claw or a path. Claws are counted by \(\sum_v\binom{d(v)}3\). Each path has a unique central edge \(\{u,v\}\); choosing its two outer neighbors yields \((d(u)-1)(d(v)-1)\) possibilities. No choices coincide or introduce a chord, as that would create a triangle or four-cycle. This proves the formula for \(c_4(G)\).

**6. Transfer to the original cut complex.** Integral combinatorial Alexander duality on the \(n\)-vertex simplex gives
\[
 \widetilde H_j(\Delta_4(G);\mathbb Z)
 \cong\widetilde H^{n-j-3}(K;\mathbb Z).
\]
Step 4 shows that the right-hand group is \(\mathbb Z^{B(G)}\) exactly when \(n-j-3=2\), and vanishes otherwise.

To upgrade to homotopy when \(n\ge8\), note from Step 2 that every five-element vertex set contains a disconnected four-element set. Thus \(\Delta_4(G)\) contains the complete \((n-6)\)-skeleton on its \(n\) vertices. With \(d=n-5\ge3\), this makes \(\Delta_4(G)\) \((d-2)\)-connected. Its reduced homology in degree \(d-1\) vanishes by the preceding calculation, so successive Hurewicz arguments make it \((d-1)\)-connected. Attaching representatives of a basis for \(\widetilde H_d\) produces a homology equivalence \(\bigvee^{B(G)} S^d\to\Delta_4(G)\); Whitehead's theorem completes the homotopy classification. For \(n=6\), the cut complex is a connected graph with free first homology of rank \(B(G)\), hence a wedge of \(B(G)\) circles. This finishes the proof.

## Verification
The accompanying `verify.py` uses only Python's standard library. Run `python3 verify.py` to check connected induced four-set enumeration, the unique-free-triangle property, every five-set obstruction, and the formula for \(c_4(G)\). It also constructs the ordinary cut complex directly and computes its mod-two top and codimension-one Betti numbers for the small graphs in the test suite. It exhaustively treats all \(2992\) labeled six-vertex graphs with no cycles of lengths three through five, and separately checks paths, stars, forests, cycles, single-cycle graphs with a tail, two disjoint six-cycles, and the Heawood and Möbius–Kantor graphs. These finite checks corroborate the all-parameter proof, but are not an infinite proof or an independent external audit.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue [1], Theorem 6.1 and Proposition 6.2, already give the complete codimension-one skeleton, an Euler-characteristic formula, torsion-freeness, and homology confined to two possible adjacent degrees under the same no-short-cycles hypothesis. Their Theorem 6.4 classifies the ordinary two-cut case of connected triangle-free graphs, and their Proposition 7.12 and Proposition 7.13 cover forests and cycles. Those portions are not new here. The additional conclusion for arbitrary graphs of girth at least six is the vanishing of codimension-one homology and, in the stated ranges, the resulting complete wedge-of-spheres classification, obtained through free triangles in the Alexander dual. The sequel [2] studies disjoint unions, squared paths, grids and their representation theory, rather than this all-high-girth four-cut theorem.

## Limitations
The homotopy type of the original four-cut complex is not determined here for \(n=7\), although its integral homology is. The result does not classify group actions, provide canonical equivalences, establish shellability, or assert that the girth assumption is optimal. The sphere-wedge equivalence is nonequivariant. Computations at finite orders do not replace the argument for arbitrary finite graphs.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first posted 2023-04-26), especially Theorem 6.1, Proposition 6.2, and Propositions 7.12–7.13. https://arxiv.org/abs/2304.13675

[2] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (2024), especially Sections 3, 5, and 6. https://arxiv.org/abs/2407.08158
