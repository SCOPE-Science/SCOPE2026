# Review of the Paley-19 out-neighborhood homotopy calculation

## Correctness — PASS
The orientation is the precise quadratic-residue orientation modulo \(19\). The standard-library verifier exhaustively enumerates every simplicial face and all matching incidences. A complete topological-sort check verifies acyclicity; the integral algebraic Morse boundary has a certified columnwise row relation, a rank-three unimodular minor, and no possible torsion in the cokernel. Thus the reduced integral homology is \(\mathbb Z\) in degree \(2\) and \(\mathbb Z^{78}\) in degree \(3\), zero otherwise. Because the Morse CW model has one vertex, no edges and only two- and three-cells, Smith reduction of the attaching degrees gives the asserted wedge homotopy equivalence. A reversed-priority acyclic matching independently reproduces both rational ranks.

## Originality — PASS on inspected evidence
The closest same-target published record computes the **directed flag complex** of the nineteen-vertex Paley tournament, whose faces are transitive subtournaments, not out-neighborhood faces. An explicit directed three-cycle \(\{1,4,6\}\) witnesses the distinction. Dochtermann--Singh, arXiv:2108.10948, develop directed neighborhood/Hom complexes and give a five-vertex table and general bounds but no nineteen-vertex Paley evaluation. Govc, arXiv:2006.05333, treats directed flag complexes, not neighborhood complexes. Searches against the indexed public result collection and primary-literature discovery did not find a theorem implying the current statement. Unindexed or differently named equivalent work remains possible.

## Value — PASS
The directed out-neighborhood construction is a natural topological invariant of tournaments, equivalently realized by a directed-edge Hom complex. Order nineteen is the first larger prime in this Paley-tournament sequence after the separately studied eleven-vertex case, and the mixed-dimensional integral wedge \(S^2\vee\bigvee^{78}S^3\) supplies a concrete complete homotopy classification where general vanishing bounds give little information. The two nonzero dimensions and their exact wedge multiplicities are motivated by this canonical same-object homotopy problem, not by an arbitrary parameter slice. No equivariant, universal, or independent-validation claim is made.

## Limitations
The finite exhaustive certificate is self-contained but has not been independently audited. It does not establish a classification of Paley tournaments in general, and the originality assessment cannot exclude inaccessible or unindexed equivalent sources.

Self-review: passed. Independent audit: not yet performed.
