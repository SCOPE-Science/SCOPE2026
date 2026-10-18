# Ordinary three-cut complexes of Möbius ladders are sphere wedges

## Finding
For an integer \(n\ge4\), let \(M_{2n}\) be the Möbius ladder on \(V=\mathbb Z/(2n)\mathbb Z\), whose edges join \(i\) to \(i+1\) and \(i\) to \(i+n\) (all indices modulo \(2n\)). Define the **ordinary three-cut complex** \(\Delta_3(M_{2n})\) by the facets \(V\setminus T\), where \(T\subseteq V\) has three vertices and \(M_{2n}[T]\) is disconnected. Then
\[
\Delta_3(M_{2n})\simeq\bigvee^{2n^2-8n+1} S^{2n-4}\qquad(n\ge4).
\]
This is an integral homotopy classification: \(\widetilde H_{2n-4}(\Delta_3(M_{2n});\mathbb Z)\cong\mathbb Z^{2n^2-8n+1}\), and all other reduced integral homology groups vanish. At the natural smallest included case, the Wagner graph \(M_8\) gives \(\Delta_3(M_8)\simeq S^4\); the ranks for \(n=5,6,7,8\) are respectively \(11,25,43,65\). No statement is made about total cut complexes, for which the defining triples must be independent.

## Assumptions and scope
All complexes are abstract simplicial complexes over the fixed ground vertex set \(V\). A face of \(\Delta_3(G)\) is precisely a vertex set whose complement contains a disconnected induced triple. The combinatorial Alexander dual \(L=\Delta_3(M_{2n})^*\) consists of sets having **no** disconnected triple. Hence \(L\) has the complete one-skeleton, and its triangles are exactly the connected induced triples. Here \(n\ge4\) is essential to ensure that the only four-cycles are the obvious antipodal-rung squares and that each rim distance-two chord identifies a unique connected triple.

## Proof
**1. Face classification.** The Möbius ladder is cubic and triangle-free for \(n\ge4\). A connected induced triple is therefore a two-edge path. There are exactly \(6n\) such triples: \(2n\) rim triples
\[
R_j=\{j,j+1,j+2\},\qquad j\in\mathbb Z/(2n)\mathbb Z,
\]
and, for each \(i\in\{0,\ldots,n-1\}\), the four triples of the square
\[
Q_i=\{a,b,c,d\},\quad a=i,\ b=i+1,\ c=i+n,\ d=i+n+1
\]
(indices modulo \(2n\)). Indeed, choosing two incident edges at a cubic vertex yields a rim path or a spoke-rim path. The distinct four-cycles are precisely the \(n\) squares \(Q_i\): a four-cycle containing spokes uses two consecutive spokes and their joining rim edges; a four-cycle with no spoke would lie in the \(2n\)-rim. Every four-vertex face of \(L\) is the vertex set of such a square. To see this, each of its four induced triples has two edges, so the induced four-vertex graph has four edges and, being triangle-free, is a four-cycle. No five-vertex face exists: if all ten triples on five vertices were connected, counting at least two edges per triple gives \(3e\ge20\), whereas a triangle-free graph on five vertices has at most six edges, giving \(3e\le18\), a contradiction. Thus \(L\) has exactly the described \(n\) tetrahedra, \(6n\) triangles, all \(\binom{2n}{2}\) edges, and no larger faces.

**2. A uniform elementary collapse to a graph.** For each \(i=0,\ldots,n-1\), perform the following elementary simplicial collapses on \(L\), respecting the indicated order across stages.

First remove \((Q_i,\{a,b,c\})\) for every \(i\). The triangle \(abc\) belongs to exactly one tetrahedron, namely \(Q_i\). Next, for every \(j\in\mathbb Z/(2n)\mathbb Z\), remove \((R_j,\{j,j+2\})\). The chord \(\{j,j+2\}\) occurs in no other connected triple and no square; in particular its cyclic distance two differs from the square-diagonal distances \(n-1\) and \(n+1\).

Finally, for each \(i\), perform in order
\[
(\{b,c,d\},\{b,c\}),\quad
(\{a,b,d\},\{a,b\}),\quad
(\{a,c,d\},\{a,d\}).
\]
For the first pair, the diagonal \(bc\) previously occurred only in \(abc\) and \(bcd\), and \(abc\) is gone. For the second, the rim edge \(ab\) previously occurred only in \(abc\), \(abd\), and the two neighboring rim triples; all but \(abd\) have been removed. For the third, the other square diagonal \(ad\) previously occurred only in \(abd\) and \(acd\), and \(abd\) is gone. Different squares have distinct pairs of opposite diagonals and distinct selected rim edges, so no subsequent pair interferes. Each listed lower-dimensional face is therefore free when used.

