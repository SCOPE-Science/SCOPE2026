# Scientific assessment

## Correctness: PASS

The exact finite-state model checks each vertex's full open neighborhood, using zero sentinels only for absent horizontal neighbors. Every feasible labeling yields exactly one state path. Full 81-state min-cost shifts across three columns at starting lengths three, four, and five are sufficient for the infinite cost periodicity; 81-state fourth-difference zero identities then imply cubic-or-lower count polynomials on each phase. Four exact terminal samples determine those polynomials uniquely. The packaged checker replays these identities and performs separate exhaustive graph-level enumeration for lengths two through six. The proof does not infer an infinite formula from a finite sample alone.

## Originality: PASS (best-knowledge, not independent priority certification)

The original 2023 full-text article introducing total perfect Roman domination gives general inequalities, complexity, and special equality cases for trees, not this infinite ladder classification. The 2022 grid-product paper concerns the weaker perfect Roman condition and excludes width two in its principal bound, while the 2024 related paper's accessible abstract concerns perfect Roman/Italian variants, not the extra total-support condition. Published-result and equivalent-formulation searches did not disclose a matching minimum-function count or a stronger theorem implying it. A potentially relevant later full text was not inspected, and searches alone cannot establish worldwide novelty.

## Mathematical value: PASS

The theorem determines an exact extremal invariant and the number of *all* optimal configurations on the natural two-row grid family, directly motivated by the 2023 introduction and complexity of the parameter. The unique optimum at lengths divisible by three contrasts with linearly and quadratically many optima in the other residue classes. The small width allows a complete 81-state exact proof and illustrates a robust finite-state mechanism. No claim is made for wider or cyclic grids or for nonoptimal labelings.

Self-review: passed. Independent audit: not yet performed.
