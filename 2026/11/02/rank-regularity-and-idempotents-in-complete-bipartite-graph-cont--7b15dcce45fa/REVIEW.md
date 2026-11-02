# Mathematical review

## Correctness — PASS

The theorem is about the entire monoid of partial functions whose inverse images of each graph simplex are simplices or empty, for all complete bipartite graphs with two non-singleton parts. The proof separates images contained in one independent part from mixed images and proves necessity and sufficiency for both descriptions. Inclusion-exclusion counts pairs of partial injections with jointly surjective image. A continuous-section criterion then characterizes regularity, and fixed-point restrictions classify idempotents. Every stated count follows by a disjoint combinatorial sum with no asymptotic approximation. The independently programmed verifier directly tested the defining continuity, regularity, and idempotent conditions against all rank coefficients for four non-star graphs. A finite test is not a substitute for the general proof.

## Originality — PASS, with historical-priority limitations

The closest fully inspected primary article is Margolis–Rhodes (2021), *Degree 2 transformation semigroups as continuous maps on graphs: Foundations and structure*, DOI 10.1142/S0218196721400051. It gives the basic continuity criterion and enumerates strictly continuous maps on balanced complete bipartite graphs in Example 2.11. Its rank formula for the strict singular subset is recovered as a specialized check. The new result instead enumerates the **full** continuous monoid, separates regular from nonregular elements, and counts all idempotents for arbitrary part sizes, including unequal ones; these statements do not follow merely from the earlier strict-submonoid table. The later Margolis–Rhodes preprint arXiv:2609.39370 (first public 2026-09-30) motivates full-monoid enumerations and explicitly advertises path and cycle families, but its complete text was not accessible. That is a concrete, unresolved priority risk; the abstract alone does not establish noncoverage. Targeted mathematical searches did not reveal an equivalent full classification, but negative search results are not a uniqueness certificate. The star-graph boundary is outside the new hypothesis \(m,n\ge2\) and does not determine the two-sided complete-bipartite formulas.

## Mathematical value — PASS

Full graph-continuous monoids of a natural infinite graph family have a substantially richer rank and regularity structure than their strict submonoids. The exact image-type/section criterion identifies every nonregular transformation and yields every coefficient of the regularity and idempotent spectra. The rank-two formula \(2mn(\binom m2+\binom n2)\) gives a direct natural obstruction; the full rank polynomial can be used in comparisons of regular Green strata and in construction of finite-semigroup examples. No claim is made about all graphs, full Green structures, or Krohn–Rhodes complexity.

## Limits and closest literature

Relevant published prior art: Margolis–Rhodes (2021), Section 2 and Example 2.11, which is about the *strict* monoid. Motivating recent literature: Margolis–Rhodes, arXiv:2609.39370 (2026-09-30), which studies the full monoid; full text was inaccessible in this review. The standalone verification covers only graph orders at most six, whereas the symbolic proof covers arbitrary positive part sizes with both at least two. Originality is supported by statement-level comparisons of strict versus full monoids and star versus non-star graphs, not asserted as absolute historical priority. The review is not independent.

Self-review: passed. Independent audit: not yet performed.
