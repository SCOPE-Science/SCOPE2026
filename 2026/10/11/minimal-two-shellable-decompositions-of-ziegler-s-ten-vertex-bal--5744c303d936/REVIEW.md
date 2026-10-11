# Review

## Correctness
PASS. The claim is finite and exact. The source facet list is reconstructed and gives face vector \( (10,38,50,21)\). Shellability is decided by the standard recursive last-facet criterion, evaluated for all \(2^{21}-1\) nonempty tetrahedron subsets. Every unordered complementary partition is then tested, and every surviving interface is independently checked for purity and two-dimensional shellability. The finalized verifier reproduces exactly \(247\) decompositions, the full block-size distribution, and the three minimum witnesses. The known non-shellability of the full complex is also recovered.

## Originality
PASS. Exact-object, constructibility, shellable-split, minimum-block and numerical searches found no statement of the \(247\)-decomposition census, the sharp five-tetrahedron minimum, or the three minimal witnesses. Ziegler supplies the ball and strong non-shellability; Hachimori records constructibility; Lutz supplies the topology/constructibility context; Dao--Doolittle--Lyle supply the minimal-Cohen--Macaulay equivalence. None implies the new finite classification. A residual risk remains that an older unindexed constructibility computation contains the same data without a searchable statement.

## Value
PASS. Ziegler's ball is a classical example separating shellability from weaker assembly properties. The new invariant directly measures the first decomposition layer by asking how the known constructibility can be witnessed using shellable children. The sharp minimum and complete set of minimum witnesses give a structural refinement of the qualitative fact "constructible but non-shellable," while the full distribution is a reproducible benchmark for algorithms that search constructibility decompositions.

## Closest literature and limitations
The closest literature establishes strong non-shellability, constructibility, and minimal Cohen--Macaulayness, but not the two-shellable split landscape. The theorem is intentionally narrower than a classification of arbitrary recursive constructibility trees and should not be read as such.

Same-model review: passed. Independent audit: not yet performed.
