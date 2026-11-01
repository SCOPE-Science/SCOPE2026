# Triality action on the \(D_4\) root-poset antichain complex

## Finding
Let \(P\) be the positive-root poset of type \(D_4\), \(X\) its simplicial complex of antichains, and \(G\cong S_3\) the diagram-automorphism group permuting the three outer simple roots. Let \(V\) denote the two-dimensional standard rational representation of \(S_3\). The full graded reduced rational homology representation is
\[
\widetilde H_0(X;\mathbb Q)\cong2\mathbf 1,\qquad
H_1(X;\mathbb Q)\cong\mathbf 1\oplus2V,\qquad
H_2(X;\mathbb Q)\cong\operatorname{sgn};
\]
all other reduced rational homology groups vanish. Thus the top homology orientation changes sign under each diagram transposition, while degree-one homology has a single invariant line.

The actual geometric fixed-point spaces distinguish the subgroup types. For any transposition \(t\), any three-cycle \(c\), and \(G=S_3\),
\[
|X|^{\langle t\rangle}\simeq (S^1\vee S^1)\sqcup\{\mathrm{pt}\}\sqcup\{\mathrm{pt}\},\qquad
|X|^{\langle c\rangle}=|X|^G\cong_{\mathrm{PL}}[0,1]\sqcup\{\mathrm{pt}\}^{\sqcup4}.
\]
The equality in the second formula is equality of subsets of \(|X|\), not merely a homotopy equivalence. Together the fixed-locus classification and character determination form one equivariant-topology theorem.

## Assumptions and scope
Use orthonormal vectors \(e_1,\ldots,e_4\) and simple roots \(\alpha_1=e_1-e_2\), \(\alpha_2=e_2-e_3\), \(\alpha_3=e_3-e_4\), \(\alpha_4=e_3+e_4\). The positive roots are precisely the twelve \(e_i\pm e_j\) for \(1\le i<j\le4\). A positive root is represented by its nonnegative coefficient quadruple in the ordered basis \((\alpha_1,\alpha_2,\alpha_3,\alpha_4)\), and the root order is componentwise order of coefficients. Two roots span an edge of \(X\) exactly when neither is below the other. The \(S_3\)-action permutes coefficient positions \(1,3,4\) while fixing position \(2\), and hence preserves the order, the simplices, and the geometric realization. The three conjugacy types are identity, transposition, and three-cycle. No claim is made about the integral isomorphism class of the degree-one group ring lattice.

## Proof
**1. Complete root and face description.** The twelve roots, indexed from \(1\) to \(12\) and grouped in increasing coefficient sum, are
\[
\begin{gathered}
(0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0),\\
(0,1,0,1),(0,1,1,0),(1,1,0,0),\\
(0,1,1,1),(1,1,0,1),(1,1,1,0),\\
(1,1,1,1),(1,2,1,1).
\end{gathered}
\]
A direct componentwise-incomparability test yields exactly the following seventeen maximal simplices, written by their root indices: `1234`, `127`, `146`, `167`, `1,10`, `245`, `257`, `2,9`, `456`, `4,8`, `567`, `5,10`, `6,9`, `7,8`, `8,9,10`, `11`, `12`. Here an unseparated three- or four-digit string denotes separate one-digit vertex labels. Their nonempty subfaces consist of \(12\) vertices, \(24\) edges, \(12\) triangles and one tetrahedron. In the augmented rational simplicial chain complex the boundary ranks, ordered by chain dimensions \(-1,0,1,2\) as targets, are
\[
\operatorname{rank}\partial_0=1,\quad
\operatorname{rank}\partial_1=9,\quad
\operatorname{rank}\partial_2=10,\quad
\operatorname{rank}\partial_3=1.
\]
These follow by exact rational row reduction of the finite signed incidence matrices defined by the displayed maximal simplices (the included verifier constructs them from the original coordinate roots). Hence the reduced Betti numbers are \(2,5,1,0\) in degrees \(0,1,2,3\). Vertices \(11\) and \(12\) are isolated, and the other ten lie in one connected component. The two isolated vertices and the remaining component are each preserved by the entire diagram group. Therefore \(\widetilde H_0(X;\mathbb Q)\) is two copies of the trivial representation, not an arbitrary two-dimensional permutation module.

**2. Fixed-set orbit-simplex lemma.** For any finite group \(H\) acting simplicially on a complex with vertex set \(P\), a point of its realization is fixed exactly when its unique barycentric coordinate vector is constant on every \(H\)-orbit of vertices. Its support must be a face. Thus the fixed set is PL homeomorphic to the simplicial complex whose vertices are those whole \(H\)-orbits that individually form faces, and whose simplices are collections of vertex orbits whose union forms a face. This proves the orbit construction without assuming that a fixed geometric point is an original vertex.

**3. Order-three and full-diagram fixed loci.** The three-cycle and full \(S_3\) have identical orbits on the twelve roots: six admissible vertex orbits, indexed here in increasing order by their least root as \(A,B,C,D,E,F\). The root content is \(A=\{1,2,4\}\), \(B=\{3\}\), \(C=\{5,6,7\}\), \(D=\{8,9,10\}\), \(E=\{11\}\), \(F=\{12\}\). Among distinct orbits, precisely \(A\cup B\) is an antichain. Therefore both fixed loci are exactly one closed one-simplex and four isolated points, and in fact are the same subset of \(|X|\).

