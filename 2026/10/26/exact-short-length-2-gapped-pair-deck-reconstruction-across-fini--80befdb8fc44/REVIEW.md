# Scientific review

## Correctness — PASS
The definition includes individual-symbol counts as well as all ordered pairs with positions separated by at least one skipped symbol. The proof establishes binary-projection preservation of observations. The complete binary finite base yields injectivity at lengths three through five and forces each changed symbol to occur three times at length six or at least twice at length seven. Thus length-six collisions use exactly two symbols, and any length-seven collision uses no more than five symbols. A complete five-letter exhaustive certificate checks all 78,125 length-seven words, with independently implemented direct and streaming deck calculations, no fibers larger than two, and support-2 and support-3 multiplicities of 10 and 15 per alphabet subset. These facts prove the all-alphabet formulas without an unverified extrapolation. The packaged checker was executed successfully.

## Originality — PASS, with residual risk
The leading 2022 paper already reports binary \(G(2)=6\) and a colliding pair; these are not new. It does not give the complete alphabet-uniform cardinalities or the support-refined n=7 classification. The 2021/2023 distinct-deck paper counts *ungapped* subsequences and the 2019 multiset-spectrum paper uses contiguous substrings. Published indexed comparisons for adjacent-pair and higher-order gapped decks concern different observables, and no stronger implication covering the new exact formulas was identified. Unindexed equivalent counts remain a risk; see the structured audit for exact searches and comparisons.

## Mathematical value — PASS
Determining how much information a constrained-read deck preserves is a natural finite-length coding/reconstruction problem. The exact length-seven formula and double-fiber classification give the optimal short reconstruction-code size for every alphabet cardinality, identify precisely when three-symbol ambiguity first arises, and show structurally why alphabets of size greater than five need not be enumerated. This is a natural complete classification, not a chosen arbitrary individual input.

## Limits
The classification is restricted to readout length two, index separation at least two, and source lengths up to seven. No higher-length result or external audit is claimed. The numerical binary threshold from prior literature is explicitly credited.

Self-review: passed. Independent audit: not yet performed.
