# Constant face vectors with arbitrarily many section types in four-dimensional double bipyramids

## Finding
For every integer \(n\ge5\), every strictly convex \(n\)-gon \(P\subset\mathbb R^2\) with the origin in its interior, and its standard double bipyramid
\[
K=\operatorname{conv}\left(\{(v_i,0,0):0\le i<n\}\cup\{\pm e_3,\pm e_4\}\right)\subset\mathbb R^4,
\]
every vertex-avoiding central hyperplane section \(S=K\cap H\) has
\[
(f_0,f_1,f_2)(S)=(2n+4,5n+4,3n+2),
\]
and exactly \(2n\) triangular facets and \(n+2\) quadrilateral facets.

Let \(k\) be the number of base vertices in one open halfspace bounded by \(H\). The combinatorial type of \(S\) is determined precisely by the unordered pair \(\{k,n-k\}\). Consequently a fixed standard double bipyramid has at most \(\lfloor n/2\rfloor\) types of generic central sections; for each \(n\ge5\), a strictly convex origin-containing polygon can be chosen so all these types occur within that *single* double bipyramid. Despite this arbitrarily large type spectrum in fixed ambient dimension four, all section face vectors are identical.

## Assumptions and scope
The polygon \(P\) is strictly convex (all \(n\) vertices extreme), ordered counterclockwise \(v_0,\ldots,v_{n-1}\), with \(0\in\operatorname{int}P\). The ambient canonical basis vectors \(e_3,e_4\) lie in the two additional coordinate directions. A generic central hyperplane is any hyperplane \(H=u^\perp\) with \(u\cdot (v_i,0,0)\ne0\) for every \(i\), and \(u\cdot e_3\ne0\), \(u\cdot e_4\ne0\). No metric symmetry or regularity of the polygon is assumed. No assertion is made for vertex-containing central hyperplanes; their section face counts may be different.

## Proof
**1. The ambient face list.** The polytope \(K\) is the iterated standard bipyramid over \(P\). Its vertices are its \(n\) base vertices and the four additional apices \(a_+,a_-,b_+,b_-\). Its edges are the \(n\) cyclic base edges, the \(4n\) base-to-apex spokes, and the four edges \(a_\sigma b_\tau\) with \(\sigma,\tau\in\{+,-\}\). Its \(2\)-faces are the \(4n\) triangles \(v_iv_{i+1}a_\sigma\) or \(v_iv_{i+1}b_\tau\) and the \(4n\) triangles \(v_i a_\sigma b_\tau\). Its \(4n\) facets are tetrahedra \(v_iv_{i+1}a_\sigma b_\tau\).

**2. All crossed edges.** A central hyperplane puts the two apices within each opposite pair on opposite sides. Since the origin lies inside the polygon, the sign sequence on the base polygon has exactly two transitions around its boundary. Thus the section meets exactly two base edges, exactly two of the four apex-to-apex edges, and, for each base vertex, exactly one edge to each apex pair (so \(2n\) spokes). Every section vertex belongs to exactly one crossed edge. Hence \(f_0=2n+4\).

**3. Facet polygons and the full face vector.** Consider each original tetrahedral facet \(v_iv_{i+1}a_\sigma b_\tau\). If its base edge has equal vertex signs, exactly one of the four choices of apex signs has no intersection; two choices make a triangular section and one makes a quadrilateral section. If the two base signs are opposite, all four choices meet the hyperplane; two give triangles and two give quadrilaterals. Since precisely two cyclic base edges have opposite signs, the number of triangular section facets is \(2(n-2)+2(2)=2n\), and quadrilateral section facets is \((n-2)+2(2)=n+2\). Therefore \(f_2=3n+2\); Euler's formula for a three-polytope gives \(f_1=f_0+f_2-2=5n+4\).

**4. An isomorphism invariant identifying the split.** Intersecting an original crossed edge with \(H\) gives a section vertex whose degree equals the number of crossed triangular \(2\)-faces incident to that original edge. Every crossed base edge and every crossed spoke gives a degree-four vertex; the two crossed edges between opposite apex pairs each give a section vertex of degree \(n\). As \(n\ge5\), these two degree-\(n\) vertices (the **hubs**) are distinguished intrinsically in the section graph. Choose one hub, say the crossing of \(a_+b_-\) after relabeling the apices according to their signs. Its \(n\) neighbors correspond bijectively to the base vertices: for a positive base vertex, the neighbor is its crossing spoke to \(b_-\); for a negative vertex, it is the crossing spoke to \(a_+\). Two of these neighbors are adjacent precisely when their associated base vertices are cyclically consecutive and have the same sign. Their induced subgraph is therefore exactly the disjoint union of two paths, on \(k\) and \(n-k\) vertices. Both hubs yield this same unordered pair. Graph isomorphism must preserve it, proving necessity.

