# First noncontractible square-knight complexes and a dihedral homology transition

## Finding

For each positive integer \(n\), let \(G_n\) be the ordinary, nonperiodic \(n\)-by-\(n\) knight-attack graph. Its vertex set is \(\{(i,j):0\leq i,j<n\}\), and two distinct vertices are joined when their coordinate differences, in absolute value and in either order, are \(1\) and \(2\). Let \(K_n=\operatorname{Ind}(G_n)\) be the complex of all sets of mutually nonattacking knights.

The first noncontractible case is the four-by-four board. More precisely,
\[
K_n\simeq *\quad(1\leq n\leq3),\qquad
K_4\simeq\bigvee^{5}S^3,\qquad
K_5\simeq\bigvee^{3}S^3.
\]

Write \(D_4=\langle r,s:r^4=s^2=1,\;srs=r^{-1}\rangle\) for the geometric symmetries of the square, with \(r\) rotating by a quarter turn and \(s\) reflecting across a horizontal middle axis. The character of \(D_4\) on \(\widetilde H_3(K_n;\mathbb Q)\), in the order identity, quarter-turn, half-turn, inverse quarter-turn, horizontal reflection, vertical reflection, main-diagonal reflection, antidiagonal reflection, is
\[
\chi_4=(5,-1,1,-1,3,3,-1,-1),\qquad
\chi_5=(3,1,-1,1,-1,-1,-1,-1).
\]
Thus, with \(A_1\) the trivial character, \(A_2\) the character equal to \(+1\) on rotations and \(-1\) on reflections, \(B_1\) the character equal to \(-1\) on quarter-turns and diagonal reflections but \(+1\) on axis reflections, and \(E\) the standard two-dimensional planar representation,
\[
\widetilde H_3(K_4;\mathbb Q)\cong A_1\oplus 2B_1\oplus E,
\qquad
\widetilde H_3(K_5;\mathbb Q)\cong A_2\oplus E.
\]
In particular, the fixed rational third homology has dimension one at board size four and zero at board size five. All other reduced integral homology groups of these two complexes vanish.

## Assumptions and scope

The boards are finite square boards with ordinary edges, not toroidal or cylindrical boundary conditions. A face is *any* collection of nonattacking knights; it is not restricted to maximal placements. Rows and columns use zero-based indexing. The claimed complete homotopy types and group characters are for \(1\leq n\leq5\), with no assertion about larger boards. The group action is the eight geometric square symmetries, not a claim to represent every abstract graph automorphism.

## Proof

For \(n\leq2\) there are no knight attacks, so \(K_n\) is a simplex and hence contractible. For \(n=3\), the central square \((1,1)\) is isolated in \(G_3\), so adjoining it cones every face and the complex is contractible.

For \(n\in\{4,5\}\) we construct a fully specified acyclic matching on the **augmented** Boolean face poset. Encode \((i,j)\) by \(in+j\) and a face by the bitmask \(m(S)=\sum_{(i,j)\in S}2^{in+j}\). Start with all legal masks, including zero. Among remaining faces \(U\), for each vertex \(v\) compute the number of pairs \((S,S\cup\{v\})\) for which both masks belong to \(U\) and \(v\notin S\). Choose \(v\) maximizing the ordered pair \((\text{number of pairs},v)\), match **all** eligible pairs at that vertex, and remove their two endpoints from \(U\). Repeat until no pair remains. This rule unambiguously determines the matching; no heuristic assumption of acyclicity is needed.

For board size four, the chosen vertex indices are
\(15,12,10,14,9,13,11,8\). The construction has 680 matched pairs and leaves exactly five unmatched four-element faces with decimal masks
\(102,240,562,1220,3840\).
For board size five, the selected indices are
\(24,15,0,23,17,22,16,20,14\). It has 27,605 matched pairs and leaves exactly three unmatched four-element faces, with masks
\(30720,137344,1060992\).

