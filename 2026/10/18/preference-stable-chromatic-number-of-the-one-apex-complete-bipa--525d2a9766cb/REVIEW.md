# Scientific review

## Correctness

PASS. An explicit greedy coloring uses \(b+2\) colors for every preference profile and orders all envy arcs backward. For \(b\ge2\), a single strict preference profile for each \((a,b)\) makes every proper \((b+1)\)-coloring unstable: removing the universal vertex's color permutes the remaining favorite colors bijectively within each of the two other parts, and the alternating color maps must contain a blocking cycle. The \(b=1\) boundary follows from the triangle lower bound. The packaged finite checks exercise both constructions, without substituting enumeration for the infinite proof.

## Originality

PASS with a declared access risk. The initiating work determines complete bipartite graphs and gives a general reachability upper bound, neither of which supplies the strict one-apex lower bound. A publicly available \(K_{2,3,3}\) result covers one distinct tripartite graph, not the family with a singleton part. A known complete-graph-minus-matching classification overlaps at a small boundary instance but does not dominate the two-parameter formula. Exact, equivalent, and stronger-statement searches found no covering theorem. The initiating manuscript's complete PDF was not accessible for a full-text inspection, leaving a specific residual risk of an overlooked general lemma.

## Value

PASS. The result determines an infinite natural next family after the recently settled complete-bipartite case. It proves that one universal apex vertex always raises this new graph-coloring invariant by **exactly one**, and supplies a reusable robust-favorites obstruction rather than an unmotivated finite calculation. It does not assert a general join theorem.

## Closest literature and limitations

Primary motivation: Koana, Oh, and Yoneda, *Graph Coloring with Color Preferences*, arXiv:2609.00569, 1 September 2026. The published \(K_{2,3,3}\) computation is a nearby but noncovering finite result. The proof is restricted to one universal vertex, and the motivating primary manuscript could not be fully inspected through the available access route; unindexed prior work remains a risk.

Self-review: passed. Independent audit: not yet performed.
