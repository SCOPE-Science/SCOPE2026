# Self-review

## Correctness
**PASS.** The exact individual-based rarefaction formula is a sum of hypergeometric absence probabilities. For comparable sorted triples, the absence numerator is discrete convex and majorization prevents reversals. For incomparable triples, the signed abundance-frequency distribution has ordered support \(C<c\le b<B\le A<a\); its twice-cumulative transform has a single negative-to-positive sign transition. Two summations by parts represent the difference of absence numerators as that transform weighted by \(\binom{N-j-2}{m-2}\). The kernel's cross-product inequality shows that as sample depth grows, its weights shift toward the earlier negative block; the sign can change only once. A complete standalone rational verifier passed every triple and depth up to census \(35\), confirmed \(176194\) summation identities and \(486980\) kernel inequalities, and rechecked the exact sharp example. The proof itself covers arbitrarily large finite censuses.

Risk: the theorem does not hold automatically for different numbers of species, census sizes, sampling conventions, or arbitrary continuous interpolants.

## Originality
**PASS.** The primary full texts of Lande–DeVries–Walla and Thompson–Withers establish generic ecological crossing mechanisms; the full Chao–Jost article discusses the relationship between size- and coverage-standardized crossing counts. None of these proves the strict integer-depth single-crossing ceiling at equal census for exactly three species or the two-depth deterministic certificate. Targeted searches for aliases (species accumulation, rarefaction, hypergeometric expectation, majorization, single crossing, total positivity, three taxa) and semantic database searches found no equivalent theorem. Existing finite examples establish existence and sharpness, not universal uniqueness of a sign change.

Risk: an unindexed probability-theoretic or total-positivity theorem might imply the result after nonobvious translation; exact noncoverage cannot be proved by searches.

## Value
**PASS.** Rarefaction exists to compare ecological richness at standardized sampling effort, but prior work demonstrates that changing effort can change rankings. Three species are the smallest richness supporting incomparable abundance profiles, making this a natural complete class rather than an arbitrary parameter slice. The result bounds the complexity of the entire all-depth comparison, and the pair of explicit Simpson/singleton endpoint statistics gives a practical certificate: when both depth comparisons agree strictly, no intermediate depth can favor the opposite community. The one-switch example proves the result is sharp and not just majorization concordance.

Self-review: passed. Independent audit: not yet performed.
