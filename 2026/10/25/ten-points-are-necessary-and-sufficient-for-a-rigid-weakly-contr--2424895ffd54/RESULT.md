# Ten points are necessary and sufficient for a rigid weakly contractible noncontractible finite space

## Finding

Let a **rigid** finite \(T_0\)-space mean a space whose only homeomorphism to itself is the identity. Among finite \(T_0\)-spaces that are weakly contractible but are not contractible, the least possible cardinality for a rigid example is **\(10\)**.

More precisely, let \(X\) have exactly ten points, no beat points, be weakly contractible, and be noncontractible. In the complete Das--Mawiong classification, the homeomorphism groups of Types I--VII, in that order, are
\[
 C_2,\quad S_3,\quad C_2\times C_2,\quad C_2\times C_2,\quad C_2,\quad C_2,\quad 1.
\]
Types I--III's order-duals have the same groups. Consequently **Type VII is the only rigid ten-point beat-point-free example**, up to homeomorphism. It is self-dual and has exactly one order-reversing self-bijection, which is an involution. Here \(C_2\) denotes the cyclic group of order two and \(S_3\) the full symmetric group on three letters.

## Assumptions and scope

Finite \(T_0\)-spaces and finite posets are identified by the specialization order. Homeomorphisms are order-preserving bijections, while **order-reversing bijections** are poset anti-automorphisms and are not called homeomorphisms here. A beat point is a point whose strict upper set has a least element or whose strict lower set has a greatest element. A space with no beat points is *minimal* in the Stong finite-space sense.

We use the published complete classification of ten-point minimal weakly contractible noncontractible spaces by Das--Mawiong [1], including its incidence lists in Sections 4.1 and 5.1. It is not a new classification of the ten underlying posets or a new proof of their weak contractibility. Cianci--Ottina [2] establish the cardinality-nine threshold and the two nine-point dual models. Costoya--Gomes--Viruel [3] record that the classical nine-point Rival model has homeomorphism group \(C_2\); the other nine-point model is its dual and hence has the same automorphism group.

The uniqueness statement is deliberately restricted to ten-point spaces **without beat points**. The threshold statement itself concerns all finite \(T_0\)-spaces, not only minimal ones.

## Proof

### 1. Layer- and incidence-preserving automorphisms

All ten classified posets have three levels: minimal elements \(C\), middle elements \(B\), and maximal elements \(A\), with \(B\) an antichain and no covering relation directly from \(C\) to \(A\). Every order automorphism preserves these three levels. Conversely, three permutations of the levels yield an automorphism precisely when they preserve the cover incidences \(C<B\) and \(B<A\), since the remaining order relations are their transitive closure. The classifications of [1] give the following observations.

For **Type I**, the three middle elements have distinct numbers \(2,3,4\) of upper neighbors, and so each middle element is fixed. Their three distinct lower-neighborhood patterns force every minimum to be fixed. The only remaining freedom is the transposition of the two maxima with identical lower neighborhoods; the group is \(C_2\).

For **Type II**, the lower incidence graph is a six-cycle: each of three middle points excludes one distinct minimum. The upper incidence has one maximum above every middle point and three other maxima, each excluding one distinct middle point. Thus any of the \(3!\) permutations of the middle points uniquely induces permutations of minima and maxima, and all preserve the order. The group is \(S_3\).

For **Type III**, the third middle point is uniquely characterized by having three lower neighbors, and the third minimum is uniquely characterized by having three upper middle neighbors. The first two middle points can be interchanged together with the first two minima and the final two maxima. Independently, the first two maxima have identical lower neighborhoods and can be exchanged. These two commuting independent involutions yield \(C_2\times C_2\).

Passing to the dual poset conjugates its order automorphisms and preserves the abstract automorphism group. This handles the three additional classified types dual to I--III.

### 2. Omission-graph principle for Types IV--VII

For any three-level poset whose middle layer is an antichain, with every \(b\in B\) covering all but exactly one element \(\mu(b)\in C\) and lying below all but exactly one element \(\nu(b)\in A\), define the **colored omission multigraph** \(\Gamma\) on the disjoint vertex sets \(C\) and \(A\). Give each middle element \(b\) a (possibly parallel) edge joining \(\mu(b)\) to \(\nu(b)\). Its bipartition-preserving automorphism group (allowing the permutation of parallel edges) is canonically the order-automorphism group of the three-level poset: both groups consist of exactly the triples of permutations preserving the omitted incidence pairs. When \(|C|=|A|\), bipartition-swapping graph automorphisms correspond in the same way to order-reversing poset bijections. These correspondences use the explicit hypothesis that no extra minimal-to-maximal cover relation occurs.

In the four classified cases, Table 1 of [1] gives the following **colored** graphs, where a singleton superscript indicates on which side an isolated vertex lies.

