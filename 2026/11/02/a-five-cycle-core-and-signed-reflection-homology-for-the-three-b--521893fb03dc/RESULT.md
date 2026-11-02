# A five-cycle core and signed reflection homology for the three-by-four perfect-matching complex

## Finding
Let \(G=P_3\square P_4\) be the Cartesian grid graph with three rows and four columns. Let \(X=\mathcal M_p(G)\) be the simplicial complex whose vertices are edges of \(G\) and whose maximal faces are perfect matchings. Then
\[
X\simeq S^1,\qquad H_1(X;\mathbb Z)\cong\mathbb Z,
\]
with all other reduced homology zero. The natural row-reflection \(u\) and column-reflection \(v\) commute, and their complete action on the first integral homology is
\[
(u_*,v_*,(uv)_*)=(-1,+1,-1).
\]
In particular, the column-reflection quotient retains a one-dimensional rational first homology, whereas the row-reflection and full Klein-four quotients have vanishing reduced rational homology.

## Assumptions and scope
The graph is the **Cartesian** product, not the categorical graph product. Its vertices are \((r,c)\) with \(0\le r<3\) and \(0\le c<4\). Two vertices are adjacent when their Manhattan distance equals one. The vertices of \(X\) are the seventeen grid edges. Every simplex is a subset of one of the eleven perfect matchings. The row reflection is \(u(r,c)=(2-r,c)\); the column reflection is \(v(r,c)=(r,3-c)\). They act on \(X\) by permuting the grid edges. All homotopy statements concern geometric realizations of finite simplicial complexes.

## Proof
**Exact collapse.** Enumerate the seventeen grid edges in the following fixed order: scan \((r,c)\) lexicographically by row then column, writing its downward edge when one exists and then its rightward edge when one exists. Enumerate perfect matchings recursively by taking the least unmatched grid vertex and pairing it with each available neighboring vertex. This produces eleven maximal simplices of six edges each. All subsets of these maximal simplices give 495 faces including the empty face, with nonempty face counts by dimension
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(17,85,164,151,66,11).
\]

`COLLAPSE.json` records 242 ordered face pairs as integer bit masks in this edge order. In each ordered pair \((a,b)\), \(a\) is a codimension-one face of \(b\) and has exactly one codimension-one coface in the currently remaining complex. It is therefore a genuine elementary simplicial collapse. The standalone `CHECK.py` reconstructs all original faces from the graph itself, checks both incidences and the unique-coface condition for **each** consecutive pair, and removes it. Exactly ten nonempty faces remain: the five vertices with edge indices \(10,13,14,15,16\), joined by precisely the five one-simplices
\[
\{10,15\},\ \{10,16\},\ \{13,14\},\ \{13,15\},\ \{14,16\}.
\]
These edges form the chordless pentagonal cycle \(10\text{--}15\text{--}13\text{--}14\text{--}16\text{--}10\). A sequence of elementary collapses is a homotopy equivalence, proving \(X\simeq S^1\) integrally (not merely rationally).

**Symmetry character.** For a graph symmetry \(g\), its simplicial Lefschetz number is computed directly from the original complex by
\[
L(g)=\sum_{\varnothing\ne\sigma\in X\,;\,g\sigma=\sigma}(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma),
\]
where the sign is that of the permutation of the vertices of each fixed simplex, in the fixed increasing edge-index order. The checker enumerates every simplex, verifies the induced edge permutations, and obtains
\[
L(u)=2,\qquad L(v)=0,\qquad L(uv)=2.
\]
Since \(X\) is connected and has only degree-one reduced homology, the Lefschetz formula yields \(L(g)=1-\operatorname{tr}(g_*|H_1(X;\mathbb Q))\). Therefore the rational homology character is \((-1,+1,-1)\). The integral group \(H_1(X;\mathbb Z)\cong\mathbb Z\) admits only automorphisms \(\pm1\); the rational character thus determines the integral actions.

**Quotients.** For a finite group acting simplicially, barycentric subdivision removes inversions and transfer/averaging in characteristic zero gives \(H_*(X/H;\mathbb Q)\cong H_*(X;\mathbb Q)^H\). Applying this to \(H=\langle v\rangle\), \(\langle u\rangle\), and \(\langle u,v\rangle\) proves the stated quotient rational homology. No assertion about integral quotient torsion is made.

## Verification
The complete standalone proof certificate consists of `CHECK.py` and `COLLAPSE.json`. Run `python CHECK.py` with these two files in the same directory. The checker reconstructs eleven facets and 495 faces without consulting a precomputed face table, verifies all 242 free-face incidences, checks the exact residual cycle, evaluates oriented fixed-simplex traces for all three nonidentity symmetries, and prints `GRID34_COMPLETE_COLLAPSE_AND_SYMMETRY_OK` on success. The certificate is finite and exhaustive for the stated grid. It does not assert a result for arbitrary grid sizes.

## Relationship to prior work
Chandrakar and Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809 (first publicly submitted 2024-07-08; revised 2025-04-07), prove the nonequivariant homotopy classification for two-row grids in Theorem 3.3 and explicitly pose the broader rectangular-grid sphere-wedge conjecture in Conjecture 6.1. The three-by-four Cartesian grid is the first three-row, even-column instance beyond the previously treated two-row family; the paper does not give its exact collapse or reflection homology character. Matsushita's paper on **ordinary** matching complexes of small grids studies a different simplicial construction. Bayer, Jelić Milutinović and Vega study perfect-matching complexes of honeycomb graphs, not the rectangular grid of this claim. The result is therefore a precisely scoped finite case with equivariant data; no resolution of the full-grid conjecture is claimed.

## Limitations
The conclusion is limited to one natural grid, \(P_3\square P_4\), and its two geometric reflections. It neither proves the conjectured sphere-wedge type for all rectangular grids nor determines integral torsion in quotient spaces. The proof relies on a 242-step integer-encoded elementary-collapse certificate, fully replayable from the supplied files. Identical but unindexed computations or unpublished equivalent results cannot be excluded by the literature comparison.

## References
1. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809, first version 2024-07-08, revised version 2025-04-07. https://arxiv.org/html/2407.05809v2.
2. T. Matsushita, *Matching complexes of small grids*, Electronic Journal of Combinatorics 26(3) (2019), #P3.1 (ordinary matching complex).
3. M. Bayer, M. Jelić Milutinović, and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, Electronic Journal of Combinatorics 30(2) (2023), #P2.45.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (elementary collapses and discrete Morse background).
