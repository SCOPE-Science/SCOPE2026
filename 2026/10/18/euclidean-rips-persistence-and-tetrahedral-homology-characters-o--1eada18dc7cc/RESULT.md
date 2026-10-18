# Euclidean Rips persistence and tetrahedral homology characters of the truncated tetrahedron

## Finding
Let \(P\subset\mathbb R^3\) be the twelve signed coordinate permutations of \((3,1,1)\) having positive sign product. Give \(P\) its unrescaled Euclidean distance and put \(K_r=\operatorname{VR}_{\le r}(P)\), with a simplex for every nonempty subset of diameter at most \(r\). Then for every real \(r\ge0\),
\[
K_r\simeq
\begin{cases}
\bigsqcup^{12}\mathrm{pt},&0\le r<\sqrt8,\\
\bigvee^3 S^1,&\sqrt8\le r<\sqrt{24},\\
\bigvee^5 S^2,&\sqrt{24}\le r<\sqrt{32},\\
S^2,&\sqrt{32}\le r<\sqrt{40},\\
\mathrm{pt},&r\ge\sqrt{40}.
\end{cases}
\]
The included triangulation \(B\) of the convex truncated-tetrahedron boundary lies in \(K_{\sqrt{24}}\), and \(K_{\sqrt{32}}\) simplicially collapses **onto that same included** \(B\) by 140 elementary pairs. Consequently, the inclusion in degree two
\[
H_2(K_{\sqrt{24}};\mathbb Z)\cong\mathbb Z^5
\longrightarrow H_2(K_{\sqrt{32}};\mathbb Z)\cong\mathbb Z
\]
is surjective with kernel \(\mathbb Z^4\). The nontrivial two-dimensional integral persistent barcode thus consists of four intervals \([\sqrt{24},\sqrt{32})\) and one interval \([\sqrt{24},\sqrt{40})\).

Let \(G\) be the 24-element group of coordinate permutations and even coordinate sign changes, naturally isomorphic to \(S_4\). The full rational degree-two homology representations at the two intermediate thresholds satisfy
\[
\begin{aligned}
H_2(K_{\sqrt{24}};\mathbb Q)&\cong
S^{(4)}\oplus S^{(3,1)}\oplus S^{(1,1,1,1)},\\
H_2(K_{\sqrt{32}};\mathbb Q)&\cong S^{(1,1,1,1)},\\
\ker\bigl(H_2(K_{\sqrt{24}};\mathbb Q)\to
H_2(K_{\sqrt{32}};\mathbb Q)\bigr)&\cong
S^{(4)}\oplus S^{(3,1)}.
\end{aligned}
\]
Here \(S^\lambda\) is the rational Specht representation of the indicated partition of four. Equivalently, the four homology classes killed at \(\sqrt{32}\) form, over \(\mathbb Q\), the natural four-point permutation representation. The surviving integral class transforms by the orientation character \(g\mapsto\det(g)\).

## Assumptions and scope
The sign product condition means an even number of negative coordinates, including the sign attached to the coordinate of magnitude three. The twelve distinct vertices, in lexicographic order, are recorded in `CERTIFICATES.json`. The four nonzero squared distances between distinct vertices are exactly \(8,24,32,40\), occurring for \(18,24,12,12\) unordered pairs respectively. Thus the displayed intervals include their left endpoint and exhaust the filtration. The object is the ordinary Euclidean chordal metric on a specific congruent realization of the Archimedean truncated tetrahedron, **not** its graph shortest-path metric.

The same boundary complex \(B\) is constructed by taking the four triangular supporting faces and triangulating each of the four hexagonal supporting faces using its alternating central triangle and three corner triangles. It has face vector \((12,30,20)\). The vertex labels, polygonal cyclic orders and 20 triangles are supplied with the certificate. All its edges have squared length at most \(24\), so \(B\subseteq K_{\sqrt{24}}\subseteq K_{\sqrt{32}}\).

## Proof
**Distance levels and the first stage.** Direct integer subtraction of the twelve coordinate vectors gives the stated complete distance multiplicities. At squared radius \(8\) the flag complex has face vector \((12,18,4)\). Its four triangles are the four triangular faces of the truncated tetrahedron. Each has a free edge; four explicit free-face collapses leave a connected graph with twelve vertices and fourteen edges. It therefore has homotopy type \(\bigvee^3 S^1\).

**Five two-spheres at squared radius \(24\).** The flag complex has face vector \((12,42,48,12)\). Twelve certified elementary collapses remove its twelve tetrahedra and twelve distinct triangular facets, leaving a two-dimensional complex \(R\). Relative to \(B\), this complex contains exactly twelve additional edges and sixteen additional triangles. Omit temporarily the four triangles with vertex triples \((1,2,7)\), \((1,3,9)\), \((3,6,11)\), \((5,7,11)\). The resulting subcomplex \(R_0\) collapses onto \(B\) by twelve further certified free edge–triangle pairs. Attaching the four omitted triangles to \(R_0\) amounts to attaching four two-cells along loops. All these loops are nullhomotopic since \(R_0\simeq B\cong S^2\); hence \(R\simeq B\vee\bigvee^4 S^2\simeq\bigvee^5 S^2\). Each collapse is simplicial and all four remaining cell attachments are integral.

