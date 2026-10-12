# Self-review

## Correctness
**PASS.** After site-swap normalization \(b\le c\), Simpson similarity is \(1/(1+b/a)\) and Jaccard similarity is \(1/(1+(b+c)/a)\). Since the reciprocal map is strictly decreasing, strict rank reversal is exactly the opposite ordering of the minimum-unique ratio \(b/a\) and total-unique ratio \((b+c)/a\). Exact enumeration gives no reversal through gamma richness \(3\), exactly three at gamma richness \(4\), and the displayed infinite family follows from the positive difference \((r^2-2)/((r+1)(r+2))\).

Risk: the finite classification is by pairwise Venn signatures and does not classify the joint geometry of four simultaneously labeled communities.

## Originality
**PASS.** The primary literature explicitly supplies the \(a,b,c\) formulas and explains the broad-sense versus turnover distinction, including Simpson's invariance to unique species added only to the richer site. Those facts motivate the result but do not state the exact all-pairs reversal criterion, the gamma-richness-four minimum, the complete three-pair first layer, or the infinite family. Searches by aliases, exact signatures, rank-reversal language, and minimum-species language found no covering statement.

Risk: the formulas and ternary-plot literature make the result a natural derivation, and an unindexed exercise or software regression example could contain one or more witnesses. No source located was found to state the sharp boundary theorem.

## Value
**PASS.** Presence–absence beta-diversity measures are widely used, and the cited literature emphasizes that choosing a richness-sensitive versus richness-insensitive measure can materially change ecological conclusions. The criterion isolates the exact mechanism of a ranking change without simulation, and the four-species boundary supplies the smallest possible benchmark. The infinite family shows that the effect is structural, not a tiny finite anomaly.

Self-review: passed. Independent audit: not yet performed.
