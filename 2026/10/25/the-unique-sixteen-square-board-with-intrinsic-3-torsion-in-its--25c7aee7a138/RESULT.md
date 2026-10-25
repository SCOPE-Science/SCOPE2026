# The unique sixteen-square board with intrinsic \(3\)-torsion in its rook complex

## Finding
Let \(B=[5]\times[5]\) and let \(M(A)\), for \(A\subseteq B\), be the simplicial complex of all nonattacking rook placements on the allowed squares \(A\). Thus vertices are occupied squares, and faces are subsets having at most one square in each row and each column.

**Theorem.** For every \(A\subseteq B\) with \(|A|\le15\), \(H_2(M(A);\mathbb Z)\) is torsion-free. Among the boards with exactly sixteen allowed squares, precisely one isomorphism type, under separate permutations of rows and columns, has torsion in \(H_2\). A representative \(A_*\), given row by row, is
\[
\{1,2\},\quad \{1,3,4\},\quad \{3,4,5\},\quad
\{2,3,4,5\},\quad \{2,3,4,5\}.
\]
For this exceptional board,
\[
H_2(M(A_*);\mathbb Z)\cong\mathbb Z/3\mathbb Z.
\]
Its inclusion in the full chessboard complex induces an isomorphism
\[
H_2(M(A_*);\mathbb Z)\longrightarrow H_2(M_{5,5};\mathbb Z)
\cong\mathbb Z/3\mathbb Z.
\]
Exactly \(3600\) labeled sixteen-square boards have this property. The statement concerns **intrinsic torsion of the induced complex**, not the minimum number of vertices in a cycle mapping nontrivially into the ambient torsion group.

## Assumptions and scope
The board has five distinguished row positions and five distinguished column positions. A board is a subset of its 25 squares; unused rows and columns are permitted. Allowed symmetries independently permute rows and columns, without assuming transposition. \(M(A)\) is the full simplicial matching complex of the bipartite graph whose edges are the occupied squares; homology is unreduced integral simplicial homology in degree two. The conclusions quantify over *every* board with at most sixteen occupied squares, not merely connected or spanning boards.

Use zero-based square index \(5r+c\) for \(r,c\in\{0,1,2,3,4\}\). The exceptional board has row bitmasks \((3,13,28,30,30)\), with least significant bit recording the first column. The order-three cycle can be written as the join product
\[
z=(e_{11}-e_{12})\wedge(e_{23}-e_{24})\wedge(e_{35}-e_{45}),
\]
with the wedge interpreted as the alternating oriented product of reduced zero-cycles on the three disjoint row/column groups. Its eight oriented triangles have square-index triples \((0,7,14),(0,7,19),(0,8,14),(0,8,19),(1,7,14),(1,7,19),(1,8,14),(1,8,19)\), with coefficients \((1,-1,-1,1,-1,1,1,-1)\), respectively.

## Proof
**Exhaustive orbit reduction.** Represent a row by a five-bit mask. Permuting the rows makes its five masks nondecreasing, and permuting the five columns acts through the 120 permutations of bit positions. Taking the lexicographically least transformed sorted row tuple yields one canonical representative of every row-and-column orbit: enumerating every five-element multiset of the 32 row masks and retaining those with total population at most sixteen is exhaustive. The standalone verifier constructs these representatives instead of relying on an imported table. The numbers of canonical types for \(|A|=0,1,\ldots,16\) are
\[
(1,1,3,6,16,34,69,130,234,367,527,669,755,755,669,527,367).
\]

**Integral torsion criterion.** For each canonical board, construct signed simplicial boundary \(\partial_3:C_3(M(A);\mathbb Z)\to C_2(M(A);\mathbb Z)\). Repeatedly choose a matrix entry equal to \(\pm1\), eliminate its row and column by integral elementary operations, and continue until there is no unit entry. Every pivot is unimodular. Since \(\operatorname{im}\partial_2\) is a free abelian group and the exact sequence
\[
0\to H_2(M(A);\mathbb Z)\to C_2(M(A);\mathbb Z)/\operatorname{im}\partial_3\to\operatorname{im}\partial_2\to0
\]
splits, the torsion of \(H_2\) is exactly the torsion of the cokernel of \(\partial_3\). The verifier checks that the entire residual integer matrix is zero for every one of the \(4763\) canonical boards with fewer than sixteen squares, and for 366 of the 367 canonical sixteen-square boards. Here \(4763\) is the sum of the first sixteen type counts above.

