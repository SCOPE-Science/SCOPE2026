# Full octahedral homology representations of two unordered graph particles

## Finding
Let \(O=K_{2,2,2}\) be the 1-skeleton of the octahedron, and let \(X=\operatorname{UConf}_2(|O|)\) be the space of unordered, distinct pairs of points on this graph. The graph automorphism group \(G\cong S_4\times C_2\) acts naturally on \(X\). Write \(\varepsilon\) for the nontrivial rational character of the central inversion \(C_2\), and \(S^\lambda\) for the rational Specht module for the proper-rotation subgroup \(S_4\).

The integral homology, including all degrees, is
\[
H_j(X;\mathbb Z)\cong\begin{cases}\mathbb Z&j=0,\\\mathbb Z^8&j=1,\\\mathbb Z^4&j=2,\\0&j>2.\end{cases}
\]
The full natural rational representations are
\[
H_1(X;\mathbb Q)\cong(S^{(4)}\oplus S^{(3,1)})\boxtimes\varepsilon\;\oplus\;(S^{(1,1,1,1)}\oplus S^{(2,1,1)})\boxtimes\mathbf1,
\]
\[
H_2(X;\mathbb Q)\cong(S^{(1,1,1,1)}\oplus S^{(2,1,1)})\boxtimes\varepsilon.
\]
The second formula has the following **integral** strengthening. There are four explicit integral product-torus classes \(w_1,\ldots,w_4\) forming a basis of \(H_2(X;\mathbb Z)\). If \(\pi_g\in S_4\) permutes the four opposite-face pairs, and \(\delta(g)\in\{+1,-1\}\) is the determinant of the geometric octahedral isometry, then
\[
g_*(w_i)=\delta(g)\operatorname{sgn}(\pi_g)w_{\pi_g(i)}.
\]
Hence the integral second-homology module is a sign-and-determinant twist of the four-point permutation lattice. The proper-rotation subgroup fixes a one-dimensional subspace of first rational homology but no nonzero second-homology class; the full group fixes no nonzero positive-degree rational homology class.

## Assumptions and scope
Use opposite vertex pairs \(\{0,1\},\{2,3\},\{4,5\}\). An edge joins two vertices exactly when they belong to distinct pairs. Vertices, edges and squares of the unordered discretized two-particle complex are, respectively, unordered pairs of distinct original vertices; a vertex and a disjoint closed edge; and two disjoint closed edges. Cells inherit the orientations from increasing vertex labels, ordered edge factors, and their cubical products. The conclusion concerns the ordinary collision-free configuration space of **unlabeled** points, not the ordered space, a matching complex, or a sink configuration space.

The central \(C_2\) is geometric antipodal inversion, and the complementary \(S_4\) is the **orientation-preserving** subgroup of the full 48-element octahedral symmetry group. This choice is essential for interpreting the displayed tensor factors. Every graph automorphism is realized by a signed permutation of the three pairs of opposite vertices.

## Proof
**The cubical model.** The edge-disjoint closed-cell model has \(15\) zero-cells, \(48\) one-cells and \(30\) two-cells. For two particles, the original octahedral graph satisfies the Prue–Scrimshaw subdivision conditions: distinct essential vertices are separated by at least one edge, and every nontrivial circuit has at least three edges. Thus inclusion of the discretized complex induces an integral homology isomorphism with \(X\); because inclusion commutes with graph automorphisms, this is also an isomorphism of their homology representations.

**Exact integral homology.** Let \(d_1\) and \(d_2\) be the incidence matrices with signed cubical orientations. The attached executable certificate constructs these matrices and verifies \(d_1d_2=0\), \(\operatorname{rank}d_1=14\), and \(\operatorname{rank}d_2=26\) over the rationals. It computes the *integral Smith normal form* of \(d_2\), whose 26 nonzero invariant factors all equal \(1\). Connectivity and the rank data establish the displayed integral homology groups, including absence of torsion in first homology. No chains exist in dimensions above two.

**The integral torus basis.** Four representative faces are
\[
(0,2,4),\quad(0,2,5),\quad(0,3,4),\quad(0,3,5).
\]
Each chosen face and its antipodal face support disjoint oriented triangle loops; their product is an embedded torus in the unordered configuration space. Writing their four signed square-cycles as columns \(z_i\), the certificate checks \(d_2z_i=0\). The \(4\times4\) matrix of their coefficients on the square cells with canonical indices \(0,1,5,6\) has determinant \(+1\). Because the integral cycle kernel has rank four and is saturated, this proves that the four tori form an **integral**, not just rational, basis.

