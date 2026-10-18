# A six-block homotopy decomposition for three-dimensional \(3\times3\times n\) chessboards

## Finding

For each integer \(n\ge3\), let \(X_n\) be the three-dimensional chessboard complex on positions \((i,j,k)\), where \(i,j\in\{0,1,2\}\) and \(k\in\{0,\ldots,n-1\}\): a set of positions is a face exactly when its positions have pairwise different values in **each** coordinate. Let \(Y_n=\Delta_{3,n}\) denote the ordinary two-dimensional chessboard complex of nonattacking rooks on three rows and \(n\) columns.

There is a homotopy equivalence, natural at the level of the six indicated subcomplexes,
\[
X_n\simeq\left(\bigvee_{\sigma\in S_3}Y_n\right)\vee\bigvee^{9n-5}S^1.
\]
Consequently the **complete integral homotopy types** are
\[
X_n\simeq
\begin{cases}
\bigvee^{46}S^1,&n=3,\\[2mm]
\left(\bigvee^6(S^1\times S^1)\right)\vee\bigvee^{31}S^1,&n=4,\\[2mm]
\bigvee^{9n-5}S^1\vee\bigvee^{6(n^3-6n^2+8n-1)}S^2,&n\ge5.
\end{cases}
\]
Each wedge of tori means a wedge of based copies of \(S^1\times S^1\), **not** a connected sum. In particular, \(\pi_1(X_n)\) is free of rank \(9n+19\) when \(n=3\), is the free product of six copies of \(\mathbb Z^2\) and a free group of rank \(31\) when \(n=4\), and is free of rank \(9n-5\) for \(n\ge5\). All integral homology is torsion-free.

## Assumptions and scope

The complex is **not** a clique or independence complex of its ordinary cell-adjacency grid. It is the matching complex of the complete tripartite three-uniform hypergraph with parts of sizes \(3,3,n\): one rook rules out any other rook sharing any coordinate. Faces have cardinality at most three, and all six components in the wedge above are based and connected. The theorem covers all integers \(n\ge3\), with no asymptotic or numerical assumption. The primary topological statement is the based homotopy equivalence of finite CW complexes; no assertion of equivariant homotopy equivalence is made.

## Proof

**1. Six blocks and their intersections.** For each permutation \(\sigma\in S_3\), let \(Y_n^\sigma\subseteq X_n\) be induced by the \(3n\) vertices \((i,\sigma(i),k)\) with \(i\in\{0,1,2\}\) and \(0\le k<n\). Forgetting the middle coordinate gives a simplicial isomorphism \(Y_n^\sigma\cong\Delta_{3,n}\). Every face of \(X_n\) with two or three vertices belongs to exactly one block: two distinct first- and second-coordinate values specify two entries of a permutation of three letters, hence the unique third entry. Every singleton \((i,j,k)\) belongs to exactly the two permutations satisfying \(\sigma(i)=j\). Thus \(X_n=\bigcup_{\sigma\in S_3}Y_n^\sigma\), every nonempty pairwise block intersection consists of \(n\) discrete vertices (and contains no edges), and every triple intersection is empty.

Two permutations have a common assignment \(i\mapsto j\) precisely when their quotient is a transposition, so the intersection graph on the six permutations is the complete bipartite graph \(K_{3,3}\), with the even and odd permutations as its parts. For each of its nine edges there are precisely \(n\) distinct identification vertices, yielding \(9n\) individual identifications.

**2. Homotopy gluing.** Each \(Y_n^\sigma\) is path connected for \(n\ge3\). Replace each point-identification between two disjoint block copies with a closed interval having endpoints at those two points. Contracting each interval recovers their original union, and this map is a homotopy equivalence (the homotopy pushout of cofibrations along discrete points). As each block is path connected, moving the attaching point of each interval inside its block to a chosen basepoint does not change the homotopy type of the resulting graph of spaces. The latter is a wedge of the six blocks with the realization of a connected multigraph having six vertices and \(9n\) edges, hence first Betti number \(9n-6+1=9n-5\). This proves the displayed uniform decomposition. No higher nerve-intersection terms occur because no vertex lies in three blocks.

**3. The \(3\times n\) blocks.** For all \(n\ge3\), the ordinary chessboard complex \(Y_n\) has face numbers
\[
(f_0,f_1,f_2)=(3n,\;3n(n-1),\;n(n-1)(n-2)).
\]
For \(n=3\), each edge belongs to exactly one triangle, so all six triangles may be removed by elementary simplicial collapses. The remaining connected graph has first Betti number \(1-f_0+f_1-f_2=4\). Thus \(Y_3\simeq\bigvee^4 S^1\).

