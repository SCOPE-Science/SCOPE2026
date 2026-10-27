# Self-review

## Correctness — PASS
The residue-class invariant establishes necessity for both input letters. Conjugating the rank-deficient letter with powers of the cyclic permutation produces single-vertex contractions \(j\mapsto j+d\). The noncoprime successor map splits into disjoint cycles; retaining one vertex in each cycle makes the missing vertices a union of directed paths, whose topological deletion order proves sufficiency. The macro schedule count is a disjoint-chain linear-extension multinomial, and the generating polynomial follows by independent choices of nonempty subsets across residue classes. A direct full power-automaton traversal and a separate counting recursion corroborate the core claims on the recorded finite ranges. This proves the infinite family symbolically, not by extrapolating finite tests.

## Originality — PASS within inspected evidence
Don (2016, Proposition 15) proves full reachability for coprime displacements, which does not imply the stated noncoprime image-set enumeration or canonical contraction-order counts. Hoffmann (2020) concerns full reachability and synchronizing-word state complexity; Casas–Volkov (2022, Proposition 1) gives a subgroup obstruction but not an exact reachable-image census; Ferens–Szykuła (2026) gives general algorithmic criteria and reaching bounds; Szykuła (2026) surveys open synchronization and subset questions. The closest publicly indexed independent result on cyclic defect-one automata addresses codimension-two reachability under different hypotheses, not the entire rank generating function. Actual semantic searches of mathematical research records and primary text produced no dominating noncoprime theorem. A publication not indexed or not inspected could still supply an equivalent result; this is a priority risk rather than a novelty proof by absence.

## Value — PASS
The noncoprime phase is precisely where the familiar coprime complete-reachability theorem ceases to apply. The classification supplies the entire image language of a natural infinite family of strongly connected, non-synchronizing circular automata, all image-rank counts, and the exact number of minimal-rank-loss macro schedules for each labelled target. The structure is a useful concrete benchmark for image reachability of transformations, rather than an arbitrary finite slice or recomputation of a known table.

## Remaining limits
Only images from the full state set and the explicitly defined simple-idempotent family are treated. Canonical macro schedules are not all words with the same letter-count optimum. Historical priority beyond accessible indexed literature remains an unresolved risk.

Self-review: passed. Independent audit: not yet performed.
