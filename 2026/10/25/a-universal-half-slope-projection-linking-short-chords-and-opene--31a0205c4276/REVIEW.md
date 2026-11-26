# Independent mathematical audit

## correctness

PASS

A fixed short chord costs 1/(2n-1); two disjoint fixed chords cost 1/[(2n-1)(2n-3)], so short-chord factorial moments give the stated variance. For each different-chord LR pair the opener needs a partner strictly to its right beyond the closer, and the closer needs a partner strictly to its left before the opener. The product of these two counts gives the position formula. Conditioning on B_i leaves a uniform matching when its endpoints are removed; the only added different-chord adjacency is the seam, whose expectation is the stated q_i and vanishes at boundary positions. At n=2 the reduced matching has A=0. An independent mixed-moment derivation counts all LR pairs: the forced LR is removed, no neighboring LR is destroyed, and the new seam is subtracted. Summing the seam probabilities over i gives E L_(n-1), so E[SL]=1+[(2n-2)/(2n-1)]E L_(n-1) and Cov(S,L)=(n-1)/(2n-1). For the LR marginal, insertion immediately after the new first opener gains one; inserting after an old opener gains one unless it replaces an old LR. There are n-k gains in all. The first two conditional moments yield the given variance; affine projection then gives the slope, residual and correlation with strictly positive variance for n≥2. The independent rational recheck propagated the full LR distribution and checked the full-LR seam mixed moment through n=44 (independent_recheck.py); the original enumeration script was read, not executed. The result is not an identity for the nonlinear conditional mean or for cyclic matching.

## originality

PASS

The distinct claim is the mixed covariance and position-resolved seam, and the half-slope and signs they yield. Neither short-chord nor LR marginal laws are new. The strongest same-formula hit concerns a demonstrably different second statistic.

## value

PASS

The count of adjacent openers and closers is a natural local matching statistic. Removing its same-chord contribution reverses a nonzero covariance exactly, and the invariant affine slope and explicit seam effect make the result a useful benchmark for joint matching laws. The value is in the mixed identity and local correction, not in rederiving the known two marginal laws or in claiming independence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
