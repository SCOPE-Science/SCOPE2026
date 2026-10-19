# Scientific review: minimum maximal matchings of the Nauru graph

## Correctness — PASS

The minimum size is at least eight: the 36 graph edges must be dominated by matching edges, each of which dominates at most five edges in a cubic graph. Two independent exhaustive constructions establish that there are exactly 90 feasible eight-edge maximal matchings. One enumerates all independent sets of eight omitted vertices and their complementary perfect matchings; the other branches directly on matched or unmatched vertices. The independently generated lists agree entry by entry. All 4,005 unordered pairs of states are compared under the exactly defined replacement metric, giving the stated exchange graphs. Independent certificate checking reconstructs the graph, maximality, transitions, components, shortest paths and induced dihedral symmetry actions. The methods are finite exhaustive proofs, not extrapolations from a sample.

## Originality — PASS (provisional literature judgment)

Brazil, da Fonseca, de Figueiredo and Sasaki (arXiv:1204.2727, 2012) already display an eight-edge maximal matching of the Nauru graph. That scalar value is not asserted as novel. Yannakakis and Gavril (1980) establish the edge-domination framework. Solomon and Solomon (2021) study matching reconfiguration with a permitted one-edge drop in cardinality, unlike the no-slack minimum-maximal constraint imposed here. Edge-dominating-set token sliding without the matching requirement is likewise a different state space. Direct inspections, targeted mathematical searches and comparisons with related finite graph findings did not identify prior coverage of the 90-state enumeration, the three 30-vertex components, or the sharp four-edge threshold. Remaining uncertainty includes unindexed tables, alternate terminology and supplementary computations; absence of a search hit is not proof of publication priority.

## Value — PASS

A minimum maximal matching is an optimal independent edge-dominating set. This is a natural local-coverage optimization problem in its own right, and a small change budget can determine whether one optimum is maintainably transformed to another. For the Nauru graph, the elementary minimum cardinality had been known but not the geometry of **all** its optimal solutions. Here every optimum is frozen under one-edge substitutions, two-edge moves give three mutually isolated but internally connected regions, and precisely four simultaneous substitutions are needed for universal reachability. This sharp resource-versus-mobility boundary and the symmetry explanation are the motivating mathematical facts, not an arbitrary isolated count. No general theorem outside this graph is claimed or needed for the finite classification's value.

## Limits and closest literature

This is an exact finite classification, not a general result for cubic graphs. It assumes two endpoint matchings both remain minimum maximal after each permitted simultaneous exchange; states below the optimum size or nonmaximal states are disallowed. The 2012 Nauru matching example and the later broader reconfiguration with cardinality slack are intentionally not recast as new work. Broader databases and inaccessible or unindexed supplementary materials remain a residual priority risk.

Self-review: passed. Independent audit: not yet performed.
