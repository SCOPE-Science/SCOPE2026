# Scientific review: exact crown-graph locating-domination enumeration

## Correctness
PASS. The two-sided indexed-neighborhood identities reduce locating-domination to at most one entirely omitted matched pair, together with explicit small-side exceptions. Counting all such profiles and subtracting the two disjoint invalid families gives the claimed all-size polynomial for every \(n\ge4\), with separate exact treatment of \(n=2,3\). The minimum coefficient follows by coefficient extraction and a positive-count inequality for \(n\ge5\). The reliability formula is the Bernoulli evaluation of that polynomial, and its limiting profile follows from the binomial-to-Poisson limit. Exhaustive tests of every vertex subset for \(2\le n\le9\) and exact coefficient checks to \(n=200\) independently support the proof without replacing it.

## Originality
PASS subject to stated priority uncertainty. The accessible full primary manuscript by Hernando–Mora–Pelayo (arXiv:1711.01951v1) treats locating-domination numbers in bipartite graphs and complements, rather than a crown-graph cardinality distribution. Bousquet–Deschamps–Lehtilä–Parreau investigate oriented variants, while Chakraborty–Foucaud–Henning–Laihonen address domination/locating-domination partitions. The closest published crown-graph result located in the mathematical-record search counts *edge-metric bases*, which distinguish edges by distances rather than distinguishing unselected vertices by their selected open-neighborhoods. Likewise, restrained domination of crown graphs lacks the required signature uniqueness. Neither stronger implication nor equivalence covering the proposed polynomial was established in the inspected sources. Publication priority remains uncertain because unindexed or uninspected sources may contain the same enumeration.

## Mathematical value
PASS. A natural two-parameter deployment graph is analyzed at the level of all feasible sensor configurations, not only the minimum number of sensors. The exact classification identifies every optimum and every cardinality coefficient, and yields an independent-failure reliability law with a nontrivial Poisson transition on the natural scale \(n^{-1/2}\). These outputs are useful even if an optimal-size bound alone were already known.

## Limitations and scientific risks
The proof is for ordinary locating domination, not identifying codes, open locating-total domination or edge-metric resolution. The asymptotic reliability theorem assumes independent equal-probability vertex selection. An earlier unindexed equivalent characterization or polynomial could supersede novelty. The verification program checks finite instances only.

Self-review: passed. Independent audit: not yet performed.