For the face order above set \((w_1,w_2,w_3,w_4)=(-z_1,z_2,z_3,-z_4)\). Direct signed cellular action for all 48 graph automorphisms verifies the exact integral formula \(g_*w_i=\delta(g)\operatorname{sgn}(\pi_g)w_{\pi_g(i)}\), giving the second-homology module and its rational decomposition.

**The first-homology character.** Every automorphism is tested against both boundary operators by exact signed matrices. Trace of the action on the cubical cellular chain groups and on the explicit torus basis gives \(\chi_{H_1}(g)=1+\chi_{H_2}(g)-(\operatorname{tr}_{C_0}(g)-\operatorname{tr}_{C_1}(g)+\operatorname{tr}_{C_2}(g))\) by the equivariant Euler–Poincaré identity. On each of the five \(S_4\)-cycle types, the two characters for determinant \(+1\) and determinant \(-1\) are:

| Proper-rotation cycle type | \(\chi_{H_1},\chi_{H_2}\) for \(\delta=+1\) | \(\chi_{H_1},\chi_{H_2}\) for \(\delta=-1\) |
|---|---|---|
| \((1,1,1,1)\) | \((8,4)\) | \((0,-4)\) |
| \((2,1,1)\) | \((0,-2)\) | \((-4,2)\) |
| \((2,2)\) | \((0,0)\) | \((0,0)\) |
| \((3,1)\) | \((2,1)\) | \((0,-1)\) |
| \((4)\) | \((0,0)\) | \((0,0)\) |

The exact inner product of these ten class values with the five irreducible \(S_4\)-characters and each \(C_2\)-character gives multiplicity one exactly for the four summands stated in degree one, and for the two summands stated in degree two. The dimensions check as \(1+3+1+3=8\) and \(1+3=4\).

## Verification
Run `python octahedral_two_point_verify.py` with Python 3.10 or later and SymPy installed. The verifier constructs its own graph, cells, signed differentials, integral Smith normal form, four torus cycles, all 48 automorphism actions, ten character-class values, and rational character inner products. It explicitly checks chain-equivariance and the unimodular torus minor. An executed run prints five PASS summaries and the complete ten-class character table. The exact finite calculation is exhaustive because all six vertices, twelve edges, thirty square cells, and 48 graph automorphisms are enumerated.

## Relationship to prior work
Farley–Sabalka developed discrete Morse methods for graph braid groups; Prue–Scrimshaw established the improved subdivision criterion used to identify the discrete model. Barnett–Farber's planar two-particle results already explain the existence of product torus classes and compute homological invariants for the **ordered** configuration space. General graph-braid and particle-statistics literature also provides nonequivariant first-homology structure. These broader methods and known facts are credited; the claim here is **the explicit full 48-element action on the unordered homology together with the signed integral torus-permutation lattice**, not the invention of product tori, the finite cubical model, or ordinary graph-braid homology.

Published computations for the cuboctahedral two-particle configuration space concern a different graph with a different homology rank. Published octahedral **matching-complex** representations concern another simplicial construction and do not imply the result here. No directly equivalent octahedral unordered full-character computation was identified in targeted searches; this does not establish bibliographic uniqueness.

## Limitations
The representation of first homology is classified **over \(\mathbb Q\)**, not as an integral \(\mathbb Z[G]\)-lattice. The explicit integral representation statement is restricted to **second** homology. No claim is made about cup products, the graph braid group's presentation, collision-allowing variants, three or more particles, or a uniform result for other Platonic graphs. Exact computer calculations supply finite combinatorial certificates, while the equivalence to the continuous configuration space uses the cited topological theorem. A full independent audit has not been performed.

## References
- D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539 (first submitted 2004-10-25).
- K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180 (2009); see planar-graph torus results.
- P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511 (2009); subdivision theorem.
- A. Sawicki, *Topology of graph configuration spaces and quantum statistics*, arXiv:1408.7002 (2014); background on first homology.
- J. M. Harrison, J. P. Keating, J. M. Robbins and A. Sawicki, *n-Particle Quantum Statistics on Graphs*, Communications in Mathematical Physics 330 (2014), 1293–1326, DOI 10.1007/s00220-014-2091-0.
- *Non-abelian Quantum Statistics on Graphs*, Communications in Mathematical Physics (2019), DOI 10.1007/s00220-019-03583-5; product-cycle context.
