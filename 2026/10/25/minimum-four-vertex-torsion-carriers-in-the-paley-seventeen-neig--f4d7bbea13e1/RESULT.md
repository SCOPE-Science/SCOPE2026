# Minimum four-vertex torsion carriers in the Paley-seventeen neighborhood complex

## Finding
Let \(P_{17}\) be the Paley graph on \(\mathbb F_{17}\), and let \(K=\mathcal N(P_{17})\) be its **open** Lovász neighborhood complex. Exactly **476 four-vertex subsets** \(W\) support a nonzero class in the image of
\[
\widetilde H_2(K[W];\mathbb F_3)\longrightarrow\widetilde H_2(K;\mathbb F_3)\cong\mathbb F_3.
\]
Four vertices are the smallest possible support. Every such \(K[W]\) is the boundary of a tetrahedron. Among all **510** induced tetrahedral boundaries, **34** are null-homologous in \(K\) over \(\mathbb F_3\); the other **476** represent its unique nonzero homology direction, up to scalar.

Under the order-136 quadratic-residue affine group, the 476 essential boundaries form five orbits. Their lexicographically least vertex representatives and sizes are
\[
\begin{array}{c|ccccc}
W& (0,1,3,13)&(0,1,4,7)&(0,1,4,14)&(0,1,6,7)&(0,1,6,12)\\
\hline
|G\cdot W|&136&136&68&68&68.
\end{array}
\]
The 34 null-homologous induced tetrahedral boundaries form a single orbit with representative \((0,1,4,5)\). These assertions concern ambient homology, not merely homology of the induced subcomplex.

## Assumptions and scope
Identify vertices with \(\{0,1,\ldots,16\}\) and put
\[
Q=\{1,2,4,8,9,13,15,16\}\subset\mathbb F_{17}.
\]
The Paley graph has edge \(\{u,v\}\) precisely when \(v-u\in Q\). The open neighborhood of \(a\) is \(a+Q\). Thus a subset is a face of \(K\) if and only if it lies inside at least one \(a+Q\). The simplicial orientations are induced by increasing vertex order. All homology in the new classification uses \(\mathbb F_3\) coefficients; no statement about homotopy classes of these embedded spheres is made.

The acting subgroup is \(G=\{x\mapsto ax+b:a\in Q,\ b\in\mathbb F_{17}\}\). Each element preserves graph adjacency and hence simplices of \(K\). The theorem needs only this explicitly specified subgroup, without relying on a classification of all automorphisms.

## Proof
**Chain dimensions and the ambient homology.** Enumerating nonempty subsets of the 17 eight-element neighborhoods produces the face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)=(17,136,612,1122,952,476,136,17).
\]
The exact simplicial boundary columns with increasing orientations give the following ranks, computed by deterministic sparse finite-field elimination:
\[
\begin{array}{c|cc}
&\operatorname{rank}(\partial_2)&\operatorname{rank}(\partial_3)\\
\hline
\mathbb F_3&120&491\\
\mathbb F_{101}&120&492.
\end{array}
\]
Every two vertices of \(K\) span an edge, hence \(\operatorname{rank}(\partial_1)=16\). Therefore \(\operatorname{rank}(\partial_2)\le136-16=120\) over every field, and the lower bound from \(\mathbb F_{101}\) forces rational rank 120. The chain identity \(\partial_2\partial_3=0\) bounds rational \(\operatorname{rank}(\partial_3)\le612-120=492\), attained by the \(\mathbb F_{101}\) computation. Accordingly,
\[
\dim_{\mathbb F_3}\widetilde H_2(K;\mathbb F_3)=612-120-491=1,
\qquad \widetilde H_2(K;\mathbb Q)=0.
\]
Moreover \(H_1(K;\mathbb F_3)=0\), so the nonzero degree-two mod-three class is the reduction of an integral three-primary torsion class by the universal coefficient theorem. The previously established integral order-three homology is not reproved here.

**Sharp support bound.** A nonzero 2-cycle in a simplicial complex supported on at most four vertices requires all four oriented triangles of a tetrahedron boundary: each edge in the support must have canceling incidences. No three-vertex complex has nonzero second homology. On four vertices a nonzero cycle exists exactly when all four triangles belong to the complex, while their tetrahedron is absent. Such a subcomplex is \(S^2\), and its potential generator is
\[
z_W=\sum_{i=0}^{3}(-1)^i[W\setminus\{w_i\}],
\quad W=\{w_0<w_1<w_2<w_3\}.
\]

**Exhaustive classification and direct certificates.** The standalone verifier enumerates all \(\binom{17}{4}=2380\) four-sets. It identifies exactly 510 satisfying the missing-tetrahedron criterion. For each, it reduces the four-term vector \(z_W\) in the complete \(\mathbb F_3\)-column span of \(\partial_3\). Its remainder is zero exactly when the ambient homology class vanishes. All 510 candidates form six affine orbits, with canonical representatives and sizes as in the statement. Direct reductions are repeated for every member of every orbit: the five essential orbits account for \(136+136+68+68+68=476\) spheres, and the null orbit accounts for 34. This completes the support minimum and the orbit census.

## Verification
Run `python3 verify.py` with Python 3.9 or newer; no third-party modules or external files are needed. The program reconstructs every face from the graph formula, checks \(\partial_2\partial_3=0\) integrally, computes both prime-field rank pairs, enumerates the affine action and every four-set, constructs signed tetrahedral boundary cycles, and checks their ambient \(\mathbb F_3\) membership by exact column elimination. Its final line is `VERIFY_OK_PALEY17_NEIGHBORHOOD_TORSION_CARRIERS`.

## Relationship to prior work
Kahle's 2005 neighborhood-complex paper introduces the applicable graph-topological framework and proves results about random graphs; its theorems do not give this Paley-seventeen carrier classification. A previously published direct computation for \(\mathcal N(P_{17})\), *Three-torsion in the neighborhood complex of the Paley graph of order seventeen*, establishes the stronger nonequivariant homotopy type \(M(\mathbb Z/3,2)\vee\bigvee^{35} S^3\). Its complete publicly available `RESULT.md` was examined: its face enumeration and homotopy calculation do **not** classify four-vertex supports, distinguish the 34 null boundaries, or give the five essential affine orbits. Another prior calculation determines the affine representation on homology, without classifying these local carriers. Such ambient computations alone do not imply the images of the 510 individual sphere cycles.

## Limitations
The classification is finite and applies only to the specified open neighborhood complex and \(\mathbb F_3\)-homology. It does not establish exact integer orders independently of the cited homotopy result, solve higher support thresholds, or classify representatives in other complexes. Exhaustive finite-field computation is used for the complete 510-sphere ambient-image test. Bibliographic uniqueness is not asserted; unindexed or otherwise inaccessible work remains possible.

## References
1. M. Kahle, *The Neighborhood Complex of a Random Graph*, arXiv:math/0512077, initial public version December 4, 2005. https://arxiv.org/abs/math/0512077 .
2. *Three-torsion in the neighborhood complex of the Paley graph of order seventeen*, published scientific result and full proof: https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-three-torsion-in-the-neighborhood-complex-of-the-paley-graph-of--3bbd3a54ace8/RESULT.md .
3. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803 (2012). https://arxiv.org/abs/1210.2803 .
