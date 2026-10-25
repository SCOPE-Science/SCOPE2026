# The four-by-four Sudoku placement complex collapses to a torus

## Finding

Let \(G=\mathrm{Sud}(2)\) be the usual sixteen-vertex Sudoku graph, with a vertex for each square of a four-by-four board divided into four two-by-two blocks. Two squares are adjacent when they share a row, column, or block. Then its ordinary independence complex has the simple-homotopy reduction
\[
\operatorname{Ind}(G)\searrow L,
\qquad |L|\cong S^1\times S^1.
\]
In particular, \(\operatorname{Ind}(G)\simeq S^1\times S^1\), its fundamental group is \(\mathbb Z^2\), and its integral homology groups are \(H_0\cong\mathbb Z\), \(H_1\cong\mathbb Z^2\), \(H_2\cong\mathbb Z\), and zero in higher degrees. The cup product of a suitable integral basis of \(H^1\) evaluates to a generator of \(H^2\).

## Assumptions and scope

This is the ordinary *single-symbol placement complex*, not the complex of complete Sudoku grids or a graph coloring complex. A face records cells that may simultaneously carry one fixed symbol under Sudoku's row, column and block restrictions. The ground set is \(V=\{0,1,\ldots,15\}\); vertex \(i=4r+c\) denotes row \(r\), column \(c\), with \(0\le r,c<4\). For distinct \(i=4r+c\), \(j=4s+d\), declare a graph edge precisely when
\[
r=s\quad\text{or}\quad c=d\quad\text{or}\quad
(\lfloor r/2\rfloor,\lfloor c/2\rfloor)=(\lfloor s/2\rfloor,\lfloor d/2\rfloor).
\]
The independence complex includes the empty face; all computations below count nonempty faces. The graph has exactly 56 edges and every vertex has degree seven.

## Proof

**Complete finite face set.** Encode a face \(S\subseteq V\) by \(m(S)=\sum_{i\in S}2^i\). Start with the empty face. For each mask from 1 through 65535 in increasing order, remove its least-significant set bit, obtaining \(R\) and vertex \(i\). The mask is a face if and only if \(R\) is a face and \(i\) has no graph neighbor in \(R\). Induction on the mask proves this exhaustive recurrence. The resulting nonempty face vector by dimension is
\[
(f_0,f_1,f_2,f_3)=(16,64,64,16),
\]
with no faces of dimension above three.

**Explicit simplicial collapses.** In the current nonempty face set, let a candidate pair \((S,T)\) consist of a face and its one-vertex enlargement, with \(T\) the *only* remaining strict coface of \(S\). At each step choose the candidate minimizing the integer key \((-|T|,m(S),m(T))\), and remove both. This makes every step an elementary simplicial collapse, rather than merely a chain cancellation. The exact mask pairs, in chronological order, are:

```
(292,33060) (296,16680) (322,33090) (386,16770)
(532,33300) (536,16920) (577,33345) (641,17025)
(1048,9240) (1064,5160) (1153,9345) (1154,5250)
(2068,10260) (2084,6180) (2113,10305) (2114,6210)
(260,33028) (264,16648) (320,33088) (384,16768)
(516,33284) (520,16904) (576,33344) (640,17024)
(1025,9217) (1026,5122) (1040,9232) (1056,5152)
(2049,10241) (2050,6146) (2064,10256) (2080,6176)
```

The first sixteen pairs remove one free triangle with each tetrahedron; the last sixteen remove one free edge with each triangle. Checking all remaining strict cofaces at each step establishes freeness. Exactly 32 elementary collapses remain, leaving a two-dimensional simplicial complex \(L\) with
\[
(f_0(L),f_1(L),f_2(L))=(16,48,32).
\]

**Identify the surface.** Every remaining edge is incident with exactly two remaining triangles. The one-skeleton of \(L\) is connected; at every one of its sixteen vertices, the link is a connected two-regular graph (hence one cycle). Thus \(L\) is a connected closed triangulated surface. Assign each triangle an orientation, propagate across shared edges so their signed boundaries cancel, and verify consistency around every dual adjacency. The certificate verifies this succeeds for all 32 triangles, so the surface is orientable. Its Euler characteristic is \(16-48+32=0\). The classification of closed connected orientable surfaces therefore identifies \(|L|\) as the genus-one torus. A sequence of simplicial collapses is a simple-homotopy equivalence and proves the asserted equivalence and the stated integral (co)homological conclusions.

## Verification

The standalone standard-library-only program `verify.py` reconstructs the graph from the row/column/block rule, enumerates all 65,536 masks by the stated induction, and independently generates each collapse using the deterministic key. It checks the exact face vector, the 32 chronological pairs, coface uniqueness, the surviving face vector, the degree-two edge incidences, the connectivity of the one-skeleton and of every vertex link, and an explicitly propagated coherent orientation. The witness is an exact finite exhaustive proof certificate; it does not rely on approximate topology software, floating-point arithmetic, or a presumed homology-to-homotopy inference.

## Relationship to prior work

Sander introduced and analyzed \(\mathrm{Sud}(n)\) as a graph and determined its integral spectrum, with the special graph \(\mathrm{Sud}(2)\) pictured explicitly. This supplies the same row/column/block graph but no simplicial collapse or surface classification. Jones, Perkins and Roach's full discussion of Sudoku symmetries enumerates 288 complete four-by-four grids; these full-coloring counts do not determine the topology of compatible placements of *one* symbol. Goyal, Shukla and Singh's product-graph theorem covers independence complexes of categorical products of two complete graphs and gives wedges of circles, not the four-factor Sudoku NEPS graph. Likewise, the ordinary four-by-four rook/chessboard complex has a published sphere-wedge homotopy type, but \(\operatorname{Ind}(\mathrm{Sud}(2))\) is its proper subcomplex and that ambient classification does not imply this torus reduction. Searches of comparable indexed findings are recorded in `AUDIT.json`.

## Limitations

The result concerns precisely the sixteen-cell standard two-by-two-block Sudoku graph and does not assert a formula for larger Sudoku graphs, all partial Sudoku grid-colorings, or their homotopy types. The claim of novelty is a best-knowledge literature comparison, not proof of uniqueness; a differently indexed equivalent computation may exist. The included finite certificate proves the indicated homotopy type but is not an independently audited implementation.

## References

1. Torsten Sander, *Sudoku Graphs are Integral*, Electronic Journal of Combinatorics **16** (2009), #N25; https://doi.org/10.37236/263 (public 2009-07-24).
2. Siân K. Jones, Stephanie Perkins, Paul A. Roach, *The Structure of Reduced Sudoku Grids and the Sudoku Symmetry Group*, International Journal of Combinatorics (2012), 760310; https://doi.org/10.1155/2012/760310.
3. Shuchita Goyal, Samir Shukla, Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (2019), Proposition 3.2 and Theorem 5.1; https://arxiv.org/abs/1905.06926.
