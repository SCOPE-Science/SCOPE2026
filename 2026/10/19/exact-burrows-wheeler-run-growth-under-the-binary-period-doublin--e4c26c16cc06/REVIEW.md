# Mathematical assessment

## Correctness — PASS

The four parity-and-input-symbol classes of cyclic rotations have strictly ordered short prefixes. Their within-class orders reverse the original rotation orders, giving an exact BWT last-column identity. The odd symbol-one counts make all period-doubling iterates primitive. Splitting the transferred BWT by the initial rotation symbol yields an exact run increment of two from the third iterate onward, with checked base \(\mathrm{BWT}(W_2)=1000\). The supplied checker verifies independent finite cases; the proof covers all lengths.

## Originality — PASS with residual uncertainty

The closest structural prior results are Brlek et al. (IWOCA 2019), exact BWT formulas for Thue–Morse and certain composed morphisms, and Frosini et al. (DLT 2022), logarithmic-order bounds for general binary morphic iterates. The latter cannot imply the coefficient or offset. Fici et al. (CPM 2023) studied period-doubling BWT sensitivity for input words chosen independently of the substitution fixed point; their conclusion does not determine the iterate series. Currie et al. (2013) studied extremal infinite shift words rather than finite cyclic BWT. No equivalent exact all-level transfer or run formula was found in the inspected sources. An unindexed result or inaccessible historical record may overlap.

## Value — PASS

The exact run count is a natural compression invariant and the last-column transfer theorem applies beyond a single family. The formula resolves the sharp logarithmic growth behavior at every substitution depth for the canonical period-doubling word; it is not a one-off computation.

## Scope and limitations

The BWT is cyclic, without sentinel, and runs are counted linearly. The transfer theorem needs primitivity and cyclic avoidance of \(11\). The exact iterate formula starts at \(k=2\). Finite computational checks alone do not prove the theorem, and independent validation is not represented.

Self-review: passed. Independent audit: not yet performed.