| Type | Omission graph \(\Gamma\) | Part-preserving group | Number of part-swapping automorphisms |
| --- | --- | --- | ---: |
| IV | \(C_4\sqcup K_1^C\sqcup K_1^A\) | \(C_2\times C_2\) | 4 |
| V | \(P_5\sqcup K_1^A\) | \(C_2\) | 0 |
| VI | \(P_5\sqcup K_1^C\) | \(C_2\) | 0 |
| VII | \(P_4\sqcup P_2\) | \(1\) | 1 |

For clarity, \(P_j\) is the path on \(j\) vertices, and \(C_4\) the four-cycle. In the Type IV four-cycle, each side of the bipartition may be transposed independently, giving the Klein four group; the two isolated vertices are forced within each side. In Types V and VI, the only nonidentity part-preserving automorphism reverses the five-vertex path. In Type VII, the two path components have distinct orders, and reversing the four-vertex path swaps its two bipartition classes. Reversing the two-vertex path also swaps its classes. Consequently no nontrivial **part-preserving** automorphism exists, but there is exactly one global **part-swapping** automorphism. This proves the asserted rigidity and uniqueness of its order-reversal.

Explicitly, for Type VII using the labeling of [1], the involution exchanges \(c_1\leftrightarrow a_3\), \(c_2\leftrightarrow a_2\), \(c_3\leftrightarrow a_1\), and \(b_1\leftrightarrow b_4\), while fixing \(b_2,b_3\). The displayed incidence lists directly show that it reverses the specialization order. Because there is exactly one order-reversing bijection, its square must be the identity, also visible from the displayed exchanges.

### 3. The sharp minimum

Theorem 3.6 of [2] excludes every finite \(T_0\)-space with fewer than nine points that is weakly contractible and noncontractible. Theorem 3.7 of [2] classifies the nine-point possibilities as a single model and its order-dual. The classical model is the Rival example for which [3, Section 3] reports \(\operatorname{Aut}\cong C_2\); order duality does not change the automorphism group. Thus no such nine-point space is rigid. Type VII is a ten-point minimal weakly contractible noncontractible space by [1] and is rigid by Step 2. Therefore the minimum cardinality is exactly \(10\).

## Verification

The standalone standard-library script `verify.py` hard-codes exactly the seven published lower- and upper-cover tables, enumerates permutations of all three levels exhaustively, and checks each transformed incidence set for equality with the original. It also independently enumerates all order-reversing bijections when \(|A|=|C|\), asserts each of the seven group orders, checks element-order distributions distinguishing \(S_3\) from the Klein four group, and verifies that the unique Type VII anti-automorphism squares to the identity. Its execution printed all seven expected group orders and the line `All exact incidence and group assertions passed.`

A second implementation using directed graph isomorphisms of the cover relation, rather than the layer-wise permutation restrictions, returned matching automorphism and anti-automorphism counts for all seven types. Both checks are finite and exhaustive **within the previously classified list**; exhaustiveness of that underlying ten-point classification, and the nine-point classification, are cited from [1] and [2], rather than inferred from these computations.

## Relationship to prior work

Cianci--Ottina [2] proved the nine-point threshold and classified the smallest examples. Costoya--Gomes--Viruel [3] studied automorphism groups of minimal Alexandroff spaces and their realization in much larger weakly contractible spaces; their framework includes the group of the classical nine-point model. Das--Mawiong [1] classified all ten-point minimal examples and provided their order relations, self-duality patterns, and topological proofs. The new content here is the **complete automorphism-group evaluation** of this precise finite classification, the reusable omission-graph reduction, the unique rigid but self-dual ten-point minimal model, and the resulting sharp cardinality threshold for rigidity.

## Limitations

No uniqueness is asserted among all (possibly nonminimal) ten-point weakly contractible noncontractible spaces. No new construction or weak-contractibility proof is given beyond the classified Type VII, and no claim is made about spaces on more than ten points. The assertion that the threshold is \(10\) depends on the published nine- and ten-point classification theorems and the identification of the classical Rival nine-point example in [2] and [3]. The literature comparison is substantive but cannot certify exhaustive global originality.

## References

[1] P. Das and S. M. Mawiong, *On Weakly Contractible Non-Contractible Finite Topological Spaces of Ten Points*, arXiv:2605.06155, first public version May 7, 2026, Sections 4.1 and 5.1, Theorems 1.1, 4.1 and 5.1. https://arxiv.org/abs/2605.06155

[2] N. Cianci and M. Ottina, *Smallest homotopically trivial non-contractible spaces*, arXiv:1608.05307, first public version August 18, 2016, Theorems 3.6--3.7. https://arxiv.org/abs/1608.05307

[3] C. Costoya, R. Gomes and A. Viruel, *Realization of permutation modules via Alexandroff spaces*, arXiv:2308.16675, Section 3 (automorphism group of Rival's model and relation to self-homotopy equivalences). https://arxiv.org/abs/2308.16675