**5. Sufficiency.** For a fixed split size \(k\), the sign pattern of the polygon vertices consists of one consecutive positive arc of length \(k\), and its negative complement. Every such pattern is obtained from any other by a cyclic rotation of the abstract polygon. Simultaneously relabeling the apex signs identifies all crossed faces and their inclusion relations, hence all section face lattices. Interchanging the halfspace signs identifies split size \(k\) with \(n-k\). This proves sufficiency and the upper bound \(\lfloor n/2\rfloor\).

**6. Sharp realization within one polytope.** Fix a small \(\delta\in(0,\pi/6)\). Choose one polygon vertex at polar angle \(0\), another at \(\pi+\delta\), and the remaining \(n-2\) vertices at distinct increasing angles strictly between \(\pi-2\delta\) and \(\pi-\delta\), all on the Euclidean unit circle. Every angular gap between consecutive vertices is strictly less than \(\pi\), so their convex hull is strictly convex and contains the origin in its interior. Rotate the open semicircle \((\alpha,\alpha+\pi)\) as \(\alpha\) ranges from \(-2\delta\) to \(-\delta\): it always contains the vertex at angle \(0\), never the vertex at \(\pi+\delta\), and its moving endpoint sweeps the remaining \(n-2\) vertices individually. Consequently each split size \(k=1,2,\ldots,n-1\) occurs for some generic central hyperplane, realizing every unordered pair and hence exactly \(\lfloor n/2\rfloor\) distinct types. This completes the proof.

## Verification
The dependency-free program `verify.py` reconstructs crossed edges, the section graph through crossed ambient triangular faces, and triangular/quadrilateral section facets from all \(4n\) ambient tetrahedra. It checks all cyclic contiguous sign-run sizes \(1\le k<n\) for every integer \(5\le n\le100\), including the two hub degrees and connected-component sizes of their induced neighborhoods. These 4,944 finite cases verify the formulas but are not used to replace the proof for arbitrary \(n\).

Run: `python3 verify.py`.

## Relationship to prior work
Sanyal, Werner and Ziegler (2007; arXiv:0708.3661) study face numbers of centrally symmetric four-polytopes, not central-section type spectra of standard double bipyramids. Brandenburg, De Loera and Meroni (2023; arXiv:2304.14239) give general slicing-chamber decompositions and algorithms that could in principle enumerate the sections of a specified polytope, but do not give this closed classification. De Loera, Lopez-Campos and Torres (2024; arXiv:2412.12419) study the possible numbers of vertices of sections and cyclic polytopes/hypercubes rather than this equal-face-vector family. Birkemeyer, Brose, Brandenburg and Prün (2026; arXiv:2609.16195), Section 3, analyze standard bipyramids and explicitly provide general lower bounds for their central-section face counts rather than a complete standard-bipyramid classification. The face-intersection principle and slicing-chamber principle are prior mathematics; the contribution asserted here is the exact constant-face-vector family and sharp, unbounded type count within one four-polytope.

## Limitations
The theorem concerns the canonical **standard** double bipyramid, not arbitrary combinatorial realizations. The maximum count \(\lfloor n/2\rfloor\) is over the generic sections of a suitable one-polytope realization for each \(n\), not every polygon. Non-generic vertex-containing hyperplanes are excluded. Since the underlying graph of a three-polytope determines its face lattice, the degree-and-neighborhood invariant suffices. The originality assessment remains subject to independent historical priority checking, notably of older combinatorial-section literature not exhaustively indexed.

## References
1. R. Sanyal, A. Werner and G. M. Ziegler, *On Kalai's conjectures concerning centrally symmetric polytopes*, arXiv:0708.3661v1 (2007-08-27), https://arxiv.org/abs/0708.3661.
2. M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1 (2023-04-27), https://arxiv.org/abs/2304.14239.
3. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419v1 (2024-12-17), https://arxiv.org/abs/2412.12419.
4. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg and N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195v1 (2026-09-14), https://arxiv.org/abs/2609.16195.
