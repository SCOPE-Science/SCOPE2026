# Complete graph-metric Vietoris–Rips filtration of the Desargues configuration

## Finding

Let \(\mathcal D\) be the incidence graph whose vertices are all two-element and three-element subsets of \([5]=\{1,2,3,4,5\}\), with an edge between a pair and a triple precisely when the pair is contained in the triple. This is the twenty-vertex, thirty-edge Desargues graph. Equip its vertices with the unit-edge shortest-path distance and use inclusive Vietoris–Rips complexes, \(K_r=\mathrm{VR}_{\le}(\mathcal D;r)\), for real \(r\ge0\). Then

\[
|K_r|\simeq
\begin{cases}
\bigsqcup^{20}\mathrm{pt},&0\le r<1,\\
\bigvee^{11}S^1,&1\le r<2,\\
\bigvee^{19}S^2,&2\le r<3,\\
S^3,&3\le r<4,\\
S^9,&4\le r<5,\\
\mathrm{pt},&r\ge5.
\end{cases}
\]

At scale three the forbidden-distance graph is exactly \(P\square K_2\), where \(P\) is the Petersen graph, and hence \(K_3\cong\operatorname{Ind}(P\square K_2)\) as abstract simplicial complexes. In particular the independence complex of the Petersen prism is homotopy equivalent to \(S^3\).

The complete nonzero positive-dimensional barcode over **every field** has eleven degree-one intervals \([1,2)\), nineteen degree-two intervals \([2,3)\), one degree-three interval \([3,4)\), and one degree-nine interval \([4,5)\). In degree zero there are nineteen intervals \([0,1)\) and one interval \([0,\infty)\). All integral homology at every scale is torsion-free.

The scale-two wedge decomposition is a special case of the previously established Feng–Nukala result and is **not independently claimed as new**. The substantive additional determination is the scale-three sphere and the resulting complete persistent homology of the Desargues graph, with a reproducible integral proof.

## Assumptions and scope

The graph is finite and has **vertices only**, not the continuous edge realization. The metric is unit-edge shortest-path distance. The filtration is inclusive: a nonempty finite subset is a face exactly when all its pairwise distances are at most \(r\). No claim is made about Euclidean embeddings, weighted graph metrics, other incidence structures, or noninteger threshold conventions.

The five integer values of positive distances are exactly the symmetric-difference sizes of the corresponding subsets of \([5]\). Indeed a graph edge toggles one element. Conversely, swapping one element while remaining on a two- or three-element layer takes two incidence steps, and each mixed-size pair has a path attaining its symmetric-difference distance by appropriate alternating insertions and deletions. Thus, for all vertices \(A,B\), \(d_{\mathcal D}(A,B)=|A\triangle B|\). This identity is also checked exhaustively in the accompanying verifier.

## Proof

**Scale zero and one.** The distance-one flag complex is the graph itself because it is bipartite and triangle-free. It is connected with twenty vertices and thirty edges, so its cycle rank is \(30-20+1=11\). Below distance one its vertices are isolated.

**Scale two.** Enumerate all maximal cliques in the distance-at-most-two graph by the deterministic Bron–Kerbosch rule specified in the attached verifier and close them under faces. The exact face vector in dimensions zero to three is \((20,90,120,30)\). The verifier gives thirty elementary free-face collapses, removing all tetrahedra and leaving a two-dimensional complex with vector \((20,90,90)\). For the fundamental group, contract the lexicographically selected spanning tree in its one-skeleton; every edge in the tree is trivial. Apply triangle relations repeatedly: whenever two boundary edges of a triangle are already trivial, its third is trivial. The explicit certificate reaches all ninety edges in five rounds. Consequently \(\pi_1(K_2)=1\). The surviving two-complex has Euler characteristic \(20-90+90=20\), so its reduced integral second homology is free of rank nineteen. The Hurewicz theorem and homological Whitehead theorem identify its homotopy type with nineteen two-spheres, independently consistent with Feng–Nukala, Theorem 13, specialized to two- and three-subsets of a five-element set.

**Scale three: independent-set description.** Distances exceeding three are exactly symmetric differences of sizes four and five. Apply the complement map on the three-subsets to label both ten-vertex layers by two-subsets. On either layer, two vertices are forbidden precisely when the underlying two-subsets are disjoint, so each layer's forbidden graph is the Petersen graph. The only forbidden cross-layer pairs are corresponding complementary pair–triple pairs, forming a perfect matching. The full forbidden graph is therefore the Cartesian prism \(P\square K_2\), and the allowed clique complex is its independence complex.

**Scale three: exact integral calculation.** The complete scale-three complex has face vector \((20,150,540,1000,960,450,80)\) and 110 inclusion-maximal simplices. A deterministic sequence of **1,040 ordinary elementary simplicial collapses**, each verified to remove a codimension-one free face with exactly one proper coface, leaves a three-dimensional complex \(L\) with face vector \((20,150,540,410)\). The attached standalone program constructs every simplex from scratch and executes the full sequence rather than trusting saved logs.

