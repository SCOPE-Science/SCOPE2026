# Ten paired-triangle tori give the integral \(S_6\)-module of two-point \(K_6\) configurations

## Finding
Let \(G=K_6\) have vertices \(V=\{0,1,2,3,4,5\}\), and let \(X=\operatorname{UConf}_2(|G|)\) denote configurations of two *unordered, distinct* points on its geometric realization. Write \(\mathcal P\) for the ten unordered partitions \(P=\{A,B\}\) of \(V\) into two three-element sets. The embedded disjoint triangles \(G[A]\) and \(G[B]\) define a geometric product torus and an integral two-cycle.

There is a canonical consistent normalization \(z_P\) of their orientations such that
\[
H_2(X;\mathbb Z)\cong \mathbb Z^{9},\qquad
\sum_{P\in\mathcal P}z_P=0,
\]
and this is **the only integral relation** among the ten cycles. Every nine of their homology classes are an integral basis. Moreover, for every vertex permutation \(\sigma\in S_6\),
\[
\sigma_*(z_P)=\operatorname{sgn}(\sigma)z_{\sigma P},\qquad
H_2(X;\mathbb Z)\cong
\operatorname{sgn}_6\otimes\left(\mathbb Z[\mathcal P]/\mathbb Z\sum_{P\in\mathcal P}e_P\right).
\]
This specifies a particular **integral lattice**, not merely its rational character or rank.

## Assumptions and scope
Use the unsubdivided complete graph with its natural one-dimensional CW structure, and only two unordered collision-free particles. Every essential-to-essential path in \(K_6\) has at least one edge, and every simple graph circuit has at least three; the two-particle subdivision criterion therefore applies without modifying edges. The associated unordered cubical complex has exactly \(15\) vertices, \(60\) one-cubes, and \(45\) two-cubes; it is a deformation retract of \(X\) and has no cells in dimension greater than two.

Index edges lexicographically as the fifteen two-subsets of \(V\), each oriented from its smaller endpoint to its larger. A two-cube \((e,f)\) is indexed by a pair of *vertex-disjoint edges* in increasing edge-index order; this order determines its product orientation. A one-cube is indexed by an oriented edge \(e\) and a vertex \(v\notin e\), with its orientation inherited from \(e\).

For each \(P=\{A,B\}\), let \(A=(a_0<a_1<a_2)\) be the unique triple containing vertex \(0\), and let \(B=(b_0<b_1<b_2)\) be the complementary sorted triple. Define the directed cycles \(\gamma_A=(a_0a_1)+(a_1a_2)+(a_2a_0)\) and \(\gamma_B=(b_0b_1)+(b_1b_2)+(b_2b_0)\), where reversed edge orientation is negative. Let \(s(A,B)\in\{\pm1\}\) be the sign of the permutation with one-line notation \((a_0,a_1,a_2,b_0,b_1,b_2)\). Then
\[
z_P=s(A,B)(\gamma_A\times\gamma_B),
\]
with wedge/product coordinates translated to the preceding increasing-edge two-cube orientations. Reversing the factor order contributes a minus sign, as expected for two one-cycles.

## Proof
**1. Exact cellular boundary.** The two-cube with oriented edges \(e=[a,b]\) and \(f=[c,d]\), with \(a<b\), \(c<d\), \(e<f\), has boundary
\[
\partial_2(e,f)=(f,b)-(f,a)-(e,d)+(e,c).
\]
Here \((f,b)\) denotes the one-cube with edge \(f\) and free vertex \(b\). This fixes signs and makes a reproducible integer matrix \(B\) of dimension \(60\times45\). Each product \(z_P\) is a cycle since the two directed triangle cycles have zero boundary and lie in disjoint subgraphs. The companion program reconstructs all entries from the graph alone and verifies \(Bz_P=0\) for each of ten partitions.

**2. The diagonal relation.** For a given two-cube \((e,f)\), the endpoints of \(e\) and \(f\) are four distinct vertices, leaving exactly two vertices \(u,v\). The square occurs in only the two triangle-pair products that complete \(e\) with \(u\) and \(f\) with \(v\), or complete \(e\) with \(v\) and \(f\) with \(u\). Direct comparison of the oriented triangle edges, together with the sign of the block permutation \((A,B)\), gives opposite coefficients. Consequently \(\sum_Pz_P=0\) coefficientwise in \(C_2\), not merely modulo boundaries. These ten normalized tori are thus not linearly independent.

