# A mixed-dimensional integral sphere wedge for the Nauru two-independence complex

## Finding
Let \(G=\operatorname{GP}(12,5)\) be the 24-vertex Nauru graph, and let \(X=\operatorname{Ind}_2(G)\) be the simplicial complex of subsets inducing connected components of order at most two. Then the complete integral homotopy type is
\[
X\simeq\bigvee^{9}S^{7}\ \vee\ \bigvee^{3}S^{8}.
\]
Consequently, the only nonzero reduced integral homology groups are \(\widetilde H_7(X;\mathbb Z)\cong\mathbb Z^9\) and \(\widetilde H_8(X;\mathbb Z)\cong\mathbb Z^3\). The complex is 6-connected and has ordinary Euler characteristic \(-5\). The statement is about ordinary (nonequivariant) homotopy, not just ranks over a field.

## Assumptions and scope
The graph is finite, simple, undirected, and has vertices \(u_i,v_i\) indexed by \(i\in\mathbb Z/12\mathbb Z\). Its 36 edges are \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+5}\}\), with each edge understood as unordered and counted once. We use the labels \(u_i=i\) and \(v_i=12+i\), for \(0\le i<12\). A subset \(F\) is a face of \(X\) if and only if every vertex of the induced graph \(G[F]\) has degree at most one. Equivalently, \(G[F]\) has no not-necessarily-induced three-vertex path. The empty subset is included as a combinatorial face but is excluded from the ordinary discrete-Morse matching poset. All simplices are oriented using increasing vertex labels.

The earlier literature calls the same complex a \(P_3\)-devoid complex or a dissociation complex. This is not the graph-theoretic distance-two independence complex, and it is not the ordinary independence complex \(\operatorname{Ind}_1(G)\).

## Proof
**Complete face enumeration.** Represent a subset by its 24-bit mask. Starting with the empty mask, visit the vertices in increasing order. For each existing face \(F\) and current vertex \(v\), add \(F\cup\{v\}\) exactly when the number of selected neighbors of \(v\) is at most one and any such selected neighbor has no neighbor already selected in \(F\). This condition is necessary and sufficient to preserve induced degree at most one, and induction on the processed vertices proves that every face is generated exactly once. The standalone verifier reconstructs the adjacency masks and checks the face condition independently on every generated mask. The resulting 561,397 nonempty faces have counts by dimension \(0,1,\ldots,12\):
\[
(24,276,1952,9306,31080,73648,123192,142521,109856,53160,14568,1790,24).
\]
The alternating face sum is \(\chi(X)=-5\), which agrees with the final homotopy calculation.

**An explicit matching.** On the set of all nonempty faces, use the following vertex-pivot order, in the prescribed 0-based labels:
\[
(20,4,19,10,22,14,5,18,12,15,16,7,21,2,0,23,17,11,1,3,9,13,6,8).
\]
At pivot \(v\), pair each still-unmatched face \(F\) not containing \(v\) with \(F\cup\{v\}\) whenever that coface is also still unmatched, and remove both faces from future pivots. This constructs 280,690 disjoint pairs of incident simplices. Exactly 17 simplices remain unmatched: one vertex, eleven 7-simplices, and five 8-simplices. The eleven critical 7-face masks, in increasing integer order, are
\[
(2396745,4317346,4485672,4487208,4551200,4552736,6342753,6389955,8571172,8590092,12779910),
\]
and the five critical 8-face masks are
\[
(4225322,4417674,4547233,4679816,12644960).
\]
The critical zero-dimensional face is also recomputed rather than assumed.

**Acyclicity, without relying on an untested pivot heuristic.** Construct the full directed Hasse diagram on all 561,397 nonempty faces. For each codimension-one incidence \(F\subset E\), direct \(E\to F\), except that matched incidences are reversed. The verifier evaluates all 4,345,776 such incidences and then applies Kahn's topological-sort algorithm. All 561,397 vertices are removed, with none remaining. Thus the displayed matching is acyclic. Finite discrete Morse theory provides a CW complex with precisely one 0-cell, eleven 7-cells, and five 8-cells, homotopy equivalent to \(X\).

