# A torus spine for open-neighborhood complexes of triangular cycle cylinders

## Finding
Let \(n\ge5\), let \(G_n=K_3\mathbin\square C_n\) be the Cartesian product graph, and let \(\mathcal N(G_n)\) be its **open** Lovász neighborhood complex. There is an explicit sequence of exactly \(6n\) elementary simplicial collapses
\[
\mathcal N(G_n)\searrow T_n,
\qquad |T_n|\cong_{\mathrm{PL}}S^1\times S^1,
\qquad f(T_n)=(3n,9n,6n).
\]
Here \(T_n\) is the explicitly described, connected, closed orientable triangulated surface below. Consequently, \(\pi_1(\mathcal N(G_n))\cong\mathbb Z^2\), its reduced integral homology is \(\widetilde H_1\cong\mathbb Z^2\), \(\widetilde H_2\cong\mathbb Z\), and zero otherwise, and the integral degree-one cup pairing is unimodular. In particular, it is **not** a wedge of spheres.

For every \(n\ge6\) divisible by \(3\), the graph \(G_n\) is a connected **noncirculant** four-regular graph. Thus these infinitely many cases are not covered by the existing classification of four-regular circulant neighborhood complexes; they also lie outside the recently studied \(K_m\square C_n\) regime \(m\ge4\).

## Assumptions and scope
The vertices are \(v_{i,a}\) for \(i\in\mathbb Z/n\mathbb Z\) and \(a\in\mathbb Z/3\mathbb Z\). Adjacency means equal \(i\) and unequal \(a\), or equal \(a\) and cycle coordinates differing by one. The open neighborhood of \(v_{i,a}\) is
\[
F_{i,a}=\{v_{i,a+1},v_{i,a+2},v_{i-1,a},v_{i+1,a}\}.
\]
The complex \(\mathcal N(G_n)\) consists of the nonempty subsets of these four-vertex sets. Its facets are exactly the \(3n\) tetrahedra \(F_{i,a}\), all distinct when \(n\ge5\). The open-neighborhood condition excludes each center from its own generating set. All modular indices below are taken in their indicated cyclic groups.

## Proof
**1. Unique opposite-layer edge and the local collapses.** For any center \((i,a)\), set \(L=v_{i-1,a}\), \(R=v_{i+1,a}\), \(P=v_{i,a+1}\), and \(Q=v_{i,a+2}\). The edge \(e_{i,a}=\{L,R\}\) occurs in exactly one generating tetrahedron, namely \(F_{i,a}=\{L,R,P,Q\}\). Indeed the two vertices are in the same color but their cycle coordinates are distance two apart, and for \(n\ge5\) their unique common **graph neighbor** is \(v_{i,a}\). In a neighborhood complex, the generating tetrahedra containing a face are indexed by its common graph neighbors.

The triangle \(\{L,R,P\}\) is therefore a free face of \(F_{i,a}\), and we collapse the pair \((\{L,R,P\},F_{i,a})\). After its removal, the edge \(e_{i,a}\) occurs in exactly the remaining triangle \(\{L,R,Q\}\), making \((e_{i,a},\{L,R,Q\})\) a free pair. Repeat these two genuine elementary collapses for every \((i,a)\), in arbitrary fixed order. Faces containing different edges \(e_{i,a}\) cannot coincide: each such edge has a unique center, and these pairs are disjoint. Exactly \(2(3n)=6n\) pairs are removed; no other faces disappear.

**2. Description of the surviving triangles.** The other two triangles of \(F_{i,a}\) are \(\{L,P,Q\}\) and \(\{R,P,Q\}\), since the removed triangles were precisely those containing both \(L\) and \(R\). Thus the surviving complex \(T_n\) consists of every face of the triangles
\[
A_{i,a}=\{v_{i,a+1},v_{i,a+2},v_{i+1,a}\},\quad
B_{i,a}=\{v_{i,a},v_{i+1,a+1},v_{i+1,a+2}\}
\]
for \(i\in\mathbb Z/n\mathbb Z\) and \(a\in\mathbb Z/3\mathbb Z\). Each is unique, giving \(6n\) triangles. The edges are the \(3n\) edges in the triangular columns and the \(6n\) edges between consecutive columns with differing colors. These are distinct for \(n\ge5\). There are \(3n\) vertices, so \(f(T_n)=(3n,9n,6n)\) and Euler characteristic \(0\).

**3. The surface and its orientation.** Each cross-column edge \(\{v_{i,b},v_{i+1,a}\}\), where \(a\ne b\), occurs in exactly two of the triangles in step 2: one with its other vertex in column \(i\) and one with its other vertex in column \(i+1\). Each within-column edge likewise occurs in exactly two triangles, one in the preceding strip and one in the following strip. For a fixed column vertex, its simplicial link has six vertices and six edges, forming a single six-cycle (its two neighbors in the same column and four neighbors in adjacent columns). Thus \(|T_n|\) is a closed connected triangulated two-manifold. Connectedness is immediate from its cross-column and within-column edges, which form a connected spanning graph.