**The included sphere at squared radius \(32\).** The flag complex has face vector \((12,54,112,108,48,8)\). Its 140 listed elementary free-face pairs collapse it onto the **specified subcomplex** \(B\), giving an inclusion-preserving simple-homotopy equivalence. For an independent structural check, the complement of its one-skeleton is the disjoint union of three four-cycles. Accordingly the Rips complex is the join of three independence complexes of four-cycles; each such independence complex collapses to two points, and their join has homotopy type \(S^2\). Unlike this abstract homotopy identification, the 140-pair certificate retains the included geometric boundary and hence controls the persistence map.

**Persistence and symmetry.** Since \(B\hookrightarrow K_{\sqrt{32}}\) is a homotopy equivalence and factors through \(K_{\sqrt{24}}\), the map on integral second homology from squared radius \(24\) to squared radius \(32\) is surjective. Its kernel is free of rank four because its domain is \(\mathbb Z^5\) and codomain \(\mathbb Z\). At squared radius \(40\), all twelve vertices form a full simplex, so the surviving class dies there. This proves the two-dimensional barcode and rules out hidden integral torsion.

The coordinate permutation/even-sign group preserves the entire filtration and the boundary sphere. Its induced orientation action on \(H_2(B;\mathbb Z)\) is \(\det(g)\); the inclusion identifies this with \(H_2(K_{\sqrt{32}};\mathbb Z)\). To identify the earlier rational representation, compute the reduced Lefschetz trace of each of the 24 transformations on the 114 simplices of \(K_{\sqrt{24}}\). A fixed simplex contributes its orientation sign multiplied by \((-1)^{\dim}\), with \(-1\) for the reduced augmentation term. Because the complex is a wedge of two-spheres, this is exactly its degree-two homology trace. On the five \(S_4\) classes \((1^4),(2,1^2),(2^2),(3,1),(4)\), the traces are \((5,1,1,2,-1)\). The sphere action at squared radius \(32\) has traces \((1,-1,1,1,-1)\). Comparing with the standard rational \(S_4\) character table gives the displayed decompositions; surjectivity and semisimplicity identify the kernel representation. This completes all asserted classifications.

## Verification
`VERIFY.py` is a standalone Python standard-library checker. Run `python3 VERIFY.py` from the directory containing both that script and `CERTIFICATES.json`. It reconstructs all 4,095 possible nonempty subsets at the final threshold, checks exact squared distances and all four Rips stages, reconstructs the eight supporting facets using integer vector products, verifies the boundary is a connected triangulated closed surface with Euler characteristic two, and replays every elementary collapse against all currently present strict cofaces. It also enumerates the entire 24-element symmetry group, signs on fixed simplices and all five conjugacy classes. Expected terminal status includes `VERIFY_OK`, `COLLAPSES_OK`, `GEOMETRIC_SPHERE_OK`, `S4_CHARACTERS_OK`, and `INTEGRAL_PERSISTENCE_OK`. No floating-point computations are needed.

## Relationship to prior work
M. Adamaszek's *Clique complexes and graph powers* (first public 2011-04-03, arXiv:1104.0433) develops graph-power Vietoris–Rips methods and explicitly computes other graph families, but not this Euclidean truncated-tetrahedral filtration. Saleh, Titz Mite and Witzel's *Vietoris–Rips complexes of Platonic solids* (first public 2023-02-28, arXiv:2302.14388) classifies the five Platonic solids and identifies Archimedean solids as an extension, without proving the present result.

The published *Graph-metric Rips filtration of the truncated tetrahedron* (published-finding corpus, 2026-10-04) proves that the graph shortest-path filtration has types twelve points, three circles, five two-spheres and finally a point at graph-distance thresholds \(0,1,2,3\). The first two nontrivial graph stages agree with the Euclidean thresholds of squared length \(8\) and \(24\). But **graph distance three consists of two distinct Euclidean shells**, squared lengths \(32\) and \(40\), each containing twelve pairs. The graph-metric theorem combines both shells at once, so it neither implies the intervening Euclidean two-sphere, the 140-pair relative collapse, the integral persistence map, nor the tetrahedral symmetry representations. The matching-complex homology of the truncated-tetrahedral graph concerns a different topological functor. Searches found no previously established statement dominating this full metric-and-symmetry claim; literature indexing remains incomplete.

## Limitations
This is an exact theorem for a single 12-point Euclidean configuration. It does not classify other Archimedean solids, arbitrary truncation ratios, or an infinite polytope family. The equivariant decomposition of the kernel is over \(\mathbb Q\); no claim is made that the integral kernel is isomorphic, as an integral group lattice, to the four-point permutation module. The relative elementary-collapse sequence is not claimed to be equivariant. Scientific novelty is qualified by residual risk of unindexed equivalent calculations, particularly in older geometric-topology literature. No independent scientific audit is represented.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, submitted 2011-04-03; introduction and Sections 1–3.
2. N. Saleh, T. Titz Mite and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388, submitted 2023-02-28; especially the theorem and discussion of Archimedean extensions.
3. *The graph-metric Rips filtration of the truncated tetrahedron*, published-finding corpus published mathematical finding, 2026-10-04 (public result containing `RESULT.md`, primary statement and proof).
4. N. Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, doctoral thesis, 2023; publicly available abstract consulted; full dissertation not used to claim exhaustive noncoverage.