**Integral attaching-degree calculation.** Let \(c_1,\dots,c_{11}\) be the critical 7-simplices in the stated order and \(d_1,\dots,d_5\) the critical 8-simplices. Using the orientations by vertex label, recursively eliminate each matched 7/8 pair via its incidence coefficient \(\pm1\) in the ordinary simplicial boundary. Each matched upper 7-face (paired with a 6-face) projects to zero; each critical 7-face projects to its corresponding basis vector. For a matched lower 7-face \(F\) with matched 8-coface \(E\), solve the signed boundary relation \(\partial E=0\) for the coefficient of \(F\), expressing its projection through the projections of the remaining facets of \(E\). The acyclic orientation makes this a terminating exact integer recurrence. Applying it to all five critical 8-faces produces the following full signed Morse boundary matrix, whose rows correspond to \(c_1,\dots,c_{11}\) and columns to \(d_1,\dots,d_5\):
\[
\partial^{\mathrm M}_8=
\begin{pmatrix}
0&0&0&0&0\\
0&0&0&0&0\\
0&0&0&0&0\\
1&0&0&-1&0\\
0&-1&-1&0&1\\
1&0&0&-1&0\\
0&0&0&0&0\\
0&0&0&0&0\\
0&0&0&0&0\\
0&0&0&0&0\\
0&0&0&0&0
\end{pmatrix}.
\]
Its third column equals its second, its fourth is the negative of its first, and its fifth is the negative of its second. The minor using rows four and five and columns one and two has determinant \(-1\). Therefore the matrix has rank two, its image is primitive, and its only nonzero Smith invariant factors are \(1,1\). This is an **integral** assertion: no torsion is hidden by finite-field calculations.

**Homotopy deduction.** Before attaching the 8-cells, the Morse CW complex is the wedge of eleven 7-spheres. Its seventh homotopy group is \(\mathbb Z^{11}\), so all five attaching maps \(S^7\to\bigvee^{11}S^7\) are classified by their integral degree vectors. The unimodular Smith reductions are realized by homotopy self-equivalences of the wedge and elementary changes of attaching-cell bases. The two unit maps cancel two 7/8-cell pairs; the other three 8-cells attach trivially. The resulting homotopy type is exactly nine 7-spheres wedged with three 8-spheres. No assertion about equivariant homotopy is required for this conclusion.

## Verification
The accompanying `verify.py` requires standard Python 3 only. Running `python3 verify.py` enumerates all faces from the explicit graph, separately checks every face's induced degrees, constructs all 280,690 matching pairs, verifies the 17 critical cells, topologically sorts all 4,345,776 Hasse incidences, reconstructs the exact signed integer Morse boundary matrix, and checks a unit determinant and all column relations. Its terminal marker is `ALL_CHECKS_PASS`; the checked stdout is embedded as `verification_output.txt`. The program uses no internet access, external dataset, or package dependency.

## Relationship to prior work
Taylan's January 27, 2015 archive-era preprint defines devoid complexes and establishes results for paths, cycles, and forests. Its general matching machinery is a source of method, but its displayed homotopy classifications do not compute the 24-vertex Nauru case. Deshpande and Singh study higher independence complexes of complete multipartite, fully whiskered, path, cycle, and perfect rooted tree graph families; none of their listed family classifications contains this graph.

An accessible earlier computation for this **same graph** establishes the **ordinary** independence-complex type \(\operatorname{Ind}_1(G)\simeq\bigvee^4S^5\vee S^6\). That result is a distinct simplex condition and does not determine the two-independence complex. A previously computed two-independence type for the dodecahedral graph \(\operatorname{GP}(10,2)\), a different generalized Petersen graph, likewise does not imply the Nauru calculation. Results on metric Vietoris–Rips complexes of the Nauru graph use different simplices. These distinctions are comparisons of claims, not deductions of novelty from similar or dissimilar titles. Searches under the Nauru, generalized Petersen, dissociation and \(P_3\)-devoid aliases identified no covering classification in the inspected sources; such a search cannot exclude equivalent unindexed work.

## Limitations
This is a finite graph-specific calculation with an exhaustive reproducible certificate, not a classification of all generalized Petersen graphs or all higher-independence parameters. The homotopy equivalence is not claimed to be equivariant under the automorphism group. The complete finite incidence computation is verified by the supplied program; isolated finite experiments without exhaustive incidence checks would not establish the statement. Independent mathematical review and definitive publication-priority verification have not been performed.

## References
1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first publicly posted 2015-01-27, https://arxiv.org/abs/1501.06754. Its title page lists MSC 55U10 among its classifications.
2. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, https://arxiv.org/abs/2001.05448.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
4. A published ordinary-independence computation for the Nauru graph, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-nauru-independence-complex-is-bigvee-4-s-5-vee-s-6--7c319734d8d8.
5. D. Eppstein, *The Many Faces of the Nauru Graph*, 2007-12-12, https://11011110.github.io/blog/2007/12/12/many-faces-of.html.
