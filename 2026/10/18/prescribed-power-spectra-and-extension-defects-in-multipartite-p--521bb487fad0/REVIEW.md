# Scientific review

## Correctness — PASS

The proof first shows that \(f^d=\operatorname{id}_{\operatorname{dom}f}\) forces an invariant domain, then identifies the corresponding induced-graph automorphism group with a product of wreath products. Conditioning on the outer permutation cycle containing a specified block gives the recurrence \(W_{s,m}(d)\), including \(d=1\), the empty domain and one-part graphs. The extension count uses the original full-part-size strata and a constructive complementary-bijection argument proving preservation of the power constraint. Rank-two nonextendibility is completely exhausted by swaps across unequal original part sizes. A standalone checker verified 45 unrefined plus 45 extension-refined exhaustive graph cases and 56 direct symmetric-group cases; computation is independent corroboration, not the proof.

## Originality — PASS within the sources inspected

The closest inspected primary paper, Jajcay–Jajcayová–Szakács–Szendrei (arXiv:1809.04422, 2018), identifies maximal subgroups of partial graph automorphism monoids with induced-subgraph automorphism groups and studies inverse-monoid characterization; it does not supply the all-power, rank-refined enumeration or exact power-preserving extension count. Chih–Plessas (arXiv:1506.02093) focus on inverse-semigroup, idempotent and ideal structure. Gardiner's 1976 homogeneous graph criterion already gives the equal-size condition for unrestricted partial-automorphism extension, so that known qualitative criterion is explicitly excluded from the novelty claim. The asserted advance is the exact paired enumerators and finite-order preserving extension defect, not the component decomposition or classical wreath cycle-index algebra. A 2022 computational survey was identified but was not fully inspectable; an unindexed equivalent count remains the principal risk.

## Value — PASS

The family of inverse monoids of partial automorphisms is a natural extension of automorphism groups. Counting the \(d\)-th roots of *all idempotents* by rank for every positive \(d\) is a complete parameterized invariant across infinitely many monoids, not a small numerical slice. Counting those roots that extend while retaining the prescribed order isolates a mathematically motivated local-to-global symmetry obstruction. The exact first-defect formula at rank two and its sharp equal-part-size boundary quantify, rather than merely restate, classical homogeneity.

## Limitations and residual risk

The result is confined to complete multipartite simple graphs. The checker uses finite exhaustive tests, whereas universality rests on the proof. Equivalences via wreath-product permutation-cycle indices and unindexed partial-automorphism enumeration remain possible. Full access to Jajcayová's 2022 computational paper was not obtained. No independent external review or certification was performed.

Self-review: passed. Independent audit: not yet performed.
