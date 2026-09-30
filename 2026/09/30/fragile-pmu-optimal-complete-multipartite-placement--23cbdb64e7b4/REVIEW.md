# Review

## Correctness assessment
PASS. The survivor-set characterization is exact: survivors in at least two parts observe every vertex during the domination step, while survivors confined to one part can complete observation exactly when at most one vertex of that part remains unobserved. The failure events used in the probability sum are disjoint. Pascal's identity gives the stated marginal penalty, and coefficientwise monotonicity gives discrete convexity. The greedy allocation follows from merging nondecreasing marginal chains. Exact-rational exhaustive checks independently reproduce the structural criterion, reliability values, marginal monotonicity, and optimizer on all complete multipartite types through order eight.

## Originality assessment
PASS, best-of-knowledge. The closest literature introduces fragile power domination, gives general probability bounds, exact star calculations, and a complete-multipartite expected-value polynomial; a later preprint studies further expected-value-polynomial structure. The reviewed claim is narrower and different: an exact full-observation reliability formula for arbitrary fixed placements on every complete multipartite graph, plus an exact greedy optimizer for every fixed budget and failure probability. Searches for the claim, its synonyms, and stronger placement-optimization coverage did not identify a source containing this result.

## Value assessment
PASS. The theorem converts a potentially exponential comparison over PMU placements and failure patterns into a closed reliability formula and a simple exact marginal-cost allocation rule. The zero-cost and first positive-cost tiers also give immediate closed forms for a nontrivial range of sensor budgets.

## Closest literature
The closest source is *Power domination with random sensor failure* (arXiv:2312.12259; later *Australasian Journal of Combinatorics* 94(1) (2026), 1--24), which supplies the fragile-power-domination framework and complete-multipartite expected-value calculations. *On Fragile Power Domination* (arXiv:2507.14620) is a later related study. Neither source located in the review supplied the complete-multipartite full-observation formula and fixed-budget greedy placement theorem stated here.

## Scientific limitations
The result assumes identical independent sensor failures and simple complete multipartite graphs, with at most one sensor per vertex. It does not address heterogeneous reliability, correlated failures, other propagation rules, or graph classes beyond complete multipartite graphs. Literature coverage is best-of-knowledge and may miss inaccessible or differently phrased work.

Same-model review: passed. Independent audit: not yet performed.


The revised package received a same-model three-axis review on 2026-09-30 UTC. See AUDIT.json for actual comparisons, replay scope and residual risks. No independent audit or external certification is asserted.
