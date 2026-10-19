# Scientific review: Dihedral conjugacy and rank enumeration of retractions of finite cycles

## Correctness

**PASS.** A graph-endomorphism idempotent fixes its image, and each proper image is a path arc; its complement maps as a bounded nearest-neighbor walk. This gives the labeled rank formula without omissions. The dihedral group is transitive on arcs, the chosen arc stabilizer has order two, and the reflection acts on complementary walks by reversing time and complementing height. Burnside's lemma and midpoint splitting give the orbit formula. The determinant recurrence and reflection principle independently express the walk counts. Odd cycles have only automorphism endomorphisms. The included two finite verifiers corroborate every labeled coefficient through cycle length 16 and every conjugacy coefficient through cycle length 15; proof, not finite checking, covers all sizes.

## Originality

**PASS within checked literature, with explicit residual risk.** Dimitrova et al. (2023, arXiv:2310.04149) establish the endomorphism-monoid setting, regularity and Green relations, total cardinalities and generating ranks, but the inspected full text does not give a rank-indexed enumeration of idempotent retractions modulo dihedral unit conjugation. **The unrefined Dyck-path sequence is already known** as OEIS A287709, and Bacher (arXiv:2403.08120) gives Dyck-path enumeration results. They do not identify the dihedral unit-conjugacy action or count its reflection-fixed retractions by rank. Completed targeted searches of mathematical findings and literature found no equivalent or dominating theorem. Relevant path-homomorphism work was located in abstract only, and work outside the indexed corpus might subsume the claim; these are documented, not dismissed.

## Value

**PASS.** The classification determines a natural complete family of rank-resolved algebraic orbit invariants for cycle endomorphism monoids. It explains which retractions are identified by graph automorphism and why reflection-fixed walks must be counted separately. The main result is not merely the already catalogued Dyck scalar sequence: it gives the unit-conjugacy polynomial and the stabilizer structure for every cycle order.

## Scope and limitations

Only full adjacency-preserving graph endomorphisms and dihedral unit-conjugacy are treated; neither weak/partial maps nor nonunit conjugacy are classified. The finite scripts are reproducibility checks, not independent infinite proof. Unindexed literature and an abstract-only path-congruence comparison remain originality risks.

Self-review: passed. Independent audit: not yet performed.
