# Self-review

## Correctness — PASS

The six possible received pairs are determined by the positive/heavy coordinates of a ternary source multiset. For every source length \(\,n\ge4\,\), all codewords are heavy in at least one coordinate and only twelve possible words have exactly one heavy coordinate. Counting the three pure received-pair incidences yields the rigorous inequality \(2M-12\le3L\), hence \(M\le\lfloor3L/2\rfloor+6\). The explicit symmetric twelve-word core and the balanced edge additions meet the bound for \(L\ge6\); a direct length-four witness and injective signature-preserving lift handle \(L=5\). Equality at even \(L\) forces all three pure lists to saturate, inclusion of all twelve one-heavy messages, and exactly two heavy coordinates in every other message.

The standalone source checker reproduced the constructions in 198 parameter cases, all 9,119 source-word lift transitions across lengths four through thirty-six, and all \(2^{15}\) length-four subcodes. These tests corroborate, rather than replace, the symbolic proof. Boundary assumptions and quantifiers were checked directly.

## Originality — PASS within inspected evidence

The nearest primary source, Kreindel–Barouch Essayag–Zabokritskiy, arXiv:2601.05636, gives exact two-survivor **unique-decoding** values using a pairwise intersection condition. Its follow-up arXiv:2603.18322 develops distance-ball geometry and bounds, without determining bounded lists of size \(L\ge5\). An accessible previous finding establishes the four-list ternary two-survivor value, and a different result covers only \(L\le2\) for two survivors. The present high-list formula and even-list equality conditions are not implied by either. Targeted research-record and primary-literature searches did not identify a covering result; equivalent unindexed material remains a historical-priority risk.

## Mathematical value — PASS

The exact formula \(M_3(n,L;2)=\lfloor3L/2\rfloor+6\) holds over an infinite, naturally motivated two-parameter family, with explicit optimal codes and a new structural explanation of the slope through twelve exceptional words and balanced two-heavy edge incidences. The even-\(L\) equality rigidity is a substantive restriction on all maximizers. The given source-length condition is sufficient, not necessarily the first attainment length; that distinction is retained consistently across the claim and proof.

## Remaining limits

The precise smaller-length profile, other alphabet sizes and survivor lengths, full uniqueness classification and independent mathematical validation remain outside the result.

Self-review: passed. Independent audit: not yet performed.
