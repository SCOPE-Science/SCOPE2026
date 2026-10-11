# Empty triangles realize all shortest integral homology types in the 1133 minimal Klein bottle
## Finding
Let \(K\) be the unique eight-vertex Klein-bottle triangulation in Cervone's valence class 1133. Its first integral homology is
\[
H_1(K;\mathbb Z)\cong \mathbb Z\oplus\mathbb Z/2.
\]
If \(t\) denotes the unique element of order two and \(g\) is a primitive generator of the free quotient, then the 20 empty triangles of \(K\) have the exact unoriented homology spectrum
\[
8\cdot t,\qquad 6\cdot \{g,-g\},\qquad 6\cdot \{g+t,-g+t\}.
\]
In particular, every empty triangle is homologically essential. The three-edge simple cycles realize exactly the three nonzero unoriented integral-homology types whose free coordinate has absolute value at most one.

With Cervone's labels, the order-two triangles are \(ABC,ABG,ADE,ADG,BCF,BCH,CEF,DEF\). Choosing \(g\) to be the class of \(ABE\), the six representatives of \(\{g,-g\}\) are \(ABE,ABF,ACD,ACF,AFH,BDF\), and the six representatives of \(\{g+t,-g+t\}\) are \(ACE,BCD,BDE,BEG,CDG,CEG\).

## Assumptions and scope
The complex is the 1133 triangulation displayed and analyzed by Cervone. The verifier uses the sixteen faces read from Cervone's face table:
\[
ABD,ABH,ACG,ACH,ADF,AEF,AEG,BCE,BCG,BDG,BEF,BFH,CDE,CDF,CFH,DEG.
\]
These faces have \(8\) vertices, \(24\) edges, and \(16\) triangles. Their vertex degrees are \(4,5,6,6,6,7,7,7\), so the degree-count vector is exactly 1133. Cervone proves that this degree class contains a unique eight-vertex Klein-bottle triangulation.

An empty triangle means a three-vertex set whose three edges occur in the one-skeleton but which is not a two-simplex. Homology classes are integral unless a coefficient field is explicitly shown. Orientation is forgotten only in the final multiplicity statement, so \(x\) and \(-x\) count as the same unoriented type.

## Proof
Contract the spanning tree consisting of the seven edges incident to vertex \(A\). The remaining \(17\) edges give generators for the integral cycle group of the one-skeleton. The sixteen oriented face boundaries give a \(16\times17\) presentation matrix \(R\) for \(H_1(K;\mathbb Z)\).

Exact elimination gives \(\operatorname{rank}_{\mathbb Q}R=16\). The greatest common divisor of the seventeen maximal \(16\times16\) minors is \(2\). Hence the cokernel has free rank one and torsion subgroup of order two, proving
\[
H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2.
\]

The signed maximal minors also give a primitive right-null vector of \(R\). After division by their gcd, this vector defines a primitive homomorphism \(H_1(K;\mathbb Z)\to\mathbb Z\), hence a free coordinate. Exhausting all three-cliques in the one-skeleton gives \(36\) triangles in the graph: the \(16\) faces and exactly \(20\) empty triangles. Evaluation of the primitive free coordinate on those twenty cycles is zero on exactly eight and has absolute value one on exactly twelve.

To distinguish zero from the order-two class, reduce the same presentation modulo \(2\). The relation matrix has rank \(15\) over \(\mathbf F_2\), so \(H_1(K;\mathbf F_2)\) has dimension two. Every one of the twenty empty triangles is nonzero in this quotient. Therefore each of the eight cycles with zero integral free coordinate is the unique nonzero torsion element \(t\). The other twelve cycles have primitive free coordinate \(\pm1\). Their mod-two classes split into two classes of six, which are exactly the two torsion cosets of a primitive free class, namely \(\{g,-g\}\) and \(\{g+t,-g+t\}\) after choosing \(g=[ABE]\).

Finally, every simple three-edge cycle in a simplicial complex is a three-clique. The facial three-cliques are null-homologous and the twenty nonfacial three-cliques are precisely the empty triangles just classified. Thus no additional three-edge homology types occur.

## Verification
The standalone `verify.py` reconstructs the face complex, checks the 1133 valence profile, forms the spanning-tree presentation, computes all maximal determinants by fraction-free Bareiss elimination, derives the primitive cofactor cocycle, enumerates every three-clique, and classifies all empty triangles integrally and modulo \(2\). Its replay result is:

`VERIFY_OK f=8,24,16 valence=4x1,5x1,6x3,7x3 H1=Z+Z/2 empty3=20 integral_classes=8,6,6 torsion_empty=8 primitive_empty=12 mod2_nonzero=20`

The determinant computation is exact over the integers; no floating-point or probabilistic step is used.

## Relationship to prior work
Cervone classifies all eight-vertex Klein-bottle triangulations, proves uniqueness of the 1133 valence class, and gives the exact labeled 1133 complex. He also uses mod-two first homology when analyzing possible immersion double-sets, but does not classify the homology classes of the complex's empty triangles. Sulanke's later complete irreducible-triangulation classification concerns equivalence classes and irreducibility, not this integral empty-triangle spectrum. Lutz's survey places the eight-vertex Klein bottle in the vertex-minimal triangulation literature.

The closest retrieved contemporary record concerns homology actions of minimal finite-space Klein-bottle models rather than simplicial empty triangles, and therefore neither implies nor tabulates the \(8,6,6\) spectrum here.

## Limitations
The claim concerns one of the six combinatorially distinct eight-vertex Klein-bottle triangulations: the unique 1133 type. It does not assert the same spectrum for the other five types, nor does it classify longer cycles. The literature comparison cannot exclude an unindexed historical computation of the same finite spectrum. The public-source date records the earliest exact public full-text snapshot verified for the Cervone source, not the journal issue date.

## References
1. D. P. Cervone, *Vertex-Minimal Simplicial Immersions of the Klein Bottle in Three Space*, Geometriae Dedicata 50 (1994), 117–141. DOI: 10.1007/BF01265307. Author full text archived at timestamp 20040309191227.
2. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:math/0506372v1, 18 June 2005.
3. T. Sulanke, *Note on the Irreducible Triangulations of the Klein Bottle*, arXiv:math/0407008v1, 1 July 2004.
