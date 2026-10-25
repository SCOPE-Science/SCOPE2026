# Multiplicity-free symmetric-group homology of the seven-vertex triangle-free graph complex

## Finding
Let \(T_7\) have one vertex for each of the 21 edges of the seven-vertex complete graph. A set of these vertices forms a face exactly when the corresponding spanning simple graph has no triangle. Permutations of the seven underlying graph vertices induce a simplicial \(\mathfrak S_7\)-action. Its complete rational reduced homology representation is
\[
\begin{aligned}
\widetilde H_5(T_7;\mathbb Q)&\cong S^{(2,1,1,1,1,1)}\oplus S^{(1,1,1,1,1,1,1)},\\
\widetilde H_7(T_7;\mathbb Q)&\cong S^{(4,2,1)}\oplus S^{(4,1,1,1)},\\
\widetilde H_8(T_7;\mathbb Q)&\cong S^{(7)},
\end{aligned}
\]
and it is zero in every other degree. Here \(S^{\lambda}\) is the rational irreducible Specht representation of the partition \(\lambda\vdash7\). The three nonzero dimensions are \(7,55,1\). All irreducible constituents appear with multiplicity one in their degree. The lowest nonzero homology is \(\operatorname{sgn}\otimes\mathbb Q^7\) (sign-twisted point-permutation module); the highest is the trivial representation.

## Assumptions and scope
All graphs are finite, simple, and loopless, with labeled underlying vertex set \(\{0,1,2,3,4,5,6\}\); simplicial chains use increasing edge-index orientation, where complete-graph edges are ordered lexicographically. The field is \(\mathbb Q\). The statement concerns the **rational equivariant homology representation**, not a newly discovered integral Betti table and not a claimed homotopy decomposition. The published integral groups are consistent with \(\widetilde H_5\cong\mathbb Z^7\), \(\widetilde H_6\cong\mathbb Z/2\), \(\widetilde H_7\cong\mathbb Z^{55}\), and \(\widetilde H_8\cong\mathbb Z\), with the other reduced integral groups zero.

## Proof
An exact finite chain algorithm computes the equivariant homology. Encode a graph by a 21-bit mask and retain it if and only if no three-edge triangle mask is contained in it. Exhaustive inspection of all \(2^{21}\) edge masks produces 133,501 faces including the empty face. The face counts by dimensions minus one through eleven are \((1,21,210,1295,5355,15204,29344,37110,28875,12670,2961,420,35)\).

Make an elementary acyclic algebraic-Morse matching by successively toggling the least unused edge index: on the currently unmatched face set, pair every face lacking the edge with its union with that edge when both remain available, then remove both. The supplied exact implementation produces 66,695 pairs. Direct the matched covering incidences upward and all other covering incidences downward. A full topological sort of all 917,280 incidences visits all 133,501 faces, certifying the matching is acyclic. The critical cells occur in degrees five through nine, with counts \((8,22,77,3,1)\).

Over the integers, eliminate each matched unit boundary pivot by the corresponding elementary chain cancellation; the recursive projection of a lower matched face replaces it with the negative, orientation-weighted sum of the other faces of its paired upper face. The resulting Morse boundary matrices in degrees six to nine have ranks \((1,21,1,1)\); the one nonunit Smith factor in the degree-seven differential is 2. Therefore rational homology occurs only in degrees five, seven, and eight, of dimensions \((7,55,1)\). Reverse-order independent matching and integral Smith computations provide a second check on the stated reduced integral groups.

To obtain the *representation*, the accompanying `equivariant_verifier.py` constructs the integral Morse projection and recursive chain inclusion. It checks the chain-map identity on every critical generator and the action-chain-map identity for permutations representing all fifteen conjugacy types of \(\mathfrak S_7\). Signed permutations of oriented simplices descend to the Morse complex via projection-after-action-after-inclusion. Over \(\mathbb Q\), the trace on a chain group is the sum of the traces on its homology and its boundary subspace and on the image of its next differential. Computing traces on exact rational bases therefore yields the character on each surviving homology group. As an independent check, for each conjugacy type the alternating sum of these homology traces matches the signed fixed-face simplicial Lefschetz sum over all 133,501 faces.