The **entire** face incidences are checked, rather than a random sample: 5,788 cover relations for board size four and 353,749 for board size five. Each unmatched Hasse cover is directed from its lower to its upper face, and each matched cover is reversed. Kahn's exact topological-sort algorithm visits all 1,365 and 55,213 vertices, respectively; hence the matching orientation is acyclic. The matching includes exactly one augmented pair \((\varnothing,\{v_0\})\). Remove the empty face and that pair. The ordinary simplicial matching remains acyclic, and its critical cells are one zero-cell \(\{v_0\}\) and precisely five or three three-cells. By discrete Morse theory, each complex is homotopy equivalent to a CW complex with these cells and no cells in dimensions one or two. Every three-cell attaches to the unique point, proving the displayed integral wedges of three-spheres. This is a complete finite proof by an executable, fully specified certificate; it does not infer an infinite statement from a sample.

For the symmetry character, let \(g\) permute the board squares geometrically. The signed action of \(g\) on the oriented simplex \([v_1,\ldots,v_k]\) is the sign of the permutation of its image vertices when the underlying placement is invariant under \(g\). The reduced simplicial Lefschetz identity therefore gives
\[
\widetilde L(g)= -1+\sum_{\substack{\varnothing\ne S\in K_n\\gS=S}}
(-1)^{|S|-1}\operatorname{sgn}(g|_S).
\]
Here \(-1\) is the contribution of the augmented empty simplex. Since reduced homology is concentrated in degree three, \(\chi_n(g)=-\widetilde L(g)\). Enumerating every invariant face under all eight transformations gives the two displayed character vectors. Their inner products with the five ordinary irreducible characters of \(D_4\) give the stated decompositions. Finally, group averaging yields invariant dimensions \(\frac18\sum_g\chi_4(g)=1\) and \(\frac18\sum_g\chi_5(g)=0\).

## Verification

The standalone script `verify_knight_complex.py` uses two distinct exhaustive face-enumeration procedures, checks their sets agree, builds the matching using the rule above, verifies every face-incidence orientation is acyclic, and calculates all eight signed Lefschetz numbers. It also checks square-symmetry adjacency preservation and the irreducible-character multiplicities. Its complete output is in `verification_output.txt`.

For \(n=4\), the numbers of faces of cardinality \(0\) through \(8\) are
\((1,16,96,276,412,340,170,48,6)\).
For \(n=5\), the numbers of faces of cardinality \(0\) through \(13\) are
\((1,25,252,1360,4436,9386,13384,12996,8526,3679,994,158,15,1)\).
The certificate checks cover all faces and every Hasse incidence. The mathematical argument for the homotopy type uses the actual acyclic matching, not only Euler characteristics or mod-two Betti numbers.

## Relationship to prior work

The publisher's full text of Bode and Harborth (2000), notably its square-board Table 1 on p. 212 and later board sections, records the maximum numbers of nonattacking knights—eight for the four-by-four board and thirteen for the five-by-five board—but does not derive the topology of the complex of **all** placements or the symmetry action on homology. Bode and Harborth (2003) address independence numbers on triangular and hexagonal boards, not these homotopy representations. The standard acyclic-matching framework is due to Forman and is also developed by Kozlov (2005); the discrete-Morse theorem itself is not claimed as new. Topological classifications of ordinary Cartesian grids concern a different adjacency relation from the knight's move. The present exact wedge multiplicities and dihedral-module change are the contribution.

## Limitations

The classification only covers square boards of sizes at most five. The exhaustive proof covers 1,365 and 55,213 faces, respectively; no search or computation on larger boards proves what happens there. Although relevant references were inspected and targeted searches found no covering statement, an equivalent result in unindexed literature cannot be categorically excluded. The resulting homotopy equivalences are not asserted to be equivariant; the rational symmetry representations are established separately by Lefschetz theory.

## References

1. J.-P. Bode and H. Harborth, *Independent Chess Pieces on Euclidean Boards*, Journal of Combinatorial Mathematics and Combinatorial Computing **33** (2000), 209–223. Publisher facsimile: https://combinatorialpress.com/article/jcmcc/Volume%20033/vol-033-paper%2014.pdf.
2. J.-P. Bode and H. Harborth, *Independence for knights on hexagon and triangle boards*, Discrete Mathematics **272** (2003), 27–35. DOI: https://doi.org/10.1016/S0012-365X(03)00181-X.
3. D. N. Kozlov, *Discrete Morse Theory for Free Chain Complexes*, Comptes Rendus Mathématique **340** (2005), 867–872. Preprint: https://arxiv.org/abs/cs/0504090.
4. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145.
