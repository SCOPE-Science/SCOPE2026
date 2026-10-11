# A sharp simple-homotopy stability threshold for triangle-chorded cycles

## Finding
For an integer \(n\geq6\), let \(C_n\) have cyclically numbered vertices \(0,1,\ldots,n-1\), and form \(G_n=C_n+\{0,2\}\) by inserting the length-two chord. Write
\[
\mathcal B_3(H)=\{S\subseteq V(H):\alpha(H[S])\leq2\}.
\]
Here \(\alpha\) is the maximum cardinality of an independent vertex set, and all complexes include the empty face. Then
\[
\mathcal B_3(G_6)\searrow\{\mathrm{vertex}\},\qquad
\mathcal B_3(G_n)\searrow\mathcal B_3(C_n)\simeq S^3\quad(n\geq7).
\]
The arrows denote **finite sequences of elementary simplicial collapses**, not just equalities of Betti numbers. For \(n\geq7\), exactly \(4n-18\) faces are introduced by the chord, and they cancel in \(2n-9\) explicit free-face pairs. Hence the six-vertex exception is a genuine homotopy change: \(\mathcal B_3(C_6)\simeq S^3\) while \(\mathcal B_3(G_6)\) is contractible.

## Assumptions and scope
The graph is finite, simple, and has **only** the cycle edges and the additional edge \(\{0,2\}\). There are no pendant edges, additional chords, or claims about other distances. The parameter is every integer \(n\geq6\). The result determines simple-homotopy behavior over the integers; it does not assert an equivariant collapse.

## Proof
**Face-difference lemma for \(n\geq7\).** Denote \(A=\mathcal B_3(C_n)\) and \(K=\mathcal B_3(G_n)\). Adding an edge can only eliminate independent triples that contain both its endpoints. Consequently \(A\subseteq K\); every face of \(K\setminus A\) contains vertices \(0\) and \(2\), together with some vertex \(j\) satisfying \(4\leq j\leq n-2\).

The complete list of added faces is
\[
\begin{aligned}
T_j&=\{0,2,j\},&4\leq j\leq n-2,\\
A_j&=\{0,1,2,j\},&4\leq j\leq n-2,\\
B_j&=\{0,2,j,j+1\},&3\leq j\leq n-2,\\
U_j&=\{0,1,2,j,j+1\},&3\leq j\leq n-2.
\end{aligned}
\]
To see exhaustiveness, note first that every five-element subset of a cycle on at least six vertices contains an independent triple, so \(A\) has no faces of cardinality five or more. Any added face must contain \(\{0,2\}\). If it has at least six vertices and contains \(1\), at least three selected vertices lie in the induced path on \(\{3,\ldots,n-1\}\); two of these are nonadjacent, and together with \(1\) they form an independent triple. If it omits \(1\), at least four selected vertices lie in that path; at least three are in \(\{3,\ldots,n-2\}\), two of which are nonadjacent and form an independent triple with \(0\). Thus no added face has more than five vertices.

A five-element added face must contain \(1\): if it omitted \(1\), the other three vertices would be in \(\{3,\ldots,n-1\}\); to avoid an independent triple with \(0\), two in \(\{3,\ldots,n-2\}\) must be consecutive, while the third must be \(n-1\). Among those two consecutive vertices, one is neither \(3\) nor \(n-2\), and together with \(2,n-1\) it forms an independent triple. With \(1\) present, the other two vertices must be consecutive because \(1\) is nonadjacent to every vertex of \(\{3,\ldots,n-1\}\). Therefore precisely the five-element faces \(U_j\) occur. A four-element added face containing \(1\) is precisely an \(A_j\); without \(1\), its other two vertices must be consecutive, giving \(B_j\) (including the endpoint pair \(\{n-2,n-1\}\)). Three-element added faces are exactly the \(T_j\). Conversely every listed face has independence number at most two: each \(U_j\) is a subset of the union of the triangle on \(\{0,1,2\}\) and the edge on \(\{j,j+1\}\), so no independent triple exists. The other listed faces are its subsets. Thus the list is exact.

**Two-stage collapse.** For each \(3\leq j\leq n-2\), the tetrahedron \(B_j\) is contained in exactly one maximal five-vertex face, namely \(U_j\). Hence remove the free pair \((B_j,U_j)\), for all such \(j\). After these \(n-4\) elementary collapses, each added triangle \(T_j\), for \(4\leq j\leq n-2\), lies in the unique remaining added tetrahedron \(A_j\). No face originally in \(A\) can contain a newly added face, by downward closure. Remove each free pair \((T_j,A_j)\). Exactly \(n-5\) further elementary collapses leave **precisely** \(A\). This proves the claimed simple-homotopy equivalence without using a homology-only inference.

**Homotopy type.** Carnero Bravo's Corollary 39, citing the cycle total-cut classification, establishes \(\mathcal B_3(C_n)\simeq S^3\) for all \(n\geq6\). The explicit collapse therefore identifies \(\mathcal B_3(G_n)\simeq S^3\) for all \(n\geq7\).

**Six-vertex boundary.** The complete face set of \(\mathcal B_3(G_6)\) has \(56\) elements including the empty face, with nonempty face counts \((6,15,19,12,3)\) by increasing cardinality. The accompanying `verify.py` enumerates all those faces directly from the graph edges, then constructs and checks \(27\) elementary free-face pairs, reducing the complex to the single vertex \(0\). Every step is checked against the actual current maximal faces, giving a finite complete collapse certificate.

## Verification
Execute `python3 verify.py` using Python 3 and its standard library. The program independently enumerates the face sets of \(\mathcal B_3(C_n)\) and \(\mathcal B_3(G_n)\) for every integer \(7\leq n\leq18\), checks the complete predicted difference including absent six-vertex faces, and replays the free-face collapses. It separately constructs the entire six-vertex complex and verifies its \(27\) elementary collapses. The successful output is `VERIFY_OK 27 six-vertex collapses; 12 full enumerations and exact two-stage elementary collapses`. These finite tests supplement the parameter-uniform combinatorial argument above; they are not substituted for it.

## Relationship to prior work
The bounded-independence construction is the three-robust clique complex of Filakovský's 2026 paper, which studies bipartite square-sequence graphs. Carnero Bravo's 2026 Corollary 39, building on earlier cycle results, already establishes the sphere type of \(\mathcal B_3(C_n)\); this known cycle classification is an input, not a new claim. Neither source gives the explicit simple collapse from the triangle-chorded graph to the cycle. In particular the inserted chord creates a triangle and removes bipartiteness, so results restricted to bipartite graphs do not cover this graph. The additional \(n-4\) four-dimensional faces make equality of dimensions or Euler characteristics alone insufficient to establish the new conclusion.

## Limitations
The proof applies to exactly one chord connecting vertices two steps apart and to \(n\geq6\), not to arbitrary chord lengths or extra edges. The six-vertex case is proved using a complete finite certificate; its deterministic implementation is included. No new classification of the unchorded cycles is claimed. A mathematical literature search cannot rule out equivalent unindexed work, and no independent audit has been performed.

## References
1. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427 (first public 2026-02-24), particularly Corollary 39 and Section 5.3, https://arxiv.org/abs/2602.21427.
2. M. Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365 (first public 2026-02-11), https://arxiv.org/abs/2602.11365.
3. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503 (2022), as cited for the cycle case by Carnero Bravo.
