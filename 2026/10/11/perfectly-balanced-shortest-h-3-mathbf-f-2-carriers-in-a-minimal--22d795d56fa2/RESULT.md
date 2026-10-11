# Perfectly balanced shortest \(H_3(\mathbf F_2)\)-carriers in a minimal thirteen-vertex \(S^3\times S^3\)
## Finding
Let \(K=(S^3\times S^3)^a_{13}\) be Lutz's thirteen-vertex triangulation of \(S^3\times S^3\). The published complex is four-neighborly, has face vector
\[
(13,78,286,715,1014,728,208),
\]
and is asymmetric.

Over \(\mathbf F_2\),
\[
H_3(K;\mathbf F_2)\cong\mathbf F_2^2.
\]
The minimum vertex support of a nonzero class is \(5\). Exactly \(273\) five-vertex supports attain this minimum: the five-sets that are not four-simplices.

Define
\[
\alpha=[\partial\{1,2,3,5,7\}],\qquad
\beta=[\partial\{1,2,3,5,8\}].
\]
These are distinct nonzero classes and hence form a basis of \(H_3(K;\mathbf F_2)\). The \(273\) minimum carriers split perfectly evenly:
\[
91\text{ represent }\alpha,\qquad
91\text{ represent }\beta,\qquad
91\text{ represent }\alpha+\beta.
\]
In particular,
\[
[\partial\{1,2,3,7,8\}]=\alpha+\beta.
\]

The family of minimum supports is also vertex-regular: every one of the thirteen vertices lies in exactly \(105\) of the \(273\) missing five-sets.

## Assumptions and scope
A missing four-simplex is a five-vertex set whose five tetrahedral facets are all present but which is not itself a four-simplex. Four-neighborliness of \(K\) means every four-vertex set is a tetrahedron, so every five-set carries the complete boundary of a four-simplex.

Support size means the number of vertices appearing in a simplicial cycle. Homology is taken over \(\mathbf F_2\), so orientations and signs are irrelevant. The statement concerns the labelled triangulation \((S^3\times S^3)^a_{13}\), not the other known thirteen-vertex triangulations of the same manifold.

## Proof
The exact \(208\)-facet presentation reconstructs
\[
f(K)=(13,78,286,715,1014,728,208).
\]
Since
\[
715=\binom{13}{4},
\]
every four-set is a tetrahedron. No nonzero simplicial \(3\)-cycle can be supported on fewer than five vertices: on four vertices there is only one possible \(3\)-simplex, whose boundary is nonzero.

There are
\[
\binom{13}{5}=1287
\]
five-vertex sets and \(1014\) four-simplices. Hence there are exactly
\[
1287-1014=273
\]
missing four-simplices. The boundary of each such five-set is a simplicial \(3\)-cycle on five vertices. If the five-set is an actual four-simplex, the same boundary is a boundary in \(K\) and is homologically zero.

For the global homology calculation, exact mod-two elimination gives
\[
\operatorname{rank}\partial_3=220,\qquad
\operatorname{rank}\partial_4=493.
\]
Therefore
\[
\dim_{\mathbf F_2}H_3(K;\mathbf F_2)
=715-220-493=2.
\]

The verifier row-reduces the complete \(\partial_4\)-boundary space inside the \(715\)-dimensional tetrahedral chain group. It then constructs the boundary cycle of every missing five-set and reduces it modulo \(\operatorname{im}\partial_4\). All \(273\) are nonzero. Exactly three quotient classes occur, as required by the two-dimensional homology group, and each occurs exactly \(91\) times.

The lexicographically first carriers of the three quotient classes are
\[
\{1,2,3,5,7\},\qquad
\{1,2,3,5,8\},\qquad
\{1,2,3,7,8\}.
\]
Calling the first two classes \(\alpha\) and \(\beta\), exact chain reduction verifies that the third equals \(\alpha+\beta\). This proves the complete \(91,91,91\) shortest-carrier spectrum.

Finally, direct incidence counting over the complete \(273\)-support family gives \(105\) carriers through every vertex. The identity
\[
273\cdot5=13\cdot105
\]
is the corresponding global incidence check.

## Verification
The standalone `verify.py` contains all \(208\) published facets and uses only the Python standard library.

It reconstructs every face, verifies four-neighborliness and the full face vector, computes both mod-two boundary ranks by exact bit-vector elimination, enumerates all \(1287\) five-sets, and checks every present and missing four-simplex boundary. The quotient reduction is performed against a reduced row-echelon basis of \(\operatorname{im}\partial_4\), so equality of the reduced chains is exactly equality of homology classes for these \(3\)-cycles.

Exact successful output:

`VERIFY_OK f=13,78,286,715,1014,728,208 H3_F2_dim=2 missing5=273 all_missing5_nonzero=yes class_counts=91,91,91 reps=12357|12358|12378 class_relation=alpha+beta=gamma carrier_vertex_degree=105`

The computation exhausts every five-vertex support. No larger-support enumeration is needed for the minimum statement.

## Relationship to prior work
Lutz introduced this explicit thirteen-vertex triangulation, proved vertex minimality, and records that it is four-neighborly and tight. Tightness already makes nontriviality of induced homology a natural expectation, so the present finding does not claim novelty for the existence of small nonzero middle-homology carriers.

The new statement is the complete class-level refinement of the shortest layer: all \(273\) missing four-simplex boundaries are classified simultaneously, and the three nonzero classes of \(H_3(K;\mathbf F_2)\) receive exactly \(91\) shortest carriers each. This perfect balance is not explained by simplicial symmetry because Lutz also records that the triangulation is asymmetric.

Later tight-triangulation literature lists Lutz's thirteen-vertex \(S^3\times S^3\) examples among the known tight six-manifolds, but the inspected statements do not give the \(273\)-carrier class distribution or the \(91,91,91\) balance.

## Limitations
The result is mod-two and specific to \((S^3\times S^3)^a_{13}\). It does not classify the integral classes of the \(273\) embedded tetrahedral \(3\)-spheres, nor does it compare the other known thirteen-vertex triangulations of \(S^3\times S^3\).

The equality \(91,91,91\) is an exact finite invariant of this labelled complex. An unindexed historical computation could contain the same distribution even though no covering indexed statement was located.

## References
1. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:`math/0506372v1`, submitted 2005-06-18; Theorem 46 and the preceding \(208\)-facet table.
2. B. Bagchi and B. Datta, *On stellated spheres and a tightness criterion for combinatorial manifolds*, European Journal of Combinatorics 36 (2014), 294--313, DOI `10.1016/j.ejc.2013.07.018`.
