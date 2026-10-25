# The first noncontractible square knight-placement complex and its dihedral homology

## Finding

Let \(N_n\) be the ordinary, nonperiodic knight-attack graph on an \(n\)-by-\(n\) chessboard, and let \(K_n=\operatorname{Ind}(N_n)\) consist of all mutually nonattacking knight placements. For every \(1\le n\le3\), \(K_n\) is contractible, whereas

\[
K_4\simeq\bigvee^{5} S^3.
\]

Moreover, write \(D_4=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle\), where on zero-based board coordinates \(r(a,b)=(b,3-a)\) and \(s(a,b)=(a,3-b)\). Let \(\eta\) be the one-dimensional rational character with \(\eta(r)=-1\), \(\eta(s)=1\), and let \(\rho\) be the ordinary two-dimensional rational geometric representation of the square. Then

\[
\widetilde H_3(K_4;\mathbb Q)\cong\mathbf1\oplus2\eta\oplus\rho
\qquad\text{as }\mathbb Q[D_4]\text{-modules}.
\]

Equivalently, the character at \(1,r,r^2,r^3,s,rs,r^2s,r^3s\) is \((5,-1,1,-1,3,-1,3,-1)\). All other reduced integral homology groups vanish, and \(\widetilde H_3(K_4;\mathbb Z)\cong\mathbb Z^5\). The \(D_4\)-invariant rational third homology is one-dimensional.

## Assumptions and scope

Vertices are \((a,b)\in\{0,1,2,3\}^2\) for \(N_4\); distinct vertices are joined exactly when \(\{|a-c|,|b-d|\}=\{1,2\}\). There is **no wraparound**. Nonempty simplices of \(K_4\) are bitmasks \(m\in\{1,\ldots,65535\}\), with bit index \(4a+b\). More generally \(N_n\) uses the same knight rule on \(\{0,\ldots,n-1\}^2\). Homotopy equivalence is nonequivariant; the stated homology representation is rational. The exact integral representation lattice and boards \(n>4\) are not classified here.

## Proof

For \(n=1,2\) the knight graph has no edges, so its independence complex is a simplex. For \(n=3\), the central board square is isolated in the knight graph; its independence complex is a cone. Thus all smaller square boards are contractible.

For \(n=4\), enumerate independent subsets recursively: a nonzero mask \(m\), whose least set bit is \(2^i\), is independent precisely when \(m-2^i\) is independent and no vertex in \(m-2^i\) is adjacent to \(i\). The resulting f-vector, in simplex dimensions zero through seven, is

\[
(16,96,276,412,340,170,48,6).
\]

Define an explicit matching on the face poset of **nonempty** simplices. Use the following vertex order, indexed from zero in row-major order:

`[13,9,0,8,7,4,15,2,11,3,1,10,6,5,12,14]`.

For each pivot \(i\) in turn, and for each as-yet-unmatched nonempty face \(\sigma\) not containing \(i\), pair \(\sigma\) with \(\sigma\cup\{i\}\) whenever both are unmatched. Remove both from further consideration. This specifies 679 distinct cover pairs. Exactly six faces are unmatched, with bitmasks

`[8192,51,102,1248,17476,19457]`.

The first is a vertex and the other five are three-simplices. A complete directed-acyclicity certificate is provided in `verify_knight4.py`: form every one of the 5,772 cover relations between **nonempty** simplices, direct unmatched relations downwards, reverse every matched relation, and topologically sort the resulting directed graph. All 1,364 nodes are removed, so it is acyclic. These are finite integer and Boolean computations on an explicitly defined complex, not sampling. By the acyclic-matching theorem of discrete Morse theory, \(K_4\) is homotopy equivalent to a CW complex with one zero-cell and five three-cells, and no cells in other positive degrees. All attaching maps necessarily go to the point, giving the asserted wedge of five three-spheres. In particular integral homology is free, with the stated rank.

The natural square rotations and reflections preserve knight adjacency, hence act simplicially. For every symmetry \(g\), let \(\epsilon_\sigma(g)\in\{1,-1\}\) be the sign of its induced permutation of the vertices of a setwise fixed nonempty simplex \(\sigma\). Its simplicial Lefschetz number is

