# Integral multipath homology classifies the three regular seven-vertex tournaments

## Finding

For every regular tournament \(T\) on seven vertices, define \(X(T)\) to be the multipath simplicial complex on its directed arcs: a face is a set of arcs forming a vertex-disjoint union of directed simple paths (isolated vertices allowed). All reduced integral homology groups of \(X(T)\) are free abelian and vanish outside degrees \(3,4,5\). Exactly three nonisomorphic regular tournaments exist, and their reduced Betti triples \((\widetilde\beta_3,\widetilde\beta_4,\widetilde\beta_5)\) are, respectively,

\[
(13,43,17),\qquad (12,44,15),\qquad (15,38,24).
\]

Thus the reduced integral homology *distinguishes all three isomorphism classes* of regular tournaments of order seven. These have automorphism-group orders \(7,3,21\), respectively, and correspond to \(720,1680,240\) labeled orientations. The third is the seven-vertex Paley (quadratic-residue) tournament. That individual case has been calculated previously; the two other cases and the exhaustive three-class comparison are the new contribution here.

## Assumptions and scope

A tournament is an orientation of every edge of a complete simple graph, with exactly one arc on each unordered pair. Regularity means each of the seven vertices has outdegree three (and indegree three). The vertex set for a labeled representative is \(\{0,1,2,3,4,5,6\}\). Order the 21 unordered pairs \((i,j)\) lexicographically for \(i<j\). A representative is encoded by an integer \(m\): the bit of position \(k\) is one precisely when the \(k\)-th pair is oriented from the smaller vertex to the larger. The representatives are

\[
m\in\{17976,22066,85298\}.
\]

The corresponding classification is:

| Representative | Labeled orbit | Automorphisms | Nonempty faces | \(\widetilde\beta_3\) | \(\widetilde\beta_4\) | \(\widetilde\beta_5\) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `17976` | 720 | 7 | 2926 | 13 | 43 | 17 |
| `22066` | 1680 | 3 | 2922 | 12 | 44 | 15 |
| `85298` | 240 | 21 | 2940 | 15 | 38 | 24 |

All representatives have precisely \(21,168,630,1113,819\) faces in dimensions \(0,1,2,3,4\), respectively. Their counts of dimension-five faces are \(175,171,189\). The theorem concerns **integral homology**, not a claimed wedge-of-spheres homotopy equivalence, Steenrod operations, or an equivariant refinement.

## Proof

**Exhaustiveness of the isomorphism classes.** The 21 unordered vertex pairs determine a binary orientation choice. The executable enumeration recursively considers both choices, discarding a branch only when some vertex already has more than three outgoing arcs or cannot reach three with the remaining incident pairs. Every regular tournament therefore survives, and every surviving orientation is regular. The enumeration gives exactly \(2640\) labeled regular tournaments. Applying all \(7!=5040\) vertex permutations to each of the three displayed masks produces three pairwise disjoint orbits, of sizes \(720,1680,240\); their union has size \(2640\). Hence the list is exhaustive and each representative has the stated automorphism-group order by orbit-stabilizer.

**The simplicial complexes.** Each face has at most one outgoing and at most one incoming arc at each vertex and contains no directed cycle. Conversely, those conditions make every weak component an isolated vertex or a directed simple path. The checker enumerates all faces first by decisions on the 21 arcs and independently by assigning each vertex at most one outgoing successor, rejecting repeated targets and cycles. The two complete sets of face masks agree: including the empty simplex, they have \(2927,2923,2941\) elements.

**An acyclic matching and its integer Morse chain complex.** On each face poset, consider the ordered arcs and repeatedly pair each still-unmatched face \(\sigma\) with \(\sigma\cup\{e\}\) whenever both occur, sweeping through the arcs in order. Discard the pair containing the augmented empty face, retaining its vertex as the critical zero-cell. No other pair is changed. The resulting pair counts are \(1407,1414,1410\), respectively. Direct construction of every directed edge of the Hasse diagram—orienting matched incidences upward and all other incidences downward—and a complete topological-sort check prove acyclicity. The numbers of checked nonempty Hasse incidences are \(11823,11799,11907\).

There are no critical cells in dimension one. The critical cell counts in dimensions \(2,3,4,5\) are, in representative order,

