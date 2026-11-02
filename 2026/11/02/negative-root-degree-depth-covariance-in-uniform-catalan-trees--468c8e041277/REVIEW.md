# Self-review

## Correctness: PASS

The object is a uniform rooted ordered tree counted by edges; root outdegree is the number of primitive Dyck excursions and the total vertex depth is the sum of ascent starting heights plus the edge count. Differentiating the explicit primitive decomposition simultaneously by area and by root-child count yields three exact integer moment sums. Direct substitution produces the covariance for all \(n\ge1\). A positive difference of successive ratios, starting at equality for \(n=1\), certifies strict negativity for all \(n\ge2\). The central-binomial expansion yields the stated asymptotic, with a remainder of order \(n^{-1/2}\). The standalone Python checker passes 760 exact assertions, including all 16,796 paths for \(n=10\). Scientific risk: no computational test independently proves an identity beyond its tested range, which is why the coefficient and ratio arguments are included.

## Originality: PASS (qualified)

The most relevant accessible primary Dyck-area paper, Blanco–Petersen, arXiv:1206.0803, treats the noncrossing-partition rank, not root excursion count. Its definition in the introduction distinguishes these statistics. The relevant section of Dershowitz–Rinderknecht's 2015 Catalan-tree work treats root-degree enumeration and expected path length separately without stating the mixed covariance. General prior enumerators and the classic Catalan identities are openly credited. The actual external comparison included mixed area/returns aliases and other random-tree models; the closest root-degree/path-length identity is for *random recursive trees*, not uniform plane trees. No matching exact formula or stronger dominating theorem was identified among inspected sources. Scientific risk: a broader historical bivariate generating function, including earlier general tree-pattern work that was not fully accessible, could implicitly cover the formula. Independent priority review has not occurred.

## Mathematical value: PASS

A root's branching is a natural local shape statistic, while cumulative distance is a natural aggregate cost for searches in a hierarchical tree. The strict all-size negative covariance, explicit finite correction, and limiting order \(-2n\) quantify their interaction. This is more informative than combining separate marginal expectations or a small-size census, and the all-size sign needs an actual inequality rather than relying on an asymptotic. The result does not claim stochastic ordering, causality, or an unrelated extension.

Self-review: passed. Independent audit: not yet performed.