**3. Exact rank and saturation certificates.** Number the forty-five two-cubes lexicographically by their two edge indices. The following nine row indices (zero-based)
\[
R_9=(0,1,3,6,7,9,12,13,18)
\]
give a \(9\times9\) minor of the **unnormalized** torus matrix using the first nine partitions in the lexicographic order of their triple \(A\):
\[
\det T[R_9,0{:}9]=+1.
\]
Hence those nine integral cycles are independent and form a **primitive** sublattice of the ambient free two-chain lattice \(C_2\). On the boundary matrix use row indices
\[
R_{36}=(0,1,2,4,5,6,8,9,10,12,13,14,16,17,18,20,21,22,24,25,26,28,29,30,33,34,36,37,38,40,41,42,46,48,49,50)
\]
and column indices
\[
C_{36}=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37).
\]
The exact integer determinant is
\[
\det B[R_{36},C_{36}]=+2\ne0.
\]
Therefore \(\operatorname{rank}\partial_2\ge36\), while the nine independent two-cycles give \(\operatorname{rank}\partial_2\le45-9=36\). As no three-cells exist, \(H_2(X;\mathbb Z)=\ker\partial_2\) is a rank-nine primitive subgroup of \(C_2\). Since the first nine torus cycles themselves form a rank-nine primitive sublattice of \(C_2\), they **equal** this kernel. The relation from step 2 expresses the tenth as a sum of the first nine with coefficients \(\pm1\), proving that *every* omission gives another integral basis and that the relation module is precisely the integral diagonal.

**4. The full symmetry action.** The product of two oriented triangle cycles changes sign when the two factors are interchanged; a permutation of vertices acts on each directed triangle by the sign of its internal three-vertex reordering. Comparing these signs with the sign of the concatenated block permutation produces, for all \(\sigma\in S_6\),
\(\sigma_*(z_P)=\operatorname{sgn}(\sigma)z_{\sigma P}\). This identity can alternatively be verified *exactly* on each of the forty-five signed two-cubes for all \(720\) permutations; the supplied program does so. Because the diagonal relation spans the entire kernel among the ten cycles, their integral sign-twisted permutation quotient is exactly \(H_2(X;\mathbb Z)\).

## Verification
Run `python3 verify.py` in the directory containing this document and the verifier (Python standard library only). It regenerates the graph, the \(60\times45\) signed cellular boundary, and the \(45\times10\) torus matrix. It checks every product-torus boundary, the exact ten-term relation, the determinant-one minor, the nonzero boundary minor of determinant two, and all \(720\) vertex permutations on every normalized torus chain. All determinants use fraction-free integer elimination. The expected final line is `CONCLUSION_H2_Z9_ANY_NINE_INTEGRAL_BASIS`. These are exhaustive finite checks on the specifically defined finite CW complex; the correctness argument above supplies their topological interpretation.

## Relationship to prior work
Ko and Park, *Characteristics of Graph Braid Groups* (arXiv:1101.2648v1, 13 January 2011), establish the graph-configuration framework, the applicable cubical model, and general first-homology formulas, including the nonplanar torsion phenomenon. These are not new here. Ramos and Yun, *Computing Stable Homology Representations of Graph Configuration Spaces* (arXiv:2606.13813v1, 11 June 2026), Theorem 3.10 and Table 2, already determine the **rational** \(S_6\)-module on second unordered homology, and Proposition 3.12 identifies the relevant disjoint-three-cycle toric source in the **ordered** rational setting. The previously determined rank nine, rational Specht module, and rational toric structure are **not** claimed as new. The contribution here is the exact *integral* presentation, primitive basis property for every set of nine geometric torus classes, and corresponding integral \(S_6\)-lattice. A rational isomorphism cannot certify integral saturation or index one.

## Limitations
This result concerns precisely \(K_6\), two *unordered* collision-free particles, and second integral homology. It does not assert analogous integral presentations for larger complete graphs, other particle numbers, or first cohomology. The nine-by-nine and thirty-six-by-thirty-six determinants are finite exact certificates whose reproducibility relies on the specified indexing. Comparable but unlocated integral presentations could exist; exhaustive publication priority and independent scientific audit are not established.

## References
- K. H. Ko and H. W. Park, *Characteristics of Graph Braid Groups*, arXiv:1101.2648v1 (13 January 2011), especially introductory cubical model and Theorem 3.16.
- E. Ramos and C. H. Yun, *Computing Stable Homology Representations of Graph Configuration Spaces*, arXiv:2606.13813v1 (11 June 2026), §3.2, Theorem 3.10, Table 2, Proposition 3.12.