\[
(1,32,61,17),\qquad (0,23,55,15),\qquad (3,36,56,24).
\]

The Morse boundary is computed over \(\mathbb Z\), using the ordinary alternating simplicial boundary and exact elimination along each matched incidence (its coefficient is \(\pm1\)). The complete critical-face indices and full integer Morse matrices are stored in `morse_certificate.json`, and `verify_regular7.py` independently regenerates and checks them. The Smith nonzero diagonal invariants for \(\partial_3\) and \(\partial_4\) are

\[
\begin{array}{c|c|c|c}
 m & \operatorname{SNF}_{\ne0}(\partial_3)&\operatorname{SNF}_{\ne0}(\partial_4)&\partial_5\\\hline
17976&(1)&(1^{\times18})&0\\
22066&()&(1^{\times11})&0\\
85298&(1^{\times3})&(1^{\times18})&0
\end{array}
\]

All compositions of successive Morse boundaries are zero. In particular, the images of \(\partial_3\) and \(\partial_4\) are primitive direct summands of their target free groups. It follows from the critical dimensions, ranks and integral Smith forms that the reduced integral homology is free, with the three listed rank triples; the critical zero-cell gives connectedness and every other degree vanishes.

**Independent checks.** Direct Gaussian elimination over \(\mathbb F_2\) on the original full simplicial boundary matrices (without the Morse matching) gives rank lists \((1,20,148,482,618,158)\), \((1,20,148,482,619,156)\), and \((1,20,148,482,616,165)\) in source dimensions \(0,1,2,3,4,5\) with an augmented boundary in dimension zero. These reproduce the corresponding mod-two Betti numbers. Independently, enumerating cyclically directed Hamiltonian cycles, each uniquely rooted at vertex zero, gives \(17,15,24\), agreeing with the respective top-dimensional ranks.

## Verification

Use Python 3 with SymPy installed, from a directory containing both standalone artifacts:

```sh
python verify_regular7.py
```

The checker proves exhaustiveness of the three tournament orbits, independently reconstructs each face set, checks the complete matched Hasse graph for acyclicity, reconstructs the integer Morse boundaries and compares every entry with `morse_certificate.json`, determines Smith invariants, independently computes full mod-two simplicial ranks, and checks Hamiltonian-cycle counts. `verification_output.txt` records the exact output of a successful execution. The executable, rather than its output log alone, supplies the finite proof certificate.

## Relationship to prior work

Caputi, Collari, Di Trani and Smith defined multipath complexes and classified several families, notably **transitive** tournaments (their Theorem 5.1); their transitive assumption does not apply to any of the regular seven-vertex representatives here. Their earlier path-poset work gives the underlying simplicial construction but no regular-seven census. The closely related literature on tournament flag complexes and tournaplexes uses simplices indexed by induced tournaments on **vertex subsets**, not by sets of directed arcs satisfying the multipath condition, so those calculations do not imply this theorem. A previous calculation covers the Paley representative alone; the present result adds the other two inequivalent regular orientations and the exhaustive comparison.

## Limitations

Only regular tournaments of order seven are classified; nonregular tournaments and larger orders are not addressed. Integral homology alone does not determine homotopy types or operations on cohomology. All homology and enumeration claims are finitely decidable and replayable from the stated artifacts; the mathematical novelty comparison is limited to the literature and records actually inspected, so equivalent unindexed work is still possible. No independent external audit is asserted.

## References

1. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (first public 2022-08-09), especially Definitions 2.1–2.2, Theorems 3.4 and 5.1 and Remarks 5.8–5.9. https://arxiv.org/abs/2208.04656
2. L. Caputi, C. Collari and S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, arXiv:2110.11206 (2021), especially Sections 1 and 6. https://arxiv.org/abs/2110.11206
3. L. Caputi, C. Collari and S. Di Trani, *Multipath cohomology of directed graphs*, arXiv:2108.02690 (2021). https://arxiv.org/abs/2108.02690
4. *Complexes of tournaments, directionality filtrations and persistent homology*, Journal of Applied and Computational Topology (2021), DOI 10.1007/s41468-021-00068-0 (a different tournament-based complex).
