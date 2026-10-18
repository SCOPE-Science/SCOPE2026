# Scientific review

## Correctness

**PASS.** The merger identity follows directly from squared abundances. Holding merged mass fixed, the product of the two abundances is maximized only at equality; holding merged abundances fixed, Cauchy–Schwarz uniquely minimizes the remaining sum of squares at an equal remainder. Their strict effects on the reciprocal-concentration loss reduce the global optimization to one scalar variable. Its rational derivative factors exactly into a positive denominator and a strictly monotone quartic, giving a unique global maximum. The extremal proportions are strictly positive. The asymptotic coefficient follows by bounding and passing to the limit in the quartic equation. All boundary and normalization arguments are included in the proof; standalone executable finite checks have passed.

## Originality

**PASS, subject to the identified bibliographic risk.** Hill (1973, DOI `10.2307/1934352`) introduces the effective-diversity index and an all-pairs doubling identity, not an arbitrary single-pair global optimization. Bozzuto and Blanckenhorn (DOI `10.1080/21513732.2016.1260638`) study taxonomic resolution with structured binning and mortality but do not state the unique extremizer and its all-dimension asymptotic. Ricotta and Feoli (DOI `10.1016/j.ecolind.2024.111971`) analyze interpretation of Hill numbers, not the merger loss maximum. The classic Herfindahl identity for the raw concentration increase is acknowledged; it does not itself establish the optimized inverse-concentration loss. Searches for the ecological and economic alias formulations and comparisons with nearby finite-Hill and niche-overlap results have not identified a statement that implies the theorem. A relevant older optimization under a different alias remains possible; an independent bibliographic audit is outstanding.

## Value

**PASS.** Taxonomic binning is a real source of biodiversity measurement distortion. The theorem provides the exact worst-case price, the unique abundance configuration that creates it, and a sharp linear growth law for arbitrary initial species richness. It contrasts that potentially unbounded absolute loss with a universal one-half relative bound and an at-most-two loss in a perfectly even assemblage. This differentiates the result from merely restating the increase \(2ab\) in raw Simpson concentration or evaluating a few prescribed communities. The model does not account for estimated abundances, multiple merges or biological causal effects.

Self-review: passed. Independent audit: not yet performed.