\[
L(g)=\sum_{\substack{\emptyset\ne\sigma\in K_4\\g\sigma=\sigma}}
(-1)^{\dim\sigma}\epsilon_\sigma(g).
\]

The complete fixed-simplex enumeration gives

\[
\big(L(1),L(r),L(r^2),L(r^3),L(s),L(rs),L(r^2s),L(r^3s)\big)
=(-4,2,0,2,-2,2,-2,2).
\]

As the only nonzero unreduced rational homology is \(H_0\cong\mathbb Q\) and \(H_3\cong\mathbb Q^5\), the Lefschetz formula is \(L(g)=1-\operatorname{tr}(g\mid H_3)\), yielding the character in the finding. The proposed rational decomposition has the same character: \(\mathbf1\) contributes one everywhere, \(2\eta\) contributes \(2(-1)^j\) on \(r^js^e\), while \(\rho\) contributes \(2,0,-2,0\) on rotations \(r^0,r^1,r^2,r^3\) and zero on reflections. Rational representations of finite groups are semisimple, and equality of characters gives the module isomorphism. Averaging the character over all eight elements gives invariant dimension one.

## Verification

Run `python3 verify_knight4.py` from the directory containing that file, with Python 3.9 or later and no third-party dependencies. The program recomputes the 24 knight edges, all 1,364 nonempty independent simplices, the 679 matching pairs, the six critical cells, all 5,772 oriented cover incidences, and an explicit topological ordering of the directed matching graph. It separately computes all simplicial boundary ranks over \(\mathbb F_2\) and independently enumerates signed fixed-face Lefschetz sums for each of the eight square symmetries. Its actual output is included as `verification_output.txt`.

The \(\mathbb F_2\) check yields reduced Betti ranks \((0,0,0,5,0,0,0,0)\), but the integral homotopy conclusion depends on the complete acyclic Morse matching, **not** on field ranks. The listed exact finite certificate and mathematical Morse theorem establish the result; no extrapolation to larger board sizes occurs.

## Relationship to prior work

Bousquet-Mélou, Linusson and Nevo [1] use acyclic Morse matchings to determine homotopy types for ordinary square-lattice independent-set complexes, where edges join nearest neighbors of the lattice; their explicitly treated graphs do not have the knight-move adjacency. Cibu, Ding, DiSilvio, Kononova, Lee, Morrison and Singal [2] consider the **same** nonperiodic knight-attack graphs and their toroidal versions, but Sections 7–8 and Appendix B analyze graph gonality, not independence-complex homotopy or a dihedral homology character. The classical independence-complex framework [1,3] motivates the computation but does not imply its numerical homotopy or equivariant conclusions.

The toroidal four-by-four knight graph is graph-theoretically different: its periodic knight adjacency has 32 edges and is a four-cube, whereas the ordinary knight graph here has 24 edges. Previously available sphere-wedge results for the four-cube therefore do not imply the five-sphere result or its \(D_4\)-character. General independent-set counts and maximum-knight placements likewise do not determine the integral homotopy type or the symmetry character.

## Limitations

This is a finite exact classification at the first noncontractible **square** board, not an asymptotic or all-board theorem. It does not classify rectangular boards, integral equivariant splitting, or nonlinear action on homotopy groups. The matching is not claimed to be equivariant; the equivariant conclusion follows independently from signed Lefschetz counts. A targeted literature and research-record comparison revealed no implication of the exact result, but exhaustive bibliographic uniqueness is not asserted. A separate independent mathematical audit has not been carried out.

## References

1. M. Bousquet-Mélou, S. Linusson and E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890, first submitted 2007-01-30. https://arxiv.org/abs/math/0701890
2. N. Cibu, K. Ding, S. DiSilvio, S. Kononova, C. Lee, R. Morrison and K. Singal, *The Gonality of Chess Graphs*, arXiv:2403.03907v1, first submitted 2024-03-06. https://arxiv.org/html/2403.03907v1
3. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics **27** (2006), 906–923. https://doi.org/10.1016/j.ejc.2005.04.010
