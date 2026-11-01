# Five independent three-torsion classes survive diagonal deletion in the six-by-six chessboard complex

## Finding
Let \(Q=[6]\times[6]\) be the complete six-by-six chessboard and let \(D=\{(i,j)\in Q:i\ne j\}\) be the board with its diagonal removed. For a board \(E\), let \(\mathcal M(E)\) be its rook (matching) complex: simplices are collections of positions in distinct rows and distinct columns. The canonical inclusion
\[\iota:\mathcal M(D)\hookrightarrow\mathcal M(Q)\]
induces an **injection on all three-primary torsion in reduced integral third homology**:
\[
\iota_*:T_3\widetilde H_3(\mathcal M(D);\mathbb Z)
\longrightarrow T_3\widetilde H_3(\mathcal M(Q);\mathbb Z)
\quad\text{is injective}.
\]
In fact the groups are \((\mathbb Z/3\mathbb Z)^5\) and \((\mathbb Z/3\mathbb Z)^{10}\), respectively, so this is a five-dimensional injection of \(\mathbb F_3\)-vector spaces. Here \(T_3\) denotes the subgroup of elements of three-power order. The groups themselves were previously calculated; the assertion about the **map** is the finding.

## Assumptions and scope
The board has exactly six rows and six columns, and the forbidden positions are the six pairs with equal indices. Orientation of every simplex is the increasing ordering of the integer label \(6i+j\), with \(0\le i,j<6\). The chain group \(C_k\) is freely generated over \(\mathbb Z\) by matchings of size \(k+1\). The boundary is the alternating signed deletion of one position. The map \(\iota_*\) is that of the literal inclusion with identical positions and orientations. No statement is made for other board sizes, higher torsion exponents, or other degrees.

## Proof
**Step 1: finite integral boundary data.** Enumerate a matching by its increasing rows and its ordered distinct columns. The complete numbers of simplices, including the empty face as the first entry, are
\[
(1,30,315,1420,2715,1854,265)\quad\text{for }\mathcal M(D)
\]
and
\[
(1,36,450,2400,5400,4320,720)\quad\text{for }\mathcal M(Q).
\]
The relevant integral boundary matrices are \(\partial_4^D:C_4(D)\to C_3(D)\), of size \(2715\times1854\), and \(\partial_4^Q\), of size \(5400\times4320\). The attached `verify.py` creates every matrix entry directly from these definitions; no external tables are inputs.

**Step 2: the five source torsion generators.** Perform 1552 exact unit-pivot eliminations of \(\partial_4^D\). Each pivot has coefficient \(\pm1\); the algorithm records unimodular integral changes of columns together with original-column witnesses. The remaining 302 columns include exactly 16 nonzero columns, all divisible by three. Upon division by three, the residual nonzero matrix has Smith factors
\[
\operatorname{diag}(1,1,1,1,1,0,\ldots,0).
\]
Thus the full integral boundary matrix has precisely five nonunit Smith factors, each equal to three. Consequently the three-primary torsion in \(\operatorname{coker}\partial_4^D\), and hence in \(\widetilde H_3(\mathcal M(D);\mathbb Z)\), is \((\mathbb Z/3\mathbb Z)^5\). The equality of torsion subgroups follows from the exact sequence \(0\to H_3\to\operatorname{coker}\partial_4\to\operatorname{im}\partial_3\to0\), because the last group is free abelian.

More concretely, let \(w_j\in C_4(D)\) be the tracked integral column witnesses for each of the 16 nonzero residual columns. Put \(z_j=(\partial_4^D w_j)/3\in C_3(D)\). These are integral because every residual entry is divisible by three. The verifier checks the identities \(\partial_4^D w_j=3z_j\) independently using the **original unreduced boundary matrix**. Applying \(\partial_3\) gives \(3\partial_3 z_j=0\); since \(C_2\) is torsion-free, each \(z_j\) is an integral cycle. Their mod-three homology classes span a five-dimensional space, which is exactly the image of source three-torsion under reduction modulo three.

**Step 3: injectivity after restoring the diagonal.** The inclusion sends each \(z_j\) to the same signed three-chain on the complete board. Over \(\mathbb F_3\), an exact sparse elimination of the complete-board \(\partial_4^Q\) gives rank \(3380\); the corresponding rank for \(\partial_4^D\) is \(1552\). Reduce the sixteen embedded \(z_j\) modulo these respective boundary subspaces. Their classes span dimension five **both before and after inclusion**. As each \(z_j\) is killed by three in integral homology, all source three-torsion classes map to three-torsion classes. An element in the kernel of the integral map would reduce to zero over \(\mathbb F_3\), contradicting the preserved dimension five. The source three-torsion reduction is injective by the universal coefficient theorem, so the entire three-primary torsion map is injective.

Every cited pivot, Smith factor and finite-field rank is computed by the self-contained attached program. The proof is a complete exact finite chain calculation, not extrapolation from numerical samples.

## Verification
Run `python3 verify.py` from the package directory with Python 3.10 or later and SymPy installed. The program enumerates all faces afresh, constructs signed integral simplicial boundaries, executes a witness-tracked unit-pivot reduction, checks exact integral boundary identities, computes Smith normal form on the residual matrix, and independently projects the resulting torsion cycles into both mod-three homology quotients. Its full stdout is in `verification_output.txt`, ending in `VERIFY_OK`. All arithmetic is exact integers or finite-field arithmetic. The verifier specifies a deterministic ordering and performs every claimed check without external inputs or previously stored matrix files.

## Relationship to prior work
Shareshian and Wachs, *Torsion in the Matching Complex and Chessboard Complex* (public arXiv version dated September 3, 2004), identify these rook complexes and report the above source and target integral homology groups in Tables 8.1 and 1.2. Their Section 8, especially Lemma 8.2 and Theorem 8.3, establishes nonvanishing under inclusion, not injectivity of the full five-dimensional three-torsion subgroup. Therefore neither the already-known torsion ranks nor their nonvanishing lemma imply the present five-dimensional persistence statement. The exact map is the additional object computed here.

Jonsson's *On the 3-torsion Part of the Homology of the Chessboard Complex* treats the ambient rectangular chessboard homology through long exact sequences and related methods; its inspected results do not provide the exact diagonal-deletion inclusion map. The crown graph formulation \(\mathcal M(K_{6,6}\setminus M)\hookrightarrow\mathcal M(K_{6,6})\), or equivalently the derangement-rook-complex inclusion, is the same object, not an independent result.

## Limitations
The theorem is for one canonical finite inclusion; it does not assert a general theorem for all deleted diagonals. The source and target group computations are prior results rather than newly discovered ranks. The proof is reproducible but depends on correct execution of finite exact arithmetic and the explicitly described Smith and modular rank arguments; independent mathematical validation has not been performed. Existing equivalent work outside the inspected sources may exist.

## References
1. J. Shareshian and M. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054v1 (first posted September 3, 2004), especially Tables 1.2 and 8.1 and Section 8. https://arxiv.org/html/math/0409054v1
2. J. Jonsson, *On the 3-torsion Part of the Homology of the Chessboard Complex*, arXiv:1203.5644 (2012 preprint). https://arxiv.org/abs/1203.5644
3. A. Björner and V. Welker, *Complexes of directed graphs*, SIAM Journal on Discrete Mathematics 12 (1999), 413–424 (connectivity result as cited in [1]).