The characters, with columns \(\chi_5,\chi_7,\chi_8\), for cycle types in descending order are:

| Cycle type | \(\chi_5\) | \(\chi_7\) | \(\chi_8\) |
| --- | ---: | ---: | ---: |
| \((7)\) | 0 | -1 | 1 |
| \((6,1)\) | -1 | 1 | 1 |
| \((5,2)\) | 0 | 0 | 1 |
| \((5,1,1)\) | 2 | 0 | 1 |
| \((4,3)\) | 0 | -1 | 1 |
| \((4,2,1)\) | 1 | 1 | 1 |
| \((4,1,1,1)\) | -3 | -1 | 1 |
| \((3,3,1)\) | 1 | 1 | 1 |
| \((3,2,2)\) | 0 | 1 | 1 |
| \((3,2,1,1)\) | -2 | -1 | 1 |
| \((3,1,1,1,1)\) | 4 | 1 | 1 |
| \((2,2,2,1)\) | -1 | 1 | 1 |
| \((2,2,1,1,1)\) | 3 | -5 | 1 |
| \((2,1,1,1,1,1)\) | -5 | 5 | 1 |
| \((1,1,1,1,1,1,1)\) | 7 | 55 | 1 |

The exact Murnaghan–Nakayama algorithm reconstructs the irreducible \(\mathfrak S_7\) character table and checks row orthogonality. Inner products of these homology characters with all fifteen irreducible characters yield exactly the constituents displayed in the Finding. The lowest character also equals permutation sign times the number of fixed underlying vertices, a direct independent identity. This completes the equivariant decomposition.

## Verification
Execute `python3 homology_verifier.py`, `python3 equivariant_verifier.py`, and `python3 character_decomposition.py` with Python 3 and SymPy installed, in the same directory as the included scripts. The provided text outputs record completed actual executions. The homology verifier includes explicit Hasse-DAG acyclicity checks, two integral Morse reductions, exact Smith normal forms and a final `VERIFY_OK`. The equivariant verifier independently checks the fifteen class-representative action traces against the 133,501-face Lefschetz sum and checks the chain-map relation. The decomposition verifier checks irreducible-character orthogonality, integrality, multiplicities and dimension totals. Its input is `equivariant_output.txt`, embedded alongside it.

## Relationship to prior work
Jonsson's *Simplicial Complexes of Graphs* (2008), chapter 26, table 26.2, already tabulates **integral homology** for the same graph complex in the dual bounded-covering-number notation \(\operatorname{Cov}_{7,4}\). This finding does not assert originality of those groups or their Alexander-dual consequences. The 2006 bounded-covering-number article treats the broader family and provides the historical context. The new statement determines the full degree-by-degree \(\mathfrak S_7\)-representation, which cannot be recovered from the tabulated nonequivariant Betti groups alone. Known symmetric-group results for other bounded-covering-number parameters or other graph complexes do not imply this particular Specht decomposition.

## Limitations
The accessible extracts of Jonsson's directly relevant book identified the existing homology table, but its **complete chapter text was not accessible**. The possibility of an unindexed equivalent character computation there or elsewhere remains a material originality risk. No integral \(\mathfrak S_7\)-lattice classification, nonequivariant homotopy wedge, or independently audited theorem is claimed. The proof is finite and exhaustive for precisely seven underlying graph vertices; it is not an all-size theorem.

## References
1. Jakob Jonsson, *Simplicial Complexes of Graphs and Hypergraphs with a Bounded Covering Number*, SIAM J. Discrete Math. 19 (2005/2006), DOI: https://doi.org/10.1137/S0895480104443680 (public online record dated 2006-08-01).
2. Jakob Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, 2008, chapter 26, Table 26.2, DOI: https://doi.org/10.1007/978-3-540-75859-4.
3. Robin Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145.
