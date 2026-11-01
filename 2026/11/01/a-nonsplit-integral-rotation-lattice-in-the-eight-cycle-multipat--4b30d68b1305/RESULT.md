# A nonsplit integral rotation lattice in the eight-cycle multipath complex

## Finding
Let \(D\) be the fully bidirected cycle on \(\mathbb Z/8\mathbb Z\), and let \(X=X(D)\) be its simplicial multipath complex. Each directed edge is a vertex of \(X\), and a set of directed edges is a simplex precisely when its directed graph is a disjoint union of directed paths and isolated vertices. The rotation \(\rho(i)=i+1\) acts on \(X\).

The natural rank-three integral lattice \(L=H_3(X;\mathbb Z)\) is **not** the direct sum of the integral rotation-sign lattice and any integral rank-two lattice realizing the quarter-turn rational representation. Despite
\[
L\otimes\mathbb Q\cong\mathbb Q_{-}\oplus\mathbb Q(i),
\]
the rational summands cannot be separated over \(\mathbb Z\). The obstruction is already visible modulo two: the rotation on \(H^3(X;\mathbb F_2)\), in an explicitly computed basis, has matrix
\[
A=\begin{pmatrix}1&0&1\1&0&0\1&1&0\end{pmatrix}\pmod2,
\qquad\dim_{\mathbb F_2}\ker(A-I)=1.
\]
In fact \(A-I\) has rank two and is a single three-dimensional nilpotent Jordan block. This is a finite, exact integral non-splitting result; no extension-class order is claimed.

## Assumptions and scope
The graph has exactly eight vertices and sixteen distinct directed arcs. Write \(f_i:i\to i+1\) and \(b_i:i+1\to i\), indices modulo eight, and number arc vertices \(0,\ldots,7\) for \(f_i\) and \(8,\ldots,15\) for \(b_i\). A set of arcs is a multipath if each graph vertex has indegree and outdegree at most one and there is no directed cycle. For this underlying simple undirected cycle, the forbidden directed cycles are a reverse-arc pair or all eight arrows in one coherent direction. Cohomology and mod-two reduction use ordinary simplicial cochains, with no additional normalization.

## Proof
**1. Rational constituents.** Caputi–Collari–Smith, Theorem 2.10 (their polygon parameter is seven), gives \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^3\), \(\widetilde H_6(X;\mathbb Z)\cong\mathbb Z^2\), and no other reduced integral homology. The two top classes are the boundaries of the forbidden all-forward and all-backward eight-arc simplices. Rotation acts on either by the sign of an eight-cycle. Thus its traces on degree six for \(\rho,\rho^2,\rho^4\) are respectively \(-2,2,2\).

The reduced Lefschetz numbers for those three rotations are respectively \(-1,3,-1\). For \(\rho\), only the empty arc set is invariant. For \(\rho^2\), the invariant multipaths comprise the empty set and four singleton edge orbits, giving four isolated geometric fixed points. For \(\rho^4\), the invariant orbit selections are precisely the multipaths of the four-vertex bidirected cycle; its reduced Euler characteristic is \(-1\), by the cited homology theorem or direct enumeration. The Lefschetz identity, using degrees three and six, yields
\[
\operatorname{tr}(\rho\mid H_3)=-1,\quad
\operatorname{tr}(\rho^2\mid H_3)=-1,\quad
\operatorname{tr}(\rho^4\mid H_3)=3.
\]
Because \(\rho^4\) is of finite order and has trace three on a rational three-dimensional space, it is the identity there. Consequently the eigenvalues of \(\rho\) are \(-1,i,-i\); the rational representation is exactly \(\mathbb Q_-\oplus\mathbb Q(i)\).

**2. Exact mod-two action.** Enumerate each nonempty subset of the sixteen arcs and retain exactly the multipaths defined above. The complete simplex counts in dimensions zero through six are
\[
(16,96,272,384,272,96,16).
\]
Form the coboundary matrices over \(\mathbb F_2\) by face containment. In degrees two and three their ranks are \(191\) and \(190\), respectively. Hence
\[
\dim H^3(X;\mathbb F_2)=384-190-191=3.
\]
An exact Gaussian elimination of the degree-three cocycle space modulo degree-two coboundaries produces three quotient classes. Rotating their supporting directed-edge sets, reducing modulo coboundaries and expressing in this basis gives rotation-matrix columns (encoded as three-bit integers) \((7,4,1)\), i.e. the displayed matrix \(A\). The rank of \(A-I\) is two. The attached standalone Python checker enumerates all faces, constructs both matrices, performs these quotient eliminations, and checks every stated finite calculation. This proves the degree-three mod-two invariant dimension to be one, not merely an experimental estimate.

**3. Obstruction to integral splitting.** Since integral homology is torsion-free and is concentrated in degrees three and six, the universal coefficient theorem identifies \(H^3(X;\mathbb F_2)\) with the mod-two reduction of the dual lattice \(L^*=\operatorname{Hom}(L,\mathbb Z)\), equivariantly (up to the harmless choice between \(\rho\) and \(\rho^{-1}\)). If \(L\) split as the integer sign line plus a rank-two lattice \(M\) with rational eigenvalues \(i,-i\), the reduction of the sign line would have a one-dimensional fixed subspace. On \(M\), the integral action \(R\) satisfies \(R^2=-I\). Modulo two, \((R-I)^2=0\) but \(R\not\equiv I\pmod2\): otherwise \(R=I+2B\) would give \(I+2(B+B^2)=0\), impossible modulo two. Thus its mod-two reduction has a one-dimensional fixed subspace. Every such split lattice, and also its dual, therefore has **two** mod-two fixed dimensions. The computed value is one. The integral decomposition cannot exist.

## Verification
Run `python3 bp8_integral_rotation.py` with standard Python 3. The verifier prints `FACES 16 96 272 384 272 96 16`, `COBOUNDARY_RANKS degree2=191 degree3=190`, `H3_F2_DIMENSION 3`, `ROTATION_COLUMNS_BINARY 7 4 1`, `RANK_ROTATION_MINUS_IDENTITY 2`, `FIXED_DIMENSION 1`, and `VERIFY_OK`. All relevant faces and boundary incidences for the specified finite graph are exhaustively generated; no sampling is used. The rational trace step is a mathematical deduction from the cited published homology ranks and direct fixed-face counts.

## Relationship to prior work
Caputi, Collari and Smith compute the integral Betti numbers and connectivity of all bidirected polygon multipath complexes but do not determine this integral cyclic lattice. The separately published *Dihedral rational homology of bidirectional-polygon multipath complexes* determines the rational dihedral character, hence the two rational summands, but expressly does not identify the integral group-ring lattice. Its rational character does not imply the splitting or non-splitting exhibited here. The new information is the mod-two Jordan extension tying together distinct rational eigenspaces.

## Limitations
The theorem concerns the eight-vertex cycle only and proves non-splitting, not the full integral isomorphism class, exact extension order, or an all-cycle formula. It uses published integral Betti numbers; the finite mod-two action and non-splitting argument are independently reproducible from the included code and proof. Equivalent unindexed work remains a residual originality risk; there has been no independent mathematical audit.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (first public January 9, 2026), especially Theorem 2.10. https://arxiv.org/html/2601.05670v1
2. *Dihedral rational homology of bidirectional-polygon multipath complexes* (public mathematical result, 2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-dihedral-rational-homology-of-bidirectional-polygon-multipath-co--627013477864