Orient each triangle and tetrahedron by increasing vertex labels. The exact integral boundary matrix \(\partial_3:C_3(L;\mathbb Z)\to C_2(L;\mathbb Z)\) has size \(540\times410\). Repeated unimodular row/column elimination at entries \(\pm1\) gives **409 unit pivots and one entirely zero residual column**; no nonzero residual matrix remains. Every operation is an invertible integer elementary operation. Hence its image is a primitive rank-409 sublattice of \(C_2\), and its kernel is \(\mathbb Z\).

The inclusion \(K_2\hookrightarrow K_3\) surjects on fundamental groups: an added distance-three edge is homotopic across a two-simplex to an existing two-edge path of length at most two in the distance-two graph. Thus \(K_3\) is simply connected. Because \(L\) has connected one-skeleton, \(\operatorname{rank}\partial_1=19\); simple connectivity forces \(\operatorname{rank}\partial_2=150-19=131\). Since \(540-131=409\), the primitive image of \(\partial_3\) equals \(\ker\partial_2\) and \(H_2(L;\mathbb Z)=0\). Therefore \(L\) is simply connected with \(H_3(L;\mathbb Z)=\mathbb Z\) and zero other reduced integral homology. Hurewicz produces a map \(S^3\to L\) inducing a homology isomorphism; the homological Whitehead theorem makes this a homotopy equivalence. Hence \(K_3\simeq S^3\).

**Scales four and five.** Exactly ten unordered pairs are at distance five, and these pairs partition all twenty vertices. Thus the scale-four flag complex excludes precisely ten opposite vertex pairs, making it the tenfold join of \(S^0\), the boundary of the ten-dimensional cross-polytope and hence \(S^9\). At scale five every pair is allowed, so the complex is a simplex.

**Persistence.** Every positive-dimensional homology group is concentrated in a different dimension at each successive noncontractible stage. Thus no positive-dimensional persistence class can survive its next integer threshold, while the stated ranks determine all bars. The graph becomes connected exactly at threshold one, giving the degree-zero barcode. All assertions are over integral chains except where explicit mod-two checks are described.

## Verification

Run `python3 verify_desargues.py` with a recent Python 3 standard library. The program has no external dependencies, downloads, or input files. It enumerates all graph distances and maximal distance-threshold cliques, constructs their faces, checks every free-face pair before deleting it, proves the fundamental-group edge-generator reduction by exact triangle relations, computes independent mod-two boundary ranks, and carries out full integer unit elimination on \(\partial_3\). The expected completion marker is `VERIFY_OK`.

The verified distance-pair counts at distances one through five are \((30,60,60,30,10)\). The scale-two collapse has thirty pairs, five rounds of triangle-generator propagation, and nineteen two-dimensional homology generators. The scale-three collapse has 1,040 pairs; its residual tetrahedral boundary matrix has 409 unit pivots and one zero column. There are ten antipodal pairs and 1,024 scale-four maximal facets. These are complete finite checks on a fixed twenty-vertex graph, not extrapolations from a sample of parameters.

## Relationship to prior work

Adamaszek and Adams (first publicly posted 2015-03-12) develop the homotopy and persistence framework for Vietoris–Rips complexes of circles, with primary MSC 55U10; their circle classification does not cover the Desargues configuration. Feng and Nukala (arXiv:2302.14664, Theorem 13) already treat the scale-two two-and-three-subset metric and imply the nineteen-two-sphere term above; their paper explicitly focuses on scale two and states that larger-scale subset Rips complexes are poorly understood. Saleh, Titz Mite and Witzel (arXiv:2302.14388) give the full graph-metric filtration of the **dodecahedral** graph. It has the same number of vertices and edges as the Desargues graph but has a different scale-two and scale-three homotopy type, including nine three-spheres rather than the single three-sphere found here. This dodecahedral theorem is not being reformulated as a new result. Carnero Bravo (arXiv:2505.06457) studies independence complexes of several graph products, especially categorical and strong products of paths, not the Cartesian Petersen prism identified at scale three here.

## Limitations

This is a complete, exact result for one canonical finite graph, not a general theorem for every \((10_3)\) configuration, cubic graph, or graph product. Its primary proof of the nonstandard scale-three calculation uses a finite, fully executable free-face and integral-chain certificate. The certificate's logic is auditable and does not purport to give an independent external validation. Neither a complete survey of unpublished work nor priority over inaccessible or unindexed literature is established. The present review is internal to the mathematical argument; no independent audit has been performed.

## References

1. M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, first public version 2015-03-12, arXiv:1503.03669v1, published in *Pacific Journal of Mathematics* 290 (2017), 1–40. The published version lists primary MSC 55U10.
2. Z. Feng and N. C. P. Nukala, *On Vietoris–Rips complexes of finite metric spaces with scale 2*, arXiv:2302.14664, Theorem 13 and Section 7.
3. N. Saleh, T. Titz Mite and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388, main theorem and Section 2.
4. A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457, introduction and graph-product definitions.
