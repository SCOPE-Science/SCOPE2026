# Scientific review: excitation recurrence on cocktail-party graphs

## Correctness

PASS. The local rule differs from global three-color rotation only when precisely one vertex is excited and its unique matched partner is resting. The proof exhausts every possibility for the other vertices: no resting, no refractory, at least two resting and one refractory, or exactly one resting. The four explicit chains show extinction or entry into a rotating three-cycle for every graph order at least six. Periodic colorings are characterized by nonempty color classes and a single-vertex predecessor-color exclusion. Three pairwise disjoint excluded families each contain \(n(2^{n-2}-1)\) colorings. The four-vertex exception is separately checked over its entire finite state space. The independently implemented neighbor-enumerating functional-graph checker found exactly the predicted cycles for all even orders from two through twelve.

## Originality

PASS (qualified). Gravner–Lyu–Sivakoff (arXiv:1610.07320v1, 2016-10-24), in the material examined, characterize oscillation and synchronization on arbitrary connected graphs by cycle integrals, but do not give this complete-graph-minus-perfect-matching exact labelled primitive-orbit census. Doba (2018) studies general maximum cycle density and likewise does not provide this special-family count or its four-to-three-period transition. Epperlein–Siegmund (2013) establish existence results for phase-locked trajectories in generalized systems, not this count. Accessible related calculations for complete bipartite, crown, friendship and split graphs concern different edge sets and do not imply this formula. Searches under Greenberg–Hastings, excitable cellular automata, perfect matching deletion, cocktail-party graph, and primitive periodic orbit terminology found no equivalent statement. Residual priority risk remains for unindexed or inaccessible sources.

## Mathematical value

PASS. The graph family is canonical: the unique graph on \(2m\) vertices with a specified perfect matching as exactly its missing edges. Its recurrence differs sharply from the four-cycle boundary: enlarging by one matched pair eliminates four-period oscillation but yields exponentially many three-cycle attractors. The exact count and the exponentially small fraction of nonperiodic initial configurations distinguish orbit abundance from convergence behavior in a standard excitable network model. This is a complete all-size classification, not an arbitrary isolated parameter computation.

## Limitations and closest literature

The result does not claim new general graph synchronization theory, sharp transient bounds, a basin census, stochastic dynamics or higher-state Greenberg–Hastings behavior. The inspected general-graph theorems of Gravner–Lyu–Sivakoff (2016) and Doba (2018) are antecedents, not independently reproduced or challenged. Historical or terminology-related overlap remains possible.

Self-review: passed. Independent audit: not yet performed.