For \(n=4\), every edge belongs to exactly two triangles. Every vertex link is a six-cycle, making \(Y_4\) a closed connected triangulated surface. Orient its triangles by the parity of the permutation of four columns obtained by appending the unused column to the three selected columns in row order. Adjacent triangles give opposite induced edge orientations. Thus the surface is orientable, and its Euler characteristic is \(12-36+24=0\); classification of orientable closed surfaces identifies \(Y_4\cong S^1\times S^1\) as a topological surface.

For \(n\ge5\), Theorem 1.1 of Björner--Lovász--Vrećica--Živaljević proves \(Y_n\) is \((\nu-2)\)-connected, with \(\nu=\min\{3,n,\lfloor(n+4)/3\rfloor\}=3\). Hence \(Y_n\) is simply connected. It is two-dimensional, so its only reduced integral homology is a free group in degree two, of rank
\[
\widetilde\chi(Y_n)=3n-3n(n-1)+n(n-1)(n-2)-1
=n^3-6n^2+8n-1.
\]
By Hurewicz, a set of maps from two-spheres representing an integral basis induces an isomorphism on all homology. The homological Whitehead theorem for simply connected CW complexes makes their wedge a homotopy equivalence. Therefore \(Y_n\simeq\bigvee^{n^3-6n^2+8n-1}S^2\).

**4. Substitution.** Substitute these three ordinary-chessboard classifications into the six-block decomposition. For \(n=3\), the circle rank is \(6\cdot4+(9\cdot3-5)=46\). For \(n=4\), the six torus summands and \(9\cdot4-5=31\) circles survive. For \(n\ge5\), the number of circle and sphere summands is as stated. This also establishes all asserted integral homology groups and fundamental groups.

## Verification

The included `verify.py` is a self-contained Python 3 program requiring only the standard library. Run `python3 verify.py`. It exhaustively rebuilds the faces of \(X_n\) and \(Y_n\) for \(3\le n\le7\), checks uniqueness of the block carrying each edge, that each vertex occurs in precisely two blocks, that all triple intersections vanish, and that the six-block multigraph has \(9n\) edges. It also verifies the ordinary chessboard boundary ranks over two finite fields, checks orientability and vertex links of \(Y_4\), and matches Euler characteristics to the symbolic formula. Its final line is `VERIFY_OK BLOCK_COVER SIX_ORDINARY_CHESSBOARDS NINE_N_POINT_GLUINGS NO_TRIPLE_INTERSECTIONS`.

The infinite-family proof is the gluing argument and published chessboard-connectivity theorem, **not** an inference from the finite computational samples. Finite-field ranks are likewise not used as proofs of integral torsion-freeness.

## Relationship to prior work

Björner, Lovász, Vrećica and Živaljević established the connectivity bound for ordinary two-dimensional chessboard complexes. Their explicit descriptions of small chessboards include the torus at \((3,4)\); their Section 3 treats inclusion of ordinary chessboard homology into higher-dimensional chessboards, but does not provide the present six-block homotopy splitting for \((3,3,n)\). Živaljević and Vrećica's work on cycle-free chessboard complexes concerns a different subcomplex condition, and its ordinary \((3,4)\) discussion agrees with the torus identification. The present statement concerns the **three-way** nonattacking-rook matching complex, not the ordinary two-dimensional one or the independence complex of a categorical graph product.

Michelle Wachs's *Topology of matching, chessboard, and general bounded degree graph complexes* (Section 9, especially Problems 9.10--9.13) defines multidimensional chessboards and surveys rational homology, connectivity and higher-dimensional hypergraph questions. Its inspected general statements do not supply a six-copy \(3	imes n\) homotopy splitting or the persistent free fundamental group of the \(3	imes3	imes n\) subclass.

## Limitations

No general formula for arbitrary tripartite side lengths \((a,b,n)\) is claimed; the uniqueness of the completing permutation is special to two sides of size three. The equivalence is nonequivariant, and neither a preferred set of based wedge maps nor a natural splitting under every coordinate permutation is claimed. Absolute bibliographic priority cannot be established by searches alone; an equivalent higher-dimensional-rook decomposition under different terminology remains a residual literature risk.

## References

1. A. Björner, L. Lovász, S. T. Vrećica, R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, Journal of the London Mathematical Society **49** (1994), 25–39. DOI: `10.1112/jlms/49.1.25`; accessible full text: `https://lovasz.web.elte.hu/morepapers/chess.pdf` (especially Theorem 1.1 and Section 3).
2. S. Vrećica and R. T. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:`0710.5252`, version 1 publicly submitted 27 October 2007. Contextual comparison with ordinary chessboard complexes.
3. M. L. Wachs, *Topology of matching, chessboard, and general bounded degree graph complexes*, survey, Section 9, public full text `https://www.math.miami.edu/~wachs/papers/tmc.pdf` (general higher-dimensional chessboard definitions and open problems).
