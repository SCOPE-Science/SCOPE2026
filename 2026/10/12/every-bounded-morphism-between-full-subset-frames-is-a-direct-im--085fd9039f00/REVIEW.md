# Self-review

## Correctness — PASS

For nonempty full powerset frames under reverse inclusion, singleton worlds are exactly the maximal worlds. The back condition forces every singleton to map to a singleton, producing a unique underlying set map. Monotonicity gives one inclusion at every world; lifting each target singleton and descending to an arbitrary source singleton gives the reverse inclusion. Conversely, the explicit preimage intersection \(A\cap c^{-1}[T]\) proves the back condition for any nonempty target successor. This construction does not invoke choice, so the proof covers infinite sets. Composition and the finite counts are direct consequences. Independent finite enumeration checked all 826,113 possible world maps for nine pairs of frame sizes \(1\le n,m\le3\), matching the classification exactly. These computations are not a substitute for the general proof.

## Originality — PASS, with residual risk

Han Xiao (2026, arXiv:2606.31893) uses the Medvedev frames and \(p\)-morphisms for axiomatizability, but the inspected statements and proof do not classify all frame-to-frame maps. Nicola Vio (2023, Section 6.3, Lemmas 6.22--6.25) already constructs all permutation automorphisms and useful onto maps; these are explicit prior special cases. Ciardelli (2009, Section 3.4.1) identifies singleton endpoints and saturation, and Gyenis (2018, Section 4) treats infinite Medvedev powersets and support morphisms. Their stated results do not include the complete hom-set bijection for arbitrary nonempty source and target sets. Searches for the category equivalence, all-map classification, and Stirling-number onto counts did not locate such a statement. An equivalent formulation in older semilattice, modal-frame, or category theory literature is a real residual risk; lack of a search match is not itself a proof of novelty.

## Value — PASS

This is a complete structural classification of an established family of Kripke frames, not a numerical spot check: it identifies every bounded morphism, composes these morphisms by ordinary composition of set functions, describes every image as a generated subframe, and gives all finite hom-set and onto-hom-set cardinalities at once. Because \(p\)-morphic images govern transfer of intuitionistic-frame validity, the exact criterion for surjective reductions has direct semantic meaning. The unrestricted-set formulation also distinguishes the construction from finite counting alone.

## Scope and limitations

The result applies only to full nonempty powersets with reverse inclusion. It does not classify morphisms from arbitrary products of other finite rooted frames, nor does it derive the nonfinite axiomatizability results of the motivating source. Older categorical formulations may subsume the statement. The enumeration tests are exhaustive only for frame sizes at most three; the unbounded theorem rests on the written proof.

Self-review: passed. Independent audit: not yet performed.
