# Pentagonal-antiprism matching homotopy and its dihedral character

## Finding
Let \(A\) be the ten-vertex pentagonal-antiprism graph, equivalently the square of a ten-cycle. The ordinary matching complex \(\mathcal M(A)\) has the **integral homotopy type**
\[
\mathcal M(A)\simeq \bigvee^4 S^2\ \vee\ \bigvee^8 S^3.
\]
For its natural dihedral group \(D_{10}=\langle r,s\mid r^{10}=s^2=1,\ srs=r^{-1}\rangle\), write \(\chi_{\alpha,\beta}\) for the one-dimensional character sending \(r\) to \(\alpha\in\{+1,-1\}\) and \(s\) to \(\beta\in\{+1,-1\}\). Let \(V_j\), for \(j=1,2,3,4\), be the complex two-dimensional dihedral irreducible with rotation eigenvalues \(e^{\pm \pi i j/5}\) and reflection trace zero. After complexification the full nonzero homology representations are
\[
\widetilde H_2(\mathcal M(A);\mathbb C)\cong 2\chi_{+,-}\oplus2\chi_{-,+},
\qquad
\widetilde H_3(\mathcal M(A);\mathbb C)\cong3\chi_{+,+}\oplus\chi_{-,-}\oplus V_2\oplus V_4.
\]
In particular, the integral reduced homology is \(\mathbb Z^4\) in degree two, \(\mathbb Z^8\) in degree three, and zero otherwise. The four-dimensional complex representation \(V_2\oplus V_4\) descends to a rational representation; the individual \(V_j\) need not be rationally defined.

## Assumptions and scope
All graphs are finite, simple and undirected. Explicitly \(V(A)=\mathbb Z/10\mathbb Z\) and
\[
E(A)=\big\{\{i,i+d\}:i\in\mathbb Z/10\mathbb Z,\ d\in\{1,2\}\big\},
\]
with subscripts reduced modulo ten, yielding twenty distinct edges. The complex \(\mathcal M(A)\) consists of all pairwise vertex-disjoint sets of edges, **not** the perfect-matching complex. Let \(r(i)=i+1\) and \(s(i)=-i\). The dihedral action permutes the graph edges and thus simplicial vertices, with the usual signs from sorting oriented simplices. The matching complex is three-dimensional at homology level but has simplices through dimension four. No claim is made about antiprisms of other sizes.

## Proof
Sort the twenty undirected graph edges lexicographically and index them \(0,\ldots,19\). Encode a matching \(\sigma\) by the integer bitmask \(\sum_{j\in\sigma}2^j\). Exhaustively forming all matchings of cardinalities one to five gives the face counts \((20,130,310,225,22)\), plus the augmented empty face, for a total of \(708\). They are exactly the masks satisfying the graph's vertex-disjointness condition.

Apply the sequential matching-tree toggles in the edge-index order
`(1,17,10,14,16,6,0,8,5,13,12,7,2,15,9,3,18,19,4,11)`: for each index, pair every presently unmatched face not containing that edge with its one-edge extension, when both are still unmatched. This gives \(347\) disjoint incident pairs and leaves exactly five unmatched two-simplices, with masks `(16672,16897,16904,20481,32897)`, and nine unmatched three-simplices, with masks `(34840,67720,264324,266276,266372,270624,270864,532768,557584)`. No other augmented faces are unmatched. Direct inspection of the complete directed Hasse graph, reversing the matched face incidences, establishes acyclicity. For an ordinary (unaugmented) Morse CW model, unpair the empty face from its matched singleton; this yields one critical zero-cell and does not create a directed cycle (the empty face becomes a sink). There are no critical one-cells.

Orient each simplex by its ascending edge indices. For an unmatched lower-dimensional face \(\tau\) paired to the upper face \(u\), compute its algebraic Morse projection recursively from the alternating boundary of \(u\): if \(\langle\partial u,\tau\rangle=\epsilon\in\{\pm1\}\), set the projection of \(\tau\) to \(-\epsilon\) times the sum of the projections of the other boundary faces, weighted by their oriented incidence coefficients. Unmatched critical faces project to their basis elements, and paired upper faces project to zero. Acyclicity makes this recursion terminating and exact over \(\mathbb Z\).

In the stated orders of the five two-cells and nine three-cells, the resulting complete integer Morse differential is the \(5\)-by-\(9\) matrix with all entries zero except row zero and row one, each having entries \((+1,-1,+1)\) in columns five, six and seven (zero-based indices). This matrix has rank one and a unit entry. The Morse two-skeleton is a wedge of five two-spheres because it has one zero-cell and no one-cells. By \(\pi_2(\bigvee^5S^2)\cong\mathbb Z^5\), the matrix completely specifies the nine three-cell attaching maps up to homotopy. Unimodular changes of two-cell generators and three-cell attaching-map generators reduce the matrix to a single unit pivot. Thus a two-cell/three-cell pair cancels and the remaining attaching maps are nullhomotopic, producing the asserted wedge of four two-spheres and eight three-spheres. This step proves the homotopy type, not just the Betti numbers.

