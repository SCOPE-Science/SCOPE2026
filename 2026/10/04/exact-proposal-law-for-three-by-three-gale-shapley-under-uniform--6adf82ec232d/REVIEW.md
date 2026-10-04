# Same-model scientific review

## Correctness
**PASS.** The claim is a complete finite census. All \(46656\) strict labeled profiles are run through two Gale–Shapley implementations that agree on matching and proposal count. The proposal count is independently constrained by the exact identity between proposals and the sum of the men-optimal partner ranks. All six perfect matchings are separately tested for stability at every profile. Exact rational arithmetic gives the mean, variance, and conditional means.

Risk: the proof is computational rather than a symbolic classification. The universe is small and exhaustive, and the known one-round count and published stable-matching multiplicity marginals provide independent external calibration.

## Originality
**PASS.** The proposal count itself is classical, and the \(P=3\) one-round count \(10368\) is explicitly prior. The published three-by-three counts of profiles with one, two, or three stable matchings are also prior. The inspected literature does not state the full proposal law, the sharp support endpoint at seven, the seven-atom men-optimal partner-rank law, or the proposal-count/stable-multiplicity joint table. Exact-number searches and semantic searches found no equivalent statement.

Risk: an unindexed exercise, thesis, note, or software table may contain the same finite distribution. Wilson's 1972 paper was used for historical runtime context rather than a whole-document novelty absence claim.

## Value
**PASS.** The number of proposals is the canonical execution-cost statistic for Gale–Shapley, central to both its worst-case and random-input analyses. The three-by-three market is the first size with genuinely varied stable-set multiplicity and nontrivial proposal tails. The exact law gives a finite calibration for asymptotic theory and reveals a sharp link between algorithmic effort, men-optimal partner ranks, and stable-set multiplicity.

Same-model review: passed. Independent audit: not yet performed.
