# A 710-sphere double of a join of two simplex boundaries

## Finding

Let \(A\) and \(B\) be disjoint sets of cardinalities four and five. Write \(X=\partial\Delta^3_A*\partial\Delta^4_B\), a triangulated six-sphere. Let \(D(X)\) denote the simplicial double: its vertices are the two-element faces of \(X\), and a collection of those vertices forms a simplex exactly when they are pairwise disjoint and their combined endpoint set is a face of \(X\).

The complete integral homotopy type is
\[
\boxed{|D(X)|\simeq\bigvee^{710}S^2.}
\]
The reduced integral homology is therefore \(\mathbb Z^{710}\) in degree two and zero in every other degree. There is no torsion.

The natural \(S_4\times S_5\)-action permutes the two blocks separately. Its degree-two rational homology character is determined on all 35 conjugacy classes in `character_table.csv`; its 35 rational irreducible multiplicities are in `irreducible_multiplicities.csv`. Exactly 22 isomorphism types occur with nonzero multiplicity. In particular,
\[
\widetilde H_2(D(X);\mathbb Q)^{S_4\times S_5}=0.
\]
Here the superscript means the subspace fixed by every block-preserving permutation.

## Assumptions and scope

A face of \(X\) may contain every proper subset of \(A\) and every proper subset of \(B\), but must not contain all of either block. Fix \(A=\{0,1,2,3\}\) and \(B=\{4,5,6,7,8\}\). Order the 36 vertices of \(D(X)\) lexicographically by their underlying unordered endpoint pairs. The simplices of \(D(X)\) are precisely the nonempty matchings on these nine labels whose covered vertices omit at least one element from each block. This is an equivalent, restricted complete-graph matching-complex description.

At most seven endpoints are allowed, so a matching contains at most three edges and \(D(X)\) has dimension two. No claims are made for arbitrary block sizes or higher tupling parameters.

## Proof

**Exhaustive face description.** The exact executable `verify.py` first enumerates admissible edge families by increasing edge index, extending a family only if the next edge is disjoint from all previously selected edges and does not saturate either block. It independently enumerates all one-, two-, three- and four-edge subsets of the 36 possible edges and tests the same predicate from scratch. The two methods agree on the complete face vector
\[
(f_0,f_1,f_2)=(36,375,1050),
\]
with no higher-dimensional faces. In particular the reduced Euler characteristic is \(36-375+1050-1=710\).

**Discrete-Morse matching.** The following finite algorithm defines a partial matching of the face poset, excluding the empty face. Initially all nonempty faces are unmarked. Traverse the 36 edges in the fixed lexicographic order. At the stage for an edge \(e\), traverse the nonempty faces in order of cardinality then lexicographic order. Whenever a still-unmarked face \(\sigma\) omits \(e\) and the enlarged face \(\sigma\cup\{e\}\) is a still-unmarked face, pair these two faces and mark both. In this way every pair is a codimension-one face relation; no simplex belongs to two pairs.

The executable enumerates all 1,461 nonempty faces, constructs the matching, and obtains exactly 375 pairs: 35 vertex-to-edge pairs and 340 edge-to-triangle pairs. The unmatched faces consist of exactly one vertex and 710 triangles, with no unmatched edges.

**Global acyclicity certificate.** Orient each unmatched codimension-one incidence downward and each matched incidence upward in the Hasse diagram. The executable constructs all 3,900 codimension-one incidences directly from the enumerated simplices, then applies Kahn's exact integer topological-sort algorithm. Every one of the 1,461 vertices is removed by that algorithm. Thus the directed Hasse graph is acyclic, so the matching is an acyclic discrete-Morse matching in the sense of Forman. This is a finite exhaustive proof, not a sample of possible paths. Discrete Morse theory produces a CW complex with one cell of dimension zero and exactly 710 cells of dimension two. Since all two-cells attach to the unique zero-cell, that CW complex is the wedge of 710 two-spheres, proving the integral homotopy assertion.

**Rational block-permutation character.** For a block-preserving permutation \(g\), let \(F_k\) denote the set of oriented \(k\)-simplices of \(D(X)\), oriented by increasing edge index. The signed action on simplicial chains gives
\[
\operatorname{tr}(g\mid H_2(D(X);\mathbb Q))
=-1+\sum_{k=0}^{2}(-1)^k
 \sum_{\substack{\sigma\in F_k\\g\sigma=\sigma}}
 \operatorname{sgn}(g\mid\sigma).
\]
This follows from the Hopf trace identity, since the only nonzero ordinary homology groups are the one-dimensional trivial \(H_0\) and the 710-dimensional \(H_2\). The verifier checks the signed fixed-simplex sum for all \(4!5!=2880\) group elements, confirms constant values on all 35 pairs of cycle types and exports the complete character table. Its character average is zero, proving absence of invariants. An independent character-theoretic step computes irreducible multiplicities using the Murnaghan–Nakayama rule and exact rational class sums. Exact orthogonality checks, nonnegativity, integrality and recovery of total dimension 710 validate that decomposition.

## Verification

Run `python3 verify.py` from the directory containing the three accompanying files `verify.py`, `character_table.csv` and `irreducible_multiplicities.csv`. The standalone script requires only the Python standard library, reconstructs the complexes and writes both CSV files deterministically. The complete run prints `ALL_VERIFY_OK` only after all assertions pass.

The observed checks are: two face enumerators give \((36,375,1050)\), the mod-two boundary maps have ranks 35 and 340, the Morse matching has 375 pairs and critical-cell counts \((1,0,710)\), the full oriented Hasse graph has 3,900 incidences and is acyclic, and all 2,880 group elements satisfy the character and representation tests. The mod-two computation is corroborating evidence; the integral homotopy statement follows from the acyclic matching.

## Relationship to prior work

Lesh, Schreiner and Wahl (arXiv:2506.10436, first public June 12, 2025, subsequently revised) introduced doubling and \(r\)-tupling and proved a weak Cohen–Macaulay connectivity theorem. Their Theorem A applied to this six-sphere gives a weak Cohen–Macaulay bound of dimension one, rather than this exact two-dimensional wedge decomposition or its symmetry representation. Their complete-simplex examples identify doubles with ordinary complete-graph matching complexes; those examples do not equal the present restriction that forbids saturating either block.

Jonsson (arXiv:1203.5658) analyzes integral torsion in ordinary complete-graph matching complexes, including the nine-label case. That object includes matchings saturating a block and is therefore larger than the present double. Known torsion in the complete matching complex does not determine this restricted complex, which is torsion-free by the explicit matching.

## Limitations

This is a complete computer-assisted proof for the specified nine-vertex source complex, not an infinite-family theorem. The block-preserving representation is calculated over \(\mathbb Q\), not as a decomposed integral \(S_4\times S_5\)-lattice. An equivariant homotopy equivalence is not claimed. The correctness of the finite exhaustive certificate can be reproduced independently by running and inspecting the embedded script; no independent external mathematical audit has been performed. Overlap with unindexed literature is possible.

## References

- K. Lesh, B. Schreiner, N. Wahl, *The double of a simplicial complex*, arXiv:2506.10436 (first public version, 2025-06-12; revised 2026). Definition 2.1 and Theorem A. https://arxiv.org/abs/2506.10436
- J. Jonsson, *More Torsion in the Homology of the Matching Complex*, arXiv:1203.5658 (2012), especially the nine-label complete matching-complex calculations. https://arxiv.org/abs/1203.5658
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. Discrete Morse matching theorem.
