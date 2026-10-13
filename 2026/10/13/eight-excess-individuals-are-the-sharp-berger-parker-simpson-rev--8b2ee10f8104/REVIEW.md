# Self-review

## Correctness
**PASS.** At fixed richness and total abundance, Berger–Parker ranking is exactly ranking by the maximum excess count, while Simpson ranking is exactly ranking by the excess sum of squares. The extremal bounds \(Q_{\max}(r,m)\) and \(Q_{\min}(r,m)\) exclude reversal for every \(r\le7\). Complete partition enumeration at \(r=8\) gives exactly four unrestricted reversing excess-pair types, and the fixed-richness length constraint yields first-layer counts \(1,2,3,4\) for \(k=3,4,5,\ge6\). The universal witness and the equivalence of the two Simpson conventions are replayed by the packaged verifier, which returns `VERIFY_OK`.

Risk: zero-abundance categories, unequal totals, or arbitrary real-valued weights define different boundary problems.

## Originality
**PASS.** Prior ecological literature directly compares Berger–Parker and Simpson dominance and already shows that diversity indices can produce different community rankings. That generic disagreement is not new. The accepted claim is the sharp positive-integer fixed-richness threshold and complete first layer. Searches using exact vectors, smallest-resolution language, fixed richness, integer abundance, ranking reversal, and majorization language did not locate the \(k+8\) theorem or its first-layer classification.

Risk: the reduction is elementary enough that an unindexed teaching example or software test could contain the same eleven-individual witness.

## Value
**PASS.** Berger–Parker and Simpson are established dominance summaries that intentionally weight abundant species differently. The smallest integer community resolution at which that weighting choice can reverse a comparative judgment is a natural interpretive benchmark. The excess-unit normalization shows that the threshold is independent of richness, and the complete first layer provides a compact diagnostic suite rather than a single arbitrary numerical example.

Self-review: passed. Independent audit: not yet performed.
