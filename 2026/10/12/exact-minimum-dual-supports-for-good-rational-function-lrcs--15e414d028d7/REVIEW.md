# Review

## Correctness

PASS. Theorem 3.2 gives generator columns whose \(j=0\) block is an extended Vandermonde system and whose fiber label is encoded by the distinct constants \(d_m\). Every at-most-\(r\) column set is therefore independent, while each full fiber supplies a unique dependence of size \(r+1\). For an arbitrary dependence of that size, the \(j=0\) and \(j=1\) blocks must use proportional coefficient vectors because the extended Vandermonde nullspace is one-dimensional; nonzero coefficients and pairwise distinct \(d_m\) then force a single fiber. This proves the dual distance, support classification, word count, and uniqueness of minimum-size repair. The packaged verifier independently checks a source instance and a higher-locality instance and confirms the necessary \(t=1\) boundary failure.

## Originality

PASS. The primary 2026 source defines the rational-function LRC family, its local fibers, and its optimal parameters but does not discuss dual words or minimum-weight dual supports. The closest recent general duality paper proves only the generic implication \(d(C^\perp)\le r+1\) from locality and does not classify equality supports. Searches across the source identifier, Tamo--Barg/good-polynomial aliases, dual distance, minimum dual words, recovery-set uniqueness, and fiber-Vandermonde formulations found no prior statement implying the exact formula \(A_{r+1}(C^\perp)=l(q-1)\) for this family. Residual risk remains that an unindexed matroidal or good-polynomial source contains an equivalent specialization.

## Value

PASS. The source's purpose is efficient local repair, so identifying every smallest repair set is a direct structural invariant of the new construction rather than an arbitrary finite statistic. The theorem upgrades existence of one local group per coordinate to an exact repair hypergraph at the minimum size, simultaneously giving the dual minimum distance and its complete minimum-weight spectrum. This is useful for availability analysis and for distinguishing this family from optimal LRCs with additional minimum recovery alternatives.

Self-review: passed. Independent audit: not yet performed.
