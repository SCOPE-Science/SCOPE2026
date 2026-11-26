# Independent mathematical audit

## correctness

PASS

For every real cut, the two inverse branches above a point are antipodal and equally weighted, with exactly one branch in the half-open semicircle. Iterating independence of the current bit from the next state yields all cylinder probabilities. For a dyadic cut 2^r a=k, the low r−1 bits distinguish the two thresholds in the high-bit cases: the indicator is 1 exactly when the high bit disagrees with the comparison s_next≥k. This gives the backward maps in RESULT.md lines 23–38. Below k, F_0 repeatedly halves with floor; at or above k, the distance to M−1 repeatedly halves with floor. Both regions are invariant, and m=r−1 steps send them to 0 and M−1, respectively; for k=0 only the upper region exists. F_1 sends the two endpoints to M/2 and M/2−1 (for k>0), in the same region exactly when k≠M/2. Hence F_0^m F_1 F_0^m is constant outside the exception, including k=0. A later reset fixes the state there, and the intervening backward maps give the earlier state and bit. Independent aligned length-L blocks give failure probability (1−2^−L)^j for the first j blocks; reset occurrences downstream of every coordinate hold simultaneously almost surely. This reconstructs a measurable inverse and shift commutation then gives conjugacy. At k=M/2 the code is successive-bit XOR; the two choices of initial bit give complementary preimages, and no others. Typical output is not eventually constant, so binary endpoints cannot supply additional preimages. Reflection preserves Lebesgue measure, so an injective full-measure set cannot pick one of each typical reflected pair.

## originality

PASS

Fair output via balanced inverse branches, reset words in general, and Walsh examples of fair output are not the distinct contribution. The supported contribution is the all-dyadic-cut classification for this specified half-circle sensor, with an explicit word and inverse-delay bound outside the quarter cut, and the exact exceptional fibers. Neither the material inspected on this same doubling map nor general coding theory supplies this combination. This is a bounded comparison rather than a priority certificate.

## value

PASS

The mandated natural observation family has identical complete output laws, yet the factor map loses one bit at exactly one dyadic location and is almost-surely recoverable elsewhere. The classification separates a distributional diagnostic from actual state information, and a single explicit precision-dependent reset word makes the contrast constructive with a quantitative delay bound. This is more than a demonstration of fairness or a generic reset-word criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
