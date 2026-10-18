# Scientific review of the arithmetic Mordell–Weil rank

## Correctness — PASS

The precise curve is Burek's equation (1.5), whose geometric rank \(12\) and torsion-freeness are established in the source. The proof constructs trace/anti-trace sections and obtains nonzero exact height determinants \(16777216/9\) and \(256\) for eight and four sections, respectively. Each intersection rule follows the local type-IV resolution calculation in the originating Appendix A.3. All twelve source identities and both good specializations' full height matrices are checked by the included standalone exact-arithmetic script. Specialization gives genuine lower bounds; the known geometric rank gives the upper bound. This avoids assuming saturation of the twelve-point lattice.

## Originality — PASS

The source paper proves geometric rank \(12\) and supplies twelve sections over \(\mathbb Q(i)(v,t)\), but not the rank over \(\mathbb Q(v,t)\). Kumar–Kuwata's geometric lattice and fields-of-definition results do not calculate this two-variable fixed rank. Direct comparison with the nearest previously recorded same-family point-count/height-distribution result shows it determines a different invariant of a single K3 fibre rather than Galois descent for the family. Targeted mathematical-literature and indexed-result searches did not reveal a covering statement. Residual risk: an unindexed calculation or a nonobvious consequence of earlier field-of-definition work could duplicate this value; search non-detection alone is not a novelty proof.

## Mathematical value — PASS

The rank discrepancy is an arithmetic obstruction to descending the sections of a naturally constructed high-rank elliptic Calabi–Yau threefold. The specific eight/four decomposition identifies exactly how much of its Mordell–Weil space exists over the original rational-function field, rather than merely over a convenient quadratic coefficient extension. It concerns the central invariant in the originating work, not an incidental numerical feature. It is a complete exact answer for this particular field-extension question.

## Closest literature and limits

Dominik Burek, arXiv:2610.01276v1, Theorem 1.1/Proposition 5.6/Appendix A; Abhinav Kumar and Masato Kuwata, arXiv:1409.2931, Theorems 2.10–2.11 and 5.1–5.3. The calculation gives rational ranks, not a saturated integral Mordell–Weil basis. The geometric rank bound remains an explicit external premise.

Self-review: passed. Independent audit: not yet performed.