There are exactly \(6n\) elementary collapse pairs: \(n\) tetrahedron–triangle pairs and \(5n\) triangle–edge pairs. All triangles and tetrahedra disappear, leaving a graph \(H_n\) with \(2n\) vertices and \(\binom{2n}{2}-5n\) edges. It is connected: all the antipodal spokes \(\{i,i+n\}\) remain, as do the rim edges \(\{j,j+1\}\) for \(n\le j<2n\), which form a path from \(n\) through \(2n-1\) to \(0\). Every other vertex attaches via a spoke. Thus
\[
L\searrow H_n\simeq\bigvee^{\beta_n}S^1,
\qquad
\beta_n=\binom{2n}{2}-5n-2n+1=2n^2-8n+1.
\]
The collapses are integral homotopy equivalences, so \(L\) has free first integral homology of rank \(\beta_n\) and no other nonzero reduced integral homology.

**3. From dual homology to homotopy.** Combinatorial Alexander duality over \(\mathbb Z\) gives
\[
\widetilde H_k(\Delta_3(M_{2n});\mathbb Z)
\cong \widetilde H^{2n-k-3}(L;\mathbb Z).
\]
By the previous step and the universal coefficient theorem, only \(k=2n-4\) survives, with rank \(\beta_n\). Because \(L\) contains no five-vertex face, every five-element subset of \(V\) contains a disconnected triple; hence \(\Delta_3(M_{2n})\) contains the full \((2n-6)\)-skeleton of the simplex on \(V\). In particular, for \(n\ge4\) the complex contains the full two-skeleton and is simply connected. The complex has dimension at most \(2n-4\), since every facet is a complement of a triple. Successive Hurewicz arguments upgrade its vanishing lower integral homology to \((2n-5)\)-connectivity. A map from a wedge of \(\beta_n\) spheres in degree \(2n-4\) representing a basis of the sole homology group is then a homology equivalence between simply connected CW complexes, hence a homotopy equivalence by Whitehead's theorem. This establishes the displayed integral homotopy type for every \(n\ge4\).

## Verification
Run `python3 VERIFY.py` with Python 3 standard library. It constructs the two relevant complexes independently from the graph adjacency relation, checks **every** specified free-face collapse for all \(4\le n\le40\), and checks the remaining graph's connectivity and exact cycle rank. It also independently enumerates **all faces** of the ordinary three-cut complex and calculates exact mod-two boundary ranks at \(n=4,5,6\). All 37 collapse checks and three full-cut calculations pass and agree with the theorem. These finite computations corroborate—but do not replace—the uniform proofs of freeness, face classification and homotopy conversion.

## Relationship to prior work
Agarwal and Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs* (arXiv:2608.30601; first posted 2026-08-31, updated 2026-09-14), classify different complexes. Their Section 6, Problem 26, specifically proposes determining cut and total-cut topology of these ladders; their paper does not assert the ordinary three-cut result above. Bayer et al., *Topology of Cut Complexes of Graphs* (arXiv:2304.13675), and *Topology of Cut Complexes II* (arXiv:2407.08158) treat other graph families and some general skeleton and homology statements. The published calculation *Sphere-wedge topology of three-cut complexes of circular ladders* (2026) obtains the same formula for the **nonisomorphic** prism graphs \(C_n\square K_2\), not the Möbius ladders. The published result *Three-cut complexes of triangle-free graphs with edge-disjoint squares* (2026) does not apply here: consecutive squares \(Q_i,Q_{i+1}\) share an antipodal spoke. Likewise the high-girth theorem for cut complexes does not apply, since \(M_{2n}\) has four-cycles. The present proof uses a separately verified collapse on the twisted cyclic family.

## Limitations
The claim is confined to the **ordinary** parameter-three cut complex of the named Möbius ladder family for \(n\ge4\). It does not settle all cut parameters, total cut complexes, shellability, automorphism representations, or graphs obtained by other twists. It uses established Alexander duality, Hurewicz and Whitehead theorems and makes no claim of inventing them. A search of published records cannot exclude every unindexed equivalent theorem; in particular, publication priority must not be inferred solely from nonmatching search results. Independent scientific confirmation has not been performed.

## References
- A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, 2026-08-31 (v1); v2 posted 2026-09-14; Section 6, Problem 26. https://arxiv.org/abs/2608.30601
- M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675. https://arxiv.org/abs/2304.13675
- M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158. https://arxiv.org/abs/2407.08158
- *Sphere-wedge topology of three-cut complexes of circular ladders*, published mathematical result, 2026-10-11.
- *Three-cut complexes of triangle-free graphs with edge-disjoint squares*, published mathematical result, 2026-10-11.
- *High-girth cut complexes are wedges of top-dimensional spheres*, published mathematical result, 2026-10-11.
- A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002 (Alexander duality, Hurewicz, Whitehead).