Orient each triangle \(A_{i,a}\) by \((v_{i,a+1},v_{i,a+2},v_{i+1,a})\) and each triangle \(B_{i,a}\) by \((v_{i,a},v_{i+1,a+2},v_{i+1,a+1})\). The two induced orientations on every edge are opposite: this follows directly by checking the two types of edges just identified. Hence these orientations form a coherent global orientation; in particular, the surface is orientable. By the classification of connected closed orientable surfaces, Euler characteristic zero implies \(|T_n|\cong_{\mathrm{PL}}S^1\times S^1\). Since elementary collapses preserve homotopy type, all asserted homotopy, cohomology and integral cup-product conclusions follow.

**4. A genuinely noncirculant infinite subfamily.** The only three-cycles in \(G_n\), for \(n\ge5\), are its \(n\) three-vertex complete-graph fibers. Any automorphism must permute these fibers, inducing a dihedral automorphism of the base cycle. Because consecutive fibers are joined by exactly a matching pairing equal color labels, the color permutation must be the same in every fiber. Consequently \(\operatorname{Aut}(G_n)\cong S_3\times D_n\). When \(3\mid n\), every element of this group has order at most \(2n<3n\): a rotation has order dividing \(n\), a reflection order two, and a color permutation order one, two or three. A circulant graph on \(3n\) vertices necessarily has an automorphism acting as a \(3n\)-cycle. Thus \(G_n\) is not a circulant graph for \(3\mid n\). The collapse in steps 1–3 nevertheless applies to these graphs, supplying an infinite noncirculant torus family.

## Verification
The standalone file `verify_triangular_cylinder_neighborhood.py` reconstructs all open-neighborhood simplices from the generating neighborhoods, checks **each actual free-face pair** and the precise final face set, verifies all edge incidences and cancellation of the signed fundamental two-cycle, and checks every vertex link is a connected cycle. It passes for every \(5\le n\le14\), checking \(570\) individual elementary pairs in total and reproducing the expected f-vectors. This bounded exhaustive calculation verifies concrete instances; the arbitrary-\(n\) theorem is proved by the symbolic local and surface arguments above.

## Relationship to prior work
Shukla [1, Theorems 6(C), 14 and Lemma 12] classifies the neighborhood complexes of four-regular **circulant** graphs, often as connected sums of tori, and gives related local collapse methods. The present theorem makes no novelty claim for its overlapping circulant subfamily (notably \(3\nmid n\)); its infinite \(3\mid n\) subfamily is **not circulant**, as proved above, and hence not covered by that theorem. The exact uniform \(6n\)-step collapse and identified triangulated core are also a direct constructive statement, rather than a consequence of the classifying phrase “connected sum of tori.”

The recent study [2] determines \(\mathcal N(K_m\square C_n)\) for \(m\ge4,n\ge5\), obtaining a wedge with fundamental group \(\mathbb Z\), and explicitly makes no claim for \(m=3\). The present theorem resolves precisely this boundary case and finds a qualitatively different answer, namely the aspherical torus with nontrivial degree-one cup product. A separate toroidal square-grid theorem [3] assumes no nonzero period shorter than five in the Manhattan metric, excluding the triangular \(C_3\) fiber and its length-three cycles. Graphs and input complexes therefore differ, and its theorem does not entail the present one.

## Limitations
The proof requires \(n\ge5\). It does not classify the short cycles \(n=3,4\), higher clique sizes, or any equivariant actions on homology. The old circulant results are explicitly acknowledged where they apply; the new unexcluded range is \(3\mid n\), \(n\ge6\), and the uniform explicit collapse description. Searches and accessible primary-text comparisons do not eliminate the possibility of an unindexed equivalent treatment of noncirculant triangular cylinders. No independent external audit has been performed.

## References
[1] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, *Electron. J. Combin.* 26(2) (2019), P2.4, https://doi.org/10.37236/7549; first preprint arXiv:1802.04526 (2018-02-13).

[2] *Mixed-dimensional neighborhood homotopy of complete-graph cycle products*, public research record posted 2026-10-11, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-mixed-dimensional-neighborhood-homotopy-of-complete-graph-cycle--3a53c8927b3c/RESULT.md .

[3] *Toroidal grid neighborhood complexes collapse to one or two tori*, public research record posted 2026-10-11, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-toroidal-grid-neighborhood-complexes-collapse-to-one-or-two-tori--737edf71bc86/RESULT.md .