For the equivariant claim, the rank of \(B_2=\operatorname{im}(\partial_3:C_3\to C_2)\) is \(195\), as computed by exact modular Gaussian elimination in each of characteristics \(101\) and \(103\). For every \(g\in D_{10}\), the signed action on ordered matching simplices gives its traces \(\operatorname{tr}(g\mid C_i)\). Restrict the action to an independent column basis for \(B_2\) and evaluate its trace using a verified left inverse of a \(195\)-by-\(195\) nonsingular coordinate submatrix. The identities
\[
\operatorname{tr}(g\mid\widetilde H_2)=\operatorname{tr}(g\mid C_2)-\operatorname{tr}(g\mid C_1)+\operatorname{tr}(g\mid C_0)-1-\operatorname{tr}(g\mid B_2),
\]
\[
\operatorname{tr}(g\mid\widetilde H_3)=\operatorname{tr}(g\mid C_3)-\operatorname{tr}(g\mid B_2)-\operatorname{tr}(g\mid C_4)
\]
follow from the vanishing of first homology, injectivity of \(\partial_4\), and exact equivariant short sequences of chain groups. (The latter homological facts were established by the integral Morse complex.) Each true rational homology trace is an integer of absolute value at most the corresponding Betti number, eight; hence reduction modulo either prime uniquely determines it. Both primes give identical answers.

The complete character values, displayed as ordered pairs (degree-two trace, degree-three trace), are as follows. For \(g=r^k\), \(k=0,\ldots,9\): `(4,8), (0,1), (4,3), (0,1), (4,3), (0,6), (4,3), (0,1), (4,3), (0,1)`. For \(g=sr^k\) in the same order: `(0,2), (-4,4), (0,2), (-4,4), (0,2), (-4,4), (0,2), (-4,4), (0,2), (-4,4)`. The alternating sum of the two homological traces equals the reduced Lefschetz trace obtained directly from the signed simplex permutations for all twenty elements. Character orthogonality and the standard dihedral character table then give the displayed irreducible decomposition.

## Verification
The standalone `verify.py` included with this result uses only Python 3.10+ and NumPy. Running `python verify.py` reconstructs all 708 augmented faces from the graph, verifies each face pairing and the acyclic oriented Hasse graph, independently computes the complete signed integral Morse differential, performs exact linear algebra modulo \(101\) and \(103\), checks all twenty group elements and the reduced Lefschetz identities, and prints `PASS`. Its exact integral unit entry and explicit acyclic matching certify the claimed homotopy reduction; modular character calculations certify rational traces because of the a priori integral trace bounds. The finite verification is exhaustive for this fixed graph, not an extrapolation to an infinite family.

## Relationship to prior work
The matching-complex theory of Bayer, Jelić Milutinović and Vega proves the contractible-or-sphere-wedge alternative for **outerplanar** graphs and explicitly motivates the analogous question for planar graphs. The pentagonal-antiprism graph is planar and four-regular, hence not outerplanar (an outerplanar graph has a vertex of degree at most two). The published outerplanar theorem therefore does not imply the result. The graph's identification with a squared even cycle is standard; the result concerns the independence complex of its **line graph**, not the independence complex of the squared cycle itself. Existing homotopy computations for Petersen, Desargues and dodecahedral matching complexes apply to different graphs. The computed dihedral module further distinguishes the result from unequivariant sphere-wedge statements.

## Limitations
The theorem treats a single natural ten-vertex graph and its full dihedral action, not every planar graph or every antiprism. The originality conclusion is based on the accessible literature and indexed claims; unindexed equivalent results remain possible. The complete text of a recent three-row grid-matching paper was inaccessible, but its identified domain is different. Independent validation of the new classification has not been performed.

## References
1. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (first posted 7 November 2024), particularly Theorem 2 and Section 3. https://arxiv.org/html/2411.04601v2
2. Chauhan, Sharma and Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366 (posted 23 September 2026); related current computational topology, not a classification of the antiprism. https://arxiv.org/abs/2609.27366
3. E. W. Weisstein, *Antiprism Graph*, MathWorld. https://mathworld.wolfram.com/AntiprismGraph.html
4. Source of the graph-independent Morse cancellation mechanism: R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145. The verification and explicit finite certificate for the present graph are provided here.
