# An absolutely irreducible 39-dimensional projective collineation action on a noncover complex

## Finding
Let \(\Pi=\mathrm{PG}(2,3)\) have its thirteen points and thirteen projective lines. Let \(K\) be the noncover complex on the point set, in which a subset is a face exactly when it is disjoint from at least one projective line. The natural projective collineation group \(G=\mathrm{PGL}_3(\mathbb F_3)\), of order \(5616\), acts simplicially on \(K\).

The \(39\)-dimensional rational representation \(\widetilde H_4(K;\mathbb Q)\) is **absolutely irreducible** under the entire group \(G\), and \(\widetilde H_5(K;\mathbb Q)\cong\mathbb Q\) is the trivial one-dimensional representation. There is no other reduced rational homology. In particular, no nonzero fourth-homology class is fixed by all projective collineations, although fifth homology contains a fixed generator.

Its complete fourth-homology character depends only on the permutation cycle type of the action on the thirteen points. The following table lists all types occurring in the group; counts sum to \(5616\).

| Cycle type on 13 points | Number of group elements | Fourth-homology trace |
|---|---:|---:|
| \(1^{13}\) | 1 | 39 |
| \(2^4 1^5\) | 117 | -1 |
| \(3^3 1^4\) | 104 | 3 |
| \(3^4 1\) | 624 | 0 |
| \(4^2 2^2 1\) | 702 | -1 |
| \(6\,3\,2\,1^2\) | 936 | -1 |
| \(8\,4\,1\) | 1404 | 1 |
| \(13\) | 1728 | 0 |

## Assumptions and scope
Projective points are nonzero triples over \(\mathbb F_3\) modulo nonzero scalar multiplication. Projective lines are kernels of nonzero covectors modulo scalar multiplication. A simplex is any nonempty set of points omitting all points of at least one line; the empty face is included formally. The topological realization is of the nonempty simplices. The result concerns ordinary reduced rational simplicial homology, not an equivariant homotopy decomposition or an integral representation-lattice classification. The known nonequivariant integral homotopy type is \(K\simeq\bigvee^{39} S^4\vee S^5\); the representation-theoretic refinement is the finding here.

## Proof
First, exhaustive generation of the lines by the dot-product kernel and of all their point-set complements gives \(3862\) faces counting the empty face, with face counts by cardinality \((1,13,78,286,702,1170,1014,468,117,13)\). A greedy vertex-toggle matching applied to the faces in fixed point order produces exactly \(1910\) matched pairs and critical-cell vector \((c_0,c_4,c_5)=(1,39,1)\), with no other critical cells. Orient unmatched Hasse incidences down and matched incidences up; exhaustive topological sorting verifies the resulting directed graph is acyclic on all \(3861\) nonempty faces and all \(20085\) cover incidences. Integral algebraic Morse reduction along this explicit matching gives zero for each of the \(39\) boundary coefficients from the unique critical five-cell to the critical four-cells. Thus \(\widetilde H_4(K;\mathbb Z)\cong\mathbb Z^{39}\) and \(\widetilde H_5(K;\mathbb Z)\cong\mathbb Z\), with all other reduced homology zero. These computations are independently reproducible by `noncover_morse_check.py`.

Every projective collineation acts on faces. For a permutation \(g\) of the thirteen points, a face is setwise invariant precisely when it is a union of cycles of \(g\). Such a simplex on \(k\) vertices, comprising \(r\) cycles, contributes \((-1)^{k-1}(-1)^{k-r}\) to its simplicial Lefschetz trace. Adding the reduced augmentation term \(-1\) gives the reduced Lefschetz number \(\widetilde L(g)\). Since the only positive reduced homology degrees are four and five, \(\widetilde L(g)=\chi_4(g)-\chi_5(g)\).

Every projective class over \(\mathbb F_3\) has a unique determinant-one representative: a scalar multiplication changes a three-by-three determinant by that scalar, and the only nontrivial scalar is \(-1\). Hence \(G\cong\mathrm{SL}_3(\mathbb F_3)\). This group is perfect: every elementary generator \(E_{ij}(a)\) is a commutator \([E_{ik}(a),E_{kj}(1)]\) for three distinct indices, and elementary matrices generate the special linear group. Consequently its only rational one-dimensional character is trivial, so \(\chi_5(g)=1\) for every \(g\) and \(\chi_4(g)=\widetilde L(g)+1\).

Enumerate all \(3^9\) matrices over \(\mathbb F_3\), keep exactly one normalized representative of each invertible projective class, and compute each permutation of the thirteen points. This yields \(5616\) distinct elements. Exact signed fixed-face enumeration yields the eight rows of the character table. Direct integer summation gives
\[
\sum_{g\in G}\chi_4(g)=0,\qquad
\sum_{g\in G}\chi_4(g)^2=5616=|G|.
\]
Therefore \(\langle\chi_4,\chi_4\rangle_G=1\). Orthogonality of complex irreducible characters implies the complexification of \(\widetilde H_4(K;\mathbb Q)\) is irreducible; hence this rational representation is absolutely irreducible. The first sum also proves the fourth-homology invariant space has dimension zero. The full independent enumeration and character checks are contained in `noncover_character_check.py`.

## Verification
Run `python noncover_morse_check.py 3` followed by `python noncover_character_check.py` with ordinary Python 3. Both scripts use only the standard library, enumerate their respective finite universes exhaustively, and independently reconstruct projective points and faces. The Morse program checks all \(20085\) nonempty Hasse incidences, every acyclicity condition, and all integral coefficients in the remaining boundary. The character program checks group size, projective permutation uniqueness, the complete cycle-type character table, the character sum, and the character self-inner product. Representative output is recorded in `verification_output.txt`.

## Relationship to prior work
The noncover-complex framework and conventions appear in Kim and Kim, *Domination numbers and noncover complexes of hypergraphs* (arXiv:2101.01850v1; first public January 6, 2021). A previously published classification of the open-neighborhood complex of the ternary projective **nonincidence** graph gives, on each of its two components, the same nonequivariant homotopy type \(\bigvee^{39}S^4\vee S^5\): one such component is exactly \(K\), because the open neighborhood of a line-vertex consists of the points outside that line. That earlier rank and homotopy statement is not claimed to be new. The present assertion concerns the previously unstated complete \(5616\)-element collineation character and its absolute irreducibility, which are not logical consequences of nonequivariant homotopy classification.

## Limitations
No equivariant homotopy equivalence or integral \(\mathbb Z[G]\)-lattice classification is asserted. Absolute irreducibility follows from a finite exact character calculation, not a universal projective-plane theorem. The closest same-object published result was available as an indexed abstract rather than inspectable full text, and equivalent unpublished or unindexed equivariant calculations are a residual originality risk. Independent mathematical review has not been performed.

## References
1. J. Kim and M. Kim, *Domination numbers and noncover complexes of hypergraphs*, arXiv:2101.01850v1 (2021), publicly posted 2021-01-06.
2. *Mixed-dimensional neighborhood-complex homotopy of the ternary projective nonincidence graph*, publicly indexed mathematical research finding (2026); the same-object nonequivariant benchmark.
3. I. Novik, *Lyubeznik's Resolution and Rooted Complexes* (2002), section on the Fano matroid cocircuit ideal; a related but different matroidal cellular-resolution construction.
