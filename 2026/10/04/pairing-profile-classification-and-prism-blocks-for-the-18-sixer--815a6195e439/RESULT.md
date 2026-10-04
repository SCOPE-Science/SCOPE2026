# Pairing-profile classification and prism blocks for the 18-sixer orbit on the Fermat cubic surface
## Finding
Let \(S_F\subset\mathbf P^3\) be the Fermat cubic surface \(x_0^3+x_1^3+x_2^3+x_3^3=0\). The three pairings of the four coordinates partition its 27 lines into three nine-line families \(\mathscr F_0,\mathscr F_1,\mathscr F_2\). For a sixer \(T\), set
\[
p(T)=\operatorname{sort}\bigl(|T\cap\mathscr F_0|,|T\cap\mathscr F_1|,|T\cap\mathscr F_2|\bigr).
\]
Every sixer has exactly one of the profiles \(p(T)=(0,3,3)\) or \(p(T)=(2,2,2)\). These profiles exactly distinguish the two automorphism orbits of sixers: the 18-element orbit has profile \( (0,3,3)\), while the 54-element orbit has profile \( (2,2,2)\).

The 18-element orbit has a further canonical three-block structure. For \(r\in\{0,1,2}\), let \(B_r\) consist of the sixers omitting \(\mathscr F_r\). Then \(|B_r|=6\). Any two sixers from distinct blocks meet in exactly one line. Inside each \(B_r\), exactly nine of the 15 unordered pairs are disjoint and exactly six meet in three lines. The graph on \(B_r\) whose edges are disjoint pairs is a triangular prism; the graph whose edges are the pairs meeting in three lines is a 6-cycle. Hence, among all unordered pairs of sixers in the 18-element orbit, intersection sizes \(0,1,3\) occur respectively \(27,108,18\) times.

## Assumptions and scope
The line families use the standard three coordinate pairings
\[
(01|23),\qquad(02|13),\qquad(03|12),
\]
and within each pairing the two line equations use cube roots of unity. A sixer means a set of six pairwise skew lines. The claim is set-theoretic and combinatorial for the Fermat cubic surface over characteristic zero. It does not assert an analogous profile classification for arbitrary smooth cubic surfaces.

## Proof
Favacchio--Malara prove that the Fermat cubic has 72 sixers and that its automorphism group has exactly two orbits on them, of sizes 18 and 54. Their orbit representatives have, respectively, three lines from each of two coordinate-pairing families and no line from the third, and two lines from each of all three families.

The diagonal subgroup of the Fermat automorphism group preserves each of the three coordinate-pairing families, while coordinate permutations permute the three families. Therefore the sorted profile \(p(T)\) is automorphism-invariant. Since the two published representatives have profiles \( (0,3,3)\) and \( (2,2,2)\), and the two published orbits exhaust all 72 sixers, those are the only profiles and they characterize the two orbits.

For the 18-element orbit, the omitted pairing is therefore well-defined. Coordinate permutations act transitively on the three pairings, so the three omitted-family blocks have equal size; because they partition an 18-element orbit, each has size six.

It remains to determine intersections inside and across those blocks. This is a finite exact calculation. The accompanying verifier constructs the 27 lines over the exact field \(\mathbf Q(\omega)\), with \(\omega^2+\omega+1=0\), declares two lines skew precisely when their four defining linear equations have rank four, enumerates all six-cliques in the resulting skewness graph, and reconstructs the 648 monomial automorphisms. It obtains exactly 72 sixers in orbits of sizes 18 and 54 and then performs the complete pair census in the 18-orbit. Across distinct omitted-family blocks all \(6\cdot6=36\) pairs have intersection one. In each block, the 15 pairs split as nine with intersection zero and six with intersection three. The disjointness graph is connected and 3-regular on six vertices with exactly two triangles, hence is the triangular prism; the three-line-intersection graph is connected, 2-regular, and triangle-free on six vertices, hence is \(C_6\). Summing over the three blocks and three cross-block pairs gives \(27,108,18\) for intersection sizes \(0,1,3\).

## Verification
Run `python verify.py`. The verifier uses only Python's standard library and exact rational arithmetic in \(\mathbf Q(\omega)\). It independently reconstructs the 27 lines, all 72 sixers, the 648 monomial automorphisms, the orbit sizes, the two profile classes, the three six-element blocks, every cross-block and within-block intersection, and both six-vertex graph types. The recorded output ends in `VERIFY_OK`.

## Relationship to prior work
Favacchio--Malara establish the 72 sixers, the 18/54 orbit decomposition, explicit representatives, and the associated blow-down models. Those facts supply the finite universe and the two representative profiles. The profile criterion for every sixer, the omitted-family block decomposition of the 18-orbit, and the complete intersection/prism-cycle census above are not stated in the inspected article or its public computational source. The present result is a structural consequence plus an exhaustive exact refinement of their classification, not a new count of sixers.

## Limitations
The novelty check covered the initiating article, its public computational source, targeted searches for equivalent formulations, a semantic database search, and the prior accepted local ledger. A classical source could encode the same incidence structure under different terminology; this remains a residual originality risk. The verifier proves the finite incidence statement exactly but does not supply a moduli-theoretic interpretation of the triangular-prism blocks.

## References
1. Giuseppe Favacchio and Grzegorz Malara, *On the Geometry of Sixers on the Fermat Cubic Surface*, arXiv:2608.23716v1, 24 August 2026.
2. Grzegorz Malara, public companion repository for the paper, `GrzMal/sixers-on-the-fermat-cubic-surface`, including `fermat_sixers.py`.