**Exceptional certificate.** For the remaining board, the complex has \((c_0,c_1,c_2,c_3,c_4)=(16,82,161,108,14)\). The exact integer reduction of \(\partial_3\) produces 93 unit pivots and one residual nonzero column consisting of twelve \(+3\) and twelve \(-3\) entries (all other remaining columns zero). Hence the torsion of its second homology is exactly \(\mathbb Z/3\mathbb Z\), while \(\operatorname{rank}_{\mathbb Q}\partial_3=94\). Exact mod-three reduction gives \(\operatorname{rank}_{\mathbb F_3}\partial_2=67\); since \(\partial_2\partial_3=0\), its rational rank is at most \(161-94=67\), and by reduction modulo three it is at least 67. Thus \(\operatorname{rank}_{\mathbb Q}H_2=161-94-67=0\), so \(H_2(M(A_*);\mathbb Z)\cong\mathbb Z/3\mathbb Z\), with no free part.

**Nontrivial ambient inclusion.** The displayed chain \(z\) satisfies \(\partial_2 z=0\). Over \(\mathbb F_3\), the image of \(\partial_3\) has rank 93 on \(A_*\), and adjoining \(z\) raises it to 94. On the full board the ranks of \(\partial_2\) and \(\partial_3\) modulo three are respectively 176 and 423; adjoining the same \(z\) to the full third-boundary image raises rank to 424. Therefore the induced map on degree-two mod-three homology is nonzero. The established integral calculation \(H_2(M_{5,5};\mathbb Z)\cong\mathbb Z/3\mathbb Z\) of Shareshian–Wachs and Jonsson, together with the one-dimensional mod-three homology on both sides, implies the integral inclusion map is an isomorphism. Independent row and column permutations of \(A_*\) produce \(3600\) distinct labeled boards, verified by complete enumeration of the \(5!\cdot5!\) permutations.

## Verification
Run `python3 verify_chessboard_16.py` from the package directory. The script requires only Python's standard library, generates all boards rather than reading a dataset, performs signed exact integral unit elimination, checks both simplicial boundary compositions, independently calculates the mod-three ranks and explicit cycle nonboundary tests, and counts the labeled symmetry orbit. The supplied `verification_output.txt` records the executed deterministic output. In particular, the verifier prints `VERIFY_OK_UNIQUE_16_SQUARE_INTRINSIC_THREE_TORSION` only after every assertion passes.

## Relationship to prior work
Shareshian and Wachs, *Torsion in the Matching Complex and Chessboard Complex* (arXiv:math/0409054, notably Theorem 1.7 and Section 8), establish ambient chessboard torsion and examine subboards for connectivity and nonzero homology. Their sufficient subboard cycles may be supported on fewer squares without producing **intrinsic** homology torsion in that smaller induced complex. Jonsson, *On the 3-torsion Part of the Homology of the Chessboard Complex* (arXiv:1203.5644, Section 3), gives a computer-free proof of the full \(M_{5,5}\) group and constructs generators using a substantially larger subcomplex. Those statements neither classify all sparse \(5\times5\) boards by intrinsic torsion nor yield the uniqueness of the sixteen-square threshold. The exact first-threshold uniqueness and integral inclusion of the exceptional minimal board are the present result.

## Limitations
The assertion is restricted to subboards of a five-by-five board, their degree-two intrinsic integral homology, and support cardinalities at most sixteen. It is not a homotopy classification, a universal bound for other chessboard sizes, nor an assertion that every smaller support maps trivially to ambient \(H_2\). Finite exhaustive classification proves the stated finite range but does not establish an all-parameter theorem. The previously known full-board homology group is used as a cited premise; the code independently checks the required finite boundary ranks and the nonzero inclusion.

## References
1. John Shareshian and Michelle L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, initial public preprint 3 September 2004; *Advances in Mathematics* **212** (2007), 525–570. Section 8 addresses subboards and Theorem 1.7 handles ambient torsion.
2. Jakob Jonsson, *On the 3-torsion Part of the Homology of the Chessboard Complex*, arXiv:1203.5644, initial public preprint 26 March 2012; *Annals of Combinatorics* **14** (2010), 487–505. Section 3 computes \(H_2(M_{5,5};\mathbb Z)\).
