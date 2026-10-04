# Review

## Correctness

PASS. After the exterior of one triangle is exposed, only the number of distinct ambient components meeting its three vertices matters. There are exactly three cases. For two ambient components, two of the triangle edges are parallel opportunities to merge the components; for three ambient components, the component-count reduction is the rank of a Bernoulli subgraph of a triangle. These calculations give the two coefficients in the exact covariance formula.

The cycle-rank formula is obtained by adding the exactly known covariance between the triangle indicator and the three participating edge indicators. The subcritical limits follow because two fixed triangle vertices connect through the exterior with probability \(O(n^{-1})\) when \(p=c/n\) and \(c<1\).

## Originality

PASS, with a residual older-random-graph risk. Elçi--Weigel--Fytas was inspected in full at its percolation edge classification and Russo--Margulis derivation. It gives exact component/edge and bridge relations, but the inspected text does not state a triangle-count covariance or a three-point connectivity partition formula.

Janson's classical subgraph-count paper is a plausible broader source for triangle fluctuations. Only publisher-level material was available during inspection, so it is not used to certify whole-document noncoverage. Its accessible description concerns asymptotic subgraph-count distributions rather than exact covariance with total components; this unresolved comparison is retained as a residual risk.

Targeted semantic-database and web searches for component–triangle covariance, cycle-rank–triangle covariance, and three-point percolation formulations did not locate the accepted identity.

## Value

PASS. Component count and cycle rank are the zeroth and first Betti numbers of a graph, while triangle count is the basic local cycle statistic. The theorem gives an exact finite relation between a local motif and global topology, with the sign split explained by a concrete three-point connectivity state.

The subcritical limits make the interpretation quantitative: one open triangle contributes asymptotically twice its Poisson-scale intensity in lost components but one unit of cycle rank. This is a natural bridge between percolation connectivity and motif-count fluctuation theory.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK graph_parameter_checks=18 percolation_states=3888 connectivity_states=4110 triangle_instances=60`.
