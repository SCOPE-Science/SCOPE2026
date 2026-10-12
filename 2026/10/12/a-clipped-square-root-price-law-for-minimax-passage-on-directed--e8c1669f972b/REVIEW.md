# Scientific review

## Correctness — PASS

The reduction to maximum over paths missing one edge follows directly from the unique oriented routes. A global weighted Cauchy--Schwarz bound applies to every positive budget-feasible rate vector. Its strictly concave simplex dual has a unique KKT maximizer, with threshold equation and positive complementary weights. The explicit normalized rates attain that bound; equality in Cauchy--Schwarz proves uniqueness even at tied prices and active-set transitions. The exact example and finite independent Markov-generator tests corroborate, but do not substitute for, the proof.

## Originality — PASS, with residual risk

Closest inspected sources include Yu--Karaman--Rus (arXiv:1309.6041, cyclic surveillance), Agharkar--Patel--Bullo (2014, average first passage), Carron--Patel--Bullo (2016, doubly weighted hitting formulas), and Breen--Kirkland (2017, maximum discrete-time first passage under stationarity/graph constraints). The first uses a distinct Poisson observation objective, the middle works optimize stationary-weighted mean outcomes rather than maximum pairwise delay under arc-rate price budget, and the last gives a stationary-distribution comparison, not a rate-price minimax optimizer. No inspected primary statement dominates the clipped allocation. A specialized unpublished or unindexed precedent remains a risk; database search alone is not novelty proof.

## Value — PASS

The exact solution exhibits a structural regime transition for a natural reliability/latency allocation problem: low-price arcs share one rate, high-price arcs obey an inverse-square-root cost law, and for three nodes the transition is controlled by the triangle inequality on edge prices. It improves the explicit \((1,3,100)\) example from maximum expected latency \(208\) under uniform rates to \(144\). Positive-rate uniqueness and \(O(n\log n)\) construction eliminate general numerical minimax optimization for this entire directed-ring class. This is an exact graph-family classification, not a mere restatement of generic KKT conditions.

## Scope and uncertainty

Only continuous-time one-way cycles, independent exponential waiting times, strictly positive linear rate prices, fixed total rate expenditure, and ordered-pair first passage are covered. Stationary distributions, reverse edges, return times, and nonlinear resource functions are outside the theorem. Primary-source date evidence is the 2013-09-24 UTC arXiv submission; a 2017 related paper is compared only for overlap. No independent scientific audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
