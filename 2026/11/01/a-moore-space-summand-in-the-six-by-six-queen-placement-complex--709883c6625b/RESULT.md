# A Moore-space summand in the six-by-six queen-placement complex

## Finding
Let \(Q_6\) be the graph whose vertices are the thirty-six squares of an ordinary (nonperiodic) \(6\)-by-\(6\) chessboard; squares are adjacent when they lie in one row, column, or diagonal. Let \(K_6=\operatorname{Ind}(Q_6)\), whose faces are placements of mutually nonattacking queens, including the empty placement. There is an integral homotopy equivalence
\[
K_6\simeq M(\mathbb Z/2,2)\vee\bigvee^{19}S^3,
\qquad M(\mathbb Z/2,2)=S^2\cup_{2}e^3.
\]
In particular, \(\widetilde H_2(K_6;\mathbb Z)\cong\mathbb Z/2\mathbb Z\), \(\widetilde H_3(K_6;\mathbb Z)\cong\mathbb Z^{19}\), and all other reduced integral homology is zero. Among ordinary square chessboards of side at most six, this is the first whose nonattacking-queen complex has integral homology torsion. Under the standard order-eight dihedral symmetry group of the square, the rational third-homology character is
\[
\bigl(19,-5,7,-5,1,1,-5,-5\bigr),
\]
listed for identity, quarter-turn, half-turn, inverse quarter-turn, horizontal reflection, vertical reflection, main-diagonal reflection, and anti-diagonal reflection. In particular its invariant rational subspace has dimension one.

## Assumptions and scope
All squares are indexed by \(6i+j\), for \(0\leq i,j<6\). Two distinct squares \((i,j)\), \((k,l)\) attack one another exactly when \(i=k\), or \(j=l\), or \(|i-k|=|j-l|\). No wraparound or toroidal identification is used. All homotopy and integral homology assertions concern the geometric realization of this finite abstract simplicial complex. The theorem does not assert analogous behavior for all larger boards.

## Proof
Exhaustive construction by extending nonattacking placements, independently cross-checked by selecting row subsets and injecting columns, gives the complete face-number vector by cardinality
\[
(f_{-1},f_0,f_1,f_2,f_3,f_4,f_5)=(1,36,340,1024,982,248,4).
\]
An explicit algebraic discrete-Morse matching is defined without search or choices other than fixed row-major order: begin with all faces unmatched; for \(v=0,1,\ldots,35\), pair every then-unmatched face \(A\) not containing \(v\) with \(A\cup\{v\}\), whenever both are then unmatched and the union is a face. These pairs are disjoint. The associated directed Hasse graph is obtained by orienting each matched incidence upward and every other incidence downward. The standalone verifier constructs all its \(2,635\) faces and \(8,980\) directed incidences and gives a topological ordering of the whole graph, thereby verifying acyclicity without relying on a numerical Morse inequality. There are \(1,274\) pairs and \(87\) unmatched faces, respectively \(34\) in dimension two and \(53\) in dimension three. The empty face belongs to a matching with a vertex. Hence the nonaugmented complex has a CW Morse model with one zero-cell, \(34\) two-cells, \(53\) three-cells, and no other cells.

Fix the increasing-vertex simplicial orientations. Calculate the integral cellular Morse boundary from the surviving three-cells to the surviving two-cells by recursively eliminating paired incidence coefficients: if a lower face \(A\) is paired with the higher face \(B\), project the signed boundary of \(B\) to surviving lower faces, solving for the coefficient of \(A\); for a surviving lower face, projection is its coordinate unit vector. The resulting \(34\)-by-\(53\) integer matrix has \(241\) nonzero entries, each of absolute value at most two. Repeatedly pivot on an entry \(\pm1\), using only unimodular integer row and column operations; the supplied deterministic elimination performs \(33\) such pivots. The remaining one-by-twenty row has four nonzero entries, all equal to \(\pm2\); its gcd is two. The Smith factors are therefore \(33\) units and one factor two, with rank \(34\) and free kernel rank \(19\). This proves the asserted integral homology groups.

For the stronger homotopy statement, observe that the Morse CW model is simply connected and has no cells above dimension three. Its two-skeleton is a wedge of \(34\) two-spheres, and its three-cell attaching maps lie in \(\pi_2(\bigvee^{34}S^2)\cong\mathbb Z^{34}\). The integral boundary matrix thus classifies those attaching maps. Unimodular basis changes are realized by homotopy self-equivalences of the two-skeleton and by three-cell slides. Putting the boundary into Smith form leaves one degree-two attachment, \(33\) canceling degree-one attachments, and \(19\) null attachments. This yields exactly the displayed Moore-space and sphere wedge.

For dihedral symmetry, count fixed faces with their orientation permutation signs. The reduced simplicial Lefschetz values are \((-19,5,-7,5,-1,-1,5,5)\) in the stated group-element order. Since the only nonzero rational reduced homology occurs in dimension three, the homology character is their negative. Averaging its eight values gives invariant dimension one. Direct integral discrete-Morse models for the smaller square boards (sizes one through five) have torsion-free homology; for size five the surviving two-to-one Morse boundary is zero. Thus side six is the first torsion occurrence within this natural sequence.

## Verification
The accompanying `verify.py` uses only the Python standard library and independently rebuilds both face enumerations, all matching incidences, the complete acyclicity test, signed integral Morse boundaries, unimodular integer reduction and all eight signed Lefschetz values. It additionally computes ranks of the original unreduced simplicial boundaries modulo \(2\), \(3\), and \(5\). The reduced Betti ranks in dimensions two and three are respectively \((1,20)\) over \(\mathbb F_2\) and \((0,19)\) over either \(\mathbb F_3\) or \(\mathbb F_5\), corroborating the computed two-torsion. Running `python3 verify.py` terminates with `VERIFY_OK`; `VERIFY_OUTPUT.txt` is a recorded successful run. All data and operations required for the certificate are implemented in the included source rather than relying on archived program paths or logs.

## Relationship to prior work
Chaiken, Hanusa and Zaslavsky's papers on the \(q\)-queens problem develop the geometry and enumeration of nonattacking configurations on square boards, not this integral simplicial homotopy classification. Standard literature on independence complexes motivates taking all compatible queen placements as faces; none of the inspected sources determines the above Moore summand or full dihedral character. The five-by-five nonattacking queen complex has a previously recorded torsion-free wedge homotopy type, which does not imply the next board's torsion. An existing classification or equivalent calculation not encountered by the searches would limit originality.

## Limitations
The result concerns exactly ordinary boards of side six and the verified smaller-size torsion threshold. It does not classify all queen-placement complexes or their symmetry modules in other dimensions. The proof is a complete finite discrete-Morse and integer-chain computation, not a claim about unrestricted chessboard size. No external independent mathematical audit has been performed.

## References
1. S. Chaiken, C. R. H. Hanusa and T. Zaslavsky, *A q-Queens Problem. I. General Theory*, arXiv:1303.1879 (initial public posting 2013-03-08), https://arxiv.org/abs/1303.1879.
2. S. Chaiken, C. R. H. Hanusa and T. Zaslavsky, *A q-Queens Problem. II. The Square Board*, arXiv:1402.4880 (initial public posting 2014-02-20), https://arxiv.org/abs/1402.4880.
3. R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145. Used solely as standard discrete-Morse background.
