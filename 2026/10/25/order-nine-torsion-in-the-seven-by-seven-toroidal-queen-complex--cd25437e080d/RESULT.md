# Order-nine torsion in the seven-by-seven toroidal queen complex

## Finding

Let \(Q_7\) be the abstract simplicial complex whose vertices are the \(49\) squares \((x,y)\in(\mathbb Z/7\mathbb Z)^2\), and whose nonempty faces are sets of pairwise nonattacking queens on the toroidal board. Two queens attack if their difference has zero first coordinate, zero second coordinate, zero coordinate difference, or zero coordinate sum, all modulo \(7\).

The **complete reduced integral homology** is
\[
\widetilde H_i(Q_7;\mathbb Z)\cong
\begin{cases}
\mathbb Z/9\mathbb Z,&i=2,\\
\mathbb Z^{120},&i=3,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, a natural board-placement complex has genuine order-nine (rather than merely order-three) integral torsion. Furthermore, \(Q_7\) is simplicially isomorphic to the clique complex of the Paley graph of order \(49\).

## Assumptions and scope

Torus means both chessboard directions are periodic, and diagonals wrap in the same way. A face is a subset of squares, with at most one queen per square. The homology uses the usual integral oriented simplicial boundary, with augmentations used for reduced degree zero. The claim concerns exactly the order-seven toroidal board; it asserts integral homology, not a specific homotopy decomposition.

## Proof

**Equivalence to the square-order Paley graph.** Identify \(\mathbb F_{49}=\mathbb F_7[\omega]\), with \(\omega^2=3\), where \(3\) is nonsquare modulo \(7\). Map a board square to
\[
\Phi(x,y)=(2x+3y)+(2x+y)\omega.
\]
The determinant of the underlying \(\mathbb F_7\)-linear map is \(3\), hence \(\Phi\) is bijective. Its norm satisfies \(N(\Phi(x,y))=-(x^2+y^2)\). A nonzero element of \(\mathbb F_{49}\) is a square exactly when its norm belongs to \(\{1,2,4\}\subset\mathbb F_7\). For every nonzero displacement \((x,y)\), this norm is a square precisely when \(x\ne0\), \(y\ne0\), and \(y/x\in\{2,3,4,5\}\). These are exactly the nonattacking displacements, so the legal-placement graph is the Paley graph. The accompanying verifier checks all \(1{,}176\) unordered pairs directly.

**Exhaustive face complex.** Generate each clique exactly once by appending higher-labeled compatible vertices. The numbers of faces in dimensions \(0\) through \(6\) are, respectively,
\[
(49,588,2156,2450,882,196,28).
\]
There are exactly \(6{,}349\) nonempty faces. Of the maximal faces, \(294\) have size \(5\) and \(28\) have size \(7\). These counts also provide an independent Euler-characteristic check: the alternating face sum is \(-119\), consistent with the final free rank \(120\) and no free second homology.

**Acyclic discrete-Morse reduction.** Label square \((x,y)\) by \(7x+y\). Apply the elementary toggle algorithm to the complete set of faces using the vertex order stored in `verify.py` (the `ORDER` list). At each vertex, simultaneously pair every still-unmatched face not containing the vertex with its still-unmatched union with that vertex, removing both. This makes \(3{,}093\) pairs and leaves exactly \(163\) critical simplices: one dimension-zero simplex, twenty-one dimension-two simplices, and one hundred forty-one dimension-three simplices. The complete Hasse diagram has \(6{,}349\) nodes and \(23{,}226\) face incidences. Reverse its matched arrows and perform an exhaustive topological sort; every node is reached. Hence the matching is acyclic, yielding an integral Morse chain complex with precisely the stated critical generators and no other positive-dimensional degrees.

**Integral boundary and Smith certificate.** Orient every face by increasing vertex labels. To obtain the third Morse boundary, eliminate each matched lower triangle against its paired tetrahedron with its signed unit incidence. Recursively, a critical triangle projects to its basis vector, an upper-matched triangle to zero, and a lower-matched triangle to the negative signed projection of the other facets of its paired tetrahedron. The resulting exact integral matrix is \(21\times141\), with \(1{,}055\) nonzero entries and maximum absolute entry \(3\). Its complete signed rows appear in `MORSE_MATRIX.tsv`, whose SHA-256 is `3c1e317b0ee8d399811ab580f53ab7d9c6cdb0d480372b316e8c0047b1f5dabf`.

Use elementary integral row and column operations to isolate twenty unit pivots, then take the gcd of the remaining row of length \(121\). It is \(9\), with the row nonzero. Every operation is unimodular and the prior twenty diagonal pivots are not disturbed, so the Smith invariant factors are exactly \(1\) twenty times and \(9\) once. In the reduced Morse complex, the second differential is zero because there are no critical one-cells; hence its degree-two homology is the cokernel of this third differential, namely \(\mathbb Z/9\). Its degree-three homology is the kernel of this surjective-over-\(\mathbb Q\) \(21\times141\) map and is free of rank \(141-21=120\). There are no other reduced critical degrees. This proves the claim.

## Verification

The standalone standard-library Python script `verify.py` reconstructs the graph and all faces, tests the Paley correspondence for every pair, builds the matching, checks all directed incidences for acyclicity, independently constructs the signed Morse differential, computes twenty unit pivots and a final row gcd of nine, and calculates the simplicial boundary ranks over \(\mathbb F_2\). Its actual output is `verification_output.txt`; the computed matrix SHA-256 agrees with `MORSE_MATRIX.tsv`. The six nontrivial mod-two boundary ranks, in ascending degree, are \((48,540,1616,714,168,28)\), agreeing with the free integral third-homology rank \(120\) and absence of two-torsion.

To reproduce: with Python 3, place `verify.py` alone in a writable directory and run `python3 verify.py`. No third-party software or downloads are required. Verify the last row gcd and the terminal `VERIFY_OK` line (printed first by design). Note that mod-two arithmetic alone cannot detect the order-nine torsion; the exact integer reduction is essential.

## Relationship to prior work

The published toroidal-queen literature, including Cairns (2001), concerns existence and maximum numbers of nonattacking placements rather than integral topology of the complex of *all* placements. The Paley-graph literature, including Blokhuis (1984) and Baker–Ebert–Hemmeter–Woldar (1996), determines maximum and some other maximal clique configurations, but those results do not determine the integral boundary maps among all clique faces. The latter paper was inspected in full in its available author-uploaded transcription, including its theorems and examples. Related indexed graph-topology calculations for Paley graphs of order \(29\) or \(17\) concern different spaces or graph orders and do not imply this conclusion. No directly equivalent integral computation was found in the searches performed; this is qualified bibliographic evidence, not a guarantee that an unindexed statement does not exist.

## Limitations

The theorem concerns the exact \(7\times7\) periodic-board complex, equivalently the Paley-order-\(49\) clique complex. No claim is made about arbitrary rectangular boards, other moduli, or the full integral homotopy type. The proof is an exhaustive finite certificate implemented in Python; it is not independent validation. Earlier maximal-clique classifications are treated as prior information rather than as new results. The first exact-day public date verified for the toroidal-queen primary source used here is June 11, 2001; the related Paley-clique article appeared in 1996, but its first public *day* was not verified in the accessible record.

## References

1. G. Cairns, *Queens on Non-square Tori*, Electronic Journal of Combinatorics **8** (2001), N6, first published 2001-06-11, DOI: `10.37236/1591`.
2. R. D. Baker, G. L. Ebert, J. Hemmeter and A. J. Woldar, *Maximal cliques in the Paley graph of square order*, Journal of Statistical Planning and Inference **56** (1996), 33–38, DOI: `10.1016/S0378-3758(96)00006-7`.
3. A. Blokhuis, *On subsets of \(GF(q^2)\) with square differences*, 1984, DOI: `10.1016/1385-7258(84)90036-2` (abstract and citation inspected).
