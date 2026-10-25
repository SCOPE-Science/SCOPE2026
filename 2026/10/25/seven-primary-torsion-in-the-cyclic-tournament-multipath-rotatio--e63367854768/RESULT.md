# Seven-primary torsion in the cyclic-tournament multipath rotation quotient

## Finding
Let \(T\) be the regular cyclic tournament on \(\mathbb Z/7\mathbb Z\): its arcs are \(i\to i+d\) for \(d\in\{1,2,3\}\), with endpoints reduced modulo seven. Let \(X(T)\) be the simplicial multipath complex: its vertices are the twenty-one arcs of \(T\), and its faces are subsets of arcs that form disjoint unions of directed simple paths (isolated underlying graph vertices are permitted). Let \(C_7\) act by translating endpoints of every arc. This action is free on \(|X(T)|\).

The integral reduced homology of \(X(T)\) is
\[
\widetilde H_j(X(T);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{13},&j=3,\\
\mathbb Z^{43},&j=4,\\
\mathbb Z^{17},&j=5,\\
0,&\text{otherwise.}
\end{cases}
\]
The integral homology of the orbit space \(Y=|X(T)|/C_7\) is
\[
H_j(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=0,\\
\mathbb Z/7\mathbb Z,&j=1,\\
\mathbb Z\oplus(\mathbb Z/7\mathbb Z)^2,&j=3,\\
\mathbb Z^7,&j=4,\\
\mathbb Z^5,&j=5,\\
0,&\text{otherwise.}
\end{cases}
\]
In particular the rotation quotient acquires **two independent seven-primary homology classes in degree three**, although the covering complex has torsion-free integral homology.

Write \(W=\mathbb Q(\zeta_7)\) for the six-dimensional rational cyclotomic representation of \(C_7\). The complete positive-degree rational homology representation is
\[
H_3(X(T);\mathbb Q)\cong\mathbf1\oplus W^{\oplus2},\quad
H_4(X(T);\mathbb Q)\cong\mathbf1^{\oplus7}\oplus W^{\oplus6},\quad
H_5(X(T);\mathbb Q)\cong\mathbf1^{\oplus5}\oplus W^{\oplus2}.
\]
All other positive-degree rational homology groups vanish.

## Assumptions and scope
All homology is ordinary simplicial or cellular homology with coefficients explicitly shown; the displayed \(\widetilde H_j\) groups are reduced. The tournament convention is the exact arc rule above, not the quadratic-residue Paley orientation. An oriented face is ordered by arcs in ascending order of initial vertex, then increment \(d\). The quotient is a cellular (or delta-complex) orbit space, not necessarily an abstract simplicial complex with orbit vertices.

No nontrivial translation stabilizes a nonempty face: all arc orbits have seven elements but a multipath has at most six arcs. Therefore the quotient cellular chain groups have one basis generator per orbit of oriented simplices, with boundary coefficients determined by translation and orientation signs.

## Proof
First enumerate all \(2^{21}\) subsets of the tournament arc set. A subset is a multipath precisely when each underlying vertex has at most one selected incoming and one selected outgoing arc and the resulting partial successor function has no directed cycle. This decidable criterion is both necessary and sufficient. It yields the face numbers in dimensions zero through five:
\[
(21,168,630,1113,819,175).
\]
There are no higher-dimensional faces.

For the original complex, greedily pair each still-unpaired face not containing the next arc with the face obtained by adjoining that arc, processing the twenty-one arcs in the fixed order. Include the empty face for the reduced chain computation. Exhaustively orient the Hasse diagram downward on unmatched cover relations and upward on paired relations; a topological sort verifies acyclicity. There are \(1416\) pairs, and the remaining reduced Morse chain groups have ranks \(24,54,17\) in degrees three, four and five, and zero elsewhere. Elimination along the acyclic matching gives Morse boundary \(\partial_5=0\) and a \(24\)-by-\(54\) boundary \(\partial_4\) whose integral Smith factors consist of exactly eleven units. Thus the original reduced homology has free ranks \(24-11=13\), \(54-11=43\), and \(17\), with no torsion. The included program verifies the acyclicity and computes these differentials from gradient-path recursion; independent direct boundary ranks over the fields of seven and 101 elements are \((20,148,482,618,158)\), confirming the free ranks without substituting finite-field ranks for integral Smith factors.

Next take the orbits of all simplices under endpoint translations. The quotient has cellular counts
\[
(3,24,90,159,117,25)
\]
in degrees zero through five. For each orbit choose the lexicographically least arc-bitmask representative. Translate every codimension-one face of a representative to its own chosen representative, multiplying by the permutation sign required to reorder the translated arcs. This is exactly the cellular differential of the free quotient. Its integral Smith factors are, by degree:

| Boundary | Nonzero Smith invariant factors |
| --- | --- |
| \(\partial_1\) | \(1\) repeated \(2\) times |
| \(\partial_2\) | \(1\) repeated \(21\) times; \(7\) once |
| \(\partial_3\) | \(1\) repeated \(68\) times |
| \(\partial_4\) | \(1\) repeated \(88\) times; \(7\) twice |
| \(\partial_5\) | \(1\) repeated \(20\) times |

The exact matrices satisfy \(\partial_{j-1}\partial_j=0\). Their ranks give free homology ranks \((1,0,0,1,7,5)\). For integer matrices forming a chain complex with free chain groups, the torsion of \(H_j\) agrees with the torsion of the cokernel of \(\partial_{j+1}\), because the image of \(\partial_j\) is free. Hence the two displayed seven-factors in \(\partial_4\) give the two degree-three torsion classes; the single seven-factor in \(\partial_2\) gives the degree-one class, and no other torsion occurs.

Finally, for any finite group acting freely cellularly on a finite complex, transfer over \(\mathbb Q\) identifies \(H_j(Y;\mathbb Q)\) with \(H_j(X(T);\mathbb Q)^{C_7}\). Since the only rational irreducibles of \(C_7\) are the trivial representation and the six-dimensional cyclotomic representation, the total Betti ranks and invariant ranks uniquely determine the displayed multiplicities.

## Verification
Run `python check.py` with Python 3.10+ and SymPy 1.14.0 (or a compatible SymPy version). The checker exhaustively enumerates the simplices, validates the Morse matching by testing its full directed Hasse graph for cycles, calculates its exact integer Morse differential, independently checks direct boundary ranks modulo seven and 101, builds the signed cellular quotient boundary, verifies successive differential products vanish, and computes all integral Smith factors. Every asserted group is reconstructed from the outputs. The code requires neither a downloaded dataset nor any unpublished external certificate.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith developed the multipath complex framework and determined several graph families, including a wedge-of-spheres theorem for **transitive** tournaments [1]. That theorem does not address the cyclic regular tournament here, and a nonequivariant wedge description would not determine the integral homology of its rotation quotient. Caputi, Collari and Ramos proved general finite-generation and torsion-boundedness results for multipath homology of bounded-genus quivers and a reduction to matching complexes **when there are no directed cycles** [2]. Neither statement determines the present quotient's two seven-primary degree-three classes. This calculation treats a canonical strongly cyclic tournament and gives both its integral orbit-space homology and complete rational rotation module.

## Limitations
This is an exact result for the seven-vertex regular cyclic tournament, not an all-parameter theorem for cyclic tournaments. No integral \(\mathbb Z[C_7]\)-lattice classification, explicit geometric representatives of the quotient torsion classes, or full homotopy-type classification is claimed. A complete independent audit has not been performed; the certificate is a reproducible exact finite computation. An equivalent result outside the inspected literature remains possible.

## References
[1] L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (first posted 2022-08-09), Mathematika 70 (2024), article e12235. https://arxiv.org/abs/2208.04656

[2] L. Caputi, C. Collari, E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248 (first posted 2024-01-02). https://arxiv.org/abs/2401.01248
