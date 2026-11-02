# Review of last-occurrence matching normal form

## Correctness — PASS

The source operation is universal over later successor rows. Since the upset tests are thresholds, a row can falsify an antecedent-to-consequent inclusion precisely when its minimum lies in the half-open target interval. The greatest violating row index therefore determines the whole output upset. Singleton target intervals recover every last-occurrence entry, which is injective because one row has one minimum. Every partial injection has an explicit singleton-row representative. Counting partial injections proves the closed form, and independent row choices with forced and optional minima prove the fiber product. Exhaustive direct-semantics tests cover all binary relations through four worlds, not infinity; the generality comes from the proof.

## Originality — PASS within inspected evidence

De Groot–Litak (2026), Definition 3.5 and Proposition 3.10, supply the flat semantics and the previously known invariance under upward-closing each successor row. The inspected source does not give the cross-row last-occurrence equivalence, the partial-injection bijection, canonical least fiber representative, or exact fiber formula. A related published Bell-number result is restricted to relations satisfying two S4-like axioms and expressly does not count all flat relations. Other nearby finite-chain results use different connective/frame axioms. OEIS A002720 already enumerates partial injections; the combinatorial sequence itself is not claimed as new. Literature comparison and semantic equivalence checks were performed, but a historical-priority risk remains.

## Value — PASS

The number of relational presentations alone is \(2^{n^2}\), but many induce the same algebraic operation. The theorem classifies all distinct operations from unrestricted finite-chain flat frames, supplies minimal concrete presentations and measures each observational fiber exactly. This is a natural structural and enumerative complement to the finite model and relational-semantics theory, not a single arbitrary instance or a table recomputation.

## Limits and closest prior results

The theorem is fixed-carrier and fixed-order; it does not classify arbitrary-poset algebras, sharp implication, or abstract algebras lacking a given chain-frame representation. Primary comparison: de Groot and Litak, arXiv:2603.28402, Sections 3.1–3.3, 4–5 and appendix. Other comparisons: the restricted S4-like flat-chain Bell census, maxima forms for different intuitionistic tense relations, and the general partial-permutation sequence OEIS A002720. Independent validation was not performed.

Self-review: passed. Independent audit: not yet performed.
