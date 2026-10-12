# Five minimal three-node circuits in Wuebben's mirror node subsystem
## Finding
Consider the mirror \(X^{\circ}\) in Wuebben's unique \(\mathbb F_1\) Batyrev mirror pair. Its node subsystem consists of \(26\) ordinary double points, one for each unit-square face of the \(26\)-vertex polar polytope. For each square
\[
S=(q_a,q_b,q_c,q_d)
\]
in cyclic order, Wuebben associates the diagonal-relation row
\[
\rho_S=e_a-e_b+e_c-e_d.
\]

Order the \(26\) square faces lexicographically by their one-based polar-vertex index sets. Then the row matroid of
\[
\{\rho_S:S\text{ a unit-square face}\}
\]
has girth \(3\), and it has exactly five circuits of that minimum size. In row indices they are
\[
\boxed{
\{7,8,22\},\quad
\{12,14,20\},\quad
\{13,14,23\},\quad
\{17,18,25\},\quad
\{19,20,26\}.
}
\]
Equivalently, the five triples of square faces are
\[
\begin{aligned}
&\{(3,5,13,16),(3,5,23,25),(13,16,23,25)\},\\
&\{(5,6,11,12),(5,6,25,26),(11,12,25,26)\},\\
&\{(5,6,15,16),(5,6,25,26),(15,16,25,26)\},\\
&\{(10,12,18,20),(10,12,24,26),(18,20,24,26)\},\\
&\{(11,12,19,20),(11,12,25,26),(19,20,25,26)\}.
\end{aligned}
\]
Here each tuple records one-based polar-vertex indices.

There is no dependent pair of node rows. Each displayed triple has a primitive dependence with coefficients in \(\{\pm1\}\); after an overall sign choice the five coefficient triples are
\[
(1,-1,1),\quad
(1,-1,1),\quad
(1,-1,-1),\quad
(1,-1,1),\quad
(1,-1,1).
\]
Thus the smallest nontrivial dependencies among the \(26\) node rows involve exactly three nodes, and there are precisely five such minimum-support dependencies.

## Assumptions and scope
Work over \(\mathbf Q\) with the explicit \(22\)-vertex reflexive polytope \(\Delta_{\mathbb F_1}\) printed in Wuebben's Theorem 6.1 and its polar \(\Delta_{\mathbb F_1}^{\circ}\).

The initiating paper proves that the mirror \(X^{\circ}\) has \(26\) ordinary double points, two \(\mathrm{dP}_7\)-cone points and two \(\mathrm{dP}_6\)-cone points. Its Remark 6.3 defines the \(26\) diagonal-relation rows, computes their rank \(18\), and identifies exactly two coloop rows. The present finding concerns the matroid of those same \(26\) node rows.

A circuit means an inclusion-minimal linearly dependent subset of the rows over \(\mathbf Q\). The matroid girth is the cardinality of a smallest circuit.

No claim is made that a minimum-support node relation by itself gives a smoothing of \(X^{\circ}\). The four additional del Pezzo-cone singularities participate in the mixed local-to-global obstruction problem.

## Proof
The proof is a complete exact computation on the printed polytope.

Starting with the \(22\) vertices of \(\Delta_{\mathbb F_1}\), enumerate every supporting hyperplane through four affinely independent vertices. Primitive integral normals recover exactly \(26\) facets, all at lattice distance \(1\). Negating their primitive normals gives the \(26\) vertices of \(\Delta_{\mathbb F_1}^{\circ}\).

Enumerating intersections of pairs of polar facets and retaining the two-dimensional intersections gives \(68\) two-faces, of which exactly \(26\) have four vertices. This reproduces Wuebben's count of the \(26\) unit-square faces.

For each square, inspect its three pairings of opposite vertex pairs. Exactly one pairing has equal endpoint sum, hence gives a parallelogram relation. Assign coefficients \(+1,+1,-1,-1\) to the two diagonals, producing a row in \(\mathbf Z^{26}\). Exact Gaussian elimination over \(\mathbf Q\) gives
\[
\operatorname{rank}\{\rho_S\}=18,
\]
reproducing the initiating source. Deleting rows \(9\) and \(11\) lowers the rank to \(17\), deleting both lowers it to \(16\), and deleting any other single row leaves rank \(18\); this also reproduces the two-coloop check.

To determine the matroid girth and every minimum circuit, exhaust all supports of cardinalities \(1\), \(2\), and \(3\). Every row is nonzero, and every pair has rank \(2\). Among the
\[
\binom{26}{3}=2600
\]
three-row subsets, exactly five have rank \(2\); they are the five supports displayed above. Because no support of smaller cardinality is dependent, every one of the five is a circuit and the girth is \(3\).

Finally, direct integer addition of the rows verifies the five displayed primitive coefficient triples. Therefore the list is complete.

## Verification
The bundled `verify.py` reconstructs the polar polytope and all \(26\) square relations from the \(22\) vertices printed in Theorem 6.1 using only exact integer arithmetic and rational Gaussian elimination.

It independently checks:
\[
\#\operatorname{Vert}(\Delta_{\mathbb F_1}^{\circ})=26,\qquad
\#\{\text{square faces}\}=26,\qquad
\operatorname{rank}=18,
\]
the two published coloop rows, the absence of dependent pairs, the complete enumeration of all \(2600\) triples, the five circuit supports, the corresponding square-face triples, and the five primitive signed relations.

The saved replay output ends in `VERIFY_OK`. Finite enumeration is exhaustive here because the claim is explicitly about the finite \(26\)-row matroid; no finite experiment is being used to infer an infinite statement.

## Relationship to prior work
Wuebben's initiating paper states the rank \(18\) calculation and the existence of exactly two coloops, using these facts to show that no dependence can have all \(26\) coefficients nonzero. Its ancillary `src/paper3_node_relations.py` reconstructs that rank and the two coloop faces exactly. Neither the paper nor that ancillary script enumerates the minimum-support circuits or states the matroid girth.

A later public manuscript in the same project, *Mirror Symmetry for Conifold Relations in Calabi--Yau Threefolds*, develops the integral relation lattice controlling exceptional curves and mirror vanishing spheres for a specified class of toric Calabi--Yau degenerations, and gives explicit generating relations in several examples. Inspection of its statements and examples found no computation of the five minimum circuits of this \(26\)-row subsystem.

Targeted searches for this source, the \(26\)-node relation matrix, minimum-support relations, three-node circuits, and equivalent matroid language did not locate the five-circuit classification.

## Limitations
This is a finite structural invariant of Wuebben's node subsystem. It does not classify all circuits of the \(26\)-row matroid, only those of minimum cardinality.

The two coloop rows still vanish in every node relation, so none of the five circuits repairs the full-support obstruction established by Wuebben.

Most importantly, \(X^{\circ}\) has four additional del Pezzo-cone singularities. The five three-node circuits do not by themselves prove the existence of partial or global smoothings of the mixed-singularity threefold.

## References
1. B. J. Wuebben, *Doubly isolated Batyrev mirror pairs and non-smoothable Calabi--Yau threefolds*, arXiv:2610.03753v1, first public 2026-09-26; especially Theorem 6.1 and Remarks 6.2--6.3.
2. The ancillary file `src/paper3_node_relations.py` distributed with arXiv:2610.03753v1, which reconstructs the \(26\) node rows, their rank, and the two coloops.
3. B. J. Wuebben, *Mirror Symmetry for Conifold Relations in Calabi--Yau Threefolds*, public manuscript dated 2026-09-29 in the associated research repository; especially the definition of the integral relation lattice and the examples section.