**4. Transposition fixed locus.** For the diagram transposition exchanging \(\alpha_1\) and \(\alpha_3\), the nine admissible root orbits are indexed \(0,\ldots,8\) in the following order: \(\{1\}\), \(\{2,4\}\), \(\{3\}\), \(\{5\}\), \(\{6,7\}\), \(\{8,9\}\), \(\{10\}\), \(\{11\}\), \(\{12\}\). Exact incomparability gives as maximal simplices the triangle \(\{0,1,2\}\), the six edges \(\{0,4\}\), \(\{0,6\}\), \(\{1,3\}\), \(\{3,4\}\), \(\{3,6\}\), \(\{5,6\}\), and the two isolated vertices \(7\), \(8\). Thus the fixed complex has nine vertices, nine edges and one triangle. The edge \(\{0,1\}\) is a free face of the unique triangle, so one elementary collapse removes it and that triangle. The remaining graph has a connected seven-vertex, eight-edge component and two isolated vertices. A connected graph with seven vertices and eight edges has cycle rank \(8-7+1=2\), so the fixed space has the stated homotopy type.

**5. Character determination.** Write \(\chi_j(g)=\operatorname{tr}(g\mid\widetilde H_j(X;\mathbb Q))\). By the (reduced) Hopf–Lefschetz formula, the alternating trace on homology is the reduced Euler characteristic of the geometric fixed locus; one may barycentrically subdivide to obtain a pointwise simplicial fixed subcomplex. The three alternating traces (identity, transposition, three-cycle) are \(-2,0,4\), respectively. We already have \(\chi_0=(2,2,2)\) and \(\dim H_1=5\), \(\dim H_2=1\). An element of order three acts as \(+1\) on the one-dimensional rational \(H_2\), while each transposition acts by some common \(s\in\{+1,-1\}\). Accordingly
\[
\chi_1=(5,2+s,-1),\qquad \chi_2=(1,s,1).
\]
Write \(\chi_1=a\mathbf1+b\operatorname{sgn}+cV\), with \(a,b,c\) nonnegative integers and \(V\) of character \((2,0,-1)\). If \(s=+1\), then the three character equations uniquely give \((a,b,c)=(2,-1,2)\), impossible. Hence \(s=-1\) and the unique solution is \((a,b,c)=(1,0,2)\). This proves the claimed full graded rational character. The nonnegative-integrality argument is essential; the alternating traces alone do not, without this representation-theoretic step, determine the top sign.

## Verification
Run `python3 verify.py`. This self-contained Python program derives all twelve positive roots from the explicit \(D_4\) simple basis, enumerates every antichain, performs exact rational Gaussian elimination of augmented signed boundary matrices, constructs the fixed orbit-simplex complexes independently for the identity subgroup types, identifies the transposition triangle-and-graph collapse, checks the two fixed complexes and their component ranks, and verifies the unique allowable character solution. Its expected final marker is `VERIFY_OK`. The enumerations are exhaustive for this finite root system; no extrapolation to higher-rank \(D_n\) is made.

## Relationship to prior work
Mu and Welker (arXiv:2609.14054, first publicly posted 12 September 2026) introduce the antichain complex of root posets and determine shellability by Dynkin type, making type \(D_4\) a natural first nonshellable case. Existing nonequivariant homology and homotopy classifications of this particular finite complex determine dimensions of the groups but do not by themselves determine the diagram-automorphism action. Classical foldings \(D_4\to G_2\) and \(D_4\to B_3\) explain why the subgroup fixed loci are natural to consider; the theorem also supplies their actual geometric homotopy types and, crucially, the full rational \(S_3\) action on separate homology degrees. No assertion about Coxeter group actions on distinct Boolean, Coxeter, or hyperplane-arrangement complexes is made.

## Limitations
The finite equivariant computation determines rational homology characters, not the entire integral degree-one module, any unstable equivariant homotopy type, nor a uniform result for higher-rank root systems. The first paper's public abstract and bibliographic record were accessible, but its complete manuscript was not obtainable for a page-by-page comparison; this leaves possible incidental overlap in its uninspected sections. Equivalent older results under the language of Dynkin folding and nonnesting antichains may be unindexed. Neither a negative literature search nor the finite computation constitutes independent validation.

## References
1. L. Mu and V. Welker, *Simplicial Complexes of Antichains in Root Posets and Related Combinatorics of Dyck Paths*, arXiv:2609.14054v1 (first posted 2026-09-12), https://arxiv.org/abs/2609.14054.
2. C. M. Ringel, *The Root Posets and Their Rich Antichains*, arXiv:1306.1593 (2013), https://arxiv.org/abs/1306.1593. (Background on root-poset antichains, not an equivariant computation.)
3. Standard Dynkin diagram folding of \(D_4\) to \(G_2\) or \(B_3\), as background for the diagram-automorphism action (no use of a folding homology theorem).
