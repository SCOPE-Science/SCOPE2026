# Independent mathematical audit

## correctness

PASS

In the stated block-only action, comparing compositions makes g equivariant and each f constant as a function of the block along a sigma-cycle. Idempotence means g fixes its image pointwise and f_{g(i)} f_i=f_i. Thus retained cycles have local retractions, counted by choosing r fixed image points and r choices per remaining point. An omitted cycle maps equivariantly onto a retained cycle exactly when the length divides its own; each target has as many phases as its length, independently of the local map, which has r^n choices into the retained image. Omitted cycles contribute no new image points. The resulting factorization gives both the rank polynomial and its support without cancellation. Divisibility descent and the compulsory retention of one cycle per minimal length prove the minimum; equality forces exactly one such cycle and local rank one, giving the separate phase-product coefficient. The transposition example and total 15 agree with direct enumeration; the unrestricted total 189 also follows by counting 54, 108, 27 for respectively one, two, three fixed blocks. A full three-cycle permits only the 2 rank-one and 1 rank-two local retractions. Separate direct pointwise checks tested 3,864,241 candidate maps over five profiles including equal cycle lengths (2,2), incomparable minima (2,3), and n=3. For n=2, (2,2) gives 8z^2+20z^4+4z^6+z^8; (2,3) gives 4z^5+2z^7+2z^8+z^10. Replay at /workspace/branches/4b5c8355-0ddb-4f56-9262-47612cd1d65f/direct_rank_check.py. The supplied check.py was inspected, not executed; these bounded checks corroborate, not prove, the universal result.

## originality

PASS

The supported distinction is the point-image-weighted census for n>=2 with both uniform-block preservation and a fixed coordinate-preserving block symmetry, not the local idempotence or divisibility rules. The closest enumerator coincides at n=1 only.

## value

PASS

Rank is the size of a block-compatible equivariant retract, not merely an auxiliary count. The formula answers both feasibility and multiplicity for each size; it pinpoints the mandatory cycle types and exact multiplicities of smallest retracts even when minimal lengths are incomparable. This is useful for finite transformation monoids with prescribed symmetry and is more informative than an unrestricted count or a characterization of allowed block maps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
